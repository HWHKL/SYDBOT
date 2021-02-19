'''公主连接Re:dive的游戏数据'''


'''角色名称

遵照格式： id: [台服官译简体, 日文原名, 英文名(罗马音), B服官译, 常见别称, 带错别字的别称等] （<-依此顺序）
若暂无台服官译则用日文原名占位，台日用全角括号，英文用半角括号
'''
CHARA_NAME = {
    1000: ["未知角色", "未知キャラ", "Unknown"],
    1001: ["日和", "ヒヨリ", "Hiyori", "日和莉", "猫拳", "🐱👊"],
    1002: ["优衣", "ユイ", "Yui", "种田", "普田", "由衣", "结衣", "ue", "↗↘↗↘"],
    1003: ["怜", "レイ", "Rei", "剑圣", "普怜", "伶"],
    1004: ["禊", "ミソギ", "Misogi", "未奏希", "炸弹", "炸弹人", "💣"],
    1005: ["茉莉", "マツリ", "Matsuri", "跳跳虎", "老虎", "虎", "🐅"],
    1006: ["茜里", "アカリ", "Akari", "妹法", "妹妹法"],
    1007: ["宫子", "ミヤコ", "Miyako", "布丁", "布", "🍮"],
    1008: ["雪", "ユキ", "Yuki", "小雪", "镜子", "镜法", "伪娘", "男孩子", "男孩纸"],
    1009: ["杏奈", "アンナ", "Anna", "中二", "煤气罐"],
    1010: ["真步", "マホ", "Maho", "狐狸", "真扎", "咕噜灵波", "真布", "🦊"],
    1011: ["璃乃", "リノ", "Rino", "妹弓"],
    1012: ["初音", "ハツネ", "Hatsune", "hego", "星法", "星星法", "⭐法", "睡法"],
    1013: ["七七香", "ナナカ", "Nanaka", "娜娜卡", "77k", "77香"],
    1014: ["霞", "カスミ", "Kasumi", "香澄", "侦探", "杜宾犬", "驴", "驴子", "🔍"],
    1015: ["美里", "ミサト", "Misato", "圣母"],
    1016: ["铃奈", "スズナ", "Suzuna", "暴击弓", "暴弓", "爆击弓", "爆弓", "政委"],
    1017: ["香织", "カオリ", "Kaori", "琉球犬", "狗子", "狗", "狗拳", "🐶", "🐕", "🐶👊🏻", "🐶👊"],
    1018: ["伊绪", "イオ", "Io", "老师", "魅魔"],

    1020: ["美美", "ミミ", "Mimi", "兔子", "兔兔", "兔剑", "萝卜霸断剑", "人参霸断剑", "天兔霸断剑", "🐇", "🐰"],
    1021: ["胡桃", "クルミ", "Kurumi", "铃铛", "🔔"],
    1022: ["依里", "ヨリ", "Yori", "姐法", "姐姐法"],
    1023: ["绫音", "アヤネ", "Ayane", "熊锤", "🐻🔨", "🐻"],

    1025: ["铃莓", "スズメ", "Suzume", "女仆", "妹抖"],
    1026: ["铃", "リン", "Rin", "松鼠", "🐿", "🐿️"],
    1027: ["惠理子", "エリコ", "Eriko", "病娇"],
    1028: ["咲恋", "サレン", "Saren", "充电宝", "青梅竹马", "幼驯染", "院长", "园长", "🔋", "普电"],
    1029: ["望", "ノゾミ", "Nozomi", "偶像", "小望", "🎤"],
    1030: ["妮诺", "ニノン", "Ninon", "妮侬", "扇子"],
    1031: ["忍", "シノブ", "Shinobu", "普忍", "鬼父", "💀"],
    1032: ["秋乃", "アキノ", "Akino", "哈哈剑"],
    1033: ["真阳", "マヒル", "Mahiru", "奶牛", "🐄", "🐮", "真☀"],
    1034: ["优花梨", "ユカリ", "Yukari", "由加莉", "黄骑", "酒鬼", "奶骑", "圣骑", "🍺", "🍺👻"],

    1036: ["镜华", "キョウカ", "Kyouka", "小仓唯", "xcw", "小苍唯", "8岁", "八岁", "喷水萝", "八岁喷水萝", "8岁喷水萝"],
    1037: ["智", "トモ", "Tomo", "卜毛"],
    1038: ["栞", "シオリ", "Shiori", "tp弓", "小栞", "白虎弓", "白虎妹"],

    1040: ["碧", "アオイ", "Aoi", "香菜", "香菜弓", "绿毛弓", "毒弓", "绿帽弓", "绿帽"],

    1042: ["千歌", "チカ", "Chika", "绿毛奶"],
    1043: ["真琴", "マコト", "Makoto", "狼", "🐺", "月月", "朋", "狼姐"],
    1044: ["伊莉亚", "イリヤ", "Iriya", "伊利亚", "伊莉雅", "伊利雅", "yly", "吸血鬼", "那个女人"],
    1045: ["空花", "クウカ", "Kuuka", "抖m", "抖"],
    1046: ["珠希", "タマキ", "Tamaki", "猫剑", "🐱剑", "🐱🗡️"],
    1047: ["纯", "ジュン", "Jun", "黑骑", "saber"],
    1048: ["美冬", "ミフユ", "Mifuyu", "子龙", "赵子龙"],
    1049: ["静流", "シズル", "Shizuru", "姐姐"],
    1050: ["美咲", "ミサキ", "Misaki", "大眼", "👀", "👁️", "👁"],
    1051: ["深月", "ミツキ", "Mitsuki", "眼罩", "抖s"],
    1052: ["莉玛", "リマ", "Rima", "Lima", "草泥马", "羊驼", "🦙", "🐐"],
    1053: ["莫妮卡", "モニカ", "Monika", "毛二力"],
    1054: ["纺希", "ツムギ", "Tsumugi", "裁缝", "蜘蛛侠", "🕷️", "🕸️"],
    1055: ["步未", "アユミ", "Ayumi", "步美", "路人", "路人妹"],
    1056: ["流夏", "ルカ", "Ruka", "大姐", "大姐头", "儿力", "luka", "刘夏"],
    1057: ["吉塔", "ジータ", "Jiita", "姬塔", "团长", "吉他", "🎸", "骑空士", "qks"],
    1058: ["贪吃佩可", "ペコリーヌ", "Pecoriinu", "佩可莉姆", "吃货", "佩可", "公主", "饭团", "🍙"],
    1059: ["可可萝", "コッコロ", "Kokkoro", "可可罗", "妈", "普白"],
    1060: ["凯留", "キャル", "Kyaru", "凯露", "百地希留耶", "希留耶", "Kiruya", "黑猫", "臭鼬", "普黑", "接头霸王", "街头霸王"],
    1061: ["矛依未", "ムイミ", "Muimi", "诺维姆", "Noemu", "夏娜", "511", "无意义", "天楼霸断剑"],

    1063: ["亚里莎", "アリサ", "Arisa", "鸭梨瞎", "瞎子", "亚里沙", "鸭梨傻", "亚丽莎", "亚莉莎", "瞎子弓", "🍐🦐", "yls"],

    1065: ["嘉夜", "カヤ", "Kaya", "憨憨龙", "龙拳", "🐲👊🏻", "🐉👊🏻", "接龙笨比"],
    1066: ["祈梨", "イノリ", "Inori", "梨老八", "李老八"],
    1067: ["穗希", "ホマレ", "Homare"],
    1068: ["拉比林斯达", "ラビリスタ", "Rabirisuta", "迷宫女王", "模索路晶", "模索路", "晶", "王晶"],
    1069: ["真那", "マナ", "Mana", "霸瞳皇帝", "千里真那", "千里", "霸瞳", "霸铜"],
    1070: ["似似花", "ネネカ", "Neneka", "变貌大妃", "现士实似似花", "現士実似々花", "現士実", "现士实", "nnk", "448", "捏捏卡", "变貌", "大妃"],
    1071: ["克莉丝提娜", "クリスティーナ", "Kurisutiina", "誓约女君", "克莉丝提娜·摩根", "Christina", "Cristina", "克总", "女帝", "克", "摩根"],
    1072: ["可萝爹", "長老", "Chourou", "岳父", "爷爷"],
    1073: ["拉基拉基", "ラジニカーント", "Rajinigaanto", "跳跃王", "Rajiraji", "Lajilaji", "垃圾垃圾", "教授"],

    1075: ["贪吃佩可(夏日)", "ペコリーヌ(サマー)", "Pekoriinu(Summer)", "佩可莉姆(夏日)", "水吃", "水饭", "水吃货", "水佩可", "水公主", "水饭团", "水🍙", "泳吃", "泳饭", "泳吃货", "泳佩可", "泳公主", "泳饭团", "泳🍙", "泳装吃货", "泳装公主", "泳装饭团", "泳装🍙", "佩可(夏日)", "🥡", "👙🍙", "泼妇"],
    1076: ["可可萝(夏日)", "コッコロ(サマー)", "Kokkoro(Summer)", "水白", "水妈", "水可", "水可可", "水可可萝", "水可可罗", "泳装妈", "泳装可可萝", "泳装可可罗"],
    1077: ["铃莓(夏日)", "スズメ(サマー)", "Suzume(Summer)", "水女仆", "水妹抖"],
    1078: ["凯留(夏日)", "キャル(サマー)", "Kyaru(Summer)", "水黑", "水黑猫", "水臭鼬", "泳装黑猫", "泳装臭鼬", "潶", "溴", "💧黑"],
    1079: ["珠希(夏日)", "タマキ(サマー)", "Tamaki(Summer)", "水猫剑", "水猫", "渵", "💧🐱🗡️", "水🐱🗡️"],
    1080: ["美冬(夏日)", "ミフユ(サマー)", "Mifuyu(Summer)", "水子龙", "水美冬"],
    1081: ["忍(万圣节)", "シノブ(ハロウィン)", "Shinobu(Halloween)", "万圣忍", "瓜忍", "🎃忍", "🎃💀"],
    1082: ["宫子(万圣节)", "ミヤコ(ハロウィン)", "Miyako(Halloween)", "万圣宫子", "万圣布丁", "狼丁", "狼布丁", "万圣🍮", "🐺🍮", "🎃🍮", "👻🍮"],
    1083: ["美咲(万圣节)", "ミサキ(ハロウィン)", "Misaki(Halloween)", "万圣美咲", "万圣大眼", "瓜眼", "🎃眼", "🎃👀", "🎃👁️", "🎃👁"],
    1084: ["千歌(圣诞节)", "チカ(クリスマス)", "Chika(Xmas)", "圣诞千歌", "圣千", "蛋鸽", "🎄💰🎶", "🎄千🎶", "🎄1000🎶"],
    1085: ["胡桃(圣诞节)", "クルミ(クリスマス)", "Kurumi(Xmas)", "圣诞胡桃", "圣诞铃铛"],
    1086: ["绫音(圣诞节)", "アヤネ(クリスマス)", "Ayane(Xmas)", "圣诞熊锤", "蛋锤", "圣锤", "🎄🐻🔨", "🎄🐻"],
    1087: ["日和(新年)", "ヒヨリ(ニューイヤー)", "Hiyori(NewYear)", "新年日和", "春猫", "👘🐱"],
    1088: ["优衣(新年)", "ユイ(ニューイヤー)", "Yui(NewYear)", "新年优衣", "春田", "新年由衣"],
    1089: ["怜(新年)", "レイ(ニューイヤー)", "Rei(NewYear)", "春剑", "春怜", "春伶", "新春剑圣", "新年怜", "新年剑圣"],
    1090: ["惠理子(情人节)", "エリコ(バレンタイン)", "Eriko(Valentine)", "情人节病娇", "恋病", "情病", "恋病娇", "情病娇"],
    1091: ["静流(情人节)", "シズル(バレンタイン)", "Shizuru(Valentine)", "情人节静流", "情姐", "情人节姐姐"],
    1092: ["安", "アン", "An", "胖安", "55kg"],
    1093: ["露", "ルゥ", "Ruu", "逃课女王"],
    1094: ["古蕾娅", "グレア", "Gurea", "龙姬", "古雷娅", "古蕾亚", "古雷亚", "🐲🐔", "🐉🐔"],
    1095: ["空花(大江户)", "クウカ(オーエド)", "Kuuka(Ooedo)", "江户空花", "江户抖m", "江m", "花m", "江花"],
    1096: ["妮诺(大江户)", "ニノン(オーエド)", "Ninon(Ooedo)", "江户扇子", "忍扇"],
    1097: ["雷姆", "レム", "Remu", "蕾姆"],
    1098: ["拉姆", "ラム", "Ramu"],
    1099: ["爱蜜莉雅", "エミリア", "Emiria", "艾米莉亚", "emt"],
    1100: ["铃奈(夏日)", "スズナ(サマー)", "Suzuna(Summer)", "瀑击弓", "水爆", "水爆弓", "水暴", "瀑", "水暴弓", "瀑弓", "泳装暴弓", "泳装爆弓"],
    1101: ["伊绪(夏日)", "イオ(サマー)", "Io(Summer)", "水魅魔", "水老师", "泳装魅魔", "泳装老师"],
    1103: ["咲恋(夏日)", "サレン(サマー)", "Saren(Summer)", "水电", "泳装充电宝", "泳装咲恋", "水着咲恋", "水电站", "水电宝", "水充", "👙🔋"],
    1104: ["真琴(夏日)", "マコト(サマー)", "Makoto(Summer)", "水狼", "浪", "水🐺", "泳狼", "泳月", "泳月月", "泳朋", "水月", "水月月", "水朋", "👙🐺"],
    1105: ["香织(夏日)", "カオリ(サマー)", "Kaori(Summer)", "水狗", "泃", "水🐶", "水🐕", "泳狗"],
    1106: ["真步(夏日)", "マホ(サマー)", "Maho(Summer)", "水狐狸", "水狐", "水壶", "水真步", "水maho", "氵🦊", "水🦊", "💧🦊"],
    1107: ["碧(插班生)", "アオイ(編入生)", "Aoi(Hennyuusei)", "生菜", "插班碧"],
    1108: ["克萝依", "クロエ", "Kuroe", "华哥", "黑江", "黑江花子", "花子"],
    1109: ["琪爱儿", "チエル", "Chieru", "切露", "茄露", "茄噜", "切噜"],
    1110: ["优妮", "ユニ", "Yuni", "真行寺由仁", "由仁", "u2", "优妮辈先", "辈先", "书记", "uni", "先辈", "仙贝", "油腻", "优妮先辈", "学姐", "18岁黑丝学姐"],
    1111: ["镜华(万圣节)", "キョウカ(ハロウィン)", "Kyouka(Halloween)", "万圣镜华", "万圣小仓唯", "万圣xcw", "猫仓唯", "黑猫仓唯", "mcw", "猫唯", "猫仓", "喵唯"],
    1112: ["禊(万圣节)", "ミソギ(ハロウィン)", "Misogi(Halloween)", "万圣禊", "万圣炸弹人", "瓜炸弹人", "万圣炸弹", "万圣炸", "瓜炸", "南瓜炸", "🎃💣"],
    1113: ["美美(万圣节)", "ミミ(ハロウィン)", "Mimi(Halloween)", "万圣兔", "万圣兔子", "万圣兔兔", "绷带兔", "绷带兔子", "万圣美美", "绷带美美", "万圣🐰", "绷带🐰", "🎃🐰", "万圣🐇", "绷带🐇", "🎃🐇"],
    1114: ["露娜", "ルナ", "Runa", "露仓唯", "露cw"],
    1115: ["克莉丝提娜(圣诞节)", "クリスティーナ(クリスマス)", "Kurisutiina(Xmas)", "Christina(Xmas)", "Cristina(Xmas)", "圣诞克", "圣诞克总", "圣诞女帝", "蛋克", "圣克", "必胜客"],
    1116: ["望(圣诞节)", "ノゾミ(クリスマス)", "Nozomi(Xmas)", "圣诞望", "圣诞偶像", "蛋偶像", "蛋望"],
    1117: ["伊莉亚(圣诞节)", "イリヤ(クリスマス)", "Iriya(Xmas)", "圣诞伊莉亚", "圣诞伊利亚", "圣诞伊莉雅", "圣诞伊利雅", "圣诞yly", "圣诞吸血鬼", "圣伊", "圣yly"],

    1119: ["可可萝(新年)", "コッコロ(ニューイヤー)", "Kokkoro(NewYear)", "春可可", "春白", "新年妈", "春妈"],
    1120: ["凯留(新年)", "キャル(ニューイヤー)", "Kyaru(NewYear)", "春凯留", "春黑猫", "春黑", "春臭鼬", "新年凯留", "新年黑猫", "新年臭鼬", "唯一神"],
    1121: ["铃莓(新年)", "スズメ(ニューイヤー)", "Suzume(NewYear)", "春铃莓", "春女仆", "春妹抖", "新年铃莓", "新年女仆", "新年妹抖"],
    1122: ["霞(魔法少女)", "カスミ(マジカル)", "Kasumi(MagiGirl)", "魔法少女霞", "魔法侦探", "魔法杜宾犬", "魔法驴", "魔法驴子", "魔驴", "魔法霞", "魔法少驴"],
    1123: ["栞(魔法少女)", "シオリ(マジカル)", "Shiori(MagiGirl)", "魔法少女栞", "魔法tp弓", "魔法小栞", "魔法白虎弓", "魔法白虎妹", "魔法白虎", "魔栞"],
    1124: ["卯月(偶像大师)", "ウヅキ(デレマス)", "Udsuki(DEREM@S)", "卯月", "卵用", "Udsuki(DEREMAS)", "岛村卯月"],
    1125: ["凛(偶像大师)", "リン(デレマス)", "Rin(DEREM@S)", "凛", "Rin(DEREMAS)", "涩谷凛", "西部凛"],
    1126: ["未央(偶像大师)", "ミオ(デレマス)", "Mio(DEREM@S)", "未央", "Mio(DEREMAS)", "本田未央"],
    1127: ["铃(游侠)", "リン(レンジャー)", "Rin(Ranger)", "骑兵松鼠", "游侠松鼠", "游骑兵松鼠", "护林员松鼠", "护林松鼠", "游侠🐿️", "武松"],
    1128: ["真阳(游侠)", "マヒル(レンジャー)", "Mahiru(Ranger)", "骑兵奶牛", "游侠奶牛", "游骑兵奶牛", "护林员奶牛", "护林奶牛", "游侠🐄", "游侠🐮"],
    1129: ["璃乃(奇境)", "リノ(ワンダー)", "Rino(Wonder)", "璃乃(仙境)", "爽弓", "爱丽丝弓", "爱弓", "兔弓", "奇境妹弓", "仙境妹弓", "白丝妹弓"],
    1130: ["步未(奇境)", "アユミ(ワンダー)", "Ayumi(Wonder)", "步未(仙境)", "路人兔", "兔人妹", "爱丽丝路人", "奇境路人", "仙境路人"],
    1131: ["流夏(夏日)", "ルカ(サマー)", "Ruka(Summer)", "泳装流夏", "水流夏", "泳装刘夏", "水刘夏", "泳装大姐", "泳装大姐头", "水大姐", "水大姐头", "水儿力", "泳装儿力", "水流"],
    1132: ["杏奈(夏日)", "アンナ(サマー)", "Anna(Summer)", "泳装中二", "泳装煤气罐", "水中二", "水煤气罐", "冲", "冲二"],
    1133: ["七七香(夏日)", "ナナカ(サマー)", "Nanaka(Summer)", "泳装娜娜卡", "泳装77k", "泳装77香", "水娜娜卡", "水77k", "水77香", "水nnk","水七七香"],
    1134: ["初音(夏日)", "ハツネ(サマー)", "Hatsune(Summer)", "水星", "海星", "水hego", "水星法", "泳装星法", "水⭐法", "水睡法", "湦"],
    1135: ["美里(夏日)", "ミサト(サマー)", "Misato(Summer)", "水母", "泳装圣母", "水圣母"],
    1136: ["纯(夏日)", "ジュン(サマー)", "Jun(Summer)", "泳装黑骑", "水黑骑", "泳装纯", "水纯", "小次郎"],
    1137: ["茜里(天使)", "アカリ(エンジェル)", "Akari(Angel)", "天使妹法", "天使茜里", "丘比特妹法"],
    1138: ["依里(天使)", "ヨリ(エンジェル)", "Yori(Angel)", "天使姐法", "天使依里", "丘比特姐法"],
    1139: ["纺希(万圣节)", "ツムギ(ハロウィン)", "Tsumugi(Halloween)", "万圣裁缝", "万圣蜘蛛侠", "🎃🕷️", "🎃🕸️", "万裁", "瓜裁", "鬼裁", "鬼才"],
    1140: ["怜(万圣节)", "レイ(ハロウィン)", "Rei(Halloween)", "万圣剑圣", "万剑", "瓜剑", "瓜怜", "万圣怜"],
    1141: ["茉莉(万圣节)", "マツリ(ハロウィン)", "Matsuri(Halloween)", "万圣跳跳虎", "万圣老虎", "瓜虎", "🎃🐅"],
    1142: ["莫妮卡(魔法少女)", "モニカ(マジカル)", "魔法少女莫妮卡", "魔二力"],
    1143: ["智(魔法少女)", "トモ(マジカル)", "魔法少女智", "琪露诺", "9智", "⑨"],
    1144: ["秋乃(圣诞节)", "アキノ(クリスマス)", "Akino(Xmas)", "圣剑", "生煎", "圣诞哈哈剑", "哈哈剑(圣诞节)", "圣哈", "蛋哈", "蛋剑"],
    1145: ["咲恋(圣诞节)", "サレン(クリスマス)", "Saren(Xmas)", "圣诞充电宝", "圣电", "圣诞咲恋"],
    1146: ["优花梨(圣诞节)", "ユカリ(クリスマス)", "Yukari(Xmas)", "蛋黄", "由加莉(圣诞节)", "圣诞黄骑", "圣诞圣骑", "蛋骑", "黄骑(圣诞节)"],
    1147: ["矛依未(新年)", "ムイミ（ニューイヤー）", "春511", "新春511", "新年511"],
    1150: ["似似花(新年)", "春nnk", "春似似花", "春妃", "新年nnk", "新春nnk",],
    # =================================== #
    1155: ["可可萝(仪装束)","コッコロ(儀装束)","礼妈","礼仪妈","礼服妈","姨妈"],
    1156: ["优衣(仪装束)","ユイ(儀装束)","礼优衣","礼仪优衣","礼服优衣","礼田","礼装优衣"],
    1701: ["环奈","桥本环奈","毛大力"],
    1702: ["环奈(振袖)","新春环奈","振袖环奈","春环"],
    1801: ["日和(公主)", "ヒヨリ（プリンセス）","公主猫拳","fes猫拳"],
    1802: ["优衣(公主)", "ユイ(プリンセス)", "Yui(Princess)", "公主优衣", "公主yui", "公主种田", "公主田", "公主ue", "掉毛优衣", "掉毛yui", "掉毛ue", "掉毛", "飞翼优衣", "飞翼ue", "飞翼", "飞翼高达"],

    1804: ["贪吃佩可(公主)", "ペコリーヌ(プリンセス)", "Pekoriinu(Princess)", "公主吃", "公主饭", "公主吃货", "公主佩可", "公主饭团", "公主🍙", "命运高达", "高达", "命运公主", "高达公主", "命吃", "春哥高达", "🤖🍙", "🤖"],
    1805: ["可可萝(公主)", "コッコロ（プリンセス）", "Kokkoro(Princess)", "公主妈", "月光妈", "蝶妈", "蝴蝶妈", "月光蝶妈", "公主可", "公主可萝", "公主可可萝", "月光可", "月光可萝", "月光可可萝", "蝶可", "蝶可萝", "蝶可可萝"],




    # =================================== #Yozi
    
    1523: ["朝武芳乃","芳乃"],
	1524: ["常陆茉子","茉子"],
    1525: ["丛雨","幼刀"],
	1526: ["蕾娜·列支敦瑙尔","蕾娜"],
	1527: ["鞍马小春","小春"],
    1528: ["马庭芦花","芦花","芦花姐"],
	1529: ["明月栞那","栞那"],
	1530: ["四季夏目","夏目"],
	1531: ["墨染希"],
	1532: ["火打谷爱衣","爱衣"],
	1533: ["汐山凉音","凉音"],
	1534: ["绫地宁宁","宁宁"],
	1535: ["因幡爱瑠","爱瑠"],
	1536: ["椎叶䌷"],
	1537: ["户隐憧子","憧子"],
	1538: ["仮屋和奏","和奏"],
	1539: ["三司绫濑","绫濑"],
	1540: ["在原七海","七海"],
	1541: ["式部茉优","茉优"],
	1542: ["二条院羽月","羽月"],
	1543: ["壬生千咲","千咲"],

# =================================== #bangdream
    1601: ["丸山彩","aya","彩","彩彩","修哇修哇"],
    1602: ["弦卷心","弦巻こころ","kkr","kokoro","心","扣扣肉"],
    1603: ["冰川日菜","hina","日菜","永州白菜"],
    1604: ["户山香澄","cdd","ksm","dd"],
    1605: ["花园多惠","花園たえ","otae","花园多英","おたえ","tae","tea","多惠"],
    1606: ["牛込里美","牛込りみ","里美","りみりん","rimi","李美丽","巧克力螺"],
    1607: ["山吹沙绫","沙绫","saya","Saaya","发酵少女"],
    1608: ["市谷有咲","有咲","ars","秋妈妈"],
    1609: ["白鹭千圣","千圣","cst","小千"],
    1610: ["大和麻弥","maya","呼嘿嘿","哦吼吼","弥麻和大"],
    1611: ["若宫伊芙","若宮イブ","伊布","ibu","武士道"],
    1612: ["美竹兰","兰","ran","lan","巴巴恩波神"],
    1613: ["宇田川巴","巴","tomoe","soiya","ソイヤ"],
    1614: ["上原绯玛丽","上原ひまり","绯玛丽","himari","hmr","小绯","肥玛丽"],
    1615: ["青叶摩卡","青葉モカ","moka","摩卡","毛力"],
    1616: ["羽泽鸫","羽沢つぐみ","鸫","tsugu","tsugumi","茨菇","tgm"],
    1617: ["湊友希那","yukina","ykn","友希那","湊女人","憋笑企鹅","摔角手aiai"],
    1618: ["冰川纱夜","sayo","纱夜","薯条妹","本质谐星","琴行老板"],
    1619: ["今井莉莎","今井リサ","risa","lisa","莉莎","锂砂镍"],
    1620: ["白金燐子","燐子","燐燐","rinrin","りんりん","提词姬","......"],
    1621: ["宇田川亚子","宇田川あこ","亚子","ako"],
    1622: ["松原花音","花音","kanon","卡农","迷宫水母"],
    1623: ["奥泽美咲","奥沢美咲""msk","米歇尔","苦劳人","ミッシェル"],
    1624: ["北泽育美","北沢はぐみ","育美","hagumi","hgm","はぐ","星空凛"],
    1625: ["濑田薰","瀬田薫","薰","kaoru","薰哥","哈卡奈","哈卡乃","儚い"],
    1626: ["仓田真白","倉田ましろ","真白","mashiro","msr"],
    1627: ["桐谷透子","桐ケ谷透子","透子","touko"],
    1628: ["广町七深","広町七深","七深","nanami","丸三彩"],
    1629: ["二叶筑紫","二葉つくし","筑紫","tsukushi","二叶土笔","二爷柱子"],
    1630: ["八潮瑠唯","rui","瑠唯","るいるい","道理轰炸机","600W"],
    1631: ["朝日六花","六花","rokka","lock","六六","吉他狂战士"],
    1632: ["佐藤益木","佐藤ますき","益木","masuki","masking","キング","king"],
    1633: ["鳰原令王那","令王那","reona","pareo","パレオ","忠犬PARE公","暗黑丸山彩"],
    1634: ["和奏瑞依","和奏レイ","瑞依","LAYER"],
    1635: ["珠手知由","珠手ちゆ","知由","CHU²","chuchu","チュチ","小矮子革命儿","chu平方"],





































# =================================== #blhx

    6000: ['卡辛','卡辛a','卡辛b'],
    6001: ['唐斯','唐斯a','唐斯b'],
    6002: ['克雷文','克雷文a','克雷文b'],
    6003: ['麦考尔','麦考尔a','麦考尔b'],
    6004: ['奥利克','奥利克a','奥利克b'],
    6005: ['富特','富特a','富特b'],
    6006: ['斯彭斯','斯彭斯a','斯彭斯b'],
    6007: ['小猎兔犬','小猎兔犬a','小猎兔犬b'],
    6008: ['大斗犬','大斗犬a','大斗犬b'],
    6009: ['彗星','彗星a','彗星b'],
    6010: ['新月','新月a','新月b'],
    6011: ['小天鹅','小天鹅a','小天鹅b'],
    6012: ['狐提','狐提a','狐提b'],
    6013: ['不知火','不知火a','不知火b'],
    6014: ['Z20','Z20a','Z20b'],
    6015: ['Z21','Z21a','Z21b'],
    6016: ['睦月','睦月a','睦月b'],
    6017: ['如月','如月a','如月b'],
    6018: ['卯月a','卯月b'],
    6019: ['水无月','水无月a','水无月b'],
    6020: ['三日月','三日月a','三日月b'],
    6021: ['杜威','杜威a','杜威b'],
    6022: ['格里德利','格里德利a','格里德利b'],
    6023: ['弗莱彻','弗莱彻a','弗莱彻b'],
    6024: ['撒切尔','撒切尔a','撒切尔b'],
    6025: ['本森','本森a','本森b'],
    6026: ['西姆斯','西姆斯a','西姆斯b'],
    6027: ['哈曼','哈曼a','哈曼b'],
    6028: ['女将','女将a','女将b'],
    6029: ['阿卡司塔','阿卡司塔a','阿卡司塔b'],
    6030: ['热心','热心a','热心b'],
    6031: ['命运女神','命运女神a','命运女神b'],
    6032: ['猎人','猎人a','猎人b'],
    6033: ['天后','天后a','天后b'],
    6034: ['晓','晓a','晓b'],
    6035: ['雷','雷a','雷b'],
    6036: ['电','电a','电b'],
    6037: ['白露','白露a','白露b'],
    6038: ['阳炎','阳炎a','阳炎b'],
    6039: ['初春','初春a','初春b'],
    6040: ['若叶','若叶a','若叶b'],
    6041: ['初霜','初霜a','初霜b'],
    6042: ['有明','有明a','有明b'],
    6043: ['夕暮','夕暮a','夕暮b'],
    6044: ['黑潮','黑潮a','黑潮b'],
    6045: ['亲潮','亲潮a','亲潮b'],
    6046: ['贝利','贝利a','贝利b'],
    6047: ['Z19','Z19a','Z19b'],
    6048: ['神风','神风a','神风b'],
    6049: ['松风','松风a','松风b'],
    6050: ['文月','文月a','文月b'],
    6051: ['长月','长月a','长月b'],
    6052: ['清波','清波a','清波b'],
    6053: ['拉德福特','拉德福特a','拉德福特b'],
    6054: ['杰金斯','杰金斯a','杰金斯b'],
    6055: ['丘比特','丘比特a','丘比特b'],
    6056: ['泽西','泽西a','泽西b'],
    6057: ['浦风','浦风a','浦风b'],
    6058: ['矶风','矶风a','矶风b'],
    6059: ['滨风','滨风a','滨风b'],
    6060: ['谷风','谷风a','谷风b'],
    6061: ['朝潮','朝潮a','朝潮b'],
    6062: ['大潮','大潮a','大潮b'],
    6063: ['满潮','满潮a','满潮b'],
    6064: ['荒潮','荒潮a','荒潮b'],
    6065: ['Z18','Z18a','Z18b'],
    6066: ['福尔班','福尔班a','福尔班b'],
    6067: ['勒马尔','勒马尔a','勒马尔b'],
    6068: ['布什','布什a','布什b'],
    6069: ['霍比','霍比a','霍比b'],
    6070: ['科尔克','科尔克a','科尔克b'],
    6071: ['黑泽伍德','黑泽伍德a','黑泽伍德b'],
    6072: ['旗风','旗风a','旗风b'],
    6073: ['金伯利','金伯利a','金伯利b'],
    6074: ['回声','回声a','回声b'],
    6075: ['艾尔温','艾尔温a','艾尔温b'],
    6076: ['贝奇','贝奇a','贝奇b'],
    6077: ['斯坦利','斯坦利a','斯坦利b'],
    6078: ['斯莫利','斯莫利a','斯莫利b'],
    6079: ['哈尔西·鲍威尔','哈尔西·鲍威尔a','哈尔西·鲍威尔b'],
    6080: ['泛用型布里','泛用型布里a','泛用型布里b'],
    6081: ['莫里','莫里a','莫里b'],
    6082: ['查尔斯·奥斯本','查尔斯·奥斯本a','查尔斯·奥斯本b'],
    6083: ['拉菲','拉菲a','拉菲b'],
    6084: ['格伦维尔','格伦维尔a','格伦维尔b'],
    6085: ['萤火虫','萤火虫a','萤火虫b'],
    6086: ['勇敢','勇敢a','勇敢b'],
    6087: ['标枪','标枪a','标枪b'],
    6088: ['吸血鬼a','吸血鬼b'],
    6089: ['吹雪','吹雪a','吹雪b'],
    6090: ['绫波','绫波a','绫波b'],
    6091: ['响','响a','响b'],
    6092: ['时雨','时雨a','时雨b'],
    6093: ['野分','野分a','野分b'],
    6094: ['Z1','Z1a','Z1b'],
    6095: ['Z23','Z23a','Z23b'],
    6096: ['Z25','Z25a','Z25b'],
    6097: ['鞍山','鞍山a','鞍山b'],
    6098: ['抚顺','抚顺a','抚顺b'],
    6099: ['长春','长春a','长春b'],
    6100: ['太原','太原a','太原b'],
    6101: ['新月JP','新月JPa','新月JPb'],
    6102: ['春月','春月a','春月b'],
    6103: ['宵月','宵月a','宵月b'],
    6104: ['尼古拉斯','尼古拉斯a','尼古拉斯b'],
    6105: ['无敌','无敌a','无敌b'],
    6106: ['火枪手','火枪手a','火枪手b'],
    6107: ['Z35','Z35a','Z35b'],
    6108: ['鲁莽','鲁莽a','鲁莽b'],
    6109: ['卷波','卷波a','卷波b'],
    6110: ['马拉尼','马拉尼a','马拉尼b'],
    6111: ['Z2','Z2a','Z2b'],
    6112: ['Z36','Z36a','Z36b'],
    6113: ['倔强','倔强a','倔强b'],
    6114: ['龙骑兵','龙骑兵a','龙骑兵b'],
    6115: ['霞a','霞b'],
    6116: ['浦波','浦波a','浦波b'],
    6117: ['威严','威严a','威严b'],
    6118: ['明斯克','明斯克a','明斯克b'],
    6119: ['库珀','库珀a','库珀b'],
    6120: ['花月','花月a','花月b'],
    6121: ['长波','长波a','长波b'],
    6122: ['塔尔图','塔尔图a','塔尔图b'],
    6123: ['爱斯基摩人','爱斯基摩人a','爱斯基摩人b'],
    6124: ['伊卡洛斯','伊卡洛斯a','伊卡洛斯b'],
    6125: ['Z26','Z26a','Z26b'],
    6126: ['试作型布里MKII','试作型布里MKIIa','试作型布里MKIIb'],
    6127: ['埃尔德里奇','埃尔德里奇a','埃尔德里奇b'],
    6128: ['夕立','夕立a','夕立b'],
    6129: ['雪风','雪风a','雪风b'],
    6130: ['Z46','Z46a','Z46b'],
    6131: ['江风','江风a','江风b'],
    6132: ['凯旋','凯旋a','凯旋b'],
    6133: ['恶毒','恶毒a','恶毒b'],
    6134: ['塔什干','塔什干a','塔什干b'],
    6135: ['凉月','凉月a','凉月b'],
    6136: ['特装型布里MKIII','特装型布里MKIIIa','特装型布里MKIIIb'],
    6137: ['北风','北风a','北风b'],
    6138: ['布兰','布兰a','布兰b'],
    6139: ['群白之心','群白之心a','群白之心b'],
    6140: ['22','22a','22b'],
    6141: ['33','33a','33b'],
    6142: ['猫音','猫音a','猫音b'],
    6143: ['绊爱','绊爱a','绊爱b'],
    6144: ['奥马哈','奥马哈a','奥马哈b'],
    6145: ['罗利','罗利a','罗利b'],
    6146: ['利安得','利安得a','利安得b'],
    6147: ['长良','长良a','长良b'],
    6148: ['阿武隈','阿武隈a','阿武隈b'],
    6149: ['柯尼斯堡','柯尼斯堡a','柯尼斯堡b'],
    6150: ['卡尔斯鲁厄','卡尔斯鲁厄a','卡尔斯鲁厄b'],
    6151: ['科隆','科隆a','科隆b'],
    6152: ['里士满','里士满a','里士满b'],
    6153: ['布鲁克林','布鲁克林a','布鲁克林b'],
    6154: ['菲尼克斯','菲尼克斯a','菲尼克斯b'],
    6155: ['亚特兰大','亚特兰大a','亚特兰大b'],
    6156: ['朱诺','朱诺a','朱诺b'],
    6157: ['阿基里斯','阿基里斯a','阿基里斯b'],
    6158: ['阿贾克斯','阿贾克斯a','阿贾克斯b'],
    6159: ['南安普顿','南安普顿a','南安普顿b'],
    6160: ['阿瑞托莎','阿瑞托莎a','阿瑞托莎b'],
    6161: ['加拉蒂亚','加拉蒂亚a','加拉蒂亚b'],
    6162: ['五十铃','五十铃a','五十铃b'],
    6163: ['莱比锡','莱比锡a','莱比锡b'],
    6164: ['火奴鲁鲁','火奴鲁鲁a','火奴鲁鲁b'],
    6165: ['川内','川内a','川内b'],
    6166: ['那珂','那珂a','那珂b'],
    6167: ['斐济','斐济a','斐济b'],
    6168: ['牙买加','牙买加a','牙买加b'],
    6169: ['孟菲斯','孟菲斯a','孟菲斯b'],
    6170: ['纽卡斯尔','纽卡斯尔a','纽卡斯尔b'],
    6171: ['康克德','康克德a','康克德b'],
    6172: ['库拉索','库拉索a','库拉索b'],
    6173: ['杓鹬','杓鹬a','杓鹬b'],
    6174: ['圣胡安','圣胡安a','圣胡安b'],
    6175: ['格拉斯哥','格拉斯哥a','格拉斯哥b'],
    6176: ['马布尔黑德','马布尔黑德a','马布尔黑德b'],
    6177: ['海伦娜','海伦娜a','海伦娜b'],
    6178: ['克利夫兰','克利夫兰a','克利夫兰b'],
    6179: ['哥伦比亚','哥伦比亚a','哥伦比亚b'],
    6180: ['谢菲尔德','谢菲尔德a','谢菲尔德b'],
    6181: ['格罗斯特','格罗斯特a','格罗斯特b'],
    6182: ['爱丁堡','爱丁堡a','爱丁堡b'],
    6183: ['欧若拉','欧若拉a','欧若拉b'],
    6184: ['夕张','夕张a','夕张b'],
    6185: ['鬼怒','鬼怒a','鬼怒b'],
    6186: ['最上','最上a','最上b'],
    6187: ['三隈','三隈a','三隈b'],
    6188: ['逸仙','逸仙a','逸仙b'],
    6189: ['宁海','宁海a','宁海b'],
    6190: ['平海','平海a','平海b'],
    6191: ['圣路易斯','圣路易斯a','圣路易斯b'],
    6192: ['神通','神通a','神通b'],
    6193: ['阿贺野','阿贺野a','阿贺野b'],
    6194: ['丹佛','丹佛a','丹佛b'],
    6195: ['小贝法','小贝法a','小贝法b'],
    6196: ['埃米尔·贝尔汀','埃米尔·贝尔汀a','埃米尔·贝尔汀b'],
    6197: ['小海伦娜','小海伦娜a','小海伦娜b'],
    6198: ['小克利夫兰','小克利夫兰a','小克利夫兰b'],
    6199: ['小圣地亚哥','小圣地亚哥a','小圣地亚哥b'],
    6200: ['伯明翰','伯明翰a','伯明翰b'],
    6201: ['黑太子','黑太子a','黑太子b'],
    6202: ['克利夫兰(μ兵装)','克利夫兰(μ兵装)a','克利夫兰(μ兵装)b'],
    6203: ['谢菲尔德(μ兵装)','谢菲尔德(μ兵装)a','谢菲尔德(μ兵装)b'],
    6204: ['比洛克西','比洛克西a','比洛克西b'],
    6205: ['水星纪念','水星纪念a','水星纪念b'],
    6206: ['圣地亚哥','圣地亚哥a','圣地亚哥b'],
    6207: ['黛朵','黛朵a','黛朵b'],
    6208: ['贝尔法斯特','贝尔法斯特a','贝尔法斯特b'],
    6209: ['阿芙乐尔','阿芙乐尔a','阿芙乐尔b'],
    6210: ['能代','能代a','能代b'],
    6211: ['蒙彼利埃','蒙彼利埃a','蒙彼利埃b'],
    6212: ['天狼星','天狼星a','天狼星b'],
    6213: ['确捷','确捷a','确捷b'],
    6214: ['恰巴耶夫','恰巴耶夫a','恰巴耶夫b'],
    6215: ['里诺','里诺a','里诺b'],
    6216: ['赫敏','赫敏a','赫敏b'],
    6217: ['海王星','海王星a','海王星b'],
    6218: ['西雅图','西雅图a','西雅图b'],
    6219: ['美因茨','美因茨a','美因茨b'],
    6220: ['涅普顿','涅普顿a','涅普顿b'],
    6221: ['绀紫之心','绀紫之心a','绀紫之心b'],
    6222: ['露露缇耶','露露缇耶a','露露缇耶b'],
    6223: ['彭萨科拉','彭萨科拉a','彭萨科拉b'],
    6224: ['盐湖城','盐湖城a','盐湖城b'],
    6225: ['古鹰','古鹰a','古鹰b'],
    6226: ['加古','加古a','加古b'],
    6227: ['青叶','青叶a','青叶b'],
    6228: ['衣笠','衣笠a','衣笠b'],
    6229: ['北安普敦','北安普敦a','北安普敦b'],
    6230: ['芝加哥','芝加哥a','芝加哥b'],
    6231: ['波特兰','波特兰a','波特兰b'],
    6232: ['什罗普郡','什罗普郡a','什罗普郡b'],
    6233: ['肯特','肯特a','肯特b'],
    6234: ['萨福克','萨福克a','萨福克b'],
    6235: ['诺福克','诺福克a','诺福克b'],
    6236: ['妙高','妙高a','妙高b'],
    6237: ['那智','那智a','那智b'],
    6238: ['苏塞克斯','苏塞克斯a','苏塞克斯b'],
    6239: ['特伦托','特伦托a','特伦托b'],
    6240: ['休斯敦','休斯敦a','休斯敦b'],
    6241: ['印第安纳波利斯','印第安纳波利斯a','印第安纳波利斯b'],
    6242: ['阿斯托利亚','阿斯托利亚a','阿斯托利亚b'],
    6243: ['昆西','昆西a','昆西b'],
    6244: ['文森斯','文森斯a','文森斯b'],
    6245: ['威奇塔','威奇塔a','威奇塔b'],
    6246: ['伦敦','伦敦a','伦敦b'],
    6247: ['多塞特郡','多塞特郡a','多塞特郡b'],
    6248: ['约克','约克a','约克b'],
    6249: ['埃克塞特','埃克塞特a','埃克塞特b'],
    6250: ['足柄','足柄a','足柄b'],
    6251: ['希佩尔海军上将','希佩尔海军上将a','希佩尔海军上将b'],
    6252: ['德意志','德意志a','德意志b'],
    6253: ['斯佩伯爵海军上将','斯佩伯爵海军上将a','斯佩伯爵海军上将b'],
    6254: ['铃谷','铃谷a','铃谷b'],
    6255: ['希佩尔海军上将(μ兵装)','希佩尔海军上将(μ兵装)a','希佩尔海军上将(μ兵装)b'],
    6256: ['熊野','熊野a','熊野b'],
    6257: ['巴尔的摩','巴尔的摩a','巴尔的摩b'],
    6258: ['高雄','高雄a','高雄b'],
    6259: ['爱宕','爱宕a','爱宕b'],
    6260: ['摩耶','摩耶a','摩耶b'],
    6261: ['鸟海','鸟海a','鸟海b'],
    6262: ['欧根亲王','欧根亲王a','欧根亲王b'],
    6263: ['明尼阿波利斯','明尼阿波利斯a','明尼阿波利斯b'],
    6264: ['扎拉','扎拉a','扎拉b'],
    6265: ['布莱默顿','布莱默顿a','布莱默顿b'],
    6266: ['伊吹','伊吹a','伊吹b'],
    6267: ['罗恩','罗恩a','罗恩b'],
    6268: ['路易九世','路易九世a','路易九世b'],
    6269: ['柴郡','柴郡a','柴郡b'],
    6270: ['德雷克','德雷克a','德雷克b'],
    6271: ['最上改1'],
    6272: ['诺瓦露','诺瓦露a','诺瓦露b'],
    6273: ['圣黑之心','圣黑之心a','圣黑之心b'],
    6274: ['久远','久远a','久远b'],
    6275: ['绊爱·Elegant','绊爱·Eleganta','绊爱·Elegantb'],
    6276: ['吾妻','吾妻a','吾妻b'],
    6277: ['反击','反击a','反击b'],
    6278: ['声望','声望a','声望b'],
    6279: ['金刚','金刚a','金刚b'],
    6280: ['比叡','比叡a','比叡b'],
    6281: ['榛名','榛名a','榛名b'],
    6282: ['雾岛','雾岛a','雾岛b'],
    6283: ['沙恩霍斯特','沙恩霍斯特a','沙恩霍斯特b'],
    6284: ['格奈森瑙','格奈森瑙a','格奈森瑙b'],
    6285: ['敦刻尔克','敦刻尔克a','敦刻尔克b'],
    6286: ['小比叡','小比叡a','小比叡b'],
    6287: ['小声望','小声望a','小声望b'],
    6288: ['胡德','胡德a','胡德b'],
    6289: ['天城','天城a','天城b'],
    6290: ['奥丁','奥丁a','奥丁b'],
    6291: ['内华达','内华达a','内华达b'],
    6292: ['俄克拉荷马','俄克拉荷马a','俄克拉荷马b'],
    6293: ['宾夕法尼亚','宾夕法尼亚a','宾夕法尼亚b'],
    6294: ['田纳西','田纳西a','田纳西b'],
    6295: ['加利福尼亚','加利福尼亚a','加利福尼亚b'],
    6296: ['扶桑','扶桑a','扶桑b'],
    6297: ['山城','山城a','山城b'],
    6298: ['伊势','伊势a','伊势b'],
    6299: ['日向','日向a','日向b'],
    6300: ['加富尔伯爵','加富尔伯爵a','加富尔伯爵b'],
    6301: ['亚利桑那','亚利桑那a','亚利桑那b'],
    6302: ['科罗拉多','科罗拉多a','科罗拉多b'],
    6303: ['马里兰','马里兰a','马里兰b'],
    6304: ['西弗吉尼亚','西弗吉尼亚a','西弗吉尼亚b'],
    6305: ['伊丽莎白女王','伊丽莎白女王a','伊丽莎白女王b'],
    6306: ['纳尔逊','纳尔逊a','纳尔逊b'],
    6307: ['罗德尼','罗德尼a','罗德尼b'],
    6308: ['陆奥','陆奥a','陆奥b'],
    6309: ['朱利奥·凯撒','朱利奥·凯撒a','朱利奥·凯撒b'],
    6310: ['甘古特','甘古特a','甘古特b'],
    6311: ['英勇','英勇a','英勇b'],
    6312: ['北卡罗来纳','北卡罗来纳a','北卡罗来纳b'],
    6313: ['华盛顿','华盛顿a','华盛顿b'],
    6314: ['南达科他','南达科他a','南达科他b'],
    6315: ['厌战','厌战a','厌战b'],
    6316: ['英王乔治五世','英王乔治五世a','英王乔治五世b'],
    6317: ['威尔士亲王','威尔士亲王a','威尔士亲王b'],
    6318: ['约克公爵','约克公爵a','约克公爵b'],
    6319: ['长门','长门a','长门b'],
    6320: ['纪伊','纪伊a','纪伊b'],
    6321: ['土佐','土佐a','土佐b'],
    6322: ['俾斯麦','俾斯麦a','俾斯麦b'],
    6323: ['提尔比茨','提尔比茨a','提尔比茨b'],
    6324: ['三笠','三笠a','三笠b'],
    6325: ['让·巴尔','让·巴尔a','让·巴尔b'],
    6326: ['马萨诸塞','马萨诸塞a','马萨诸塞b'],
    6327: ['加贺BB','加贺BBa','加贺BBb'],
    6328: ['阿拉巴马','阿拉巴马a','阿拉巴马b'],
    6329: ['利托里奥','利托里奥a','利托里奥b'],
    6330: ['加斯科涅(μ兵装)','加斯科涅(μ兵装)a','加斯科涅(μ兵装)b'],
    6331: ['骏河','骏河a','骏河b'],
    6332: ['苏维埃罗西亚','苏维埃罗西亚a','苏维埃罗西亚b'],
    6333: ['豪','豪a','豪b'],
    6334: ['君主','君主a','君主b'],
    6335: ['出云','出云a','出云b'],
    6336: ['佐治亚','佐治亚a','佐治亚b'],
    6337: ['腓特烈大帝','腓特烈大帝a','腓特烈大帝b'],
    6338: ['加斯科涅','加斯科涅a','加斯科涅b'],
    6339: ['香槟','香槟a','香槟b'],
    6340: ['绊爱·SuperGamer','绊爱·SuperGamera','绊爱·SuperGamerb'],
    6341: ['胡蜂','胡蜂a','胡蜂b'],
    6342: ['列克星敦','列克星敦a','列克星敦b'],
    6343: ['萨拉托加','萨拉托加a','萨拉托加b'],
    6344: ['约克城','约克城a','约克城b'],
    6345: ['大黄蜂','大黄蜂a','大黄蜂b'],
    6346: ['鹰','鹰a','鹰b'],
    6347: ['皇家方舟','皇家方舟a','皇家方舟b'],
    6348: ['光荣','光荣a','光荣b'],
    6349: ['苍龙','苍龙a','苍龙b'],
    6350: ['飞龙','飞龙a','飞龙b'],
    6351: ['小赤城','小赤城a','小赤城b'],
    6352: ['小齐柏林','小齐柏林a','小齐柏林b'],
    6353: ['小光辉','小光辉a','小光辉b'],
    6354: ['企业','企业a','企业b'],
    6355: ['光辉','光辉a','光辉b'],
    6356: ['胜利','胜利a','胜利b'],
    6357: ['可畏','可畏a','可畏b'],
    6358: ['赤城','赤城a','赤城b'],
    6359: ['加贺','加贺a','加贺b'],
    6360: ['翔鹤','翔鹤a','翔鹤b'],
    6361: ['瑞鹤','瑞鹤a','瑞鹤b'],
    6362: ['大凤','大凤a','大凤b'],
    6363: ['齐柏林伯爵','齐柏林伯爵a','齐柏林伯爵b'],
    6364: ['埃塞克斯','埃塞克斯a','埃塞克斯b'],
    6365: ['香格里拉','香格里拉a','香格里拉b'],
    6366: ['邦克山','邦克山a','邦克山b'],
    6367: ['赤城(μ兵装)','赤城(μ兵装)a','赤城(μ兵装)b'],
    6368: ['无畏','无畏a','无畏b'],
    6369: ['信浓','信浓a','信浓b'],
    6370: ['贝露','贝露a','贝露b'],
    6371: ['翡绿之心','翡绿之心a','翡绿之心b'],
    6372: ['芙米露露','芙米露露a','芙米露露b'],
    6373: ['绊爱·Anniversary','绊爱·Anniversarya','绊爱·Anniversaryb'],
    6374: ['扶桑改1'],
    6375: ['山城改1'],
    6376: ['伊势改1'],
    6377: ['日向改1'],
    6378: ['博格','博格a','博格b'],
    6379: ['兰利','兰利a','兰利b'],
    6380: ['突击者','突击者a','突击者b'],
    6381: ['竞技神','竞技神a','竞技神b'],
    6382: ['长岛','长岛a','长岛b'],
    6383: ['飞鹰','飞鹰a','飞鹰b'],
    6384: ['隼鹰','隼鹰a','隼鹰b'],
    6385: ['祥凤','祥凤a','祥凤b'],
    6386: ['卡萨布兰卡','卡萨布兰卡a','卡萨布兰卡b'],
    6387: ['独角兽','独角兽a','独角兽b'],
    6388: ['凤翔','凤翔a','凤翔b'],
    6389: ['龙骧','龙骧a','龙骧b'],
    6390: ['追赶者','追赶者a','追赶者b'],
    6391: ['独立','独立a','独立b'],
    6392: ['巴丹','巴丹a','巴丹b'],
    6393: ['千岁','千岁a','千岁b'],
    6394: ['千代田','千代田a','千代田b'],
    6395: ['普林斯顿','普林斯顿a','普林斯顿b'],
    6396: ['半人马','半人马a','半人马b'],
    6397: ['龙凤','龙凤a','龙凤b'],
    6398: ['英仙座','英仙座a','英仙座b'],
    6399: ['乌璐露','乌璐露a','乌璐露b'],
    6400: ['萨拉娜','萨拉娜a','萨拉娜b'],
    6401: ['黑暗界','黑暗界a','黑暗界b'],
    6402: ['恐怖','恐怖a','恐怖b'],
    6403: ['阿贝克隆比','阿贝克隆比a','阿贝克隆比b'],
    6404: ['女灶神','女灶神a','女灶神b'],
    6405: ['明石','明石a','明石b'],
    6406: ['伊26','伊26a','伊26b'],
    6407: ['伊58','伊58a','伊58b'],
    6408: ['鲦鱼','鲦鱼a','鲦鱼b'],
    6409: ['U-557','U-557a','U-557b'],
    6410: ['絮库夫','絮库夫a','絮库夫b'],
    6411: ['U-556','U-556a','U-556b'],
    6412: ['U-73','U-73a','U-73b'],
    6413: ['伊25','伊25a','伊25b'],
    6414: ['伊56','伊56a','伊56b'],
    6415: ['U-522','U-522a','U-522b'],
    6416: ['U-110','U-110a','U-110b'],
    6417: ['蓝鳃鱼','蓝鳃鱼a','蓝鳃鱼b'],
    6418: ['伊19','伊19a','伊19b'],
    6419: ['U-81','U-81a','U-81b'],
    6420: ['U-47','U-47a','U-47b'],
    6421: ['大青花鱼','大青花鱼a','大青花鱼b'],
    6422: ['伊13','伊13a','伊13b'],
    6423: ['伊168','伊168a','伊168b'],
    6424: ['U-101','U-101a','U-101b'],
    6425: ['棘鳍','棘鳍a','棘鳍b'],
    6426: ['U-96','U-96a','U-96b'],
    6427: ['樫野','樫野a','樫野b'],
    6428: ['卡辛改','卡辛改a','卡辛改b'],
    6429: ['唐斯改','唐斯改a','唐斯改b'],
    6430: ['拉菲改','拉菲改a','拉菲改b'],
    6431: ['西姆斯改','西姆斯改a','西姆斯改b'],
    6432: ['哈曼改','哈曼改a','哈曼改b'],
    6433: ['海伦娜改','海伦娜改a','海伦娜改b'],
    6434: ['圣地亚哥改','圣地亚哥改a','圣地亚哥改b'],
    6435: ['波特兰改','波特兰改a','波特兰改b'],
    6436: ['内华达改','内华达改a','内华达改b'],
    6437: ['俄克拉荷马改','俄克拉荷马改a','俄克拉荷马改b'],
    6438: ['长岛改','长岛改a','长岛改b'],
    6439: ['博格改','博格改a','博格改b'],
    6440: ['兰利改','兰利改a','兰利改b'],
    6441: ['萨拉托加改','萨拉托加改a','萨拉托加改b'],
    6442: ['突击者改','突击者改a','突击者改b'],
    6443: ['女将改','女将改a','女将改b'],
    6444: ['阿卡司塔改','阿卡司塔改a','阿卡司塔改b'],
    6445: ['热心改','热心改a','热心改b'],
    6446: ['彗星改','彗星改a','彗星改b'],
    6447: ['新月改','新月改a','新月改b'],
    6448: ['小天鹅改','小天鹅改a','小天鹅改b'],
    6449: ['狐提改','狐提改a','狐提改b'],
    6450: ['命运女神改','命运女神改a','命运女神改b'],
    6451: ['标枪改','标枪改a','标枪改b'],
    6452: ['利安得改','利安得改a','利安得改b'],
    6453: ['阿基里斯改','阿基里斯改a','阿基里斯改b'],
    6454: ['阿贾克斯改','阿贾克斯改a','阿贾克斯改b'],
    6455: ['伦敦改','伦敦改a','伦敦改b'],
    6456: ['萨福克改','萨福克改a','萨福克改b'],
    6457: ['约克改','约克改a','约克改b'],
    6458: ['埃克塞特改','埃克塞特改a','埃克塞特改b'],
    6459: ['厌战改','厌战改a','厌战改b'],
    6460: ['竞技神改','竞技神改a','竞技神改b'],
    6461: ['绫波改','绫波改a','绫波改b'],
    6462: ['时雨改','时雨改a','时雨改b'],
    6463: ['阳炎改','阳炎改a','阳炎改b'],
    6464: ['不知火改','不知火改a','不知火改b'],
    6465: ['初春改','初春改a','初春改b'],
    6466: ['初霜改','初霜改a','初霜改b'],
    6467: ['有明改','有明改a','有明改b'],
    6468: ['夕暮改','夕暮改a','夕暮改b'],
    6469: ['夕张改','夕张改a','夕张改b'],
    6470: ['五十铃改','五十铃改a','五十铃改b'],
    6471: ['鬼怒改','鬼怒改a','鬼怒改b'],
    6472: ['阿武隈改','阿武隈改a','阿武隈改b'],
    6473: ['最上改','最上改a','最上改b'],
    6474: ['古鹰改','古鹰改a','古鹰改b'],
    6475: ['加古改','加古改a','加古改b'],
    6476: ['扶桑改','扶桑改a','扶桑改b'],
    6477: ['山城改','山城改a','山城改b'],
    6478: ['伊势改','伊势改a','伊势改b'],
    6479: ['日向改','日向改a','日向改b'],
    6480: ['祥凤改','祥凤改a','祥凤改b'],
    6481: ['苍龙改','苍龙改a','苍龙改b'],
    6482: ['飞龙改','飞龙改a','飞龙改b'],
    6483: ['Z1改','Z1改a','Z1改b'],
    6484: ['Z23改','Z23改a','Z23改b'],
    6485: ['卡尔斯鲁厄改','卡尔斯鲁厄改a','卡尔斯鲁厄改b'],
    6486: ['科隆改','科隆改a','科隆改b'],
    6487: ['莱比锡改','莱比锡改a','莱比锡改b'],
    6488: ['宁海改','宁海改a','宁海改b'],
    6489: ['平海改','平海改a','平海改b'],
    6490: ['贝利改','贝利改a','贝利改b'],
    6491: ['神风改','神风改a','神风改b'],
    6492: ['松风改','松风改a','松风改b'],
    6493: ['睦月改','睦月改a','睦月改b'],
    6494: ['如月改','如月改a','如月改b'],
    6495: ['尼古拉斯改','尼古拉斯改a','尼古拉斯改b'],
    6496: ['川内改','川内改a','川内改b'],
    6497: ['神通改','神通改a','神通改b'],
    6498: ['滨风改','滨风改a','滨风改b'],
    6499: ['谷风改','谷风改a','谷风改b'],
    6500: ['福尔班改','福尔班改a','福尔班改b'],
    6501: ['埃米尔·贝尔汀改','埃米尔·贝尔汀改a','埃米尔·贝尔汀改b'],
    6502: ['勒马尔改','勒马尔改a','勒马尔改b'],
    6503: ['纽卡斯尔改','纽卡斯尔改a','纽卡斯尔改b'],
    6504: ['库拉索改','库拉索改a','库拉索改b'],
    6505: ['杓鹬改','杓鹬改a','杓鹬改b'],
 # =================================== #
    7001: ["安柏", "安帕"],
    7002: ["丽莎",],
    7003: ["芭芭拉", "886", "巴巴拉"],
    7004: ["香菱"],
    7005: ["凝光"],
    7006: ["北斗"],
    7007: ["菲谢尔", "皇女", "王女"],
    7008: ["诺艾尔"],
    7009: ["砂糖"],
    7010: ["琴"],
    7011: ["七七", "77"],
    7012: ["莫娜"],
    7013: ["刻晴","刻师傅","资本家"],
    7014: ["可莉"],
    7015: ["迪奥娜", "dio娜"],
    7016: ["辛焱"],
    7017: ["甘雨", "椰羊"],
    7018: ["胡桃(原神)","胡堂主",'往生堂堂主','原神胡桃'],
    7019: ['荧','萤'],









    # =================================== #

  #  1907: ["大古", "タイゴ", "Taigo", "大吾", "鬼道大吾"],
    1908: ["花凛", "カリン", "Karin", "绿毛恶魔"],
    1909: ["涅比亚", "ネビア", "Nevia", "Nebia"],
   # 1910: ["真崎", "マサキ", "Masaki"],
    1911: ["米涅尔β", "ミネルβ", "MineruBeta", "米涅尔", "ミネル", "Mineru"],


   # 1914: ["豪绅", "ゴウシン", "Goushin"],
   # 1915: ["克里吉塔", "クレジック", "Kurejikku"],
  #  1916: ["基洛", "キイロ", "Kiiro"],
  #  1917: ["善", "ゼーン", "Seen"],
    1918: ["兰法", "ランファ", "Ranfa"],
 #   1919: ["阿佐尔德", "アンゾールド", "Anzoorudo"],
    1920: ["美空", "ミソラ", "Misora"],
 
    4031: ["骷髅", "髑髏", "Dokuro", "骷髅老爹", "老爹"],
 
    9000: ["祐树", "ユウキ", "Yuuki", "骑士", "骑士君"],
    9401: ["爱梅斯", "アメス", "Amesu", "菲欧", "フィオ", "Fio"],
    
    9601: ["01", "001", "one"],
    9602: ["02", "002", "two"],
    9603: ["03", "003", "three"],
    9604: ["04", "004", "four"]

}
