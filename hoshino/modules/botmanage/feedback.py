import hoshino
from hoshino import Service, priv
from hoshino.typing import CQEvent
from hoshino.util import DailyNumberLimiter

sv_help = '''
[反馈] 后接反馈内容 联系维护组
'''.strip()

sv = Service(
    name = '反馈',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '反馈', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["帮助反馈"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=False)

_max = 3
lmt = DailyNumberLimiter(_max)
EXCEED_NOTICE = f'您今天已经反馈过{_max}次了，请明早5点后再来！'

@sv.on_prefix('反馈')
async def feedback(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, EXCEED_NOTICE, at_sender=True)
    text = ev.message
    if not text:
        await bot.send(ev, f"请发送反馈+您要反馈的内容~", at_sender=True)
    else:
        coffee = hoshino.config.SUPERUSERS[0]
        await bot.send_private_msg(self_id=ev.self_id, user_id=coffee, message=f'Q{uid}@群{ev.group_id}\n{text}')
        await bot.send(ev, f'您的反馈已发送至维护组！\n======\n{text}', at_sender=True)
        lmt.increase(uid)
