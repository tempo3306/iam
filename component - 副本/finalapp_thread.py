'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 11:31
'''
import wx
from wx.lib.pubsub import pub
import threading,time
from threading import Thread
import winreg
import sys,os
from .imgcut import cut_img,findconfirm,findrefresh,findpos
from .login import ConfirmUser,Keeplogin
from .staticmethod import OnClick_chujia,OnClick_Tijiao,OnClick_Shuaxin,OnClick_confirm
from .staticmethod import SmartTijiao
from .variable import get_val,set_val
class HashThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread
    def run(self):
        """Run Worker Thread."""
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION", 0,
                             winreg.KEY_ALL_ACCESS)
        try:
            name = os.path.realpath(sys.argv[0])  # 获取运行路径
            name = name.split('\\')[-1]
            winreg.SetValueEx(key, '%s'%name, 0, winreg.REG_DWORD, 0x00002710)    #10:2710  8:1f40
        except:
            print('error in set value!')
class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()
    def run(self):
        for i in range(1000000):
            findpos_on = get_val('findpos_on')
            if findpos_on:
                findpos()
class confirmThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(confirmThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.035)
            tijiao_num = get_val('tijiao_num')
            if tijiao_num == 2:
                try:
                    findconfirm()
                except:
                    print("查找确认出错")
    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞
    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞
    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
class refreshThread(Thread):
    def __init__(self, *args, **kwargs):
        super(refreshThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.05)
            try:
                findrefresh()
            except:
                print("刷新失败")
    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞
    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞
    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
class cutimgThread(Thread):
    def __init__(self, *args, **kwargs):
        super(cutimgThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.04)
            try:
                cut_img()
            except:
                print("截图失败")
    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞
    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞
    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
class LoginThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    def run(self):
        Username = get_val('Username')
        Password = get_val('Password')
        login_result = get_val('login_result')
        version = get_val('version')
        set_val('login_result',ConfirmUser(Username,Password,version))
        print(login_result)
        wx.CallAfter(pub.sendMessage, "connect")
class controlThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    def run(self):
        wx.Sleep(10)
        wx.CallAfter(pub.sendMessage, "connect failure")
class KeepThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    def run(self):
        for i in range(1000000):
            time.sleep(90)
            Keeplogin()
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    def run(self):
        tijiao_delay = get_val('tijiao_delay')
        final_tijiao = get_val('final_tijiao')
        strategy_price = get_val('strategy_price')
        lowest_price = get_val('lowest_price')
        own_price1 = get_val('own_price1')
        own_price2 = get_val('own_price2')
        moni_second = get_val('moni_second')
        strategy_on = get_val('strategy_on')
        moni_on = get_val('moni_on')
        tijiao_on = get_val('tijiao_on')
        tijiao_OK = get_val('tijiao_OK')
        second_real_time1 = get_val('second_real_time1')
        second_real_time2 = get_val('second_real_time2')
        one_advance = get_val('one_advance')
        second_advance = get_val('second_advance')
        tijiao_num = get_val('tijiao_num')
        tijiao_OK = get_val('tijiao_OK')
        chujia_on = get_val('chujia_on')
        tijiao_on = get_val('tijiao_on')
        tijiao_one = get_val('tijiao_one')
        a_time = get_val('a_time')
        one_real_time1 = get_val('one_real_time1')
        one_real_time2 = get_val('one_real_time2')
        guopai_on = get_val('guopai_on')
        twice = get_val('twice')
        one_delay = get_val('one_delay')
        second_delay = get_val('second_delay')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        for i in range(10000000):
            time.sleep(0.05)  # 间隔0.1秒判断一次
            if tijiao_on and strategy_on and guopai_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and a_time >= one_real_time2 and not tijiao_one:  # 判断是否满足条件
                    set_val('tijiao_on',False)
                    SmartTijiao()  # 调用方法
                    set_val('tijiao_on',False)
                    set_val('tijiao_one',True)
                elif tijiao_num == 2 and a_time >= second_real_time2:  # 判断是否满足条件
                    set_val('tijiao_on',False)
                    SmartTijiao()  # 调用方法
                    set_val('tijiao_on',False)
                elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and a_time <= one_real_time2 - one_delay and not tijiao_one:  # 价格判断
                    set_val('tijiao_on',False)
                    set_val('tijiao_on',False)  #执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
                    set_val('tijiao_one',True)
                elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and a_time <= second_real_time2 - second_delay:  # 价格判断
                    set_val('tijiao_on',False)
                    set_val('tijiao_on',False)  #执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
            if strategy_on and guopai_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                    OnClick_chujia()  # 调用出价
                    set_val('own_price1',lowest_price+one_diff)
                    set_val('tijiao_on',True)
                elif tijiao_num == 2 and twice and second_real_time1 <= a_time:  # 判断是否满足条件
                    OnClick_chujia()  # 调用出价
                    set_val('own_price2',lowest_price+second_diff)
                    set_val('tijiao_on',True)
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    def run(self):
        moni_second = get_val('moni_second')
        strategy_on = get_val('strategy_on')
        moni_on = get_val('moni_on')
        tijiao_on = get_val('tijiao_on')
        own_price1 = get_val('own_price1')
        own_price2 = get_val('own_price2')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        tijiao_num = get_val('tijiao_num')
        tijiao_OK = get_val('tijiao_OK')
        one_advance = get_val('one_advance')
        second_advance = get_val('second_advance')
        tijiao_one = get_val('tijiao_one')
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        lowest_price = get_val('lowest_price')
        chujia_on = get_val('chujia_on')
        twice = get_val('twice')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        for i in range(10000000):
            time.sleep(0.05)  # 间隔0.1秒判断一次
            if tijiao_on and strategy_on and moni_on and tijiao_OK:  # 判断是否需要提交，模拟开启方可触发
                if tijiao_num == 1 and moni_second >= one_time2 and not tijiao_one:  # 判断是否满足条件
                    SmartTijiao()  # 调用方法
                    set_val('tijiao_on',False)
                    set_val('tijiao_one',True)  #第一枪已开
                elif tijiao_num == 2 and moni_second >= second_time2 and twice:  # 判断是否满足条件
                    SmartTijiao()  # 调用方法
                    set_val('tijiao_on',False)
                elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and not tijiao_one:  # 价格判断
                    set_val('tijiao_on',False)  #执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
                    set_val('tijiao_one',True)  #第一枪已开
                elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and twice:  # 价格判断
                    set_val('tijiao_on',False)  #执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
            if strategy_on and moni_on and chujia_on:  # 判断是否需要出价,模拟开启方可触发
                if tijiao_num == 1 and one_time1 <= moni_second <= one_time1 + 0.6:  # 判断是否满足条件
                    OnClick_chujia()  # 调用方法
                    print("第一次")
                    set_val('own_price1',lowest_price+one_diff)
                    set_val('tijiao_on',True)
                elif tijiao_num == 2 and twice and second_time1 < moni_second:
                    OnClick_chujia()  # 调用方法
                    print("第二次")
                    set_val('own_price2',lowest_price+second_diff)
                    set_val('tijiao_on',True)
