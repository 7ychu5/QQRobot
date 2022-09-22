from nonebot import on_command, CommandSession

from .data_source import get_zc

@on_command('zc', aliases=('嘴臭'), only_to_me=True)
async def yy(session: CommandSession):
    zc_report = await get_zc()
    await session.send(zc_report)
    
    