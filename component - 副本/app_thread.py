# encoding: utf-8
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

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.

        # wx.Sleep(15)
        # TopFrame.Refresh_hash()
        ####################修改打开的IE版本
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION", 0,
                             winreg.KEY_ALL_ACCESS)

        # key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
        #                       r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION", 0,
        #                       _winreg.KEY_ALL_ACCESS)
        #
        # key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
        #                      r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_ENABLE_SCRIPT_PASTE_URLACTION_IF_PROMPT", 0,
        #                      winreg.KEY_ALL_ACCESS)
        try:
            # 设置注册表python.exe 值为 11000(IE11)
            name = os.path.realpath(sys.argv[0])  # 获取运行路径
            name = name.split('\\')[-1]
            winreg.SetValueEx(key, '%s'%name, 0, winreg.REG_DWORD, 0x00002710)    #10:2710  8:1f40
            # winreg.SetValueEx(key2, '%s'%name, 0, winreg.REG_DWORD, 0x00000001)
        except:
            # 设置出现错误
            print('error in set value!')

        # 用完取消注册表设置
        # winreg.DeleteValue(key, 'python.exe')
        # 关闭打开的注册表
        # winreg.CloseKey(key)


# 创建一个确认进程
#!--<script src="{{bootstrap_find_resource('jquery.js', cdn='jquery')}}"></script>-->
class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        for i in range(1000000):
            global findpos_on
            # print(findpos_on,"findpos_on")
            if findpos_on:
                findpos()
                # try:
                #     print("找着呢")
                #     findpos()  # 定位
                #     time.sleep(0.1)  # 0.1秒间隔
                # except:
                #     logging.error("findposthread error")
                #     print("findposthread error")


# 创建一个确认进程
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
            global tijiao_num
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


# class confirmThread(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.setDaemon(True)
#         self.start()
#
#     def run(self):
#         global confirm_need, confirm_on
#         global confirm_need, confirm_on ,confirm_one,chujia_on
#         for i in range(100):
#             wx.Sleep(0.1)
#             if confirm_need:
#                 findconfirm()
#                 if confirm_on:
#                     # TopFrame.OnClick_confirm()
#                     confirm_need=False
#                     confirm_on=False
#                     confirm_one=False
#                     chujia_on=True
#         confirm_one = False #进程结束的时候允许
# 创建一个刷新进程
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
        # for i in range(50):
        # print("查找刷新")
        # print(refresh_need)
        # if refresh_need:
        #     findrefresh()
        # if refresh_on:
        #     TopFrame.OnClick_Shuaxin()  # 刷新验证码

        # refresh_one=False  #进程结束的时候允许
        # refresh_on = False  # 关闭点击刷新
        # refresh_need = False  # 关闭查找刷新

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False
###########
#截图线程
# 创建一个刷新进程
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
        # for i in range(50):
        # print("查找刷新")
        # print(refresh_need)
        # if refresh_need:
        #     findrefresh()
        # if refresh_on:
        #     TopFrame.OnClick_Shuaxin()  # 刷新验证码

        # refresh_one=False  #进程结束的时候允许
        # refresh_on = False  # 关闭点击刷新
        # refresh_need = False  # 关闭查找刷新

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False




# ----------------------------------------------------------------------
# 登录验证器
class LoginThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        # self.controlthread=controlThread()
        global Username,Password, login_result, version
        login_result = ConfirmUser(Username,Password,version)
        print(login_result)
        # logging.info("%s"%login_result)
        wx.CallAfter(pub.sendMessage, "connect")


###限定登录时间
class controlThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        wx.Sleep(10)
        wx.CallAfter(pub.sendMessage, "connect failure")


# 登录状态验证器
class KeepThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        for i in range(1000000):
            time.sleep(90)
            Keeplogin()


