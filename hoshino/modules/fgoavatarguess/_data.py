'''Fate/GrandOrder的数据'''
'''角色名称
遵照格式： id: [常用译名 , 常见别称, 外号, 带错别字的别称等] （<-依此顺序）
'''
CHARA_NAME = {
    1001: ["玛修·基列莱特","玛修","色茄子","学妹","马修"],
    1002: ["阿尔托莉雅·潘德拉贡","阿尔托利亚","呆毛","saber","棉被","吾王"],
    1003: ["阿尔托莉雅·潘德拉贡(Alter)","黑呆","黑无毛","黑SABER"],
    1004: ["阿尔托莉雅·潘德拉贡〔Lily〕","莉莉","白SABER"],
    1005: ["尼禄·克劳狄乌斯","唔呣","罗马之花","红SABER"],
    1006: ["齐格飞","飞哥","对不起先生","七个肺"],
    1007: ["盖乌斯·尤利乌斯·恺撒","凯撒","胖尼禄","凯胖"],
    1008: ["阿蒂拉","大王","B提拉","彩笔","阿提拉"],
    1009: ["吉尔·德·雷","剑元帅","贞德厨"],
    1010: ["骑士迪昂","百合剑","迪昂"],
    1011: ["卫宫","巨侠","emiya","红茶"],
    1012: ["吉尔伽美什","闪闪","金闪闪","弓闪"],
    1013: ["罗宾汉","绿茶","罗宾"],
    1014: ["阿塔兰忒","猫茶","阿塔","塔喵"],
    1015: ["尤瑞艾莉","二姐"],
    1016: ["阿拉什","大英雄","stella","自爆弓"],
    1017: ["库·丘林","大狗","库丘林","枪狗","狗"],
    1018: ["伊丽莎白·巴托里","龙娘","伊丽莎白"],
    1019: ["武藏坊弁庆","武僧","武藏坊"],
    1020: ["库·丘林〔Prototype〕","旧狗"],
    1021: ["列奥尼达一世","炎头","斯巴达"],
    1022: ["罗穆路斯","罗马"],
    1023: ["美杜莎","R姐"],
    1024: ["乔尔乔斯","乔老师"],
    1025: ["爱德华·蒂奇","黑胡子"],
    1026: ["布狄卡","布妈"],
    1027: ["牛若丸","牛肉丸"],
    1028: ["亚历山大","幼帝"],
    1029: ["玛丽·安托瓦内特","蛋糕","WO酱","玛丽"],
    1030: ["玛尔达","马达"],
    1031: ["美狄亚","c妈"],
    1032: ["吉尔·德·雷(caster)","C元帅"],
    1033: ["汉斯·克里斯蒂安·安徒生","安日天","安徒生"],
    1034: ["威廉·莎士比亚","莎翁","莎士比亚"],
    1035: ["梅菲斯托费勒斯","梅菲斯特"],
    1036: ["沃尔夫冈·阿马德乌斯·莫扎特","莫渣特","莫扎特"],
    1037: ["诸葛孔明〔埃尔梅罗Ⅱ世〕","王妃","诸葛孔明","孔明","诸葛亮","为所欲为"],
    1038: ["库·丘林(caster)","术狗","c汪","c狗"],
    1039: ["佐佐木小次郎","屠龙剑圣","小次郎"],
    1040: ["咒腕哈桑","真哈桑","咒腕"],
    1041: ["斯忒诺","大姐"],
    1042: ["荆轲","毛腿王"],
    1043: ["夏尔·亨利·桑松","处刑","夏尔","桑松","处刑人"],
    1044: ["歌剧魅影","赛巴斯","魅影"],
    1045: ["玛塔·哈丽","舞娘","玛塔哈丽"],
    1046: ["卡米拉","大龙娘"],
    1047: ["赫拉克勒斯","B叔"],
    1048: ["兰斯洛特","岳父","长江骑士","狂兰"],
    1049: ["吕布奉先","吕高达","吕布","马中赤兔"],
    1050: ["斯巴达克斯","抖M","微笑boy"],
    1051: ["坂田金时","狗蛋","金时","gold"],
    1052: ["莉弗拉德三世","大公","刺绣公"],
    1053: ["阿斯忒里俄斯","小牛","牛牛"],
    1054: ["卡利古拉","鬼舅","尼禄舅舅"],
    1055: ["大流士三世","大表哥","酋长","大流士"],
    1056: ["清姬","斯托卡"],
    1057: ["血斧埃里克","血斧王"],
    1058: ["玉藻猫","B狐"],
    1059: ["贞德","村姑"],
    1060: ["俄里翁","月神"],
    1061: ["伊丽莎白·巴托里〔万圣节〕","C龙娘","术龙娘"],
    1062: ["玉藻前","c狐","小玉"],
    1063: ["大卫","制杖弓兵","所罗王他爹"],
    1064: ["赫克托耳","赫叔","友尽的证明"],
    1065: ["弗朗西斯·德雷克","海盗船长","船长","德雷克"],
    1066: ["安妮·伯妮＆玛莉·瑞德","骑双子","安与玛丽"],
    1067: ["美狄亚〔Lily〕","C子","美狄亚lily"],
    1068: ["冲田总司","樱SABER","总司","冲田"],
    1069: ["织田信长","nobu","第六天萌王","信长","弓信"],
    1070: ["斯卡哈","BBA","紫发老太婆"],
    1071: ["迪卢木多·奥迪那","刷子","迪卢木多"],
    1072: ["弗格斯·马克·罗伊","小刚","弗格斯"],
    1073: ["阿尔托莉雅・潘德拉贡〔圣诞Alter〕","骑黑呆","圣诞黑呆"],
    1074: ["童谣","魔导书","爱丽丝"],
    1075: ["开膛手杰克","女儿","小红鞋"],
    1076: ["莫德雷德","小莫","坑爹剑"],
    1077: ["尼古拉·特斯拉","特总","特斯拉"],
    1078: ["阿尔托莉雅・潘德拉贡〔Alter〕","枪黑呆","乳下"],
    1079: ["冯·霍恩海姆·帕拉塞尔苏斯","豆爸","霍恩海姆"],
    1080: ["查尔斯·巴贝奇","蒸汽王","巴贝奇","BBQ"],
    1081: ["亨利·杰基尔＆海德","化身博士","海德"],
    1082: ["弗兰肯斯坦","肯娘","弗兰"],
    1083: ["所罗门(beast)","小便王"],
    1084: ["阿周那","周黑鸭","阿三"],
    1085: ["迦尔纳","小太阳"],
    1086: ["谜之女主角X","x毛","星战呆毛"],
    1087: ["芬恩`麦克库尔","苦主","芬恩"],
    1088: ["布伦希尔德","布姐"],
    1089: ["贝奥武夫","贝爷"],
    1090: ["尼禄·克劳狄乌斯〔花嫁〕","嫁王","花嫁尼禄"],
    1091: ["两仪式(根源)","根源式"],
    1092: ["两仪式","式姐","织哥"],
    1093: ["天草四郎","圣诞假面","天草"],
    1094: ["阿斯托尔福","黑虎阿福","阿福"],
    1095: ["幼吉尔","幼闪"],
    1096: ["岩窟王","伯爵","岛崎信长","库哈哈哈哈"],
    1097: ["南丁格尔","护士","南丁","男丁"],
    1098: ["库·丘林〔Alter〕","黑狗","狂狗"],
    1099: ["女王梅芙","妹夫","梅芙"],
    1100: ["海伦娜·布拉瓦茨基","海妈","海伦娜"],
    1101: ["罗摩","红阿塔"],
    1102: ["李书文","李大师"],
    1103: ["托马斯·爱迪生","托马狮","爱迪生","爱迪狮"],
    1104: ["杰罗尼莫","萨满"],
    1105: ["比利小子","快枪手","比利"],
    1106: ["贞德〔Alter〕","黑贞"],
    1107: ["安哥拉曼纽","小安"],
    1108: ["伊斯坎达尔","大帝"],
    1109: ["卫宫〔Assassin〕","切丝PAPA","卫宫切嗣"],
    1110: ["百貌哈桑","体操团"],
    1111: ["爱丽丝菲尔〔天之衣〕","太太","天之衣"],
    1112: ["酒吞童子","凹酱","酒吞"],
    1113: ["玄奘三藏","唐僧","唐三藏"],
    1114: ["源赖光","奶光","赖光"],
    1115: ["坂田金时(rider)","R狗蛋","r金时"],
    1116: ["茨木童子","脚神","茨木"],
    1117: ["风魔小太郎","五代风魔","小太郎","风魔"],
    1118: ["奥斯曼狄斯","拉二","拉美西斯二世"],
    1119: ["阿尔托莉雅·潘德拉贡(lancer)","狮子王","乳上","白枪呆","枪呆"],
    1120: ["尼托克丽丝","女法老","尼托"],
    1121: ["兰斯洛特(saber)","剑兰","剑长江"],
    1122: ["崔斯坦","崔悲伤","老崔"],
    1123: ["高文","gay文"],
    1124: ["静谧哈桑","毒娘","静谧"],
    1125: ["俵藤太","送水弓","送米弓","俵哥","俵爷"],
    1126: ["贝德维尔","小贝","贝狄威尔"],
    1127: ["莱昂纳多·达·芬奇","大碧池","奸商","达芬奇"],
    1128: ["玉藻前(水着)","枪狐","泳装玉藻前"],
    1129: ["阿尔托莉雅·潘德拉贡(水着)","弓呆","泳装呆毛"],
    1130: ["玛丽·安托瓦内特(水着)","C玛丽","泳装蛋糕"],
    1131: ["安妮·伯妮＆玛莉·瑞德(水着)","弓双子","泳装双子"],
    1132: ["莫德雷德(水着)","R莫","泳装小莫"],
    1133: ["斯卡哈(水着)","杀师酱","泳装斯卡哈","泳装师匠"],
    1134: ["清姬(水着)","枪清姬","泳装清姬"],
    1135: ["玛尔达(水着)","铁拳圣女","泳装马达"],
    1136: ["伊莉雅丝菲尔·冯·爱因兹贝伦","小学生","伊利亚","伊莉雅","伊利亚斯菲尔"],
    1137: ["克洛伊·冯·爱因兹贝伦","小黑","克洛伊"],
    1138: ["伊丽莎白·巴托里〔勇者〕","剑龙娘","勇者龙娘"],
    1139: ["克娄巴特拉","艳后","埃及艳后","超高校级艳后"],
    1140: ["弗拉德三世〔EXTRA〕","枪大公"],
    1141: ["贞德·Alter·Santa·Lily","幼贞","圣诞幼贞"],
    1142: ["伊什塔尔","弓凛","伊修塔尔"],
    1143: ["恩奇都","小恩"],
    1144: ["魁札尔·科亚特尔","羽蛇神","大姐姐"],
    1145: ["吉尔伽美什(caster)","c闪","贤王","村长"],
    1146: ["美杜莎(lily)","安娜","美杜莎lily"],
    1147: ["戈耳工","魔神R姐","戈尔贡"],
    1148: ["豹人","老虎","藤虎"],
    1149: ["提亚马特","提妈"],
    1150: ["梅林","老色鬼","阿瓦隆剑圣","网络偶像"],
    1151: ["盖提亚","盖总"],
    1152: ["所罗门","医生"],
    1153: ["宫本武藏","火箭队","武藏"],
    1154: ["“山中老人”","爷爷","王哈桑","狂战信条"],
    1155: ["谜之女主角X〔Alter〕","bx毛","黑X毛"],
    1156: ["詹姆斯·莫里亚蒂","教授","莫里亚蒂"],
    1157: ["卫宫〔Alter〕","黑A","黑卫宫","黑不溜秋"],
    1158: ["黑森·罗伯","狼王","萝卜"],
    1159: ["燕青","小乙"],
    1160: ["亚瑟·潘德拉贡〔Prototype〕","旧剑","亚瑟"],
    1161: ["土方岁三","副长","土方"],
    1162: ["茶茶","淀殿"],
    1163: ["melt lilith","莉莉丝","刀锋战士"],
    1164: ["Passionlip","lip"],
    1165: ["铃鹿御前","JK狐"],
    1166: ["BB","2B"],
    1167: ["杀生院祈荒","尼姑","杀生院"],
    1168: ["BeastⅢ／R","魔性菩萨"],
    1169: ["山鲁佐德","1001"],
    1170: ["武则天","媚娘","武媚娘"],
    1171: ["彭忒西勒亚","CEO","彭忒"],
    1172: ["克里斯托弗·哥伦布","颜艺老头","哥伦布"],
    1173: ["夏洛克·福尔摩斯","老福","福尔摩斯"],
    1174: ["保罗·班扬","伐木巨人","保罗"],
    1175: ["尼禄·克劳狄乌斯(Caster)","水尼禄","水泥"],
    1176: ["弗兰肯斯坦(Saber)","剑肯娘","泳装肯娘"],
    1177: ["尼托克丽丝(Assassin)","水尼托","泳装尼托"],
    1178: ["织田信长(Berserker)","狂信长","泳装信长"],
    1179: ["阿尔托莉雅·潘德拉贡〔Alter〕(Rider)","水骑呆","泳装黑呆"],
    1180: ["海伦娜·布拉瓦茨基(Archer)","奥特曼","泳装海伦娜","弓海伦娜"],
    1181: ["源赖光(Lancer)","枪奶光","泳装源赖光"],
    1182: ["伊什塔尔(Rider)","骑凛","泳装凛"],
    1183: ["帕尔瓦蒂","雪山樱"],
    1184: ["巴御前","鲅鱼圈"],
    1185: ["望月千代女","蛇巫女"],
    1186: ["宝藏院胤舜","秃子","宝藏院"],
    1187: ["柳生但马守宗矩","柳糖","柳生"],
    1188: ["加藤段藏","飞加藤","段藏"],
    1189: ["刑部姬","老邢","宅女"],
    1190: ["机械伊丽酱","机械龙娘"],
    1191: ["机械伊丽酱II号机","机械龙娘2号"],
    1192: ["喀耳刻","C姑妈","喀尔刻"],
    1193: ["哪吒","三太子"],
    1194: ["示巴女王","所罗门老婆","示巴"],
    1195: ["阿比盖尔·威廉姆斯","阿比","阿比盖尔","Abigail"],
    1196: ["埃蕾什基伽勒","艾蕾","枪凛"],
    1197: ["阿蒂拉·圣诞","弓大王","弓提拉","圣诞阿提拉"],
    1198: ["葛饰北斋","阿荣","北宅"],
    1199: ["塞弥拉弥斯","女帝"],
    1200: ["浅上藤乃","拆桥","藤乃"],
    1201: ["阿纳斯塔西娅","皇女"],
    1202: ["阿塔兰忒〔Alter〕","黑塔","黑阿塔"],
    1203: ["阿维斯布隆","哲学家"],
    1204: ["安东尼奥·萨列里","萨老师","安东尼奥","萨列里"],
    1205: ["伊凡雷帝","雷弟","雷帝"],
    1206: ["阿喀琉斯","脚后跟","阿脚","铁华团团长"],
    1207: ["喀戎","老师","马老师"],
    1208: ["齐格","齐傲天"],
    1209: ["冲田总司〔Alter〕","魔总","魔神总司"],
    1210: ["冈田以藏","始末犬"],
    1211: ["坂本龙马","替身使者","龙马"],
    1212: ["拿破仑","拿皇"],
    1213: ["齐格鲁德","西哥","西格鲁德"],
    1214: ["瓦尔基里","女武神"],
    1215: ["斯卡哈=斯卡蒂","CBA","斯卡蒂"],
    1216: ["贞德(水着)","弓贞","姐姐","泳装贞德"],
    1217: ["茨木童子(水着)","枪茨木","泳装茨木"],
    1218: ["牛若丸(水着)","狗肉丸","泳装牛肉丸"],
    1219: ["贞德〔Alter〕(水着)","狂贞","泳装黑贞"],
    1220: ["BB(水着)","泳装bb"],
    1221: ["女王梅芙(水着)","泳装梅芙"],
    1222: ["谜之女主角XX","XX毛"],
    1223: ["迪尔姆德·奥迪那(saber)","剑刷"],
    1224: ["志度内","熊莉亚"],
    1225: ["酒吞童子(护法少女)","C酒吞"],
    1226: ["项羽","人马","西楚霸王"],
    1227: ["兰陵王","长恭"],
    1228: ["秦良玉","包子头"],
    1229: ["始皇帝","政哥哥","大幺蛾子","秦始皇"],
    1230: ["虞美人","摸虞","虞姬"],
    1231: ["赤兔马","吕布赤兔","孽障","马中吕布"],
    1232: ["布拉达曼特","尻枪","屁股枪"],
    1233: ["魁札尔·科亚特尔〔桑巴／圣诞〕","圣诞羽蛇神"],
    1234: ["红阎魔","小麻雀"],
    1235: ["李书文(assasin)","老李"],
    1236: ["美游·艾德费尔特","卫宫美游","美游"],
    1237: ["紫式部","奶紫"],
    1238: ["Kingprotea","巨萝莉", "巨樱", "绷带樱","帝王花"],
    1239: ["迦摩","夹馍","伽摩"],
    1240: ["BeastⅢ／L","黑樱"],
    1241: ["司马懿","莱妹","义妹"],
    1242: ["阿斯特蕾亚","金钻头"],
    1243: ["格蕾","小灰","格雷"],
    1244: ["吉娜可","伟大的石像神","大象","吉娜可‧加里吉利"],
    1245: ["拉克什米·芭伊","印度贞德"],
    1246: ["威廉·退尔","大叔"],
    1247: ["阿周那〔Alter〕","狂那"],
    1248: ["马嘶","轮子哥"],
    1249: ["阿斯克勒庇俄斯","医神"],
    1250: ["魔王信长","魔信"],
    1251: ["森长可","鬼武藏"],
    1252: ["长尾景虎","上杉谦信"],
    1253: ["莱昂纳多·达·芬奇(lily)","小碧池"],
    1254: ["伊阿宋","渣宋"],
    1255: ["帕里斯","白莲花"],
    1256: ["加雷斯","加妹"],
    1257: ["巴沙洛缪·罗伯茨","海贼男爵","罗伯茨"],
    1258: ["陈宫","自爆军师"],
    1259: ["夏绿蒂·科黛","暗杀天使","夏绿蒂"],
    1260: ["莎乐美","病娇"],
    1261: ["宫本武藏(水着)","水武藏"],
    1262: ["刑部姬(水着)","弓刑","泳装刑部姬"],
    1263: ["卡米拉(水着)","骑米拉","泳装大龙娘"],
    1264: ["葛饰北斋(水着)","剑北斋","泳装北宅"],
    1265: ["阿尔托莉雅·潘德拉贡(兔女郎)","兔子王"],
    1266: ["朗姆达莉莉丝","企鹅莉莉丝","lilith(水着)"],
    1267: ["冲田总司(水着)","杀总司","泳装总司"],
    1268: ["宇宙伊修塔尔","宇宙凛"],
    1269: ["灾星简","野姑娘杰恩"],
    1270: ["阿斯托尔福(saber)","剑阿福","乌鸦坐飞机"],
    1271: ["南丁格尔(圣诞)","弓南丁","圣诞南丁"],
    1272: ["超人俄里翁","超人熊"],
    1273: ["曼德里卡多","大老师","曼德利"],
    1274: ["欧罗巴","祖奶奶"],
    1275: ["杨贵妃","杨玉环"],
    1276: ["清少纳言","Switch","VTB"],
    1277: ["奥德修斯","假面骑士"],
    1278: ["狄俄斯库里","双子座","内田骨科"],
    1280: ["罗穆路斯=奎里努斯","神祖"],
    1281: ["旅行者","小王子"],
    1282: ["鬼女红叶","恐龙","红叶"],
    1283: ["宇津见绘里世","14岁","绘里世","爱丽瑟"],
    1284: ["阿尔托利雅(caster)","Caber","c呆"],
    1285: ["杀生院祈荒(水着)","水杀生院","人鱼","泳装杀生院"],
    1286: ["伊莉雅丝菲尔·冯·爱因兹贝伦(水着)","泳装伊莉雅","泳装伊利亚"],
    1287: ["布伦希尔德(水着)","泳装布姐"],
    1288: ["虞美人(水着)","水鱼","泳装虞姬"],
    1289: ["阿比盖尔·威廉姆斯〔夏〕","泳装阿比"],
    1290: ["巴御前(水着)","泳装巴御前"],
    1291: ["紫式部(水着)","水紫奶","泳装紫式部"],

}