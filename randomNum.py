#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   randomNum.py
@Time    :   2019/11/25 21:54:49
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   随机计算能力
'''
import random
import numpy as np


class RandomNum():
    def random_num(self, index):
        return random.randint(0, index)

    def random_index(self, arr, rate):
        """随机变量的概率函数"""
        #
        # 参数rate为list<int>
        # 返回概率事件的下标索引
        index = 0
        np.random.seed(0)
        p = np.array(rate)
        index = np.random.choice(arr, p=p.ravel())
        return index

    def random_individual_value(self, index):
        # 随机六项个体值
        return[random.randint(0, index)for _ in range(6)]
