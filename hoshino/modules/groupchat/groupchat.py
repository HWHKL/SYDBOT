import random
import os
import requests
import math

from nonebot import MessageSegment
import hoshino
from hoshino import R, Service, priv, util
from nonebot import NoticeSession


lmt = util.DailyNumberLimiter(5)

sv_help = '''
迫害龙王  ;当前龙王  ;龙王排行榜
群地位       |查看自己的群地位
戳一戳@群友  |让bot戳TA
@bot夸我     |bot送你礼物哦
来点鸡汤;今日一言
跟我学+内容  |让bot发这句话的语音
'''.strip()

sv = Service(
        name = '水群助手',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.ADMIN, #管理权限
        visible = True, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '娱乐', #属于哪一类
        help_ = sv_help #帮助文本
        )

@sv.on_fullmatch(["帮助水群助手"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=False)



@sv.on_fullmatch('迫害龙王')
async def who_is_longwang(bot, ev):
    gid = ev.group_id
    img_path = R.img('longwang/').path
    data = await bot.get_group_honor_info(group_id=gid, type='talkative')
    talkative = data['current_talkative']
    uid = talkative['user_id']
    files = os.listdir(img_path)
    filename = random.choice(files)
    img = R.img('longwang/', filename)
    at = MessageSegment.at(uid)
    msg = f'{at}\n{img.cqcode}'
    await bot.send(ev, msg)

@sv.on_fullmatch(('群地位',))
async def show_group_role(bot, event):
	if not priv.check_priv(event, priv.SUPERUSER):
		return
	me = await bot.get_login_info()
	gid = event.group_id
	uid = me['user_id']
	name = me['nickname']
	info = await bot.get_group_member_info(group_id=event.group_id, user_id=uid)
	role = info['role']
	await bot.send(event, f'{name}在此群的地位是{role}')

@sv.on_notice('notify')
async def new_longwang(session: NoticeSession):
    if session.event['sub_type'] == 'honor' and session.event['honor_type'] == 'talkative':
        uid = session.event['user_id']
        gid = session.event['group_id']
        at = MessageSegment.at(uid)
        bot = hoshino.get_bot()
        data = await bot.get_group_honor_info(group_id=gid, type='talkative')
        current_talkactive = data['current_talkative']
        day = current_talkactive['day_count']
        msg = f'新的龙王已经出现{at}，已蝉联{day}天'
        await session.send(msg)


@sv.on_fullmatch('当前龙王')
async def current_long(bot, event):
    gid = event.group_id
    data = await bot.get_group_honor_info(group_id=gid, type='talkative')
    current_talkactive = data['current_talkative']
    day = current_talkactive['day_count']
    uid = current_talkactive['user_id']
    at = MessageSegment.at(uid)
    msg = f'群龙王{at}，已蝉联{day}天'
    await bot.send(event, msg)


@sv.on_prefix('设置管理员')
async def set_admin(bot, event):
    gid = event.group_id
    u_priv = priv.get_user_priv(event)
    if u_priv >= sv.manage_priv:
        for m in event.message:
            if m.type == 'at' and m.data['qq'] != 'all':
                user = int(m.data['qq'])
                await bot.set_group_admin(group_id=gid, user_id=user, enable=True)
        await bot.send(event, '我好了')
    else:
        await bot.send(event, '才不听你的呢')


@sv.on_prefix('取消管理员')
async def unset_admin(bot, event):
    gid = event.group_id
    u_priv = priv.get_user_priv(event)
    if u_priv >= sv.manage_priv:
        for m in event.message:
            if m.type == 'at' and m.data['qq'] != 'all':
                user = int(m.data['qq'])
                await bot.set_group_admin(group_id=gid, user_id=user, enable=False)
        await bot.send(event, '我好了')
    else:
        await bot.send(event, '才不听你的呢')


@sv.on_prefix('设置群名')
async def set_group_name(bot, event):
    gid = event.group_id
    name = event.message.extract_plain_text().strip()
    if not name:
        await bot.finish(event, '群名都没有的你设置个锤子')
    u_priv = priv.get_user_priv(event)
    if u_priv >= sv.manage_priv:
        await bot.set_group_name(group_id=gid, group_name=name)
        await bot.send(event, '我好了')
    else:
        await bot.send(event, '才不听你的呢')


@sv.on_prefix('戳一戳')
async def send_poke(bot, event):
    msg = event.message
    for m in msg:
        if m.type == 'at' and m.data['qq'] != 'all':
            u = int(m.data['qq'])
            if u != event.self_id:
                poke_other = MessageSegment(type_='poke', data={'qq': u})
                await bot.send(event, poke_other)


@sv.on_prefix('申请头衔')
async def set_group_title(bot, ctx):
    msg = ctx.message.extract_plain_text().strip()
    group = ctx.group_id
    uid = ctx.user_id
    try:
        await bot.set_group_special_title(group_id=group, user_id=uid, special_title=msg, duration=-1)
        await bot.send(ctx, f'申请头衔{msg}成功')
    except Exception as ex:
        sv.logger.exception(ex)
        await bot.send(ctx, f'申请头衔{msg}失败了')




@sv.on_fullmatch('夸我', only_to_me=True)
async def kuangwo(bot, event):
    uid = event.user_id
    url = 'https://chp.shadiao.app/api.php'
    txt = requests.get(url=url, timeout=10).text
    msg = MessageSegment(type_='text', data={'text': txt})
    await bot.send(event, msg, at_sender=True)
    if not lmt.check(uid):
        return
    lmt.increase(uid)
    giftlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    gift = random.choice(giftlist)
    sendgift = MessageSegment(type_='gift', data={'qq': uid, 'id': gift})
    await bot.send(event, sendgift)


@sv.on_fullmatch('来点鸡汤', only_to_me=True)
async def jitang(bot, event):
    url = 'https://du.shadiao.app/api.php'
    txt = requests.get(url=url, timeout=10).text
    await bot.send(event, txt, at_sender=True)


@sv.on_fullmatch('今日一言', only_to_me=True)
async def yiyan(bot, event):
    juzi_type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    c = random.choice(juzi_type)
    url = f'https://international.v1.hitokoto.cn?c={c}&encode=text&charset=utf-8'
    try:
        txt = requests.get(url=url, timeout=10).text
        await bot.send(event, txt, at_sender=True)
    except Exception as ex:
        sv.logger.exception(ex)


@sv.on_prefix('跟我学', only_to_me=True)
async def txt_to_voice(bot, event):
    msg = event.message.extract_plain_text().strip()
    if not msg:
        return
    tts = MessageSegment(type_='tts', data={'text': msg})
    await bot.send(event, tts)


@sv.on_fullmatch('龙王排行榜')
async def longwangbang(bot, event):
    gid = event.group_id
    data = await bot.get_group_honor_info(group_id=gid, type='talkative')
    group = await bot.get_group_info(group_id=gid, no_cache=False)
    group_name = group['group_name']
    talkactive_list = data['talkative_list']
    msg = ''
    for index in range(len(talkactive_list)):
        rank = index + 1
        talkactive = talkactive_list[index]
        nickname = talkactive['nickname']
        desc = talkactive['description']
        msg += f'{rank}：{nickname}获得龙王{desc}\n'
    res = f'''群【{group_name}】龙王排行榜：
{msg}
'''.strip()
    await bot.send(event, res)



