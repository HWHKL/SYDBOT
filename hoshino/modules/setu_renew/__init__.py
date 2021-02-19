import hoshino
import asyncio
from .base import *
from nonebot import scheduler
from .config import get_config, get_group_config, get_group_info, load_config, set_group_config,group_list_check, set_group_list

HELP_MSG = '''
来 [num] 张 [keyword] 涩/色/瑟图 : 来num张keyword的涩图(不指定数量与关键字发送一张随机涩图)
涩/色/瑟图 : 发送一张随机涩图
提取图片pid ： 获取指定id的p站图片，没有时发送链接
本日涩图排行榜 [page] : 获取[第page页]p站排行榜(需开启acggov模块)
看涩图 [n] 或 [start end] : 获取p站排行榜[第n名/从start名到end名]色图(需开启acggov模块)
'''
sv = hoshino.Service('setu', bundle='pcr娱乐', help_=HELP_MSG)

#设置limiter 
tlmt = hoshino.util.DailyNumberLimiter(get_config('base', 'daily_max'))
flmt = hoshino.util.FreqLimiter(get_config('base', 'freq_limit'))

def check_lmt(uid, num, gid):
    if uid in hoshino.config.SUPERUSERS:
        return 0, ''
    if group_list_check(gid) != 0:
        if group_list_check(gid) == 1:
            return 1, f'此功能启用了白名单模式,本群未在白名单中,请联系维护组解决'
        else:
            return 1, f'此功能已在本群禁用,可能因为人数超限或之前有滥用行为,请联系维护组解决'
    if not tlmt.check(uid):
        return 1, f"您今天已经冲过{get_config('base', 'daily_max')}次了,请明天再来~"
    if num > 1 and (get_config('base', 'daily_max') - tlmt.get_num(uid)) < num:
            return 1, f"您今天的剩余次数为{get_config('base', 'daily_max') - tlmt.get_num(uid)}次,已不足{num}次,请冲少点(恼)!"
    if not flmt.check(uid):
        return 1, f'您冲的太快了,{round(flmt.left_time(uid))}秒后再来吧~'
    #tlmt.increase(uid,num)
    flmt.start_cd(uid)
    return 0, ''

