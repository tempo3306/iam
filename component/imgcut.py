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
from component.variable import set_val, get_val
import logging
from component.read_pic import readpic, grab_screen

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




def timeset( imgpos_currenttime):
    try:
        currenttime = cv2.cvtColor(imgpos_currenttime, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite('time.png', currenttime)
        currenttime = readpic(currenttime)  # 识别出来的时间
        print(currenttime)
        a_time = get_val('a_time')
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        b = a + ' ' + currenttime
        a_time_temp = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')) + 0.6  # 转时间戳   补个平均时差
        if a_time_temp - 0.9 <= a_time <= a_time_temp + 0.9:
            pass
        else:
            set_val('a_time', a_time_temp)
    except:
        logger.exception('this is an exception message')








def findpos():
    sc = grab_screen()
    img = np.asarray(sc)
    dick_target = get_val('dick_target')
    template = dick_target[2]
    time_template = dick_target[3]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    px_relative = get_val('px_relative')
    py_relative = get_val('py_relative')
    px_timerelative = get_val('px_timerelative')
    py_timerelative = get_val('py_timerelative')
    Position_frame = get_val('Position_frame')
    P_relative2 = get_val('P_relative2')

    res2 = cv2.matchTemplate(img, time_template, cv2.TM_CCOEFF_NORMED)
    time_min_val, time_max_val, time_min_loc, time_max_loc = cv2.minMaxLoc(res2)

    print('findpos_on', max_val)

    if max_val > 0.75:  # 找不到不动作
        ##计算位置
        set_val('px_lowestprice', max_loc[0] + px_relative)
        set_val('py_lowestprice', max_loc[1] + py_relative)
        Px = get_val('Px')
        Py = get_val('Py')
        set_val('px_calculate_relative', max_loc[0] + px_relative - Px) ##计算得到相差
        set_val('py_calculate_relative', max_loc[1] + py_relative - Py)
        ##计算时间位置
        print('time_max_val', time_max_val)
        set_val('Px_currenttime', time_max_loc[0] + px_timerelative)    #时间的位置
        set_val('Py_currenttime', time_max_loc[1] + py_timerelative)



        px_lowestprice = get_val('px_lowestprice')
        py_lowestprice = get_val('py_lowestprice')
        set_val('Px_lowestprice', px_lowestprice)
        set_val('Py_lowestprice', py_lowestprice)
        Px_lowestprice = get_val('Px_lowestprice')
        Py_lowestprice = get_val('Py_lowestprice')

        print("找到的Px_lowestprice", Px_lowestprice)
        print("找到的Py_lowestprice", Py_lowestprice)


        for i in range(len(Position_frame)):
            Position_frame[i][0] = Px_lowestprice + P_relative2[i][0]
            Position_frame[i][1] = Py_lowestprice + P_relative2[i][1]
        set_val('Position_frame', Position_frame)
        ##几个截图位置, 通过服务器传来的相对位置 进行计算
        refresh_area_relative = get_val('refresh_area_relative')
        confirm_area_relative = get_val('confirm_area_relative')
        yan_confirm_area_relative = get_val('yan_confirm_area_relative')
        Pos_controlframe_relative = get_val('Pos_controlframe_relative')
        Pos_yanzhengma_relative = get_val('Pos_yanzhengma_relative')  # 验证码所在位置
        Pos_yanzhengmaframe_relative = get_val('Pos_yanzhengmaframe_relative')  # 验证码框放置位置
        set_val('refresh_area', [refresh_area_relative[0] + Px_lowestprice, refresh_area_relative[1] + Py_lowestprice,
                                 refresh_area_relative[2] + Px_lowestprice, refresh_area_relative[3] + Py_lowestprice])
        set_val('confirm_area', [confirm_area_relative[0] + Px_lowestprice, confirm_area_relative[1] + Py_lowestprice,
                                 confirm_area_relative[2] + Px_lowestprice, confirm_area_relative[3] + Py_lowestprice])
        set_val('yan_confirm_area', [yan_confirm_area_relative[0] + Px_lowestprice,
                                     yan_confirm_area_relative[1] + Py_lowestprice,
                                     yan_confirm_area_relative[2] + Px_lowestprice,
                                     yan_confirm_area_relative[3] + Py_lowestprice])
        set_val('Pos_controlframe', [Pos_controlframe_relative[0] + Px_lowestprice,
                                     Pos_controlframe_relative[1] + Py_lowestprice])
        set_val('Pos_yanzhengma', [Position_frame[6][0] + Pos_yanzhengma_relative[0],
                                   Position_frame[6][1] + Pos_yanzhengma_relative[1],
                                   Position_frame[6][0] + Pos_yanzhengma_relative[2],
                                   Position_frame[6][1] + Pos_yanzhengma_relative[3]])  # 验证码所在位置
        set_val('Pos_yanzhengmaframe', [Px_lowestprice + Pos_yanzhengmaframe_relative[0],
                                        Py_lowestprice + Pos_yanzhengmaframe_relative[1]])  # 验证码框放置位置
        set_val('Pos_timeframe', [245 - 344 + Px_lowestprice, 399 - 183 + Py_lowestprice])

        lowestprice_sizex = get_val('lowestprice_sizex')
        lowestprice_sizey = get_val('lowestprice_sizey')
        currenttime_sizex = get_val('currenttime_sizex')
        currenttime_sizey = get_val('currenttime_sizey')
        set_val('lowest', [Px_lowestprice, Py_lowestprice, lowestprice_sizex + Px_lowestprice,
                           lowestprice_sizey + Py_lowestprice])
        Px_currenttime = get_val("Px_currenttime")
        Py_currenttime = get_val("Py_currenttime")
        set_val('currenttime', [Px_currenttime, Py_currenttime, Px_currenttime + currenttime_sizex,
                                Py_currenttime + currenttime_sizey])
        dis_x = 50
        dis_y = 100
        x1 = Px_lowestprice - dis_x  # 截图起始点
        y1 = Py_lowestprice - dis_y
        lowest = get_val('lowest')
        refresh_area = get_val('refresh_area')
        confirm_area = get_val('confirm_area')
        Pos_yanzhengma = get_val('Pos_yanzhengma')
        yan_confirm_area = get_val('yan_confirm_area')
        currenttime = get_val('currenttime')

        cal_area = [lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area, currenttime]  # 构建截图区域
        use_area = []
        set_val('sc_area', [Px_lowestprice - dis_x, Py_lowestprice - dis_y, Px_lowestprice + 600, Py_lowestprice + 120])
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            use_area.append(temp)
        set_val('use_area', use_area)



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
    use_area = get_val('use_area')
    sc_area = get_val('sc_area')
    img = only_screenshot(sc_area)  # 获取得到的截图
    img = np.asarray(img)  # 转化为numpy数组
    try:
        set_val('imgpos_lowestprice', img[use_area[0][1]:use_area[0][3], use_area[0][0]:use_area[0][2]])  # ok
        set_val('imgpos_refresh', img[use_area[1][1]:use_area[1][3], use_area[1][0]:use_area[1][2]])  # ok
        set_val('imgpos_confirm', img[use_area[2][1]:use_area[2][3], use_area[2][0]:use_area[2][2]])
        set_val('imgpos_yanzhengma', img[use_area[3][1]:use_area[3][3], use_area[3][0]:use_area[3][2]])  # ok
        set_val('imgpos_yanzhengmaconfirm', img[use_area[4][1]:use_area[4][3], use_area[4][0]:use_area[4][2]])  # ok
        set_val('imgpos_currenttime', img[use_area[5][1]:use_area[5][3], use_area[5][0]:use_area[5][2]])
    except:
        logger.error("cut_img 这里出错")
        logger.exception('this is an exception message')


def findrefresh():
    dick_target = get_val('dick_target')
    template = dick_target[0]
    imgpos_refresh = get_val('imgpos_refresh')
    sc = imgpos_refresh
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # print(max_val)

    if max_val >= 0.8:
        print("refresh")
        OnClick_Shuaxin()  # 刷新验证码
        set_val('yanzhengma_view', True)  # 激活放大器
        set_val('yanzhengma_find', False)  # 表示需要确认是否找到验证码
    else:
        set_val('yanzhengma_find', True)


def findconfirm():
    dick_target = get_val('dick_target')
    smartprice_chujia = get_val('smartprice_chujia')
    template = dick_target[1]
    imgpos_confirm = get_val('imgpos_confirm')
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
        dick_target = get_val('dick_target')
        template = dick_target[1]
        imgpos_yanzhengmaconfirm = get_val('imgpos_yanzhengmaconfirm')
        sc = imgpos_yanzhengmaconfirm
        img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)  # 转灰度图
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        yanzhengma_control = get_val('yanzhengma_control')
        if max_val > 0.9 and yanzhengma_control:
            set_val('yanzhengma_view', True)
        elif max_val <= 0.9:
            set_val('yanzhengma_view', False)
            set_val('yanzhengma_close', True)
            set_val('yanzhengma_control', True)
    except:
        logger.exception("error message")

# @calculate_usetime
def Price_read():
    imgpos_lowestprice = get_val('imgpos_lowestprice')

    # avt = get_val('avt')
    # avt += 1
    # if avt == 500 or avt == 501:
    #     avt = 0
    # set_val('avt', avt)
    # cv2.imwrite(r'./pic/%s.png' % avt, imgpos_lowestprice)

    lowest_price_img = cv2.cvtColor(imgpos_lowestprice, cv2.COLOR_BGR2GRAY)
    price = readpic(lowest_price_img)
    return price
