from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'weather'),'lib.plugins.weather')
#    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'GroupIncrease'),'lib.plugins.GroupIncrease')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'ghs'),'lib.plugins.ghs')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'yiyan'),'lib.plugins.yiyan')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'zuichou'),'lib.plugins.zuichou')
    nonebot.load_plugins(path.join(path.dirname(__file__), 'lib', 'plugins', 'hls'),'lib.plugins.hls')
    nonebot.run()