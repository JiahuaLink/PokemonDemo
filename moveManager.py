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
import random

class MoveManager():

    # 技能选择
    def select(self, data):
        #
        print("选择技能:")
        choose = int(input())
        move = None
        player = data["player"]["base_info"]
        pkmon_name = player["name"]
        moves = data["player"]["moves"]
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

        # 选其中一个技能 
        moveinfo = moves[move]
        print("%s使出了%s" % (pkmon_name, moveinfo["name"]))
        # 计算是否命中
        isHit = self.is_move_accuracy(moveinfo, data)
        if isHit == True:    
            # 判断技能类型进行伤害计算后返回计算后的值
            data = self.move_effect(moveinfo, data)
            
        # 保存伤害计算结果
        FileManager().save_battle_env(data)
        
    def is_move_accuracy(self, moveinfo, data):
        '''
        1 判断特性对命中的影响(暂无)
        2 将攻击方的命中等级减去防御方的回避等级。
        3 如果最终命中等级大于6，最终命中等级=6；如果最终命中等级小于-6，最终命中等级=-6
        4 求技能基础命中。
        5 如果技能基础命中为101，判定为命中
        6 用技能基础命中乘以命中等级修正，向下取整。
        7 天气、道具影响（暂无）
        8 产生1～100的随机数，如果小于等于命中，判定为命中，否则判定为失误。
        '''
        our_stat = data["player"]["statistic_level"]
        enemy_stat = data["enemy"]["statistic_level"]
        our_accuracy_level = our_stat["accuracy_level"]
        enmey_avoid_level = enemy_stat["avoid_level"]
        accuracy = moveinfo["accuracy"]
            
        if accuracy == '—':
            print("必然命中!")
            return True
        final_level = int(our_accuracy_level)-int(enmey_avoid_level)
            
        if final_level >= 6:
            final_level = 6
        elif final_level <= -6:
            final_level = -6
        final_accuracy = int(Statistic().accuracy_level_calc(accuracy,final_level))
        
        print("基础命中率为%s \n命中等级为%s \n最终命中率为%d \n" % (accuracy, final_level, final_accuracy))
        randnum = random.randint(0, 100)
        print("随机数为%d" % randnum)
        if randnum <= final_accuracy:
            print("命中敌人")
            return True
        else:
            print("没有命中敌人")
            return False
    # 
    def move_effect(self, moveinfo, data):
        '''
        判断是什么类型的招式 物理 特殊 变化,判断有没有异常状态
        '''
        category = moveinfo["category"]
        if category == "物理" or category == "特殊":
            
            # 计算物理特殊伤害
            data = Damages().damages_calc(moveinfo, data)
            # 计算技能状态效果
            data = self.additional_effect(moveinfo,data)
            # 检测技能的异常效果           
            
        elif category == "变化":
            # 变化伤害
            print("变化技能")
        else:
            pass
        return data
    
    def additional_effect(self,moveinfo,data):
        volatile = moveinfo["volatile"]
        for style, effect in volatile.items():
            if effect !=0:
                print("有%s效果" % style)
                '''
                判断技能触发
                '''
                volatile_rate = effect
                status = data["enemy"]["status"]
                randnum = random.randint(0,100)
                print("随机数为%s" % randnum)
                if randnum <= volatile_rate:
                    print("敌人%s了" % style)
                    status["volatile"] = style
                else:
                    print("没有命中异常状态")
                data["enemy"]["status"] = status
        
        return data
        
        