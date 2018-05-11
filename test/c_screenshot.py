import  win32gui
import win32ui
import win32con
import win32api
from mss import mss
import numpy as np
import cv2


def grab_screen(region=None, title=None):
    hwin = win32gui.GetDesktopWindow()
    if region:
        left,top,x2,y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    elif title:
        gtawin = win32gui.FindWindow(None, title)
        if not gtawin:
            raise Exception('window title not found')
        #get the bounding box of the window
        left, top, x2, y2 = win32gui.GetWindowRect(gtawin)
        width = x2 - left +1
        height = y2 - top +1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imwrite('n.png', img)



grab_screen()


# def new_screenshot(name):  # x,y  pos      w,h size
#     # hwnd = win32gui.FindWindow(None, windowname)
#     wDC = win32gui.GetWindowDC(0)
#     dcObj = win32ui.CreateDCFromHandle(wDC)
#     cDC = dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, 900, 900)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((0, 0), (900, 900), dcObj, (0, 0), win32con.SRCCOPY)
#     # dataBitMap.SaveBitmapFile(cDC, name)
#     # Free Resources
#     im = dataBitMap.GetBitmapBits(True)  # Tried False also
#     im.shape = ()
#
#
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(0, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())


# def new_screenshot(name):  # x,y  pos      w,h size
#     # hwnd = win32gui.FindWindow(None, windowname)
#     wDC = win32gui.GetWindowDC(0)
#     dcObj = win32ui.CreateDCFromHandle(wDC)
#     cDC = dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, 900, 900)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((0, 0), (900, 900), dcObj, (0, 0), win32con.SRCCOPY)
#     dataBitMap.SaveBitmapFile(cDC, name)
#     # Free Resources
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(0, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())



# if __name__ == '__main__':
    # new_screenshot('5.png')