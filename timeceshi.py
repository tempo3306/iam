# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/21 17:12
'''
import win32con,win32api

def Delete():
    win32api.keybd_event(0x08,0,0,0)
    win32api.keybd_event(0x08,0,win32con.KEYEVENTF_KEYUP, 0)
for i in range(15):
    Delete()