#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   playerControls.py
@Time    :   2019/11/28 23:03:59
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   控制事件
'''

# here put the import lib
from battleEvent import BattleEvent

class PlayerControls():
    
    def playcontrols(self, data):
        
        player = data["player"]["base_info"]
        print("%s要做什么？\n【攻击】【背包】【精灵】【逃跑】\n" % player["name"])
        choose = int(input())
        if choose == 1:
            print("%s选择了攻击" % player["name"])
            BattleEvent().atk_event(data,"player","enemy")
        elif choose == 2:
            print("背包")
        elif choose == 3:
            print("精灵")
        elif choose == 4:
            print("逃跑")
        else:
            print("命令错误")

class EnemyControls():
    
    
    def enemycontrols(self, data):
        BattleEvent().atk_event(data,"enemy","player")