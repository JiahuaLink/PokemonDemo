#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fileManager.py
@Time    :   2019/11/25 21:50:11
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   csv表格处理
'''

import pandas as pd
import csv
import sys
import json


# here put the import lib
class FileManager():

    # 将数据保存到文件
    def save2file(self, file, data):
        # 打开文件
        fd = open(file, 'a+', encoding='utf-8-sig', newline='')
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)
        fd.close()

    def open_battle_env(self):
        file = open('batleinfo.txt', 'r')
        js = file.read()
        dic = json.loads(js)
        file.close()
        return dic

    def save_battle_env(self, dic):
        js = json.dumps(dic)
        file = open('batleinfo.txt', 'w')
        file.write(js)
        file.close()


class IninConfig():
    @classmethod
    def get_data(self, file):
        abspath = sys.path[0]
        path = abspath + "\\config\\" + file
        # header==None 没有标题行
        data = pd.DataFrame(pd.read_csv(path))
        return data
