'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
version = '5.1'
num = 0
avt = 90100
test = False
host_ali = "http://hupai.pro"
url1 = "http://moni.51hupai.org/"
url2 = "www.baidu.com"      
url3 = "www.baidu.com"       
url4 = "http://127.0.0.1:5000/Moni"
mainicon = 'ico.ico'
view = False        
do = False        
o0000ooooooo0oo00oo00 = False        
o0000oo0ooo0oo000o00o = False             
o00ooo00oo0oo0oo0o000 = False              
oooo00ooo00o0oo0o0ooo = True            
o00000oo000ooooo00ooo = True          
oooo00000o0o0oooooo0o = 0                              
o000ooo0000oo0o0ooooo = False          
oo0oo0ooo0oo0oo0000oo = 0               
oo00o00o000o000oo0oo0 = 0               
web_on = False             
ooo00ooooo0o00ooo00o0 = False           
operation_show = False           
o00oo0oo0000ooo00oooo = False               
import time
oo000000oooo0oo00oo00 = time.time()          
b_time = 0          
moni_minute = 29
oo0oo0ooo000000oo0000 = 0
o00o0ooooooo0oo0ooo00_time = 0        
ooo0000oo00ooooo00oo0 = 0       
ooo00000o0oo0oooooo0o = 0      
ooo0o0000oo0oo0o00ooo = False                          
oooo000000o00o00oo0oo = False
oo000oo0oo0000o00oo00 = 53          
o00oo0o0o000oo000oooo = 0.0          
oo00ooo0oo000o0oo0000 = True          
o0oo000oooo0o00oo0oo0 = False                 
delay = False        
delay_time = 0.5          
oo00oooo0o00oooo0o0o0 = False          
oooo0oo0ooooooo000o0o = True           
pricelist = [80000 + i * 100 for i in range(400)]          
IDnumber = 0        
account = 0       
passwd = 0      
o0ooo000ooooooo0o000o = 0
import pyautogui as pg
def o00oo00oooooo000o0o0o():
    with open('dick.dl', 'rb') as dick:
        global oo0ooo0000oo0o00o0o00
        oo0ooo0000oo0o00o0o00 = pickle.load(dick)                 
    with open('cf.btn', 'rb') as cf:
        global ooo00oo0000o00o0oo0oo
        ooo00oo0000o00o0oo0oo = pickle.load(cf)                            
    with open("target.tkl", 'rb')  as tar:
        global ooo0oo00ooo0o00000000
        ooo0oo00ooo0o00000000 = pickle.load(tar)            
o00o00o00000ooooo0o0o = 48           
o0000ooo00oo000o0o00o = 55           
o0ooo0oo000oo00o000o0 = 1000000000000             
ooo00oo0000o00o0o00o0 = 1000000000000             
oo0oo00ooooo0000o00o0 = 700           
o00000o0o0ooo0o0o0oo0 = 0.5         
o0ooo0o00o0o00000ooo0 = 100            
o000o000o0000ooo0o0o0 = 48            
ooooo0o000oooo0o0ooo0 = 55           
o00oo0oo0o0ooooooo0oo = 1000000000000             
oo00ooo0o0o00o0oo0oo0 = 1000000000000             
ooo0ooooo0o000oo0ooo0 = 600           
o0o00oooo0o0ooo000oo0 = 0.5           
oo0oo0oooo0ooo0oo0000 = 100              
osl = [0] * 15                          
o0o0000oo000o00o0o0o0 = True                      
ooo0ooo0o000o00oo000o = False                  
o0oo0ooo0o00oo00o0o00 = 93400         
oo000oo00o0oo0o0000oo = 0         
oooooo0o0000o0o0oo0o0 = 0         
own_price = 0        
oo0000o00o0000oo00oo0 = False           
e_on = True                  
o0ooo000o00oo0oooo0o0 = False                   
twice = False          
o0000ooo000000ooo00o0 = 1                         
ooo0ooo0o000o00oo000oe = False             
websize = [902, 700]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2          
Py2 = Pxy[1] / 2
Px = (Pxy[0] - websize[0]) / 2 - 80
Py = (Pxy[1] - websize[1]) / 2
P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]]               
P_relative2 = [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
oo0o0oo0o0o0oo00o0oo0 = [[0, 0] for i in range(len(P_relative))]
for i in range(len(oo0o0oo0o0o0oo00o0oo0)):
    oo0o0oo0o0o0oo00o0oo0[i][0] = Px1 + P_relative[i][0]
    oo0o0oo0o0o0oo00o0oo0[i][1] = Py2 + P_relative[i][1]
px_ajust, py_ajust = 0, 0
for i in range(len(P_relative)):
    P_relative[i][0] += websize[0] / 2 + px_ajust
    P_relative[i][1] += websize[1] / 2 + py_ajust      
px_price = 770 - 171
py_price = 260
px_priceframe = 220 - 191
py_priceframe = 480
px_timeframe = 22
py_timeframe = 350
o0oo00oooooo0ooo00oooframe = 245
o0oooo0000oo00000o00oframe = 290
ooo00o0oo00oo0ooo0o00frame_pos = [o0oo00oooooo0ooo00oooframe, o0oooo0000oo00000o00oframe]
px_o00ooo00000o00000o00oframe = 400 - 215
py_o00ooo00000o00000o00oframe = 460
px_mini = 200
py_mini = 40
o0o0000ooooo00oo0oo00 = [400, 80]
o0o0000ooo0oo00ooo0o0 = [400, 220]
Timesize = [200, 50]
ooo00o0oo00oo0ooo0o00_area = [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py]
o00o0000o000000o000o0 = [396 - 150, 11 - 100, 396 + 150, 11 + 100]
o00000o0oo0oooo00oo00 = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
o0o0000oo000000o00000 = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
o000000o00000o0o000oo = [0,0]
webview_pos = [-25,0]                      
Px_price = Px + px_price
Py_price = Py + py_price
Pos_price = [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini]               
o00o0oo0oo0oo0ooooo00 = []           
Px_priceframe = Px + px_priceframe
Py_priceframe = Py + py_priceframe
Pos_priceframe = [Px_priceframe, Py_priceframe]
Px_timeframe = px_timeframe + Px
Py_timeframe = py_timeframe + Py
o000o0o00o0oooo0ooo00 = [Px_timeframe, Py_timeframe]
o00ooo00oooo0ooo00ooo = [Px + 40, Py + 480]
Px_o00ooo00000o00000o00oframe = Px + px_o00ooo00000o00000o00oframe
Py_o00ooo00000o00000o00oframe = Py + py_o00ooo00000o00000o00oframe
o00o0oo0oo0oo0ooooo00frame = [Px_o00ooo00000o00000o00oframe, Py_o00ooo00000o00000o00oframe]
o0oo00oooooo0ooo00ooo = 0                         
o0oooo0000oo00000o00o = 0            
ooo0o00oooo00000o0ooo = Px + o0oo00oooooo0ooo00ooo
o0ooooo000o0o00oooooo = Py + o0oooo0000oo00000o00o
ooo00o0oo00oo0ooo0o00_sizex = 82           
ooo00o0oo00oo0ooo0o00_sizey = 16
oo0000o0oo00ooooooooo =ooo0o00oooo00000o0ooo-25             
o0oo0oo0ooo0o00000o0o = o0ooooo000o0o00oooooo+17
currenttime_sizex = 132
currenttime_sizey = 16
o0000o0o0o00000o0oo00 = 49                
o00o0oo0000oo0oo0000o = 0
px_confirm = 656
py_confirm = 475
Px_confirm = Px + px_confirm
Py_confirm = Py + py_confirm
confirm_sizex = 113
confirm_sizey = 28
oo0oooo0000oo00oooooo = False          
oo00ooo0o0oo00oo000oo = False          
oo0oooo0000oo00ooooooe = False             
px_o0oo0o0oo000ooo0ooooo = 550
py_o0oo0o0oo000ooo0ooooo = 413
Px_o0oo0o0oo000ooo0ooooo = Px + px_o0oo0o0oo000ooo0ooooo
Py_o0oo0o0oo000ooo0ooooo = Py + py_o0oo0o0oo000ooo0ooooo
o0oo0o0oo000ooo0ooooo_sizex = 108
o0oo0o0oo000ooo0ooooo_sizey = 21
o0o0o00o00oo0o0oo0000 = False          
oo0oo0oo0oo00o00o000o = False          
oooo0000oooo0ooo0000o = False             
oooo00o0oooo00000000o = False        
ooo0oo0o000000o00oooo_interval = False        
o00000ooo00000ooo0000 = False      
o00ooo00o0oo0o0oo0ooo = False            
import numpy as np
o0oooo0oo00o00o0000oo = [ooo0o00oooo00000o0ooo - 10, o0ooooo000o0o00oooooo - 100, ooo0o00oooo00000o0ooo + 600, o0ooooo000o0o00oooooo + 120]
oo0000o00o0o0000o00o0 = []
nptemp = []
ooooo00oo000oo0ooooo0 = np.array(nptemp)       
o00000ooo00o000oooo00 = np.array(nptemp)       
o0o000o0o0o000o0o0o00 = np.array(nptemp)         
impos_o00ooo00000o00000o00o = np.array(nptemp)       
o0oo0000ooooo00o00oo0confirm = np.array(nptemp)         
oo0oooo0o00o0ooooooo0 = np.array(nptemp)        
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
import imagehash
import logging
timenow = time.time()
time_local = time.localtime(timenow)
myapplog = time.strftime("%Y%m%d%H%M%S", time_local)
print(myapplog)            
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%s.log' % myapplog,
                    filemode='w')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
import win32gui, win32api
import cv2
from PIL import ImageGrab
yimg = ImageGrab.grab().save("o00ooo00000o00000o00o.png")
o0o0ooooo0oo0o00o0000 = Image.open("o00ooo00000o00000o00o.png")                         
def Click(x, y):        
    a = win32gui.GetCursorPos()
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
def Click2(x, y):        
    a = win32gui.GetCursorPos()
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos(a)
import win32clipboard
def Paste():            
    win32api.keybd_event(17, 0, 0, 0)               
    win32api.keybd_event(86, 0, 0, 0)            
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)        
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
def oo0o00o0ooo0o00oooooo():
    win32api.keybd_event(17, 0, 0, 0)               
    win32api.keybd_event(86, 0, 0, 0)            
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)        
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
def oooooo0o0oooo0o0o0o0o():
    sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    global ooo0oo00ooo0o00000000
    template = ooo0oo00ooo0o00000000[2]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    global o0oo00oooooo0ooo00ooo, o0oooo0000oo00000o00o, o0000o0o0o00000o0oo00, o00o0oo0000oo0oo0000o, ooo0o00oooo00000o0ooo, o0ooooo000o0o00oooooo, Px, Py
    global o00o0000o000000o000o0, o00000o0oo0oooo00oo00, o000o0o00o0oooo0ooo00, o00ooo00oooo0ooo00ooo, o00o0oo0oo0oo0ooooo00, o00o0oo0oo0oo0ooooo00frame, o0o0000oo000000o00000
    global oo0000o00o0o0000o00o0, o0oooo0oo00o00o0000oo          
    global oo0o0oo0o0o0oo00o0oo0, o00o0000o000000o000o0, o00000o0oo0oooo00oo00, o000o0o00o0oooo0ooo00, o00ooo00oooo0ooo00ooo, o00o0oo0oo0oo0ooooo00, o00o0oo0oo0oo0ooooo00frame, o0o0000oo000000o00000
    global oo0000o0oo00ooooooooo,o0oo0oo0ooo0o00000o0o           
    global o000000o00000o0o000oo
    if max_val > 0.9:          
        o0oo00oooooo0ooo00ooo = max_loc[0] + o0000o0o0o00000o0oo00
        o0oooo0000oo00000o00o = max_loc[1] + o00o0oo0000oo0oo0000o
        ooo0o00oooo00000o0ooo = o0oo00oooooo0ooo00ooo
        o0ooooo000o0o00oooooo = o0oooo0000oo00000o00o
        oo0000o0oo00ooooooooo = ooo0o00oooo00000o0ooo -27             
        o0oo0oo0ooo0o00000o0o = o0ooooo000o0o00oooooo -16
        o000000o00000o0o000oo = [o0oo00oooooo0ooo00ooo-9,o0oooo0000oo00000o00o+84]
        for i in range(len(oo0o0oo0o0o0oo00o0oo0)):
            oo0o0oo0o0o0oo00o0oo0[i][0] = ooo0o00oooo00000o0ooo + P_relative2[i][0]
            oo0o0oo0o0o0oo00o0oo0[i][1] = o0ooooo000o0o00oooooo + P_relative2[i][1]
        o00o0000o000000o000o0 = [396 - 150 + ooo0o00oooo00000o0ooo, 11 - 100 + o0ooooo000o0o00oooooo, 396 + 150 + ooo0o00oooo00000o0ooo,
                        11 + 100 + o0ooooo000o0o00oooooo]
        o00000o0oo0oooo00oo00 = [505 - 80 + ooo0o00oooo00000o0ooo, 68 - 50 + o0ooooo000o0o00oooooo, 505 + 80 + ooo0o00oooo00000o0ooo,
                        68 + 50 + o0ooooo000o0o00oooooo]
        o0o0000oo000000o00000 = [205 - 80 + ooo0o00oooo00000o0ooo, 68 - 50 + o0ooooo000o0o00oooooo, 405 + 80 + ooo0o00oooo00000o0ooo,
                            68 + 50 + o0ooooo000o0o00oooooo]
        o00ooo00oooo0ooo00ooo = [192 - 344 + ooo0o00oooo00000o0ooo, 514 - 183 + o0ooooo000o0o00oooooo]
        o00o0oo0oo0oo0ooooo00 = [oo0o0oo0o0o0oo00o0oo0[5][0] - 277, oo0o0oo0o0o0oo00o0oo0[5][1] - 65, oo0o0oo0o0o0oo00o0oo0[5][0] - 97,
                          oo0o0oo0o0o0oo00o0oo0[5][1] + 45]           
        o00o0oo0oo0oo0ooooo00frame = [ooo0o00oooo00000o0ooo + 297, o0ooooo000o0o00oooooo - 283]            
        global oooo0oo0ooooooo000o0o, o00000oo000ooooo00ooo
        oooo0oo0ooooooo000o0o = False        
        o00000oo000ooooo00ooo = True        
        lowest = [ooo0o00oooo00000o0ooo, o0ooooo000o0o00oooooo,  ooo00o0oo00oo0ooo0o00_sizex+ooo0o00oooo00000o0ooo, ooo00o0oo00oo0ooo0o00_sizey+o0ooooo000o0o00oooooo]
        currenttime = [oo0000o0oo00ooooooooo,o0oo0oo0ooo0o00000o0o,oo0000o0oo00ooooooooo+currenttime_sizex,o0oo0oo0ooo0o00000o0o+currenttime_sizey]
        dis_x=50
        dis_y=100
        x1 = ooo0o00oooo00000o0ooo - dis_x         
        y1 = o0ooooo000o0o00oooooo - dis_y
        cal_area = [lowest, o00o0000o000000o000o0, o00000o0oo0oooo00oo00, o00o0oo0oo0oo0ooooo00, o0o0000oo000000o00000 , currenttime]          
        oo0000o00o0o0000o00o0 = []
        o0oooo0oo00o00o0000oo = [ooo0o00oooo00000o0ooo - dis_x, o0ooooo000o0o00oooooo - dis_y, ooo0o00oooo00000o0ooo + 600, o0ooooo000o0o00oooooo + 120]
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            oo0000o00o0o0000o00o0.append(temp)
def ooo0000oo0oo0o00o0o00(area):                          
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
    im = dataBitMap.GetBitmapBits(True)                    
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
def cut_img():                                                                                   
    global oo0000o00o0o0000o00o0, o0oooo0oo00o00o0000oo, ooooo00oo000oo0ooooo0, o0oo0000ooooo00o00oo0, o00000ooo00o000oooo00, o0o000o0o0o000o0o0o00, o0oo0000ooooo00o00oo0confirm,oo0oooo0o00o0ooooooo0
    img = ooo0000oo0oo0o00o0o00(o0oooo0oo00o00o0000oo)           
    img = np.asarray(img)              
    ooooo00oo000oo0ooooo0 = img[oo0000o00o0o0000o00o0[0][1]:oo0000o00o0o0000o00o0[0][3], oo0000o00o0o0000o00o0[0][0]:oo0000o00o0o0000o00o0[0][2]]      
    o00000ooo00o000oooo00 = img[oo0000o00o0o0000o00o0[1][1]:oo0000o00o0o0000o00o0[1][3], oo0000o00o0o0000o00o0[1][0]:oo0000o00o0o0000o00o0[1][2]]      
    o0o000o0o0o000o0o0o00 = img[oo0000o00o0o0000o00o0[2][1]:oo0000o00o0o0000o00o0[2][3], oo0000o00o0o0000o00o0[2][0]:oo0000o00o0o0000o00o0[2][2]]
    o0oo0000ooooo00o00oo0 = img[oo0000o00o0o0000o00o0[3][1]:oo0000o00o0o0000o00o0[3][3], oo0000o00o0o0000o00o0[3][0]:oo0000o00o0o0000o00o0[3][2]]      
    o0oo0000ooooo00o00oo0confirm = img[oo0000o00o0o0000o00o0[4][1]:oo0000o00o0o0000o00o0[4][3], oo0000o00o0o0000o00o0[4][0]:oo0000o00o0o0000o00o0[4][2]]      
    oo0oooo0o00o0ooooooo0 = img[oo0000o00o0o0000o00o0[5][1]:oo0000o00o0o0000o00o0[5][3], oo0000o00o0o0000o00o0[5][0]:oo0000o00o0o0000o00o0[5][2]]
