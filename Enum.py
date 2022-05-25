from enum import Enum

class CmdEnum(Enum):
    RECORD = "查询战绩"
    BIND = "绑定id"
    MAP = "地图信息"
    CRAFTING = "当前制造"

class UsageEnum(Enum):
    BIND = '.{cmd} EA_ID [自动将qq号与EA id绑定]'.format(cmd=CmdEnum.BIND.value)
    RECORD = '.{cmd} EA_ID [若已绑定EA id,可不输入EA_ID]'.format(cmd=CmdEnum.RECORD.value)
    MAP = '.{cmd}'.format(cmd=CmdEnum.MAP.value)
    CRAFTING = '.{cmd}'.format(cmd=CmdEnum.CRAFTING.value)