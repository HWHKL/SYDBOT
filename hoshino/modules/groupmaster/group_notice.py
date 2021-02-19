
import hoshino
from hoshino import Service, priv
from hoshino.typing import NoticeSession
sv_help = '''看名字！'''
sv1 = Service(
        name = '退群通知',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.ADMIN, #管理权限
        visible = True, #是否可见
        enable_on_default = True, #是否默认启用
        bundle = '退群通知', #属于哪一类
        help_ = sv_help #帮助文本
        )
        
@sv1.on_notice('group_decrease.leave')
async def leave_notice(session: NoticeSession):
    await session.send(f"{session.ctx['user_id']}离开这里啦。")
sv_help1 = '''看名字！'''
sv2 = Service(
        name = '入群欢迎',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.ADMIN, #管理权限
        visible = True, #是否可见
        enable_on_default = True, #是否默认启用
        bundle = '入群欢迎', #属于哪一类
        help_ = sv_help1 #帮助文本
        )
        
@sv2.on_notice('group_increase')
async def increace_welcome(session: NoticeSession):
    
    if session.event.user_id == session.event.self_id:
        return  # ignore myself
    
    welcomes = hoshino.config.groupmaster.increase_welcome
    gid = session.event.group_id
    if gid in welcomes:
        await session.send(welcomes[gid], at_sender=True)
    elif 'default' in welcomes:
        await session.send(welcomes['default'], at_sender=True)
