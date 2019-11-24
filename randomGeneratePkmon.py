#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   randomGeneratePkmon.py
@Time    :   2019/11/24 23:25:28
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

# here put the import lib
import random

import pandas as pd
import csv
import json
path = "D:/python/pkmon/pkmondex.csv"

# 基础能力值
BASE_VALUE = 255
# 个体值
INDIVIDUAL_VALUE = 31
# 最低等级
MIN_LEVEL = 2
# 最大等级
MAX_LEVEL = 4

# 性格修正
CHARACTER_VALUE = 1
# header==None不把第一列作为属性，避免第一行不能用
data = pd.DataFrame(pd.read_csv(path, header=None))


def random_pkmon():
    # print(random.randint(0,9))
    #随机生成的精灵编号不超过最大值
    maxnum = data.shape[0] - 1
    pkmon_num = random.randint(0, maxnum)
    print(maxnum, pkmon_num)
    #随机取出一行数据(随机获取一只精灵)
    pkmon_raw = data.loc[0:maxnum].values[pkmon_num]
    produce_pkmon(pkmon_raw)


def random_num(index):
    return random.randint(0, index)


def produce_pkmon(pkmon_raw):
    serialNum = pkmon_raw[0]
    pkmon_name = pkmon_raw[1]
    pkmon_type1 = pkmon_raw[2]
    pkmon_type2 = (pkmon_raw[3] if pkmon_raw[3]!="NaN" else "")
    
    ability = ability_selector(pkmon_raw[4], pkmon_raw[5], pkmon_raw[6])
    level = lv_selector()
    hp_value = hp_selector(pkmon_raw[7], level)
    atk_value = stat_selector(pkmon_raw[8], level)
    atk_sp_value = stat_selector(pkmon_raw[9], level)
    defend_value = stat_selector(pkmon_raw[10], level)
    defend_sp_value = stat_selector(pkmon_raw[11], level)
    speed_value = stat_selector(pkmon_raw[12], level)
    #print("HP:%s\natk_value:%s\natk_sp_value:%s\ndefend_value:%s\ndefend_sp_value:%s\nspeed_value:%s\n" % hp_value, atk_value, defend_value, atk_sp_value, defend_sp_value, speed_value)
    print(serialNum, pkmon_name, pkmon_type1, pkmon_type2, ability, level,
          hp_value, atk_value, defend_value, atk_sp_value, defend_sp_value,
          speed_value)


def lv_selector():
    level = random.randint(MIN_LEVEL, MAX_LEVEL)
    #等级为
    print("等级为%s" % level)
    return level


#随机选择特性
def ability_selector(ab1, ab2, ab3):
    ability=""
    if ab2 == "NaN":
        arr = [ab1, ab2, ab3]
        rate = [75, 0, 25]
    else:
        arr = [ab1, ab2, ab3]
        rate = [45, 30, 25]
    if arr[random_index(rate)] == ab1:
        ability = ab1
        print("草丛中冒出了一只普通特性1:%s" % ability)
    if arr[random_index(rate)] == ab2:
        ability = ab2
        print("草丛中冒出了一只普通特性2:%s" % ability)
    if arr[random_index(rate)] == ab3:
        ability = ab3
        print("草丛中冒出了一只隐藏特性:%s" % ability)

    return ability


def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        print(start, scope)
        if randnum <= start:
            break
    print(index)
    return index


def hp_selector(hp_value, level):

    hp_values = int((hp_value * 2 + random_num(INDIVIDUAL_VALUE) * 2 +
                     random_num(BASE_VALUE) / 4) * level / 100 + 10 + level)
    
    return hp_values


#攻击特攻防御特防速度能力值
def stat_selector(value, level):

    values = int(((value * 2 + random_num(INDIVIDUAL_VALUE) +
                   random_num(BASE_VALUE) / 4) * level / 100 + 10 + 5) *
                 CHARACTER_VALUE)
    
    return values


# data = parse4data(pkmonHtml)

# data = zip(serialNum, pkmon_name, pkmon_type1, pkmon_type2, ability1,
#                ability2, hidden_ability, hp_value, atk_value, defend_value,
#                atk_sp_value, defend_sp_value, speed_value)
#     return data
# save2file(fm, fd, data)


# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('pkmondex.txt', 'w', encoding='utf-8')
    elif fm == 'json':
        fd = open('pkmondex.json', 'w', encoding='utf-8')
    elif fm == 'csv':
        fd = open('randompkmon.csv', 'w', encoding='utf-8', newline='')
    return fd


# 将数据保存到文件
def save2file(fm, fd, data):
    fd = openfile(fm)
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('agree：' + str(item[0]) + '\n')
            fd.write('authod：' + str(item[1]) + '\n')
            fd.write('star：' + str(item[2]) + '\n')
            fd.write('content：' + str(item[3]) + '\n')
    if fm == 'json':
        temp = ('agree', 'authod', 'star', 'content')
        for item in data:
            json.dump(dict(zip(temp, item)), fd, ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)
    fd.close()
    print('结束爬取')


random_pkmon()