'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 9:33
'''
import win32gui

import cv2
import win32con
import win32api
import win32clipboard
import time
import threading

from component.read_pic import grab_screen
from component.variable import set_val, get_val, get_dick, set_dick
import ctypes
from ctypes import wintypes
from wx.lib.pubsub import pub
import time
import logging

logger = logging.getLogger()


def calculate_usetime(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('current Function [%s] run time is %.5f' % (func.__name__, time.time() - local_time))

    return wrapper




def Click(x, y):  # 鼠标点击
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    # print(x, y)


def Click2(x, y):  # 鼠标点击
    a = win32gui.GetCursorPos()
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos(a)  # 模拟键盘输入



def Paste():  # ctrl + V
    win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


import wx


def Paste_moni(price):
    id = get_val('moni_webframe')
    moni = wx.FindWindowById(id)
    browser = moni.htmlpanel.webview
    script = "$('#selfwrite').val('{0}')".format(price)
    browser.RunScript(script)


def setText(aString):
    aString = aString.encode('utf-8')
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()


def Delete():
    win32api.keybd_event(0x08, 0, 0, 0)
    win32api.keybd_event(0x08, 0, win32con.KEYEVENTF_KEYUP, 0)


def many_delete():
    for i in range(10):
        Delete()


'''
tijiao_num  
1代表初始状态 等待第二次出价  
2代表第二次出价结束 等待第三次出价
3代表等待自动补枪
0代表所有触发都结束
'''


def OnClick_Tijiao(delay=0):
    one_delay = get_val('one_delay')
    second_delay = get_val('second_delay')
    tijiao_num = get_val('tijiao_num')
    twice = get_val('twice')
    smart_autoprice = get_val('smart_autoprice')
    set_val('confirm_need', True)
    print("tijiao_num", tijiao_num)
    print("smart_autoprice", smart_autoprice)
    print("twice", twice)
    if tijiao_num == 1:
        if twice:
            set_val('tijiao_num', 2)
        elif smart_autoprice:
            set_val('tijiao_num', 3)
        else:
            set_val('tijiao_num', 0)
        timer = threading.Timer(delay, Tijiao)
        timer.start()
        set_val('tijiao_on', False)
    elif tijiao_num == 2:
        set_val('tijiao_num', 0)
        timer = threading.Timer(delay, Tijiao)
        timer.start()
        set_val('tijiao_on', False)
    elif tijiao_num == 3:
        set_val('tijiao_num', 0)
        Tijiao()
    else:
        Tijiao()


def Tijiao():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[2][0], Position_frame[2][1])
    set_val('tijiao_OK', False)  # 需要按E解锁，自动提交
    set_val('chujia_on', True)  # 激活自动
    smart_autoprice = get_val('smart_autoprice')
    tijiao_num = get_val('tijiao_num')
    # print("tijiao_num", tijiao_num)
    # print("smart_autoprice", smart_autoprice)
    if tijiao_num == 2:
        set_val('current_pricestatus_label', '等待第三次出价')
        second_time1 = get_val('second_time1')
        second_diff = get_val('second_diff')
        current_pricestatus = '{0:.1f}秒加{1}'.format(second_time1, second_diff)
        set_val('current_pricestatus', current_pricestatus)
    elif tijiao_num == 0:
        set_val('current_pricestatus_label', '等待拍牌结果')
        set_val('current_pricestatus', '请不要关闭页面')

    elif tijiao_num == 3:
        print("tijiao_fsdfs")
        set_val('smartprice_chujia', True)  ##开启智能出价， 打开确认查找
        set_val('current_pricestatus_label', '智能补枪')
        set_val('current_pricestatus', '智能出价')
        print("开启智能出价")


def SmartTijiao():
    tijiao_on = get_val('tijiao_on')
    tijiao_OK = get_val('tijiao_OK')
    tijiao_num = get_val('tijiao_num')
    confirm_need = get_val('confirm_need')
    own_price1 = get_val('own_price1')
    own_price2 = get_val('own_price2')
    moni_on = get_val('moni_on')
    changetime = get_val('changetime')
    a_time = get_val('a_time')
    lowest_price = get_val('lowest_price')
    twice = get_val('twice')
    set_val('confirm_need', True)

    interval = a_time - changetime
    if tijiao_num == 2:  # 说明是第二枪出价
        if lowest_price <= own_price2 - 600:
            print("触发延迟")
            set_val('tijiao_num', 0)
            timer = threading.Timer(0.5, Tijiao)
            timer.start()
            set_val('tijiao_on', False)
        elif lowest_price == own_price2 - 500 and interval < 0.95:
            set_val('tijiao_num', 0)
            timesleep = (1 - interval) / 3 + 0.25
            timer = threading.Timer(timesleep, Tijiao)
            timer.start()
            set_val('tijiao_on', False)
        else:
            set_val('tijiao_num', 0)
            Tijiao()
            set_val('tijiao_on', False)
    elif tijiao_num == 1:
        if lowest_price <= own_price1 - 600:
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)
            else:
                set_val('tijiao_num', 0)
            timer = threading.Timer(0.5, Tijiao)
            timer.start()
        elif lowest_price == own_price1 - 500 and interval < 0.95:
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)
            else:
                set_val('tijiao_num', 0)
            timesleep = (1 - interval) / 3 + 0.25
            timer = threading.Timer(timesleep, Tijiao)
            timer.start()
        else:
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)
            else:
                set_val('tijiao_num', 0)
            Tijiao()


def OnClick_Shuaxin():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[3][0], Position_frame[3][1])
    Click(Position_frame[6][0], Position_frame[6][1])
    set_val('yanzhengma_view', True)  # 激活放大器
    set_val('yanzhengma_count', 0)  # 归零


def OnClick_confirm():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[4][0], Position_frame[4][1])


def Refresh_web():
    moni_on = get_val('moni_on')
    if moni_on:
        wx.CallAfter(pub.sendMessage, "moni refresh_web")
    else:
        wx.CallAfter(pub.sendMessage, "guopai refresh_web")

def Onekey_login():
    guopai_on = get_val('guopai_on')
    if guopai_on:
        wx.CallAfter(pub.sendMessage, "onekey_login")
    ##截图
    login_yanzhengma = get_val('login_yanzhengma')

    img = grab_screen(region=login_yanzhengma)
    num = get_val('num')
    set_val('num', num+1)
    cv2.imwrite('login_%d.png' %num, img)

##-------------------------------------------------------------------------------------
##智能出价
def Smart_chujia():
    Position_frame = get_val('Position_frame')
    moni_on = get_val('moni_on')
    Click(Position_frame[4][0], Position_frame[4][1])  ##确认
    price = smart_price()  ##智能计算出价
    set_val('userprice', price)  ##保存用户出价
    if moni_on:
        wx.CallAfter(pub.sendMessage, 'moni smartchujia', price=price)
        # wx.CallAfter(self.call, 1, ‘abc’, name=”ccc”, help=”test”)
        # wx.FutureCall(5000, self.call, ‘call after 100ms’, name=”test”)
    else:
        print("国拍智能出价")
        guopai_chujia(price)


def esc_chujia():
    Position_frame = get_val('Position_frame')
    moni_on = get_val('moni_on')
    Click(Position_frame[7][0], Position_frame[7][1])  # 取消
    Click(Position_frame[4][0], Position_frame[4][1])  ##确认
    price = smart_price()  ##智能计算出价
    set_val('userprice', price)  ##保存用户出价
    if moni_on:
        wx.CallAfter(pub.sendMessage, 'moni smartchujia', price=price)
        # wx.CallAfter(self.call, 1, ‘abc’, name=”ccc”, help=”test”)
        # wx.FutureCall(5000, self.call, ‘call after 100ms’, name=”test”)
    else:
        guopai_chujia(price)


##智能出价
time_price = {'35': 1200,
              '36': 1100, '37': 1100, '38': 1100, '39': 1100, '40': 1100, '41': 1100,
              '42': 1100, '43': 1100, '44': 1000, '45': 1000, '46': 900, '47': 800,
              '48': 800, '49': 700, '50': 700, '51': 600, '52': 600, '53': 500, '54': 500,
              '55': 500, '56': 300
              }


def smart_price():
    lowest_price = get_val('lowest_price')
    a_time = get_val('a_time')
    structtime = time.localtime(a_time)
    timestr = time.strftime("%H-%M-%S", structtime)
    hour, minute, second = timestr.split('-')
    if int(hour) == 11 and int(minute) == 29:
        add_price = time_price.get(second, 1300)
        return add_price + lowest_price
    else:
        return 1300 + lowest_price  ##除了榜上有的其余均加1300出价


##-------------------------------------------------------------------------------------


def OnClick_chujia():
    guopai_on = get_val('guopai_on')
    if guopai_on:
        lowest_price = get_val('lowest_price')
        tijiao_num = get_val('tijiao_num')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        twice = get_val('twice')

        if tijiao_num == 1:
            own_price1 = lowest_price + one_diff
            set_val('own_price1', own_price1)
            setText(str(own_price1))
            guopai_chujia(own_price1)
            set_val('current_pricestatus_label', '等待第二次提交')
            one_time2 = get_val('one_time2')
            one_advance = get_val('one_advance')
            strategy_type = get_dick('strategy_type')
            if strategy_type == '2':
                set_val('current_pricestatus', '动态提交中')
            else:
                current_pricestatus = '{0:.1f}秒提前{1}'.format(one_time2, one_advance)
                set_val('current_pricestatus', current_pricestatus)
            ##5.1秒后调用取消出
            timer = threading.Timer(5.1, Cancel_chujia)
            timer.start()
        elif tijiao_num == 2 and twice:
            own_price2 = lowest_price + second_diff
            set_val('own_price2', own_price2)
            guopai_chujia(own_price2)
            set_val('current_pricestatus_label', '等待第三次提交')
            second_time2 = get_val('second_time2')
            second_advance = get_val('second_advance')
            strategy_type = get_dick('strategy_type')

            ##提交关闭
            set_val('tijiao_OK', False)
    else:
        wx.CallAfter(pub.sendMessage, 'moni chujia')  # 调用方法
    set_val('tijiao_on', True)
    set_val('chujia_on', False)
    set_val('chujia_interval', False)  # 间隔结束


def guopai_chujia(price):
    Position_frame = get_val('Position_frame')
    setText(str(price))
    selfdelete()
    Click(Position_frame[1][0], Position_frame[1][1])
    Click(Position_frame[6][0], Position_frame[6][1])

    set_val('yanzhengma_count', 0)  # 计数器，制造延迟
    set_val('yanzhengma_close', False)  # 激活验证码放大  开启查找确认
    set_val('refresh_need', True)  # 激活刷新验证码


##如果一直处理提交状态和查找验证码阶段，取消后重新出价
def Cancel_chujia():
    tijiao_on = get_val('tijiao_on')
    yanzhengma_find = get_val('yanzhengma_find')
    tijiao_ok = get_val('tijiao_ok')
    if tijiao_on and not yanzhengma_find and not tijiao_ok:
        print("触发2")
        Position_frame = get_val('Position_frame')
        Click(Position_frame[7][0], Position_frame[7][1])  # 取消
        userprice = get_val('userprice')
        setText(str(userprice))
        selfdelete()
        Click(Position_frame[1][0], Position_frame[1][1])
        Click(Position_frame[6][0], Position_frame[6][1])
        # 验证码放大打开
        set_val('yanzhengma_close', True)  # 打开验证码放大器 查找确认
        ##提交关闭
        set_val('tijiao_OK', False)


##智能调整
def Smart_ajust_chujia(price):
    Position_frame = get_val('Position_frame')
    Click(Position_frame[7][0], Position_frame[7][1])  # 取消
    setText(str(price))
    selfdelete()
    Click(Position_frame[1][0], Position_frame[1][1])
    Click(Position_frame[6][0], Position_frame[6][1])
    # 验证码放大打开
    set_val('yanzhengma_count', 0)  # 计数器，制造延迟
    set_val('yanzhengma_close', True)  # 打开验证码放大器
    ##提交关闭
    set_val('tijiao_OK', False)


##测试用
def Cancel_chujia_test():
    x, y = win32api.GetCursorPos()
    print(x, y)
    # 615 546
    # 689 559
    from component.read_pic import grab_screen2
    imgpos_yanzhengmaconfirm = get_val('imgpos_yanzhengmaconfirm')

    # img = grab_screen2(region=(x, y, x + 76, y + 16))
    cv2.imwrite('yan_confirm.png', imgpos_yanzhengmaconfirm)

    px, py = win32api.GetCursorPos()
    Position_frame = get_val('Position_frame')
    # Position_frame = get_val('Position_frame')
    # Click(Position_frame[7][0], Position_frame[7][1])  # 取消
    # own_price = get_val('own_price1')
    # setText(str(own_price))
    # selfdelete()
    # Click(Position_frame[1][0], Position_frame[1][1])
    # Click(Position_frame[5][0], Position_frame[5][1])
    # # 验证码放大打开
    # set_val('yanzhengma_count', 0)  # 计数器，制造延迟
    # set_val('yanzhengma_view', True)  # 打开验证码放大器
    # ##提交关闭
    # set_val('tijiao_OK', False)


def OnH_chujia():
    moni_on = get_val('moni_on')

    from component.globalvals import   Varible
    a = Varible.a
    Varible.a = a + 10
    print(a)
    if moni_on:
        Position_frame = get_val('Position_frame')
        lowest_price = get_val('lowest_price')
        one_diff = get_val('one_diff')
        set_val('own_price1', lowest_price + one_diff)
        own_price1 = get_val('own_price1')
        setText(str(own_price1))
        Paste_moni(own_price1)
        Click(Position_frame[1][0], Position_frame[1][1])  ##出价
        Click(Position_frame[6][0], Position_frame[6][1])  ##点击验证码框
        set_val('yanzhengma_close', True)
    else:
        OnH_guopai_chujia()


def OnH_guopai_chujia():
    Position_frame = get_val('Position_frame')
    lowest_price = get_val('lowest_price')
    one_diff = get_val('one_diff')
    set_val('yanzhengma_view', True)
    set_val('yanzhengma_count', 0)
    set_val('own_price1', lowest_price + one_diff)
    own_price1 = get_val('own_price1')
    setText(str(own_price1))
    selfdelete()
    Click(Position_frame[1][0], Position_frame[1][1])
    Click(Position_frame[6][0], Position_frame[6][1])


def selfdelete():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[5][0], Position_frame[5][1])
    many_delete()
    Paste()  # 真粘贴


def selfChujia():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[4][0], Position_frame[4][1])
    Click(Position_frame[0][0], Position_frame[0][1])
    Click(Position_frame[1][0], Position_frame[1][1])
    Click(Position_frame[6][0], Position_frame[6][1])
    set_val('price_view', True)
    set_val('price_count', 0)
    set_val('yanzhengma_count', 0)
    set_val('yanzhengma_view', True)


def selfTijiao():
    Position_frame = get_val('Position_frame')
    Click(Position_frame[2][0], Position_frame[2][1])


def OnClick_Backspace():
    for i in range(6):
        win32api.keybd_event(8, 0, 0, 0)  #
        win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键


def tijiao_ok():
    # tijiao_on = get_val('tijiao_on')
    # enter_on = get_dick('enter_on')
    # smartprice_chujia = get_val('smartprice_chujia')
    # if not enter_on:
    #     set_val('tijiao_OK', True)
    #     set_val('yanzhengma_view', False)
    #     set_val('yanzhengma_close', True)
    #     set_val('yanzhengma_control', False)
    # elif not enter_on and smartprice_chujia:
    #     set_val('tijiao_OK', True)
    #     set_val('yanzhengma_view', False)
    #     set_val('yanzhengma_close', True)
    #     set_val('yanzhengma_control', False)
    pass

def tijiao_ok2():
    enter_on = get_dick('enter_on')
    tijiao_on = get_val('tijiao_on')
    smartprice_chujia = get_val('smartprice_chujia')
    if enter_on :
        set_val('tijiao_OK', True)
        set_val('yanzhengma_close', True)
        set_val('yanzhengma_view', False)
        set_val('yanzhengma_control', False)
    elif enter_on and smartprice_chujia:
        set_val('tijiao_OK', True)
        set_val('yanzhengma_view', False)
        set_val('yanzhengma_close', True)
        set_val('yanzhengma_control', False)




def query():
    query_interval = get_val('query_interval')
    query_on = get_val('query_on')
    Position_frame = get_val('Position_frame')
    if not query_interval and not query_on:
        set_val('query_on', True)
        set_val('query_interval', True)
        moni_on = get_val('moni_on')
        if not moni_on:
            setText(str(1000000))  # 出一定超出的价格
            selfdelete()
        else:
            Paste_moni(1000000)
        Click(Position_frame[1][0], Position_frame[1][1])
        timer1 = threading.Timer(4, query_sleep4)
        timer1.start()
        timer2 = threading.Timer(6, query_sleep6)
        timer2.start()
    elif query_interval and query_on:
        Click(Position_frame[7][0], Position_frame[7][1])
        set_val('query_on', False)


def query_sleep4():
    query_on = get_val('query_on')
    Position_frame = get_val('Position_frame')
    if query_on:
        Click(Position_frame[7][0], Position_frame[7][1])
        set_val('query_on', False)


def query_sleep6():
    set_val('query_interval', False)


def nothing():
    pass


##热键模块
# 快捷键对应的驱动函数   1: TopFrame.handle_Jiajia
VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
           '8': 0x38,
           '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
           'q': 0x51, 'h': 0x48,
           }
user32 = ctypes.windll.user32
HOTKEYS1 = {1: (VK_CODE['2'], win32con.MOD_ALT), 2: (VK_CODE['3'], win32con.MOD_ALT),
            3: (VK_CODE['4'], win32con.MOD_ALT), 4: (VK_CODE['5'], win32con.MOD_ALT),
            5: (VK_CODE['6'], win32con.MOD_ALT), 6: (VK_CODE['7'], win32con.MOD_ALT),
            }
HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
            10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
            13: (VK_CODE['q'], 0x4000), 14: (VK_CODE['h'], 0x4000),
            15: (win32con.VK_ESCAPE, 0x4000),
            16: (win32con.VK_F1, 0x4000), 17: (win32con.VK_F5, 0x4000),
            18: (win32con.VK_F7, 0x4000),}

HOTKEY_ACTIONS = {
    1: Cancel_chujia_test, 2: OnClick_chujia, 3: many_delete,
    4: nothing, 5: nothing,
    6: nothing, 7: OnClick_Shuaxin, 8: selfTijiao,
    9: selfChujia, 10: OnClick_Backspace, 11: tijiao_ok,
    12: tijiao_ok2,
    13: query, 14: OnH_chujia,
    15: esc_chujia,
    16: OnClick_Tijiao, 17: Refresh_web, 18: Onekey_login}


# 启动监听
def Hotkey_listen():
    try:
        msg = wintypes.MSG()
        byref = ctypes.byref
        while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            # print("listening")
            if msg.message == win32con.WM_HOTKEY:
                action_to_take = HOTKEY_ACTIONS.get(msg.wParam)
                # if action_to_take:
                if action_to_take:
                    action_to_take()
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageA(byref(msg))
    except:
        logger.exception("listening stop")
    finally:
        print("失败")
        for id in HOTKEYS1.keys():
            user32.UnregisterHotKey(None, id)
        for id in HOTKEYS2.keys():
            user32.UnregisterHotKey(None, id)
        set_val('listening', False)


##开启
def Hotkey_open():
    try:
        # 注册快捷键
        set_val('hotkey_on', True)
        for id, (vk, modifiers) in HOTKEYS1.items():
            if not user32.RegisterHotKey(None, id, modifiers, vk):
                print("Unable to register id", id)
                set_val('hotkey_on', False)
            else:
                print("成功了1")

        for id, (vk, modifiers) in HOTKEYS2.items():
            if not user32.RegisterHotKey(None, id, modifiers, vk):
                print("Unable to register id", id)
                set_val('hotkey_on', False)
            else:
                print("成功了2")
    except:
        print("绑定失败")
    finally:
        pass


def Hotkey_close():
    try:
        for id in HOTKEYS1.keys():
            user32.UnregisterHotKey(None, id)
        for id in HOTKEYS2.keys():
            user32.UnregisterHotKey(None, id)
        set_val('hotkey_on', False)
    except:
        set_val('hotkey_on', True)
    finally:
        pass


# 创建一个确认进程
class ListenThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ListenThread, self).__init__(*args, **kwargs)
        self.setDaemon(True)
        self.start()

    def run(self):
        # while self.__running.isSet():
        #     self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
        Hotkey_listen()


##时间转化
##将当前时间与 价格列表对应起来
def trans_time():
    pricelist = get_val('price_list')
    lowest_price = get_val('lowest_price')
    a_time = get_val('a_time')
    structtime = time.localtime(a_time)
    timestr = time.strftime("%H-%M-%S", structtime)
    hour, minute, second = timestr.split('-')
    if int(hour) == 11 and int(minute) == 29:
        pricelist[int(second)] = lowest_price


def changetime(a):  # 换算成时间戳
    final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
    return final_time  # 以时间戳输出


def get_nowtime():
    # tem1 = time.time()
    # a = time.strftime('%Y-%m-%d', time.localtime(tem1))
    a = get_val('timebase_str')
    return a  # 输出时间格式字符串


def gettime(choice):  # choice1:55, choice2:0.5
    tem = get_nowtime()
    b = tem + ' 11:29:' + str(int(choice))
    c = changetime(b) + float(choice) - int(choice)
    return c  # 得到用户所确定的最终时间戳


##初始化 还原
def init_strategy():
    strategy_type = get_dick('strategy_type')
    init_description()
    if strategy_type == '0':
        init_strategy0()
    elif strategy_type == '1':
        init_strategy1()
    elif strategy_type == '2':
        init_strategy2()
    elif strategy_type == '3':
        init_strategy3()

def init_strategy0():
    set_val('twice', False)
    set_val('strategy_on', True)
    set_val('chujia_on', True)
    set_val('tijiao_on', False)
    set_val('tijiao_num', 1)  # 初始化
    set_val('tijiao_OK', False)
    set_val('tijiao_one', False)  # 单枪未开
    set_val('smartprice_chujia', False)
    init_label()


def init_strategy1():
    set_val('strategy_on', True)
    set_val('twice', True)
    set_val('chujia_on', True)
    set_val('tijiao_on', False)
    set_val('tijiao_num', 1)  # 初始化
    set_val('tijiao_OK', False)
    set_val('tijiao_one', False)  # 单枪未开
    set_val('smartprice_chujia', False)
    init_label()

def init_strategy2():
    set_val('twice', False)
    set_val('strategy_on', True)
    set_val('chujia_on', True)
    set_val('tijiao_on', False)
    set_val('tijiao_num', 1)  # 初始化
    set_val('tijiao_OK', False)
    set_val('tijiao_one', False)  # 单枪未开
    set_val('smartprice_chujia', False)
    init_label()

def init_strategy3():
    set_val('strategy_on', True)
    set_val('twice', True)
    set_val('chujia_on', True)
    set_val('tijiao_on', False)
    set_val('tijiao_num', 1)  # 初始化
    set_val('tijiao_OK', False)
    set_val('tijiao_one', False)  # 单枪未开
    set_val('smartprice_chujia', False)
    init_label()



def init_label():
    set_val('current_pricestatus_label', '等待第二次出价')
    one_time1 = get_val('one_time1')
    one_diff = get_val('one_diff')
    current_pricestatus = '{0:.1f}秒加{1}'.format(one_time1, one_diff)
    set_val('current_pricestatus', current_pricestatus)






#set_dick('strategy_description', '')
def init_description():
    strategy_type = get_dick('strategy_type')
    if strategy_type == '0': #单枪     'strategy_description': '单枪   48秒加700截止56秒提前100’
        one_time1 = get_val('one_time1')
        one_diff = get_val('one_diff')
        description = f'单枪  {one_time1}秒加{one_diff} 出价'
        set_dick('strategy_description', description)
    elif strategy_type == '1':
        one_time1 = get_val('one_time1')
        second_time1 = get_val('second_time1')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        description = f'双枪  {one_time1}秒加{one_diff}出价  {second_time1}秒加{second_diff}出价'
        set_dick('strategy_description', description)
    elif strategy_type == '2': #单枪     'strategy_description': '单枪   48秒加700截止56秒提前100’
        one_time1 = get_val('one_time1')
        one_diff = get_val('one_diff')
        description = f'单枪动态  {one_time1}秒加{one_diff}出价'
        set_dick('strategy_description', description)
    elif strategy_type == '3':
        one_time1 = get_val('one_time1')
        second_time1 = get_val('second_time1')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        description = f'双枪动态  {one_time1}秒加{one_diff}出价  {second_time1}秒加{second_diff}出价'
        set_dick('strategy_description', description)