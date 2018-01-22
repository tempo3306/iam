# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
####################
#参数
#id Topframe 1    Operationframe 2  guopaiweb 3 moniweb 4

version='1.6'
num=0
avt=0
############全局变量参数表##96.22#######
host_ali="121.196.220.94"
# host_ali="127.0.0.1"
#网址
url1="http://moni.51hupai.org/"
url2="www.baidu.com"
#icon路径
mainicon='ico.ico'

# global全局变量，操作控制
view=False  # 定位显示
do=False  # 开启辅助
ad_view=False  # 显示广告

price_view=False #显示价格,控制截图
price_on=False   #价格是否显示
price_count=0    #辅助计时，正确显示价格
web_on=False     #监测web是否开启
#时间
view_time=False #时间框是否开启
operation_show=False  #策略框是否开启
time_on=False  #操作面板上是否开启时间
import time
a_time = time.time()  #国拍初始时间
b_time=0              #制作0.1秒

moni_minute=29
moni_second=0

chujia_time=0         #出价时间

Username=0             #用户名
Password=0          #密码


moni_on=False             #判断开启的是哪个窗口 ，限制同时只能开启一个
guopai_on=False


strategy1=53           #策略整数时间
strategy2=0.0          #策略小数时间

# tijiao_delay=0         #策略提交延时
# final_tijiao=1000000000 #最终提交时间


strategy_on=True      #策略是否开启
strategy_repeat=False  #判断是否重复，避免重复进程
# guopai_tijiao=False #国拍提交次数

delay=False   #是否延迟
delay_time=0.5 #延迟大小设置

login_result=False #登录成功与否


findpos_on=True  #控制是否找位置

pricelist=[80000+i*100  for i in range(200)]   #用于验证识别
IDnumber=0  #身份证号
account=0   #标书号
passwd=0    #密码


######################################################
import pyautogui as pg
#初始化hash字典
def Create_hash():
    with open('dick.dl','rb') as dick:
        global dick_hash
        dick_hash=pickle.load(dick)  #读取得到dick_hash
    with open('cf.btn','rb') as cf:
        global cf_hash
        cf_hash=pickle.load(cf)   #read confirm and refresh

    with open("target.tkl",'rb')  as tar:
        global dick_target
        dick_target=pickle.load(tar)  # 要寻找对象的对象


#######################################
#策略相关参数
one_time1=48 #第一次出价加价
one_time2=55 #第一次出价提交
one_real_time1=1000000000000 #换算之后的出价时间
one_real_time2=1000000000000 #换算之后的提交时间
one_diff=700 #第一次加价幅度
one_delay=0.5 #第一次延迟
one_advance=100 #第一次提交提前量


second_time1=48 #第二次次出价加价
second_time2=55 #第二次出价提交
second_real_time1=1000000000000 #换算之后的出价时间
second_real_time2=1000000000000 #换算之后的提交时间
second_diff=600 #第二次加价幅度
second_delay=0.5 #第二次出价延迟
second_advance=100 #第二次出价提交提前量

osl = [0] * 15  #策略容器初始化   判定+10参数+确认选项

chujia_on=True  #完成一次出价之后关闭，完成出价后关闭
tijiao_on=False  #是否需要提交,完成提交后打开


lowest_price=86000 #最低成交价
own_price1=0 #第一次出价
own_price2=0 #第二次出价
own_price=0 #当前出价

tijiao_OK=False #表示输完验证码
e_on=True #表示s激活tijiao_OK
enter_on=False #表示回车激活tijiao_Ok

