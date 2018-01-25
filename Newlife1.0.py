# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
####################
# 参数
# id Topframe 1    Operationframe 2  guopaiweb 3 controlframe 4
# 无确认
# 新增验证码放大器功能
# 时间同步
import logging,time
timenow = time.time()
# 转换成localtime
time_local = time.localtime(timenow)
# 转换成新的时间格式(2016-05-09 18:59:20)
myapplog = time.strftime("%Y%m%d%H%M%S", time_local)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%s.log' % myapplog,
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
# ----------------------------------------------------------------
# 导入模块#####################
import sys

if sys.platform != 'win32':
    exit()
import pyautogui as pg
import ctypes
from ctypes import wintypes
import wx.html2
import wx
import pickle
import wx.adv
from PIL import Image

# --------------------------------------------------------------------------------
##########生成日志文件##########

# --------------------------------------------------------------------------------
# 鼠标点击
import win32gui, win32api
import cv2
from PIL import ImageGrab
import win32clipboard

from component.staticmethod import Click,Click2,Paste_moni,Paste,setText,Delete
from component.imgcut import cut_pic,new_screenshot,new_screenshot_getimg,readpic,timeset
from component.imgcut import findpos, findrefresh, find_yan_confirm, findconfirm, cut_img
from component.imgcut import new_screenshot, new_screenshot_getimg


from component.staticmethod import Click,Click2,Delete,setText

from component.staticmethod import Paste,Paste_moni

from component.app_thread import cutimgThread,findposThread,HashThread
from component.app_thread import confirmThread,refreshThread,TijiaoThread,MoniTijiaoThread
from component.app_thread import LoginThread
from component.variable import set_val,get_val

##############
# 图片打开提速
yimg = ImageGrab.grab().save("yanzhengma.png")
yanzhengma_img = Image.open("yanzhengma.png")  # 打开图片的全局变量 ,提升第一次打开的速度
set_val('yanzhengma_img',yanzhengma_img)


# 模拟键盘输入
# 对应码`

# ------------------------------------------------------------------------------------
###全新的载图  ScreenShot

import win32con
import time

# --------------------------------------------------------------------------------
# PING网速测试
# import os
# import socket
# import struct
# import select
# import time

