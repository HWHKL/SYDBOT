import math
from hoshino import Service, priv


sv = Service("击剑路径计算")

sv_help = '''
击剑路径 100  | 计算今天5次战斗的最优路径
此功能存在±1~3名的误差，排名越低误差越大
'''.strip()

sv = Service(
        name = '击剑路径',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.ADMIN, #管理权限
        visible = True, #是否可见
        enable_on_default = True, #是否默认启用
        bundle = '通用', #属于哪一类
        help_ = sv_help #帮助文本
        )

@sv.on_fullmatch(["帮助击剑路径"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)


@sv.on_rex(r'击剑路径 (.{0,5})$')
async def arena_route(bot,ev):
    num=int(ev['match'].group(1))
    r={}
    rank = 0
    while num>1:
        rank += 1
        if (num<=11):
            num = 1
        elif (num<69):
            num -= 10
        else:
            num = math.floor(num*0.85)
        r[rank] = num
    await bot.send(ev,"最优击剑路径(大概)："+','.join(map(str,list(r.values())[:5])),at_sender=True)