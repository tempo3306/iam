import numpy as np
import urllib
import cv2
import win32gui
import win32con
import win32ui
import numpy as np


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


    dataBitMap.CreateCompatibleBitmap(dcObj, x, y)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (x, y), dcObj, (0, 0), win32con.SRCCOPY)
    bmpinfo = dataBitMap.GetInfo()
    x = bmpinfo['bmWidth']
    y = bmpinfo['bmHeight']
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    im = np.asarray(bytearray(im), dtype="uint8").reshape(x, y)
    print(im)

    # im = np.fromstring(im, np.uint8)

    img = cv2.imdecode(im, cv2.IMREAD_COLOR)
    cv2.imwrite('URL.png', img)
    # bmpinfo = dataBitMap.GetInfo()
    # img = Image.frombuffer(
    #     'RGB',
    #     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    #     im, 'raw', 'RGBX', 0, 1).convert('L')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return img


if __name__ == '__main__':
    new_screenshot((100, 100, 200, 200))