# ICMP_ECHO_REQUEST = 8  # Platform specific
# DEFAULT_TIMEOUT = 2
# DEFAULT_COUNT = 1
#
#
# class Pinger(object):
#     """ Pings to a host -- the Pythonic way"""
#
#     def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
#         self.target_host = target_host
#         self.count = count
#         self.timeout = timeout
#
#
#     def do_checksum(self, source_string):
#         """  Verify the packet integritity """
#         sum = 0
#         max_count = (len(source_string) / 2) * 2
#         count = 0
#         while count < max_count:  # 分割数据每两比特(16bit)为一组
#             val = source_string[count + 1]* 256 + source_string[count]
#             sum = sum + val
#             sum = sum & 0xffffffff
#             count = count + 2
#
#         if max_count < len(source_string):   # 如果数据长度为基数,则将最后一位单独相加
#             sum = sum + source_string[len(source_string) - 1]
#             sum = sum & 0xffffffff
#         sum = (sum >> 16) + (sum & 0xffff)  # 将高16位与低16位相加直到高16位为0
#         sum = sum + (sum >> 16)
#         answer = ~sum
#         answer = answer & 0xffff
#         answer = answer >> 8 | (answer << 8 & 0xff00)
#         return answer  # 返回的是十进制整数
#
#     def receive_ping(self, sock, ID, timeout):
#         time_remaining = timeout
#         while True:
#             start_time = time.time()
#             readable = select.select([sock], [], [], time_remaining)
#             time_spent = (time.time() - start_time)
#             if readable[0] == []:  # Timeout
#                 return
#
#             time_received = time.time()
#             recv_packet, addr = sock.recvfrom(1024)
#             icmp_header = recv_packet[20:28]
#             type, code, checksum, packet_ID, sequence = struct.unpack(
#                 "bbHHh", icmp_header
#             )
#             if packet_ID == ID:
#                 bytes_In_double = struct.calcsize("d")
#                 time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
#                 return time_received - time_sent
#
#             time_remaining = time_remaining - time_spent
#             if time_remaining <= 0:
#                 return
#
#     def send_ping(self, sock, ID):
#         """
#         Send ping to the target host
#         """
#         target_addr = socket.gethostbyname(self.target_host)
#
#         my_checksum = 0
#
#         # Create a dummy heder with a 0 checksum.
#         header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
#         bytes_In_double = struct.calcsize("d")
#         data = (192 - bytes_In_double) * "Q"
#         data = struct.pack("d", time.time()) + bytes(data,encoding="utf-8")
#
#         # Get the checksum on the data and the dummy header.
#         my_checksum = self.do_checksum(header + data)
#         header = struct.pack(
#             "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
#         )
#         packet = header + data
#         sock.sendto(packet, (target_addr, 1))
#
#     def ping_once(self):
#         """
#         Returns the delay (in seconds) or none on timeout.
#         """
#         icmp = socket.getprotobyname("icmp")
#         try:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
#         except socket.error as er:
#             if er[0] == 1:
#                 # Not superuser, so operation not permitted
#                 er[1] += "ICMP messages can only be sent from root user processes"
#                 raise socket.error(er[1])
#         except Exception as e:
#             print ("Exception: %s" % (e))
#
#
#         my_ID = os.getpid() & 0xFFFF
#
#         self.send_ping(sock, my_ID)
#         delay = self.receive_ping(sock, my_ID, self.timeout)
#         sock.close()
#         return delay
#
#     def ping(self):
#         """
#         Run the ping process
#         """
#         for i in range(self.count):
#             # print("Ping to %s..." % self.target_host)
#             try:
#                 delay = self.ping_once()
#             except socket.gaierror as e:
#                 # print ("Ping failed. (socket error: '%s')" % e)
#                 return "timeout"
#
#             if delay == None:
#                 # print("Ping failed. (timeout within %ssec.)" % self.timeout)
#                 return "timeout"
#
#             else:
#                 delay = delay * 1000
#                 # print("Get ping in %0.4fms" % delay)
#                 return int(delay)
# #定义网速查询的类
# pinger=Pinger(url2)

# ---------------------------------------------------------------------------------
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
        pass
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

from component.login import ConfirmUser,Logout,Keeplogin,send_mail
# --------------------------------------------------------------------------------
# 采集用户信息
import smtplib
# import time
# import codecs
from email.mime.text import MIMEText
import os
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
# --------------------------------------------------------------------------------
# 进程管理
from threading import Thread
import threading
from wx.lib.pubsub import pub  # 代替了publisher
# --------------------------------------------------------------------------------

####验证登录
####记录一个全局变量Username
import socket, sys, json

timeout = 10
socket.setdefaulttimeout(timeout)  # 设定截止时间

from urllib import request
import json

# --------------------------------------------------------------------------------
# 计算机视觉
def Com_read():
    pass


# --------------------------------------------------------------------------------
# 自动操作
def Com_decision():
    pass


# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# #调整时间
# import socket
# import struct
# import time
# import win32api
# TimeServer = '210.72.145.39'  # 国家授时中心ip
# Port = 123
# def Adjust_time():
#     pass
# def getTime():
#     TIME_1970 = 2208988800
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     data = '\x1b' + 47 * '\0'
#     data=bytes(data, encoding="utf-8")
#     client.sendto(data, (TimeServer, Port))
#     data, address = client.recvfrom(1024)
#     data_result = struct.unpack('!12I', data)[10]
#     data_result -= TIME_1970
#     return data_result
#
#
# def setSystemTime():
#     tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(getTime())
#     win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0)
#     print ("Set System OK!")


# ----------------------------------------------------------------------
from component.WebFrame import WebFrame
from component.GuopaiFrame import GuopaiFrame
from component.OperationFrame import OperationFrame
mainicon = get_val('mainicon')
dick_target = get_val('dick_target')






# ----------------------------------------------------------------------
class PosFrame(wx.Frame):
    def __init__(self, pos, pos_name):
        x, y = pos
        wx.Frame.__init__(self, None, -1, 'POS',
                          pos=(x - 20, y - 10), size=(30, 20), style=wx.FRAME_TOOL_WINDOW)
        panel = wx.Panel(self, -1, size=(30, 20))
        # 这是一个基本的静态文本
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        t1 = []
        t1.append(wx.StaticText(panel, -1, pos_name,
                                (0, 0)))
        for i in range(len(t1)):
            t1[i].SetFont(font)


