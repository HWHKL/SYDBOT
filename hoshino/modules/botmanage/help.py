from hoshino import Service, priv, config
from hoshino.typing import CQEvent

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

TOP_MANUAL1 = '''
使用说明:
方括号[ ]内为关键词
空格不可省略
为保证与标准xcwbot类功能接轨
进行统一化分类帮助
※注意某些功能被隐藏或没有说明
※注意某些功能无法被您开关
'''.strip()

TOP_MANUAL2 = '''
※本bot有五类功能，触发关键词：
- [帮助订阅]
- [帮助查询]
- [帮助娱乐]
- [帮助通用]
- [帮助会战]
以上关键词中[帮助]可替换为[详细帮助]
'''.strip()

TOP_MANUAL3 = '''
※本部分仅管理员及以上权限有效
※控制功能开关:
- [开启 XX] （有空格）
- [禁用 XX] （有空格）
XX为功能名
※本群功能开关总览:
- [lssv]
'''.strip()

TOP_MANUAL4 = '''
※本版本yobot为插件版
想要了解yobot：
- 发送 [帮助]
'''.strip()

TOP_MANUAL5 = '''
※查看单个功能详情
开启功能后发送：
- [帮助XX] （无空格）
XX为功能名
'''.strip()

BANGZHU_GN = '''
※查看单个功能详情
开启功能后发送：
- [帮助XX] （无空格）
XX为功能名
'''.strip()

BANGZHU_KG = '''
※本部分仅群管及以上权限有效
※控制功能开关:
- [开启 XX] （有空格）
- [禁用 XX] （有空格）
XX为功能名
※本群功能开关总览:
- [lssv]
'''.strip()

def gen_bundle_manual(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible:
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name}")
    return '\n'.join(manual)

def gen_bundle_manual_all(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible:
            spit_line = '=' * max(0, 18 - len(sv.name))
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name} {spit_line}")
            if sv.help:
                manual.append(sv.help)
    return '\n'.join(manual)

@sv.on_prefix(('help', '帮助', '幫助'))
async def send_help(bot, ev: CQEvent):
    gid = ev.group_id
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    services = Service.get_bundles()
    if not bundle_name:
        data_all = []
        data1 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": TOP_MANUAL1
            }
            }
        data2 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": TOP_MANUAL2
            }
            }    
        data3 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": TOP_MANUAL3
            }
            }
        data4 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": TOP_MANUAL4
            }
            }
        data5 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": TOP_MANUAL5
            }
            }
        data_all=[data1,data2,data3,data4,data5]
        await bot.send_group_forward_msg(group_id=ev['group_id'], messages=data_all)
        await bot.send(ev, f'当前版本{config.version}')
    elif bundle_name in bundles:
        msg = gen_bundle_manual(bundle_name, bundles[bundle_name], ev.group_id)
        data_all = []
        data1 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": msg
            }
            }
        data2 ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": BANGZHU_GN
            }
            }    
        data_all=[data1,data2]
        await bot.send_group_forward_msg(group_id=ev['group_id'], messages=data_all)
        

@sv.on_prefix(('详细help', '详细帮助', '详细幫助'))
async def send_help(bot, ev: CQEvent):
    uid = ev.user_id
    gid = ev.group_id
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    if not bundle_name:
        await bot.send(ev, TOP_MANUAL)
        await bot.send(ev, f'当前版本{config.version}')
    elif bundle_name in bundles:
        msg = gen_bundle_manual_all(bundle_name, bundles[bundle_name], ev.group_id)
        data ={
            "type": "node",
            "data": {
                "name": '工具人',
                "uin": '2857117409',
                "content": msg
            }
            }
        await bot.send_group_forward_msg(group_id=gid, messages=data)
        
@sv.on_fullmatch(["帮助功能开关"])
async def bangzhu_kg(bot, ev):
    await bot.send(ev, BANGZHU_KG)