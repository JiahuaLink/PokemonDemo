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
    moves = pokemon["moves"]

    gifname = '%s.gif' % serial_num
    # moves=pokemon["moves"]
    # move1=moves["move1"]

    return render_template('index.html', filename=gifname,pokemon=pokemon,moves=moves )


if __name__ == "__main__":
    # 随机生成一只宝可梦,进入对战空间
    pokemon = RanomPkmon().random_pkmon()
    mypkmon = MyPkmon().get_my_pkmon()
    # print(pokemon)
    #BattleRoom().battlewith(mypkmon, pokemon)
    app.run(host="127.0.0.1", port=8000, debug=True)
