'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 10:07
'''
import cv2
import win32gui
import win32ui
import win32con
import win32api
import numpy as np
import time
from component.staticmethod import OnClick_Shuaxin, OnClick_confirm, Smart_chujia, calculate_usetime
from component.variable import V_global
import logging

logger = logging.getLogger()


def cut_pic(img, size, name):
    img = np.asarray(img)
    i1 = img[0:24, :150]
    i2 = img[48:110, 30:]
    im = np.concatenate([i2, i1])
    im = cv2.resize(im, tuple(size))
    cv2.imwrite(name, im)


# def new_screenshot(area):  # x,y  pos      w,h size
#     x, y = area[0], area[1]
#     w, h = area[2], area[3]
#     hwnd = win32gui.FindWindow(None, "win32")
#     wDC = win32gui.GetWindowDC(hwnd)
#     dcObj = win32ui.CreateDCFromHandle(wDC)
#     cDC = dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, x, y)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((0, 0), (x, y), dcObj, (0, 0), win32con.SRCCOPY)
#     im = dataBitMap.GetBitmapBits(True)  # Tried False also
#     bmpinfo = dataBitMap.GetInfo()
#     img = np.frombuffer(im, dtype='uint8')
#     img.shape = (bmpinfo['bmWidth'], bmpinfo['bmHeight'], 4)
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(hwnd, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())
#     img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
#     return img


# def new_screenshot_getimg(area, size, name):
#     x, y = area[0], area[1]
#     w, h = area[2], area[3]
#     hwnd = win32gui.FindWindow(None, "win32")
#     wDC = win32gui.GetWindowDC(hwnd)
#     dcObj = win32ui.CreateDCFromHandle(wDC)
#     cDC = dcObj.CreateCompatibleDC()
#     dataBitMap = win32ui.CreateBitmap()
#     dataBitMap.CreateCompatibleBitmap(dcObj, w - x, h - y)
#     cDC.SelectObject(dataBitMap)
#     cDC.BitBlt((-x, -y), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
#     im = dataBitMap.GetBitmapBits(True)  # Tried False also
#     bmpinfo = dataBitMap.GetInfo()
#     img = Image.frombuffer(
#         'RGB',
#         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#         im, 'raw', 'RGBX', 0, 1)
#     img = np.array(img)
#     cut_pic(img, size, name)
#     dcObj.DeleteDC()
#     cDC.DeleteDC()
#     win32gui.ReleaseDC(hwnd, wDC)
#     win32gui.DeleteObject(dataBitMap.GetHandle())


SZ = 20
bin_n = 16  # Number of bins


def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n * ang / (2 * np.pi))  # quantizing binvalues in (0...16)
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)  # hist is a 64 bit vector
    return hist


# 二值化，切割
def cut(img):
    try:
        # ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        ret, thresh1 = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY_INV)
        # thresh1=fushi(thresh1)
        # image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        image, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        imgn = []
        xy = []
        for i in range(len(contours)):
            cnt = contours[i]
            x, y, w, h = cv2.boundingRect(cnt)
            xy.append([x, y, w, h])

        xy = sorted(xy)

        xy0 = []  ##存放切块
        ##前n-1个块
        for i in range(len(xy) - 1):
            diff = xy[i + 1][0] - xy[i][0]
            if diff < 4:
                t0 = min(xy[i][0], xy[i + 1][0])
                t1 = min(xy[i][1], xy[i + 1][1])
                t2 = max(xy[i][2] + xy[i][0], xy[i + 1][2] + xy[i + 1][0]) - t0
                t3 = max(xy[i][3] + xy[i][1], xy[i + 1][3] + xy[i + 1][1]) - t1
                xy[i + 1] = [t0, t1, t2, t3]
            elif 4 <= diff < 12:
                xy0.append(xy[i])
            else:
                if 12 <= diff <= 16:
                    temp1 = [xy[i][0], xy[i][1], xy[i][2] - int(diff / 2), xy[i][3]]
                    temp2 = [int(diff / 2) + xy[i][0], xy[i + 1][1], xy[i + 1][2], xy[i + 1][3]]
                    xy0.append(temp1)
                    xy0.append(temp2)
                elif 17 <= diff <= 23:
                    t1 = int(diff / 3)
                    t2 = int(diff / 3) * 2
                    temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                    temp2 = [xy[i][0] + t1, xy[i][1], t2 - t1, xy[i][3]]
                    temp3 = [xy[i][0] + t2, xy[i][1], diff - t2, xy[i][3]]
                    xy0.append(temp1)
                    xy0.append(temp2)
                    xy0.append(temp3)
                elif 24 <= diff <= 30:
                    t1 = int(diff / 4)
                    t2 = int(diff / 4) * 2
                    t3 = int(diff / 4) * 3
                    temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                    temp2 = [xy[i][0] + t1, xy[i][1], t2 - t1, xy[i][3]]
                    temp3 = [xy[i][0] + t2, xy[i][1], t3 - t2, xy[i][3]]
                    temp4 = [xy[i][0] + t3, xy[i][1], diff - t3, xy[i][3]]
                    xy0.append(temp1)
                    xy0.append(temp2)
                    xy0.append(temp3)
                    xy0.append(temp4)
                elif 31 <= diff:
                    t1 = int(diff / 5)
                    t2 = int(diff / 5) * 2
                    t3 = int(diff / 5) * 3
                    t4 = int(diff / 5) * 4
                    temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                    temp2 = [xy[i][0] + t1, xy[i][1], t2 - t1, xy[i][3]]
                    temp3 = [xy[i][0] + t2, xy[i][1], t3 - t2, xy[i][3]]
                    temp4 = [xy[i][0] + t3, xy[i][1], t4 - t3, xy[i][3]]
                    temp5 = [xy[i][0] + t4, xy[i][1], diff - t4, xy[i][3]]
                    xy0.append(temp1)
                    xy0.append(temp2)
                    xy0.append(temp3)
                    xy0.append(temp4)
                    xy0.append(temp5)

        # 最后一个 图像块
        diff = xy[-1][2]  # 最后一个 图像块
        if diff < 3:
            pass
        elif 3 <= diff < 12:
            xy0.append(xy[-1])
        else:
            if 12 <= diff <= 16:
                temp1 = [xy[-1][0], xy[-1][1], int(diff / 2), xy[-1][3]]
                temp2 = [int(diff / 2) + xy[-1][0], xy[-1][1], xy[-1][2] - int(diff / 2), xy[-1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
            elif 17 <= diff <= 23:
                t1 = int(diff / 3)
                t2 = int(diff / 3) * 2
                temp1 = [xy[-1][0], xy[-1][1], t1, xy[-1][3]]
                temp2 = [xy[-1][0] + t1, xy[-1][1], t2 - t1, xy[-1][3]]
                temp3 = [xy[-1][0] + t2, xy[-1][1], diff - t2, xy[-1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
            elif 24 <= diff <= 30:
                t1 = int(diff / 4)
                t2 = int(diff / 4) * 2
                t3 = int(diff / 4) * 3
                temp1 = [xy[-1][0], xy[-1][1], t1, xy[-1][3]]
                temp2 = [xy[-1][0] + t1, xy[-1][1], t2 - t1, xy[-1][3]]
                temp3 = [xy[-1][0] + t2, xy[-1][1], t3 - t2, xy[-1][3]]
                temp4 = [xy[-1][0] + t3, xy[-1][1], diff - t3, xy[-1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
            elif 31 <= diff:
                t1 = int(diff / 5)
                t2 = int(diff / 5) * 2
                t3 = int(diff / 5) * 3
                t4 = int(diff / 5) * 4
                temp1 = [xy[-1][0], xy[-1][1], t1, xy[-1][3]]
                temp2 = [xy[-1][0] + t1, xy[-1][1], t2 - t1, xy[-1][3]]
                temp3 = [xy[-1][0] + t2, xy[-1][1], t3 - t2, xy[-1][3]]
                temp4 = [xy[-1][0] + t3, xy[-1][1], t4 - t3, xy[-1][3]]
                temp5 = [xy[-1][0] + t4, xy[-1][1], diff - t4, xy[-1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
                xy0.append(temp5)

        for i in range(len(xy0)):
            x, y, w, h = xy0[i]
            imgn.append(image[y:y + h, x:x + w])
        for i in range(len(imgn)):
            imgn[i] = cv2.resize(imgn[i], (8, 8))

        return imgn
    except:
        logger.exception("error message")
        return []

def readpic(img, maindata):
    svm = cv2.ml.SVM_load(maindata)
    testData = cut(img)
    testData = list(map(hog, testData))
    testData = np.float32(testData).reshape(-1, 64)
    result = svm.predict(testData)
    result = result[1].reshape(-1).astype(int).astype(str)
    for i in range(len(result)):
        if result[i] == '11':
            result[i] = ':'
    price = "".join(list(result))
    return price  # 返回的是price str   也可以是时间


def timeset( imgpos_currenttime, maindata):
    try:
        currenttime = cv2.cvtColor(imgpos_currenttime, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite('time.png', currenttime)
        currenttime = readpic(currenttime, maindata)  # 识别出来的时间
        print(currenttime)
        a_time = V_global.a_time
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        b = a + ' ' + currenttime
        a_time_temp = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')) + 0.6  # 转时间戳   补个平均时差
        if a_time_temp - 0.9 <= a_time <= a_time_temp + 0.9:
            pass
        else:
            V_global.a_time = a_time_temp
    except:
        logger.exception('this is an exception message')





def grab_screen(region=None, title=None):
    hwin = win32gui.GetDesktopWindow()
    if region:
        left, top, x2, y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    elif title:
        gtawin = win32gui.FindWindow(None, title)
        if not gtawin:
            raise Exception('window title not found')
        # get the bounding box of the window
        left, top, x2, y2 = win32gui.GetWindowRect(gtawin)
        width = x2 - left + 1
        height = y2 - top + 1
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
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    return img


def findpos():
    sc = grab_screen()
    img = np.asarray(sc)
    dick_target = V_global.dick_target
    template = dick_target[2]
    time_template = dick_target[3]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    px_relative = V_global.px_relative
    py_relative = V_global.py_relative
    px_timerelative = V_global.px_timerelative
    py_timerelative = V_global.py_timerelative
    Position_frame = V_global.Position_frame
    P_relative2 = V_global.P_relative2

    res2 = cv2.matchTemplate(img, time_template, cv2.TM_CCOEFF_NORMED)
    time_min_val, time_max_val, time_min_loc, time_max_loc = cv2.minMaxLoc(res2)

    print('findpos_on', max_val)

    if max_val > 0.75:  # 找不到不动作
        ##计算位置
        V_global.px_lowestprice = max_loc[0]+px_relative
        V_global.py_lowestprice = max_loc[1]+py_relative
        Px = V_global.Px
        Py = V_global.Py
        V_global.px_calculate_relative = max_loc[0]+px_relative-Px ##计算得到相差
        V_global.py_calculate_relative = max_loc[1]+py_relative-Py
        ##计算时间位置
        print('time_max_val', time_max_val)
        V_global.Px_currenttime = time_max_loc[0]+px_timerelative ##时间的位置
        V_global.Py_currenttime = time_max_loc[1]+py_timerelative



        px_lowestprice = V_global.px_lowestprice
        py_lowestprice = V_global.py_lowestprice
        V_global.Px_lowestprice = px_lowestprice
        V_global.Py_lowestprice = py_lowestprice
        Px_lowestprice = V_global.Px_lowestprice
        Py_lowestprice = V_global.Py_lowestprice

        print("找到的Px_lowestprice", Px_lowestprice)
        print("找到的Py_lowestprice", Py_lowestprice)


        for i in range(len(Position_frame)):
            Position_frame[i][0] = Px_lowestprice + P_relative2[i][0]
            Position_frame[i][1] = Py_lowestprice + P_relative2[i][1]
        V_global.Position_frame = Position_frame
        ##几个截图位置, 通过服务器传来的相对位置 进行计算
        refresh_area_relative = V_global.refresh_area_relative
        confirm_area_relative = V_global.confirm_area_relative
        yan_confirm_area_relative = V_global.yan_confirm_area_relative
        Pos_controlframe_relative = V_global.Pos_controlframe_relative
        Pos_yanzhengma_relative = V_global.Pos_yanzhengma_relative ## 验证码所在位置
        Pos_yanzhengmaframe_relative = V_global.Pos_yanzhengmaframe_relative ## 验证码框放置位置
        V_global.refresh_area = [refresh_area_relative[0]+Px_lowestprice,refresh_area_relative[1]+Py_lowestprice,
                                 refresh_area_relative[2] + Px_lowestprice, refresh_area_relative[3] + Py_lowestprice]
        V_global.confirm_area = [confirm_area_relative[0]+Px_lowestprice,confirm_area_relative[1]+Py_lowestprice,
                                 confirm_area_relative[2] + Px_lowestprice, confirm_area_relative[3] + Py_lowestprice]
        V_global.yan_confirm_area = [yan_confirm_area_relative[0]+Px_lowestprice,
                                     yan_confirm_area_relative[1] + Py_lowestprice,
                                     yan_confirm_area_relative[2] + Px_lowestprice,
                                     yan_confirm_area_relative[3] + Py_lowestprice]
        V_global.Pos_controlframe = [Pos_controlframe_relative[0]+Px_lowestprice,
                                     Pos_controlframe_relative[1] + Py_lowestprice]
        V_global.Pos_yanzhengma = [Position_frame[6][0]+Pos_yanzhengma_relative[0],
                                   Position_frame[6][1] + Pos_yanzhengma_relative[1],
                                   Position_frame[6][0] + Pos_yanzhengma_relative[2],
                                   Position_frame[6][1] + Pos_yanzhengma_relative[3]]  # 验证码所在位置
        V_global.Pos_yanzhengmaframe = [Px_lowestprice+Pos_yanzhengmaframe_relative[0],
                                        Py_lowestprice + Pos_yanzhengmaframe_relative[1]]  # 验证码框放置位置
        V_global.Pos_timeframe = [245-344+Px_lowestprice,399-183+Py_lowestprice]

        lowestprice_sizex = V_global.lowestprice_sizex
        lowestprice_sizey = V_global.lowestprice_sizey
        currenttime_sizex = V_global.currenttime_sizex
        currenttime_sizey = V_global.currenttime_sizey
        V_global.lowest = [Px_lowestprice,Py_lowestprice,lowestprice_sizex+Px_lowestprice,
                           lowestprice_sizey + Py_lowestprice]
        Px_currenttime = V_global.Px_currenttime
        Py_currenttime = V_global.Py_currenttime
        V_global.currenttime = [Px_currenttime,Py_currenttime,Px_currenttime+currenttime_sizex,
                                Py_currenttime + currenttime_sizey]
        dis_x = 50
        dis_y = 100
        x1 = Px_lowestprice - dis_x  # 截图起始点
        y1 = Py_lowestprice - dis_y
        lowest = V_global.lowest
        refresh_area = V_global.refresh_area
        confirm_area = V_global.confirm_area
        Pos_yanzhengma = V_global.Pos_yanzhengma
        yan_confirm_area = V_global.yan_confirm_area
        currenttime = V_global.currenttime

        cal_area = [lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area, currenttime]  # 构建截图区域
        use_area = []
        V_global.sc_area = [Px_lowestprice-dis_x,Py_lowestprice-dis_y,Px_lowestprice+600,Py_lowestprice+120]
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            use_area.append(temp)
        V_global.use_area = use_area



def new_screenshot(area):
    hwin = win32gui.GetDesktopWindow()
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
    bmp.SaveBitmapFile(memdc, 'screenshot.bmp')



def only_screenshot(area):  # x,y  pos      w,h size
    a = time.time()
    x, y = int(area[0]), int(area[1])
    w, h = int(area[2]), int(area[3])
    hwnd = win32gui.FindWindow(None, "win32")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w - x, h - y)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((-x, -y), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    bmpinfo = dataBitMap.GetInfo()
    img = np.frombuffer(im, dtype='uint8')
    img.shape = (bmpinfo['bmHeight'], bmpinfo['bmWidth'], 4)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    b = time.time()
    return img

# @calculate_usetime
def cut_img():  # 将所得的img 处理成  lowestprice_img   confirm_img  yanzhengma_confirm_img  refresh_img
    use_area = V_global.use_area
    sc_area = V_global.sc_area
    img = only_screenshot(sc_area)  # 获取得到的截图
    img = np.asarray(img)  # 转化为numpy数组
    try:
        V_global.imgpos_lowestprice = img[use_area[0][1]:use_area[0][3],use_area[0][0]:use_area[0][2]] ## ok
        V_global.imgpos_refresh = img[use_area[1][1]:use_area[1][3],use_area[1][0]:use_area[1][2]] ## ok
        V_global.imgpos_confirm = img[use_area[2][1]:use_area[2][3],use_area[2][0]:use_area[2][2]]
        V_global.imgpos_yanzhengma = img[use_area[3][1]:use_area[3][3],use_area[3][0]:use_area[3][2]] ## ok
        V_global.imgpos_yanzhengmaconfirm = img[use_area[4][1]:use_area[4][3],use_area[4][0]:use_area[4][2]] ## ok
        V_global.imgpos_currenttime = img[use_area[5][1]:use_area[5][3],use_area[5][0]:use_area[5][2]]
    except:
        logger.error("cut_img 这里出错")
        logger.exception('this is an exception message')


def findrefresh():
    dick_target = V_global.dick_target
    template = dick_target[0]
    imgpos_refresh = V_global.imgpos_refresh
    sc = imgpos_refresh
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # print(max_val)

    if max_val >= 0.8:
        print("refresh")
        OnClick_Shuaxin()  # 刷新验证码
        V_global.yanzhengma_view = True ## 激活放大器
        V_global.yanzhengma_find = False ## 表示需要确认是否找到验证码
    else:
        V_global.yanzhengma_find = True


def findconfirm():
    dick_target = V_global.dick_target
    smartprice_chujia = V_global.smartprice_chujia
    template = dick_target[1]
    imgpos_confirm = V_global.imgpos_confirm
    sc = imgpos_confirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.9:
        print(max_val, 'max_val')
        if not smartprice_chujia:
            OnClick_confirm()
        else:
            print("max_val", max_val)
            Smart_chujia()


def find_yan_confirm():
    try:
        dick_target = V_global.dick_target
        template = dick_target[1]
        imgpos_yanzhengmaconfirm = V_global.imgpos_yanzhengmaconfirm
        sc = imgpos_yanzhengmaconfirm
        img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        yanzhengma_control = V_global.yanzhengma_control
        if max_val > 0.9 and yanzhengma_control:
            V_global.yanzhengma_view = True
        elif max_val <= 0.9:
            V_global.yanzhengma_view = False
            V_global.yanzhengma_close = True
            V_global.yanzhengma_control = True
    except:
        logger.exception("error message")

# @calculate_usetime
def Price_read():
    imgpos_lowestprice = V_global.imgpos_lowestprice

    # avt = get_val('avt')
    # avt += 1
    # if avt == 500 or avt == 501:
    #     avt = 0
    # set_val('avt', avt)
    # cv2.imwrite(r'./pic/%s.png' % avt, imgpos_lowestprice)

    lowest_price_img = cv2.cvtColor(imgpos_lowestprice, cv2.COLOR_BGR2GRAY)
    price = readpic(lowest_price_img, 'maindata.xml')
    return price
