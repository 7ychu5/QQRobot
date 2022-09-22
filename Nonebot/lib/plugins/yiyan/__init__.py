from nonebot import on_command, CommandSession

from .data_source import get_yy

@on_command('yy', aliases=('一言'), only_to_me=False)
async def yy(session: CommandSession):
    yy_report = await get_yy()
    await session.send(yy_report)
    
    