class PriceFrame(wx.Frame):
    def __init__(self, image, size, pos):
        wx.Frame.__init__(self, None, -1, 'Price', size=size, pos=pos,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        self.panel = wx.Panel(self, size=size)
        # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        self.bmp = wx.StaticBitmap(self.panel, -1, wx.Bitmap(image))



class AdFrame(wx.Frame):
    def __init__(self):  ##########版本号
        wx.Frame.__init__(self, None, -1, "广告",
                          pos=(0, 250), size=(250, 200), style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        panel = wx.Panel(self, -1, size=(250, 200))
        # 这是一个基本的静态文本
        font = wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL)
        t1 = []
        t1.append(wx.StaticText(panel, -1, " 专业代拍软件",
                                (15, 10)))
        t1.append(wx.StaticText(panel, -1, " 专业代拍团队",
                                (15, 60)))
        t1.append(wx.StaticText(panel, -1, "关注微信公众号",
                                (15, 110)))
        t1.append(wx.StaticText(panel, -1, " 小鲜肉拍牌",
                                (15, 160)))
        for i in range(len(t1)):
            t1[i].SetFont(font)





# 控制小窗
class ControlFrame(wx.Frame):  # 为webframe提供控制操作
    def __init__(self):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 4, size=(330, 200), style=wx.NO_BORDER | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR, \
                          pos=(Px + 40, Py + 480), name="control")
        self.panel = wx.Panel(self, -1, size=(330, 270))
        # self.button1=wx.Button(self.panel,pos=(0,0),size=(50,25),label="关闭")
        # self.Bind(wx.EVT_BUTTON, self.o_closeweb, self.button1)
        font1 = wx.Font(25, wx.SWISS, wx.NORMAL, wx.NORMAL)
        font2 = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.adtext = wx.StaticText(self.panel, label=u"沪牌一号", pos=(90, 20))
        self.adtext.SetFont(font1)
        self.pricetext = wx.StaticText(self.panel, label=u"最低成交价:", pos=(50, 90))
        self.pricetext.SetFont(font2)
        self.price = wx.StaticText(self.panel, pos=(190, 90))
        self.price.SetFont(font2)
        self.timetext = wx.StaticText(self.panel, label=u"当前时间:", pos=(50, 130))
        self.timetext.SetFont(font2)
        self.time = wx.StaticText(self.panel, pos=(190, 130))
        self.time.SetFont(font2)

        self.netstattext = wx.StaticText(self.panel, pos=(80, 170), label=u"网速")
        self.netstattext.SetFont(font2)
        self.netstat = wx.StaticText(self.panel, pos=(190, 170))

        # dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        # 定时器
        self.timetimer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Timego, self.timetimer1)
        self.timetimer1.Start(100)

    def o_closeweb(self, event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()

    def Timego(self, event):
        global lowest_price, moni_second, a_time
        self.price.SetLabel("%s" % lowest_price)
        if moni_on:
            self.time.SetLabel("11:29:%s" % int(moni_second))
        else:
            timestr1 = time.localtime(a_time)
            timestr2 = time.strftime("%H:%M:%S", timestr1)
            self.time.SetLabel(timestr2)
        global pinger
        pingnow = pinger.ping()
        if pingnow == "timeout":
            self.netstat.SetLabel("%s" % pingnow)
        else:
            self.netstat.SetLabel("%sms" % pingnow)





#################最低成交价显示##################
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(100)  # 设定时间间隔

    def Draw(self, dc):  # 绘制当前时间
        global lowest_price
        st = str(lowest_price)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):  # 更新
        global lowest_price
        st = str(lowest_price)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def OnTimer(self, evt):  # 显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        self.Modify(dc)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)  # 用于重绘事件
        self.Draw(dc)


class LowestpriceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=lowestpriceframe_pos,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        # wx.Frame.__init__(self, None, -1,'Time',size=(400,160), pos=Pos_timeframe,
        #                   style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        LowestpriceWindow(self)


