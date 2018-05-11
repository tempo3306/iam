import numpy as np
import urllib
import cv2
import win32gui
import win32con
import win32ui
import numpy as np
from PIL import Image

#
# url = 'http://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png'
# resp = urllib.urlopen(url)
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# cv2.imshow('URL2Image', image)
# cv2.waitKey()

def new_screenshot(area):  # x,y  pos      w,h size
    x, y = area[0], area[1]
    w, h = area[2], area[3]
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()

    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
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
    return img


if __name__ == '__main__':
    new_screenshot((0, 0, 1366, 768))