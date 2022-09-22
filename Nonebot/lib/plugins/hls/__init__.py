from nonebot import on_command, CommandSession

@on_command('hls', aliases=('黑历史'), only_to_me=False)
async def pic(session: CommandSession):
    await session.send('[CQ:image,file=https://7ychu5.xyz/wp-content/uploads/hls.php,cache=0]')
    