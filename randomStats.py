#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   randomStats.py
@Time    :   2019/11/25 21:57:08
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   能力值生成器，根据相关逻辑计算方式生成能力值
'''
import random
import numpy as np
import randomNum


# here put the import lib
class Selector():
    # 基础能力值
    BASE_VALUE = 255
    # 个体值
    INDIVIDUAL_VALUE = 31
    # 最低等级
    MIN_LEVEL = 2
    # 最大等级
    MAX_LEVEL = 40

    # 性格修正
    CHARACTER_VALUE = 1

    def lv_selector(self):
        level = random.randint(self.MIN_LEVEL, self.MAX_LEVEL)
        # 等级为
        # print("等级为%s" % level)
        return level

    # 随机选择特性
    def ability_selector(self, ab1, ab2, ab3):
        ability = ""
        try:
            np.isnan(ab2)
            arr = [0, 1, 2]
            rate = [0.95, 0, 0.05]
        except Exception:
            arr = [0, 1, 2]
            rate = [0.5, 0.45, 0.05]
        if arr[randomNum.RandomNum().random_index(arr, rate)] == 0:
            ability = ab1
            # print("草丛中冒出了一只普通特性1:%s" % ability)
        if arr[randomNum.RandomNum().random_index(arr, rate)] == 1:
            ability = ab2
            # print("草丛中冒出了一只普通特性2:%s" % ability)
        if arr[randomNum.RandomNum().random_index(arr, rate)] == 2:
            ability = ab3
            # print("草丛中冒出了一只隐藏特性:%s" % ability)

        return ability

    def hp_selector(self, hp_value, level):

        hp_values = int(
            (hp_value * 2 +
             randomNum.RandomNum().random_num(self.INDIVIDUAL_VALUE) * 2 +
             randomNum.RandomNum().random_num(self.BASE_VALUE) / 4) * level /
            100 + 10 + level)

        return hp_values

    # 攻击特攻防御特防速度能力值
    def stat_selector(self, value, level):

        values = int(
            ((value * 2 +
              randomNum.RandomNum().random_num(self.INDIVIDUAL_VALUE) +
              randomNum.RandomNum().random_num(self.BASE_VALUE) / 4) * level /
             100 + 10 + 5) * self.CHARACTER_VALUE)

        return values

    def individual_selector(self):
        return randomNum.RandomNum().random_individual_value(
            self.INDIVIDUAL_VALUE)
