# Refer to the code of priconne games in HoshinoBot by @Ice-Cirno
# Slightly modified by GWYOG
# Slightly modified again by assassingyk
# Under GPL-3.0 License

import os
import sqlite3
import asyncio
import random
import hoshino

from hoshino import Service
from .chara import *
from .config import *
from hoshino.typing import MessageSegment, CQEvent
from hoshino.util import DailyNumberLimiter


class Dao:
    def __init__(self, db_path):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self._create_table()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self.connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS win_record "
                "(gid INT NOT NULL, uid INT NOT NULL, count INT NOT NULL, PRIMARY KEY(gid, uid))"
            )

    def get_win_count(self, gid, uid):
        with self.connect() as conn:
            r = conn.execute(
                "SELECT count FROM win_record WHERE gid=? AND uid=?", (gid, uid)
            ).fetchone()
            return r[0] if r else 0

    def record_winning(self, gid, uid):
        n = self.get_win_count(gid, uid)
        n += 1
        with self.connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO win_record (gid, uid, count) VALUES (?, ?, ?)",
                (gid, uid, n),
            )
        return n

    def get_ranking(self, gid):
        with self.connect() as conn:
            r = conn.execute(
                "SELECT uid, count FROM win_record WHERE gid=? ORDER BY count DESC LIMIT 10",
                (gid,),
            ).fetchall()
            return r


class GameMaster:
    def __init__(self, db_path):
        self.db_path = db_path
        self.playing = {}

    def is_playing(self, gid):
        return gid in self.playing

    def start_game(self, gid):
        return Game(gid, self)

    def exit_game(self, gid):
        del self.playing[gid]

    def get_game(self, gid):
        return self.playing[gid] if gid in self.playing else None

    @property
    def db(self):
        return Dao(self.db_path)


class Game:
    def __init__(self, gid, game_master):
        self.gid = gid
        self.gm = game_master
        self.answer = 0
        self.winner = 0

    def __enter__(self):
        self.gm.playing[self.gid] = self
        return self

    def __exit__(self, type_, value, trace):
        if self.gid in self.gm.playing and self.gm.playing[self.gid] == self:
            del self.gm.playing[self.gid]

    def record(self):
        return self.gm.db.record_winning(self.gid, self.winner)


sv = Service('fgovoiceguess', bundle='娱乐', help_='''
[猜从者语音] 猜猜随机的战斗开始语音来自哪位从者
'''.strip())

ONE_TURN_TIME = 30
HOSHINO_RES_PATH = os.path.expanduser(hoshino.config.RES_DIR)
DIR_PATH = os.path.join(HOSHINO_RES_PATH, 'voice', 'voice_fgo')
DB_PATH = os.path.expanduser("~/.hoshino/fgo_voice_guess.db")

gm = GameMaster(DB_PATH)

lmt = DailyNumberLimiter(5)



@sv.on_fullmatch(("猜从者语音排行", "猜从者语音排行榜", "猜从者语音群排行"))
async def arkvoice_guess_group_ranking(bot, ev: CQEvent):
    ranking = gm.db.get_ranking(ev.group_id)
    msg = ["【猜从者语音小游戏排行榜】"]
    for i, item in enumerate(ranking):
        uid, count = item
        m = await bot.get_group_member_info(self_id=ev.self_id, group_id=ev.group_id, user_id=uid)
        name = m["card"] or m["nickname"] or str(uid)
        msg.append(f"第{i + 1}名: {name}, 猜对{count}次")
    await bot.send(ev, "\n".join(msg))


@sv.on_prefix('猜从者语音')
async def arknights_voice_guess(bot, ev: CQEvent):
    uid = ev.user_id
    if gm.is_playing(ev.group_id):
        await bot.finish(ev, "游戏仍在进行中…")
    if not lmt.check(uid):
        await bot.send(ev, '您今天已经玩了5次从者语音了，休息一下，明天再来吧！', at_sender=True)
        return
    lmt.increase(uid)
    with gm.start_game(ev.group_id) as game:

        file_list = os.listdir(DIR_PATH)
        chosen_file = random.choice(file_list)
        file_path = os.path.join(DIR_PATH, chosen_file)
        await bot.send(ev, f'猜猜这个战斗开始语音来自哪位从者? ({ONE_TURN_TIME}s后公布答案)')
        await bot.send(ev, MessageSegment.record(f'file:///{os.path.abspath(file_path)}'))
        chara_id = chosen_file[0:3]
        game.answer = int(chara_id)+1000
        await asyncio.sleep(ONE_TURN_TIME)
        # 结算
        if game.winner:
            return
        c = OtherChara(game.answer)
    ansimg=R.img(f'{ICON_RES}/{ICON_PREFIX}{game.answer + ID_OFFSET}_0.{ICON_EXT}').cqcode
    await bot.send(ev, f"正确答案是: {c.name} {ansimg}\n很遗憾，没有人答对~")


@sv.on_message()
async def on_voice_chara_name(bot, ev: CQEvent):
    game = gm.get_game(ev.group_id)
    if not game or game.winner:
        return
    aid = name2id(ev.message.extract_plain_text())
    c = OtherChara(aid)
    if aid != UNKNOWN and aid == game.answer:
        game.winner = ev.user_id
        n = game.record()
        gm.exit_game(ev.group_id)
        ansimg=R.img(f'{ICON_RES}/{ICON_PREFIX}{game.answer + ID_OFFSET}_0.{ICON_EXT}').cqcode
        msg = f"正确答案是: {c.name}{ansimg}\n{MessageSegment.at(ev.user_id)}猜对了，真厉害！TA已经猜对{n}次了~"
        await bot.send(ev, msg)
