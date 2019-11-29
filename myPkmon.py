#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   myPkmon.py
@Time    :   2019/11/26 23:24:04
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   获取自己的精灵
'''

# here put the import lib
import fileManager as fl
from generateMoves import GenerateMove

class MyPkmon():

    MY_POKEMON_FILE = 'mypkmon.csv'

    def get_my_pkmon(self):
        data = fl.IninConfig().get_data(self.MY_POKEMON_FILE)
        # 随机取出一行数据(取队列第一只精灵)
        pkmon_raw = data.loc[0:5].values[0]
        mypkmon = self.dict_to_pkmon(pkmon_raw)
        return mypkmon

    def dict_to_pkmon(self, pkmon_raw):
        moves_dict = GenerateMove().random_moves()
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
            "speed_v": pkmon_raw[17],
            "moves":moves_dict
        }
        return pkmon_dict
