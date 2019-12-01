#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MovesSelector.py
@Time    :   2019/11/29 21:42:19
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   技能伤害计算
            
'''
from fileManager import FileManager
from damageCalculator import Damages
from statisticCalculator import Statistic


class MoveManager():

    
    # 技能选择
    def select(self, choose, data):
        # 
        pkmon_name = data["player"]["pkmon_name"]
        
        moves = data["player"]["moves"]
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

        # 选其中一个技能 进行伤害计算
        moveinfo = moves[move]
        print("%s使出了%s" % (pkmon_name, moveinfo["name"]))
        # 计算是否命中

        # 计算伤害
        data = Damages().damages_calc(moveinfo, data)
        FileManager().save_battle_env(data)
        




class MovesList():
    pass