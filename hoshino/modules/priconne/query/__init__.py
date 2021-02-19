from hoshino import Service

sv_help = '''
[黄骑充电] 由加莉1动规律
[角色站位] 角色站位表
[露娜充电] 露娜充电规律
[半月刊]   活动半月刊
[角色专武] 专武顺序
'''.strip()


sv = Service('常用查询', help_=sv_help, bundle='查询')

from .query import *
from .miner import *