def oo0000o00000000o0oo00():
    global ooo0oo00ooo0o00000000, o0o0o00o00oo0o0oo0000, oo0oo0oo0oo00o00o000o, oooo0000oooo0ooo0000o, oo0o0oo0o0o0oo00o0oo0, o00o0000o000000o000o0, o00000o0oo0oooo00oo00
    template = ooo0oo00ooo0o00000000[0]
    global o00000ooo00o000oooo00
    sc = o00000ooo00o000oooo00
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    logging.info("查找刷新")
    if max_val >= 0.8:
        logging.info("刷新")
        TopFrame.o0oo00o0o000o0oo00o00()
        global o00ooo00oo0oo0oo0o000, oooo00ooo00o0oo0o0ooo, oo00o00o000o000oo0oo0
        o00ooo00oo0oo0oo0o000 = True         
        oo00o00o000o000oo0oo0 = 0      
def oo0oooooo0o0000000o00():
    global ooo0oo00ooo0o00000000, oo0oooo0000oo00oooooo, oo0o0oo0o0o0oo00o0oo0
    template = ooo0oo00ooo0o00000000[1]
    global o0o000o0o0o000o0o0o00
    sc = o0o000o0o0o000o0o0o00
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.9:
        TopFrame.oo00o0oo0o0o00o00oo0o()
    if oo0oooo0000oo00oooooo and max_val < 0.9:
        print("暂停确认")
def o0o00oo00oo0oo0o000o0():
    global ooo0oo00ooo0o00000000, oo0oooo0000oo00oooooo, oo0o0oo0o0o0oo00o0oo0, o00ooo00oo0oo0oo0o000, oooo00ooo00o0oo0o0ooo
    template = ooo0oo00ooo0o00000000[1]
    global o0oo0000ooooo00o00oo0confirm
    sc = o0oo0000ooooo00o00oo0confirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.9:
        o00ooo00oo0oo0oo0o000 = False
        oooo00ooo00o0oo0o0ooo = True
def cut_pic(img, size, name):
    img = np.asarray(img)
    i1 = img[0:24, :150]
    i2 = img[48:110, 30:]
    im = np.concatenate([i2, i1])
    im = cv2.resize(im, tuple(size))
    cv2.imwrite(name, im)
import win32gui
import win32ui
import win32con
import time
def o00o00000oo0o00o0oooo(area):                          
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
    im = dataBitMap.GetBitmapBits(True)                    
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
def o00o00000oo0o00o0oooo_getimg(area, size, name):
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
    im = dataBitMap.GetBitmapBits(True)                    
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
bin_n = 16                  
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n * ang / (2 * np.pi))                                    
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)                           
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
import copy
def readpic(img):
    svm = cv2.ml.SVM_load('maindata.xml')
    testData = cut(img)
    testData = list(map(hog, testData))
    testData = np.float32(testData).reshape(-1, 64)
    result = svm.predict(testData)
    result = result[1].reshape(-1).astype(int).astype(str)
    for i in range(len(result)):
        if result[i] == '11':
            result[i] = ':'
    price = "".join(list(result))
    print("price==",price)
    return price                          
def timeset():
    global oo000000oooo0oo00oo00, oo0oooo0o00o0ooooooo0, oo0oo0ooo000000oo0000
    currenttime = cv2.cvtColor(oo0oooo0o00o0ooooooo0, cv2.COLOR_BGR2GRAY)
    currenttime = readpic(currenttime)           
    cv2.imwrite("zp.png", oo0oooo0o00o0ooooooo0)
    print(currenttime)
    tem1 = time.time()
    a = time.strftime('%Y-%m-%d', time.localtime(tem1))
    b = a + ' ' + currenttime
    oo000000oooo0oo00oo00 = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')) + 0.5                 
    try:
        oo0oo0ooo000000oo0000 = int(currenttime.split(':')[2]) + 0.5
    except:
        pass
import winreg, re, subprocess
oo000o0ooo000o00o0000 = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'
def o0o000o000oo00o0000oo():
    global oo000o0ooo000o00o0000
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            oo000o0ooo000o00o0000 = result[0]
    except:
        pass
    if not os.path.exists(oo000o0ooo000o00o0000):
        if os.path.exists('C:\Program Files (x86)'):
            pass
def openweb(url):
    global oo000o0ooo000o00o0000
    subprocess.Popen([oo000o0ooo000o00o0000, url])
def openIE(url):
    global iepath
    subprocess.Popen([iepath, url])
import smtplib
from email.mime.text import MIMEText
import os
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
from threading import Thread
import threading
from wx.lib.pubsub import pub                
import socket, sys, json
timeout = 10
socket.setdefaulttimeout(timeout)          
from urllib import request
import json
def o000oo0oooo00o0000oo0():
    try:
        target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % ooo0000oo00ooooo00oo0 + '&' + 'passwd=%s' % ooo00000o0oo0oooooo0o
        print(target_url)
        response = request.urlopen(target_url)
        print(response)
        result = response.read()
        result = str(result, encoding='utf-8')
        result = json.loads(result)
    except:
        return {'result': 'net error'}
    return result
def Logout():
    host = host_ali
    port = 8080
    global ooo0000oo00ooooo00oo0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
def o000000000o0ooooo0oo0():
    host = host_ali
    port = 8080
    global ooo0000oo00ooooo00oo0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
    data = ['keep', ooo0000oo00ooooo00oo0, ooo00000o0oo0oooooo0o]
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")           
    logging.info('发送信息 %s' % str(data, encoding="utf-8"))
    s.send(data)
    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")
def oo00oo0o000o000oo000o(subject, to_list, file_name):
    data = open(file_name, 'rb')
    ctype, encoding = mimetypes.guess_type(file_name)
    if ctype is None and encoding is None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = email.mime.base.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.encoders.encode_base64(file_msg)
    basename = os.path.basename(file_name)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    to_list = to_list
    mail_host = 'smtp.qq.com'
    mail_user = os.environ.get('MAIL_USERNAME')
    mail_pass = os.environ.get('MAIL_PASSWORD')
    me = mail_user
    msg = MIMEMultipart()
    msg.attach(file_msg)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    server = smtplib.SMTP_SSL(mail_host, 465)                       
    server.login(mail_user, mail_pass)
    print('login in  successfully')
    server.sendmail(me, to_list, msg.as_string())
    server.quit()
    print('send email  successfully')
def Upload():
    pass                 
def o0000o00000oo00o0o0oo():
    pass
def o00o0oo000o0o00o0ooo0():
    pass
