import time
import win32gui, win32api, win32ui, win32con

import mss
import numpy
import cv2
import numpy as np


def take_screenshot1():
    hwnd = win32gui.FindWindow(None, "win32")

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, 500, 500)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (500, 500), dcObj, (0, 0), win32con.SRCCOPY)

    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    img = np.array(im)
    cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    print(img)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


take_screenshot1()


# with mss.mss() as sct:
#     monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 640}
#     img = numpy.array(sct.grab(monitor))
#     print(img)




#
# def window_capture(filename):
#     t = time.time()
#     # hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
#     # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
#     hwnd = win32gui.FindWindow(None, "win32")
#     hwndDC = win32gui.GetWindowDC(hwnd)
#     # 根据窗口的DC获取mfcDC
#     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
#     # mfcDC创建可兼容的DC
#     saveDC = mfcDC.CreateCompatibleDC()
#     # 创建bigmap准备保存图片
#     saveBitMap = win32ui.CreateBitmap()
#     # 获取监控器信息
#     MoniterDev = win32api.EnumDisplayMonitors(None, None)
#     w = MoniterDev[0][2][2]
#     h = MoniterDev[0][2][3]
#     # 为bitmap开辟空间
#     saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
#     # 高度saveDC，将截图保存到saveBitmap中
#     saveDC.SelectObject(saveBitMap)
#
#     # 截取从左上角（0，0）长宽为（w，h）的图片
#     saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
#     saveBitMap.SaveBitmapFile(saveDC, filename)
#
# window_capture('2.png')