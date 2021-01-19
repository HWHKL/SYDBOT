from hoshino import Service

sv_help = '''
[黄骑充能] 由加莉1动规律
[角色站位] 角色站位表
'''.strip()

sv = Service('pcr-query', help_=sv_help, bundle='pcr查询')

from .query import *
from .miner import *
