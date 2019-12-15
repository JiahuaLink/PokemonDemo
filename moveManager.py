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
    def select(self, data, myself, aims):
        #
        move = None
        # 获取当前攻击方
        attacker = data[myself]["base_info"]
        pkmon_name = attacker["name"]
        
        battle_info = data[myself]["battle_info"]
        moves = battle_info["moves"]
        if myself == "player":

            # choose = int(input())
            choose = random.randint(1, 4)
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
        else:
            move = "move" + str(random.randint(1, 4))
        # 选其中一个技能
        moveinfo = moves[move]
        print("%s使出了%s" % (pkmon_name, moveinfo["name"]))
        # 计算是否命中
        isHit = self.is_move_accuracy(moveinfo, data, myself, aims)
        if isHit is True:
            # 判断技能类型进行伤害计算后返回计算后的值
            data = self.move_effect(moveinfo, data, myself, aims)

        # 保存伤害计算结果
        FileManager().save_battle_env(data)

    def is_move_accuracy(self, moveinfo, data, myself, aims):
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
        our_info = data[myself]["base_info"]
        enemy_info = data[aims]["base_info"]
        
        move_name = moveinfo["name"]
        accuracy = moveinfo["accuracy"]
        
        our_battle_info = data[myself]["battle_info"]
        our_stat = our_battle_info["statistic_level"]
        our_ac_level = our_stat["命中"]
        
        enemy_bt_info = data[aims]["battle_info"]
        enemy_stat = enemy_bt_info["statistic_level"]
        enmey_av_level = enemy_stat["闪避"]
        


        if accuracy == '—':
            print("必然命中!")
            return True
        if accuracy == '变化':
            if move_name == "角钻":
                accuracy = int(our_info["level"]) - int(enemy_info["level"])
            else:
                accuracy = 101 
        final_level = int(our_ac_level)-int(enmey_av_level)

        if final_level >= 6:
            final_level = 6
        elif final_level <= -6:
            final_level = -6
        final_accuracy = int(
            Statistic().accuracy_level_calc(accuracy, final_level))

        # print("基础命中率为%s \n命中等级为%s \n最终命中率为%d" %
        # (accuracy, final_level, final_accuracy))
        randnum = random.randint(0, 100)
        # print("随机数为%d" % randnum)
        if randnum <= final_accuracy:
            # print("命中")
            return True
        else:
            print("没有命中")
            return False
    #

    def move_effect(self, moveinfo, data, myself, aims):
        '''
        判断是什么类型的招式 物理 特殊 变化,判断有没有异常状态
        '''
        category = moveinfo["category"]
        if category == "物理" or category == "特殊":

            # 计算物理特殊伤害
            data = Damages().damages_calc(moveinfo, data, myself, aims)
            # 计算技能状态效果
            data = self.additional_effect(moveinfo, data, myself, aims)
            # 检测技能的异常效果

        elif category == "变化":
            # 变化伤害
            # print("变化技能")
            # 计算技能状态效果
            data = self.additional_effect(moveinfo, data, myself, aims)
        else:
            pass
        return data

    def additional_effect(self, moveinfo, data, myself, aims):
        '''
        追加技能效果：异常状态、能力等级的上升下降
        '''
        state = moveinfo["state"]
        volatile = state["异常"]
        state_level = state["能力"]
        enemy_info = data[aims]["base_info"]
        attacker_info = data[myself]["base_info"]
        atk_bt_info = data[myself]["battle_info"]
        attacker_statistic = attacker_info["statistic"]
        enemy_name = enemy_info["name"]
        my_name = attacker_info["name"]
        for style, effect in volatile.items():
            if effect != 0:
                # print("有%s效果" % style)
                '''
                判断技能触发追加效果   异常啊技能等级
                '''
                volatile_rate = effect
                
                status = atk_bt_info["status"]
                randnum = random.randint(0, 100)
                # print("随机数为%s" % randnum)
                if randnum <= volatile_rate:
                    print("%s%s了" % (enemy_name, style))
                    status["volatile"] = style
                else:
                    # print("没有命中异常状态")
                    pass
                atk_bt_info["status"] = status
        for style, level in state_level.items():
            if level != 0:
                '''
                判断能力提升降低
                '''
                stat_level = atk_bt_info["statistic_level"][style]

                if style == '命中' or style == '闪避':
                    pass
                else:
                    lv_times = Statistic().stat_level_calc(level, stat_level, 
                                                           my_name, style)
                    print("原%s值为%s" % (style, attacker_statistic[style]))
                    value = attacker_statistic[style]                                    
                    atk_bt_info["battle_statistic"][style] = int(
                        value * lv_times)
                    
                    print("提升后%s值为%s" %
                          (style, atk_bt_info["battle_statistic"][style]))
                    
                    stat_level += level
                    atk_bt_info["statistic_level"][style] = stat_level
                    
        return data
