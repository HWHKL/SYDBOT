from hoshino import Service, priv


sv = Service(
        name = '消息造假',  #功能名
        use_priv = priv.SUPERUSER, #使用权限   
        manage_priv = priv.SUPERUSER, #管理权限
        visible = False, #是否可见
        enable_on_default = False, #是否默认启用
        bundle = '消息造假', #属于哪一类
        help_ = '你猜' #帮助文本
        )
# 多条消息的分隔符
SPLIT_TEXT = "\n"

def split_mes(mes:str):
    # 把整条消息分割成列表
    #mes = mes.replace("[CQ:at,qq=","").replace("]","")
    mes = mes.replace("\r\n","\n")
    mes_list = mes.split(SPLIT_TEXT)

    for i in range(len(mes_list)):
        # 按空格分割指令段
        temp_txt = mes_list[i].split(" ")

        # 去除多余的空字符串
        temp_list = [txt for txt in temp_txt if txt != ""]

        mes_list[i] = temp_list

    return mes_list


def produce_fake_mes(mes:str):
    # 生成假消息

    mes_list = split_mes(mes)

    data_list = []

    for mes in mes_list:
        uid,name,message = mes
        uid = uid.replace("[CQ:at,qq=","").replace("]","")

        data = {
            "type": "node",
            "data": {
                "name": name,
                "uin": uid,
                "content": message
            }
        }
        data_list.append(data)
    return data_list




@sv.on_prefix("假消息")
async def fake_mes(bot, ev):

    mes = ev["raw_message"][3:].strip()
    data = produce_fake_mes(mes)
    await bot.send_group_forward_msg(group_id=ev['group_id'], messages=data)


