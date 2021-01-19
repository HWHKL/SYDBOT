# -*- coding: UTF-8 -*-
"""
 * @author  zfj
 * @date  2020/9/26 15:39
"""
from hoshino import *
from hoshino import Service
import requests
import re


Cookie = {'__cfduid': 'd12d675fa3c54e7a3028de93ca583e35b1607663226'}
apiPath = r'http://jjc-finder.wa.vg'

sv = Service('zfjbot-jjc-finder')

def post_jjc(user_id):
    print("start")
    apiPath = r'http://jjc-finder.wa.vg'
    data_post = {'user_id': user_id}
    header = {
        'Host': 'jjc-finder.wa.vg',
        'Connection': 'keep-alive',
        'Origin': 'http://jjc-finder.wa.vg',
        'Content - Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                  'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://jjc-finder.wa.vg/',
        'Accept-Encoding': 'none',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    Cookie = {'__cfduid': 'd12d675fa3c54e7a3028de93ca583e35b1607663226'}
    try:
        with requests.post(apiPath, headers=header, data=data_post, cookies=Cookie, timeout=300) as resp:
            res = resp.text
            return res

    except Exception as ex:
        print("error", ex)
        return ex

@sv.on_prefix("jjc场次")
async def jjc_finder(bot,ev):
    for msg_seg in ev.message:
        if msg_seg.type == 'text' and msg_seg.data['text']:
            user_id=msg_seg.data['text']
        else:
            await bot.send(ev,"发生什么了吗")
            return
    await bot.send(ev,f"查询中，网络较慢请耐心等待...")
    if len(user_id) == 13:
        res1 = post_jjc(user_id)
        if res1 != "error":
            res1 = res1.replace('\n', '').replace('\r', '')
            res1 = ' '.join(res1.split()).replace(" ", '')
            res_group1 = re.search('^(.*?)用户名</th><td>(.*?)</td>.*$', res1)
            res_group2 = re.search('^(.*?)等级/经验</th><td>(.*?)</td>.*$', res1)
            res_group3 = re.search('^(.*?)战力</th><td>(.*?)</td>.*$', res1)
            res_group4 = re.search('^(.*?)竞技场</th><td>(.*?)</td>.*$', res1)
            res_group5 = re.search('^(.*?)公主竞技场</th><td>(.*?)</td>.*$', res1)
            res_group6 = re.search('^(.*?)<h5>前百战力(.*?)</h5>.*$', res1)
            res_group7 = re.search('^(.*?)<h5>平均战力(.*?)</h5>.*$', res1)
            if res_group1:
                print(user_id)
                print("res_group1.group(2)", res_group1.group(2))
                print("res_group2.group(2)", res_group2.group(2))
                print("res_group3.group(2)", res_group3.group(2))
                print("res_group4.group(2)", res_group4.group(2))
                print("res_group5.group(2)", res_group5.group(2))
                if res_group6:
                    print("res_group6.group(2)", res_group6.group(2))
                    print("res_group7.group(2)", res_group7.group(2))
                    reply = f'用户名:{res_group1.group(2)}\n' \
                            + f'等级/经验:{res_group2.group(2)}\n' \
                            + f'战力:{res_group3.group(2)}\n' \
                            + f'竞技场场次：{res_group4.group(2)}\n' \
                            + f'公主竞技场场次：{res_group5.group(2)}\n' \
                            + f'前百战力{res_group6.group(2)}\n' \
                            + f'平均战力{res_group7.group(2)}'
                    await bot.send(ev,reply)
                if not res_group6:
                    reply = f'用户名:{res_group1.group(2)}\n' \
                            + f'等级/经验:{res_group2.group(2)}\n' \
                            + f'战力:{res_group3.group(2)}\n' \
                            + f'竞技场场次：{res_group4.group(2)}\n' \
                            + f'公主竞技场场次：{res_group5.group(2)}\n'\
                            + f'================\n场均战力查询失败，可能您还未进场或者稍后再试'
                    await bot.send(ev,reply)
        else:
            await bot.send(ev,f"查询失败，Error:\n{res1}")
    else:
        await bot.send(ev,"ID有误")
