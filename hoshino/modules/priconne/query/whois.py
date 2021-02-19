import random
import os
import requests
from nonebot import MessageSegment
import hoshino

from hoshino import R, Service, priv, util
from nonebot import NoticeSession

from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter

from .. import chara
from . import sv

lmt = FreqLimiter(5)


sv_help = '''
xx是谁 谁是xx |查询xx是谁的昵称
此功能任何人都能启用或禁用
（因为误触率太高了
'''.strip()

sv = Service(
        name = '昵称查询',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.NORMAL, #管理权限
        visible = True, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '通用', #属于哪一类
        help_ = sv_help #帮助文本
        )

@sv.on_fullmatch(["帮助昵称查询"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)



@sv.on_suffix('是谁')
@sv.on_prefix('谁是')
async def whois(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        return
    id_ = chara.name2id(name)
    confi = 100
    guess = False
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(name)
        guess = True
    c = chara.fromid(id_)

    if confi < 60:
        return

    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, f'兰德索尔花名册冷却中(剩余 {int(lmt.left_time(uid)) + 1}秒)')

    lmt.start_cd(uid, 120 if guess else 0)
    if guess:
        msg = f'兰德索尔似乎没有叫"{name}"的人.../n请使用[反馈]功能向维护组提交昵称！'
        await bot.send(ev, msg)
        msg = f'您有{confi}%的可能在找{guess_name} {c.icon.cqcode} {c.name}'
        await bot.send(ev, msg)
    else:
        msg = f'{c.icon.cqcode} {c.name}'
        await bot.send(ev, msg, at_sender=True)
