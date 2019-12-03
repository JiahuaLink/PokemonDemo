#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battleRoom.py
@Time    :   2019/11/26 22:46:19
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   战功场景初始化
'''

# here put the import libn
from fileManager import FileManager
from battleProcess import BattleProcess


class BattleRoom():
    # 与精灵战斗
    def battlewith(self, mypkmon, wild_pkmon):
        # 首先派出自己的精灵
        
        # 双方精灵加入战斗场景(写入文本文件)
        battle_manger = {'player': mypkmon, 'enemy': wild_pkmon}
        # print(battle_manger)
        # 测试获取的等级
        print("该你上场了，去吧，%s!\n" % battle_manger['player']['pkmon_name'])
        
        FileManager().save_battle_env(battle_manger)
        BattleProcess().start(battle_manger)


        
        
        
        