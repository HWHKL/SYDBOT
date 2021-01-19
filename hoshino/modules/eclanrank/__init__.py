"""
作者艾琳有栖

版本 0.1.0

基于 nonebot pcr公会站排行插件

使用 会战排行关键字 查询一个公会名或者rank

会战锁定公会名 来进行锁定一个公会
会战解锁公会名 解锁一个公会

公会排行 查询绑定的公会


查询记录之前的排名

"""
from nonebot import *
from . import util
from . import clanrank
from . import locked
from hoshino import Service  # 如果使用hoshino的分群管理取消注释这行

#
sv = Service('工会排名', visible= True, enable_on_default= False, bundle='工会排名', help_='''
会战排行  | 查询公会名或排行 | 会战排行K.A. <br>会战排行1000
会战锁定  | 锁定后根据设定自动推送排行信息<br>并且会自动记录上次的排行信息做比较 | 会战锁定K.A.
会战解锁 | 解锁一个被锁定的公会 | 会战解锁K.A.
公会排行 | 查询当前锁定的公会 | 公会排行
'''.strip())

# 初始化配置文件
config = util.get_config()

# 初始化nonebot
_bot = get_bot()


@sv.on_message('group')  # 如果使用hoshino的分群管理取消注释这行 并注释下一行的 @_bot.on_message("group")
# @_bot.on_message("group") # nonebot使用这
async def epck_main(*params):
    bot, ctx = (_bot, params[0]) if len(params) == 1 else params

    msg = str(ctx['message']).strip()
    # 查询会战
    keyword = util.get_msg_keyword(config['comm']['keyword'], msg, True)
    if keyword:
        return await bot.send(ctx, clanrank.get_rank(keyword))
    # 会战锁定
    keyword = util.get_msg_keyword(config['comm']['locked'], msg, True)
    if keyword:
        return await bot.send(ctx, locked.lock(ctx, keyword))
    # 会战解锁
    keyword = util.get_msg_keyword(config['comm']['unlocked'], msg, True)
    if keyword:
        return await bot.send(ctx, locked.unlock(ctx, keyword))
    # 会战锁定查询
    keyword = util.get_msg_keyword(config['comm']['defaultLucked'], msg, True)
    if keyword == '':
        return await bot.send(ctx, locked.default_rank(ctx['group_id']))