class TopFrame(wx.Frame):
    def __init__(self, name, rev):               
        wx.Frame.__init__(self, None, 1, name,
                          size=(280, 300), pos=(Px - 120, Py), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.statusbar.SetStatusText(u"版本号", 0)
        self.statusbar.SetStatusText(u"%s" % rev, 1)
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        self.statusbar.SetBackgroundColour((240, 255, 255))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour((240, 255, 255))
        self.SetBackgroundColour((240, 255, 255))
        self.operationarea = wx.StaticBox(panel, label="基本功能")
        self.operationareasizer = wx.StaticBoxSizer(self.operationarea, wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.monibutton = wx.Button(panel, label='打开模拟')
        self.Bind(wx.EVT_BUTTON, self.ooo000o00ooo00oooo00o, self.monibutton)
        self.o00o0o00o00oo0000o0o0button = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.ooo0000oooo0o0o0o0oo0, self.o00o0o00o00oo0000o0o0button)
        self.hbox1.Add(self.monibutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.o00o0o00o00oo0000o0o0button, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox1)
        self.helpbutton = wx.Button(panel, label='查看帮助')
        self.Bind(wx.EVT_BUTTON, self.help, self.helpbutton)
        self.rulebutton = wx.Button(panel, label='查看规定')
        self.Bind(wx.EVT_BUTTON, self.rule, self.rulebutton)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2.Add(self.helpbutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox2.Add(self.rulebutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox2)
        self.set = wx.StaticBox(panel, label="常规设置")
        self.setsizer = wx.StaticBoxSizer(self.set)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.advanceset = wx.Button(panel, label='策略设置')
        self.posautoset = wx.Button(panel, label='刷新定位')
        self.Bind(wx.EVT_BUTTON, self.ooo0ooo00o0oooo0o0ooo, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.o00o0o0o000000oo0o000, self.posautoset)
        self.hbox3.Add(self.advanceset, 0, wx.ALL | wx.CENTER, 5)
        self.hbox3.Add(self.posautoset, 0, wx.ALL | wx.CENTER, 5)
        self.hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.highadvanceset = wx.Button(panel, label='动态策略')
        self.timeautoreset = wx.Button(panel, label='时间同步')
        self.hbox4.Add(self.highadvanceset, 0, wx.ALL | wx.CENTER, 5)
        self.hbox4.Add(self.timeautoreset, 0, wx.ALL | wx.CENTER, 5)
        self.vbox_setting = wx.BoxSizer(wx.VERTICAL)
        self.vbox_setting.Add(self.hbox3)
        self.vbox_setting.Add(self.hbox4)
        self.setsizer.Add(self.vbox_setting)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.operationareasizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox.Add(self.setsizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox)
        self.thread = TimeThread()          
        self.operationframe = OperationFrame()
        self.operationframe.Show(False)        
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.oo0o00oo0ooo000o00o0o, self.timer2)                 
        self.timer2.Start(100)          
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.o00oo0ooo0ooo00oooooo, self.timer3)                   
        self.timer3.Start(50)
        self.Bind(wx.EVT_BUTTON, self.o0o0ooo000o0oo000oo0o, self.timeautoreset)            
        pub.subscribe(self.o0o000ooo000o0o0ooo00, "open dianxin")        
        pub.subscribe(self.oooo0oo0000o0o0o000o0, "open nodianxin")         
        pub.subscribe(self.oo0oooo0ooo0000000o0o, "open userweb")             
    def ooo000o00ooo00oooo00o(self, event):
        global o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oo0000o00o0000oo00oo0, twice
        timer0 = threading.Timer(5, oooooo0o0oooo0o0o0o0o)
        oo00ooo0oo000o0oo0000 = True
        twice = False
        o0o0000oo000o00o0o0o0 = True
        ooo0ooo0o000o00oo000o = False
        o0000ooo000000ooo00o0 = 1       
        oo0000o00o0000oo00oo0 = False
        global Px, Py, url1, o0000ooooooo0oo00oo00, web_on, do, oooo000000o00o00oo0oo, ooo0o0000oo0oo0o00ooo, o0oo000oooo0o00oo0oo0
        if oooo000000o00o00oo0oo:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif ooo0o0000oo0oo0o00ooo:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                ooo0o0000oo0oo0o00ooo = True        
                o0000ooooooo0oo00oo00 = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟')
                if o00oo0oo0000ooo00oooo:
                    self.operationframe.oo00o0o0000ooo000o000()
                if not o0oo000oooo0o00oo0oo0:                
                    self.moniooo0oo0o000000o00oooothread = MoniTijiaoThread()            
                    self.ooo0oo0o000000o00oooothread = TijiaoThread()            
                    o0oo000oooo0o00oo0oo0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()
    def ooo0000oooo0o0o0o0oo0(self, event):
        o00o0o00o00oo0000o0o0 = Guopaiframe("国拍")
    def o0o000ooo000o0o0ooo00(self):
        global o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oo0000o00o0000oo00oo0, twice
        timer0 = threading.Timer(5, oooooo0o0oooo0o0o0o0o)
        oo00ooo0oo000o0oo0000 = True
        twice = False
        o0o0000oo000o00o0o0o0 = True
        ooo0ooo0o000o00oo000o = False
        o0000ooo000000ooo00o0 = 1       
        oo0000o00o0000oo00oo0 = False
        global Px, Py, url2, o0000ooooooo0oo00oo00, web_on, do, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo, o0oo000oooo0o00oo0oo0
        if ooo0o0000oo0oo0o00ooo:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooo000000o00o00oo0oo:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                o0000ooooooo0oo00oo00 = True
                oooo000000o00o00oo0oo = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o00oo0oo0000ooo00oooo:
                    self.operationframe.oo00o0o0000ooo000o000()
                if not o0oo000oooo0o00oo0oo0:                
                    self.moniooo0oo0o000000o00oooothread = MoniTijiaoThread()            
                    self.ooo0oo0o000000o00oooothread = TijiaoThread()            
                    o0oo000oooo0o00oo0oo0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,  style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def oooo0oo0000o0o0o000o0(self):
        global o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oo0000o00o0000oo00oo0, twice
        timer0 = threading.Timer(5, oooooo0o0oooo0o0o0o0o)
        oo00ooo0oo000o0oo0000 = True
        twice = False           
        o0o0000oo000o00o0o0o0 = True
        ooo0ooo0o000o00oo000o = False
        o0000ooo000000ooo00o0 = 1       
        oo0000o00o0000oo00oo0 = False
        global Px, Py, url3, o0000ooooooo0oo00oo00, web_on, do, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo, o0oo000oooo0o00oo0oo0
        if ooo0o0000oo0oo0o00ooo:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooo000000o00o00oo0oo:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                o0000ooooooo0oo00oo00 = True
                oooo000000o00o00oo0oo = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o00oo0oo0000ooo00oooo:
                    self.operationframe.oo00o0o0000ooo000o000()
                if not o0oo000oooo0o00oo0oo0:                
                    self.moniooo0oo0o000000o00oooothread = MoniTijiaoThread()            
                    self.ooo0oo0o000000o00oooothread = TijiaoThread()            
                    o0oo000oooo0o00oo0oo0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos ,style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def oo0oooo0ooo0000000o0o(self):
        global o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oo0000o00o0000oo00oo0, twice
        timer0 = threading.Timer(5, oooooo0o0oooo0o0o0o0o)                
        oo00ooo0oo000o0oo0000 = True
        twice = False
        o0o0000oo000o00o0o0o0 = True
        ooo0ooo0o000o00oo000o = False
        o0000ooo000000ooo00o0 = 1       
        oo0000o00o0000oo00oo0 = False
        global Px, Py, url3, o0000ooooooo0oo00oo00, web_on, do, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo, o0oo000oooo0o00oo0oo0
        self.Open()
        if do:
            o0000ooooooo0oo00oo00 = True
            oooo000000o00o00oo0oo = True
            if o00oo0oo0000ooo00oooo:
                self.operationframe.oo00o0o0000ooo000o000()
            if not o0oo000oooo0o00oo0oo0:                
                self.moniooo0oo0o000000o00oooothread = MoniTijiaoThread()            
                self.ooo0oo0o000000o00oooothread = TijiaoThread()            
                o0oo000oooo0o00oo0oo0 = True
                openIE(url3)
                self.Listen()
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            self.Close()             
    def ooo000oooo0oo000oo0o0(self, event):
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
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)
    def rule(self, event):
        url = "http://hupai.pro/rules"
        OpenwebThread(url)
    def help(self, event):
        url = "http://hupai.pro/coursestudy"
        OpenwebThread(url)
    def o000oo0o000oo000o0o0o(self, event):
        pass
    def oooooo0o0o000ooooo000(self, event):
        pass
    def oooo00ooo00o00oo0o000(self, event):
        pass
    def ooo0ooo00o0oooo0o0ooo(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)
    def o00o0o0o000000oo0o000(self, event):
        oooooo0o0oooo0o0o0o0o()
    def o000o0oo00000ooo00ooo(self, event):
        pass
    def o00oo0ooo0ooo00oooooo(self, event):   
        global o0oo0ooo0o00oo00o0o00, oooo0oo0ooooooo000o0o, o0ooo000ooooooo0o000o
        try:
            price = int(TopFrame.oooo0o0o00000oo00ooo0())           
            if price in pricelist:        
                oooo0oo0ooooooo000o0o = False
                if o0oo0ooo0o00oo00o0o00 == price:
                    pass
                else:
                    o0oo0ooo0o00oo00o0o00 = price
                    if ooo0o0000oo0oo0o00ooo:
                        o0ooo000ooooooo0o000o = oo0oo0ooo000000oo0000
                    else:
                        o0ooo000ooooooo0o000o = oo000000oooo0oo00oo00
            else:
                print("重新查找")
                oooo0oo0ooooooo000o0o = True
        except:
            oooo0oo0ooooooo000o0o = True
    def oo0000ooo0o0o00o0oooo(self, event):
        global oooo0oo0ooooooo000o0o
        if oooo0oo0ooooooo000o0o:
            try:
                oooooo0o0oooo0o0o0o0o()
            except:
                logging.error("oo0000ooo0o0o00o0oooo error")
                print("oo0000ooo0o0o00o0oooo error")
    def o0o0ooo000o0oo000oo0o(self, event):
        timeset()          
    @staticmethod
    def Confirm():
        global ooo00oo0000o00o0oo0oo, oo0oooo0000oo00oooooo
        confirm_hash = TopFrame.Confirm_hash()          
        if confirm_hash == ooo00oo0000o00o0oo0oo[0]:
            oo0oooo0000oo00oooooo = True
    @staticmethod
    def Refresh():
        o0oo0o0oo000ooo0ooooo_hash = TopFrame.Refresh_hash()          
        global ooo00oo0000o00o0oo0oo, o0o0o00o00oo0o0oo0000
        if o0oo0o0oo000ooo0ooooo_hash == ooo00oo0000o00o0oo0oo[1]:
            o0o0o00o00oo0o0oo0000 = True
    @staticmethod
    def oooo0o0o00000oo00ooo0():
        global ooooo00oo000oo0ooooo0 , oooo0oo0ooooooo000o0o
        global num
        num+=1
        o0oo0ooo0o00oo00o0o00 = cv2.cvtColor(ooooo00oo000oo0ooooo0, cv2.COLOR_BGR2GRAY)
        price = readpic(o0oo0ooo0o00oo00o0o00)
        print("price=",price)
        return price
    @staticmethod
    def o00oo000ooo0oooooooo0():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[0][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[0][1] = po[1]
    @staticmethod
    def o0o0oo0ooo0000o0o00o0():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[1][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[1][1] = po[1]
    @staticmethod
    def ooo00oo000oo0000000o0():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[2][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[2][1] = po[1]
    @staticmethod
    def oo0o0o0o000oo0o0oo000():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[3][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[3][1] = po[1]
    @staticmethod
    def o000o0000o0o0oo0oo0oo():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[4][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[4][1] = po[1]
    @staticmethod
    def o000oooo0o0000o00o000():
        po = pg.position()
        oo0o0oo0o0o0oo00o0oo0[5][0] = po[0]
        oo0o0oo0o0o0oo00o0oo0[5][1] = po[1]
    @staticmethod
    def o0o0oo00ooooo0o00oo00():
        TopFrame.o00oo000ooo0oooooooo0()
    @staticmethod
    def o0o0ooo0000000oo00ooo():
        TopFrame.o0o0oo0ooo0000o0o00o0()
    @staticmethod
    def o00o0oo00o0oo0000oo00():
        x,y=win32api.GetCursorPos()
        print("x=",x," y=",y)
    @staticmethod
    def o00o0o0o00o00o0o00o00():
        TopFrame.oo0o0o0o000oo0o0oo000()
    @staticmethod
    def oo00oo00oooo0oo0o0000():
        TopFrame.o000o0000o0o0oo0oo0oo()
    @staticmethod
    def oo0ooooo0oo0oo0o00000():
        TopFrame.o000oooo0o0000o00o000()
    @classmethod
    def o00ooo000o0o00oo00000(cls):
        global web_on, ooo0ooo0o000o00oo000o, o00000o0o0ooo0o0o0oo0, o0o00oooo0o0ooo000oo0, o0000ooo000000ooo00o0
        global ooo0ooo0o000o00oo000o, o0o0000oo000o00o0o0o0, oo0oooo0000oo00ooooooe, oo00ooo0o0oo00oo000oo
        oo00ooo0o0oo00oo000oo = True
        if o0000ooo000000ooo00o0 == 1:
            timer = threading.Timer(o00000o0o0ooo0o0o0oo0, cls.Tijiao)
            timer.start()
            ooo0ooo0o000o00oo000o = False
            if twice:
                o0000ooo000000ooo00o0 = 2
        elif o0000ooo000000ooo00o0 == 2:
            o0000ooo000000ooo00o0 = 0
            timer = threading.Timer(o0o00oooo0o0ooo000oo0, cls.Tijiao)
            timer.start()
            ooo0ooo0o000o00oo000o = False
        else:
            cls.Tijiao()
    @staticmethod
    def Tijiao():
        global ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, o0000ooo000000ooo00o0 ,o0o0000oo000o00o0o0o0
        Click(oo0o0oo0o0o0oo00o0oo0[2][0], oo0o0oo0o0o0oo00o0oo0[2][1])
        oo0000o00o0000oo00oo0 = False               
        o0o0000oo000o00o0o0o0 = True        
        global oo0oooo0000oo00ooooooe
        if not oo0oooo0000oo00ooooooe:        
            pass
    @classmethod
    def oo0o0oo0000o0000o0000(cls):
        global ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, o0000ooo000000ooo00o0, oo00ooo0o0oo00oo000oo
        oo00ooo0o0oo00oo000oo = True
        if ooo0o0000oo0oo0o00ooo:
            interval = oo0oo0ooo000000oo0000 - o0ooo000ooooooo0o000o
        else:
            interval = oo000000oooo0oo00oo00 - o0ooo000ooooooo0o000o
        if o0000ooo000000ooo00o0 == 2:            
            if o0oo0ooo0o00oo00o0o00 <= oooooo0o0000o0o0oo0o0 - 600:
                print("触发延迟")
                o0000ooo000000ooo00o0 = 0
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                ooo0ooo0o000o00oo000o = False
            elif o0oo0ooo0o00oo00o0o00 == oooooo0o0000o0o0oo0o0 - 500 and interval < 0.95:
                o0000ooo000000ooo00o0 = 0
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                ooo0ooo0o000o00oo000o = False
            else:
                o0000ooo000000ooo00o0 = 0
                cls.Tijiao()
                ooo0ooo0o000o00oo000o = False
        elif o0000ooo000000ooo00o0 == 1:
            if o0oo0ooo0o00oo00o0o00 <= oo000oo00o0oo0o0000oo - 600:
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                ooo0ooo0o000o00oo000o = False
                if twice:
                    o0000ooo000000ooo00o0 = 2
            elif o0oo0ooo0o00oo00o0o00 == oo000oo00o0oo0o0000oo - 500 and interval < 0.95:
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                ooo0ooo0o000o00oo000o = False
                if twice:
                    o0000ooo000000ooo00o0 = 2
            else:
                cls.Tijiao()
                ooo0ooo0o000o00oo000o = False
                if twice:
                    o0000ooo000000ooo00o0 = 2
    @staticmethod
    def o0oo00o0o000o0oo00o00():
        Click(oo0o0oo0o0o0oo00o0oo0[3][0], oo0o0oo0o0o0oo00o0oo0[3][1])
        Click(oo0o0oo0o0o0oo00o0oo0[5][0], oo0o0oo0o0o0oo00o0oo0[5][1])
        global o00ooo00oo0oo0oo0o000, oooo00ooo00o0oo0o0ooo, oo00o00o000o000oo0oo0
        o00ooo00oo0oo0oo0o000 = True         
        oo00o00o000o000oo0oo0 = 0      
    @staticmethod
    def oo00o0oo0o0o00o00oo0o():
        Click(oo0o0oo0o0o0oo00o0oo0[4][0], oo0o0oo0o0o0oo00o0oo0[4][1])
    @staticmethod
    def o0o00oo0o0000ooo0000o():
        global web_on, o0oo0ooo0o00oo00o0o00, oo00o00o000o000oo0oo0
        global o0000ooo000000ooo00o0, oo000oo00o0oo0o0000oo, oooooo0o0000o0o0oo0o0, oo0oo00ooooo0000o00o0, ooo0ooooo0o000oo0ooo0
        global ooo0ooo0o000o00oo000o, o0o0000oo000o00o0o0o0
        global oo0oo0oo0oo00o00o000o, oooo0000oooo0ooo0000o, oooo00o0oooo00000000o, o00ooo00oo0oo0oo0o000
        oo00o00o000o000oo0oo0 = 0            
        o00ooo00oo0oo0oo0o000 = True            
        print("到这了")
        ooo0ooo0o000o00oo000o = True          
        oo0oo0oo0oo00o00o000o = True           
        if o0000ooo000000ooo00o0 == 1:
            oo000oo00o0oo0o0000oo = o0oo0ooo0o00oo00o0o00 + oo0oo00ooooo0000o00o0
            setText(str(oo000oo00o0oo0o0000oo))
            TopFrame.o0oo000oo0ooo00o000o0()
            Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
            Click(oo0o0oo0o0o0oo00o0oo0[5][0], oo0o0oo0o0o0oo00o0oo0[5][1])
            ooo0ooo0o000o00oo000o = True
            o0o0000oo000o00o0o0o0 = False
            oooo00o0oooo00000000o = False        
        elif o0000ooo000000ooo00o0 == 2 and twice:
            oooooo0o0000o0o0oo0o0 = o0oo0ooo0o00oo00o0o00 + ooo0ooooo0o000oo0ooo0
            setText(str(oooooo0o0000o0o0oo0o0))
            TopFrame.o0oo000oo0ooo00o000o0()
            Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
            Click(oo0o0oo0o0o0oo00o0oo0[5][0], oo0o0oo0o0o0oo00o0oo0[5][1])
            ooo0ooo0o000o00oo000o = True
            o0o0000oo000o00o0o0o0 = False
            oooo00o0oooo00000000o = False        
    @staticmethod
    def oo0oo0o0o0o0o00o0000o():
        global o00ooo00oo0oo0oo0o000, oo00o00o000o000oo0oo0
        o00ooo00oo0oo0oo0o000 = True
        oo00o00o000o000oo0oo0 = 0
        oo000oo00o0oo0o0000oo = o0oo0ooo0o00oo00o0o00 + oo0oo00ooooo0000o00o0
        setText(str(oo000oo00o0oo0o0000oo))
        TopFrame.o0oo000oo0ooo00o000o0()
        Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
        Click(oo0o0oo0o0o0oo00o0oo0[5][0], oo0o0oo0o0o0oo00o0oo0[5][1])
    @staticmethod
    def o0oo000oo0ooo00o000o0():
        Click2(oo0o0oo0o0o0oo00o0oo0[6][0], oo0o0oo0o0o0oo00o0oo0[6][1] - 5)
        Click2(oo0o0oo0o0o0oo00o0oo0[6][0], oo0o0oo0o0o0oo00o0oo0[6][1])
        Click2(oo0o0oo0o0o0oo00o0oo0[6][0], oo0o0oo0o0o0oo00o0oo0[6][1])
        Delete()
        Delete()
        if ooo0o0000oo0oo0o00ooo:
            oo0o00o0ooo0o00oooooo()      
        else:
            Paste()       
    @staticmethod
    def o000o0o0o0o0o0oo00000():
        global o0000oo0ooo0oo000o00o, oo0oo0ooo0oo0oo0000oo, oo00o00o000o000oo0oo0, o00ooo00oo0oo0oo0o000
        Click(oo0o0oo0o0o0oo00o0oo0[4][0], oo0o0oo0o0o0oo00o0oo0[4][1])
        Click(oo0o0oo0o0o0oo00o0oo0[0][0], oo0o0oo0o0o0oo00o0oo0[0][1])
        Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
        Click(oo0o0oo0o0o0oo00o0oo0[5][0], oo0o0oo0o0o0oo00o0oo0[5][1])
        o0000oo0ooo0oo000o00o = True
        oo0oo0ooo0oo0oo0000oo = 0
        oo00o00o000o000oo0oo0 = 0
        o00ooo00oo0oo0oo0o000 = True
    @staticmethod
    def oo0o000o0o0000oooo000():
        OperationFrame.o00oo000000oooo0oo0oo()
        Click(oo0o0oo0o0o0oo00o0oo0[2][0], oo0o0oo0o0o0oo00o0oo0[2][1])
    @staticmethod
    def o00o0o0ooooooo0o0oo00():
        pg.press('backspace')
    def oo0o00oo0ooo000o00o0o(self, event):
        if not web_on and o00oo0oo0000ooo00oooo:             
            self.operationframe.o00ooo0oo00o000o0oo0o()
    @staticmethod
    def o0ooo0ooo0o0o00000ooo():
        global oo0000o00o0000oo00oo0, oo0oo0oo0oo00o00o000o, ooo0ooo0o000o00oo000o, oooo00ooo00o0oo0o0ooo, o00ooo00oo0oo0oo0o000
        if e_on and ooo0ooo0o000o00oo000o:
            print("o0ooo0ooo0o0o00000ooo")
            oo0000o00o0000oo00oo0 = True
            o00ooo00oo0oo0oo0o000 = False
            oooo00ooo00o0oo0o0ooo = True
    @staticmethod
    def ooo0oo00oo00oo00o0ooo():
        global oo0000o00o0000oo00oo0, oo0oo0oo0oo00o00o000o, oooo00ooo00o0oo0o0ooo, o00ooo00oo0oo0oo0o000
        if o0ooo000o00oo0oooo0o0 and ooo0ooo0o000o00oo000o:
            oo0000o00o0000oo00oo0 = True
        if o0ooo000o00oo0oooo0o0:
            oooo00ooo00o0oo0o0ooo = True
            o00ooo00oo0oo0oo0o000 = False
    @classmethod
    def query(cls):
        global o00000ooo00000ooo0000, o00ooo00o0oo0o0oo0ooo
        if not o00000ooo00000ooo0000 and not o00ooo00o0oo0o0oo0ooo:
            o00ooo00o0oo0o0oo0ooo = True
            o00000ooo00000ooo0000 = True
            setText(str(1000000))            
            TopFrame.o0oo000oo0ooo00o000o0()
            Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
            timer1 = threading.Timer(3, cls.ooo00oo00o0o0o000000o)
            timer1.start()
            timer2 = threading.Timer(5, cls.oo00000oo0000o0oooooo)
            timer2.start()
        elif o00000ooo00000ooo0000 and o00ooo00o0oo0o0oo0ooo:
            Click(oo0o0oo0o0o0oo00o0oo0[7][0], oo0o0oo0o0o0oo00o0oo0[7][1])
            o00ooo00o0oo0o0oo0ooo = False
    @staticmethod
    def ooo00oo00o0o0o000000o():
        global o00000ooo00000ooo0000, o00ooo00o0oo0o0oo0ooo
        if o00ooo00o0oo0o0oo0ooo:
            Click(oo0o0oo0o0o0oo00o0oo0[7][0], oo0o0oo0o0o0oo00o0oo0[7][1])
            o00ooo00o0oo0o0oo0ooo = False
    @staticmethod
    def oo00000oo0000o0oooooo():
        global o00000ooo00000ooo0000
        o00000ooo00000ooo0000 = False
    @staticmethod
    def Open():
        global do, web_on
        if not do:
            do = True
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
    @staticmethod
    def Listen():
        try:
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51, 'h': 0x48}
            HOTKEY_ACTIONS = {
                1: TopFrame.o0o0oo00ooooo0o00oo00, 2: TopFrame.o0o0ooo0000000oo00ooo, 3: TopFrame.o00o0oo00o0oo0000oo00,
                4: TopFrame.o00o0o0o00o00o0o00o00, 5: TopFrame.oo00oo00oooo0oo0o0000,
                6: TopFrame.oo0ooooo0oo0oo0o00000, 7: TopFrame.o0oo00o0o000o0oo00o00, 8: TopFrame.oo0o000o0o0000oooo000,
                9: (lambda: TopFrame.o000o0o0o0o0o0oo00000()), 10: TopFrame.o00o0o0ooooooo0o0oo00, 11: TopFrame.o0ooo0ooo0o0o00000ooo,
                12: TopFrame.ooo0oo00oo00oo00o0ooo,
                13: TopFrame.query, 14: TopFrame.oo0oo0o0o0o0o00o0000o}                  
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
    @staticmethod
    def Close():
        global do
        if do:
            do = False
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
            logging.info("close assistant success")
        else:
            pass
    def o000000oo0o00oooo00oo(self, evt):
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
    def OnClose(self, event):
        ret = wx.MessageBox('真的要退出助手吗?', '确认', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            import sys
            self.Show(False)
            try:
                self.Close_time1(event)              
                self.Close_time2(event)
            except:
                pass
            Logout()      
            wx.GetApp().ExitMainLoop()
            event.Skip()
            sys.exit(None)
    def o0ooo00o00oo0ooo00o00(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()
    @classmethod
    def oo0o0o0o00o00o000oo00(cls):
        cls.Close()
    def ooooo00ooooo0oo0ooooo(self, event):
        wx.CallAfter(pub.sendMessage, "o0oo0o0oo000ooo0ooooo")
        self.MovePos(event)
        global view
        if not view:
            view = True
            for i in range(len(oo0o0oo0o0o0oo00o0oo0)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(oo0o0oo0o0o0oo00o0oo0)):
                self.posframe[i].Hide()
    def o0000o00o0o000o0oo000(self, event):
        self.MovePos(event)
        self.oo00oooo00o0000000o0o()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)
    def MovePos(self, event):
        global o00o00ooo000o000o0oo0
        for i in range(5):
            posx, posy = oo0o0oo0o0o0oo00o0oo0[i]
            self.posframe[i].Move(posx - 10, posy - 5)
    def oo00oooo00o0000000o0o(self):
        output = open('pos.log', 'wb')
        pickle.dump(oo0o0oo0o0o0oo00o0oo0, output)
        output.close()
    def oo0o000o00oooooo00000(self, event):
        o000000000o0ooooo0oo0()
    def o0000o0o0oo0ooo0oo0oo(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global oo000oo0oo0000o00oo00, o00oo0o0o000oo000oooo
        oo000oo0oo0000o00oo00 = self.time_choice1.GetString(self.time_choice1.GetSelection())
        o00oo0o0o000oo000oooo = self.time_choice2.GetString(self.time_choice2.GetSelection())
    def o0000o0o00o0000oo0ooo(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global oo000oo0oo0000o00oo00, o00oo0o0o000oo000oooo
        oo000oo0oo0000o00oo00 = self.time_choice1.GetString(self.time_choice1.GetSelection())
        o00oo0o0o000oo000oooo = self.time_choice2.GetString(self.time_choice2.GetSelection())
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global oo000000oooo0oo00oo00
        time_local = time.localtime(oo000000oooo0oo00oo00)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global oo000000oooo0oo00oo00, b_time
        if b_time < 9:
            b_time = b_time + 1
        else:
            b_time = 0
        time_local = time.localtime(oo000000oooo0oo00oo00)
        st = time.strftime("%H:%M:%S", time_local)                       
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def OnTimer(self, evt):              
        dc = wx.BufferedDC(wx.ClientDC(self))                                   
        self.Modify(dc)
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)          
        self.Draw(dc)
class TimeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=o000o0o00o0oooo0ooo00,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        ClockWindow(self)
class MoniClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global oo0oo0ooo000000oo0000
        st = "%s:%s:%s" % (11, 29, oo0oo0ooo000000oo0000)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global oo0oo0ooo000000oo0000
        moni_s = int(oo0oo0ooo000000oo0000)       
        st = "%s:%s:%s" % (11, 29, moni_s)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def OnTimer(self, evt):              
        dc = wx.BufferedDC(wx.ClientDC(self))                                   
        self.Modify(dc)
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)          
        self.Draw(dc)
class MoniTimeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=o000o0o00o0oooo0ooo00,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        MoniClockWindow(self)
class PosFrame(wx.Frame):
    def __init__(self, pos, pos_name):
        x, y = pos
        wx.Frame.__init__(self, None, -1, 'POS',
                          pos=(x - 20, y - 10), size=(30, 20), style=wx.FRAME_TOOL_WINDOW)
        panel = wx.Panel(self, -1, size=(30, 20))
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
        self.bmp = wx.StaticBitmap(self.panel, -1, wx.Bitmap(image))
class YanzhengmaFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 18, 'Price', size=o0o0000ooo0oo00ooo0o0, pos=o00o0oo0oo0oo0ooooo00frame,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
                          )
        self.panel = wx.Panel(self, size=o0o0000ooo0oo00ooo0o0)
        self.bmp = wx.StaticBitmap(self.panel, -1)
    def o0o0oooo00o00000oo0o0(self, bm):
        self.bmp.SetBitmap(wx.Bitmap(bm))
    def OnClose(self, event):
        self.Close()
        event.Skip()
class AdFrame(wx.Frame):
    def __init__(self):               
        wx.Frame.__init__(self, None, -1, "广告",
                          pos=(0, 250), size=(250, 200), style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        panel = wx.Panel(self, -1, size=(250, 200))
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
    def __init__(self, px, py, ad, name):               
        wx.Frame.__init__(self, None, 3, name, size=(websize[0], websize[1]), pos=(px, py), style=wx.SIMPLE_BORDER)
        if ad:
            self.adframe = AdFrame()
            self.adframe.Show(True)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ad2 = ad
        global test
        pub.subscribe(self.o0oooo00o00o0oo000ooo, "close web")        
    def OnClose(self, event):
        global web_on, ooo00ooooo0o00ooo00o0, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo, o0oo000oooo0o00oo0oo0
        web_on = False
        ooo00ooooo0o00ooo00o0 = False
        ooo0o0000oo0oo0o00ooo = False
        oooo000000o00o00oo0oo = False
        TopFrame.Close()
        file = "sc_new.png"
        try:
            self.control.Destroy()
        except:
            pass
        if os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()
        event.Skip()                                  
    def o0oooo00o00o0oo000ooo(self):
        global web_on, ooo00ooooo0o00ooo00o0, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo, o0oo000oooo0o00oo0oo0
        web_on = False
        ooo00ooooo0o00ooo00o0 = False
        ooo0o0000oo0oo0o00ooo = False
        oooo000000o00o00oo0oo = False
        TopFrame.Close()
        file = "sc_new.png"
        if os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()
class ControlFrame(wx.Frame):                   
    def __init__(self):               
        wx.Frame.__init__(self, None, 4, size=(330, 200), style=wx.NO_BORDER | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR, \
                          pos=(Px + 40, Py + 480), name="control")
        self.panel = wx.Panel(self, -1, size=(330, 270))
        font1 = wx.Font(25, wx.SWISS, wx.NORMAL, wx.NORMAL)
        font2 = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.adtext = wx.StaticText(self.panel, label=u"小鲜肉代拍", pos=(90, 20))
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
        self.timetimer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Timego, self.timetimer1)
        self.timetimer1.Start(100)
    def ooooo0000o0oo0000o00o(self, event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()
    def Timego(self, event):
        global o0oo0ooo0o00oo00o0o00, oo0oo0ooo000000oo0000, oo000000oooo0oo00oo00
        self.price.SetLabel("%s" % o0oo0ooo0o00oo00o0o00)
        if ooo0o0000oo0oo0o00ooo:
            self.time.SetLabel("11:29:%s" % int(oo0oo0ooo000000oo0000))
        else:
            timestr1 = time.localtime(oo000000oooo0oo00oo00)
            timestr2 = time.strftime("%H:%M:%S", timestr1)
            self.time.SetLabel(timestr2)
        global pinger
        pingnow = pinger.ping()
        if pingnow == "timeout":
            self.netstat.SetLabel("%s" % pingnow)
        else:
            self.netstat.SetLabel("%sms" % pingnow)
class OperationFrame(wx.Frame):
    def __init__(self):               
        wx.Frame.__init__(self, None, 2, title="小鲜肉代拍", pos=(Px + 902, Py), size=(300, 425), \
                          style=wx.FRAME_NO_TASKBAR | wx.CAPTION | wx.CLOSE_BOX)                                           
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        global o0ooo0oo000oo00o000o0, o00oo0oo0o0ooooooo0oo, ooo00oo0000o00o0o00o0, oo00ooo0o0o00o0oo0oo0
        o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)
        ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)
        o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)
        oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.o0oo0o0o0o000o00o000o, self.timer1)                 
        self.timer1.Start(10)          
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.o000oooo00o000o0oo000, self.timer2)   
        self.timer2.Start(100)          
        self.lowestframe = LowestpriceFrame()
        self.lowestframe.Show(False)
        panel = wx.Panel(self, -1, size=(300, 380))
        stractagy = wx.StaticBox(panel, -1, u'选择策略:')
        self.stractagySizer = wx.StaticBoxSizer(stractagy, wx.VERTICAL)
        stractagy_label = wx.StaticText(panel, label=u"设定拍牌策略", size=(100, 50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(stractagy_label)
        stractagy_choices = [u'单枪策略', u'双枪策略', u'手动操作（热键辅助）']
        self.select_stractagy = wx.Choice(panel, -1, choices=stractagy_choices, size=(100, 50))
        hbox1.Add(self.select_stractagy)
        self.select_stractagy.SetSelection(0)
        self.timeview = wx.CheckBox(panel, -1, label=u'显示时间')          
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.timeview)
        self.button1 = wx.Button(panel, label='+1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.o0000o0ooo00oo000ooo0, self.button1)
        self.button2 = wx.Button(panel, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.oo000oo0oo0000000o00o, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.oo0oooo00o0000o0ooooo, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.oo0ooo0ooo0oo0000oo0o, self.button4)
        hbox2.Add(self.button1)
        hbox2.Add(self.button2)
        hbox2.Add(self.button3)
        hbox2.Add(self.button4)
        vb1 = wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)
        vb1.Add(hbox2)
        confirm_choice = ["E键", "回车"]
        self.confirm_choice = wx.Choice(panel, -1, choices=confirm_choice)
        self.confirm_choice.SetSelection(0)
        self.confirm_label = wx.StaticText(panel, label=u"确认提交方式     ")
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.confirm_label, flag=wx.TOP, border=4)
        hbox3.Add(self.confirm_choice)
        vb1.Add(hbox3)
        self.o00ooo000oooo0oooo00o_save = wx.Button(panel, label="保存策略", size=(60, 35))
        self.o00ooo000oooo0oooo00o_load = wx.Button(panel, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(panel, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.o00ooo000oooo0oooo00o_save)
        hbox4.Add(self.o00ooo000oooo0oooo00o_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)
        oneshot = wx.StaticBox(panel, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajioo000000oooo0oo00oo00 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))                              
        self.jiajioo000000oooo0oo00oo00.SetRange(40, 55)
        self.jiajioo000000oooo0oo00oo00.SetValue(48)
        self.jiajioo000000oooo0oo00oo00.SetIncrement(0.1)
        gridsizer1.Add(self.jiajioo000000oooo0oo00oo00, pos=(0, 0))
        miao_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))
        ooo0oo0o000000o00oooo_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_ooo0oo0o000000o00oooo = wx.Choice(panel, -1, choices=ooo0oo0o000000o00oooo_choices, size=(68, 25))
        self.select_ooo0oo0o000000o00oooo.SetSelection(0)
        gridsizer1.Add(self.select_ooo0oo0o000000o00oooo, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)
        ooo0oo0o000000o00oooo_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(ooo0oo0o000000o00oooo_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.ooo0oo0o000000o00oooo_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.ooo0oo0o000000o00oooo_time.SetRange(40.0, 57.0)
        self.ooo0oo0o000000o00oooo_time.SetValue(55.0)
        self.ooo0oo0o000000o00oooo_time.SetIncrement(0.1)
        gridsizer1.Add(self.ooo0oo0o000000o00oooo_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)
        secondshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajioo000000oooo0oo00oo002 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajioo000000oooo0oo00oo002.SetRange(40, 55)
        self.jiajioo000000oooo0oo00oo002.SetValue(48)
        self.jiajioo000000oooo0oo00oo002.SetIncrement(0.1)
        gridsizer2.Add(self.jiajioo000000oooo0oo00oo002, pos=(0, 0))
        miao_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(panel, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3))
        ooo0oo0o000000o00oooo_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_ooo0oo0o000000o00oooo2 = wx.Choice(panel, -1, choices=ooo0oo0o000000o00oooo_choices2, size=(68, 25))
        self.select_ooo0oo0o000000o00oooo2.SetSelection(0)
        gridsizer2.Add(self.select_ooo0oo0o000000o00oooo2, pos=(1, 0))
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)
        ooo0oo0o000000o00oooo_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(ooo0oo0o000000o00oooo_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.ooo0oo0o000000o00oooo_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.ooo0oo0o000000o00oooo_time2.SetRange(53.0, 57.0)
        self.ooo0oo0o000000o00oooo_time2.SetValue(55.0)
        self.ooo0oo0o000000o00oooo_time2.SetIncrement(0.1)
        gridsizer2.Add(self.ooo0oo0o000000o00oooo_time2, pos=(2, 1))
        miao3_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2), flag=wx.TOP, border=4)
        self.secondshotSizer.Add(gridsizer2, 0, flag=wx.ALL, border=5)
        self.stractagySizer.Add(vb1, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(panel, -1, label=u"拍牌功能设置")
        warning = wx.StaticText(panel, -1, label=u"10点半需要进行第一次出价")
        warning.SetForegroundColour('red')
        line = wx.StaticLine(panel, -1)
        self.vbox1.Add(title, 0, wx.ALL | wx.LEFT, 10)
        self.vbox1.Add(warning, 0, wx.LEFT, 10)
        self.vbox1.Add(line, flag=wx.EXPAND | wx.BOTTOM, border=10)
        self.vbox1.Add(self.stractagySizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.oneshotSizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.secondshotSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox1)
        self.secondsizer_Shown = False            
        self.oneshotsizer_Shown = True            
        self.vbox1.Hide(self.secondshotSizer)            
        self.Bind(wx.EVT_CHECKBOX, self.o0oo0o00o00o0ooo0o00o, self.timeview)
        self.Bind(wx.EVT_CHOICE, self.o0oo0oooo0o00o00o00oo, self.confirm_choice)
        self.Bind(wx.EVT_BUTTON, self.o00o000o0o0ooo0o0o0o0, self.o00ooo000oooo0oooo00o_save)
        self.Bind(wx.EVT_BUTTON, self.oooo00o0o0oooooooo0o0, self.o00ooo000oooo0oooo00o_load)
        self.Bind(wx.EVT_BUTTON, self.o000o00o0oo0oooo0o0o0, self.save_info)
        self.Bind(wx.EVT_CHOICE, self.o000o0o0ooo0oooo0ooo0, self.select_stractagy)
        self.Bind(wx.EVT_TEXT, self.o000oo00oo0o00oooo00o, self.jiajioo000000oooo0oo00oo00)
        self.Bind(wx.EVT_TEXT, self.o000oo00oo0oo00o00000, self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.oo0ooo0o0oo0oo0o0oo0o, self.select_ooo0oo0o000000o00oooo)
        self.Bind(wx.EVT_TEXT, self.oooo0ooo00o00ooo0oo00, self.yanchi_time)
        self.Bind(wx.EVT_TEXT, self.o0ooo00o0oo0oo0000o0o, self.ooo0oo0o000000o00oooo_time)
        self.Bind(wx.EVT_TEXT, self.o000oo00oo0o00oooo00o2, self.jiajioo000000oooo0oo00oo002)
        self.Bind(wx.EVT_TEXT, self.ooo00oooooo0ooooo00o0, self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.o0oo00o0o00oo0o0oo0o0, self.select_ooo0oo0o000000o00oooo2)
        self.Bind(wx.EVT_TEXT, self.oooo0ooo00o00ooo0oo002, self.yanchi_time2)
        self.Bind(wx.EVT_TEXT, self.ooo0oooo0oooo0o0ooooo, self.ooo0oo0o000000o00oooo_time2)
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)
        self.o00ooo00000o00000o00oframe = YanzhengmaFrame()
    def OnClose(self, event):
        self.Show(False)
    def o0oo0o0o0o000o00o000o(self, event):
        global o0000oo0ooo0oo000o00o, web_on, o000ooo0000oo0o0ooooo, ooo00ooooo0o00ooo00o0, o00ooo00oo0oo0oo0o000, o0o0000ooooo00oo0oo00, o0o0000ooo0oo00ooo0o0, oooo00ooo00o0oo0o0ooo
        global oo00o00o000o000oo0oo0, oo0oo0ooo0oo0oo0000oo, o00000oo000ooooo00ooo
        global o0oo0000ooooo00o00oo0 ,oooo00000o0o0oooooo0o
        if o00000oo000ooooo00ooo:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(o00o0oo0oo0oo0ooooo00frame)          
                    o00000oo000ooooo00ooo = False        
                except:
                    pass
        if o0000oo0ooo0oo000o00o and oo0oo0ooo0oo0oo0000oo >= 4:
            try:
                self.o0000000o0o00000o0oo0()
            except:
                pass
            self.o000oo0o0oooo00000o0o(Pos_price, o0o0000ooooo00oo0oo00, "userprice.png")
            image = "userprice.png"
            self.priceframe = PriceFrame(image, o0o0000ooooo00oo0oo00, Pos_priceframe)
            self.priceframe.Show(True)
            o0000oo0ooo0oo000o00o = False
            o000ooo0000oo0o0ooooo = True
        if oo00o00o000o000oo0oo0 >= 5 and not oooo00ooo00o0oo0o0ooo:                    
            o0o00oo00oo0oo0o000o0()
        if oooo00ooo00o0oo0o0ooo:
            try:
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        if o00ooo00oo0oo0oo0o000:
            oooo00ooo00o0oo0o0ooo = False
            cut_pic(o0oo0000ooooo00o00oo0, o0o0000ooo0oo00ooo0o0, "o00ooo00000o00000o00o.png")              
            image = "o00ooo00000o00000o00o.png"
            global o0o0ooooo0oo0o00o0000
            o0o0ooooo0oo0o00o0000 = Image.open("o00ooo00000o00000o00o.png")
            yan_hash = imagehash.dhash(o0o0ooooo0oo0o00o0000)
            if not oooo00000o0o0oooooo0o:      
                oooo00000o0o0oooooo0o = yan_hash
            elif yan_hash == oooo00000o0o0oooooo0o:         
                pass
            else:
                oooo00000o0o0oooooo0o = yan_hash
                try:
                    yan = self.FindWindowById(18)
                    yan.o0o0oooo00o00000oo0o0(image)
                    yan.Show()
                except:                 
                    pass
                finally:
                    pass
    def o000o0oooo0o000o0o0oo(self, event):
        global o00ooo00oo0oo0oo0o000, oooo00ooo00o0oo0o0ooo
        o0o00oo00oo0oo0o000o0()
    def o000oooo00o000o0oo000(self, event):
        global oo0oo0ooo0oo0oo0000oo, oo00o00o000o000oo0oo0
        oo0oo0ooo0oo0oo0000oo += 1
        oo00o00o000o000oo0oo0 += 1
        file = 'sc_new.png'
        if web_on and oo00ooo0oo000o0oo0000:
            self.lowestframe.Show(True)
        if not os.path.exists(file):
            try:
                self.o0000000o0o00000o0oo0()
            except:
                pass
        if not oo00ooo0oo000o0oo0000 or not web_on:
            self.lowestframe.Show(False)
    def o000oo0o0oooo00000o0o(self, box, size, name):
        global o0o0000ooooo00oo0oo00
        region = ImageGrab.grab(box)
        region.resize(size, Image.ANTIALIAS).save(name)
    def o000oo0o0oooo00000o0o_o00ooo00000o00000o00o(self, box, size, name):
        global o0o0000ooooo00oo0oo00
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)
    @staticmethod
    def o00oo000000oooo0oo0oo():
        try:
            os.remove("sc_new.png")
        except:
            pass
    def o0000000o0o00000o0oo0(self):
        try:
            self.priceframe.Destroy()
        except:
            pass
    def opt(self, event):
        global o0000ooo000000ooo00o0, ooo0ooo0o000o00oo000oe, o0o0000oo000o00o0o0o0
        global oo00ooo0oo000o0oo0000        
        global twice, o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, ooo0ooo0o000o00oo000oe            
        if oo0oo0ooo000000oo0000 < o00o00o00000ooooo0o0o and ooo0o0000oo0oo0o00ooo and not twice:        
            twice = False
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
        elif oo0oo0ooo000000oo0000 < o00o00o00000ooooo0o0o and ooo0o0000oo0oo0o00ooo and twice:        
            twice = True
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
    def oo0oooo00o0000o0ooooo(self, event):
        global oo000000oooo0oo00oo00, oo0oo0ooo000000oo0000, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo
        if ooo0o0000oo0oo0o00ooo:
            oo0oo0ooo000000oo0000 += 0.1
        else:
            oo000000oooo0oo00oo00 += 0.1
    def oo0ooo0ooo0oo0000oo0o(self, event):
        global oo000000oooo0oo00oo00, oo0oo0ooo000000oo0000, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo
        if ooo0o0000oo0oo0o00ooo:
            oo0oo0ooo000000oo0000 -= 0.1
        else:
            oo000000oooo0oo00oo00 -= 0.1
    def o0000o0ooo00oo000ooo0(self, event):
        global oo000000oooo0oo00oo00, oo0oo0ooo000000oo0000, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo
        if ooo0o0000oo0oo0o00ooo:
            oo0oo0ooo000000oo0000 += 1
            if oo0oo0ooo000000oo0000 >= 60:
                oo0oo0ooo000000oo0000 = 0
        else:
            oo000000oooo0oo00oo00 += 1
    def oo000oo0oo0000000o00o(self, event):
        global oo000000oooo0oo00oo00, oo0oo0ooo000000oo0000, ooo0o0000oo0oo0o00ooo, oooo000000o00o00oo0oo
        if ooo0o0000oo0oo0o00ooo:
            oo0oo0ooo000000oo0000 -= 1
            if oo0oo0ooo000000oo0000 <= 0:
                oo0oo0ooo000000oo0000 = 60
        else:
            oo000000oooo0oo00oo00 -= 1
    def o0oo0o00o00o0ooo0o00o(self, event):
        timeSelected = event.GetEventObject()
        global ooo00ooooo0o00ooo00o0, o00oo0oo0000ooo00oooo
        if timeSelected.IsChecked():
            ooo00ooooo0o00ooo00o0 = True
            o00oo0oo0000ooo00oooo = True
            if oooo000000o00o00oo0oo:
                self.timeframe1.Show(True)
            elif ooo0o0000oo0oo0o00ooo:
                self.timeframe2.Show(True)
        else:
            ooo00ooooo0o00ooo00o0 = False
            o00oo0oo0000ooo00oooo = False
            if oooo000000o00o00oo0oo:
                self.timeframe1.Show(False)
            elif ooo0o0000oo0oo0o00ooo:
                self.timeframe2.Show(False)
    def oo00o0o0000ooo000o000(self):
        if ooo0o0000oo0oo0o00ooo:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif oooo000000o00o00oo0oo:
            try:
                self.timeframe1.Show(True)
            except:
                pass
    def o00ooo0oo00o000o0oo0o(self):
        try:
            self.timeframe1.Show(False)
        except:
            pass
        try:
            self.timeframe2.Show(False)
        except:
            pass
    def o0oo0oooo0o00o00o00oo(self, event):
        global e_on, o0ooo000o00oo0oooo0o0
        con = self.confirm_choice.GetSelection()
        if con == 0:
            e_on = True
            o0ooo000o00oo0oooo0o0 = False
        elif con == 1:
            e_on = False
            o0ooo000o00oo0oooo0o0 = True
    def o000oo00oo0o00oooo00o(self, event):
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, o0ooo0oo000oo00o000o0, ooo00oo0000o00o0o00o0
        tem = self.jiajioo000000oooo0oo00oo00.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            o00o00o00000ooooo0o0o = tem
            o00o00o00000ooooo0o0o = float(o00o00o00000ooooo0o0o)
            o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)            
        else:
            self.jiajioo000000oooo0oo00oo00.SetValue(o00o00o00000ooooo0o0o)
    def o000oo00oo0oo00o00000(self, event):
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            oo0oo00ooooo0000o00o0 = int(tem)
        else:
            self.jiajia_price.SetValue(oo0oo00ooooo0000o00o0)
    def oo0ooo0o0oo0oo0o0oo0o(self, event):
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o
        select = self.select_ooo0oo0o000000o00oooo.GetString(self.select_ooo0oo0o000000o00oooo.GetSelection())
        if select == u"提前100":
            o0ooo0o00o0o00000ooo0 = 100
        elif select == u"提前200":
            o0ooo0o00o0o00000ooo0 = 200
        else:
            o0ooo0o00o0o00000ooo0 = 0
    def oooo0ooo00o00ooo0oo00(self, event):
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            o00000o0o0ooo0o0o0oo0 = float(tem)
        else:
            self.yanchi_time.SetValue(o00000o0o0ooo0o0o0oo0)
    def o0ooo00o0oo0oo0000o0o(self, event):
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, ooo00oo0000o00o0o00o0
        tem = self.ooo0oo0o000000o00oooo_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            o0000ooo00oo000o0o00o = float(tem)
            ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)            
        else:
            self.ooo0oo0o000000o00oooo_time.SetValue(o0000ooo00oo000o0o00o)
    def o000oo00oo0o00oooo00o2(self, event):
        global oo0oo0oooo0ooo0oo0000, o0o00oooo0o0ooo000oo0, ooo0ooooo0o000oo0ooo0, o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0, o00oo0oo0o0ooooooo0oo
        tem = self.jiajioo000000oooo0oo00oo002.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            o000o000o0000ooo0o0o0 = float(tem)
            o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)            
        else:
            self.jiajioo000000oooo0oo00oo002.SetValue(o000o000o0000ooo0o0o0)
    def ooo00oooooo0ooooo00o0(self, event):
        global oo0oo0oooo0ooo0oo0000, o0o00oooo0o0ooo000oo0, ooo0ooooo0o000oo0ooo0, o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0
        global o0ooo0o00o0o00000ooo0, o00000o0o0ooo0o0o0oo0, oo0oo00ooooo0000o00o0, o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            ooo0ooooo0o000oo0ooo0 = int(tem)
        else:
            self.jiajia_price2.SetValue(ooo0ooooo0o000oo0ooo0)
    def o0oo00o0o00oo0o0oo0o0(self, event):
        global oo0oo0oooo0ooo0oo0000, o0o00oooo0o0ooo000oo0, ooo0ooooo0o000oo0ooo0, o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0
        select = self.select_ooo0oo0o000000o00oooo2.GetString(self.select_ooo0oo0o000000o00oooo2.GetSelection())
        if select == u"提前100":
            oo0oo0oooo0ooo0oo0000 = 100
        elif select == u"提前200":
            oo0oo0oooo0ooo0oo0000 = 200
        else:
            oo0oo0oooo0ooo0oo0000 = 0
    def oooo0ooo00o00ooo0oo002(self, event):
        global oo0oo0oooo0ooo0oo0000, o0o00oooo0o0ooo000oo0, ooo0ooooo0o000oo0ooo0, o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0
        templist = ['0.%d' % i for i in range(11)]            
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            o0o00oooo0o0ooo000oo0 = float(tem)
        else:
            self.yanchi_time2.SetValue(o0o00oooo0o0ooo000oo0)
    def ooo0oooo0oooo0o0ooooo(self, event):
        global oo0oo0oooo0ooo0oo0000, o0o00oooo0o0ooo000oo0, ooo0ooooo0o000oo0ooo0, o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0, oo00ooo0o0o00o0oo0oo0
        tem = self.ooo0oo0o000000o00oooo_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            ooooo0o000oooo0o0ooo0 = float(tem)
            oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)            
        else:
            self.ooo0oo0o000000o00oooo_time2.SetValue(ooooo0o000oooo0o0ooo0)
    def o000o0o0ooo0oooo0ooo0(self, event):
        global oo00ooo0oo000o0oo0000        
        global twice, o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, ooo0ooo0o000o00oo000oe            
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice = False
            oo00ooo0oo000o0oo0000 = True
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
        elif stractagy_selection == u"双枪策略":
            self.oo000oo0oooooo00ooo00()
            oo00ooo0oo000o0oo0000 = True
            twice = True
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
        else:
            self.o0000ooo00o00oo00o0o0()
            oo00ooo0oo000o0oo0000 = False
            twice = False
    def oo000oo0oooooo00ooo00(self):      
        if not self.secondsizer_Shown:             
            self.vbox1.Show(self.secondshotSizer)          
            self.secondsizer_Shown = True                
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)           
            self.oneshotsizer_Shown = True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))          
        self.o0000oo0o0o00oo0000o0()
        self.Layout()
    def ss_Hide(self):      
        if self.secondsizer_Shown:             
            self.vbox1.Hide(self.secondshotSizer)             
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))          
        self.o00oooo0o0o00o00o00oo()
        self.Layout()
    def o0000ooo00o00oo00o0o0(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)
        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()
    def o00oooo0o0o00o00o00oo(self):
        global o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, oo0oo00ooooo0000o00o0, o00000o0o0ooo0o0o0oo0, o0ooo0o00o0o00000ooo0
        self.jiajioo000000oooo0oo00oo00.SetValue(48.0)
        self.ooo0oo0o000000o00oooo_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_ooo0oo0o000000o00oooo.SetSelection(0)
        self.yanchi_time.SetValue(0.5)
        o00o00o00000ooooo0o0o = 48           
        o0000ooo00oo000o0o00o = 55           
        oo0oo00ooooo0000o00o0 = 700           
        o00000o0o0ooo0o0o0oo0 = 0.5         
        o0ooo0o00o0o00000ooo0 = 100            
        global o0ooo0oo000oo00o000o0, o00oo0oo0o0ooooooo0oo, ooo00oo0000o00o0o00o0, oo00ooo0o0o00o0oo0oo0
        o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)
        ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)
        o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)
        oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)
    def o0000oo0o0o00oo0000o0(self):
        global o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, oo0oo00ooooo0000o00o0, o00000o0o0ooo0o0o0oo0, o0ooo0o00o0o00000ooo0
        global o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0, ooo0ooooo0o000oo0ooo0, o0o00oooo0o0ooo000oo0, oo0oo0oooo0ooo0oo0000
        self.jiajioo000000oooo0oo00oo00.SetValue(40.0)
        self.ooo0oo0o000000o00oooo_time.SetValue(48.0)
        self.jiajia_price.SetValue(500)
        self.select_ooo0oo0o000000o00oooo.SetSelection(2)
        self.yanchi_time.SetValue(0.0)
        self.jiajioo000000oooo0oo00oo002.SetValue(50.0)
        self.ooo0oo0o000000o00oooo_time2.SetValue(55.5)
        self.jiajia_price2.SetValue(700)
        self.select_ooo0oo0o000000o00oooo2.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)
        o00o00o00000ooooo0o0o = 40           
        o0000ooo00oo000o0o00o = 48           
        oo0oo00ooooo0000o00o0 = 500           
        o00000o0o0ooo0o0o0oo0 = 0.5         
        o0ooo0o00o0o00000ooo0 = 0            
        o000o000o0000ooo0o0o0 = 50            
        ooooo0o000oooo0o0ooo0 = 55.5           
        ooo0ooooo0o000oo0ooo0 = 700           
        o0o00oooo0o0ooo000oo0 = 0.5           
        oo0oo0oooo0ooo0oo0000 = 100              
        global o0ooo0oo000oo00o000o0, o00oo0oo0o0ooooooo0oo, ooo00oo0000o00o0o00o0, oo00ooo0o0o00o0oo0oo0
        o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)
        ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)
        o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)
        oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)
    def o00o000o0o0ooo0o0o0o0(self, event):
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
                dlg_tip = wx.MessageBox('名称不能为空', '策略保存', wx.OK | wx.ICON_ERROR)
                if dlg_tip == wx.ID_OK:
                    dlg_tip.Destroy()
                    dlg.Destroy()
    def save(self, name):
        global o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, oo0oo00ooooo0000o00o0, o00000o0o0ooo0o0o0oo0, o0ooo0o00o0o00000ooo0
        global o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0, ooo0ooooo0o000oo0ooo0, o0o00oooo0o0ooo000oo0, oo0oo0oooo0ooo0oo0000
        global osl, e_on, o0ooo000o00oo0oooo0o0          
        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0] = 0
            osl[1] = o00o00o00000ooooo0o0o
            osl[2] = o0000ooo00oo000o0o00o
            osl[3] = oo0oo00ooooo0000o00o0
            osl[4] = o00000o0o0ooo0o0o0oo0
            osl[5] = o0ooo0o00o0o00000ooo0
            osl[6] = o000o000o0000ooo0o0o0
            osl[7] = ooooo0o000oooo0o0ooo0
            osl[8] = ooo0ooooo0o000oo0ooo0
            osl[9] = o0o00oooo0o0ooo000oo0
            osl[10] = oo0oo0oooo0ooo0oo0000
            osl[11] = e_on
            osl[12] = o0ooo000o00oo0oooo0o0
        elif self.select_stractagy.GetSelection() == 1:
            osl[0] = 1
            osl[0] = 1
            osl[1] = o00o00o00000ooooo0o0o
            osl[2] = o0000ooo00oo000o0o00o
            osl[3] = oo0oo00ooooo0000o00o0
            osl[4] = o00000o0o0ooo0o0o0oo0
            osl[5] = o0ooo0o00o0o00000ooo0
            osl[6] = o000o000o0000ooo0o0o0
            osl[7] = ooooo0o000oooo0o0ooo0
            osl[8] = ooo0ooooo0o000oo0ooo0
            osl[9] = o0o00oooo0o0ooo000oo0
            osl[10] = oo0oo0oooo0ooo0oo0000
            osl[11] = e_on
            osl[12] = o0ooo000o00oo0oooo0o0
        with open('%s.o00ooo000oooo0oooo00o' % name, 'wb') as spk:
            pickle.dump(osl, spk)
    def oooo00o0o0oooooooo0o0(self, event):
        import os
        path = os.getcwd()
        choice = self.ooooo0oo0000o0ooo00oo(path)
        if choice:
            dlg = wx.SingleChoiceDialog(None, u"请选择策略:", u"策略载入",
                                        choices=choice)
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetStringSelection()           
                dlg_tip = wx.MessageDialog(None, "载入成功", u"载入策略", wx.OK | wx.ICON_INFORMATION)
                if dlg_tip.ShowModal() == wx.ID_OK:
                    dlg_tip.Destroy()
                self.load(path)
            dlg.Destroy()
        else:
            dlg_tip = wx.MessageBox('找不到任何保存的策略', '策略载入', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
    def load(self, path):
        global osl, e_on, o0ooo000o00oo0oooo0o0
        global o00o00o00000ooooo0o0o, o0000ooo00oo000o0o00o, oo0oo00ooooo0000o00o0, o00000o0o0ooo0o0o0oo0, o0ooo0o00o0o00000ooo0
        global o000o000o0000ooo0o0o0, ooooo0o000oooo0o0ooo0, ooo0ooooo0o000oo0ooo0, o0o00oooo0o0ooo000oo0, oo0oo0oooo0ooo0oo0000
        global oo00ooo0oo000o0oo0000        
        global twice, o0000ooo000000ooo00o0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, ooo0ooo0o000o00oo000oe            
        global o0ooo0oo000oo00o000o0, ooo00oo0000o00o0o00o0, o00oo0oo0o0ooooooo0oo, oo00ooo0o0o00o0oo0oo0
        try:
            with open(path, 'rb') as loadstr:
                osl = pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:      
            self.ss_Hide()
            twice = False
            oo00ooo0oo000o0oo0000 = True
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
            self.select_stractagy.SetSelection(0)
            self.jiajioo000000oooo0oo00oo00.SetValue(osl[1])
            self.ooo0oo0o000000o00oooo_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_ooo0oo0o000000o00oooo.SetSelection(0)
            elif osl[5] == 200:
                self.select_ooo0oo0o000000o00oooo.SetSelection(1)
            else:
                self.select_ooo0oo0o000000o00oooo.SetSelection(2)
            o00o00o00000ooooo0o0o = osl[1]           
            o0000ooo00oo000o0o00o = osl[2]           
            oo0oo00ooooo0000o00o0 = osl[3]           
            o00000o0o0ooo0o0o0oo0 = osl[4]         
            o0ooo0o00o0o00000ooo0 = osl[5]            
            e_on = osl[11]
            o0ooo000o00oo0oooo0o0 = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif o0ooo000o00oo0oooo0o0:
                self.confirm_choice.SetSelection(1)
            o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)
            ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)
            o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)
            oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)
        elif osl[0] == 1:      
            oo00ooo0oo000o0oo0000 = True
            twice = True
            o0o0000oo000o00o0o0o0 = True
            ooo0ooo0o000o00oo000o = False
            o0000ooo000000ooo00o0 = 1       
            oo0000o00o0000oo00oo0 = False
            ooo0ooo0o000o00oo000oe = False        
            self.oo000oo0oooooo00ooo00()
            self.select_stractagy.SetSelection(1)
            self.jiajioo000000oooo0oo00oo00.SetValue(osl[1])
            self.ooo0oo0o000000o00oooo_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_ooo0oo0o000000o00oooo.SetSelection(0)
            elif osl[5] == 200:
                self.select_ooo0oo0o000000o00oooo.SetSelection(1)
            else:
                self.select_ooo0oo0o000000o00oooo.SetSelection(2)
            self.jiajioo000000oooo0oo00oo002.SetValue(osl[6])
            self.ooo0oo0o000000o00oooo_time2.SetValue(osl[7])
            self.jiajia_price2.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_ooo0oo0o000000o00oooo2.SetSelection(0)
            elif osl[10] == 200:
                self.select_ooo0oo0o000000o00oooo2.SetSelection(1)
            else:
                self.select_ooo0oo0o000000o00oooo2.SetSelection(2)
            o00o00o00000ooooo0o0o = osl[1]           
            o0000ooo00oo000o0o00o = osl[2]           
            oo0oo00ooooo0000o00o0 = osl[3]           
            o00000o0o0ooo0o0o0oo0 = osl[4]         
            o0ooo0o00o0o00000ooo0 = osl[5]            
            o000o000o0000ooo0o0o0 = osl[6]            
            ooooo0o000oooo0o0ooo0 = osl[7]           
            ooo0ooooo0o000oo0ooo0 = osl[8]           
            o0o00oooo0o0ooo000oo0 = osl[9]           
            oo0oo0oooo0ooo0oo0000 = osl[10]              
            e_on = osl[11]
            o0ooo000o00oo0oooo0o0 = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif o0ooo000o00oo0oooo0o0:
                self.confirm_choice.SetSelection(1)
            o0ooo0oo000oo00o000o0 = self.gettime(o00o00o00000ooooo0o0o)
            ooo00oo0000o00o0o00o0 = self.gettime(o0000ooo00oo000o0o00o)
            o00oo0oo0o0ooooooo0oo = self.gettime(o000o000o0000ooo0o0o0)
            oo00ooo0o0o00o0oo0oo0 = self.gettime(ooooo0o000oooo0o0ooo0)
    def ooooo0oo0000o0ooo00oo(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.o00ooo000oooo0oooo00o':
                    L.append(os.path.join(root, file))
        return L
    def o000o00o0oo0oooo0o0o0(self, event):
        pass
    def o0ooo000ooooooo0o000o(self, a):          
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time          
    def o00000o0000000oo0o0o0(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a             
    def gettime(self, choice):                          
        tem = self.o00000o0000000oo0o0o0()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.o0ooo000ooooooo0o000o(b) + float(choice) - int(choice)
        return c                 
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global o0oo0ooo0o00oo00o0o00
        st = str(o0oo0ooo0o00oo00o0o00)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global o0oo0ooo0o00oo00o0o00
        st = str(o0oo0ooo0o00oo00o0o00)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def OnTimer(self, evt):              
        dc = wx.BufferedDC(wx.ClientDC(self))                                   
        self.Modify(dc)
    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)          
        self.Draw(dc)
class LowestpriceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=ooo00o0oo00oo0ooo0o00frame_pos,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        LowestpriceWindow(self)
import string
import wx.lib.agw.hyperlink as hyperlink
class LoginFrame(wx.Frame):
    def __init__(self, name, user, psd):               
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.welcomelabel = wx.StaticText(self.panel, -1, label="请输入用户名和密码", style=wx.ALIGN_CENTER)
        self.sizer_v1.Add(self.welcomelabel, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
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
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.o0000oo0o0o000oo0oo0o)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()
        self.helplink = hyperlink.HyperLinkCtrl(self.panel, -1, u"查看帮助")
        self.helplink.UnsetToolTip()
        self.helplink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.o0000oo0o0o000oo0oo0o)
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
        self.Center()         
        pub.subscribe(self.oo00ooooo0oooo0o0o0oo, "connect")
        self.hashthread = HashThread()
    def oo00ooooo0oooo0o0o0oo(self):
        self.loginbtn.Enable()
        global oo00oooo0o00oooo0o0o0, url2, url3          
        if oo00oooo0o00oooo0o0o0['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)
            if ooo0000oo00ooooo00oo0 == 'helong' or ooo0000oo00ooooo00oo0 == 'yuanjunkai' or ooo0000oo00ooooo00oo0 == 'zs':
                url2 = 'http://moni.51hupai.org/'
            else:
                url2 = oo00oooo0o00oooo0o0o0['url_dianxin']
            url3 = oo00oooo0o00oooo0o0o0['url_nodianxin']
        elif oo00oooo0o00oooo0o0o0['result'] == 'net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif oo00oooo0o00oooo0o0o0['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif oo00oooo0o00oooo0o0o0['result'] == 'wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif oo00oooo0o00oooo0o0o0['result'] == 'wrong password':
            wx.MessageBox('密码错误', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('登录失败', '用户登录', wx.OK | wx.ICON_ERROR)
    def oo0o0oo0o000oo00o0o0o(self, event):
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
    def OnLogin(self, event):
        global ooo0000oo00ooooo00oo0, ooo00000o0oo0oooooo0o
        username = self.userText.GetValue()
        password = self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
        else:
            ooo0000oo00ooooo00oo0 = username               
            ooo00000o0oo0oooooo0o = password
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            event.GetEventObject().Disable()
    def o0000oo0o0o000oo0oo0o(self, event):
        print("购买")
class UserValidator(wx.Validator):
    ''' o0o000oo00o000o000o00s data as it is entered into the text controls. '''
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)
    def o0o000oo00o000o000o00(self, win):
        return True
    def oo0o0o000oo000o0o0ooo(self):
        return True
    def ooo0o00o0oooo0ooo00oo(self):
        return True
    def OnChar(self, event):
        pass
class PassValidator(wx.Validator):
    ''' o0o000oo00o000o000o00s data as it is entered into the text controls. '''
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return PassValidator()
    def o0o000oo00o000o000o00(self, win):
        return True
    def oo0o0o000oo000o0o0ooo(self):
        return True
    def ooo0o00o0oooo0ooo00oo(self):
        return True
    def OnChar(self, event):
        pass
class ConfirmLogin(wx.Frame):
    pass
class TimeThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)                          
        self.start()                    
    def run(self):
        """Run Worker Thread."""
        global oo000000oooo0oo00oo00, oo0oo0ooo000000oo0000
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            oo000000oooo0oo00oo00 += b - a                
            oo0oo0ooo000000oo0000 += b - a
            if oo0oo0ooo000000oo0000 >= 60:
                oo0oo0ooo000000oo0000 = 0
