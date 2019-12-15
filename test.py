
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/12/15 11:46:04
@Author  :   Jawa
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   None
'''

import threading
import time
lockA=threading.Lock()
lockB=threading.Lock()
def printA(n):
  if n<0:
    return
  lockA.acquire()
  print("+++")
  lockB.release()
  time.sleep(0.1)
  printA(n-1)
def printB(n):
  if n<0:  
    return
  lockB.acquire()
  print("***")
  lockA.release()
  time.sleep(0.2)
  printB(n-1) 
 
lockB.acquire()
t1=threading.Thread(target=printA,args=(10,))
t2=threading.Thread(target=printB,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()