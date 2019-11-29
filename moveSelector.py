#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MovesSelector.py
@Time    :   2019/11/29 21:42:19
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   技能选择
'''
from fileManager import FileManager


class MoveSelect():
    
    def select(self, choose, data):
        #
        move = ''
        if choose == 1:
            move = 'move1'    
        elif choose == 2:
            move = 'move2'
        elif choose == 3:
            move = 'move3'
        elif choose == 4:
            move = 'move4'
        else:
            print("啥都没做")
        pkmon_name = data["player"]["pkmon_name"]
        moves = data["player"]["moves"]
        moveinfo = moves[move]
        print("%s使出了%s" % (pkmon_name, moveinfo["move_name"]))
        FileManager().save_battle_env(data)
        pass