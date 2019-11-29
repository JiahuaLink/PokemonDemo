#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   playerControls.py
@Time    :   2019/11/28 23:03:59
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   玩家控制
'''

# here put the import lib
from battleEvent import BattleEvent

class PlayerControls():
    def playcontrols(self, choose, data):
        if choose == 1:
            print("攻击")
            BattleEvent().atk_event(data)
        elif choose == 2:
            print("背包")
        elif choose == 3:
            print("精灵")
        elif choose == 4:
            print("逃跑")
        else:
            print("命令错误")