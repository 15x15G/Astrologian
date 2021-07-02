from .luck import luck_daily

from hoshino import Service, logger
from hoshino.typing import CQEvent
from hoshino.util import escape
from hoshino.typing import CommandSession

sv = Service('Astrologian', help_='''
[占卜/zhanbu]
'''.strip())

# on_command 装饰器将函数声明为一个命令处理器
@sv.on_prefix('/zhanbu','占卜','/占卜','zhanbu',  only_to_me=False)
async def luck(bot, ev: CQEvent):
    args: list = escape(ev.message.extract_plain_text().strip()).split()
    if args:
        if "help" in args:
            msg="""
        艾欧泽亚人的一天从23:00开始！
        可以在"/占卜"后加 "重抽" "redraw" "r" 来重抽
        插件名：Astrologian 
        (forked from onebot_Astrologian_FFXIV)
        当前支持版本：hoshinobot""".strip()
        elif ("r" in args) or ("重抽" in args) or ("redraw" in args):
            msg="开拓命运吧\n"
            msg+=await luck_daily(user_id=ev.user_id,redraw=True)        
        elif args[0] == "test" and len(args)>1 and args[1].isdigit()==True:
            logger.debug("test" + ": " + args[1])
            msg=await luck_daily(user_id=int(args[1]),redraw=False)
    else:
        msg=await luck_daily(user_id=ev.user_id,redraw=False)
    await bot.send(ev, msg)
