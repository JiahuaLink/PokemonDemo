#!/usr/bin/env/python
# -*- encoding: utf-8 -*-
'''
@File    :   battleManage.py
@Time    :   2019/11/23 22:58:48
@Author  :   lijaihua
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

# here put the import lib

import pandas as pd
path = "D:/python/pkmon/battle.xls" 
data = pd.DataFrame(pd.read_excel(path))

# 获取行名为0这一行的内容
# 获取行为 2 列为2 的值，即格斗对一般的伤害

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
    '超能': '14',
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


def damage_result_display(damageTimes):
    if damageTimes == '0':
        print("没有效果")
    elif damageTimes == '0.5':
        print("几乎没有效果..")
    elif damageTimes == '1.0':
        print("效果一般")
    elif damageTimes == '2.0':
        print("效果拔群!")
    else:
        pass


for i in range(1, 18):
    for j in range(1, 18):

        atkType = str(data.loc[i - 1].values[0])
        enemyType = str(data.columns[j])
        damageTimes = str(data.loc[i - 1].values[j])
        if (damageTimes == '0.5'):
            print(atkType + "对" + enemyType + "的伤害是" + damageTimes + "倍")
            damage_result_display(damageTimes)