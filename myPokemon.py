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
from fileManager import InitConfig
from generateMoves import GenerateMove
from packagePokemon import BattlePokemon
import numpy as np


class MyPkmon():

    MY_POKEMON_FILE = 'mypkmon.csv'

    def get_my_pkmon(self):
        data = InitConfig().get_data(self.MY_POKEMON_FILE)
        # 随机取出一行数据(取队列第一只精灵)
        pkmon_raw = data.loc[0:5].values[0]
        moves_dict = GenerateMove().random_moves()
        try:
            np.isnan(pkmon_raw[4])
            pkmon_raw[4] = ""
        except Exception:
            pass
        mypkmon = BattlePokemon().package_pkmon(
            pkmon_raw[0], pkmon_raw[1], pkmon_raw[2], pkmon_raw[3],
            pkmon_raw[4], pkmon_raw[5], pkmon_raw[6], pkmon_raw[7],
            pkmon_raw[8], pkmon_raw[9], pkmon_raw[10], pkmon_raw[11],
            pkmon_raw[12], pkmon_raw[13], pkmon_raw[14], pkmon_raw[15],
            pkmon_raw[16], pkmon_raw[17], moves_dict)

        return mypkmon
