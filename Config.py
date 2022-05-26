import json

class Config:
    
    def __init__(self, js_file):
        with open(js_file, 'r') as js_f:
            self.__config = json.load(js_f)
            
    # https://apexlegendsapi.com/ 查询所需鉴权
    def getApexAuth(self):
        return self.__config["APEX_AUTH"]
    
    def getSaveDir(self):
        return self.__config["SAVE_DIR"]
    
    def getFileName(self):
        return self.__config["FILE_NAME"]