twice=False #开启两次出价
tijiao_num=1    #开启二次出价，设置为2，执行一次之后，减1
tijiao_one=False #第一次出价之后开闭
#---------------------------------------------------------------
#计算浏览器位置，左上角s
websize=[902,700]   #浏览器大小
Pxy = pg.size()  # 分辨率
Px1 = Pxy[0] / 2 #屏幕中心位置
Py2 = Pxy[1] / 2
Px=(Pxy[0]-websize[0])/2-80
Py=(Pxy[1]-websize[1])/2
#创建位置数据
#0:加价  1：出价 2：提交  3：刷新   4 ：确认   5：验证码    6:验证码输入框     7：取消
P_relative=[[343, -66], [346, 40], [96, 121], [92, 43], [201, 100],[281, 40],[261,37],[282,118]]  #各按钮相对于WEB位置
P_relative2=[[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
Position=[[0,0] for i in range(len(P_relative))]
for i in range(len(Position)):
    Position[i][0] = Px1 + P_relative[i][0]
    Position[i][1] = Py2 + P_relative[i][1]
#转换为基于浏览器左上角坐标相对位置
#按钮微调幅度--为国拍调整位置做准备
px_ajust,py_ajust=0,0
for i in range(len(P_relative)):
    P_relative[i][0]+=websize[0]/2+px_ajust
    P_relative[i][1]+=websize[1]/2+py_ajust  #微调
#price位置
px_price=770-171
py_price=260
#price框放置位置
px_priceframe=220-191
py_priceframe=480
#time放置位置
px_timeframe=245
py_timeframe=350 #460
#最低成交价框显示位置
px_lowestpriceframe=245
py_lowestpriceframe=290
lowestpriceframe_pos=[px_lowestpriceframe,py_lowestpriceframe]

#验证码位置
px_yanzhengmaframe=400-215
py_yanzhengmaframe=460


#出价截取大小
px_mini=200
py_mini=40
#价格框大小
Pricesize=[400,80]
#时间框大小
Timesize=[200,50]

#刷新、确认所在区域  [396, 11], [505, 68]   价格387    440  325    412  375    431
lowestprice_area=[179-80+Px,424-50+Py,179+80+Px,424+50+Py]
refresh_area=[396-150,11-100,396+150,11+100]
confirm_area=[505-80,68-50,505+80,68+50]


#-------------------------------------------------------------------
######################
#自动计算位置
# try:
#     log=open('pos.log',"rb")
#     Position=pickle.load(log)
# except:
#     x0,y0=pg.size()
#     Position=[[1026, 318], [1029, 427], [779, 505], [775, 427], [884, 484],[964, 421]]
#     P_relative=[(343, -66), (346, 40), (96, 121), (92, 43), (201, 100),(281, 40)]


# [[853, 317], [596, 503], [775, 424], [775, 427], [884, 484]]
#[(342, -63), (344, 39), (91, 124), (109, 37), (202, 106)]

#计算price位置
Px_price=Px+px_price
Py_price=Py+py_price
Pos_price=[Px_price,Py_price,Px_price+px_mini,Py_price+py_mini]  #所出价格截图位置BOX

#计算price框放置位置
Px_priceframe=Px+px_priceframe
Py_priceframe=Py+py_priceframe
Pos_priceframe=[Px_priceframe,Py_priceframe]

#计算time放置位置
Px_timeframe=px_timeframe
Py_timeframe=py_timeframe
Pos_timeframe=[Px_timeframe,Py_timeframe]

#计算验证码位置
Px_yanzhengmaframe=Px+px_yanzhengmaframe
Py_yanzhengmaframe=Py+py_yanzhengmaframe
Pos_yanzhengmaframe=[Px_yanzhengmaframe,Py_yanzhengmaframe]

###########################
#提供所需截图位置
#计算最低成交价位置
#最低成交价位置，大小
# px_lowestprice=159    #206   209 208 #截图相对位置
# py_lowestprice=416   #412  416
px_lowestprice=0    #206   209 208 #截图相对位置
py_lowestprice=0   #412  416


Px_lowestprice=Px+px_lowestprice
Py_lowestprice=Py+py_lowestprice
lowestprice_sizex=41 #截图范围 41
lowestprice_sizey=16

px_relative=49  #查找出来位置反算相对位置
py_relative=0
#计算确认键位置
px_confirm=656
py_confirm=475
Px_confirm=Px+px_confirm
Py_confirm=Py+py_confirm
confirm_sizex=113
confirm_sizey=28
confirm_on=False #是否需要确认
confirm_need=False #启动确认识别
confirm_one=False #限制只产生一次进程
#计算刷新位置
px_refresh=550
py_refresh=413
Px_refresh=Px+px_refresh
Py_refresh=Py+py_refresh
refresh_sizex=108
refresh_sizey=21
refresh_on=False #是否需要刷新
refresh_need=False #启动刷新识别
refresh_one=False #限制只产生一次进程

chujia_interval=False #出价间隔
tijiao_interval=False #提交间隔
query_interval=False #间隔
query_on=False #是否处于查询状态
#----------------------------------------------------------------
#导入模块#####################
import sys
if sys.platform != 'win32':
    exit()
import pyautogui as pg
import ctypes
from ctypes import wintypes
import win32con
import wx.html2
import wx
import pickle
import wx.adv
from PIL import Image
import imagehash

# #创建替代算法
# def _binary_array_to_hex(arr):
# 	"""
# 	internal function to make a hex string out of a binary array.
#
# 	binary array might be created from comparison - for example, in
# 	average hash, each pixel in the image is compared with the average pixel value.
# 	If the pixel's value is less than the average it gets a 0 and if it's more it gets a 1.
# 	Then we treat this like a string of bits and convert it to hexadecimal.
# 	"""
# 	h = 0
# 	s = []
# 	for i, v in enumerate(arr.flatten()):
# 		if v:
# 			h += 2**(i % 8)
# 		if (i % 8) == 7:
# 			s.append(hex(h)[2:].rjust(2, '0'))
# 			h = 0
# 	return "".join(s)
#
#
# class ImageHash(object):
# 	"""
# 	Hash encapsulation. Can be used for dictionary keys and comparisons.
# 	"""
# 	def __init__(self, binary_array):
# 		self.hash = binary_array
#
# 	def __str__(self):
# 		return _binary_array_to_hex(self.hash.flatten())
#
# 	def __repr__(self):
# 		return repr(self.hash)
#
# 	def __sub__(self, other):
# 		if other is None:
# 			raise TypeError('Other hash must not be None.')
# 		if self.hash.size != other.hash.size:
# 			raise TypeError('ImageHashes must be of the same shape.', self.hash.shape, other.hash.shape)
# 		return numpy.count_nonzero(self.hash != other.hash)
#
# 	def __eq__(self, other):
# 		if other is None:
# 			return False
# 		return numpy.array_equal(self.hash.flatten(), other.hash.flatten())
#
# 	def __ne__(self, other):
# 		if other is None:
# 			return False
# 		return not numpy.array_equal(self.hash.flatten(), other.hash.flatten())
#
# 	def __hash__(self):
# 		# this returns a 8 bit integer, intentionally shortening the information
# 		return sum([2**(i % 8) for i, v in enumerate(self.hash.flatten()) if v])
# #
#
# def dhash(image, hash_size=8):
#     """
#     Difference Hash computation.
#
#     following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html
#
#     computes differences horizontally
#
#     @image must be a PIL instance.
#     """
#     # resize(w, h), but numpy.array((h, w))
#     image = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
#     pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size, hash_size + 1))
#     # compute differences between columns
#     diff = pixels[:, 1:] > pixels[:, :-1]
#     return ImageHash(diff)


# --------------------------------------------------------------------------------
##########生成日志文件##########
import logging
timenow=time.time()
#转换成localtime
time_local = time.localtime(timenow)
#转换成新的时间格式(2016-05-09 18:59:20)
myapplog = time.strftime("%Y%m%d%H%M%S",time_local)
print(myapplog)  #生成时间log名
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='%s.log'%myapplog,
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
#--------------------------------------------------------------------------------
#鼠标点击
import win32gui,win32api
import cv2
from PIL import ImageGrab

def Click(x, y):  # 鼠标点击
    a = win32gui.GetCursorPos()
    x=int(x)
    y=int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    # win32api.SetCursorPos(a)
def Click2(x, y):  # 鼠标点击
    a = win32gui.GetCursorPos()
    x=int(x)
    y=int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos(a)

#模拟键盘输入
#对应码
import win32clipboard
def Paste():  #ctrl + V
    win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
#操作粘贴板
def setText(aString):
    aString=aString.encode('utf-8')
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()

def Delete():
    win32api.keybd_event(0x08,0,0,0)
    win32api.keybd_event(0x08,0,win32con.KEYEVENTF_KEYUP, 0)


#查找位置
def findpos():
    # targetimg="target.png"
    sc = ImageGrab.grab().convert('L')
    img=np.asarray(sc)
    global dick_target
    template=dick_target[2]
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(min_val)
    # print(max_val)
    # print(min_loc)
    # print(max_loc)
    global px_lowestprice,py_lowestprice,px_relative,py_relative,Px_lowestprice,Py_lowestprice,Px,Py
    px_lowestprice = max_loc[0]+px_relative
    py_lowestprice = max_loc[1]+py_relative
    Px_lowestprice=px_lowestprice
    Py_lowestprice=py_lowestprice
    # print(px_lowestprice,py_lowestprice)
    global Position,refresh_area,confirm_area
    for i in range(len(Position)):
        Position[i][0] = Px_lowestprice + P_relative2[i][0]
        Position[i][1] = Py_lowestprice + P_relative2[i][1]
    refresh_area = [396 - 150+Px_lowestprice, 11 - 100+Py_lowestprice, 396 + 150+Px_lowestprice, 11 + 100+Py_lowestprice]
    confirm_area = [505 - 80+Px_lowestprice, 68 - 50+Py_lowestprice, 505 + 80+Px_lowestprice, 68 + 50+Py_lowestprice]
    #关闭触发
    global findpos_on
    findpos_on=False

def findrefresh():
    global dick_target,refresh_on,Position,refresh_area,confirm_area
    template=dick_target[0]
    sc = ImageGrab.grab(refresh_area).convert('L')
    # sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val>=0.6:
        refresh_on=True


def findconfirm():
    global dick_target,confirm_on,Position
    template=dick_target[1]
    sc = ImageGrab.grab(confirm_area).convert('L')
    img = np.asarray(sc)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val>=0.9:
        confirm_on=True

#------------------------------------------------------------------------------------
########图像识别###########
SZ=20
bin_n = 16 # Number of bins
import numpy as np

#hog特征
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


#二值化，切割
def cut(img):
    ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgn=[]
    xy=[]
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        # print(x, y, w, h)
        xy.append([x, y, w, h])

    xy = sorted(xy)
    for i in range(len(contours)):
        x, y, w, h = xy[i]
        imgn.append(image[y:y + h, x:x + w])
    return imgn

def readpic(img):
    try:
        svm=cv2.ml.SVM_load('maindata.xml')
        testData=cut(img)
        testData=list(map(hog,testData))
        testData = np.float32(testData).reshape(-1,64)
        result = svm.predict(testData)
        result=result[1].reshape(-1).astype(int).astype(str)
        price="".join(list(result))
        return price   #返回的是price str
    except:
        return False



# --------------------------------------------------------------------------------
#PING网速测试
import os
import socket
import struct
import select
import time

ICMP_ECHO_REQUEST = 8  # Platform specific
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 1


class Pinger(object):
    """ Pings to a host -- the Pythonic way"""

    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout


    def do_checksum(self, source_string):
        """  Verify the packet integritity """
        sum = 0
        max_count = (len(source_string) / 2) * 2
        count = 0
        while count < max_count:  # 分割数据每两比特(16bit)为一组
            val = source_string[count + 1]* 256 + source_string[count]
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2

        if max_count < len(source_string):   # 如果数据长度为基数,则将最后一位单独相加
            sum = sum + source_string[len(source_string) - 1]
            sum = sum & 0xffffffff
        sum = (sum >> 16) + (sum & 0xffff)  # 将高16位与低16位相加直到高16位为0
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer  # 返回的是十进制整数

    def receive_ping(self, sock, ID, timeout):
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []:  # Timeout
                return

            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
                "bbHHh", icmp_header
            )
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
                return time_received - time_sent

            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return

    def send_ping(self, sock, ID):
        """
        Send ping to the target host
        """
        target_addr = socket.gethostbyname(self.target_host)

        my_checksum = 0

        # Create a dummy heder with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d", time.time()) + bytes(data,encoding="utf-8")

        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))

    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        """
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error as er:
            if er[0] == 1:
                # Not superuser, so operation not permitted
                er[1] += "ICMP messages can only be sent from root user processes"
                raise socket.error(er[1])
        except Exception as e:
            print ("Exception: %s" % (e))


        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock, my_ID)
        delay = self.receive_ping(sock, my_ID, self.timeout)
        sock.close()
        return delay

    def ping(self):
        """
        Run the ping process
        """
        for i in range(self.count):
            # print("Ping to %s..." % self.target_host)
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                # print ("Ping failed. (socket error: '%s')" % e)
                return "timeout"

            if delay == None:
                # print("Ping failed. (timeout within %ssec.)" % self.timeout)
                return "timeout"

            else:
                delay = delay * 1000
                # print("Get ping in %0.4fms" % delay)
                return int(delay)
#定义网速查询的类
pinger=Pinger(url2)

#---------------------------------------------------------------------------------
#打开浏览器
import winreg,re
needpath='C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1='C:\Program Files (x86)'
path2='C:\Program Files'
def getwebpath():
    global needpath
    #查找注册表键值
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key,0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            needpath='"'+result[0]+'"'
    except:
        pass
    if not os.path.exists(needpath):
        if os.path.exists('C:\Program Files (x86)'):
            pass
            # os.walk()
def openweb(url):
    command="\""+needpath+"\"" +" "+url  #需要加个空格
    os.system(command)
# --------------------------------------------------------------------------------
#采集用户信息
import smtplib
# import time
# import codecs
from email.mime.text import MIMEText
import os
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
#--------------------------------------------------------------------------------
#进程管理
from threading import Thread
import threading
from wx.lib.pubsub import pub   #代替了publisher
# --------------------------------------------------------------------------------

####验证登录
####记录一个全局变量Username
import socket, sys ,json
timeout = 10
socket.setdefaulttimeout(timeout)  #设定截止时间

def ConfirmUser():
    host = host_ali
    # host = raw_input("Plz imput destination IP:")
    # data = raw_input("Plz imput what you want to submit:")
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except socket.gaierror as e:
        logging.error('连接失败 %s' %e)
        logging.error("Address-related error connecting to server: %s" % e)
        return 'net error'
        # sys.exit(1)
    except socket.error as e:
        logging.error('连接失败 %s' %e)
        logging.error("Connection error: %s" % e)
        return 'net error'
        # sys.exit(1)

#发送激活码
    data = ['login',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")  #转化为BYTE
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)                          #发送

    s.shutdown(1)
    logging.info("Submit Complete")
    print("Submit Complete")
    try:

        login_reply = s.recv(1024)  # 收到回复
        print(login_reply)
        login_reply = str(login_reply, encoding="utf-8")#接受反馈
        login_reply = json.loads(login_reply)      #json转列表
        print(login_reply)
        buf=login_reply[0]
        if buf == 'success':                  #判断是否成功
            logging.info('登录成功 %s' % buf)
            global url2
            url2=login_reply[1]   #修改为最新网址
            return 'login success'  #登录成功，给予返回值
        elif buf == 'wrong password':
            logging.warning('密码错误 %s' %buf)
            return 'wrong password'
        elif buf == "wrong account":
            logging.warning('账号错误 %s' %buf)
            return 'wrong account'
        elif buf == 'repeat':
            logging.warning('账号错误 %s' % buf)
            return 'repeat'
    except:
        print("连接失败")
        logging.warning('连接失败 ' )
        return False


def Logout():
    host = host_ali
    # host = raw_input("Plz imput destination IP:")
    # data = raw_input("Plz imput what you want to submit:")
    port = 8080
    global Username
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
        # sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
        # sys.exit(1)

    # 发送登出信息
    data = ['logout',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")  #转化为BYTE
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)
    s.shutdown(1)
    print("Submit Log Out Complete")
    logging.info("Submit Log Out Complete")


def Keeplogin():
    host = host_ali
    # host = raw_input("Plz imput destination IP:")
    # data = raw_input("Plz imput what you want to submit:")
    port = 8080
    global Username
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
        # sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
        # sys.exit(1)

    # 发送确认信息
    data = ['keep',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")  #转化为BYTE
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)

    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")

# --------------------------------------------------------------------------------
def send_mail(subject,to_list,file_name):
    data=open(file_name,'rb')
    ctype,encoding=mimetypes.guess_type(file_name)
    if ctype is None and encoding is None:
        ctype='application/octet-stream'
    maintype,subtype=ctype.split('/',1)
    file_msg=email.mime.base.MIMEBase(maintype,subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.encoders.encode_base64(file_msg)
    basename=os.path.basename(file_name)
    file_msg.add_header('Content-Disposition','attachment',filename=basename)
    to_list=to_list
    mail_host='smtp.qq.com'
    mail_user=os.environ.get('MAIL_USERNAME')
    mail_pass=os.environ.get('MAIL_PASSWORD')
    me=mail_user
    msg=MIMEMultipart()
    msg.attach(file_msg)
    msg['Subject']=subject
    msg['From']=me
    msg['To']=";".join(to_list)
    server=smtplib.SMTP_SSL(mail_host,465)  # SSL方式加密，QQ port:465
    server.login(mail_user,mail_pass)
    print('login in  successfully')
    server.sendmail(me,to_list,msg.as_string())
    server.quit()
    print('send email  successfully')

def Upload():
    pass #采集有用信息为将来分析准备
# --------------------------------------------------------------------------------
#计算机视觉
def Com_read():
    pass

# --------------------------------------------------------------------------------
#自动操作
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
class TopFrame(wx.Frame):
    def __init__(self, name, rev):  ##########版本号
        wx.Frame.__init__(self, None, 1, name,
                          size=(320, 320))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # 状态栏
        self.statusbar = self.CreateStatusBar()
        # 将状态栏分割为3个区域,比例为1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.statusbar.SetStatusText(u"版本号", 0)

        # 设置状态栏2内容
        self.statusbar.SetStatusText(u"%s" % rev, 1)

        # 设置状态栏3内容
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        self.statusbar.SetBackgroundColour((240,255,255))
        #创建一个容器
        panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        panel.SetBackgroundColour((240,255,255))
        self.SetBackgroundColour((240,255,255))
############################
#######功能区#########
        self.operationarea=wx.StaticBox(panel,label="基本功能")
        self.operationareasizer=wx.StaticBoxSizer(self.operationarea,wx.VERTICAL)


        self.hbox1=wx.BoxSizer(wx.HORIZONTAL)
        self.monibutton = wx.Button(panel, label='打开模拟')
        self.Bind(wx.EVT_BUTTON, self.Openmoni, self.monibutton)
        ###打开国拍
        self.guopaibutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.OpenGuopai, self.guopaibutton)
        self.hbox1.Add(self.monibutton, 0 ,wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.guopaibutton, 0 ,wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox1)
        ###验证码练习
        self.helpbutton = wx.Button(panel, label='查看帮助')
        self.Bind(wx.EVT_BUTTON, self.help, self.helpbutton)
        self.rulebutton = wx.Button(panel, label='查看规定')
        self.Bind(wx.EVT_BUTTON, self.rule, self.rulebutton)
        # self.yanzhengmabutton = wx.Button(panel, label='验证码练习')
        # self.Bind(wx.EVT_BUTTON, self.Yan_practice, self.yanzhengmabutton)
        # self.testbutton = wx.Button(panel, label='考核')
        # self.Bind(wx.EVT_BUTTON, self.Yan_test, self.testbutton)
        self.hbox2=wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2.Add(self.helpbutton, 0 ,wx.ALL | wx.CENTER, 5)
        self.hbox2.Add(self.rulebutton, 0 ,wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox2)

########设置区#########
        self.set=wx.StaticBox(panel,label="常规设置")
        self.setsizer=wx.StaticBoxSizer(self.set)

        self.hbox3=wx.BoxSizer(wx.HORIZONTAL)
        self.advanceset = wx.Button(panel, label='策略设置')
        self.timeautoset = wx.Button(panel, label='comming soon')
        self.Bind(wx.EVT_BUTTON, self.Advanceset, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.Timeautoset,self.timeautoset)
        self.hbox3.Add(self.advanceset, 0 ,wx.ALL | wx.CENTER, 5)
        self.hbox3.Add(self.timeautoset, 0 ,wx.ALL | wx.CENTER, 5)
        self.setsizer.Add(self.hbox3, 0 ,wx.ALL | wx.CENTER, 5)

        self.vbox=wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.operationareasizer, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox.Add(self.setsizer, 0 ,wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox)

        # ###修改国拍网址
        # self.button16 = wx.Button(panel, label='修改国拍网址', pos=(370, 190))
        # self.Bind(wx.EVT_BUTTON, self.UrlGuopai, self.button16)
        # self.urlText = wx.TextCtrl(panel, -1, pos=(370, 230),size=(120,25))
        # ###显示提示
        # self.button7 = wx.Button(panel, label='显示帮助', pos=(10, 190))
        # self.Bind(wx.EVT_BUTTON, self.Help, self.button7)

#--------------------------------------------------------------------------------
# ########设置区############
        self.thread=TimeThread()      #创建时间进程
        self.keepthread=KeepThread()
        ###########创建操作面板
        self.operationframe = OperationFrame()
        self.operationframe.Show(False)  # 初始关闭
#--------------------------------------------------------------------------------
##########控制操作台
        self.timer2=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)#绑定一个定时器事件，主判断
        self.timer2.Start(100)  #设定时间间隔

        #读取最低成交价
        self.timer3=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)#设置一个截屏取价
        self.timer3.Start(100)
        #自动定位
        self.timer4=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Find_pos, self.timer4)#设置一个截屏取价
        self.timer4.Start(150)


        #登录确认器  ,放入独立进程管理
        # self.timer3=wx.Timer(self)
        # self.timer3.Start(90000)  #设定时间间隔，1分半执行一次
        # self.Bind(wx.EVT_TIMER,self.Confirmlogin,self.timer3)



# ------------------------------------------------------------------
# 功能区
    def Openmoni(self, event):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK
        strategy_on = True
        twice = True
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url1, ad_view, web_on, do, guopai_on, moni_on, strategy_repeat
        if guopai_on:
            wx.MessageBox('请关闭国拍页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif moni_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:

            # if not strategy_repeat :  # 判断自动出价进程是否开启
            #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
            #     strategy_repeat=True  #防止进程重复开启
            self.Open()
            if do:
                moni_on = True  # 模拟打开
                ad_view = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟')
                self.operationframe.Show(True)  # 开启控制面板显示
                # 查看时间框是否应该显示
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:  # 判断自动出价进程是否开启
                    self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                    self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                    strategy_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=(-17, 0),
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # pub.subscribe(self.tijiaoPos, "tijiao")
                # pub.subscribe(self.refreshPos, "refresh")
                # pub.subscribe(self.secondPos, "second")
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()

    def OpenGuopai(self, event):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK
        strategy_on = True
        twice = True
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url2, ad_view, web_on, do, moni_on, guopai_on, strategy_repeat
        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
            # if not strategy_repeat :  # 判断自动出价进程是否开启
            #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
            #     strategy_repeat=True  #防止进程重复开启
            if do:
                ad_view = True
                guopai_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')  # 暂时关闭广告
                self.operationframe.Show(True)  # 开启控制面板显示
                # 查看时间框是否应该显示
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:  # 判断自动出价进程是否开启
                    self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                    self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                    strategy_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=(-17, 0))
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # 价格显示

                # pub.subscribe(self.OnCalculatepos, "refresh")
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()  # 关闭可能注册的热键
            self.Listen()

    def UrlGuopai(self, event):
        global url2
        try:
            url2 = self.urlText.GetValue()
            wx.MessageBox('修改网址成功', '修改国拍网址', wx.OK)
        except:
            wx.MessageBox('请输入正确网址', '修改国址网址', wx.OK | wx.ICON_ERROR)

    def Help(self, event):
        licence = """%s

 谁帮我写个帮助啊
 啊
 啊
 啊""" % version

        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetName("小鲜肉拍牌")
        aboutInfo.SetVersion(licence)
        # aboutInfo.SetDescription("最好的拍牌软件!")
        # aboutInfo.SetCopyright("(C) 2017-2022")
        # aboutInfo.SetWebSite("http:#myapp.org")
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)
#打开帮助和规定
    def rule(self,event):
        url="http://121.196.220.94/coursestudy"
        OpenwebThread(url)
    def help(self,event):
        url="http://121.196.220.94/rules"
        OpenwebThread(url)
        # 验证码练习
    def Yan_practice(self, event):
        pass

    def Yan_test(self, event):
        pass
        # 时间调整

    def Time_adjust(self, event):
        pass

# ------------------------------------------------------------------
#设置区域
    def Advanceset(self,event):
        setting=self.FindWindowById(2)
        setting.Show(True)


    def Timeautoset(self,event):
        pass




# ------------------------------------------------------------------
#核心功能区
####截屏取价 暂时放在一起
    def Lowest_price(self, event):  #
        global lowest_price,findpos_on
        if not findpos_on:
            price = int(TopFrame.Price_read())  # 获取当前最低价hash
            # 处理价格
            if price in  pricelist:  # 字典查找
                lowest_price=price
            else:
                findpos_on=True

#原来方法识别
    # def Lowest_price(self, event):  #
    #     global lowest_price,findpos_on
    #     if not findpos_on:
    #         price_hash = TopFrame.Price_hash()  # 获取当前最低价hash
    #         # 处理价格
    #         if price_hash in dick_hash:  # 字典查找
    #             lowest_price = dick_hash[price_hash]
    #         else:
    #             findpos_on=True
            # findposThread()

            # logging.info("NONEHASH")
            # 处理确认
#自动定位
    def Find_pos(self,event):
        global findpos_on
        if findpos_on:
            findpos()




        # print(lowest_price)
    @staticmethod
    def Confirm():
        global cf_hash,confirm_on
        confirm_hash=TopFrame.Confirm_hash() #获取确认信息
        if confirm_hash == cf_hash[0]:
            confirm_on=True
    @staticmethod
    def Refresh():
        refresh_hash=TopFrame.Refresh_hash()  #获取刷新信息
        global cf_hash,refresh_on
        if refresh_hash == cf_hash[1]:
            refresh_on=True

    #image read
    @staticmethod
    def Price_read():
        lowestprice=ImageGrab.grab((Px_lowestprice, Py_lowestprice,
                                   lowestprice_sizex+Px_lowestprice, lowestprice_sizey+Py_lowestprice)).convert('L')

        # global num
        # num+=1
        # lowestprice.save("%s.png"%num)

        lowestprice=np.asarray(lowestprice)
        price=readpic(lowestprice)
        # print(price)
        return price


    @staticmethod
    def Price_hash():
        lowestprice = pg.screenshot(region=(Px_lowestprice, Py_lowestprice,
                                   lowestprice_sizex, lowestprice_sizey))
        global num
        num+=1
        # lowestprice.save("%d.png"%num)
        price_hash = imagehash.dhash(lowestprice)
        # hash = dhash(sc)
        # print("截图成功")
        return price_hash

    @staticmethod
    def Confirm_hash():
        confirm = pg.screenshot(region=(Px_confirm, Py_confirm,
                                   confirm_sizex, confirm_sizey))
        # num+=1
        # sc.save("%d.png"%num)
        confirm_hash = imagehash.dhash(confirm)
        return confirm_hash

    @staticmethod
    def Refresh_hash():
        refresh = pg.screenshot(region=(Px_refresh, Py_refresh,
                                        refresh_sizex, refresh_sizey))

        refresh_hash = imagehash.dhash(refresh)
        return refresh_hash


    @staticmethod
    def OnJiajia():
        po = pg.position()
        Position[0][0] = po[0]
        Position[0][1] = po[1]
        print(Position[0][0], "  ", Position[0][1])
        findpos()

    @staticmethod
    def OnChujia():
        po = pg.position()
        Position[1][0] = po[0]
        Position[1][1] = po[1]

    @staticmethod
    def OnTijiao():
        po = pg.position()
        Position[2][0] = po[0]
        Position[2][1] = po[1]

    @staticmethod
    def OnShuaxin():
        po = pg.position()
        Position[3][0] = po[0]
        Position[3][1] = po[1]

    @staticmethod
    def OnConfirm():
        po = pg.position()
        Position[4][0] = po[0]
        Position[4][1] = po[1]

    @staticmethod
    def OnYanzhengma():
        po = pg.position()
        Position[5][0] = po[0]
        Position[5][1] = po[1]

    ##执行定位操作
    @staticmethod
    def handle_Jiajia():
        TopFrame.OnJiajia()

    @staticmethod
    def handle_Chujia():
        TopFrame.OnChujia()

    @staticmethod
    def handle_Tijiao():
        TopFrame.OnTijiao()

    @staticmethod
    def handle_Shuaxin():
        TopFrame.OnShuaxin()

    @staticmethod
    def handle_Confirm():
        TopFrame.OnConfirm()

    @staticmethod
    def handle_Yanzhengma():
        TopFrame.OnYanzhengma()

        ###############################

        ##执行点击操作
        ##点击
        ##执行点击操作
        ##点击
    @classmethod
    def OnClick_Tijiao(cls):
        global web_on, tijiao_on, one_delay, second_delay, tijiao_num
        global tijiao_on, chujia_on, confirm_one, confirm_need
        confirm_need = True

        if tijiao_num == 1:
            timer = threading.Timer(one_delay, cls.Tijiao)
            timer.start()
            tijiao_on = False
            if twice:
                print("修改为2")
                tijiao_num = 2
            # chujia_on=True
            print("成功提交")
        elif tijiao_num == 2:
            tijiao_num = 0
            timer = threading.Timer(second_delay, cls.Tijiao)
            timer.start()
            tijiao_on = False
            # chujia_on=True
        else:
            cls.Tijiao()

    @staticmethod
    def Tijiao():
        global tijiao_on, tijiao_OK, tijiao_num
        Click(Position[2][0], Position[2][1])
        tijiao_OK = False  # 需要按E解锁，自动提交
        global confirm_one
        if not confirm_one:  # 激活确认
            confirmthread = confirmThread()
            confirm_one = False

    # @staticmethod
    # def OnClick_Jiajia():
    #     global web_on
    #     Click(Position[0][0],Position[0][1],button='left')
    #     Click(Position[1][0],Position[1][1],button='left')

    @staticmethod
    def OnClick_Shuaxin():
        global web_on
        Click(Position[3][0], Position[3][1])
        Click(Position[5][0], Position[5][1])

    @staticmethod
    def OnClick_confirm():
        print(Position[4][0], Position[4][1])
        Click(Position[4][0], Position[4][1])

    @staticmethod
    def OnClick_chujia():
        global web_on, lowest_price
        global tijiao_num, own_price1, own_price2, one_diff, second_diff
        global tijiao_on, chujia_on
        global refresh_need, refresh_one, chujia_interval
        print(chujia_interval)
        if not chujia_interval:
            print(tijiao_num, twice)
            chujia_interval = True
            tijiao_on = True  # 激活自动出价
            refresh_need = True  # 激活刷新验证码
            if tijiao_num == 1:
                own_price1 = lowest_price + one_diff
                setText(str(own_price1))
                TopFrame.selfdelete()
                Click(Position[1][0], Position[1][1])
                tijiao_on = True
                chujia_on = False
                chujia_interval = False  # 间隔结束
                print(chujia_interval)

                if not refresh_one:  # 激活确认
                    refreshthread = refreshThread()
                    refresh_one = True
            elif tijiao_num == 2 and twice:
                # print("第二次")
                own_price2 = lowest_price + second_diff
                setText(str(own_price2))
                TopFrame.selfdelete()
                Click(Position[1][0], Position[1][1])
                tijiao_on = True
                chujia_on = False
                chujia_interval = False  # 间隔结束
                if not refresh_one:  # 激活确认
                    refreshthread = refreshThread()
                    refresh_one = True

    @staticmethod
    def selfdelete():
        Click2(Position[6][0], Position[6][1])
        Click2(Position[6][0], Position[6][1])
        Delete()
        Paste()  # 粘贴

    @staticmethod
    def selfChujia():
        # for i in range(15):
        #     Click(Position[6][0], Position[6][1])
        #     Delete()
        # a=wx.FindWindowById(1)
        # a.Show(True)
        global price_view, price_count
        Click(Position[4][0], Position[4][1])
        Click(Position[0][0], Position[0][1])
        Click(Position[1][0], Position[1][1])
        price_view = True
        price_count = 0

    @staticmethod
    def selfTijiao():
        OperationFrame.Del_shot()
        Click(Position[2][0], Position[2][1])

    @staticmethod
    def OnClick_Backspace():
        pg.press('backspace')

    def MainControl(self, event):
        #####
        if not web_on and time_on:  # 网页关就把时间关掉
            self.operationframe.Closetime()
        # if web_on:
        #     try:
        #         self.operationframe.Show(True)
        #     except:
        #         pass
        # else:
        #     try:
        #         self.operationframe.Show(False)
        #     except:
        #         pass

        # 显示与隐藏主面板
        # if web_on:
        #     self.Show(False)
        # else:
        #     self.Show(True)


            ##############表示成功输入验证码

    @staticmethod
    def tijiao_ok():
        global tijiao_OK, refresh_need, tijiao_on
        if e_on and tijiao_on:
            tijiao_OK = True
            refresh_need = False  # 关闭刷新识别

    @staticmethod
    def tijiao_ok2():
        global tijiao_OK, refresh_need
        if enter_on and tijiao_on:
            tijiao_OK = True
            refresh_need = False  # 关闭刷新识别

    @classmethod
    def query(cls):
        global query_interval, query_on
        if not query_interval and not query_on:
            # print("执行")
            query_on = True
            query_interval = True
            setText(str(1000000))  # 出一定超出的价格
            Click(Position[6][0], Position[6][1])
            Click(Position[6][0], Position[6][1])
            Paste()
            Click(Position[1][0], Position[1][1])
            timer1 = threading.Timer(3, cls.query_sleep3)
            timer1.start()
            timer2 = threading.Timer(5, cls.query_sleep5)
            timer2.start()
        elif query_interval and query_on:
            # print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False

    @staticmethod
    def query_sleep3():
        # print("触发3+")
        global query_interval, query_on
        if query_on:
            # print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False

    @staticmethod
    def query_sleep5():
        # print("触发5")
        global query_interval
        query_interval = False

        # 改键控制

    @staticmethod
    def Open():
        global do, web_on
        if not do:
            do = True
            # 定义快捷键
            ############################
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            user32 = ctypes.windll.user32
            HOTKEYS1 = {1: (VK_CODE['2'], win32con.MOD_ALT), 2: (VK_CODE['3'], win32con.MOD_ALT),
                        3: (VK_CODE['4'], win32con.MOD_ALT), 4: (VK_CODE['5'], win32con.MOD_ALT),
                        5: (VK_CODE['6'], win32con.MOD_ALT), 6: (VK_CODE['7'], win32con.MOD_ALT),
                        }
            HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                        10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                        13: (VK_CODE['q'], 0x4000)}
            # 注册快捷键
            for id, (vk, modifiers) in HOTKEYS1.items():
                if not user32.RegisterHotKey(None, id, modifiers, vk):
                    print("Unable to register id", id)
                    logging.info("Unable to register id", id)
                    do = False
            for id, (vk, modifiers) in HOTKEYS2.items():
                if not user32.RegisterHotKey(None, id, modifiers, vk):
                    print("Unable to register id", id)
                    logging.info("Unable to register id", id)
                    do = False
                web_on = True

    # 启动监听
    @staticmethod
    def Listen():
        try:
            # 快捷键对应的驱动函数   1: TopFrame.handle_Jiajia
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            HOTKEY_ACTIONS = {
                1: TopFrame.handle_Jiajia, 2: TopFrame.handle_Chujia, 3: TopFrame.handle_Tijiao,
                4: TopFrame.handle_Shuaxin, 5: TopFrame.handle_Confirm,
                6: TopFrame.handle_Yanzhengma, 7: TopFrame.OnClick_Shuaxin, 8: TopFrame.selfTijiao,
                9:(lambda :TopFrame.selfChujia()), 10: TopFrame.OnClick_Backspace, 11: TopFrame.tijiao_ok, 12: TopFrame.tijiao_ok2,
                13: TopFrame.query}
            user32 = ctypes.windll.user32
            msg = wintypes.MSG()
            byref = ctypes.byref
            while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
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

    @staticmethod
    def Close():
        global do
        if do:
            do = False
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            HOTKEYS1 = {1: (VK_CODE['2'], win32con.MOD_ALT), 2: (VK_CODE['3'], win32con.MOD_ALT),
                        3: (VK_CODE['4'], win32con.MOD_ALT), 4: (VK_CODE['5'], win32con.MOD_ALT),
                        5: (VK_CODE['6'], win32con.MOD_ALT), 6: (VK_CODE['7'], win32con.MOD_ALT),
                        }
            user32 = ctypes.windll.user32
            HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                        10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                        13: (VK_CODE['q'], 0x4000)}
            for id in HOTKEYS1.keys():
                user32.UnregisterHotKey(None, id)
            for id in HOTKEYS2.keys():
                user32.UnregisterHotKey(None, id)
            logging.info("close assistant success")
        else:
            pass


# ------------------------------------------------------------------
#辅助功能区
####设置背景图片
    def OnEraseBackground(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("blue.jpg")
        dc.DrawBitmap(bmp, 0, 0)

        ##定位
        # 1: handle_Jiajia,
        # 2: handle_Chujia,
        # 3: handle_Tijiao,
        # 4: handle_Shuaxin,
        # 5: handle_Confirm,




##########主程序关闭选项#############
    def OnClose(self, event):
        ret = wx.MessageBox('真的要退出第一枪吗?', '确认', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            # do something here...
            import sys
            # command = 'taskkill /F /IM assistant_rev3.exe'        #修改
            # # 比如这里关闭QQ进程
            # os.system(command)
            # os._exit()
            self.Show(False)

            try:
                self.Close_time1(event)    #关闭可能未关闭的窗口
                self.Close_time2(event)
            except:
                pass

            Logout()             #登出
            wx.GetApp().ExitMainLoop()
            event.Skip()
            sys.exit(None)




#------------------------------------------------------------------
#放弃的功能
######## 开启辅助
    def OnOpenAssist(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()
    # 关闭辅助
    @classmethod
    def OnCloseAssist(cls):
        cls.Close()
        # global do
        # if not do:
        #     wx.MessageBox('关闭成功', '关闭辅助', wx.OK | wx.ICON_INFORMATION)
        # else:
        #     wx.MessageBox('关闭失败', '关闭辅助', wx.OK | wx.ICON_ERROR)
    # 显示位置

# ------------------------------------------------------------------
# 放弃的功能
    def OnViewPos(self, event):
        wx.CallAfter(pub.sendMessage, "refresh")
        self.MovePos(event)
        global view
        if not view:
            view = True
            for i in range(len(Position)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(Position)):
                self.posframe[i].Hide()

    # 保存位置
    def OnSavePos(self, event):
        self.MovePos(event)
        self.Save_log()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)




    #移动窗口
    def MovePos(self,event):
        global Positon
        for i in range(5):
            posx,posy = Position[i]
            self.posframe[i].Move(posx-10,posy-5)



#------------------------------------------------------------------------------



    # @classmethod
    # def OnClick_Tijiao(cls):
    #     wx.CallAfter(pub.sendMessage, "refresh")
    #     global web_on,tijiao_on,delay
    #     # print(delay)
    #     if  delay:
    #         timer = threading.Timer(0.5,cls.Tijiao )
    #         timer.start()
    #     else:
    #         cls.Tijiao()
    #
    # @staticmethod
    # def Tijiao():
    #     global tijiao_on
    #     wx.CallAfter(pub.sendMessage, "tijiao")
    #
    # @staticmethod
    # def CTijiao():
    #     global tijiao_on
    #     Click(Position[3][0] - 150, Position[3][1])
    #     Click(Position[2][0],Position[2][1] )
    #     tijiao_on=False   #关闭触发
    #
    #
    #
    # # @staticmethod
    # # def OnClick_Jiajia():
    # #     global web_on
    # #     Click(Position[0][0],Position[0][1] )
    # #     Click(Position[1][0],Position[1][1] )
    # @classmethod
    # def OnClick_Shuaxin(cls):
    #     global web_on
    #     wx.CallAfter(pub.sendMessage, "refresh")
    #
    # @staticmethod
    # def OnCClick_Shuaxin():
    #     Click(Position[3][0]-150, Position[3][1])
    #     Click(Position[3][0],Position[3][1] )
    #     Click(Position[5][0],Position[5][1] )
    #
    # @classmethod
    # def OnClick_chujia(cls):
    #     wx.CallAfter(pub.sendMessage, "second")
    #
    # @staticmethod
    # def OnCClick_second():
    #     global price_view,price_count,web_on,tijiao_on
    #     tijiao_on=True     #激活自动出价
    #     print("已经点击")
    #     global Position
    #     Click(Position[4][0], Position[4][1] )
    #     Click(Position[0][0], Position[0][1] )
    #     Click(Position[1][0], Position[1][1] )
    #     price_view = True
    #     price_count = 0






# #设定间隔辅助
#     def Price_count(self,event):
#         global price_count
#         price_count+=1



    # ----------------------------------------------------------------------


    def Save_log(self):
        output=open('pos.log','wb')
        pickle.dump(Position,output)
        output.close()

    # 截图处理，此次出价




# #############修改时间###########
#     def Add_time(self, event):
#         global a_time,moni_second,moni_on,guopai_on
#         if moni_on:
#             moni_second+=0.1
#         else:
#             a_time += 0.1
#
#     def Minus_time(self, event):
#         global a_time,moni_second,moni_on,guopai_on
#         if moni_on:
#             moni_second-=0.1
#         else:
#             a_time -= 0.1
#
#     def Add_second(self, event):
#         global a_time,moni_second,moni_on,guopai_on
#         if moni_on:
#             moni_second += 1
#             if moni_second>=60:
#                 moni_second=0
#         else:
#             a_time+=1
#
#     def Minus_second(self, event):
#         global a_time,moni_second,moni_on,guopai_on
#         if moni_on:
#             moni_second -= 1
#             if moni_second<=0:
#                 moni_second=60
#         else:
#             a_time-=1
#
# #国拍时间控制
#     def Open_time1(self, event):
#         self.timeframe1.Show(True)
#         global view_time
#         view_time=True
#     def Close_time1(self, event):
#         self.timeframe1.Show(False)
#         global view_time
#         view_time=False
# #模拟时间控制
#     def Open_time2(self, event):
#         self.timeframe2.Show(True)
#         global view_time
#         view_time=True
#     def Close_time2(self, event):
#         self.timeframe2.Show(False)
#         global view_time
#         view_time=False

# #############时间换算###############
# #转时间戳
#     def changetime(self,a):   #换算成时间戳
#         final_time=time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#         return final_time            #以时间戳输出
#
# #转字符串
#     def get_nowtime(self):
#         tem1 = time.time()
#         a = time.strftime('%Y-%m-%d', time.localtime(tem1))
#         return a               #输出时间格式字符串
# #转为最终时间戳，调用这个时间
#     def gettime(self,event,choice1,choice2):      #choice1:55,choice2:0.5
#         tem = self.get_nowtime()
#         b = tem + ' 11:29:' + str(choice1)
#         c=self.changetime(b)+float(choice2)
#         return c         #得到用户所确定的最终时间戳



#################登录确认#############
    def Confirmlogin(self,event):
        Keeplogin()


####设定策略
#修改时间
    def Choose_time1(self,event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection())+'.'+
        str(self.time_choice2.GetSelection())+ " 秒")
        global strategy1,strategy2
        strategy1=self.time_choice1.GetString(self.time_choice1.GetSelection())
        strategy2=self.time_choice2.GetString(self.time_choice2.GetSelection())


    def Choose_time2(self,event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection())+'.'+
        str(self.time_choice2.GetSelection())+ " 秒")
        global strategy1,strategy2
        strategy1=self.time_choice1.GetString(self.time_choice1.GetSelection())
        strategy2=self.time_choice2.GetString(self.time_choice2.GetSelection())

# 开启自动出价
#     def Strategy_select(self, event):
#         global tijiao_delay,strategy_on,final_tijiao,strategy_repeat,guopai_tijiao
#         strategy_on=True  #开启自动出价，打开国拍、模拟可以自动开启进程
#         guopai_tijiao=True #执行一次国拍提交
#         final_tijiao=self.gettime(event,strategy1,strategy2) #计算得到的时间戳
#         tijiao_delay=final_tijiao-a_time                     #计算得到等待时间
#
#         # print(final_tijiao,a_time)
#         #启动
#         state = event.GetEventObject().GetValue()
#         if state==True:
#             event.GetEventObject().SetLabel("己开启自动出价")
#             if not strategy_repeat :  # 判断自动出价进程是否开启
#                 self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
#                 self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
#                 strategy_repeat=True
#         else:
#             strategy_on=False
#             guopai_tijiao=False
#             event.GetEventObject().SetLabel("未开启自动出价")
#             # try:
#             #     self.monitijiaothread.terminate()
#             #     self.tijiaothread.terminate()
#             # except:
#             #     pass
#             ######关闭自动出价进程

    # def delayCheck(self,event):
    #     global delay
    #     checkBoxSelected = event.GetEventObject()
    #     if checkBoxSelected.IsChecked():
    #         delay=True
    #     else:
    #         delay=False


#####时间选择
    # def OnTimeChoose(self, event):
    #     state = event.GetEventObject().GetValue()
    #     global moni_on
    #     if state == True:
    #         moni=False
    #         event.GetEventObject().SetLabel("修改国拍时间")
    #     else:
    #         moni=True
    #         event.GetEventObject().SetLabel("修改模拟时间")


    # -----------------------------------------------------------------------
#################国拍时间显示##################
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(100)  # 设定时间间隔

    def Draw(self, dc):  # 绘制当前时间
        global a_time
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):  # 更新
        global a_time, b_time
        # a_time = a_time + 0.2
        if b_time < 9:
            b_time = b_time + 1
        else:
            b_time = 0
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)         #+ '.' + str(b_time)
        # st="%s:%s:%s"%(b_time[0],b_time[1],b_time[2])
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


#国拍时间框显示
class TimeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=Pos_timeframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        # wx.Frame.__init__(self, None, -1,'Time',size=(400,160), pos=Pos_timeframe,
        #                   style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        ClockWindow(self)


#-----------------------------------------------------------------------
#################模拟时间显示##################
class MoniClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(100)  # 设定时间间隔

    def Draw(self, dc):  # 绘制当前时间
        global moni_second
        st = "%s:%s:%s" %(11,29,moni_second)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):  # 更新
        global moni_second

        moni_s=int(moni_second)   #整数化
        st ="%s:%s:%s" %(11,29,moni_s)
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


#国拍时间框显示
class MoniTimeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200,50), pos=Pos_timeframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        # wx.Frame.__init__(self, None, -1,'Time',size=(400,160), pos=Pos_timeframe,
        #                   style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        MoniClockWindow(self)



# ----------------------------------------------------------------------
class PosFrame(wx.Frame):
    def __init__(self,pos,pos_name):
        x,y=pos
        wx.Frame.__init__(self, None, -1, 'POS',
                          pos=(x-20,y-10), size=(30, 20), style=wx.FRAME_TOOL_WINDOW )
        panel = wx.Panel(self, -1,size=(30,20))
        # 这是一个基本的静态文本
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        t1 = []
        t1.append(wx.StaticText(panel, -1, pos_name,
                                (0, 0)))
        for i in range(len(t1)):
            t1[i].SetFont(font)

class PriceFrame(wx.Frame):
    def __init__(self,image):

        wx.Frame.__init__(self, None, -1,'Price',size=Pricesize, pos=Pos_priceframe,
                          style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        self.panel=wx.Panel(self,size=Pricesize)
        #image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(image))

class YanzhengmaFrame(wx.Frame):
    def __init__(self,image):

        wx.Frame.__init__(self, None, -1,'Price',size=(400,80), pos=Pos_yanzhengmaframe,
                          style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        self.panel=wx.Panel(self,size=(400,80))
        #image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(image))



class AdFrame(wx.Frame):
    def __init__(self):  ##########版本号
        wx.Frame.__init__(self, None, -1, "广告",
                         pos=(0,250), size=(250, 200),style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        panel = wx.Panel(self, -1,size=(250,200))
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

class WebFrame(wx.Frame):
    def __init__(self,px,py,ad,name):   #name:窗口显示名称
        wx.Frame.__init__(self, None, -1, name, size=(websize[0], websize[1]), pos=(px, py),style=wx.SIMPLE_BORDER)

        # wx.Frame.__init__(self,None, -1,title="大师拍牌 QQ 178456661 - 3.663",size=(websize[0], websize[1]),\
        #  pos=(px, py),style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP&~(wx.RESIZE_BORDER))
        #wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.CLOSE_BOX))
        if ad:
            self.adframe=AdFrame()
            self.adframe.Show(True)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ad2=ad
        self.control=ControlFrame()
        self.control.Show(True)
        # panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        # panel.SetFocus()
        # panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)



    # def OnKeyDown(self, event):
    #     keycode = event.GetKeyCode()
    #     if keycode == wx.WXK_F1:
    #         x, y = pg.position()
    #         print(x, y)
    #     else:
    #         event.Skip()
    #     global num
    #     sc = pg.screenshot(region=(377, 412, 41, 16))
    #     global num
    #     print("成功")
    #     sc.save("%d.png" %num)
    #     num+=1
    #
    #
    # def Webpos(self):
    #     return self.GetPosition()  #输出位置坐标
        pub.subscribe(self.OnClose2, "close web")  #触发关闭
    def OnClose(self,event):
        global web_on,view_time,moni_on,guopai_on,strategy_repeat
        web_on=False
        view_time=False
        moni_on=False
        guopai_on=False
        TopFrame.Close()
        file="sc_new.png"
        if  os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()
        event.Skip()

    def OnClose2(self):
        global web_on,view_time,moni_on,guopai_on,strategy_repeat
        web_on=False
        view_time=False
        moni_on=False
        guopai_on=False
        TopFrame.Close()
        file="sc_new.png"
        if  os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()

#控制小窗
class ControlFrame(wx.Frame):  #为webframe提供控制操作
    def __init__(self):   #name:窗口显示名称
        wx.Frame.__init__(self, None, -1, size=(330, 270), style=wx.NO_BORDER|wx.STAY_ON_TOP|wx.FRAME_NO_TASKBAR, \
                          pos=(Px+40, Py+480) )
        self.panel=wx.Panel(self,-1,size=(330, 270))
        # self.button1=wx.Button(self.panel,pos=(0,0),size=(50,25),label="关闭")
        # self.Bind(wx.EVT_BUTTON, self.o_closeweb, self.button1)
        font1=wx.Font(25, wx.SWISS, wx.NORMAL, wx.NORMAL)
        font2=wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.adtext=wx.StaticText(self.panel,label=u"小鲜肉代拍",pos=(90,20))
        self.adtext.SetFont(font1)
        self.pricetext=wx.StaticText(self.panel,label=u"最低成交价:",pos=(50,90))
        self.pricetext.SetFont(font2)
        self.price=wx.StaticText(self.panel,pos=(190,90))
        self.price.SetFont(font2)
        self.timetext = wx.StaticText(self.panel, label=u"当前时间:",pos=(50,130))
        self.timetext.SetFont(font2)
        self.time=wx.StaticText(self.panel,pos=(190,130))
        self.time.SetFont(font2)

        self.netstattext=wx.StaticText(self.panel,pos=(80,170),label=u"网速")
        self.netstattext.SetFont(font2)
        self.netstat=wx.StaticText(self.panel,pos=(190,170))

        # dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        #定时器
        self.timetimer1=wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.Timego,self.timetimer1)
        self.timetimer1.Start(100)
    def o_closeweb(self,event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()

    def Timego(self,event):
        global lowest_price,moni_second,a_time
        self.price.SetLabel("%s"%lowest_price)
        if moni_on:
            self.time.SetLabel("11:29:%s"%int(moni_second))
        else:
            timestr1=time.localtime(a_time)
            timestr2=time.strftime("%H:%M:%S",timestr1)
            self.time.SetLabel(timestr2)
        global pinger
        pingnow=pinger.ping()
        if pingnow == "timeout":
            self.netstat.SetLabel("%s"%pingnow)
        else:
            self.netstat.SetLabel("%sms" % pingnow)
##################
#功能窗口#
class OperationFrame(wx.Frame):
    def __init__(self):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 2,title="小鲜肉代拍", pos=(1070,100),size=(300, 425),\
                          style=wx.FRAME_NO_TASKBAR|wx.CAPTION|wx.CLOSE_BOX)  # wx.FRAME_TOOL_WINDOW|   |wx.STAY_ON_TOP

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)
        #显示价格
        self.timer1=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)#绑定一个定时器事件，主判断
        self.timer1.Start(500)  #设定时间间隔
        #设定间隔
        self.timer2=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_count, self.timer2)#
        self.timer2.Start(100)  #设定时间间隔
        #显示最低成交价
        self.lowestframe = LowestpriceFrame()
        self.lowestframe.Show(False)

#############################
        ####布局
        panel = wx.Panel(self, -1, size=(300, 380))
        stractagy = wx.StaticBox(panel, -1, u'选择策略:')
        self.stractagySizer = wx.StaticBoxSizer(stractagy, wx.VERTICAL)
        stractagy_label = wx.StaticText(panel, label=u"设定拍牌策略",size=(100,50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(stractagy_label )



        # 选择策略
        stractagy_choices = [u'单枪策略', u'双枪策略',u'手动操作（热键辅助）' ]
        self.select_stractagy = wx.Choice(panel, -1, choices=stractagy_choices,size=(100,50))
        hbox1.Add(self.select_stractagy)
        self.select_stractagy.SetSelection(0)
        #时间显示
        self.timeview = wx.CheckBox(panel, -1, label=u'显示时间')  #开启时间显示
        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.timeview)


        self.button1 = wx.Button(panel, label='+1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Add_second, self.button1)
        self.button2 = wx.Button(panel, label='-1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Minus_second, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)

        hbox2.Add(self.button1)
        hbox2.Add(self.button2)
        hbox2.Add(self.button3)
        hbox2.Add(self.button4)
        #竖直SIZER
        vb1=wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)
        vb1.Add(hbox2)

        #设置确认方式
        confirm_choice=["E键","回车"]
        self.confirm_choice=wx.Choice(panel,-1,choices=confirm_choice)
        self.confirm_choice.SetSelection(0)
        self.confirm_label=wx.StaticText(panel, label=u"确认提交方式     ")
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.confirm_label,flag=wx.TOP,  border=4)
        hbox3.Add(self.confirm_choice)
        vb1.Add(hbox3)

        #策略保存与恢复
        self.strategy_save=wx.Button(panel,label="保存策略",size=(60,35))
        self.strategy_load=wx.Button(panel,label="载入策略",size=(60,35))
        self.save_info=wx.Button(panel,label="用户信息",size=(60,35))
        hbox4= wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.strategy_save)
        hbox4.Add(self.strategy_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)


        # 网格需放置于静态框中
        oneshot = wx.StaticBox(panel, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajia_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))   #,style=wx.SP_WRAP最大值向上变最小值
        self.jiajia_time.SetRange(40, 55)
        self.jiajia_time.SetValue(48)
        self.jiajia_time.SetIncrement(0.1)

        gridsizer1.Add(self.jiajia_time, pos=(0, 0))
        miao_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP|wx.ALIGN_LEFT,  border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价",style=wx.ALIGN_CENTER,size=(25,25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP,  border=4)
        self.jiajia_price = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))

        # 选择提交方式,第二排
        tijiao_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao = wx.Choice(panel, -1, choices=tijiao_choices,size=(68, 25))
        self.select_tijiao.SetSelection(0)
        gridsizer1.Add(self.select_tijiao, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP,  border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP,  border=4)

        # 选择提交方式,第三排
        tijiao_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(tijiao_label, pos=(2, 0), flag=wx.TOP,  border=4)
        self.tijiao_time = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.tijiao_time.SetRange(40.0, 57.0)
        self.tijiao_time.SetValue(55.0)
        self.tijiao_time.SetIncrement(0.1)
        gridsizer1.Add(self.tijiao_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label,  pos=(2, 2), flag=wx.TOP,  border=4)
        # 网格需放置于静态框中
        self.oneshotSizer.Add(gridsizer1, 0,flag=wx.ALL,border=5)

        # 第二枪
        # 选择加价时间,第一排
        secondshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajia_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.jiajia_time2.SetRange(40, 55)
        self.jiajia_time2.SetValue(48)
        self.jiajia_time2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajia_time2, pos=(0, 0) )
        miao_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao_label2,  pos=(0, 1) ,flag=wx.TOP|wx.ALIGN_LEFT,  border=4)
        jiahao_label2 = wx.StaticText(panel, label=u"加价",size=(25,25),style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2,  pos=(0, 2) ,flag=wx.TOP,  border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3) )
        # 选择提交方式,第二排
        tijiao_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao2 = wx.Choice(panel, -1, choices=tijiao_choices2,size=(68, 25))
        self.select_tijiao2.SetSelection(0)
        gridsizer2.Add(self.select_tijiao2, pos=(1, 0) )
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1) ,flag=wx.TOP,  border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2,  pos=(1, 3) )
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2,  pos=(1, 4) ,flag=wx.TOP,  border=4)

        # 选择提交方式,第三排
        tijiao_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(tijiao_label2, pos=(2, 0) ,flag=wx.TOP,  border=4)
        self.tijiao_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.tijiao_time2.SetRange(53.0, 57.0)
        self.tijiao_time2.SetValue(55.0)
        self.tijiao_time2.SetIncrement(0.1)
        gridsizer2.Add(self.tijiao_time2, pos=(2, 1) )
        miao3_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2) ,flag=wx.TOP,  border=4)
        # 网格需放置于静态框中
        self.secondshotSizer.Add(gridsizer2, 0,flag=wx.ALL,border=5)
        self.stractagySizer.Add(vb1, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL )

        #加横线
        title=wx.StaticText(panel,-1,label=u"拍牌功能设置")
        warning=wx.StaticText(panel,-1,label=u"10点半需要进行第一次出价")
        warning.SetForegroundColour('red')
        line=wx.StaticLine(panel, -1  )
        self.vbox1.Add(title,0,wx.ALL | wx.LEFT, 10)
        self.vbox1.Add(warning,0,wx.LEFT, 10)
        self.vbox1.Add(line,flag=wx.EXPAND|wx.BOTTOM,border=10)
        self.vbox1.Add(self.stractagySizer, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.oneshotSizer, 0,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.secondshotSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox1)

#显示参数设置
        self.secondsizer_Shown=False #二次出价默认关闭
        self.oneshotsizer_Shown=True #单次出价默认开启
        self.vbox1.Hide(self.secondshotSizer) #默认关闭二次出价



# 状态区，显示当前策略，最低成交价，时间，出价状态

#-------------待增加-------------------#

#绑定操作
        self.Bind(wx.EVT_CHECKBOX, self.Timeview,self.timeview)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice,self.confirm_choice)
        self.Bind(wx.EVT_BUTTON,self.Strategy_save,self.strategy_save)
        self.Bind(wx.EVT_BUTTON,self.Strategy_load,self.strategy_load)
        self.Bind(wx.EVT_BUTTON,self.Save_info,self.save_info)

        self.Bind(wx.EVT_CHOICE, self.Refresh_panel,self.select_stractagy)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE, self.Jiajia_time,self.jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time,self.jiajia_time)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Jiajia_price,self.jiajia_price)
        self.Bind(wx.EVT_TEXT , self.Jiajia_price,self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao,self.select_tijiao)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Yanchi_time,self.yanchi_time)
        self.Bind(wx.EVT_TEXT , self.Yanchi_time,self.yanchi_time)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Tijiao_time,self.tijiao_time)
        self.Bind(wx.EVT_TEXT , self.Tijiao_time,self.tijiao_time)

        # self.Bind(wx.EVT_SPINCTRLDOUBLE, self.Jiajia_time2,self.jiajia_time2)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2,self.jiajia_time2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Jiajia_price2,self.jiajia_price2)
        self.Bind(wx.EVT_TEXT , self.Jiajia_price2,self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao2,self.select_tijiao2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Yanchi_time2,self.yanchi_time2)
        self.Bind(wx.EVT_TEXT , self.Yanchi_time2,self.yanchi_time2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Tijiao_time2,self.tijiao_time2)
        self.Bind(wx.EVT_TEXT , self.Tijiao_time2,self.tijiao_time2)
#初始化国拍时间窗口
        self.timeframe1=TimeFrame()
        self.timeframe1.Show(False)
#初始化模拟时间窗口
        self.timeframe2=MoniTimeFrame()
        self.timeframe2.Show(False)

        # 增加一个判定事件
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(3000)

    def OnClose(self,event):
        self.Show(False)
    # 动态显示价格
    def Price_view(self, event):
        global price_view, web_on, price_on, view_time
        # print(price_view, price_count)
        if price_view and price_count >= 4:
            try:
                self.Price_close()
            except:
                pass
            self.Screen_shot()
            image = "sc_new.png"
            self.priceframe = PriceFrame(image)
            self.priceframe.Show(True)
            price_view = False
            price_on = True
            # print("到这5")

    def Price_count(self,event):
        #设计手动显示价格的判定器，制作显示间隔
        global price_count
        price_count+=1
        file='sc_new.png'
        if web_on and strategy_on:
            self.lowestframe.Show(True)
        if not os.path.exists(file):
            try:
                self.Price_close()
            except:
                pass
        #手动关闭最低价显示
        if not strategy_on or not web_on:
            self.lowestframe.Show(False)



    # 获取出价信息
    def Screen_shot(self):
        global Pricesize
        box = Pos_price
        region = ImageGrab.grab(box)
        region.resize(Pricesize, Image.ANTIALIAS).save("sc_new.png")

    # 删除此图
    @staticmethod
    def Del_shot():
        try:
            os.remove("sc_new.png")
        except:
            pass
            # 关闭显示

    def Price_close(self):
        try:
            self.priceframe.Destroy()
        except:
            pass



    def opt(self,event):
        global tijiao_num,tijiao_one,chujia_on
        global strategy_on  # 策略开启
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one  # 二次出价触发开关
        if self.select_stractagy.GetSelection == 0:
            if moni_second < one_time1 and moni_on:
                # print("触发1")
                twice = False
                strategy_on = True
                chujia_on = True
                tijiao_on = False
                tijiao_num = 1  # 初始化
                tijiao_OK = False
                tijiao_one = False  # 单枪未开
        elif self.select_stractagy.GetSelection == 1:
            if moni_second < one_time1 and moni_on:
                # print("触发2")
                strategy_on = True
                twice = True
                chujia_on = True
                tijiao_on = False
                tijiao_num = 1  # 初始化
                tijiao_OK = False
                tijiao_one = False  # 单枪未开


#时间修改操作
    def Add_time(self, event):
        global a_time,moni_second,moni_on,guopai_on
        if moni_on:
            moni_second+=0.1
        else:
            a_time += 0.1

    def Minus_time(self, event):
        global a_time,moni_second,moni_on,guopai_on
        if moni_on:
            moni_second-=0.1
        else:
            a_time -= 0.1

    def Add_second(self, event):
        global a_time,moni_second,moni_on,guopai_on
        if moni_on:
            moni_second += 1
            if moni_second>=60:
                moni_second=0
        else:
            a_time+=1

    def Minus_second(self, event):
        global a_time,moni_second,moni_on,guopai_on
        if moni_on:
            moni_second -= 1
            if moni_second<=0:
                moni_second=60
        else:
            a_time-=1
#时间显示控制器
    def Timeview(self,event):
        timeSelected = event.GetEventObject()
        global view_time,time_on
        if timeSelected.IsChecked():
            view_time=True
            time_on=True
            if guopai_on:
                self.timeframe1.Show(True)
            elif moni_on:
                self.timeframe2.Show(True)
        else:
            view_time=False
            time_on=False
            if guopai_on:
                self.timeframe1.Show(False)
            elif moni_on:
                self.timeframe2.Show(False)

    def Opentime(self):
        if moni_on:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif guopai_on:
            try:
                self.timeframe1.Show(True)
            except:
                pass


    def Closetime(self):
        try:
            self.timeframe1.Show(False)
        except:
            pass
        try:
            self.timeframe2.Show(False)
        except:
            pass

    def Confirmchoice(self,event):
        global e_on,enter_on
        con=self.confirm_choice.GetSelection()
        if con == 0:
            e_on=True
            enter_on=False
        elif con==1:
            e_on=False
            enter_on=True



    def Jiajia_time(self,event):
        global one_advance,one_delay,one_diff,one_time1,one_time2,one_real_time1,one_real_time2
        tem=self.jiajia_time.GetValue()
        templist=[40+i*0.1 for i in range(151)]
        if tem in templist:
            one_time1=tem
            one_time1=float(one_time1)
            one_real_time1 = self.gettime(one_time1)  # 计算得到的时间戳
        else:
            self.jiajia_time.SetValue(one_time1)


    def Jiajia_price(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist=[300+i*100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            one_diff=int(tem)
        else:
            self.jiajia_price.SetValue(one_diff)

#
    def Select_tijiao(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        select = self.select_tijiao.GetString(self.select_tijiao.GetSelection())
        if select == u"提前100":
            one_advance=100
        elif select == u"提前200":
            one_advance=200
        else:
            one_advance=0

    def Yanchi_time(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist=['0.%d' %i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            one_delay = float(tem)
        else:
            self.yanchi_time.SetValue(one_delay)

    def Tijiao_time(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2,one_real_time2
        tem=self.tijiao_time.GetValue()
        templist=[40+i*0.1 for i in range(171)]
        if tem in templist:
            one_time2=float(tem)
            one_real_time2 = self.gettime(one_time2)  # 计算得到的时间戳
        else:
            self.tijiao_time.SetValue(one_time2)
#双枪操作
    def Jiajia_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2,second_real_time1
        tem=self.jiajia_time2.GetValue()
        templist=[40+i*0.1 for i in range(151)]
        if tem in templist:
            second_time1=float(tem)
            second_real_time1 = self.gettime(second_time1)  # 计算得到的时间戳
        else:
            self.jiajia_time2.SetValue(second_time1)

    def Jiajia_price2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist=[300+i*100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            second_diff=int(tem)
        else:
            self.jiajia_price2.SetValue(second_diff)

    def Select_tijiao2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        select = self.select_tijiao2.GetString(self.select_tijiao2.GetSelection())
        if select == u"提前100":
            second_advance = 100
        elif select == u"提前200":
            second_advance = 200
        else:
            second_advance = 0


    def Yanchi_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        templist=['0.%d' %i for i in range(11)]  #符点数运算BUG
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            second_delay = float(tem)
        else:
            self.yanchi_time2.SetValue(second_delay)


    def Tijiao_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2,second_real_time2
        tem=self.tijiao_time2.GetValue()
        templist=[53+i*0.1 for i in range(41)]
        if tem in templist:
            second_time2=float(tem)
            second_real_time2 = self.gettime(second_time2)  # 计算得到的时间戳
        else:
            self.tijiao_time2.SetValue(second_time2)

##################
#重新绘制,面板刷新
    def Refresh_panel(self,event):
        #GetSelection 返回index
        global strategy_on #策略开启
        global twice,tijiao_num,chujia_on,tijiao_on,tijiao_OK,tijiao_one #二次出价触发开关
        stractagy_selection=self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice=False
            strategy_on=True
            chujia_on=True
            tijiao_on=False
            tijiao_num = 1  # 初始化
            tijiao_OK=False
            tijiao_one=False  #单枪未开

        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            strategy_on=True
            twice=True
            chujia_on=True
            tijiao_on=False
            tijiao_num=1  #初始化
            tijiao_OK=False
            tijiao_one = False  # 单枪未开
        else:
            self.none_show()
            strategy_on=False
            twice=False


    def ss_Shown(self): #双枪
        if not self.secondsizer_Shown:    #如果当前控件已隐藏
            self.vbox1.Show(self.secondshotSizer)    #打开双枪面板
            self.secondsizer_Shown = True    #服务器设置部分当前已隐藏
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)  #显示第一枪面板
            self.oneshotsizer_Shown=True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))  # 更新面板尺寸
        self.Secondshot_reset()
        self.Layout()

    def ss_Hide(self): #单枪
        if self.secondsizer_Shown:  # 如果当前控件已显示
            self.vbox1.Hide(self.secondshotSizer)    #如果当前控件已隐藏
            # self.setserverBtn.SetLabel(u'服务器设置↑')    #更新按钮标签
                #服务器设置部分当前已显示
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))  # 更新面板尺寸
        self.Oneshot_reset()
        self.Layout()

    def none_show(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)

        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()

    def Oneshot_reset(self):
        global one_time1,one_time2,one_diff,one_delay,one_advance
        self.jiajia_time.SetValue(48.0)
        self.tijiao_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_tijiao.SetSelection(0)
        self.yanchi_time.SetValue(0.5)

        one_time1 = 48  # 第一次出价加价
        one_time2 = 55  # 第一次出价提交
        one_diff = 700  # 第一次加价幅度
        one_delay = 0.5  # 第一次延迟
        one_advance = 100  # 第一次提交提前量
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)


    def Secondshot_reset(self):
        global one_time1,one_time2,one_diff,one_delay,one_advance
        global second_time1,second_time2,second_diff,second_delay,second_advance
        self.jiajia_time.SetValue(40.0)
        self.tijiao_time.SetValue(48.0)
        self.jiajia_price.SetValue(500)
        self.select_tijiao.SetSelection(2)
        self.yanchi_time.SetValue(0.0)

        self.jiajia_time2.SetValue(50.0)
        self.tijiao_time2.SetValue(55.5)
        self.jiajia_price2.SetValue(700)
        self.select_tijiao2.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)

        one_time1 = 40  # 第一次出价加价
        one_time2 = 48  # 第一次出价提交
        one_diff = 500  # 第一次加价幅度
        one_delay = 0.5  # 第一次延迟
        one_advance = 100  # 第一次提交提前量

        second_time1 = 50  # 第二次次出价加价
        second_time2 = 55.5  # 第二次出价提交
        second_diff = 700  # 第二次加价幅度
        second_delay = 0.5  # 第二次出价延迟
        second_advance = 100  # 第二次出价提交提前量
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)

# 定义策略保存
    def Strategy_save(self,event):
        dlg = wx.TextEntryDialog(None, '设定你的策略名称:', "策略保存", "策略1",
                                 style=wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            name = dlg.GetValue()
            if name:
                dlg_tip = wx.MessageBox('保存成功', '策略保存', wx.OK | wx.ICON_INFORMATION)
                if dlg_tip == wx.ID_OK:
                    dlg_tip.Destroy()
                    dlg.Destroy()
                self.save(name)
            else:
                dlg_tip=wx.MessageBox('名称不能为空', '策略保存', wx.OK | wx.ICON_ERROR)
                if dlg_tip == wx.ID_OK:
                    dlg_tip.Destroy()
                    dlg.Destroy()

    def save(self,name):
        global one_time1,one_time2,one_diff,one_delay,one_advance
        global second_time1,second_time2,second_diff,second_delay,second_advance
        global osl ,e_on,enter_on#策略存储容器

        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0]=0
            osl[1]=one_time1
            osl[2]=one_time2
            osl[3]=one_diff
            osl[4]=one_delay
            osl[5]=one_advance
            osl[6]=second_time1
            osl[7]=second_time2
            osl[8]=second_diff
            osl[9]=second_delay
            osl[10]=second_advance
            osl[11]=e_on
            osl[12]=enter_on
        elif self.select_stractagy.GetSelection() == 1:
            osl[0]=1
            osl[0]=1
            osl[1]=one_time1
            osl[2]=one_time2
            osl[3]=one_diff
            osl[4]=one_delay
            osl[5]=one_advance
            osl[6]=second_time1
            osl[7]=second_time2
            osl[8]=second_diff
            osl[9]=second_delay
            osl[10]=second_advance
            osl[11]=e_on
            osl[12]=enter_on
        with open('%s.strategy'%name,'wb') as spk:
            pickle.dump(osl,spk)

#输入框
    # def GetName(self):
    #     dlg = wx.TextEntryDialog(self.panel, '设定你的策略名称:', "策略保存", "策略1",
    #                              style=wx.OK)
    #     dlg.ShowModal()
    #     self.stractagyname.SetValue(dlg.GetValue())
    #     if dlg.ShowModal() == wx.ID_OK:
    #         response = dlg.GetValue()
    #         dlg.Destroy()

        #定义策略恢复


    def Strategy_load(self,event):
        import os
        path=os.getcwd()
        choice=self.findfiles(path)
        if choice:
            dlg = wx.SingleChoiceDialog(None, u"请选择策略:", u"策略载入",
                                       choices=choice)
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetStringSelection()  # 获取选择的内容
                dlg_tip = wx.MessageDialog(None, "载入成功", u"载入策略", wx.OK | wx.ICON_INFORMATION)
                if dlg_tip.ShowModal() == wx.ID_OK:
                    dlg_tip.Destroy()
                self.load(path)
            # print("载入")
            dlg.Destroy()
        else:
            dlg_tip = wx.MessageBox('找不到任何保存的策略', '策略载入', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
                dlg.Destroy()

    def load(self,path):
        global  osl,e_on,enter_on
        global one_time1, one_time2, one_diff, one_delay, one_advance
        global second_time1, second_time2, second_diff, second_delay, second_advance

        global strategy_on  # 策略开启
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one  # 二次出价触发开关
        global one_real_time1,one_real_time2,second_real_time1,second_real_time2
        try:
            with open(path,'rb') as loadstr:
                osl=pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:  #单次
            self.ss_Hide()


            twice = False
            strategy_on = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开

            self.select_stractagy.SetSelection(0)
            self.jiajia_time.SetValue(osl[1])
            self.tijiao_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_tijiao.SetSelection(0)
            elif osl[5] == 200:
                self.select_tijiao.SetSelection(1)
            else:
                self.select_tijiao.SetSelection(2)

            one_time1 = osl[1]  # 第一次出价加价
            one_time2 = osl[2]  # 第一次出价提交
            one_diff = osl[3]  # 第一次加价幅度
            one_delay = osl[4]  # 第一次延迟
            one_advance = osl[5]  # 第一次提交提前量
            #确认操作
            e_on=osl[11]
            enter_on=osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_real_time1 = self.gettime(one_time1)
            one_real_time2 = self.gettime(one_time2)
            second_real_time1 = self.gettime(second_time1)
            second_real_time2 = self.gettime(second_time2)

        elif osl[0] == 1:   #双枪
            strategy_on=True
            twice=True
            chujia_on=True
            tijiao_on=False
            tijiao_num=1  #初始化
            tijiao_OK=False
            tijiao_one = False  # 单枪未开
            self.ss_Shown()
            self.select_stractagy.SetSelection(1)
            self.jiajia_time.SetValue(osl[1])
            self.tijiao_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_tijiao.SetSelection(0)
            elif osl[5] == 200:
                self.select_tijiao.SetSelection(1)
            else:
                self.select_tijiao.SetSelection(2)
            self.jiajia_time2.SetValue(osl[6])
            self.tijiao_time2.SetValue(osl[7])
            self.jiajia_price2.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_tijiao2.SetSelection(0)
            elif osl[10] == 200:
                self.select_tijiao2.SetSelection(1)
            else:
                self.select_tijiao2.SetSelection(2)


            one_time1 = osl[1]  # 第一次出价加价
            one_time2 = osl[2]  # 第一次出价提交
            one_diff = osl[3]  # 第一次加价幅度
            one_delay = osl[4]  # 第一次延迟
            one_advance = osl[5]  # 第一次提交提前量

            second_time1 = osl[6]  # 第二次次出价加价
            second_time2 = osl[7]  # 第二次出价提交
            second_diff = osl[8]  # 第二次加价幅度
            second_delay =osl[9]  # 第二次出价延迟
            second_advance = osl[10]  # 第二次出价提交提前量
            #确认操作
            e_on=osl[11]
            enter_on=osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_real_time1 = self.gettime(one_time1)
            one_real_time2 = self.gettime(one_time2)
            second_real_time1 = self.gettime(second_time1)
            second_real_time2 = self.gettime(second_time2)

    def findfiles(self,path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.strategy':
                    L.append(os.path.join(root, file))
        return L

    def Save_info(self,event):
        pass


#############时间换算###############
# 转时间戳
    def changetime(self, a):  # 换算成时间戳
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time  # 以时间戳输出

    # 转字符串
    def get_nowtime(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a  # 输出时间格式字符串
        # 转为最终时间戳，调用这个时间

    def gettime(self,choice):  # choice1:55,choice2:0.5
        tem = self.get_nowtime()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.changetime(b) + float(choice)-int(choice)
        return c  # 得到用户所确定的最终时间戳

#################最低成交价显示##################
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
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


#--------------------------------------------------------------
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
    def __init__(self, name, user,psd):  ##########版本号
        wx.Frame.__init__(self, None, -1, name,size=(300, 240), style= wx.CAPTION | wx.CLOSE_BOX)
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
        self.sizer_v1.Add(self.welcomelabel,  flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # self.btnSizer = wx.StdDialogButtonSizer()
        self.userbox = wx.BoxSizer(wx.HORIZONTAL)
        self.userlabel = wx.StaticText(self.panel, -1, label="账号")
        self.userText = wx.TextCtrl(self.panel, -1,size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        self.userbox.Add(self.userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.userbox.Add(self.userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self.passbox = wx.BoxSizer(wx.HORIZONTAL)
        self.passlabel = wx.StaticText(self.panel, -1, label="密码")
        self.passText = wx.TextCtrl(self.panel, -1,size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
        self.passbox.Add(self.passlabel,  flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.passbox.Add(self.passText,  flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        if user:
            self.userText.SetValue(user)
        if psd:
            self.passText.SetValue(psd)
        self.sizer_v1.Add(self.userbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.sizer_v1.Add(self.passbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.userText)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.passText)

        self.monibtn = wx.Button(self.panel, -1, label="模拟",size=(90,30))
        self.loginbtn = wx.Button(self.panel, -1, label="登录",size=(90,30))
        self.btnSizer=wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.monibtn,flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.btnSizer.Add(self.loginbtn,flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.sizer_v1.Add(self.btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.loginbtn.Bind(wx.EVT_BUTTON,self.OnLogin,self.loginbtn)

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

        self.linkbox=wx.BoxSizer(wx.HORIZONTAL)
        self.linkbox.Add(self.purchaselink,flag=wx.ALIGN_LEFT|wx.RIGHT,border=20)
        self.linkbox.Add(self.helplink,flag=wx.ALIGN_RIGHT|wx.LEFT,border=20)
        self.sizer_v1.Add(self.linkbox,flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        self.SetSizer(self.sizer_v1)
        self.Center()  # 初始化居中

        pub.subscribe(self.connect_success, "connect")
        # pub.subscribe(self.connect_failure, "connect failure")

        self.hashthread=HashThread()

    def connect_success(self):
        self.loginbtn.Enable()
        global login_result
        if login_result=='login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)
            # event.Skip()
        elif login_result=='net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result=='repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result=='wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result=='wrong password':
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

    def OnLogin(self,event):
        global Username,Password
        username=self.userText.GetValue()
        password=self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
            # loginthread=TestThread()
        else:
            Username=username     #保存用户输入的账号密码
            Password=password
            self.loginthread=LoginThread()
            namepsd=[username,password]
            with open('your.name','wb') as userfile:
                pickle.dump(namepsd,userfile)
            # self.loginBtn.setlabel(u"登录中")
            event.GetEventObject().Disable()

    def Purchase(self,event):
        print("购买")



class UserValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''
    #----------------------------------------------------------------------
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    #----------------------------------------------------------------------
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)

    #----------------------------------------------------------------------
    def Validate(self, win):
        return True

    #----------------------------------------------------------------------
    def TransferToWindow(self):
        return True

    #----------------------------------------------------------------------
    def TransferFromWindow(self):
        return True

    #----------------------------------------------------------------------
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
#时间进程
class TimeThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)     #启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread
    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        global a_time,moni_second
        for i in range(1000000):
            a=time.clock()
            time.sleep(0.1)
            b=time.clock()
            a_time+=b-a  #实际运行时间作为真实间隔
            moni_second += b-a
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

#---------------------------------------
#创建hash进程，初始化
class OpenwebThread(Thread):
    def __init__(self,url):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.url=url
        self.setDaemon(True)     #启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread
    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        openweb(self.url)

class HashThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)     #启动进程之前选择，主进程关闭，子进程跟着关闭
        self.start()  # start the thread
    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        Create_hash()
        getwebpath()  #初始化浏览器地址
        # wx.Sleep(15)
        # TopFrame.Refresh_hash()


#创建一个确认进程
class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        findpos()

#创建一个确认进程
class confirmThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        global confirm_need, confirm_on
        global confirm_need, confirm_on ,confirm_one,chujia_on
        for i in range(100):
            wx.Sleep(0.1)
            # print(confirm_need)
            if confirm_need:
                # print("开启查找")
                findconfirm()
                if confirm_on:
                    TopFrame.OnClick_confirm()
                    confirm_need=False
                    confirm_on=False
                    confirm_one=False
                    chujia_on=True
        confirm_one = False #进程结束的时候允许
#创建一个刷新进程
class refreshThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        global confirm_need, confirm_on
        global refresh_need, refresh_on,refresh_one
        for i in range(60):
            if refresh_need:
                findrefresh()
                if refresh_on:
                    TopFrame.OnClick_Shuaxin()  # 刷新验证码
                    refresh_on = False
                    refresh_need = False
                    refresh_one=False
        refresh_one=False  #进程结束的时候允许


# ----------------------------------------------------------------------
#登录验证器
class LoginThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread
    # ----------------------------------------------------------------------
    def run(self):
        # self.controlthread=controlThread()
        global Username,login_result
        login_result=ConfirmUser()
        print(login_result)
        logging.info("%s"%login_result)
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


#----------------------------------------------------------------------
#自动出价触发器
#国拍出价
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        global tijiao_delay,final_tijiao,strategy_price,lowest_price,own_price1,own_price2
        global moni_second,strategy_on,moni_on,tijiao_on,tijiao_OK,second_real_time1,second_real_time2
        global one_advance,second_advance,tijiao_num,tijiao_OK,chujia_on,tijiao_on,tijiao_one
        for i in range(10000000):
            time.sleep(0.1)  #间隔0.1秒判断一次
            # print(tijiao_on,strategy_on,guopai_on)
            # print(a_time, final_tijiao)
            #触发提交
            if tijiao_on and strategy_on and guopai_on  and tijiao_OK :     #判断是否需要提交,国拍开启状态方可触发
                # print(a_time,final_tijiao)
                if tijiao_num == 1 and a_time>=one_real_time2 and not tijiao_one:  #判断是否满足条件
                    tijiao_on=False
                    TopFrame.OnClick_Tijiao()     #调用方法
                    tijiao_on=False
                    logging.info("Rone_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rone_tijiao %s%s%s" % (tijiao_num, a_time, one_real_time2))
                    tijiao_one=True
                elif tijiao_num == 2 and a_time >= second_real_time2:  # 判断是否满足条件
                    tijiao_on = False
                    TopFrame.OnClick_Tijiao()  # 调用方法
                    tijiao_on = False
                    logging.info("Rsecond_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rsecond_tijiao %s%s%s" % (tijiao_num, a_time, second_real_time2))
                elif tijiao_num ==1 and   lowest_price >= own_price1-300-one_advance and not tijiao_one:  # 价格判断
                    tijiao_on = False
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    TopFrame.OnClick_Tijiao()  # 调用方法
                    logging.info("Rone_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rone_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price1))
                    tijiao_one = True
                elif tijiao_num == 2 and lowest_price >= own_price2-300-second_advance:  # 价格判断
                    tijiao_on = False
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    TopFrame.OnClick_Tijiao()  # 调用方法
                    logging.info("Rsecond_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rsecond_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price2))
            #触发出价
            if  strategy_on and guopai_on and chujia_on:  # 判断是否需要提交,国拍开启状态方可触发
                # print(a_time,final_tijiao)
                if tijiao_num == 1 and  one_real_time1<=a_time<=one_real_time1+0.2:  # 判断是否满足条件
                    TopFrame.OnClick_chujia()  # 调用出价
                    own_price1=lowest_price+one_diff
                    tijiao_on=True   #
                    logging.info("Rone_chujia %s%s" %(strategy_on,guopai_on))
                    logging.info("Rone_chujia %s%s" %(one_time1,one_real_time1))
                if tijiao_num == 2 and twice and   second_real_time1<=a_time:  # 判断是否满足条件
                    TopFrame.OnClick_chujia()  # 调用出价
                    own_price2=lowest_price+second_diff
                    tijiao_on=True
                    logging.info("Rsecond_chujia %s%s" % (strategy_on, guopai_on))
                    logging.info("Rsecond_chujia %s%s" % (second_time1, second_real_time1))


#模拟出价
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        global moni_second,strategy_on,moni_on,tijiao_on,own_price1,own_price2,one_diff,second_diff
        global tijiao_num, tijiao_OK,one_advance,second_advance,tijiao_one
        for i in range(10000000):
            time.sleep(0.1)  #间隔0.1秒判断一次

            if tijiao_on and strategy_on and moni_on and tijiao_OK :     #判断是否需要提交，模拟开启方可触发
                # print(tijiao_on, strategy_on, moni_on, tijiao_OK)
                # print(tijiao_num,moni_second,one_time2,tijiao_one)
                # print(lowest_price, own_price1, own_price2)
                if tijiao_num == 1 and moni_second>=one_time2 and not tijiao_one:  #判断是否满足条件
                    TopFrame.OnClick_Tijiao()     #调用方法
                    logging.info("moni one_tijiao %s %s %s %s" % (tijiao_on,strategy_on, moni_on,  tijiao_OK))
                    logging.info("moni one_tijiao %s %s %s" % (tijiao_num, moni_second, one_time2))
                    tijiao_on=False
                    tijiao_one=True #第一枪已开
                elif tijiao_num == 2 and moni_second>= second_time2 and twice:  # 判断是否满足条件
                    TopFrame.OnClick_Tijiao()  # 调用方法
                    logging.info("moni1 second_tijiao %s %s %s %s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni second_tijiao %s %s %s" % (tijiao_num, moni_second, second_time2))
                    tijiao_on = False
                elif tijiao_num ==1 and   lowest_price >= own_price1-300-one_advance and  not tijiao_one:  # 价格判断
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    TopFrame.OnClick_Tijiao()  # 调用方法
                    logging.info("moni one_tijiao %s %s %s %s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni one_tijiao %s %s %s" % (tijiao_num, lowest_price, own_price1))
                    tijiao_one = True  # 第一枪已开
                elif tijiao_num == 2 and lowest_price >= own_price2-300-second_advance and twice:  # 价格判断
                    tijiao_on = False  # 执行提交之后只能通过选择进程开启自动提交
                    TopFrame.OnClick_Tijiao() # 调用方法
                    logging.info("moni2 second_tijiao %s%s%s%s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni second_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price2))
            #触发出价
            # print(strategy_on,moni_on)
            # print(strategy_on, moni_on, chujia_on)
            # print(twice, second_time1, moni_second)
            if strategy_on and moni_on and chujia_on :  # 判断是否需要出价,模拟开启方可触发
                if tijiao_num == 1 and  one_time1<=moni_second<=one_time1+0.2:   # 判断是否满足条件
                    TopFrame.OnClick_chujia()  # 调用方法
                    # print("第一次")
                    own_price1=lowest_price+one_diff
                    tijiao_on=True
                    logging.info("moni one_chujia %s %s" %(strategy_on,moni_on))
                    logging.info("moni one_chujia %s %s" %(one_time1,moni_second))
                elif tijiao_num == 2 and  twice and  second_time1<moni_second:
                    TopFrame.OnClick_chujia()  # 调用方法
                    # print("第二次")
                    own_price2=lowest_price+second_diff
                    tijiao_on=True
                    logging.info("moni second_chujia %s %s" %(strategy_on,moni_on))
                    logging.info("moni second_chujia %s %s" %(second_time1,moni_second))


class Infoframe(wx.Frame):
    def __init__(self, name, user,psd):  ##########版本号
        wx.Frame.__init__(self, None, -1, name,size=(300, 240), style= wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)


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
            psd = 0
        loginframe = LoginFrame('小鲜肉拍牌', user, psd)
        loginframe.Show(True)
        return True


if __name__ == '__main__':
    app = SketchApp()

    app.MainLoop()


# self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)