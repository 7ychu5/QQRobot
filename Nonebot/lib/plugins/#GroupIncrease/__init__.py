from nonebot import on_notice, NoticeSession

# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    await session.send('欢迎来到ExG的僵尸逃跑服务器！\n请将群名片改为游戏ID方便大家认识你哦！\n这里是玩家米花糖的机器人小号！\n目前功能有\n①可以查看色图，指令为：。来点色图\n②可以查看ExG黑历史，指令为：。黑历史\n也欢迎各位给机器人投稿更多的黑历史素材，\n但是也请不要滥玩哦！')