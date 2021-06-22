# onebot_Astrologian_FFXIV
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
向QQBot发送命令`占卜`，`/占卜`，`zhanbu`，或`/zhanbu`

## TODO

占卜结尾一言言尚未完成，目前位于`plugins\Astrologian\data\events.json`
### 说明
1. 每个`event`有一个组list，其中按从大到小顺序储存了对应的一言，默认luck为50，unluck为0，通过`luck_number`(运势)的大小来选择

2. 当`luck_number>=50`(运势)会采用luck，小于则采用unluck

3. 每个`event`可以无限增加，会返回第一个小于等于luck_number(运势)的值跳出

4. 为了后续判断，以及可读性，请将luck的数字满足 `50<=num<=100`; 而unluck满足 `0<=num<50`。并且按照从大到小的顺序排列

## 鸣谢
TODO

