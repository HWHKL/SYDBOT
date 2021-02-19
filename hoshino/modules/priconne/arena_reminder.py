import hoshino
from hoshino import R, Service, priv, util
from nonebot import NoticeSession
from hoshino.typing import CQEvent

svtw = Service(
        name = '国台服背刺时间提醒',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.NORMAL, #管理权限
        visible = True, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '订阅', #属于哪一类
        help_ = '你猜' #帮助文本
        )



svjp = Service(
        name = '日服背刺时间提醒',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.NORMAL, #管理权限
        visible = True, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '订阅', #属于哪一类
        help_ = '你猜' #帮助文本
        )



msg = '骑士君，准备好背刺了吗？'

@svtw.scheduled_job('cron', hour='14', minute='45')
async def pcr_reminder_tw():
    await svtw.broadcast(msg, 'pcr-reminder-tw', 0.2)

@svjp.scheduled_job('cron', hour='13', minute='45')
async def pcr_reminder_jp():
    await svjp.broadcast(msg, 'pcr-reminder-jp', 0.2)
