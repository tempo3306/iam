'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 11:31
'''
import wx
from wx.lib.pubsub import pub
import threading, time
from threading import Thread
import sys, os
from component.imgcut import cut_img, findconfirm, findrefresh, findpos, Price_read, cut_pic
from component.login import ConfirmUser, Keeplogin
from component.staticmethod import OnClick_chujia, OnClick_Tijiao
from component.staticmethod import SmartTijiao
from component.staticmethod import Smart_ajust_chujia
from component.staticmethod import trans_time
from component.variable import get_val, set_val
from PIL import Image
import imagehash

import logging
logger = logging.getLogger()

##初始化打开PNG
import sys
allpath = os.path.abspath(os.path.realpath(sys.argv[0]))
path = os.path.split(allpath)[0] + '\\'  # 分割
set_val('path', path)
path = get_val('path')
yanpath = path + "\\yanzhengma.png"
yanzhengma_img = Image.open(yanpath)
set_val('yanpath', yanpath)
set_val('yanzhengma_img', yanzhengma_img)



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
            winreg.SetValueEx(key, '%s' % name, 0, winreg.REG_DWORD, 0x00002710)  # 10:2710  8:1f40
            winreg.SetValueEx(key, 'python.exe', 0, winreg.REG_DWORD, 0x00002710)  # 10:2710  8:1f40
        except:
            logger.error('HashTread: error in set value!')
            logger.exception('this is an exception message')


class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        for i in range(1000000):
            try:
                findpos_on = get_val('findpos_on')
                if findpos_on:
                    findpos()
            except:
                logger.exception('this is an exception message')


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
                    logger.error("查找确认出错")
                    logger.exception('this is an exception message')

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
                logger.error("刷新失败")
                logger.exception('this is an exception message')

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
            # cut_img()
            try:
                cut_img()
            except:
                logger.error("截图失败")
                logger.exception('this is an exception message')

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
        print(version, "version")
        set_val('login_result', ConfirmUser(Username, Password, version))
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
        for i in range(10000000):
            try:
                time.sleep(0.05)  # 间隔0.05秒判断一次
                lowest_price = get_val('lowest_price')
                own_price1 = get_val('own_price1')
                own_price2 = get_val('own_price2')
                strategy_on = get_val('strategy_on')
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
                ##提交
                if tijiao_on and strategy_on and guopai_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                    if tijiao_num == 1 and a_time >= one_real_time2 and not tijiao_one:  # 判断是否满足条件
                        set_val('tijiao_on', False)
                        SmartTijiao()  # 调用方法
                        set_val('tijiao_on', False)
                        set_val('tijiao_one', True)
                    elif tijiao_num == 2 and a_time >= second_real_time2:  # 判断是否满足条件
                        set_val('tijiao_on', False)
                        SmartTijiao()  # 调用方法
                        set_val('tijiao_on', False)
                    elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and a_time <= one_real_time2 - one_delay and not tijiao_one:  # 价格判断
                        set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
                        OnClick_Tijiao()  # 调用方法
                        set_val('tijiao_one', True)
                    elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and a_time <= second_real_time2 - second_delay:  # 价格判断
                        set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
                        OnClick_Tijiao()  # 调用方法

                if strategy_on and guopai_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                    if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                        set_val('own_price1', lowest_price + one_diff)
                        set_val('userprice', lowest_price + one_diff)
                        set_val('usertime', one_real_time2) #设定当前的截止时间
                        wx.CallAfter(pub.sendMessage, 'change userprice')
                        set_val('tijiao_on', True)
                        OnClick_chujia()  # 调用出价
                    elif tijiao_num == 2 and twice and second_real_time1 <= a_time:  # 判断是否满足条件
                        set_val('own_price2', lowest_price + second_diff)
                        set_val('userprice', lowest_price + second_diff)
                        set_val('usertime', second_real_time2) #设定当前的截止时间
                        wx.CallAfter(pub.sendMessage, 'change userprice')
                        set_val('tijiao_on', True)
                        OnClick_chujia()  # 调用出价
##-----------------------------------------------------------------------------
                ##智能判断价格是否合理
                #以50秒为参考   1100  600   1200  700   1300   800
                smart_ajust = get_val('smart_ajust')
                userprice = get_val('userprice')
                one_diff = get_val('one_diff')
                smart_ajust_time = get_val('smart_ajust_time')
                smart_ajust_time_guopai = get_val('smart_ajust_time_guopai')
                smart_ajust_time_moni = get_val('smart_ajust_time_moni')
                if strategy_on and guopai_on and tijiao_on and smart_ajust:
                    if smart_ajust_time_guopai <= a_time <= smart_ajust_time_guopai + 0.6:
                        if one_diff == 1000:
                            userprice2 = lowest_price + 500
                            diff = userprice2 - userprice
                            if diff == 0 or diff == -100 or  diff == -200 or diff == -300:
                                pass
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price + 500)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price + 600)
                                Smart_ajust_chujia(userprice)
                            elif diff == 200:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price + 700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 100:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price + 800)
                                Smart_ajust_chujia(userprice)

                        elif one_diff == 1100:
                            userprice2 = lowest_price + 600
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100 or  diff == -100 or diff == -200:
                                pass
                            elif diff == -300:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 200:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)
                        elif one_diff == 1200:
                            userprice2 = lowest_price + 700
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100  or diff == 200 or  diff == -100 :
                                pass
                            elif diff == -200:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff == -300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)
                        elif one_diff == 1300:
                            userprice2 = lowest_price + 800
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100 or  diff == 200 or diff == 300:
                                pass
                            elif diff == -100:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff == -200:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff == -300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff < -300 or diff > 300:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)

                ####模拟触发
                moni_on = get_val('moni_on')
                moni_second = get_val('moni_second')
                if strategy_on and moni_on and tijiao_on and smart_ajust:
                    if smart_ajust_time_moni <= moni_second <= smart_ajust_time_moni + 0.6:
                        if one_diff == 1000:
                            userprice2 = lowest_price + 500
                            diff = userprice2 - userprice
                            print(diff)
                            if diff == 0 or diff == -100 or  diff == -200 or diff == -300:
                                pass
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price + 500)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price + 600)
                                Smart_ajust_chujia(userprice)
                            elif diff == 200:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price + 700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 100:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price + 800)
                                Smart_ajust_chujia(userprice)

                        elif one_diff == 1100:
                            userprice2 = lowest_price + 600
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100 or  diff == -100 or diff == -200:
                                pass
                            elif diff == -300:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 200:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)
                        elif one_diff == 1200:
                            userprice2 = lowest_price + 700
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100  or diff == 200 or  diff == -100 :
                                pass
                            elif diff == -200:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff == -300:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff<-300 or diff>300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff == 300:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)
                        elif one_diff == 1300:
                            userprice2 = lowest_price + 800
                            diff = userprice2 - userprice
                            if diff == 0 or diff == 100 or  diff == 200 or diff == 300:
                                pass
                            elif diff == -100:
                                userprice = lowest_price + 500
                                set_val('userprice', lowest_price+500)
                                Smart_ajust_chujia(userprice)
                            elif diff == -200:
                                userprice = lowest_price + 600
                                set_val('userprice', lowest_price+600)
                                Smart_ajust_chujia(userprice)
                            elif diff == -300:
                                userprice = lowest_price + 700
                                set_val('userprice', lowest_price+700)
                                Smart_ajust_chujia(userprice)
                            elif diff < -300 or diff > 300:
                                userprice = lowest_price + 800
                                set_val('userprice', lowest_price+800)
                                Smart_ajust_chujia(userprice)
##-----------------------------------------------------------------------------
                ## 模拟提交
                moni_second = get_val('moni_second')
                strategy_on = get_val('strategy_on')
                moni_on = get_val('moni_on')
                tijiao_on = get_val('tijiao_on')
                own_price1 = get_val('own_price1')
                own_price2 = get_val('own_price2')
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
                if tijiao_on and strategy_on and moni_on and tijiao_OK:  # 判断是否需要提交，模拟开启方可触发
                    if tijiao_num == 1 and moni_second >= one_time2 and not tijiao_one:  # 判断是否满足条件
                        SmartTijiao()  # 调用方法
                        set_val('tijiao_on', False)
                        set_val('tijiao_one', True)  # 第一枪已开
                    elif tijiao_num == 2 and moni_second >= second_time2 and twice:  # 判断是否满足条件
                        SmartTijiao()  # 调用方法
                        set_val('tijiao_on', False)
                    elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and not tijiao_one:  # 价格判断
                        set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
                        OnClick_Tijiao()  # 调用方法
                        set_val('tijiao_one', True)  # 第一枪已开
                    elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and twice:  # 价格判断
                        set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
                        OnClick_Tijiao()  # 调用方法
                if strategy_on and moni_on and chujia_on:  # 判断是否需要出价,模拟开启方可触发
                    if tijiao_num == 1 and one_time1 <= moni_second <= one_time1 + 0.6:  # 判断是否满足条件
                        wx.CallAfter(pub.sendMessage, 'moni chujia')  # 调用方法
                        set_val('own_price1', lowest_price + one_diff)
                        set_val('userprice', lowest_price + one_diff)
                        set_val('usertime', one_time2) #设定当前的截止时间
                        wx.CallAfter(pub.sendMessage, 'change userprice')
                        set_val('tijiao_on', True)
                    elif tijiao_num == 2 and twice and second_time1 <= moni_second:
                        wx.CallAfter(pub.sendMessage, 'moni chujia')  # 调用方法
                        set_val('own_price2', lowest_price + second_diff)
                        set_val('userprice', lowest_price + second_diff) #当前的出价
                        set_val('usertime', second_time2)
                        wx.CallAfter(pub.sendMessage, 'change userprice')
                        set_val('tijiao_on', True)
            except:
                logger.error("提交出错")
                logger.exception('this is an exception message')


# class MoniTijiaoThread(Thread):
#     def __init__(self):
#         """Init Worker Thread Class."""
#         Thread.__init__(self)
#         self.setDaemon(True)
#         self.start()  # start the thread
#
#     def run(self):
#         for i in range(10000000):
#             time.sleep(0.05)  # 间隔0.1秒判断一次
#             moni_second = get_val('moni_second')
#             strategy_on = get_val('strategy_on')
#             moni_on = get_val('moni_on')
#             tijiao_on = get_val('tijiao_on')
#             own_price1 = get_val('own_price1')
#             own_price2 = get_val('own_price2')
#             tijiao_num = get_val('tijiao_num')
#             tijiao_OK = get_val('tijiao_OK')
#             one_advance = get_val('one_advance')
#             second_advance = get_val('second_advance')
#             tijiao_one = get_val('tijiao_one')
#             one_time1 = get_val('one_time1')
#             one_time2 = get_val('one_time2')
#             second_time1 = get_val('second_time1')
#             second_time2 = get_val('second_time2')
#             lowest_price = get_val('lowest_price')
#             chujia_on = get_val('chujia_on')
#             twice = get_val('twice')
#             one_diff = get_val('one_diff')
#             second_diff = get_val('second_diff')
#             if tijiao_on and strategy_on and moni_on and tijiao_OK:  # 判断是否需要提交，模拟开启方可触发
#                 if tijiao_num == 1 and moni_second >= one_time2 and not tijiao_one:  # 判断是否满足条件
#                     SmartTijiao()  # 调用方法
#                     set_val('tijiao_on', False)
#                     set_val('tijiao_one', True)  # 第一枪已开
#                 elif tijiao_num == 2 and moni_second >= second_time2 and twice:  # 判断是否满足条件
#                     SmartTijiao()  # 调用方法
#                     set_val('tijiao_on', False)
#                 elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and not tijiao_one:  # 价格判断
#                     set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
#                     OnClick_Tijiao()  # 调用方法
#                     set_val('tijiao_one', True)  # 第一枪已开
#                 elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and twice:  # 价格判断
#                     set_val('tijiao_on', False)  # 执行提交之后只能通过选择进程开启自动提交
#                     OnClick_Tijiao()  # 调用方法
#             if strategy_on and moni_on and chujia_on:  # 判断是否需要出价,模拟开启方可触发
#                 if tijiao_num == 1 and one_time1 <= moni_second <= one_time1 + 0.6:  # 判断是否满足条件
#                     OnClick_chujia()  # 调用方法
#                     print("第一次")
#                     set_val('own_price1', lowest_price + one_diff)
#                     set_val('tijiao_on', True)
#                 elif tijiao_num == 2 and twice and second_time1 <= moni_second:
#                     OnClick_chujia()  # 调用方法
#                     print("第二次")
#                     set_val('own_price2', lowest_price + second_diff)
#                     set_val('tijiao_on', True)


# 时间进程
class TimeThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            a_time = get_val('a_time')
            moni_second = get_val('moni_second')
            a_time += b - a  # 实际运行时间作为真实间隔
            moni_second += b - a
            set_val('a_time', a_time)
            set_val('moni_second', moni_second)
            if moni_second >= 60:
                set_val('moni_second', 0)

            ##计数，保证间隔
            price_count = get_val('price_count')
            yanzhengma_count = get_val('yanzhengma_count')
            set_val('price_count', 1 + price_count)
            set_val('yanzhengma_count', 1 + yanzhengma_count)

# ---------------------------------------
# 打开浏览器
# 打开浏览器
import winreg, re, subprocess

needpath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'


def getwebpath():
    global needpath
    # 查找注册表键值
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            needpath = result[0]
            # needpath='"'+result[0]+'"'
    except:
        logger.exception('this is an exception message')

    if not os.path.exists(needpath):
        if os.path.exists('C:\Program Files (x86)'):
            pass
            # os.walk()


def openweb(url):
    global needpath
    # command="\""+needpath+"\"" +" "+url  #需要加个空格
    # path=r'C:\Program Files (x86)\Internet Explorer\iexplore.exe www.baidu.com'
    subprocess.Popen([needpath, url])


def openIE(url):
    global iepath
    subprocess.Popen([iepath, url])


class OpenwebThread(Thread):
    def __init__(self, url):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.url = url
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        openweb(self.url)

class GetremotetimeThread(Thread):
    def __init__(self, url):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.url = url
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        from component.staticmethod import web_request
        try:
            remotetime_url = get_val('remotetime_url')
            result = web_request(remotetime_url)
            remotetime = result['remotetime']
            set_val('a_time', remotetime+0.3) #补网络延迟
        except:
            logger.exception('this is an exception message')

## 设置一个截屏取价  和查看时间
##
class LowestpfriceThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        for i in range(10000000):
            time.sleep(0.035)
            a = time.time()
            lowest_price = get_val('lowest_price')
            pricelist = get_val('pricelist')
            moni_second = get_val('moni_second')
            a_time = get_val('a_time')
            moni_on = get_val('moni_on')
            try:
                price = int(Price_read())  # 获取当前最低价
                if price in pricelist:  # 字典查找
                    set_val('findpos_on', False)
                    if lowest_price == price:
                        trans_time()  # 保存价格
                    else:
                        set_val('lowest_price', price)
                        trans_time()  # 保存价格
                        if moni_on:
                            set_val('changetime', moni_second)
                        else:
                            set_val('changetime', a_time)
                else:
                    set_val('findpos_on', True)
            except:
                set_val('findpos_on', True)

            c = time.time()
            print(c-a, 'c-a')

