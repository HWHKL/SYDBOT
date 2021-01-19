import os
import random
import hoshino

from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment


from hoshino import R, Service, priv


sv = Service('mawo', enable_on_default=True, visible=False)
xcw_folder = R.get('record/mawo/').path


def get_xcw():
    files = os.listdir(xcw_folder)
    filename = random.choice(files)
    rec = R.get('record/mawo/', filename)
    return rec


@sv.on_fullmatch('骂我', only_to_me=True)
async def xcw(bot, ev) -> MessageSegment:
    # conditions all ok, send a xcw.
    file = get_xcw()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

@sv.on_fullmatch(('操我', '草我', '艹我', '舔我'), only_to_me=True)
async def caowo(bot, ev) -> MessageSegment:
    target = ev.user_id
    await bot.send(ev, '真是奇怪的请求呢变态桑')
    await hoshino.get_bot().set_group_ban(self_id=ev.self_id, group_id=ev.group_id, user_id=target, duration=60)

@sv.on_fullmatch('您啪骂我')
async def ninpa(bot, ev) -> MessageSegment:
    file = R.get('record/ninpa/', 'ninpa.mp3')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")