'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 9:33
'''
import win32gui
import win32con
import win32api
import win32clipboard
import time
import threading
import pyautogui as pg
from component.variable import set_val, get_val
import ctypes
from ctypes import wintypes


def Click(x, y):  # 鼠标点击
    a = win32gui.GetCursorPos()
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


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


def Paste_moni():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def setText(aString):
    aString = aString.encode('utf-8')
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()


def Delete():
    a = time.clock()
    win32api.keybd_event(0x08, 0, 0, 0)
    win32api.keybd_event(0x08, 0, win32con.KEYEVENTF_KEYUP, 0)
    b = time.clock()


def OnClick_Tijiao():
    one_delay = get_val('one_delay')
    second_delay = get_val('second_delay')
    tijiao_num = get_val('tijiao_num')
    twice = get_val('twice')
    set_val('confirm_need', True)
    if tijiao_num == 1:
        timer = threading.Timer(one_delay, Tijiao)
        timer.start()
        set_val('tijiao_on', False)
        if twice:
            set_val('tijiao_num', 2)
    elif tijiao_num == 2:
        set_val('tijiao_num', 0)
        timer = threading.Timer(second_delay, Tijiao)
        timer.start()
        set_val('tijiao_on', False)
    else:
        Tijiao()


def Tijiao():
    tijiao_on = get_val('tijiao_on')
    tijiao_OK = get_val('tijiao_OK')
    tijiao_num = get_val('tijiao_num')
    chujia_on = get_val('chujia_on')
    Position = get_val('Position')
    Click(Position[2][0], Position[2][1])
    set_val('tijiao_OK', False)  # 需要按E解锁，自动提交
    set_val('chujia_on', True)  # 激活自动
    confirm_one = get_val('confirm_one')
    if not confirm_one:  # 激活确认
        pass


def SmartTijiao():
    tijiao_on = get_val('tijiao_on')
    tijiao_OK = get_val('tijiao_OK')
    tijiao_num = get_val('tijiao_num')
    confirm_need = get_val('confirm_need')
    own_price1 = get_val('own_price1')
    own_price2 = get_val('own_price2')
    moni_on = get_val('moni_on')
    moni_second = get_val('moni_second')
    changetime = get_val('changetime')
    a_time = get_val('a_time')
    lowest_price = get_val('lowest_price')
    twice = get_val('twice')
    set_val('confirm_need', True)
    if moni_on:
        interval = moni_second - changetime
    else:
        interval = a_time - changetime
    if tijiao_num == 2:  # 说明是第二次出价
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
            timer = threading.Timer(0.5, Tijiao)
            timer.start()
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)
        elif lowest_price == own_price1 - 500 and interval < 0.95:
            timesleep = (1 - interval) / 3 + 0.25
            timer = threading.Timer(timesleep, Tijiao)
            timer.start()
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)
        else:
            Tijiao()
            set_val('tijiao_on', False)
            if twice:
                set_val('tijiao_num', 2)


def OnClick_Shuaxin():
    Position = get_val('Position')
    Click(Position[3][0], Position[3][1])
    Click(Position[5][0], Position[5][1])
    yanzhengma_view = get_val('yanzhengma_view')
    yanzhengma_close = get_val('yanzhengma_close')
    yanzhengma_count = get_val('yanzhengma_count')
    set_val('yanzhengma_view', True)  # 激活放大器
    set_val('yanzhengma_count', 0)  # 归零


def OnClick_confirm():
    Position = get_val('Position')
    Click(Position[4][0], Position[4][1])


def OnClick_chujia():
    web_on = get_val('web_on')
    lowest_price = get_val('lowest_price')
    yanzhengma_count = get_val('yanzhengma_count')
    Position = get_val('Position')
    tijiao_num = get_val('tijiao_num')
    own_price1 = get_val('own_price1')
    own_price2 = get_val('own_price2')
    one_diff = get_val('one_diff')
    second_diff = get_val('second_diff')
    tijiao_on = get_val('tijiao_on')
    chujia_on = get_val('chujia_on')
    twice = get_val('twice')
    refresh_need = get_val('refresh_need')
    refresh_one = get_val('refresh_one')
    chujia_interval = get_val('chujia_interval')
    yanzhengma_view = get_val('yanzhengma_view')
    set_val('yanzhengma_count', 0)  # 计数器，制造延迟
    set_val('yanzhengma_view', True)  # 打开验证码放大器
    set_val('tijiao_on', True)  # 激活自动出价
    set_val('refresh_need', True)  # 激活刷新验证码
    if tijiao_num == 1:
        print("我被触发了",  )
        own_price1 = lowest_price + one_diff
        set_val('own_price1', own_price1)
        setText(str(own_price1))
        selfdelete()
        Click(Position[1][0], Position[1][1])
        Click(Position[5][0], Position[5][1])
        set_val('tijiao_on', True)
        set_val('chujia_on', False)
        set_val('chujia_interval', False)  # 间隔结束
    elif tijiao_num == 2 and twice:
        own_price2 = lowest_price + second_diff
        set_val('own_price2', own_price2)
        setText(str(own_price2)) #复制价格到粘贴板
        selfdelete()
        Click(Position[1][0], Position[1][1])
        Click(Position[5][0], Position[5][1])
        set_val('tijiao_on', True)
        set_val('chujia_on', False)
        set_val('chujia_interval', False)  # 间隔结束


def OnH_chujia():
    Position = get_val('Position')
    lowest_price = get_val('lowest_price')
    one_diff = get_val('one_diff')
    set_val('yanzhengma_view', True)
    set_val('yanzhengma_count', 0)
    set_val('own_price1', lowest_price + one_diff)
    own_price1 = get_val('own_price1')
    setText(str(own_price1))
    selfdelete()
    Click(Position[1][0], Position[1][1])
    Click(Position[5][0], Position[5][1])


def selfdelete():
    Position = get_val('Position')
    moni_on = get_val('moni_on')
    Click2(Position[6][0], Position[6][1] - 5)
    Click2(Position[6][0], Position[6][1])
    Click2(Position[6][0], Position[6][1])
    Delete()
    Delete()
    if moni_on:
        Paste_moni()  # 粘贴
    else:
        Paste()  # 真粘贴


def selfChujia():
    Position = get_val('Position')
    Click(Position[4][0], Position[4][1])
    Click(Position[0][0], Position[0][1])
    Click(Position[1][0], Position[1][1])
    Click(Position[5][0], Position[5][1])
    set_val('price_view', True)
    set_val('price_count', 0)
    set_val('yanzhengma_count', 0)
    set_val('yanzhengma_view', True)


def selfTijiao():
    Position = get_val('Position')
    Click(Position[2][0], Position[2][1])


def OnClick_Backspace():
    pg.press('backspace')


def tijiao_ok():
    tijiao_OK = get_val('tijiao_OK')
    refresh_need = get_val('refresh_need')
    tijiao_on = get_val('tijiao_on')
    yanzhengma_close = get_val('yanzhengma_close')
    yanzhengma_view = get_val('yanzhengma_view')
    e_on = get_val('e_on')
    if e_on and tijiao_on:
        print("tijiao_ok")
        set_val('tijiao_OK', True)
        set_val('yanzhengma_view', False)
        set_val('yanzhengma_close', True)


def tijiao_ok2():
    tijiao_OK = get_val('tijiao_OK')
    refresh_need = get_val('refresh_need')
    yanzhengma_close = get_val('yanzhengma_close')
    yanzhengma_view = get_val('yanzhengma_view')
    enter_on = get_val('enter_on')
    tijiao_on = get_val('tijiao_on')
    if enter_on and tijiao_on:
        set_val('tijiao_OK', True)
    if enter_on:
        set_val('yanzhengma_close', True)
        set_val('yanzhengma_view', False)


def query():
    query_interval = get_val('query_interval')
    query_on = get_val('query_on')
    Position = get_val('Position')
    if not query_interval and not query_on:
        set_val('query_on', True)
        set_val('query_interval', True)
        setText(str(1000000))  # 出一定超出的价格
        selfdelete()
        Click(Position[1][0], Position[1][1])
        timer1 = threading.Timer(4, query_sleep4)
        timer1.start()
        timer2 = threading.Timer(6, query_sleep6)
        timer2.start()
    elif query_interval and query_on:
        Click(Position[7][0], Position[7][1])
        set_val('query_on', False)


def query_sleep4():
    query_on = get_val('query_on')
    Position = get_val('Position')
    if query_on:
        Click(Position[7][0], Position[7][1])
        set_val('query_on', False)


def query_sleep6():
    set_val('query_interval', False)


def nothing():
    pass


def Open():
    do = get_val('do')
    if not do:
        set_val('do', True)
        # 定义快捷键                                                                         /
        ############################
        VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                   '8': 0x38,
                   '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                   'q': 0x51, 'h': 0x48}
        user32 = ctypes.windll.user32
        HOTKEYS1 = {1: (VK_CODE['2'], win32con.MOD_ALT), 2: (VK_CODE['3'], win32con.MOD_ALT),
                    3: (VK_CODE['4'], win32con.MOD_ALT), 4: (VK_CODE['5'], win32con.MOD_ALT),
                    5: (VK_CODE['6'], win32con.MOD_ALT), 6: (VK_CODE['7'], win32con.MOD_ALT),
                    }
        HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                    10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                    13: (VK_CODE['q'], 0x4000), 14: (VK_CODE['h'], 0x4000)}
        # 注册快捷键
        for id, (vk, modifiers) in HOTKEYS1.items():
            if not user32.RegisterHotKey(None, id, modifiers, vk):
                print("Unable to register id", id)
                set_val('do', False)
        for id, (vk, modifiers) in HOTKEYS2.items():
            if not user32.RegisterHotKey(None, id, modifiers, vk):
                print("Unable to register id", id)
                set_val('do', False)
            set_val('web_on', True)


# 启动监听
def Listen():
    try:
        # 快捷键对应的驱动函数   1: TopFrame.handle_Jiajia
        VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                   '8': 0x38,
                   '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                   'q': 0x51, 'h': 0x48}
        HOTKEY_ACTIONS = {
            1: nothing, 2: nothing, 3: nothing,
            4: nothing, 5: nothing,
            6: nothing, 7: OnClick_Shuaxin, 8: selfTijiao,
            9: selfChujia, 10: OnClick_Backspace, 11: tijiao_ok,
            12: tijiao_ok2,
            13: query, 14: OnH_chujia}
        user32 = ctypes.windll.user32
        msg = wintypes.MSG()
        byref = ctypes.byref
        while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            # print("listening")
            if msg.message == win32con.WM_HOTKEY:
                action_to_take = HOTKEY_ACTIONS.get(msg.wParam)
                if action_to_take:
                    action_to_take()
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageA(byref(msg))
    finally:
        pass
        # self.Open()
        # self.Listen()
        # for id in HOTKEYS1.keys():
        #     user32.UnregisterHotKey(None, id)
        # for id in HOTKEYS2.keys():
        #     user32.UnregisterHotKey(None, id)


def Close():
    do = get_val('do')
    if do:
        set_val('do', False)
        VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                   '8': 0x38,
                   '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                   'q': 0x51, 'h': 0x48}
        HOTKEYS1 = {1: (VK_CODE['2'], win32con.MOD_ALT), 2: (VK_CODE['3'], win32con.MOD_ALT),
                    3: (VK_CODE['4'], win32con.MOD_ALT), 4: (VK_CODE['5'], win32con.MOD_ALT),
                    5: (VK_CODE['6'], win32con.MOD_ALT), 6: (VK_CODE['7'], win32con.MOD_ALT),
                    }
        user32 = ctypes.windll.user32
        HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                    10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                    13: (VK_CODE['q'], 0x4000), 14: (VK_CODE['h'], 0x4000)}
        for id in HOTKEYS1.keys():
            user32.UnregisterHotKey(None, id)
        for id in HOTKEYS2.keys():
            user32.UnregisterHotKey(None, id)
    else:
        pass


# 创建一个确认进程
class listenThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(listenThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()

    def run(self):
        while 1:
            print("fdsfds")
            Listen()
        # while self.__running.isSet():
        #     self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
        #     Listen()

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
