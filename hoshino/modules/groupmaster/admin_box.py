from hoshino import Service, priv
import random


sv_help = '''
反撤回 #反匿名(鬼知道啥时候好使
'''.strip()

sv = Service(
        name = '超级管理',  #功能名
        use_priv = priv.NORMAL, #使用权限   
        manage_priv = priv.SUPERUSER, #管理权限
        visible = False, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '超级管理', #属于哪一类
        help_ = sv_help #帮助文本
        )

@sv.on_fullmatch(["帮助超级管理"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=False)


@sv.on_notice('group_recall')
async def show_recall(session):
	bot,event=session.bot,session.event
	if event.user_id != event.operator_id:
		return
	mid = event.message_id
	uid = event.user_id
	msg = await bot.get_group_msg(message_id=mid)
	msg = msg['content']
	await bot.send(event, f'[CQ:at,qq={uid}]撤回的消息是：\n{msg}')
'''
anti_anony = ('你是谁？','为什么要匿名？')

@sv.on_message('group')
async def anti_anonymous(bot, event):
	if not event.anonymous:
		return
	await bot.send(event, random.choice(anti_anony))
	'''