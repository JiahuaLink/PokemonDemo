#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   generateMoves.py
@Time    :   2019/11/29 22:25:51
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   技能列表生成，
        1、所学技能不能超出属性范围
        2、可学技能不能高于当前等级
'''

# here put the import lib
from fileManager import InitConfig
import random


class GenerateMove():

    MOVE_FILE = "moves.csv"

    def random_moves(self):
        # print(random.randint(0,9))
        # 随机生成的技能编号不超过最大值
        data = InitConfig().get_data(self.MOVE_FILE)
        maxnum = data.shape[0] - 1
        # 循环生成4个技能
        moves = {}
        for num in range(1, 5):
            # 获取技能编号
            move_num = random.randint(0, maxnum)
            # 随机取出一行数据(随机获取一个技能)
            move_raw = data.loc[0:maxnum].values[move_num]
            move = self.produce_move(move_raw, num)
        # 四个技能存入技能字典
            move_no = "move" + str(num)
            moves[move_no] = move
        # print("总技能%s" % moves)
        return moves

    def produce_move(self, move_raw, num):
        # 编号
        move_num = move_raw[0]
        # 名称
        move_name = move_raw[1]
        # 属性类型
        move_type = move_raw[3]
        # 分类  物理/特殊/变化  变化用——表示
        move_category = move_raw[4]
        # 伤害
        move_power = move_raw[5]
        # 命中率
        move_accuracy = move_raw[6]
        # 技能点数
        move_pp = move_raw[7]
        
        

        died = move_raw[8]
        # 异常状态 中毒,烧伤,麻痹,睡眠,冰冻获取命中率
        # 中毒
        poison = move_raw[9]
        # 烧伤
        burn = move_raw[10]
        # 麻痹
        paralysis = move_raw[11]
        # 睡眠
        sleep = move_raw[12]
        # 冰冻
        freeze = move_raw[13]
        #
        volatile = {
            "中毒": poison,
            "灼伤": burn,
            "麻痹": paralysis,
            "睡眠": sleep,
            "冰冻": freeze,
        }
        # 选择技能
        # print("技能%d:%s" % (num, move_name))

        # print(" 编号:%s\n名称:%s\n 属性类型:%s\n 分类:%s\n 伤害:%s\n 命中率:\n 技能点数:%s\n" %
        #       (move_num, move_name, move_type, move_power, move_category,
        #        move_accuracy, move_pp))
        move = {
            "id": move_num,
            "name": move_name,
            "type": move_type,
            "power": move_power,
            "category": move_category,
            "accuracy": move_accuracy,
            "pp": move_pp,
            "volatile":volatile
        }
        return move
