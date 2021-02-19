import requests
from hoshino import Service, priv
from nonebot import on_command

sv_help = '''
- [上号/生而为人/生不出人/网抑云/已黑化]
'''.strip()

sv = Service(
    name = '网易云',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = '娱乐', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["帮助网易云"])
async def bangzhu(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)
    
   # resp = requests.get('http://api.heerdev.top/nemusic/random',timeout=30)
#'''
 #   if resp.status_code == requests.codes.ok:
  #      res = resp.json()
   #     sentences = res['comments']
    #    await session.send(sentences, at_sender=True)
    #    else:
      #  await session.send('上号失败，我很抱歉。您不pay被抑郁。', at_sender=True)
     #   '''

@on_command('网易云', aliases=('生不出人','网抑云'), only_to_me=False)
async def music163_sentences(session):
    resp = requests.get('https://v1.hitokoto.cn/?c=a',timeout=30)
    res = resp.json()
    sentences = res['hitokoto']
    await session.send(sentences)    
