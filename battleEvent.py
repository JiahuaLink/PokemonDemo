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
from moveSelector import MoveSelect


# here put the import lib
class BattleEvent(object):
    def atk_event(self, data):
        moves = data["player"]["moves"]
        movesinfo1 = moves["move1"]
        movesinfo2 = moves["move2"]
        movesinfo3 = moves["move3"]
        movesinfo4 = moves["move4"] 

        print(movesinfo1["name"], movesinfo2["name"], movesinfo3["name"], movesinfo4["name"])
        print("选择技能:")
        choose = int(input())
        MoveSelect().select(choose, data)

    def run_event(self):

        pass