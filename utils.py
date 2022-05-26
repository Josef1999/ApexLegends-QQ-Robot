import json
import requests
import os
from .Config import Config
from nonebot.adapters import Message

CONFIG_PATH = os.path.join(os.path.dirname(__file__),'config.json')
QQ_EAID_PATH = os.path.join(os.path.dirname(__file__),'qq_eaID.json')

CONFIG = Config(CONFIG_PATH)    

class Utils:

    @staticmethod
    def try_translate_br(br_name):
        br_translation = {
            'Storm Point'   :'风暴点',
            'Olympus'       :'奥林匹斯',
            'Kings Canyon'  :'诸王峡谷',
            "World's Edge"  :'世界尽头',
        }
        return br_translation[br_name] if br_translation.get(br_name) is not None else br_name

    @staticmethod
    def try_translate_crafting(crafting_name):
        crafting__translation = {
            'optic_variable_aog' : '2~4倍镜',
            'optic_hcog_bruiser' : '2倍镜',
            'optic_digital_threat' : '1倍金镜',
            'extended_light_mag' : '紫轻型弹匣',
            'extended_heavy_mag' : '紫重型弹匣',
            'shotgun_bolt' : '紫霰弹枪栓',
            'mobile_respawn_beacon' : '移动重生信标',
            'knockdown_shield' : '紫击倒护盾',
            'backpack' : '紫包',
            'helmet' : '紫头'
        }
        return crafting__translation[crafting_name] if crafting__translation.get(crafting_name) is not None else crafting_name

    @staticmethod
    def try_translate_legend(legend_name):
        legend_translation = {}
        return legend_translation[legend_name] if legend_translation.get(legend_name) is not None else legend_name

    @staticmethod
    def get_args(text:Message):
        if len(text) < 1:
            return []
        args = text[0].data['text'].split(' ')
        return args

    @staticmethod
    def safe_request(url):
        response = requests.get(url, timeout=(5, 5))
        return response

# apex api查询
class Query:
    __auth = CONFIG.getApexAuth()
    @staticmethod
    def record(ea_user_name):
        return Utils.safe_request('https://api.mozambiquehe.re/bridge?auth={APEX_AUTH}&player={EA_USER_NAME}&platform=PC'.format(APEX_AUTH=Query.__auth, EA_USER_NAME=ea_user_name))

    @staticmethod
    def map():
        return Utils.safe_request("https://api.mozambiquehe.re/maprotation?auth={APEX_AUTH}&version=1".format(APEX_AUTH=Query.__auth))

    @staticmethod
    def crafting():
        return Utils.safe_request("https://api.mozambiquehe.re/crafting?auth={APEX_AUTH}".format(APEX_AUTH=Query.__auth))

# 玩家信息json解析
class PlayerInfo:

    def __init__(self, js):
        self.__js = js

    def level(self):
        return self.__js["global"]['level']

    def rank(self):
        rankinfo = self.__js["global"]['rank']
        rankscore = rankinfo['rankScore']
        rankname = rankinfo['rankName']
        rankdiv = rankinfo['rankDiv']
        return rankscore, rankname, rankdiv

# 针对qq与ea_id绑定持久化
class Persistence:

    @staticmethod
    def load():
        target_file = open(QQ_EAID_PATH, 'r+')
        try:
            QQ_EA = json.load(target_file)
            print('load_sucess')
        except Exception as e:
            print(e)
            QQ_EA = {}
        target_file.close()
        return QQ_EA
    
    @staticmethod
    def write(js):
        target_file = open(QQ_EAID_PATH, 'w+')
        json.dump(js, target_file)
        target_file.close()
        return 
