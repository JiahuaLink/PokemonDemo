#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   statisticCalculator.py
@Time    :   2019/12/01 18:05:31
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   能力值计算,
             计算攻击、防御、速度、特攻、特防、命中率、闪避率七项能力提高或降低的状态
'''

# here put the import lib


class Statistic():
    '''
    能力值计算
        1、攻击、防御、速度、特攻、特防、命中率、闪避率七项能力提高或降低的状态
        2、能力变化只存在于对战中的宝可梦身上，当宝可梦离场后效果消失。
        3、宝可梦出场时，所有能力初始为0级，可以通过招式、特性或道具的效果，提高到最多+6级或降低到最多-6级
    '''

    # 基础5项能力值攻击、防御、速度、特攻、特防
    base_level = {
        -6: 25,
        -5: 28,
        -4: 33,
        -3: 40,
        -2: 50,
        -1: 66,
        0: 100,
        1: 150,
        2: 200,
        3: 250,
        4: 300,
        5: 350,
        6: 400,
    }   
    # 命中闪避等级能力变化
    accuracy_level = {
        -6: 25,
        -5: 28,
        -4: 33,
        -3: 40,
        -2: 50,
        -1: 66,
        0: 100,
        1: 150,
        2: 200,
        3: 250,
        4: 300,
        5: 350,
        6: 400,
    }
    
    
    def atk_level_calc(self):
        
        pass

    def defend_level_calc(self):

        pass

    def atk_sp_level_calc(self):

        pass

    def defend_sp_level_calc(self):

        pass

    def speed_level_calc(self):

        pass

    def accuracy_level_calc(self,accuracy,level):
        return int(accuracy)*(self.accuracy_level[level])/100
        

    def avoid_level_calc(self):

        pass
    
    def stats_change_display(self):
        '''
        上限	[宝可梦]的[能力]已经无法再提高了！
        +3	    [宝可梦]的[能力]巨幅提高了！
        +2	    [宝可梦]的[能力]大幅提高了！
        +1	    [宝可梦]的[能力]提高了！
        -1	    [宝可梦]的[能力]降低了！
        -2	    [宝可梦]的[能力]大幅降低了！
        -3	    [宝可梦]的[能力]巨幅降低了！
        下限	[宝可梦]的[能力]已经无法再降低了！
        '''
        pass