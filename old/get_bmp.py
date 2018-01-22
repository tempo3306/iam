# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/26 10:50
'''
import cv2
import time
from PIL import Image
import numpy as np
import win32gui
import win32ui
import win32con
import threading




def new_screenshot(area):

    x,y=area[0],area[1]
    w,h=area[2],area[3]
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w-x, h-y)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((-x,-y),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    bmpinfo = dataBitMap.GetInfo()
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        im, 'raw', 'RGBX', 0, 1).convert('L')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


# time.sleep(2)
# # new_screenshot((200,200,500,500))
#
# from PIL import Image
# def openya(num):
#     a=time.clock()
#     img=Image.open("yanzhengma.png")
#     img.save('%s.png'%num)
#     im=Image.open('%s.png'%num)
#     b=time.clock()
#     print(b-a)
# #
# for i in range(19):
#     openya(i)

#
class scthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
    def run(self):
        for i in range(100):
            new_screenshot((400,500,600,600))
            print(i)



thread_list=[]
for i in range(100):
    t=scthread()
    thread_list.append(t)
for i in range(100):
    thread_list[i].start()
for i in range(100):
    thread_list[i].join()
print("over")
