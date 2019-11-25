#!/usr/bin/env/python
# -*- encoding: utf-8 -*-
'''
@File    :   battleManage.py
@Time    :   2019/11/23 22:58:48
@Author  :   lijaihua
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   属性克制伤害计算器
'''

# here put the import lib

import pandas as pd
import sys


class Damage_Analyse():
    # 获取行名为0这一行的内容
    # 获取行为 2 列为2 的值，即格斗对一般的伤害
    abspath = sys.path[0]
    path = abspath + "\\config\\battle.xls"

    def init_data(self):
        data = pd.DataFrame(pd.read_excel(self.path))
        return data

    dict = {
        '一般': '1',
        '格斗': '2',
        '飞行': '3',
        '毒': '4',
        '地面': '5',
        '岩石': '6',
        '虫 ': '7',
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

    # a = '水'
    # b = '火'

    # atkType = int(dict[a])
    # enemyType = int(dict[b])
    # 第几行  作为攻击方
    # print(data.loc[atkType - 1].values[0])
    # 第几列  被攻击方
    # print(data.columns[enemyType])
    # 输出值
    # print(data.loc[atkType - 1].values[enemyType])

    def damage_result_display(self, damageTimes):
        if damageTimes == '0.0':
            print("没有效果")
        elif damageTimes == '0.5' or damageTimes == '0.25':
            print("效果很小..")
        elif damageTimes == '1.0':
            print("效果一般")
        elif damageTimes == '2.0' or damageTimes == '4.0':
            print("效果拔群!")
        else:
            pass

    def damage_calc(self, arg1, arg2, arg3):
        # 计算实际伤害倍数 attr1 : 我方技能属性  敌方属性attr2, attr3
        damage_times_1 = self.base_damage(arg1, arg2)
        damage_times_2 = self.base_damage(arg1, arg3)
        damageTimes = float(damage_times_1) * float(damage_times_2)
        print("总伤害是%s倍" % damageTimes)
        self.damage_result_display(str(damageTimes))

    def base_damage(self, attr1, attr2):
        # 传入属性名称  输出基本伤害倍数
        data = self.init_data()
        play_index = self.get_type_index(attr1)
        enemy_index = self.get_type_index(attr2)
        # atkType = str(data.loc[play_index - 1].values[0])
        # enemyType = str(data.columns[enemy_index])
        damageTimes = float(data.loc[play_index - 1].values[enemy_index])
        print(attr1 + "对" + attr2 + "的伤害是" + str(damageTimes) + "倍")
        self.damage_result_display(damageTimes)
        return damageTimes

    # 获取该属性的下标值
    def get_type_index(self, attr_name):

        return int(self.dict[attr_name])


if __name__ == "__main__":
    da = Damage_Analyse()
    da.damage_calc("超能力", "草", "毒")