@sv.on_prefix('setu')
async def send_setu(bot, ev):
    uid = ev['user_id']
    gid = ev['group_id']
    is_su = hoshino.priv.check_priv(ev, hoshino.priv.SUPERUSER)
    args = ev.message.extract_plain_text().split()

    msg = ''
    if not is_su:
        msg = '需要超级用户权限'
    elif len(args) == 0:
        msg = '无效参数'
    elif args[0] == '设置' and len(args) >= 3: #setu set module on [group]
        if len(args) >= 4 and args[3].isdigit():
            gid = int(args[3])
        key = None
        value = False
        if args[1] == 'lolicon':
            key = 'lolicon'
        elif args[1] == 'lolicon_r18':
            key = 'lolicon_r18'
        elif args[1] == 'acggov':
            key = 'acggov'
        elif args[1] == '撤回':
            key = 'withdraw'
        if args[2] == '开' or args[2] == '启用':
            value = True
        elif args[2] == '关' or args[2] == '禁用':
            value = False
        elif args[2].isdigit():
            value = int(args[2])
        if key:
            set_group_config(gid, key, value)
            msg = '设置成功！当前设置值如下:\n'
            msg += f'群/{gid} : 设置项/{key} = 值/{value}'
        else:
            msg = '无效参数'
    elif args[0] == '状态':
        if len(args) >= 2 and args[1].isdigit():
            gid = int(args[1])
        withdraw_status = "不撤回" if get_group_config(gid, "withdraw") == 0 else f'{get_group_config(gid, "withdraw")}秒'
        lolicon_status = "启用" if get_group_config(gid, "lolicon") else "禁用"
        lolicon_r18_status = "启用" if get_group_config(gid, "lolicon_r18") else "禁用"
        acggov_status = "启用" if get_group_config(gid, "acggov") else "禁用"
        msg = f'群 {gid} :'
        msg += f'\n撤回时间: {withdraw_status}'
        msg += f'\nlolicon 源: {lolicon_status}'
        msg += f'\nlolicon_r18 源: {lolicon_r18_status}'
        msg += f'\nacggov 源: {acggov_status}'
    elif args[0] == '缓存':
        await bot.send(ev, '开始缓存')
        await fetch_process()
        msg = '缓存进程结束'
    elif args[0] == '仓库':
        msg = '仓库:'
        state = check_path()
        for k, v in state.items():
            msg += f'\n{k}源 : {v}张'
    elif args[0] == "重载":
        load_config()
        msg = '重载完成'
    elif args[0] == "黑名单" and len(args) == 3:# setu 黑名单 新增/删除 gid(一次只能提供一个)
        mode = 0 if args[1] == "新增" else 1
        group_id = args[2]
        statuscode, failedgid = set_group_list(group_id,1,mode)
        if statuscode == 403:
            msg = '无法访问黑白名单'
        elif statuscode == 404:
            msg = f'群{failedgid[0]}不在黑名单中'
        elif statuscode == 401:
            msg = f'警告！黑名单模式未开启！\n成功{args[1]}群{group_id}'
        else:
            msg = f'成功{args[1]}群{group_id}'
    elif args[0] == '白名单' and len(args) == 3:  # setu 白名单 新增/删除 gid(一次只能提供一个)
        mode = 0 if args[1] == "新增" else 1
        group_id = args[2]
        statuscode, failedgid = set_group_list(group_id, 0, mode)
        if statuscode == 403:
            msg = '无法访问黑白名单'
        elif statuscode == 404:
            msg = f'群{failedgid[0]}不在白名单中'
        elif statuscode == 402:
            msg = f'警告！白名单模式未开启！\n成功{args[1]}群{group_id}'
        else:
            msg = f'成功{args[1]}群{group_id}'
    else:
        msg = '无效参数'
    await bot.send(ev, msg)


@sv.on_rex(r'^[色涩瑟][图圖]|[来來发發给給]((?P<num>\d+)|(?:.*))[张張个個幅点點份丶](?P<keyword>.*?)[色涩瑟][图圖]')
async def send_search_setu(bot, ev):
    uid = ev['user_id']
    gid = ev['group_id']
    num = ev['match'].group('num')
    if num:
        try:
            num = int(num)
            max_num = int(get_config('base', 'max_pic_once_send'))
            if num > max_num:
                await bot.send(ev, f'太贪心辣,一次只能要{max_num}份涩图哦~')
                num = max_num
            else:
                pass
        except:
            num = 1
    else:
        num = 1
    result, msg = check_lmt(uid, num, gid)
    if result != 0:
        await bot.send(ev, msg)
        return
    keyword = ev['match'].group('keyword')
    result_list = []
    if not keyword:
        for _ in range(num):
            msg = await get_setu(gid)
            if msg == None:
                await bot.send(ev, '无可用setu模块')
                return
            try:
                result_list.append(await bot.send(ev, msg))
            except:
                print('[ERROR]图片发送失败')
                await bot.send(ev,f'涩图太涩,发不出去惹...')
            await asyncio.sleep(1)
    else:
        keyword = keyword.strip()
        await bot.send(ev, '搜索中...')
        msg_list = await search_setu(gid, keyword, num)
        if len(msg_list) == 0:
            await bot.send(ev, '没~找~到~哦,随机赠送你一份setu吧~\n可能原因:1.没有使用标准或正式角色名称\n2.兄啊，你的XP怎么这么怪啊.jpg\n3.网络不佳/搜索额度超限')
            for _ in range(num):
                msg = await get_setu(gid)
                if msg == None:
                    await bot.send(ev, '无可用setu模块')
                    return
                try:
                    result_list.append(await bot.send(ev, msg))
                except:
                    print('[ERROR]图片发送失败')
                    await bot.send(ev, f'涩图太涩,发不出去惹...')
                await asyncio.sleep(1)
        else:
            for msg in msg_list:
                try:
                    result_list.append(await bot.send(ev, msg))
                except:
                    print('[ERROR]图片发送失败')
                    await bot.send(ev, f'涩图太涩,发不出去惹...')
                await asyncio.sleep(1)
    tlmt.increase(uid, len(result_list))
    second = get_group_config(gid, "withdraw")
    if second and second > 0:
        await asyncio.sleep(second)
        for result in result_list:
            try:
                await bot.delete_msg(self_id=ev['self_id'], message_id=result['message_id'])
            except:
                print('[ERROR]撤回失败')
            await asyncio.sleep(1)
            
