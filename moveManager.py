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
from damageTimes import Damage_Analyse
from randomNum import RandomNum


class MoveManager():
    # 随机修正值
    RANDOM_CORRECTION_VALUE = 255

    # 技能选择
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
        enmey_name = data["enemy"]["pkmon_name"]
        moves = data["player"]["moves"]
        # 选其中一个技能 进行伤害计算
        moveinfo = moves[move]
        print("%s使出了%s" % (pkmon_name, moveinfo["name"]))
        # 计算伤害
        damage = self.damages_calc(moveinfo, data)
        data["enemy"]["hp_value"] -= damage
        print("%s受到%d点伤害" % (enmey_name, damage))
        FileManager().save_battle_env(data)
        pass

    # 计算伤害
    def damages_calc(self, moveinfo, data):
        ''' 伤害计算流程
            1读取能力值。
            2能力值修正。
            3计算基础伤害。
            4计算属性加成修正。
            5计算属性相克修正。
            6计算随机修正 
         '''

        move_type = moveinfo["type"]
        move_power = int(moveinfo["power"])
        move_category = moveinfo["category"]
        move_accuracy = int(moveinfo["accuracy"])
        move_pp = int(moveinfo["pp"])

        our_level = int(data["player"]["level"])
        own_type1 = data["player"]["pkmon_type1"]
        own_type2 = data["player"]["pkmon_type2"]
        own_hp = int(data["player"]["hp_value"])
        own_atk = int(data["player"]["atk_value"])
        own_defend = int(data["player"]["defend_value"])
        own_atk_sp = int(data["player"]["atk_sp_value"])
        own_defend_sp = int(data["player"]["defend_sp_value"])
        own_speed = int(data["player"]["speed_value"])

        enemy_level = int(data["enemy"]["level"])
        enemy_type1 = data["enemy"]["pkmon_type1"]
        enemy_type2 = data["enemy"]["pkmon_type2"]
        enemy_hp = int(data["enemy"]["hp_value"])
        enemy_atk = int(data["enemy"]["atk_value"])
        enemy_defend = int(data["enemy"]["defend_value"])
        enemy_atk_sp = int(data["enemy"]["atk_sp_value"])
        enemy_defend_sp = int(data["enemy"]["defend_sp_value"])
        enemy_speed = int(data["enemy"]["speed_value"])
        
        print("敌方体力为%d" % enemy_hp)
        level, atk, defend = self.read_stats(our_level, move_category, own_atk, own_atk_sp, enemy_defend, enemy_defend_sp)
        base_damage = self.calc_base_damage(level, move_power, atk, defend)
        bonuses_damage = self.calc_type_bonuses(move_type, own_type1,
                                                own_type2, base_damage)
        times = Damage_Analyse().damage_calc(move_type, enemy_type1,
                                             enemy_type2)
        times_damage = bonuses_damage * times
        damages = self.random_correction_damage(times_damage)
        return damages

    #  读取能力值
    def read_stats(self, our_level, move_category, our_atk, our_atk_sp, enemy_defend,
                   enemy_defend_sp):
        '''
        如果技能是物理属性，取攻击方攻击作为攻击力；如果技能是特殊属性，取攻击方特殊作为攻击力。
        如果技能是物理属性，取防御方防御作为防御力；如果技能是特殊属性，取防御方特殊作为防御力
        '''
        atk = 0
        defend = 0
        if move_category == "物理":
            atk = our_atk
            defend = enemy_defend
            print("物理攻击：%d  物理防御：%d" % (atk, defend))
        elif move_category == "特殊":
            atk = our_atk_sp
            defend = enemy_defend_sp
            print("特殊攻击：%d 特殊防御：%d" % (atk, defend))
        elif move_category == "变化":
            print("变化技能")
            
        level = our_level
        
        print("我方等级:%d  攻击力:%d  敌方防御力:%d " % (level, atk, defend))
        return level, atk, defend

    # 计算基础伤害
    def calc_base_damage(self, our_level, move_power, atk, defend):
        '''
        基础伤害＝⌊⌊⌊攻击方等级×2÷5＋2⌋×技能威力×攻击力÷防御力⌋÷50⌋
        如果基础伤害＞997，基础伤害＝997。
        基础伤害＝基础伤害＋2
        '''
        base_damage = (((our_level * 2 / 5 + 2) * move_power * atk / defend) / 50)
        print("基础伤害为%d" % base_damage)
        if base_damage > 997:
            base_damage = 997
        base_damage += 2
        print("修正后基础伤害为%d" % base_damage)

        return base_damage

    # 属性加成修正
    def calc_type_bonuses(self, move_type, own_type1, own_type2, base_damage):
        ''' 
        如果技能属性与攻击方属性之一相同，伤害＝⌊伤害×1.5⌋
        '''
        bonuses_damage = base_damage
        if move_type == own_type1 or move_type == own_type2:
            bonuses_damage *= 1.5
            print("技能属性与攻击方属性相同,伤害为%d" % bonuses_damage)
        return bonuses_damage

    # 随机修正
    def random_correction_damage(self, damage):
        '''
        从0～255中产生随机数R，如果R＜217，重复循环，直到R≥217。
        伤害＝⌊伤害×R÷255⌋
        '''
        r_value = RandomNum().random_num(self.RANDOM_CORRECTION_VALUE)
        print("随机修正值%d\n" % r_value)
        while r_value < 127:
            r_value = RandomNum().random_num(self.RANDOM_CORRECTION_VALUE)
        damage = (damage * r_value / 255)
        print("修正后随机修正值为:%d\n 伤害值为%d\n" % (r_value, damage))
        return damage


class MovesList():
    pass