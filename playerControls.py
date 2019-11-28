#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   playerControls.py
@Time    :   2019/11/28 23:03:59
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

# here put the import lib


class PlayerControls():
    def playcontrols(self, choose):
        if choose == 1:
            print("攻击")
            
        elif choose == 2:
            print("背包")
        elif choose == 3:
            print("精灵")
        elif choose == 4:
            print("逃跑")
        else:
            print("命令错误")