# ----------------------------------------------------------------------
# 自动出价触发器
# 国拍出价
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        global tijiao_delay, final_tijiao, strategy_price, lowest_price, own_price1, own_price2
        global moni_second, strategy_on, moni_on, tijiao_on, tijiao_OK, second_real_time1, second_real_time2
        global one_advance, second_advance, tijiao_num, tijiao_OK, chujia_on, tijiao_on, tijiao_one
        global a_time, one_real_time1 ,one_real_time2,guopai_on ,twice,one_delay,second_delay
        global one_diff,second_diff
        for i in range(10000000):
            time.sleep(0.05)  # 间隔0.1秒判断一次
            # print(tijiao_on,strategy_on,guopai_on)
            # print(a_time, final_tijiao)
            # 触发提交
            if tijiao_on and strategy_on and guopai_on and tijiao_OK:  # 判断是否需要提交,国拍开启状态方可触发
                # print(a_time,final_tijiao)
                if tijiao_num == 1 and a_time >= one_real_time2 and not tijiao_one:  # 判断是否满足条件
                    tijiao_on = False
                    SmartTijiao()  # 调用方法
                    tijiao_on = False
                    tijiao_one = True
                elif tijiao_num == 2 and a_time >= second_real_time2:  # 判断是否满足条件
                    tijiao_on = False
                    SmartTijiao()  # 调用方法
                    tijiao_on = False
                elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and a_time <= one_real_time2 - one_delay and not tijiao_one:  # 价格判断
                    tijiao_on = False
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
                    tijiao_one = True
                elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and a_time <= second_real_time2 - second_delay:  # 价格判断
                    tijiao_on = False
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
            # 触发出价
            if strategy_on and guopai_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                # print(a_time,final_tijiao)
                if tijiao_num == 1 and one_real_time1 <= a_time <= one_real_time1 + 0.6:  # 判断是否满足条件
                    OnClick_chujia()  # 调用出价
                    own_price1 = lowest_price + one_diff
                    tijiao_on = True  #
                elif tijiao_num == 2 and twice and second_real_time1 <= a_time:  # 判断是否满足条件
                    OnClick_chujia()  # 调用出价
                    own_price2 = lowest_price + second_diff
                    tijiao_on = True


# 模拟出价
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        global moni_second, strategy_on, moni_on, tijiao_on, own_price1, own_price2
        global tijiao_num, tijiao_OK, one_advance, second_advance, tijiao_one
        global one_time1,one_time2,second_time1,second_time2
        global lowest_price,chujia_on,twice
        global one_diff, second_diff
        for i in range(10000000):
            time.sleep(0.05)  # 间隔0.1秒判断一次

            if tijiao_on and strategy_on and moni_on and tijiao_OK:  # 判断是否需要提交，模拟开启方可触发
                # print(tijiao_on, strategy_on, moni_on, tijiao_OK)
                # print(tijiao_num,moni_second,one_time2,tijiao_one)
                # print(lowest_price, own_price1, own_price2)
                if tijiao_num == 1 and moni_second >= one_time2 and not tijiao_one:  # 判断是否满足条件
                    SmartTijiao()  # 调用方法
                    tijiao_on = False
                    tijiao_one = True  # 第一枪已开
                elif tijiao_num == 2 and moni_second >= second_time2 and twice:  # 判断是否满足条件
                    SmartTijiao()  # 调用方法
                    tijiao_on = False
                elif tijiao_num == 1 and lowest_price >= own_price1 - 300 - one_advance and not tijiao_one:  # 价格判断
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
                    tijiao_one = True  # 第一枪已开
                elif tijiao_num == 2 and lowest_price >= own_price2 - 300 - second_advance and twice:  # 价格判断
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    OnClick_Tijiao()  # 调用方法
            # 触发出价
            # print(strategy_on,moni_on)
            # print(strategy_on, moni_on, chujia_on)
            # print(twice, second_time1, moni_second)
            if strategy_on and moni_on and chujia_on:  # 判断是否需要出价,模拟开启方可触发
                if tijiao_num == 1 and one_time1 <= moni_second <= one_time1 + 0.6:  # 判断是否满足条件
                    OnClick_chujia()  # 调用方法
                    print("第一次")
                    own_price1 = lowest_price + one_diff
                    tijiao_on = True
                elif tijiao_num == 2 and twice and second_time1 < moni_second:
                    OnClick_chujia()  # 调用方法
                    print("第二次")
                    own_price2 = lowest_price + second_diff
                    tijiao_on = True
