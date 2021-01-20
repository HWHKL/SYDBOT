PORT = 9222           #本条请保持默认
HOST = '0.0.0.0'      # 本条请保持默认,本地部署使用此条配置（QQ客户端和bot端运行在同一台计算机）
DEBUG = False           # 调试模式,不建议开启
SUPERUSERS = []    # 填写超级用户的QQ号，可填多个用半角逗号","隔开
NICKNAME = r'xcw|小仓唯|镜华|at,qq=1111111'           # 设置bot的昵称，at，qq=xxxxxxxx处为bot的QQ号,呼叫昵称等同@bot,推荐修改
IP = ''                                      #修改为你的服务器ip,推荐修改
public_address = ''                     #修改为你的服务器ip+端口,推荐修改
BOTNAME = ''
'''
-------------apikeys---------------
lolicon_api,相关插件shebot/shebot_old,申请地址https://api.lolicon.app/#/setu?id=apikey
acggov_api,相关插件acggov,setuacggov,申请地址https://www.acg-gov.com/
shitu_api,相关插件shitu,申请地址http://saucenao.com/
jjc_api,相关插件arena,申请地址https://www.pcrdfans.com/bot，请注意，光佬已经停止了key的申请，很长一段时间内大概率无法使用jjc查询
'''
lolicon_api = ''                                        
acggov_api = '' 
shitu_api = ''                                           
jjc_api = ""
                             
###################################
'''-------本部分建议不要改动-------'''
IMAGE_PATH = "../miraiGO/data/images"                 #MiraiGO用这条,保持默认即可
COMMAND_START = {''}    # 命令前缀（空字符串匹配任何消息）
COMMAND_SEP = set()     # 命令分隔符（hoshino不需要该特性，保持为set()即可）
# 发送图片的协议
# 可选 http, file, base64
# 当QQ客户端与bot端不在同一台计算机时，可用http协议
RES_PROTOCOL = 'file'
###################################
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = r'./res/'
# 使用http协议时需填写，原则上该url应指向RES_DIR目录
RES_URL = 'http://127.0.0.1:5000/static/'
###################################
'''插件开关
初次尝试部署时请先保持默认
如欲启用新模块，请认真阅读readme，逐个启用逐个配置'''
###################################
MODULES_ON = {
    'anticoncurrency',# 反并发插件
    #'authMS',#授权管理
    'arkavatarguess',
    #'birthday',#生日
    'bot_manager_web',#网页服务
    'botmanage',#服务
    'bang-gacha',#邦邦抽卡
    #'clanbattle_rank',#会战排名查询插件
    'clanbattle_report',#会战报告生成，需要修改路径
    'dice',#骰子
    'eclanrank',#排名
    #'emergeface',#换脸插件,#需要apikey
    'eqa',#问答
  #  'explosion',#每天一发惠惠 还没改
    'entertain',#其他功能
    'fake_message',#假消息
    'fgoavatarguess',#猜从者
    'generator',#营销文生成等五个小功能
    'groupchat',#龙王，合刀
    'groupmaster',#群聊基础功能
    'hiumsentences',#网抑云语录
    'image-generate',#取代原image
    #'Luna',
    #'mawo',
    'memberguess',#猜群友头像
    'meme_web',#memegenerator的web化,#勿同时开启
    'music',#点歌插件
    'mrfzguess',#明日方舟猜角色
    #'nbnhhsh',#将抽象短语转化为好好说话
    'nowtime',#发送"报时"有惊喜
   # 'ontree_scheduler',#挂树优化提醒
    #'pages',#bot网页端
    'pcr_calendar',#全服务器通用日历表，关键词为日历
    'pcravatarguess',#图片猜角色
    'pcrdescguess',#通过角色描述猜角色,#需要设置go-cqhttp的心跳间隔,#推荐3
    #'pcrmemorygames',#公主连结记忆小游戏
    #'pcrmiddaymusic',#公主连结午间音乐
    #'pcrsealkiller',#海豹杀手
   # 'pcrjjc',
    'pokemanpcr',#戳一戳卡片小游戏
    'portune',#运势插件
    'priconne',#抽卡/竞技场之类的集合
    'reload',#重启
    #'revgif',#倒放
    'rua',#搓群友头像
    'russian',#俄罗斯轮盘赌
    #'setu_mix',#俩涩图插件合二为一
    #'shebot',#插件合集，来源https://github.com/pcrbot/plugins-for-Hoshino,#其中的接头需要百度云api
    #'tarot',#塔罗牌
    #'translate',#原生翻译功能
    'voiceguess',#猜语音
    'yobot',#yobot会战功能
    'zfjbot-jjc-finder',#jjc场次
    
    
}
