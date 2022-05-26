# Apex QQ群机器人
## 分支说明
本分支:master 为针对真寻bot适配后的插件，感谢[SinKy-Yan](https://github.com/SinKy-Yan)完成了插件适配工作

## 支持功能
1. 地图信息：输出当前与即将轮换的大逃杀地图，轮换时间；当前与下半赛季排位地图，轮换时间
2. 绑定ID：自动将命令调用者的qq号与其提供EA id（非UID）绑定，并持久化在config.json中指定目录下的文件中
*注：会自动检测EA id是否有效*
3. 查询战绩：查询命令调用者提供的EA id对应的apex数据（等级、当前赛季排位信息）。缺省EA id时检测调用者是否已绑定EA id，若已绑定则查询绑定id的战绩
4. 查询制造：输出本日与本周制造

## 如何使用
### 环境搭建
Python 3.9.9

nonebot2==2.0.0b2

*注：具体搭建过程详见 https://www.bilibili.com/video/BV1aZ4y1f7e2?p=3&spm_id_from=pageDriver*

*po主讲的很详细，零基础照着做也能搭个机器人出来*

### 插件使用
详见 [真寻bot插件库](https://github.com/zhenxun-org/nonebot_plugins_zhenxun_bot/tree/index)

## 相关api依赖

**apex数据：https://apexlegendsapi.com/**

## TODO
1. 完善每日制造本地化翻译，当前本地化翻译不全
