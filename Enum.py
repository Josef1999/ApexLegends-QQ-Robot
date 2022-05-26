from enum import Enum

class CmdEnum(Enum):
    RECORD = "查询战绩"
    BIND = "绑定账号"
    MAP = "当前地图"
    CRAFTING = "当前制造"

class UsageEnum(Enum):
    RECORD = '.{cmd} EA_ID [若已绑定EA账号,可不输入EA账号]'.format(cmd=CmdEnum.RECORD.value)
    BIND = '.{cmd} EA_ID [自动将QQ号与EA账号绑定]'.format(cmd=CmdEnum.BIND.value)
    MAP = '.{cmd}'.format(cmd=CmdEnum.MAP.value)
    CRAFTING = '.{cmd}'.format(cmd=CmdEnum.CRAFTING.value)