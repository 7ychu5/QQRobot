from nonebot import on_command, CommandSession
from .data_source import get_pic

import json

permit_group = { 1011507162 }

@on_command('ghs', aliases=('来点色图'), only_to_me=False)
async def pic(session: CommandSession):
    r = session.get('r18',prompt='输入以确认')
    pic_report = await get_pic(r)
    pic_report_title = pic_report['title']
    pic_report_author = pic_report['author']
    pic_report_url = pic_report['urls']['regular']
    
    await session.send("标题："+pic_report_title+"\n作者："+pic_report_author+"\n图链在此："+pic_report_url)
    await session.send('[CQ:image,file='+pic_report_url+',cache=0]')
    #https://dev.iw233.cn/api.php?sort=random
    #http://iw233.fgimax2.fgnwctvip.com/API/Ghs.php