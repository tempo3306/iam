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
from component.imgcut import cut_img, findconfirm, findrefresh, findpos, Price_read
from component.login import ConfirmUser, Keeplogin, ConfirmCode, MoniTest, Confirm_firstprice
from component.staticmethod import OnClick_chujia, OnClick_Tijiao, calculate_usetime
from component.staticmethod import Smart_ajust_chujia
from component.staticmethod import trans_time
from component.variable import get_val, set_val, get_dick
from component.remote_control import getip_dianxin
from component.staticmethod import init_strategy

import logging

logger = logging.getLogger()

##初始化打开PNG
import sys

allpath = os.path.abspath(os.path.realpath(sys.argv[0]))
path = os.path.split(allpath)[0] + '\\'  # 分割
set_val('path', path)
path = get_val('path')
# yimg = ImageGrab.grab().save("yanzhengma.png")
yanpath = path + "\\yanzhengma.png"
# yanzhengma_img = Image.open(yanpath)
set_val('yanpath', yanpath)
set_val('yanzhengma_img', None)


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
    def __init__(self, *args, **kwargs):
        super(findposThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            time.sleep(0.4)
            try:
                findpos_on = get_val('findpos_on')
                if findpos_on:
                    findpos()
            except:
                logger.exception('this is an exception message')

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


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
            twice = get_val('twice')
            # print('tijiao_num', tijiao_num)
            smartprice_chujia = get_val('smartprice_chujia')
            if tijiao_num == 2 and twice:
                try:
                    findconfirm()
                except:
                    logger.error("查找确认出错")
                    logger.exception('this is an exception message')
            elif smartprice_chujia:
                try:
                    findconfirm()
                except:
                    logger.error("智能补枪失败")
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
                final_stage = get_val('final_stage')
                if final_stage:
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
            time.sleep(0.05)
            self.run_func()

    # @calculate_usetime
    def run_func(self):
        try:
            ###################截图
            a = time.time()
            cut_img()
            self.find_confirm()
            self.find_refresh()
            self.read_lowest_price()
        except:
            logger.error("截图失败")
            logger.exception('this is an exception message')

    # @calculate_usetime
    def find_confirm(self):
        ##################查找确认
        tijiao_num = get_val('tijiao_num')
        twice = get_val('twice')
        # print('tijiao_num', tijiao_num)
        smartprice_chujia = get_val('smartprice_chujia')
        if tijiao_num == 2 and twice:
            try:
                findconfirm()
            except:
                logger.error("查找确认出错")
                logger.exception('this is an exception message')
        elif smartprice_chujia:
            try:
                findconfirm()
            except:
                logger.error("智能补枪失败")
                logger.exception('this is an exception message')
        # c = time.time()
        # print('c-b', c-b)

    ###################查找刷新
    # @calculate_usetime
    def find_refresh(self):
        try:
            findrefresh()
        except:
            logger.error("刷新失败")
            logger.exception('this is an exception message')
        # d = time.time()
        # print('d-c', d-c)

    ###################lowestprice
    # @calculate_usetime
    def read_lowest_price(self):
        lowest_price = get_val('lowest_price')
        lowestpricelist = get_val('lowestpricelist')
        a_time = get_val('a_time')
        try:
            str_price = Price_read()
            if len(str_price) == 5:  ##防止前面
                price = int(str_price)  # 获取当前最低价
                # print('price=', price)
                if price in lowestpricelist:  # 字典查找
                    set_val('findpos_on', False)
                    if lowest_price == price:
                        trans_time()  # 保存价格
                    else:
                        set_val('lowest_price', price)
                        trans_time()  # 保存价格
                        set_val('changetime', a_time)
                else:
                    set_val('findpos_on', True)
            else:
                set_val('findpos_on', True)

        except:
            # print("识别价格失败")
            set_val('findpos_on', True)
            logger.error("识别价格失败")
            logger.exception('this is an exception message')

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


# class LoginThread(Thread):
#     def __init__(self, *args, **kwargs):
#         super(LoginThread, self).__init__(*args, **kwargs)
#         self.__flag = threading.Event()  # 用于暂停线程的标识
#         self.__flag.set()  # 设置为True
#         self.__running = threading.Event()  # 用于停止线程的标识
#         self.__running.set()  # 将running设置为True
#         self.setDaemon(True)
#         self.start()  # start the thread
#
#     def run(self):
#         Username = get_val('Username')
#         Password = get_val('Password')
#         login_result = get_val('login_result')
#         version = get_val('version')
#         print(version, "version")
#         set_val('login_result', ConfirmUser(Username, Password, version))
#         print(login_result)
#         wx.CallAfter(pub.sendMessage, "connect")
#
#     def pause(self):
#         self.__flag.clear()  # 设置为False, 让线程阻塞
#
#     def resume(self):
#         self.__flag.set()  # 设置为True, 让线程停止阻塞
#
#     def stop(self):
#         self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
#         self.__running.clear()  # 设置为False

class MoniThread(Thread):
    def __init__(self, *args, **kwargs):
        super(MoniThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        set_val('login_result', MoniTest())
        wx.CallAfter(pub.sendMessage, "monitest")

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False




class Login_codeThread(Thread):
    def __init__(self, *args, **kwargs):
        super(Login_codeThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        identify_code = get_val('Identify_code')
        version = get_val('version')
        set_val('login_result', ConfirmCode(identify_code, version))
        wx.CallAfter(pub.sendMessage, "connect")

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


class Confirmfirstprice_thread(Thread):
    def __init__(self, *args, **kwargs):
        super(Confirmfirstprice_thread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        identify_code = get_val('Identify_code')
        version = get_val('version')
        result = Confirm_firstprice()
        print(result)
        wx.CallAfter(pub.sendMessage, "firstprice", result=result)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False



class controlThread(Thread):
    def __init__(self, *args, **kwargs):
        super(controlThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        wx.Sleep(10)
        wx.CallAfter(pub.sendMessage, "connect failure")

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


class KeepThread(Thread):
    def __init__(self, *args, **kwargs):
        super(KeepThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        for i in range(1000000):
            time.sleep(90)
            # Keeplogin()

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


class TijiaoThread(Thread):
    def __init__(self, *args, **kwargs):
        super(TijiaoThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()  # start the thread

    def run(self):
        for i in range(10000000):
            try:
                time.sleep(0.025)  # 间隔0.025秒判断一次
                self.chujia()
                self.tijiao()
                self.smart_chujia()
            except:
                logger.error("提交出错")
                logger.exception('this is an exception message')


    def tijiao(self):
        # -------------------------------------------------------
        lowest_price = get_val('lowest_price')
        own_price1 = get_val('own_price1')
        own_price2 = get_val('own_price2')
        strategy_on = get_val('strategy_on')
        second_real_time2 = get_val('second_real_time2')
        one_advance = get_val('one_advance')
        second_advance = get_val('second_advance')
        tijiao_num = get_val('tijiao_num')
        tijiao_OK = get_val('tijiao_OK')
        tijiao_on = get_val('tijiao_on')
        a_time = get_val('a_time')
        one_real_time2 = get_val('one_real_time2')
        one_delay = get_val('one_delay')
        second_delay = get_val('second_delay')
        smartprice_chujia = get_val('smartprice_chujia')  ##智能出价
        one_forcetijiao_on = get_val('one_forcetijiao_on')
        second_forcetijiao_on = get_val('second_forcetijiao_on')
        strategy_type = get_dick('strategy_type')
        ##提交
        one_advance_smart1 = get_val('one_advance_smart1')
        one_delay_smart1 = get_val('one_delay_smart1')
        one_realtime2_smart1 = get_val('one_realtime2_smart1')
        one_advance_smart2 = get_val('one_advance_smart2')
        one_delay_smart2 = get_val('one_delay_smart2')
        one_realtime2_smart2 = get_val('one_realtime2_smart2')
        one_advance_smart3 = get_val('one_advance_smart3')
        one_delay_smart3 = get_val('one_delay_smart3')
        one_realtime2_smart3 = get_val('one_realtime2_smart3')
        one_realtime2_smart = get_val('one_realtime2_smart')
        ##提交
        if strategy_type == '2':  ##单枪动态提交
            if tijiao_on and strategy_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                if lowest_price >= own_price1 - 300 - one_advance_smart1 and a_time <= one_realtime2_smart1 + 0.1:  # 判断是否满足条件
                    OnClick_Tijiao(one_delay_smart1)
                elif lowest_price >= own_price1 - 300 - one_advance_smart2 \
                        and one_realtime2_smart1 + 0.1 <= a_time <= one_realtime2_smart2 + 0.1:  # 判断是否满足条件
                    OnClick_Tijiao(one_delay_smart2)
                elif lowest_price >= own_price1 - 300 - one_advance_smart3 \
                        and one_realtime2_smart2 + 0.1 <= a_time \
                        <= min(one_realtime2_smart3 + 0.1, one_realtime2_smart - one_delay_smart3):  # 判断是否满足条件
                    OnClick_Tijiao(one_delay_smart3)
                elif a_time >= one_realtime2_smart:  # 截止时间
                    OnClick_Tijiao()
        elif strategy_type == '3':  ##双枪动态提交
            if tijiao_on and strategy_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1:
                    if a_time >= one_real_time2 and one_forcetijiao_on:  # 判断是否满足条件
                        OnClick_Tijiao()
                    elif lowest_price >= own_price1 - 300 - one_advance and a_time <= one_real_time2 - one_delay:  # 价格判断
                        OnClick_Tijiao(one_delay)
                    elif lowest_price >= own_price1 - 300 - one_advance and a_time > one_real_time2:  # 价格判断
                        OnClick_Tijiao()  ##价格到了，同时时间也到了
                elif tijiao_num == 2:
                    if lowest_price >= own_price2 - 300 - one_advance_smart1 and a_time <= one_realtime2_smart1 + 0.1:  # 判断是否满足条件
                        OnClick_Tijiao(one_delay_smart1)
                    elif lowest_price >= own_price2 - 300 - one_advance_smart2 \
                            and one_realtime2_smart1 + 0.1 <= a_time <= one_realtime2_smart2 + 0.1:  # 55.1时间会有点超出
                        OnClick_Tijiao(one_delay_smart2)
                    elif lowest_price >= own_price2 - 300 - one_advance_smart3 \
                            and one_realtime2_smart2 + 0.1 <= a_time \
                            <= min(one_realtime2_smart3 + 0.1, one_realtime2_smart - one_delay_smart3):  # 判断是否满足条件
                        OnClick_Tijiao(one_delay_smart3)  # 考虑延迟时间
                    elif a_time >= one_realtime2_smart:  # 截止时间
                        OnClick_Tijiao()
        else:
            if tijiao_on and strategy_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and a_time >= one_real_time2 and one_forcetijiao_on:  # 判断是否满足条件
                    OnClick_Tijiao(one_delay)
                    # SmartTijiao()
                elif tijiao_num == 2 and a_time >= second_real_time2 and second_forcetijiao_on:  # 判断是否满足条件
                    OnClick_Tijiao(second_delay)
                    # SmartTijiao()
                elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and a_time <= one_real_time2 - one_delay:  # 价格判断
                    OnClick_Tijiao(one_delay)
                elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and a_time <= second_real_time2 - second_delay:  # 价格判断
                    OnClick_Tijiao(second_delay)

        ###-----------------------------------------------------------------------------
        ##智能出价之后提交判定
        userprice = get_val('userprice')
        final_time = get_val('final_time')
        # print('smartprice_chujia', smartprice_chujia)
        # print('tijiao_OK', tijiao_OK)
        if smartprice_chujia and tijiao_OK:
            if lowest_price >= userprice - 300 or a_time >= final_time:
                set_val('smartprice_chujia', False)  ##关闭确认查找，停止智能出价
                print("智能提交ffffffffffffff")
                OnClick_Tijiao()  # 调用方法




    def chujia(self):
        # -------------------------------------------------------
        lowest_price = get_val('lowest_price')
        strategy_on = get_val('strategy_on')
        second_real_time1 = get_val('second_real_time1')
        second_real_time2 = get_val('second_real_time2')
        tijiao_num = get_val('tijiao_num')
        chujia_on = get_val('chujia_on')
        a_time = get_val('a_time')
        one_real_time1 = get_val('one_real_time1')
        one_real_time2 = get_val('one_real_time2')
        twice = get_val('twice')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        strategy_type = get_dick('strategy_type')
        one_realtime2_smart = get_val('one_realtime2_smart')
        ##出价
        if strategy_type == '2':  ##如果为动态提交
            if strategy_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                    set_val('own_price1', lowest_price + one_diff)
                    set_val('userprice', lowest_price + one_diff)
                    set_val('usertime', one_realtime2_smart)
                    OnClick_chujia()  # 调用出价
        elif strategy_type == '3':
            if strategy_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                    set_val('own_price1', lowest_price + one_diff)
                    set_val('userprice', lowest_price + one_diff)
                    set_val('usertime', one_real_time2)  # 设定当前的截止时间
                    OnClick_chujia()  # 调用出价
                elif tijiao_num == 2 and twice and second_real_time1 <= a_time:  # 判断是否满足条件
                    set_val('own_price2', lowest_price + second_diff)
                    set_val('userprice', lowest_price + second_diff)
                    set_val('usertime', one_realtime2_smart)  # 设定当前的截止时间
                    set_val('tijiao_on', True)
                    ##国拍与模拟触发方式不一样
                    OnClick_chujia()  # 调用出价
        else:
            if strategy_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                    set_val('own_price1', lowest_price + one_diff)
                    set_val('userprice', lowest_price + one_diff)
                    set_val('usertime', one_real_time2)  # 设定当前的截止时间
                    OnClick_chujia()  # 调用出价
                elif tijiao_num == 2 and twice and second_real_time1 <= a_time:  # 判断是否满足条件
                    set_val('own_price2', lowest_price + second_diff)
                    set_val('userprice', lowest_price + second_diff)
                    set_val('usertime', second_real_time2)  # 设定当前的截止时间
                    set_val('tijiao_on', True)
                    ##国拍与模拟触发方式不一样
                    OnClick_chujia()  # 调用出价



    def smart_chujia(self):
        ###-----------------------------------------------------------------------------
        lowest_price = get_val('lowest_price')
        strategy_on = get_val('strategy_on')
        tijiao_on = get_val('tijiao_on')
        a_time = get_val('a_time')
        guopai_on = get_val('guopai_on')
        ##智能判断价格是否合理
        # 以50秒为参考   1100  600   1200  700   1300   800
        smart_ajust = get_val('smart_ajust')
        userprice = get_val('userprice')
        one_diff = get_val('one_diff')
        smart_ajust_time_guopai = get_val('smart_ajust_time_guopai')
        if strategy_on and guopai_on and tijiao_on and smart_ajust:
            if smart_ajust_time_guopai <= a_time <= smart_ajust_time_guopai + 0.6:
                if one_diff == 1000:
                    userprice2 = lowest_price + 500
                    diff = userprice2 - userprice
                    if diff == 0 or diff == -100 or diff == -200 or diff == -300:
                        pass
                    elif diff < -300 or diff > 300:
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
                    if diff == 0 or diff == 100 or diff == -100 or diff == -200:
                        pass
                    elif diff == -300:
                        userprice = lowest_price + 500
                        set_val('userprice', lowest_price + 500)
                        Smart_ajust_chujia(userprice)
                    elif diff < -300 or diff > 300:
                        userprice = lowest_price + 600
                        set_val('userprice', lowest_price + 600)
                        Smart_ajust_chujia(userprice)
                    elif diff == 300:
                        userprice = lowest_price + 700
                        set_val('userprice', lowest_price + 700)
                        Smart_ajust_chujia(userprice)
                    elif diff == 200:
                        userprice = lowest_price + 800
                        set_val('userprice', lowest_price + 800)
                        Smart_ajust_chujia(userprice)
                elif one_diff == 1200:
                    userprice2 = lowest_price + 700
                    diff = userprice2 - userprice
                    if diff == 0 or diff == 100 or diff == 200 or diff == -100:
                        pass
                    elif diff == -200:
                        userprice = lowest_price + 500
                        set_val('userprice', lowest_price + 500)
                        Smart_ajust_chujia(userprice)
                    elif diff == -300:
                        userprice = lowest_price + 600
                        set_val('userprice', lowest_price + 600)
                        Smart_ajust_chujia(userprice)
                    elif diff < -300 or diff > 300:
                        userprice = lowest_price + 700
                        set_val('userprice', lowest_price + 700)
                        Smart_ajust_chujia(userprice)
                    elif diff == 300:
                        userprice = lowest_price + 800
                        set_val('userprice', lowest_price + 800)
                        Smart_ajust_chujia(userprice)
                elif one_diff == 1300:
                    userprice2 = lowest_price + 800
                    diff = userprice2 - userprice
                    if diff == 0 or diff == 100 or diff == 200 or diff == 300:
                        pass
                    elif diff == -100:
                        userprice = lowest_price + 500
                        set_val('userprice', lowest_price + 500)
                        Smart_ajust_chujia(userprice)
                    elif diff == -200:
                        userprice = lowest_price + 600
                        set_val('userprice', lowest_price + 600)
                        Smart_ajust_chujia(userprice)
                    elif diff == -300:
                        userprice = lowest_price + 700
                        set_val('userprice', lowest_price + 700)
                        Smart_ajust_chujia(userprice)
                    elif diff < -300 or diff > 300:
                        userprice = lowest_price + 800
                        set_val('userprice', lowest_price + 800)
                        Smart_ajust_chujia(userprice)



    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


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
    def __init__(self, *args, **kwargs):
        super(TimeThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.05)
            b = time.clock()
            a_time = get_val('a_time')
            a_time += b - a  # 实际运行时间作为真实间隔f
            set_val('a_time', a_time)
            one_real_time1 = get_val('one_real_time1')
            try:
                if one_real_time1 > a_time + 0.5:  ##只要出现时间小于第一次出价就触发还原
                    init_strategy()
                start_time = get_val('start_time')
                target_time = get_val('target_time')

                if start_time < a_time < target_time:  ##11点到11点半之间
                    set_val("final_stage", True)
                else:
                    set_val("final_stage", False)
            except:
                logger.exception("error message")

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


# ---------------------------------------
# 打开浏览器
# 打开浏览器
import winreg, re, subprocess

needpath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'
import wx
set_val('neddpath', needpath)

def getwebpath():
    # 查找注册表键值
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            needpath = result[0]
            set_val('needpath', needpath)
            # needpath='"'+result[0]+'"'
    except:
        logger.exception('this is an exception message')

    if not os.path.exists(needpath):
        if os.path.exists('C:\Program Files (x86)'):
            pass
            # os.walk()

def openweb(url):
    needpath = get_val('needpath')
    # command="\""+needpath+"\"" +" "+url  #需要加个空格
    # path=r'C:\Program Files (x86)\Internet Explorer\iexplore.exe www.baidu.com'
    subprocess.Popen([needpath, url])
    # wx.Execute


def openIE(url):
    needpath = get_val('needpath')
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


class Getip_dianxinThread(Thread):
    def __init__(self, ip):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.ip = ip
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        getip_dianxin(self.ip)


class GetremotetimeThread(Thread):
    def __init__(self, *args, **kwargs):
        super(GetremotetimeThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)  # 启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        from component.remote_control import web_request
        try:
            remotetime_url = get_val('remotetime_url')
            result = web_request(remotetime_url)
            remotetime = result['currenttime']
            print("获取成功")
            set_val('a_time', remotetime + 0.1)  # 补网络延迟
        except:
            print("获取成功")
            logger.exception('this is an exception message')


## 设置一个截屏取价  和查看时间
##
class LowestpfriceThread(Thread):
    def __init__(self, *args, **kwargs):
        super(LowestpfriceThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.setDaemon(True)
        self.start()

    def run(self):
        for i in range(10000000):
            time.sleep(0.035)
            lowest_price = get_val('lowest_price')
            pricelist = get_val('pricelist')
            a_time = get_val('a_time')
            try:
                price = int(Price_read())  # 获取当前最低价
                if price in pricelist:  # 字典查找
                    set_val('findpos_on', False)
                    if lowest_price == price:
                        trans_time()  # 保存价格
                    else:
                        set_val('lowest_price', price)
                        trans_time()  # 保存价格

                        set_val('changetime', a_time)
                else:
                    set_val('findpos_on', True)
            except:
                set_val('findpos_on', True)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False


###软件启动后后台初始化，加速软件启动
class Start_thread(Thread):
    def __init__(self, *args, **kwargs):
        super(Start_thread, self).__init__(*args, **kwargs)
        self.setDaemon(True)
        self.start()

    def run(self):
        import logging, time
        version = '5.2'
        timenow = time.time()
        # 转换成localtime
        time_local = time.localtime(timenow)
        # 转换成新的时间格式(2016-05-09 18:59:20)
        myapplog = 'mylog'
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='%s.log' % myapplog,
                            filemode='w')

        root = logging.getLogger()
        print(root.name, type(root), root.parent, id(root))

        ## getwebpath()  # 初始化浏览器地址
        # 图片打开提速
        # yanzhengma_img = Image.open("yanzhengma.png")  # 打开图片的全局变量 ,提升第一次打开的速度
        # set_val('yanzhengma_img', yanzhengma_img)
        # 变量初始化
        from component.variable import Create_hash, init_val
        Create_hash()
        init_val()
        set_val('version', version)
        ###获取路径+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
        path = get_val('path')
        iconpath = path + 'logo.ico'  # 图标路径
        set_val('mainicon', iconpath)
        #获取默认浏览器位置
        getwebpath()

