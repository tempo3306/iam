# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/26 10:55
'''
import win32gui
import win32ui
import win32con
import time
import numpy as np
from PIL import Image
import cv2
time.sleep(1)
w=1366
h=768
w1=1070
h1=600
x=670
y=340

a=time.clock()
def screen1():
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w1-x, h1-y)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((-x,-y),(w1, h1) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, "f.png")
    # Free Resources



    dcObj.DeleteDC()
    cDC.DeleteDC()
    # win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())



def screen2():
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, 500, 500)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (500, 500), dcObj, (0, 0), win32con.SRCCOPY)
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    bmpinfo = dataBitMap.GetInfo()
    c=time.clock()
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
       im, 'raw', 'BGRX', 0, 1)
    img=np.array(img)
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("ft.png",img)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

total=0
for i in range(1):
    a=time.clock()
    screen2()
    b=time.clock()
    print(b-a)
    total+=b-a
print(total/50)