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
import json
import sys


# here put the import lib
class FileManager():
    # 打开文件
    def openfile(self, fm):
        fd = None
        if fm == 'txt':
            fd = open('pkmondex.txt', 'w', encoding='utf-8')
        elif fm == 'json':
            fd = open('pkmondex.json', 'w', encoding='utf-8')
        elif fm == 'csv':
            fd = open('randompkmon.csv',
                      'a+',
                      encoding='utf-8-sig',
                      newline='')
        return fd

    # 将数据保存到文件
    def save2file(self, fm, fd, data):
        fd = self.openfile(fm)
        if fm == 'txt':
            for item in data:
                fd.write('----------------------------------------\n')
                # fd.write('agree：' + str(item[0]) + '\n')
                # fd.write('authod：' + str(item[1]) + '\n')
                # fd.write('star：' + str(item[2]) + '\n')
                # fd.write('content：' + str(item[3]) + '\n')
        if fm == 'json':
            temp = ('agree', 'authod', 'star', 'content')
            for item in data:
                json.dump(dict(zip(temp, item)), fd, ensure_ascii=False)
        if fm == 'csv':
            writer = csv.writer(fd)
            for item in data:
                writer.writerow(item)
        fd.close()
        print('结束爬取')


class IninConfig():
    abspath = sys.path[0]
    path = abspath+"\\config\\pkmondex.csv"
    @classmethod
    def init_data(self):
        # header==None不把第一列作为属性，避免第一行不能用
        data = pd.DataFrame(pd.read_csv(self.path, header=None))
        return data
