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
from MoveSelector import MoveSelect


# here put the import lib
class BattleEvent(object):
    def atk_event(self, data):
        print("选择技能")
        choose = input()
        MoveSelect().select(choose, data)

    def run_event(self):

        pass