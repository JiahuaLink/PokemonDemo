#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battleProcess.py
@Time    :   2019/11/28 22:53:50
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   战斗进程实现
'''

# here put the import lib
import time
import threading
from playerControls import PlayerControls


class BattleProcess():
    lockPlayer = threading.Lock()
    lockEnemy = threading.Lock()

    def player_rounds(self, data):
        if data["player"]["hp_value"] <= 0:
            
            return
        self.lockPlayer.acquire()
        print("%s要做什么？\n【攻击】【背包】【精灵】【逃跑】\n" % data["player"]["pkmon_name"])
        choose = int(input())
        PlayerControls().playcontrols(choose, data)
        self.lockEnemy.release()
        time.sleep(0.1)
        self.player_rounds(data)

    def enemy_rounds(self, data):
        if data["enemy"]["hp_value"] <= 0:
            
            print("敌方倒下")
            return
        self.lockEnemy.acquire()
        print("%s发起了攻击" % data["enemy"]["pkmon_name"])
        self.lockPlayer.release()
        time.sleep(0.1)
        self.enemy_rounds(data)

    def start(self, data):
        self.lockEnemy.acquire()
        t1 = threading.Thread(target=self.player_rounds, args=(data, ))
        t2 = threading.Thread(target=self.enemy_rounds, args=(data, ))
        t1.start()
        t2.start()
        t1.join()
        t2.join()