@sv.on_rex(r'^[本每]日[涩色瑟]图排行榜\D*(\d*)')
async def send_ranking(bot, ev):
    gid = ev['group_id']
    page = ev['match'].group(1)
    if page and page.isdigit():
        page = int(page)
        page -= 1
    else:
        page = 0
    if page < 0:
        page = 0
    msg = await get_ranking(gid, page)
    if msg == None:
        msg = '模块未启用'
    await bot.send(ev, msg)

@sv.on_prefix(('看涩图', '看色图', '看瑟图'))
async def send_ranking_setu(bot, ev):
    uid = ev['user_id']
    gid = ev['group_id']
    start = 0
    end = 0
    args = ev.message.extract_plain_text().split()
    if len(args) > 0 and args[0].isdigit():
        start = int(args[0])
        start -= 1
        if start < 0:
            start = 0
        end = start + 1
    if len(args) > 1 and args[1].isdigit():
        end = int(args[1])
    result, msg = check_lmt(uid, end - start, gid)
    if result != 0:
        await bot.send(ev, msg)
        return
    result_list = []
    for i in range(start, end):
        msg = await get_ranking_setu(gid, i)
        if msg == None:
            await bot.send(ev, '模块未启用')
            return
        try:
            result_list.append(await bot.send(ev, msg))
        except:
            print('[ERROR]图片发送失败')
            await bot.send(ev, f'涩图太涩,发不出去惹...')
        await asyncio.sleep(1)
    tlmt.increase(uid, len(result_list))
    second = get_group_config(gid, "withdraw")
    if second and second > 0:
        await asyncio.sleep(second)
        for result in result_list:
            try:
                await bot.delete_msg(self_id=ev['self_id'], message_id=result['message_id'])
            except:
                print('[ERROR]撤回失败')
            await asyncio.sleep(1)

@sv.on_prefix('提取图片')
async def get_spec_setu(bot, ev):
    args = ev.message.extract_plain_text().split()
    try:
        args = args[0]
    except:
        await bot.send(ev,'请在命令之后提供p站id哦~')
        return
    args = str(args)
    if len(args) == 8:
        msg = get_spec_image(args)
        if not msg:
            await bot.send(ev, f'没有在本地找到这张图片/不支持r18图片的提取\n原图地址:https://pixiv.lancercmd.cc/{args}')
        else:
            await bot.send(ev,msg)
    else:
        await bot.send(ev, 'p站id无效,应为8位数字id哦~')

@sv.scheduled_job('interval', minutes=10)
async def fetch_setu_process():
    await fetch_process()


#@sv.on_fullmatch('test')
@scheduler.scheduled_job('cron', hour=4, minute=40)
async def set_ban_list():
    ban_list = []
    group_info = await get_group_info(info_type='member_count')
    for group in group_info:
        group_info[group] = int(group_info[group])
        if group_info[group] >= int(get_config('base', 'ban_if_group_num_over')):
            ban_list.append(group)
        else:
            pass
    set_group_list(ban_list,1,0)
    
