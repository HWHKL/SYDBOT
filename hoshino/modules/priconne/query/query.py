import itertools
from hoshino import util, R
from hoshino.typing import CQEvent
from . import sv


YUKARI_SHEET_ALIAS = map(lambda x: ''.join(x), itertools.product(('黄骑', '酒鬼', '黃騎'), ('充电', '充电表', '充能', '充能表')))
YUKARI_SHEET = f'''
{R.img('priconne/quick/黄骑充电.jpg').cqcode}
※大圈是1动充电对象
※黄骑四号位例外较多
※对面羊驼或中后卫坦有可能歪
※我方羊驼算一号位
'''

@sv.on_fullmatch(YUKARI_SHEET_ALIAS)
async def yukari_sheet(bot, ev):
    await bot.send(ev, YUKARI_SHEET)


@sv.on_fullmatch(('角色位置','角色站位','站位'))
async def stand_position(bot,ev):
    await bot.send(ev,R.img('priconne/quick/position.png').cqcode)


@sv.on_fullmatch(('露娜充电','露娜充电表','露娜充能','露娜充能表'))
async def stand_position(bot,ev):
    await bot.send(ev,R.img('priconne/quick/luna.jpg').cqcode)

@sv.on_fullmatch(('半月刊'))
async def stand_position(bot,ev):
    await bot.send(ev,R.img('priconne/quick/半月刊.jpg').cqcode)

@sv.on_fullmatch(('角色专武','专武顺序表','专武顺序'))
async def stand_position(bot,ev):
    await bot.send(ev,R.img('priconne/quick/zhuanwu.jpg').cqcode)

#DRAGON_TOOL = f'''
#拼音对照表：{R.img('priconne/KyaruMiniGame/注音文字.jpg').cqcode}{R.img('priconne/KyaruMiniGame/接龙.jpg').cqcode}
#龍的探索者們小遊戲單字表 https://hanshino.nctu.me/online/KyaruMiniGame
#镜像 https://hoshino.monster/KyaruMiniGame
#网站内有全词条和搜索，或需科学上网'''

'''
@sv.on_fullmatch(('一个顶俩', '拼音接龙', '韵母接龙'))
async def dragon(bot, ev):
    await bot.send(ev, DRAGON_TOOL, at_sender=True)
    await util.silence(ev, 60)
'''
