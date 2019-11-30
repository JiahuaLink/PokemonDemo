#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   randomGeneratePkmon.py
@Time    :   2019/11/24 23:25:28
@Author  :   Jawa,
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   随机生成宝可梦，包含各项基础数值（随机生成个体值）
'''

# here put the import lib
import random
from fileManager import InitConfig, FileManager
import randomStats as selector
from generateMoves import GenerateMove
import numpy as np


class RanomPkmon():
    PKMONDEX_FILE = "pkmondex.csv"

    def random_pkmon(self):
        # print(random.randint(0,9))
        # 随机生成的精灵编号不超过最大值
        data = InitConfig().get_data(self.PKMONDEX_FILE)
        maxnum = data.shape[0] - 1
        pkmon_num = random.randint(0, maxnum)
        # print(maxnum, pkmon_num)
        # 随机取出一行数据(随机获取一只精灵)
        pkmon_raw = data.loc[0:maxnum].values[pkmon_num]
        wild_pkmon = self.produce_pkmon(pkmon_raw)
        return wild_pkmon

    def produce_pkmon(self, pkmon_raw):
        select = selector.Selector()
        serial_num = pkmon_raw[0]
        pkmon_name = pkmon_raw[1]
        pkmon_type1 = pkmon_raw[2]

        pkmon_type2 = pkmon_raw[3]
        try:
            np.isnan(pkmon_type2)
            pkmon_type2 = ""
        except Exception:
            pass
        ability = select.ability_selector(pkmon_raw[4], pkmon_raw[5],
                                          pkmon_raw[6])
        level = select.lv_selector()
        hp_value = select.hp_selector(pkmon_raw[7], level)
        atk_value = select.stat_selector(pkmon_raw[8], level)
        atk_sp_value = select.stat_selector(pkmon_raw[9], level)
        defend_value = select.stat_selector(pkmon_raw[10], level)
        defend_sp_value = select.stat_selector(pkmon_raw[11], level)
        speed_value = select.stat_selector(pkmon_raw[12], level)

        # 选择技能
        moves_dict = GenerateMove().random_moves()
        hp_v, atk_v, defend_v, atk_sp_v, defend_sp_v, speed_v = select.individual_selector(
        )

        print("草丛里跳出了一只\n【LV.%s %s】【属性 %s %s】\n" %
              (level, pkmon_name, pkmon_type1, pkmon_type2))
        # print(
        #     " 编号:%s\n 等级:lv.%s\n 名字:%s\n 属性:%s %s\n 特性:%s\n 能力值:\n 体力:%s\n 攻击:%s\n 防御:%s\n 特攻:%s\n 特防:%s\n 速度:%s\n 个体值:\n 攻击:%s\n 防御:%s\n 特攻:%s\n 特防:%s\n 防御:%s\n 速度:%s\n 技能:%s\n"
        #     % (serial_num, level, pkmon_name, pkmon_type1, pkmon_type2,
        #        ability, hp_value, atk_value, defend_value, atk_sp_value,
        #        defend_sp_value, speed_value, hp_v, atk_v, defend_v, atk_sp_v,
        #        defend_sp_v, speed_v, moves_dict))
        # 保存随机精灵到文件
        data = zip([serial_num], [level], [pkmon_name], [pkmon_type1],
                   [pkmon_type2], [ability], [hp_value], [atk_value],
                   [defend_value], [atk_sp_value], [defend_sp_value],
                   [speed_value], [hp_v], [atk_v], [defend_v], [atk_sp_v],
                   [defend_sp_v], [speed_v], [moves_dict])
        FileManager().save2randompkmon(data)
        wild_pkmon = {
            "serial_num": serial_num,
            "level": level,
            "pkmon_name": pkmon_name,
            "pkmon_type1": pkmon_type1,
            "pkmon_type2": pkmon_type2,
            "ability": ability,
            "hp_value": hp_value,
            "atk_value": atk_value,
            "defend_value": defend_value,
            "atk_sp_value": atk_sp_value,
            "defend_sp_value": defend_sp_value,
            "speed_value": speed_value,
            "hp_v": hp_v,
            "atk_v": atk_v,
            "defend_v": defend_v,
            "atk_sp_v": atk_sp_v,
            "defend_sp_v": defend_sp_v,
            "speed_v": speed_v,
            "moves": moves_dict
        }
        return wild_pkmon