# Apex QQ群机器人

## 分支说明
本分支:master 为针对真寻bot适配后的插件，感谢[SinKy-Yan](https://github.com/SinKy-Yan)完成了插件适配工作

## 支持功能
1. 查询当前轮换地图：输出当前与即将轮换的大逃杀地图，轮换时间；当前与下半赛季排位地图，轮换时间
2. 绑定账号：自动将命令调用者的QQ号与其提供EA ID(非Steam ID)绑定，并保存在config.json中指定目录下的文件中,**会自动检测EA ID是否有效**
3. 查询战绩：查询命令调用者提供的EA id对应的apex数据（等级、当前赛季排位信息）。缺省EA id时检测调用者是否已绑定EA id，若已绑定则查询绑定id的战绩
4. 查询当前制造：输出本日与本周制造

## 插件使用
1. 将本仓库clone到zhenxun_bot/plugins文件夹下，放在自定义插件目录下也行
2. 在 https://portal.apexlegendsapi.com/ 中生成API KEY，填入config.json的APEX_AUTH中

## 常见QA
- Q:怎么获取绑定用的ID？
  - A: EA ID获取方式：点击登陆 EA账号与财务设定 (https://myaccount.ea.com/cp-ui/aboutme/index) ，登陆后个人页面即可查询 EA ID。

- Q:机器人为什么没有对插件提供的指令作出反应？
  - A:请检查输入的指令是否正确，若指令正确请检查服务器的日志输出。此外由于本插件使用的查询网站存在网络波动可能，并且该网站默认的api key只支持30次/min的查询频率（可升级至120次/min），故无法保证相关数据查询指令百分百可用。如上述两种情况都不适用，请阅读Issues目录下内容，若问题仍未解决，请提出新的Issue。


## 相关api依赖
信息查询API来自 [**APEX LEGENDS STATUS**](https://apexlegendsapi.com/)
