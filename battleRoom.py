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


class BattleRoom():
    # 与精灵战斗
    def battlewith(self, wild_pkmon):
        # 首先派出自己的精灵
        mypkmon = MyPkmon().get_my_pkmon()
        # 双方精灵加入战斗场景(写入文本文件)
        battle_manger = {"PLAYER": wild_pkmon, "ENEMY": mypkmon}
        print(battle_manger)
        print(battle_manger["PLAYER"]["pkmon_type2"])
