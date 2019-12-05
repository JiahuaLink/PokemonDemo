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
import datetime
from randomPokemon import RandomPkmon
from battleRoom import BattleRoom
from myPokemon import MyPkmon
from flask import Flask, render_template, request
from fileManager import FileManager
from damageCalculator import DamagesTimes


app = Flask(__name__, static_folder='./source')
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def index():
    now = datetime.datetime.now()
    ip = request.remote_addr

    pokemon = RandomPkmon().random_pkmon()
    info = pokemon["base_info"]
    stats = pokemon["statistic"]
    num = info["num"]
    name = info["name"]
    level = info["level"]
    moves = pokemon["moves"]
    dt = DamagesTimes()
    type_index1 =dt.get_type_index(info["type1"])
    type_index2 = dt.get_type_index(info["type2"])
    gifname = '%s.gif' % num
    # moves=pokemon["moves"]
    move_index1=dt.get_type_index(moves["move1"]["type"])
    move_index2=dt.get_type_index(moves["move2"]["type"])
    move_index3=dt.get_type_index(moves["move3"]["type"])
    move_index4=dt.get_type_index(moves["move4"]["type"])
    
    
    

    context = "%s 用户%s 遇到了 LV.%s %s" % (now, ip, level, name)
    FileManager().save2log(context)
    return render_template('index.html', filename=gifname,info=info,pokemon=stats,type_index1=type_index1, type_index2=type_index2, moves=moves,move_index1=move_index1,move_index2=move_index2,move_index3=move_index3,move_index4=move_index4)


if __name__ == "__main__":
    # 随机生成一只宝可梦,进入对战空间
    pokemon = RandomPkmon().random_pkmon()
    mypkmon = MyPkmon().get_my_pkmon()
    # print(pokemon)
    #BattleRoom().battlewith(mypkmon, pokemon)
    app.run(host="127.0.0.1", port=8000, debug=True)
