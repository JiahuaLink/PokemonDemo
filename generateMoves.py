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
        # 畏缩
        flinch = move_raw[14]
        # 混乱
        confusion = move_raw[15]
        # 着迷
        infatuation = move_raw[16]
        # 蓄力
        storeforce = move_raw[17]
        # 束缚
        bound = move_raw[18]
        # 硬直
        hardstraight = move_raw[19]
        # atk,defend,atk_sp,defen_sp 命中 闪避等级变化
        atk = move_raw[20]
        defend = move_raw[21]
        atk_sp = move_raw[22]
        defend_sp = move_raw[23]
        speed = move_raw[24]
        accuracy = move_raw[25]
        avoid = move_raw[26]
        
        # 异常列表
        volatile = {
            "中毒": poison,
            "灼伤": burn,
            "麻痹": paralysis,
            "睡眠": sleep,
            "冰冻": freeze,
        }

        # 能力变化
        statistic_level = {
            
            "攻击": atk,
            "防御": defend,
            "特攻": atk_sp,
            "特防": defend_sp,
            "速度": speed,
            "命中": accuracy,
            "闪避": avoid
        }
        # 精灵状态 畏缩，混乱，着迷，蓄力，束缚，硬直
        state = {
            "濒死": died,
            "畏缩": flinch,
            "混乱": confusion,
            "着迷": infatuation,
            "蓄力": storeforce,
            "束缚": bound,
            "硬直": hardstraight,
            "异常": volatile,
            "能力": statistic_level
        }
        move = {
            "id": move_num,
            "name": move_name,
            "type": move_type,
            "power": move_power,
            "category": move_category,
            "accuracy": move_accuracy,
            "pp": move_pp,
            "state": state,

        }
        return move