# --------------------------------------------------------------
# # 策略窗口
# class OperationFrame():
#     def __init__(self, px, py, ad, name):  # name:窗口显示名称
#         wx.Frame.__init__(self, None, -1, size=(300, websize[1]), \
#                           pos=(px, py), style=wx.SIMPLE_BORDER)
#         self.hbox1=wx.BoxSizer()
#         self.hbox2=wx.BoxSizer()
#         self.hbox3=wx.BoxSizer()
#
#         self.lable


# --------------------------------------------------------------
########初始登录窗口########
import string
import wx.lib.agw.hyperlink as hyperlink


class LoginFrame(wx.Frame):
    def __init__(self, name, user, psd):  ##########版本号
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # self.panel.SetBackgroundColour((0,188, 255))
        # self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        # # 设置字体
        # font_button = wx.Font(10, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        # font2 = wx.Font(15, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        # font3 = wx.Font(25, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
        # font_userlabel = wx.Font(15, wx.TELETYPE, wx.NORMAL, wx.NORMAL)

        # 主sizer
        self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.welcomelabel = wx.StaticText(self.panel, -1, label="请输入用户名和密码", style=wx.ALIGN_CENTER)
        self.sizer_v1.Add(self.welcomelabel, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # self.btnSizer = wx.StdDialogButtonSizer()
        self.userbox = wx.BoxSizer(wx.HORIZONTAL)
        self.userlabel = wx.StaticText(self.panel, -1, label="账号")
        self.userText = wx.TextCtrl(self.panel, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        self.userbox.Add(self.userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.userbox.Add(self.userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self.passbox = wx.BoxSizer(wx.HORIZONTAL)
        self.passlabel = wx.StaticText(self.panel, -1, label="密码")
        self.passText = wx.TextCtrl(self.panel, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
        self.passbox.Add(self.passlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.passbox.Add(self.passText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        if user:
            self.userText.SetValue(user)
        if psd:
            self.passText.SetValue(psd)
        self.sizer_v1.Add(self.userbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.sizer_v1.Add(self.passbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.userText)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.passText)

        self.monibtn = wx.Button(self.panel, -1, label="模拟", size=(90, 30))
        self.loginbtn = wx.Button(self.panel, -1, label="登录", size=(90, 30))
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.btnSizer.Add(self.loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.sizer_v1.Add(self.btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin, self.loginbtn)

        self.purchaselink = hyperlink.HyperLinkCtrl(self.panel, -1, u"购买账号")
        self.purchaselink.UnsetToolTip()
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.Purchase)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()

        self.helplink = hyperlink.HyperLinkCtrl(self.panel, -1, u"查看帮助")
        self.helplink.UnsetToolTip()
        self.helplink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.Purchase)
        self.helplink.AutoBrowse(False)
        self.helplink.EnableRollover(True)
        self.helplink.SetUnderlines(False, False, True)
        self.helplink.OpenInSameWindow(True)
        self.helplink.UpdateLink()

        self.linkbox = wx.BoxSizer(wx.HORIZONTAL)
        self.linkbox.Add(self.purchaselink, flag=wx.ALIGN_LEFT | wx.RIGHT, border=20)
        self.linkbox.Add(self.helplink, flag=wx.ALIGN_RIGHT | wx.LEFT, border=20)
        self.sizer_v1.Add(self.linkbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        self.SetSizer(self.sizer_v1)
        self.Center()  # 初始化居中

        pub.subscribe(self.connect_success, "connect")
        # pub.subscribe(self.connect_failure, "connect failure")

        self.hashthread = HashThread()

    def connect_success(self):
        self.loginbtn.Enable()
        global login_result, url2, url3  # dick对象

        if login_result['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)

            ##这里作为测试用
            if Username == 'helong' or Username == 'yuanjunkai' or Username == 'zs':
                url2 = 'http://moni.51hupai.org/'
            else:
                url2 = login_result['url_dianxin']
            url3 = login_result['url_nodianxin']
            # event.Skip()
        elif login_result['result'] == 'net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'wrong password':
            wx.MessageBox('密码错误', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('登录失败', '用户登录', wx.OK | wx.ICON_ERROR)

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("blue.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def OnClose(self, event):
        event.Skip()
        sys.exit(None)

    # def connect_failure(self):
    #     self.loginBtn.Enable()
    #     # self.loginthread.terminate()
    #     wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)

    def OnLogin(self, event):
        global Username, Password
        username = self.userText.GetValue()
        password = self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
            # loginthread=TestThread()
        else:
            Username = username  # 保存用户输入的账号密码
            Password = password
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            # self.loginBtn.setlabel(u"登录中")
            event.GetEventObject().Disable()

    def Purchase(self, event):
        print("购买")


class UserValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''

    # ----------------------------------------------------------------------
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    # ----------------------------------------------------------------------
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)

    # ----------------------------------------------------------------------
    def Validate(self, win):
        return True

    # ----------------------------------------------------------------------
    def TransferToWindow(self):
        return True

    # ----------------------------------------------------------------------
    def TransferFromWindow(self):
        return True

    # ----------------------------------------------------------------------
    def OnChar(self, event):
        pass
        # keycode = int(event.GetKeyCode())
        # if keycode < 256:
        #     #print keycode
        #     key = chr(keycode)
        #     #print key
        #     if key not in string.ascii_letters and key not in string.digits:
        #         return
        #     # if self.flag == 'no-alpha' and key in string.ascii_letters:
        #     #     return
        #     # if self.flag == 'no-digit' and key in string.digits:
        #     #     return
        # event.Skip()


class PassValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''

    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)

    # ----------------------------------------------------------------------
    def Clone(self):
        '''Required Validator method'''
        return PassValidator()

    # ----------------------------------------------------------------------
    def Validate(self, win):
        return True

    # ----------------------------------------------------------------------
    def TransferToWindow(self):
        return True

    # ----------------------------------------------------------------------
    def TransferFromWindow(self):
        return True

    # ----------------------------------------------------------------------
    def OnChar(self, event):
        pass
        # keycode = int(event.GetKeyCode())
        # if keycode < 256:
        #     # print keycode
        #     key = chr(keycode)
        #     # print key
        #     # if key in string.digits or key in string.ascii_letters:
        #     #     return
        #     if key not in string.digits and key not in string.ascii_letters:
        #         return
        # event.Skip()


########确认登录窗口########
class ConfirmLogin(wx.Frame):
    pass


# ----------------------------------------------------------------------
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
        global a_time, moni_second
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            a_time += b - a  # 实际运行时间作为真实间隔
            moni_second += b - a
            if moni_second >= 60:
                moni_second = 0
            # a=time.clock()
            # time.sleep(0.2)
            # a_time+=0.2
            # b=time.clock()
            # print(b-a)

            # for i in range(1000000):
            # time.sleep(0.2)
            # a_time+=0.2


#     def run(self):
#         """Run Worker Thread."""
#         # This is the code executing in the new thread.
#         global timer
#         timer = threading.Timer(0.2, runtime)
#         timer.start()
#
#     def stop(self):
#         sys.exit(None)
#
# def runtime():
#     global a_time,timer
#     a_time+=0.2
#
#     timer=threading.Timer(0.2,runtime)
#     timer.start()

# ---------------------------------------
# 创建hash进程，初始化
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



class SketchApp(wx.App):
    def OnInit(self):
        # try:
        #     bitmap = wx.Bitmap('start.png', wx.BITMAP_TYPE_PNG)
        #
        #     wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
        #                                  1500, None, -1, wx.DefaultPosition, size=(300,240),
        #                                 style=wx.BORDER_SIMPLE | wx.STAY_ON_TOP)
        #
        #     wx.Yield()
        # except:
        #     pass
        try:
            with open("your.name", 'rb') as name:
                namepsd = pickle.load(name)
                user = namepsd[0]
                psd = namepsd[1]
        except:
            user = '123456'  # 关闭
            user = '123456'  # 关闭
            psd = 0
        loginframe = LoginFrame('小鲜肉拍牌', user, psd)
        loginframe.Show(True)
        return True


if __name__ == '__main__':
    getwebpath()  # 初始化浏览器地址

    app = SketchApp()
    # 打开刷新与确认进程
    confirmthread = confirmThread()  #确认线程
    refreshthread = refreshThread()  #刷新线程
    finposthread = findposThread()   #定位线程
    cutimgthread = cutimgThread()   #截图线程
    app.MainLoop()

# self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
