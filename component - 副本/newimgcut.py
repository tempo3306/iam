'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 10:07
'''
from PIL import Image,ImageGrab
import cv2
import win32gui
import win32ui
import win32con
import numpy as np
import time
from .staticmethod import OnClick_Shuaxin,OnClick_confirm
from .variable import set_val,get_val
def cut_pic(img, size, name):
    img = np.asarray(img)
    i1 = img[0:24, :150]
    i2 = img[48:110, 30:]
    im = np.concatenate([i2, i1])
    im = cv2.resize(im, tuple(size))
    cv2.imwrite(name, im)
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
def new_screenshot_getimg(area, size, name):
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
    im = dataBitMap.GetBitmapBits(True)  # Tried False also
    bmpinfo = dataBitMap.GetInfo()
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        im, 'raw', 'RGBX', 0, 1)
    img = np.array(img)
    cut_pic(img, size, name)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
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
def cut(img):
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    image, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    imgn = []
    xy = []
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        xy.append([x, y, w, h])
    xy = sorted(xy)
    xy0 = []
    for i in range(len(xy) - 1):
        diff = xy[i + 1][0] - xy[i][0]
        if diff < 6:
            t0 = min(xy[i][0], xy[i + 1][0])
            t1 = min(xy[i][1], xy[i + 1][1])
            t2 = max(xy[i][2] + xy[i][0], xy[i + 1][2] + xy[i + 1][0]) - t0
            t3 = max(xy[i][3] + xy[i][1], xy[i + 1][3] + xy[i + 1][1]) - t1
            xy[i + 1] = [t0, t1, t2, t3]
        elif 6 <= diff < 12:
            xy0.append(xy[i])
        else:
            if 12 <= diff <= 16:
                temp1 = [xy[i][0], xy[i][1], xy[i][2] - int(diff / 2), xy[i][3]]
                temp2 = [int(diff / 2) + xy[i][0], xy[i + 1][1], xy[i + 1][2], xy[i + 1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
            elif 19 <= diff <= 23:
                t1 = int(diff / 3)
                t2 = int(diff / 3) * 2
                temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                temp2 = [xy[i][0] + t1, xy[i][1], t2, xy[i][3]]
                temp3 = [xy[i][0] + t2, xy[i][1], diff - t2, xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
            elif 26 <= diff <= 30:
                t1 = int(diff / 4)
                t2 = int(diff / 4) * 2
                t3 = int(diff / 4) * 3
                temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                temp2 = [xy[i][0] + t1, xy[i][1], t2, xy[i][3]]
                temp3 = [xy[i][0] + t2, xy[i][1], t3, xy[i][3]]
                temp4 = [xy[i][0] + t3, xy[i][1], diff - t3, xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
            elif 33 <= diff:
                t1 = int(diff / 5)
                t2 = int(diff / 5) * 2
                t3 = int(diff / 5) * 3
                t4 = int(diff / 5) * 4
                temp1 = [xy[i][0], xy[i][1], t1, xy[i][3]]
                temp2 = [xy[i][0] + t1, xy[i][1], t2, xy[i][3]]
                temp3 = [xy[i][0] + t2, xy[i][1], t3, xy[i][3]]
                temp4 = [xy[i][0] + t3, xy[i][1], t4, xy[i][3]]
                temp5 = [xy[i][0] + t4, xy[i][1], diff - t4, xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
                xy0.append(temp5)
    xy0.append(xy[-1])
    for i in range(len(xy0)):
        x, y, w, h = xy0[i]
        imgn.append(image[y:y + h, x:x + w])
    for i in range(len(imgn)):
        imgn[i] = cv2.resize(imgn[i], (8, 8))
    return imgn
def readpic(img,maindata):
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
def timeset(guopai_on,moni_on,imgpos_currenttime,moni_second,a_time,maindata):
    try:
        currenttime = cv2.cvtColor(imgpos_currenttime, cv2.COLOR_BGR2GRAY)
        currenttime = readpic(currenttime, maindata)  # 识别出来的时间
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        b = a + ' ' + currenttime
        if guopai_on:
            print(time.strptime(b, '%Y-%m-%d %H:%M:%S'))
            a_time = time.mktime(time.strptime(b,'%Y-%m-%d %H:%M:%S')) + 0.5  # 转时间戳   补个平均时差
            moni_second = moni_second
        if moni_on:
            try:
                moni_second = int(currenttime.split(':')[2]) + 0.5
                a_time = a_time
            except:
                pass
    except:
        pass
    return (moni_second, a_time)
def findpos():
    sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    global dick_target
    template = dick_target[2]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    global px_lowestprice, py_lowestprice, px_relative, py_relative, Px_lowestprice, Py_lowestprice, Px, Py
    global refresh_area, confirm_area, Pos_timeframe, Pos_controlframe, Pos_yanzhengma, Pos_yanzhengmaframe, yan_confirm_area
    global use_area, sc_area  # 用于截取图片
    global Position, refresh_area, confirm_area, Pos_timeframe, Pos_controlframe, Pos_yanzhengma, Pos_yanzhengmaframe, yan_confirm_area
    global Px_currenttime,Py_currenttime  #当前时间所在位置
    global ghostbutton_pos
    global P_relative2
    if max_val > 0.9:  # 找不到不动作
        set_val('px_lowestprice',max_loc[0]+px_relative)
        set_val('py_lowestprice',max_loc[1]+py_relative)
        set_val('Px_lowestprice',px_lowestprice)
        set_val('Py_lowestprice',py_lowestprice)
        set_val('Px_currenttime',Px_lowestprice-27)  #参考最低成交价位置
        set_val('Py_currenttime',Py_lowestprice-14)
        set_val('ghostbutton_pos',[px_lowestprice-9,py_lowestprice+84])
        for i in range(len(Position)):
            Position[i][0] = Px_lowestprice + P_relative2[i][0]
            Position[i][1] = Py_lowestprice + P_relative2[i][1]
        set_val('refresh_area',[396-150+Px_lowestprice,11-100+Py_lowestprice,396+150+Px_lowestprice,11+100+Py_lowestprice])
        set_val('confirm_area',[505-80+Px_lowestprice,68-50+Py_lowestprice,505+80+Px_lowestprice,68+50+Py_lowestprice])
        set_val('yan_confirm_area',[205-80+Px_lowestprice,68-50+Py_lowestprice,405+80+Px_lowestprice,68+50+Py_lowestprice])
        set_val('Pos_controlframe',[192-344+Px_lowestprice,514-183+Py_lowestprice])
        set_val('Pos_yanzhengma',[Position[5][0]-277,Position[5][1]-65,Position[5][0]-97,Position[5][1]+45])  #验证码所在位置
        set_val('Pos_yanzhengmaframe',[Px_lowestprice+297,Py_lowestprice-283])  #验证码框放置位置
        Pos_timeframe=[245 - 344+Px_lowestprice, 399- 183+Py_lowestprice]
        global findpos_on, yanzhengma_move ,lowestprice_sizex,lowestprice_sizey
        global currenttime_sizex,currenttime_sizey
        set_val('findpos_on',False)  #无需定位
        set_val('yanzhengma_move',True)  #需要定位
        lowest = [Px_lowestprice, Py_lowestprice,  lowestprice_sizex+Px_lowestprice, lowestprice_sizey+Py_lowestprice]
        currenttime = [Px_currenttime,Py_currenttime,Px_currenttime+currenttime_sizex,Py_currenttime+currenttime_sizey]
        dis_x=50
        dis_y=100
        x1 = Px_lowestprice - dis_x  # 截图起始点
        y1 = Py_lowestprice - dis_y
        cal_area = [lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area , currenttime]   #构建截图区域
        set_val('use_area',[])
        set_val('sc_area',[Px_lowestprice-dis_x,Py_lowestprice-dis_y,Px_lowestprice+600,Py_lowestprice+120])
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            use_area.append(temp)
def only_screenshot(area):  # x,y  pos      w,h size
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
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        im, 'raw', 'RGBX', 0, 1)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return img
def cut_img():  # 将所得的img 处理成  lowestprice_img   confirm_img  yanzhengma_confirm_img  refresh_img
    global use_area, sc_area, imgpos_lowestprice, imgpos_yanzhengma, imgpos_refresh, imgpos_confirm, imgpos_yanzhengmaconfirm,imgpos_currenttime
    img = only_screenshot(sc_area)  # 获取得到的截图
    img = np.asarray(img)  # 转化为numpy数组
    set_val('imgpos_lowestprice',img[use_area[0][1]:use_area[0][3],use_area[0][0]:use_area[0][2]])  #ok
    set_val('imgpos_refresh',img[use_area[1][1]:use_area[1][3],use_area[1][0]:use_area[1][2]])  #ok
    set_val('imgpos_confirm',img[use_area[2][1]:use_area[2][3],use_area[2][0]:use_area[2][2]])
    set_val('imgpos_yanzhengma',img[use_area[3][1]:use_area[3][3],use_area[3][0]:use_area[3][2]])  #ok
    set_val('imgpos_yanzhengmaconfirm',img[use_area[4][1]:use_area[4][3],use_area[4][0]:use_area[4][2]])  #ok
    set_val('imgpos_currenttime',img[use_area[5][1]:use_area[5][3],use_area[5][0]:use_area[5][2]])
def findrefresh():
    global dick_target, refresh_on, refresh_need, refresh_one, Position, refresh_area, confirm_area
    template = dick_target[0]
    global imgpos_refresh
    sc = imgpos_refresh
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.8:
        OnClick_Shuaxin()
        global yanzhengma_view, yanzhengma_close, yanzhengma_count
        set_val('yanzhengma_view',True)  #激活放大器
        set_val('yanzhengma_count',0)  #归零
def findconfirm():
    global dick_target, confirm_on, Position
    template = dick_target[1]
    global imgpos_confirm
    sc = imgpos_confirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.9:
        OnClick_confirm()
    if confirm_on and max_val < 0.9:
        print("暂停确认")
def find_yan_confirm():
    global dick_target, confirm_on, Position, yanzhengma_view, yanzhengma_close
    template = dick_target[1]
    global imgpos_yanzhengmaconfirm
    sc = imgpos_yanzhengmaconfirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.9:
        set_val('yanzhengma_view',False)
        set_val('yanzhengma_close',True)
def Price_read():
    global imgpos_lowestprice, findpos_on, lowest_price
    set_val('lowest_price',cv2.cvtColor(imgpos_lowestprice,cv2.COLOR_BGR2GRAY))
    price = readpic(lowest_price, 'maindata.xml')
    return price