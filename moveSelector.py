#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MovesSelector.py
@Time    :   2019/11/29 21:42:19
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   技能选择
'''
from fileManager import FileManager


class MoveSelect():
    
    def select(self, data):
        #
        
        FileManager().save_battle_env(data)
        pass