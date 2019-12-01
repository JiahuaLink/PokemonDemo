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

import os
from randomPokemon import RanomPkmon
from battleRoom import BattleRoom
from myPokemon import MyPkmon
from flask import Flask, render_template


app = Flask(__name__, static_folder='./source')
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def index():

    pokemon = RanomPkmon().random_pkmon()

    serial_num = pokemon["serial_num"]
    level = pokemon["level"]
    pkmon_name = pokemon["pkmon_name"]
    pkmon_type1 = pokemon["pkmon_type1"]
    pkmon_type2 = pokemon["pkmon_type2"]
    ability = pokemon["ability"]
    hp_value = pokemon["hp_value"]
    atk_value = pokemon["atk_value"]
    defend_value = pokemon["defend_value"]
    atk_sp_value = pokemon["atk_sp_value"]
    defend_sp_value = pokemon["defend_sp_value"]
    speed_value = pokemon["speed_value"]

    gifname = '%s.gif' % serial_num
    # moves=pokemon["moves"]
    # move1=moves["move1"]

    return render_template('index.html', filename=gifname, serial_num=serial_num, pkmon_name=pkmon_name,level=level, pkmon_type1=pkmon_type1, pkmon_type2=pkmon_type2, ability=ability, hp_value=hp_value, atk_value=atk_value, defend_value=defend_value, atk_sp_value=atk_sp_value, defend_sp_value=defend_sp_value, speed_value=speed_value)


if __name__ == "__main__":
    # 随机生成一只宝可梦,进入对战空间

    mypkmon = MyPkmon().get_my_pkmon()
    # print(pokemon)
    # BattleRoom().battlewith(mypkmon, pokemon)
    app.run(host="127.0.0.1", port=8000, debug=True)