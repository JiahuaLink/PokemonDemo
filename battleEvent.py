#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battleEvent.py
@Time    :   2019/11/29 21:50:50
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   处理战斗事件
'''
from moveManager import MoveManager


# here put the import lib
class BattleEvent(object):
    # 选择攻击
    def atk_event(self, data):
        moves = data["player"]["moves"]
        movesinfo1 = moves["move1"]
        movesinfo2 = moves["move2"]
        movesinfo3 = moves["move3"]
        movesinfo4 = moves["move4"] 
        print(movesinfo1["name"], movesinfo2["name"], movesinfo3["name"], movesinfo4["name"])

        MoveManager().select(data)
    # 选择逃跑
    def run_event(self):

        pass