# Astrologian_for_Hoshinobot

 ~~一个基于nonebot的重构的FFXIVQQ机器人占卜插件~~

 一个基于HoshinoBot的重构的FFXIVQQ机器人占卜插件

## 部署方法
1. 将`Astrologian`文件夹放入`modules`模块文件夹
   
    ```
    hoshino
    └─modules
        └─Astrologian
    ```

2. 在`__bot__.py`中添加模块
   ```
    MODULES_ON = {
    ..., #其他模块
    'Astrologian'
    }
   ```
本插件目前无特殊设置，请参考 ~~nonebot~~ [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) 进行部署

## 使用方法
 
### 超简洁方法

每日（从北京时间23：00）获取固定占卜结果

向QQBot发送命令`占卜`，`/占卜`，`zhanbu`，或`/zhanbu`

后面加`r`，`重抽`，或者`redraw`来重抽

后面加`help`来获得帮助，如`/zhanbu help`

## 鸣谢

[原插件](https://github.com/LittleNightmare/onebot_Astrologian_FFXIV)

