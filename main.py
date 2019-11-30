#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/11/30 23:14:10
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   主函数
'''

from randomPokemon import RanomPkmon
from battleRoom import BattleRoom

if __name__ == "__main__":
    rp = RanomPkmon()
    # 随机生成一只宝可梦,进入对战空间
    pokemon = rp.random_pkmon()
    # print(pokemon)
    BattleRoom().battlewith(pokemon)

