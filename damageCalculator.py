#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   damageCalculator.py
@Time    :   2019/12/01 20:07:22
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   计算伤害
用法damage_calc("我方技能属性", "敌人属性1", "属性2")
'''

from fileManager import InitConfig
from randomNum import RandomNum


class DamagesTimes():

    # 获取行名为0这一行的内容
    # 获取行为 2 列为2 的值，即格斗对一般的伤害
    POKEMON_TYPE = 'battletype.csv'
    # 根据属性名字找下标
    type_dict = {
        "": '0',
        '一般': '1',
        '格斗': '2',
        '飞行': '3',
        '毒': '4',
        '地面': '5',
        '岩石': '6',
        '虫': '7',
        '幽灵': '8',
        '钢': '9',
        '火': '10',
        '水': '11',
        '草': '12',
        '电': '13',
        '超能力': '14',
        '冰': '15',
        '龙': '16',
        '恶': '17',
        '妖精': '18'
    }

    def base_damage(self, attr1, attr2):
        ''' 传入属性名称  输出基本伤害倍数 '''
        data = InitConfig().get_data(self.POKEMON_TYPE)
        play_index = self.get_type_index(attr1)
        enemy_index = self.get_type_index(attr2)
        # atkType = str(data.loc[play_index - 1].values[0])
        # enemyType = str(data.columns[enemy_index])
        damageTimes = float(data.loc[play_index - 1].values[enemy_index])
        # print(attr1 + "对" + attr2 + "的伤害是" + str(damageTimes) + "倍")
        self.damage_result_display(damageTimes)
        return damageTimes

    # 获取该属性的下标值
    def get_type_index(self, attr_name):
        return int(self.type_dict[attr_name])

    def damage_result_display(self, damageTimes):
        ''' 属性相克效果显示 '''
        if damageTimes == '0.0':
            print("没有效果")
        elif damageTimes == '0.5' or damageTimes == '0.25':
            print("效果很小..")
        elif damageTimes == '1.0':
            # print("")
            pass
        elif damageTimes == '2.0' or damageTimes == '4.0':
            print("效果绝佳!")
        else:
            pass

    def times_calc(self, arg1, arg2, arg3):
        '''
        计算属性克制伤害倍数
        '''
        # 计算实际伤害倍数 attr1 : 我方技能属性  敌方属性attr2, attr3
        damage_times_1 = 1
        damage_times_2 = 1
        damage_times_1 = self.base_damage(arg1, arg2)
        if arg3 == '':
            damage_times_2 = 1
        else:
            damage_times_2 = self.base_damage(arg1, arg3)
        damageTimes = float(damage_times_1) * float(damage_times_2)
        # print("总伤害是%s倍" % damageTimes)
        self.damage_result_display(str(damageTimes))
        return damageTimes


class Damages():
    '''计算最终伤害量'''
    # 随机修正值
    RANDOM_CORRECTION = 255

    def damages_calc(self, moveinfo, data, myself, aims):
        ''' 伤害计算流程
            1读取能力值。
            2能力值修正。
            3计算基础伤害。
            4计算属性加成修正。
            5计算属性相克修正。
            6计算随机修正
         '''

        move_type = moveinfo["type"]
        move_power = 0
        move_pp = moveinfo["pp"]
        if moveinfo["power"] == '变化':
            move_power = 0
        elif moveinfo["power"] == '—':
            move_power = 0
        else:
            move_power = int(moveinfo["power"])
        move_category = moveinfo["category"]
        if move_pp == '—':
            pass
        else:
            moveinfo["pp"] = int(move_pp) - 1 
        our_info = data[myself]["base_info"]
        our_battle_info = data[myself]["battle_info"]
        
        our_level = int(our_info["level"])
        own_type1 = our_info["type1"]
        own_type2 = our_info["type2"]
        our_statistic = our_battle_info["battle_statistic"]
        own_atk = int(our_statistic["攻击"])
        own_atk_sp = int(our_statistic["特攻"])

        enemy_info = data[aims]["base_info"]
        enemy_battle_info = data[aims]["battle_info"]
        enmey_name = enemy_info["name"]
        enemy_type1 = enemy_info["type1"]
        enemy_type2 = enemy_info["type2"]
        enemy_statistic = enemy_battle_info["battle_statistic"]
        enemy_hp = int(enemy_statistic["hp"])
        enemy_defend = int(enemy_statistic["防御"])
        enemy_defend_sp = int(enemy_statistic["特防"])

        print("%s体力为%d" % (enmey_name, enemy_hp))
        level, atk, defend = self.read_stats(
            our_level, move_category, own_atk, own_atk_sp,
            enemy_defend, enemy_defend_sp)
        base_damage = self.calc_base_damage(level, move_power, atk, defend)
        bonuses_damage = self.calc_type_bonuses(move_type, own_type1,
                                                own_type2, base_damage)
        times = DamagesTimes().times_calc(move_type, enemy_type1, enemy_type2)
        times_damage = bonuses_damage * times
        damages = self.random_correction_damage(times_damage)

        print("%s受到%d点伤害" % (enmey_name, damages))
        enemy_battle_info["battle_statistic"]["hp"] -= damages
        
        if enemy_battle_info["battle_statistic"]["hp"] <= 0:
            enemy_battle_info["battle_statistic"]["hp"] = 0
            
            status = enemy_battle_info["status"]
            
            status["died"] = "濒死"
            
            enemy_battle_info["status"] = status
            
        # data[aims]["battle_info"] = enemy_battle_info
        
        return data

    #  读取能力值
    def read_stats(self, our_level, move_category, 
                   our_atk, our_atk_sp, 
                   enemy_defend,
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
            # print("物理攻击：%d  物理防御：%d" % (atk, defend))
        elif move_category == "特殊":
            atk = our_atk_sp
            defend = enemy_defend_sp
            # print("特殊攻击：%d 特殊防御：%d" % (atk, defend))
        elif move_category == "变化":
            # print("变化技能")
            pass

        level = our_level

        # print("我方等级:%d  攻击力:%d  敌方防御力:%d " % (level, atk, defend))
        return level, atk, defend

    # 计算基础伤害
    def calc_base_damage(self, our_level, move_power, atk, defend):
        '''
        基础伤害＝⌊⌊⌊攻击方等级×2÷5＋2⌋×技能威力×攻击力÷防御力⌋÷50⌋
        如果基础伤害＞997，基础伤害＝997。
        基础伤害＝基础伤害＋2
        '''
        base_damage = (((our_level * 2 / 5 + 2) *
                        move_power * atk / defend) / 50)
        # print("基础伤害为%d" % base_damage)
        if base_damage > 997:
            base_damage = 997
        base_damage += 2
        # print("修正后基础伤害为%d" % base_damage)

        return base_damage

    # 属性加成修正
    def calc_type_bonuses(self, move_type, own_type1, own_type2, base_damage):
        ''' 
        如果技能属性与攻击方属性之一相同，伤害＝⌊伤害×1.5⌋
        '''
        bonuses_damage = base_damage
        if move_type == own_type1 or move_type == own_type2:
            bonuses_damage *= 1.5
            #print("技能属性与攻击方属性相同,伤害为%d" % bonuses_damage)
        else:
             #print("技能属性与攻击方属性不同")
             pass
        return bonuses_damage

    # 随机修正
    def random_correction_damage(self, damage):
        '''
        从0～255中产生随机数R，如果R＜217，重复循环，直到R≥217。
        伤害＝⌊伤害×R÷255⌋
        '''
        r = RandomNum().random_num(self.RANDOM_CORRECTION)
        # print("随机修正值%d" % r)
        while r < 127:
            r = RandomNum().random_num(self.RANDOM_CORRECTION)
        damage = (damage * r / 255)
        # print("修正后随机修正值为:%d\n伤害值为%d" % (r, damage))
        return int(damage)

# if __name__ == "__main__":
#     da = DamageAnalyse()
#     da.damage_calc("超能力", "草", "毒")