class OpenwebThread(Thread):
    def __init__(self, url):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.url = url
        self.setDaemon(True)                          
        self.start()                    
    def run(self):
        """Run Worker Thread."""
        openweb(self.url)
class DeleteThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)                          
        self.start()                    
    def run(self):
        """Run Worker Thread."""
        Click2(oo0o0oo0o0o0oo00o0oo0[6][0] + 17, oo0o0oo0o0o0oo00o0oo0[6][1])
        for i in range(15):
            Delete()
        if ooo0o0000oo0oo0o00ooo:
            oo0o00o0ooo0o00oooooo()
        else:
            Paste()      
        Click(oo0o0oo0o0o0oo00o0oo0[1][0], oo0o0oo0o0o0oo00o0oo0[1][1])
class HashThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)                          
        self.start()                    
    def run(self):
        """Run Worker Thread."""
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION", 0,
                             winreg.KEY_ALL_ACCESS)
        try:
            name = os.path.realpath(sys.argv[0])          
            name = name.split('\\')[-1]
            winreg.SetValueEx(key, '%s'%name, 0, winreg.REG_DWORD, 0x00002710)                    
        except:
            print('error in set value!')
class oooooo0o0oooo0o0o0o0oThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()
    def run(self):
        for i in range(1000000):
            global oooo0oo0ooooooo000o0o
            if oooo0oo0ooooooo000o0o:
                try:
                    print("找着呢")
                    oooooo0o0oooo0o0o0o0o()      
                    time.sleep(0.1)          
                except:
                    logging.error("oooooo0o0oooo0o0o0o0othread error")
                    print("oooooo0o0oooo0o0o0o0othread error")
class confirmThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(confirmThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()             
        self.__flag.set()           
        self.__running = threading.Event()             
        self.__running.set()                   
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()                                         
            time.sleep(0.035)
            global o0000ooo000000ooo00o0
            if o0000ooo000000ooo00o0 == 2:
                try:
                    oo0oooooo0o0000000o00()
                except:
                    print("查找确认出错")
    def pause(self):
        self.__flag.clear()                   
    def resume(self):
        self.__flag.set()                    
    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            
class o0oo0o0oo000ooo0oooooThread(Thread):
    def __init__(self, *args, **kwargs):
        super(o0oo0o0oo000ooo0oooooThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()             
        self.__flag.set()           
        self.__running = threading.Event()             
        self.__running.set()                   
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()                                         
            logging.info("刷")
            time.sleep(0.035)
            try:
                oo0000o00000000o0oo00()
            except:
                print("刷新失败")
    def pause(self):
        self.__flag.clear()                   
    def resume(self):
        self.__flag.set()                    
    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            
class cutimgThread(Thread):
    def __init__(self, *args, **kwargs):
        super(cutimgThread, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()             
        self.__flag.set()           
        self.__running = threading.Event()             
        self.__running.set()                   
        self.setDaemon(True)
        self.start()
    def run(self):
        while self.__running.isSet():
            self.__flag.wait()                                         
            time.sleep(0.04)
            try:
                cut_img()
            except:
                print("截图失败")
    def pause(self):
        self.__flag.clear()                   
    def resume(self):
        self.__flag.set()                    
    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            
class LoginThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global ooo0000oo00ooooo00oo0, oo00oooo0o00oooo0o0o0
        oo00oooo0o00oooo0o0o0 = o000oo0oooo00o0000oo0()
        print(oo00oooo0o00oooo0o0o0)
        wx.CallAfter(pub.sendMessage, "connect")
class controlThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        wx.Sleep(10)
        wx.CallAfter(pub.sendMessage, "connect failure")
class KeepThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        for i in range(1000000):
            time.sleep(90)
            o000000000o0ooooo0oo0()
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global oo000ooooo00ooo0ooooo, oooooo0000o0o00o0000o, o0ooo00ooo0o0o00o00oo, o0oo0ooo0o00oo00o0o00, oo000oo00o0oo0o0000oo, oooooo0o0000o0o0oo0o0
        global oo0oo0ooo000000oo0000, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, ooo0ooo0o000o00oo000o, oo0000o00o0000oo00oo0, o00oo0oo0o0ooooooo0oo, oo00ooo0o0o00o0oo0oo0
        global o0ooo0o00o0o00000ooo0, oo0oo0oooo0ooo0oo0000, o0000ooo000000ooo00o0, oo0000o00o0000oo00oo0, o0o0000oo000o00o0o0o0, ooo0ooo0o000o00oo000o, ooo0ooo0o000o00oo000oe
        for i in range(10000000):
            time.sleep(0.05)              
            if ooo0ooo0o000o00oo000o and oo00ooo0oo000o0oo0000 and oooo000000o00o00oo0oo and oo0000o00o0000oo00oo0:                       
                if o0000ooo000000ooo00o0 == 1 and oo000000oooo0oo00oo00 >= ooo00oo0000o00o0o00o0 and not ooo0ooo0o000o00oo000oe:            
                    ooo0ooo0o000o00oo000o = False
                    TopFrame.oo0o0oo0000o0000o0000()        
                    ooo0ooo0o000o00oo000o = False
                    logging.info("Rone_ooo0oo0o000000o00oooo %s%s%s%s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo, oo0000o00o0000oo00oo0))
                    logging.info("Rone_ooo0oo0o000000o00oooo %s%s%s" % (o0000ooo000000ooo00o0, oo000000oooo0oo00oo00, ooo00oo0000o00o0o00o0))
                    ooo0ooo0o000o00oo000oe = True
                elif o0000ooo000000ooo00o0 == 2 and oo000000oooo0oo00oo00 >= oo00ooo0o0o00o0oo0oo0:            
                    ooo0ooo0o000o00oo000o = False
                    TopFrame.oo0o0oo0000o0000o0000()        
                    ooo0ooo0o000o00oo000o = False
                    logging.info("Rsecond_ooo0oo0o000000o00oooo %s%s%s%s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo, oo0000o00o0000oo00oo0))
                    logging.info("Rsecond_ooo0oo0o000000o00oooo %s%s%s" % (o0000ooo000000ooo00o0, oo000000oooo0oo00oo00, oo00ooo0o0o00o0oo0oo0))
                elif o0000ooo000000ooo00o0 == 1 and o0oo0ooo0o00oo00o0o00 >= oo000oo00o0oo0o0000oo - 300 - o0ooo0o00o0o00000ooo0 and oo000000oooo0oo00oo00 <= ooo00oo0000o00o0o00o0 - o00000o0o0ooo0o0o0oo0 and not ooo0ooo0o000o00oo000oe:        
                    ooo0ooo0o000o00oo000o = False
                    ooo0ooo0o000o00oo000o = False                        
                    TopFrame.o00ooo000o0o00oo00000()        
                    logging.info("Rone_ooo0oo0o000000o00oooo %s%s%s%s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo, oo0000o00o0000oo00oo0))
                    logging.info("Rone_ooo0oo0o000000o00oooo %s%s%s" % (o0000ooo000000ooo00o0, o0oo0ooo0o00oo00o0o00, oo000oo00o0oo0o0000oo))
                    ooo0ooo0o000o00oo000oe = True
                elif o0000ooo000000ooo00o0 == 2 and o0oo0ooo0o00oo00o0o00 >= oooooo0o0000o0o0oo0o0 - 300 - oo0oo0oooo0ooo0oo0000 and oo000000oooo0oo00oo00 <= oo00ooo0o0o00o0oo0oo0 - o0o00oooo0o0ooo000oo0:        
                    ooo0ooo0o000o00oo000o = False
                    ooo0ooo0o000o00oo000o = False                        
                    TopFrame.o00ooo000o0o00oo00000()        
                    logging.info("Rsecond_ooo0oo0o000000o00oooo %s%s%s%s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo, oo0000o00o0000oo00oo0))
                    logging.info("Rsecond_ooo0oo0o000000o00oooo %s%s%s" % (o0000ooo000000ooo00o0, o0oo0ooo0o00oo00o0o00, oooooo0o0000o0o0oo0o0))
            if oo00ooo0oo000o0oo0000 and oooo000000o00o00oo0oo and o0o0000oo000o00o0o0o0:                       
                if o0000ooo000000ooo00o0 == 1 and o0ooo0oo000oo00o000o0 <= oo000000oooo0oo00oo00 <= o0ooo0oo000oo00o000o0 + 0.6:            
                    TopFrame.o0o00oo0o0000ooo0000o()        
                    oo000oo00o0oo0o0000oo = o0oo0ooo0o00oo00o0o00 + oo0oo00ooooo0000o00o0
                    ooo0ooo0o000o00oo000o = True   
                    logging.info("Rone_o00o0ooooooo0oo0ooo00 %s%s" % (oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo))
                    logging.info("Rone_o00o0ooooooo0oo0ooo00 %s%s" % (o00o00o00000ooooo0o0o, o0ooo0oo000oo00o000o0))
                elif o0000ooo000000ooo00o0 == 2 and twice and o00oo0oo0o0ooooooo0oo <= oo000000oooo0oo00oo00:            
                    TopFrame.o0o00oo0o0000ooo0000o()        
                    oooooo0o0000o0o0oo0o0 = o0oo0ooo0o00oo00o0o00 + ooo0ooooo0o000oo0ooo0
                    ooo0ooo0o000o00oo000o = True
                    logging.info("Rsecond_o00o0ooooooo0oo0ooo00 %s%s" % (oo00ooo0oo000o0oo0000, oooo000000o00o00oo0oo))
                    logging.info("Rsecond_o00o0ooooooo0oo0ooo00 %s%s" % (o000o000o0000ooo0o0o0, o00oo0oo0o0ooooooo0oo))
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global oo0oo0ooo000000oo0000, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, ooo0ooo0o000o00oo000o, oo000oo00o0oo0o0000oo, oooooo0o0000o0o0oo0o0, oo0oo00ooooo0000o00o0, ooo0ooooo0o000oo0ooo0
        global o0000ooo000000ooo00o0, oo0000o00o0000oo00oo0, o0ooo0o00o0o00000ooo0, oo0oo0oooo0ooo0oo0000, ooo0ooo0o000o00oo000oe
        for i in range(10000000):
            time.sleep(0.05)              
            if ooo0ooo0o000o00oo000o and oo00ooo0oo000o0oo0000 and ooo0o0000oo0oo0o00ooo and oo0000o00o0000oo00oo0:                     
                if o0000ooo000000ooo00o0 == 1 and oo0oo0ooo000000oo0000 >= o0000ooo00oo000o0o00o and not ooo0ooo0o000o00oo000oe:            
                    TopFrame.oo0o0oo0000o0000o0000()        
                    logging.info("moni one_ooo0oo0o000000o00oooo %s %s %s %s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, oo0000o00o0000oo00oo0))
                    logging.info("moni one_ooo0oo0o000000o00oooo %s %s %s" % (o0000ooo000000ooo00o0, oo0oo0ooo000000oo0000, o0000ooo00oo000o0o00o))
                    ooo0ooo0o000o00oo000o = False
                    ooo0ooo0o000o00oo000oe = True         
                elif o0000ooo000000ooo00o0 == 2 and oo0oo0ooo000000oo0000 >= ooooo0o000oooo0o0ooo0 and twice:            
                    TopFrame.oo0o0oo0000o0000o0000()        
                    logging.info("moni1 second_ooo0oo0o000000o00oooo %s %s %s %s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, oo0000o00o0000oo00oo0))
                    logging.info("moni second_ooo0oo0o000000o00oooo %s %s %s" % (o0000ooo000000ooo00o0, oo0oo0ooo000000oo0000, ooooo0o000oooo0o0ooo0))
                    ooo0ooo0o000o00oo000o = False
                elif o0000ooo000000ooo00o0 == 1 and o0oo0ooo0o00oo00o0o00 >= oo000oo00o0oo0o0000oo - 300 - o0ooo0o00o0o00000ooo0 and not ooo0ooo0o000o00oo000oe:        
                    ooo0ooo0o000o00oo000o = False                        
                    TopFrame.o00ooo000o0o00oo00000()        
                    logging.info("moni one_ooo0oo0o000000o00oooo %s %s %s %s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, oo0000o00o0000oo00oo0))
                    logging.info("moni one_ooo0oo0o000000o00oooo %s %s %s" % (o0000ooo000000ooo00o0, o0oo0ooo0o00oo00o0o00, oo000oo00o0oo0o0000oo))
                    ooo0ooo0o000o00oo000oe = True         
                elif o0000ooo000000ooo00o0 == 2 and o0oo0ooo0o00oo00o0o00 >= oooooo0o0000o0o0oo0o0 - 300 - oo0oo0oooo0ooo0oo0000 and twice:        
                    ooo0ooo0o000o00oo000o = False                        
                    TopFrame.o00ooo000o0o00oo00000()        
                    logging.info("moni2 second_ooo0oo0o000000o00oooo %s%s%s%s" % (ooo0ooo0o000o00oo000o, oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo, oo0000o00o0000oo00oo0))
                    logging.info("moni second_ooo0oo0o000000o00oooo %s%s%s" % (o0000ooo000000ooo00o0, o0oo0ooo0o00oo00o0o00, oooooo0o0000o0o0oo0o0))
            if oo00ooo0oo000o0oo0000 and ooo0o0000oo0oo0o00ooo and o0o0000oo000o00o0o0o0:                     
                if o0000ooo000000ooo00o0 == 1 and o00o00o00000ooooo0o0o <= oo0oo0ooo000000oo0000 <= o00o00o00000ooooo0o0o + 0.6:            
                    TopFrame.o0o00oo0o0000ooo0000o()        
                    print("第一次")
                    oo000oo00o0oo0o0000oo = o0oo0ooo0o00oo00o0o00 + oo0oo00ooooo0000o00o0
                    ooo0ooo0o000o00oo000o = True
                    logging.info("moni one_o00o0ooooooo0oo0ooo00 %s %s" % (oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo))
                    logging.info("moni one_o00o0ooooooo0oo0ooo00 %s %s" % (o00o00o00000ooooo0o0o, oo0oo0ooo000000oo0000))
                elif o0000ooo000000ooo00o0 == 2 and twice and o000o000o0000ooo0o0o0 < oo0oo0ooo000000oo0000:
                    TopFrame.o0o00oo0o0000ooo0000o()        
                    print("第二次")
                    oooooo0o0000o0o0oo0o0 = o0oo0ooo0o00oo00o0o00 + ooo0ooooo0o000oo0ooo0
                    ooo0ooo0o000o00oo000o = True
                    logging.info("moni second_o00o0ooooooo0oo0ooo00 %s %s" % (oo00ooo0oo000o0oo0000, ooo0o0000oo0oo0o00ooo))
                    logging.info("moni second_o00o0ooooooo0oo0ooo00 %s %s" % (o000o000o0000ooo0o0o0, oo0oo0ooo000000oo0000))
class Infoframe(wx.Frame):
    def __init__(self, name, user, psd):               
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
ooo0oo00o0ooo000o0oo0 = "本地IE"
class Guopaiframe(wx.Dialog):
    def __init__(self, name):               
        wx.Frame.__init__(self, None, -1, name, size=(195, 265), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(195, 270))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.ooo0oo00o0ooo000o0oo0 = ooo0oo00o0ooo000o0oo0
        self.dianxin = wx.Button(self.panel, label="上海电信", pos=(20, 10), size=(140, 60))
        self.nodianxin = wx.Button(self.panel, label="非电信", pos=(20, 80), size=(140, 60))
        self.userweb = wx.Button(self.panel, label=self.ooo0oo00o0ooo000o0oo0, pos=(20, 150), size=(140, 60))
        self.dianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.nodianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.userweb.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_BUTTON, self.Dianxin, self.dianxin)
        self.Bind(wx.EVT_BUTTON, self.oo0oo0o00ooo0o0oo0oo0, self.nodianxin)
        self.Bind(wx.EVT_BUTTON, self.UserWeb, self.userweb)
        self.Center()
        self.ShowModal()
    def Dianxin(self, event):
        wx.CallAfter(pub.sendMessage, "open dianxin")
        self.Destroy()
        event.Skip()
    def oo0oo0o00ooo0o0oo0oo0(self, event):
        wx.CallAfter(pub.sendMessage, "open nodianxin")
        self.Destroy()
        event.Skip()
    def UserWeb(self, event):
        global ooo0oo00o0ooo000o0oo0, oooo000000o00o00oo0oo
        if ooo0oo00o0ooo000o0oo0 == '本地IE' and not oooo000000o00o00oo0oo:
            oooo000000o00o00oo0oo = True            
            ooo0oo00o0ooo000o0oo0 = '关闭辅助'
            wx.CallAfter(pub.sendMessage, "open userweb")
        else:
            ooo0oo00o0ooo000o0oo0 = '本地IE'
            oooo000000o00o00oo0oo = False            
            TopFrame.Close()
            try:
                yan = self.FindWindowById(18)
                yan.Destroy()
                global o00oo0o000o000o00oo0o
                print("关闭成功")
                o00oo0o000o000o00oo0o = False
            except:
                pass
        self.Destroy()
        event.Skip()
    def OnClose(self, event):
        self.Destroy()
        event.Skip()
class SketchApp(wx.App):
    def OnInit(self):
        try:
            with open("your.name", 'rb') as name:
                namepsd = pickle.load(name)
                user = namepsd[0]
                psd = namepsd[1]
        except:
            user = '123456'      
            user = '123456'      
            psd = 0
        loginframe = LoginFrame('小鲜肉拍牌', user, psd)
        loginframe.Show(True)
        return True
if __name__ == '__main__':
    o00oo00oooooo000o0o0o()
    o0o000o000oo00o0000oo()            
    app = SketchApp()
    confirmthread = confirmThread()       
    o0oo0o0oo000ooo0ooooothread = o0oo0o0oo000ooo0oooooThread()       
    finposthread = oooooo0o0oooo0o0o0o0oThread()        
    cutimgthread = cutimgThread()        
    app.MainLoop()
