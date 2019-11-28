#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battleRoom.py
@Time    :   2019/11/26 22:46:19
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

# here put the import lib
from myPkmon import MyPkmon
from fileManager import FileManager
from battleProcess import BattleProcess


class BattleRoom():
    # 与精灵战斗
    def battlewith(self, wild_pkmon):
        # 首先派出自己的精灵
        mypkmon = MyPkmon().get_my_pkmon()
        # 双方精灵加入战斗场景(写入文本文件)
        battle_manger = {'PLAYER': mypkmon, 'ENEMY': wild_pkmon}
        print(battle_manger)
        # 测试获取的等级
        print(battle_manger['PLAYER']['pkmon_name'])
        self.join(battle_manger)

    def join(self, battle_manger):
        FileManager().save_battle_env(battle_manger)
        data = FileManager().open_battle_env()
        
        BattleProcess().start(data)