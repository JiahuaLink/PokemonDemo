#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fileManager.py
@Time    :   2019/11/25 21:50:11
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   csv表格，json读写处理
'''

import pandas as pd
import csv
import sys
import json
import os


class FileManager():
    BATTLE_INFO = 'battleinfo.json'
    RANDOMPKMON = "randompkmon.csv"
    logfile = "pokemon.log"
    abspath = sys.path[0]
    BATTLE_FILE = os.path.join(abspath, 'config', BATTLE_INFO)
    RANDOMPKMON_CSV = os.path.join(abspath, 'config', RANDOMPKMON)
    LOG_FILE = os.path.join(abspath, 'log', logfile)

    def save2file(self, file, data):
        ''' 将数据保存到文件'''

        fd = open(file, 'a+', encoding='utf-8-sig', newline='')
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)
        fd.close()

    def open_battle_env(self):
        file = open(self.BATTLE_FILE, 'r', encoding='utf-8-sig')
        js = file.read()
        dic = json.loads(js)
        file.close()
        return dic

    def save_battle_env(self, dic):
        js = json.dumps(dic, ensure_ascii=False)
        file = open(self.BATTLE_FILE, 'w', encoding='utf-8-sig')
        file.write(js)
        file.close()

    def save2randompkmon(self, dic):
        fd = open(self.RANDOMPKMON_CSV, 'a+', encoding='utf-8-sig', newline='')

        writer = csv.writer(fd)
        for item in dic:
            writer.writerow(item)
        fd.close()

    def save2log(self, text):
        f = open(self.LOG_FILE, 'a+', encoding='utf-8-sig')
        f.write(text)
        f.write("\n")
        f.close()


class InitConfig():

    def get_data(self, file):
        abspath = sys.path[0]
        path = os.path.join(abspath, 'config', file)
        # header==None 没有标题行
        data = pd.DataFrame(pd.read_csv(path))
        return data
