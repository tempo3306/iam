# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/27 13:39
'''
import numpy as np
import cv2
import win32gui
import win32ui
import win32con
import time
import pyautogui as pg

from PIL import Image, ImageGrab

Px_lowestprice = 307
Py_lowestprice = 448



global Position, refresh_area, confirm_area, Pos_timeframe, Pos_controlframe, Pos_yanzhengma, Pos_yanzhengmaframe, yan_confirm_area

Pos_yanzhengma=[612, 391, 792, 501]
yanconfirm=[432, 466, 792, 566]
refresh_area=[553, 359, 853, 559]
lowest=[307, 448, 389, 464]
confirm_area=[732, 466, 892, 566]

cal_area = [lowest,refresh_area,confirm_area,Pos_yanzhengma,yanconfirm]
use_area = []


##得到use_area




sc_area = [Px_lowestprice - 10, Py_lowestprice - 100, Px_lowestprice + 500, Py_lowestprice + 120]


def screenshot():
    img = ImageGrab.grab(area)
    # img.save("f.png")


def only_screenshot():  # x,y  pos      w,h size
    x, y = area[0], area[1]
    w, h = area[2], area[3]
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w - x, h - y)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((-x, -y), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    # dataBitMap.SaveBitmapFile(cDC, "foo.png")
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    bmpinfo = dataBitMap.GetInfo()
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        im, 'raw', 'RGBX', 0, 1)
    # cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转灰度
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return img


def cut_img():  # 将所得的img 处理成  lowestprice_img   confirm_img  yanzhengma_confirm_img  refresh_img
    img = only_screenshot()  # 获取得到的截图
    # 切片
    img = np.asarray(img)  # 转化为numpy数组
    imgpos_lowestprice =img[ use_area[0][0]:use_area[0][2], use_area[0][2]:use_area[0][3] ]
    imgpos_refresh = img[ use_area[1][0]:use_area[1][2], use_area[1][2]:use_area[1][3] ]
    imgpos_confirm = img[ use_area[2][0]:use_area[2][2], use_area[2][2]:use_area[2][3] ]
    impos_yanzhengma = img[ use_area[3][0]:use_area[3][2], use_area[3][2]:use_area[3][3] ]
    imgpos_yanzhengmaconfirm = img[ use_area[4][0]:use_area[4][2], use_area[4][2]:use_area[4][3] ]

    print("imgpos_lowestprice = ",imgpos_lowestprice)
    print("imgpos_refresh = ",imgpos_refresh)
    print("imgpos_confirm = ",imgpos_confirm)
    print("impos_yanzhengma = ",impos_yanzhengma)
    print("imgpos_yanzhengmaconfirm = ",imgpos_yanzhengmaconfirm)



# import time
#
# total1 = 0
# total2 = 0
# for i in range(1000):
#     a = time.clock()
#     new_screenshot()
#     # img=ImageGrab.grab()
#     b = time.clock()
#     print(b - a)
#     total1 += b - a
#
# for i in range(1000):
#     a = time.clock()
#     screenshot()
#     b = time.clock()
#     print(b - a)
#     total2 += b - a
# print("total1", total1)
# print("total2", total2)
