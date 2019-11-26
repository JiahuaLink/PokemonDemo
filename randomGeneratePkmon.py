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

import fileManager as fl
import statSelector as selector
import numpy as np
from battleRoom import BattleRoom


class RanomPkmon():
    PKMONDEX_FILE = "pkmondex.csv"

    def random_pkmon(self):
        # print(random.randint(0,9))
        # 随机生成的精灵编号不超过最大值
        data = fl.IninConfig().get_data(self.PKMONDEX_FILE)
        maxnum = data.shape[0] - 1
        pkmon_num = random.randint(0, maxnum)
        # print(maxnum, pkmon_num)
        # 随机取出一行数据(随机获取一只精灵)
        pkmon_raw = data.loc[0:maxnum].values[pkmon_num]
        wild_pkmon = self.produce_pkmon(pkmon_raw)
        return wild_pkmon

    def dict_to_pkmon(self, pkmon_raw):
        pkmon_dict = {
            "serialNum": pkmon_raw[0],
            "level": pkmon_raw[1],
            "pkmon_name": pkmon_raw[2],
            "pkmon_type1": pkmon_raw[3],
            "pkmon_type2": pkmon_raw[4],
            "ability": pkmon_raw[5],
            "hp_value": pkmon_raw[6],
            "atk_value": pkmon_raw[7],
            "defend_value": pkmon_raw[8],
            "atk_sp_value": pkmon_raw[9],
            "defend_sp_value": pkmon_raw[9],
            "speed_value": pkmon_raw[11],
            "hp_v": pkmon_raw[12],
            "atk_v": pkmon_raw[13],
            "defend_v": pkmon_raw[14],
            "atk_sp_v": pkmon_raw[15],
            "defend_sp_v": pkmon_raw[16],
            "speed_v": pkmon_raw[17]
        }
        return pkmon_dict

    def produce_pkmon(self, pkmon_raw):
        select = selector.Selector()
        serialNum = pkmon_raw[0]
        pkmon_name = pkmon_raw[1]
        pkmon_type1 = pkmon_raw[2]

        pkmon_type2 = (pkmon_raw[3] if pkmon_raw[3] != "NaN" else "")
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
        hp_v, atk_v, defend_v, atk_sp_v, defend_sp_v, speed_v = select.individual_selector(
        )
        print(
            " 编号:%s\n 等级:lv.%s\n 名字:%s\n 属性:%s %s\n 特性:%s\n 能力值:\n 体力:%s\n 攻击:%s\n 防御:%s\n 特攻:%s\n 特防:%s\n 速度:%s\n 个体值:\n 攻击:%s\n 防御:%s\n 特攻:%s\n 特防:%s\n 防御:%s\n 速度:%s\n "
            % (serialNum, level, pkmon_name, pkmon_type1, pkmon_type2, ability,
               hp_value, atk_value, defend_value, atk_sp_value,
               defend_sp_value, speed_value, hp_v, atk_v, defend_v, atk_sp_v,
               defend_sp_v, speed_v))
        # data = zip([serialNum], [level], [pkmon_name], [pkmon_type1], [pkmon_type2],
        #            [ability], [hp_value], [atk_value], [defend_value], [atk_sp_value],
        #            [defend_sp_value], [speed_value], [hp_v], [atk_v], [defend_v],
        #            [atk_sp_v], [defend_sp_v], [speed_v])
        # FILE = 'randompkmon.csv'
        # fl.FileManager().save2file(FILE, data)

        wild_pkmon = {
            "serialNum": serialNum,
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
            "speed_v": speed_v
        }
        return wild_pkmon


if __name__ == "__main__":
    rp = RanomPkmon()
    # 随机生成一只宝可梦,进入对战空间

    pokemon = rp.random_pkmon()
    #print(pokemon)
    BattleRoom().battlewith(pokemon)
