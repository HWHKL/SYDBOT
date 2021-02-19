import os
import json
import traceback
import asyncio
import aiohttp
import random
import string
import re
from hoshino import R
from .config import get_config, get_group_config
from .acggov import acggov_init, acggov_fetch_process, acggov_get_setu, acggov_search_setu, acggov_get_ranking_setu, acggov_get_ranking, get_setu_native
from .lolicon import lolicon_init, lolicon_get_setu,lolicon_fetch_process, lolicon_search_setu, get_setu_native

def check_path():
    state = {}
    sub_dirs = ['acggov', 'lolicon', 'lolicon_r18']
    for item in sub_dirs:
        res = R.img('setu_mix/' + item)
        if not os.path.exists(res.path):
            os.makedirs(res.path)
        state[item] = len(os.listdir(res.path)) // 2
    return state
check_path()

def get_spec_image(id):
    image = get_setu_native(0, id)
    if not image:
        return None
    else:
        image = format_setu_msg(image)
        return image

def format_setu_msg(image):
    try:
        if image["title"]:
            msg = f'「{image["title"]}」/「{image["author"]}」\nPID:{image["id"]}[CQ:image,file=file:///{os.path.abspath(image["data"])}]'
            return msg
        else:
            return None
    except(TypeError):
        return None
    
async def get_setu(group_id):
    source_list = []
    if get_group_config(group_id, 'lolicon'):
        source_list.append(1)
    if get_group_config(group_id, 'lolicon_r18'):
        source_list.append(2)
    if get_group_config(group_id, 'acggov'):
        source_list.append(3)
    source = 0
    if len(source_list) > 0:
        source = random.choice(source_list)
    
    image = None
    if source == 1:
        image = await lolicon_get_setu(0)
    elif source == 2:
        image = await lolicon_get_setu(1)
    elif source == 3:
        image = await acggov_get_setu()
    else:
        return None
    if not image:
        return '获取失败'
    elif image['id'] != 0:
        return format_setu_msg(image)
    else:
        return image['title']

async def search_setu(group_id, keyword, num):
    source_list = []
    if get_group_config(group_id, 'lolicon') and get_group_config(group_id, 'lolicon_r18'):
        source_list.append(2)
    elif get_group_config(group_id, 'lolicon'):
        source_list.append(0)
    elif get_group_config(group_id, 'lolicon_r18'):
        source_list.append(1)
    if get_group_config(group_id, 'acggov'):
        source_list.append(3)

    if len(source_list) == 0:
        return None
    
    image_list = None
    msg_list = []
    while len(source_list) > 0 and len(msg_list) == 0:
        source = source_list.pop(random.randint(0, len(source_list) - 1))
        if source == 0:
            image_list = await lolicon_search_setu(keyword, 0, num)
        elif source == 1:
            image_list = await lolicon_search_setu(keyword, 1, num)
        elif source == 2:
            image_list = await lolicon_search_setu(keyword, 2, num)
        elif source == 3:
            image_list = await acggov_search_setu(keyword, num)
        if image_list and len(image_list) > 0:
            for image in image_list:
                msg_list.append(format_setu_msg(image))
    return msg_list

async def get_ranking(group_id, page: int = 0):
    if not get_group_config(group_id, 'acggov'):
        return None
    return await acggov_get_ranking(page)


async def get_ranking_setu(group_id, number: int) -> (int, str):
    if not get_group_config(group_id, 'acggov'):
        return None
    image = await acggov_get_ranking_setu(number)
    if not image:
        return '获取失败'
    elif image['id'] != 0:
        return format_setu_msg(image)
    else:
        return image['title']

async def fetch_process():
    tasks = []
    #tasks.append(asyncio.ensure_future(acggov_fetch_process()))
    tasks.append(asyncio.ensure_future(lolicon_fetch_process()))
    for task in asyncio.as_completed(tasks):
        await task

acggov_init()
lolicon_init()
