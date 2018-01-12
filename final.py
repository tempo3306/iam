'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
version = '5.0'
num = 0
avt = 90100
test = False
host_ali = "http://hupai.pro"
url1="http://hupai.pro/Moni"
url2 = "www.baidu.com"      
url3 = "www.baidu.com"       
url4 = "http://127.0.0.1:5000/Moni"
mainicon = 'ico.ico'
view = False        
do = False        
oooo000ooooooooo00o0o = False        
o00ooooo00o00o0000o0o = False             
ooooo0oo0oo0o0o0oooo0 = False              
oo00o00o00o0oo00o0000 = True            
oo000oooo0ooo0000o000 = True          
oo0000000oo0oooooo00o = 0                              
oo00ooo0ooo000oo0000o = False          
oo0ooooo00oo0oo000o00 = 0               
o00o00o00000oooo00oo0 = 0               
web_on = False             
o0oo0ooo0oo0o0o0oo0oo = False           
operation_show = False           
o000oo000oo0ooooo00oo = False               
import time
oooo00o00oo0000oo0o0o = time.time()          
b_time = 0          
moni_minute = 29
o0oo0ooo000oo0oo00oo0 = 0
oo000oo0o000000o0o0oo_time = 0        
oo000oo0oooo00ooo000o = 0       
o0oooo0oooo0000oooo00 = 0      
ooooo00o000o0o00oo0o0 = False                          
oooooo00o000o00o000oo = False
o0ooooooo00o0000oo00o = 53          
o00oo0o00oooo00oo0000 = 0.0          
oooooo000000ooo00oooo = True          
oooo000o00000o0ooo0o0 = False                 
delay = False        
delay_time = 0.5          
o0o00o00ooo000o0o00o0 = False          
o0oo00o0000000000o0oo = True           
pricelist = [80000 + i * 100 for i in range(400)]          
IDnumber = 0        
account = 0       
passwd = 0      
o00000000000o000oo000 = 0
import pyautogui as pg
def o00o0o0o000o00o0oo0o0():
    with open('dick.dl', 'rb') as dick:
        global oooooo000o000o0oo0oo0
        oooooo000o000o0oo0oo0 = pickle.load(dick)                 
    with open('cf.btn', 'rb') as cf:
        global oo0o0o00000o00o00000o
        oo0o0o00000o00o00000o = pickle.load(cf)                            
    with open("target.tkl", 'rb')  as tar:
        global oooooo0o0o000ooooo0oo
        oooooo0o0o000ooooo0oo = pickle.load(tar)            
o000oo0ooo0o0o000oo00 = 48           
oo00000o0oo00o0o0o0o0 = 55           
ooo0o0o0o00o000ooo0oo = 1000000000000             
o0o00ooo0ooo0o0o00o0o = 1000000000000             
o000ooooooooo000o00o0 = 700           
oo0oo00o00000oo00o000 = 0.5         
ooo0oooooo0o0ooo00ooo = 100            
oo0o0o0o000o0o00ooooo = 48            
o00o0o0000oooo0000ooo = 55           
ooo0o0ooo0000000o0o0o = 1000000000000             
o000oo0oo0ooo0ooooooo = 1000000000000             
ooo0000000000ooo00000 = 600           
oo0ooo000o0oo0o00o0o0 = 0.5           
ooo0ooo0ooo00oo0ooo0o = 100              
osl = [0] * 15                          
oo00ooo0o000o00oo00o0 = True                      
ooo000o00oo00o0oo0000 = False                  
o0000o0o0000000o00o0o = 93400         
o0ooo0ooo00o0o0o0o0oo = 0         
o0oo000o000000oo00000 = 0         
own_price = 0        
o000000000ooo0oooo00o = False           
e_on = True                  
oooo0oooo0ooo000o0oo0 = False                   
twice = False          
oooo00oo00o0o00000o00 = 1                         
ooo000o00oo00o0oo0000e = False             
websize = [902, 700]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2          
Py2 = Pxy[1] / 2
Px = (Pxy[0] - websize[0]) / 2 - 80
Py = (Pxy[1] - websize[1]) / 2
P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]]               
P_relative2 = [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
o000o0oo000o000o0o00o = [[0, 0] for i in range(len(P_relative))]
for i in range(len(o000o0oo000o000o0o00o)):
    o000o0oo000o000o0o00o[i][0] = Px1 + P_relative[i][0]
    o000o0oo000o000o0o00o[i][1] = Py2 + P_relative[i][1]
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
ooo0o0000oooo000ooo00frame = 245
o0o0oo0oooo00oooo0oooframe = 290
o0o00o0000o0oo0o00o00frame_pos = [ooo0o0000oooo000ooo00frame, o0o0oo0oooo00oooo0oooframe]
px_o0o00oo0000oo00ooo0o0frame = 400 - 215
py_o0o00oo0000oo00ooo0o0frame = 460
px_mini = 200
py_mini = 40
o0oo0ooo00o00o0o00oo0 = [400, 80]
o0oo00oo000oo0o0oo0oo = [400, 220]
Timesize = [200, 50]
o0o00o0000o0oo0o00o00_area = [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py]
o00000o0o0oo0o0o0ooo0 = [396 - 150, 11 - 100, 396 + 150, 11 + 100]
o00oo000oo0oooo0oo0oo = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
o0000o0000oooo0o00o00 = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
o0o000o0ooo000ooo0ooo = [0,0]
webview_pos = [-25,0]                      
Px_price = Px + px_price
Py_price = Py + py_price
Pos_price = [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini]               
o000oooo00o0ooo00o00o = []           
Px_priceframe = Px + px_priceframe
Py_priceframe = Py + py_priceframe
Pos_priceframe = [Px_priceframe, Py_priceframe]
Px_timeframe = px_timeframe + Px
Py_timeframe = py_timeframe + Py
oo0o00ooo0oo0o0000o0o = [Px_timeframe, Py_timeframe]
o00000oo00oo0o00o0ooo = [Px + 40, Py + 480]
Px_o0o00oo0000oo00ooo0o0frame = Px + px_o0o00oo0000oo00ooo0o0frame
Py_o0o00oo0000oo00ooo0o0frame = Py + py_o0o00oo0000oo00ooo0o0frame
o000oooo00o0ooo00o00oframe = [Px_o0o00oo0000oo00ooo0o0frame, Py_o0o00oo0000oo00ooo0o0frame]
ooo0o0000oooo000ooo00 = 0                         
o0o0oo0oooo00oooo0ooo = 0            
oo00oo0o00000oooo000o = Px + ooo0o0000oooo000ooo00
o00oo00ooooo00o0ooooo = Py + o0o0oo0oooo00oooo0ooo
o0o00o0000o0oo0o00o00_sizex = 82           
o0o00o0000o0oo0o00o00_sizey = 16
ooo00000o00oo000oo0oo =oo00oo0o00000oooo000o-25             
o0000o000oooooo000o0o = o00oo00ooooo00o0ooooo+17
currenttime_sizex = 132
currenttime_sizey = 16
oooo0o0o0ooo0ooo0o0oo = 49                
ooo0o0o00ooooo00ooo0o = 0
px_confirm = 656
py_confirm = 475
Px_confirm = Px + px_confirm
Py_confirm = Py + py_confirm
confirm_sizex = 113
confirm_sizey = 28
oooo000o0ooo0o000oo0o = False          
o00oo0000o00o0o00o0oo = False          
oooo000o0ooo0o000oo0oe = False             
px_oo0o0000o000ooo0000oo = 550
py_oo0o0000o000ooo0000oo = 413
Px_oo0o0000o000ooo0000oo = Px + px_oo0o0000o000ooo0000oo
Py_oo0o0000o000ooo0000oo = Py + py_oo0o0000o000ooo0000oo
oo0o0000o000ooo0000oo_sizex = 108
oo0o0000o000ooo0000oo_sizey = 21
oo0000ooooo000oo0o0o0 = False          
oo0o0o0o00000oo00o0oo = False          
o000oo0o00oooooo000o0 = False             
oo0ooo0o0o0oo000ooo00 = False        
o0ooo000000oo0oooo00o_interval = False        
oo00ooo00000oo0o00o00 = False      
o0oo00oooo0o00o000o0o = False            
import numpy as np
oo00oo0oo0oooooo00o00 = [oo00oo0o00000oooo000o - 10, o00oo00ooooo00o0ooooo - 100, oo00oo0o00000oooo000o + 600, o00oo00ooooo00o0ooooo + 120]
ooooo000o0o00oo00oo0o = []
nptemp = []
oo000o0o0ooooo0oo0oo0 = np.array(nptemp)       
o00oo0o0ooooooo00000o = np.array(nptemp)       
o0ooo0o0oo000000o000o = np.array(nptemp)         
impos_o0o00oo0000oo00ooo0o0 = np.array(nptemp)       
o00000o0ooooooo00o0o0confirm = np.array(nptemp)         
oo00oo00o0oo00o000o00 = np.array(nptemp)        
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
yimg = ImageGrab.grab().save("o0o00oo0000oo00ooo0o0.png")
o000oo00oo0oo0oo0o0o0 = Image.open("o0o00oo0000oo00ooo0o0.png")                         
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
def o0oo0000o000o0o0oo000():
    global o0o000o0ooo000ooo0ooo
    Click(o0o000o0ooo000ooo0ooo[0],o0o000o0ooo000ooo0ooo[1])
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
def o00ooo0oo00o0oo00o0o0():
    sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    global oooooo0o0o000ooooo0oo
    template = oooooo0o0o000ooooo0oo[2]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    global ooo0o0000oooo000ooo00, o0o0oo0oooo00oooo0ooo, oooo0o0o0ooo0ooo0o0oo, ooo0o0o00ooooo00ooo0o, oo00oo0o00000oooo000o, o00oo00ooooo00o0ooooo, Px, Py
    global o00000o0o0oo0o0o0ooo0, o00oo000oo0oooo0oo0oo, oo0o00ooo0oo0o0000o0o, o00000oo00oo0o00o0ooo, o000oooo00o0ooo00o00o, o000oooo00o0ooo00o00oframe, o0000o0000oooo0o00o00
    global ooooo000o0o00oo00oo0o, oo00oo0oo0oooooo00o00          
    global o000o0oo000o000o0o00o, o00000o0o0oo0o0o0ooo0, o00oo000oo0oooo0oo0oo, oo0o00ooo0oo0o0000o0o, o00000oo00oo0o00o0ooo, o000oooo00o0ooo00o00o, o000oooo00o0ooo00o00oframe, o0000o0000oooo0o00o00
    global ooo00000o00oo000oo0oo,o0000o000oooooo000o0o           
    global o0o000o0ooo000ooo0ooo
    if max_val > 0.9:          
        ooo0o0000oooo000ooo00 = max_loc[0] + oooo0o0o0ooo0ooo0o0oo
        o0o0oo0oooo00oooo0ooo = max_loc[1] + ooo0o0o00ooooo00ooo0o
        oo00oo0o00000oooo000o = ooo0o0000oooo000ooo00
        o00oo00ooooo00o0ooooo = o0o0oo0oooo00oooo0ooo
        ooo00000o00oo000oo0oo = oo00oo0o00000oooo000o -27             
        o0000o000oooooo000o0o = o00oo00ooooo00o0ooooo -16
        o0o000o0ooo000ooo0ooo = [ooo0o0000oooo000ooo00-9,o0o0oo0oooo00oooo0ooo+84]
        for i in range(len(o000o0oo000o000o0o00o)):
            o000o0oo000o000o0o00o[i][0] = oo00oo0o00000oooo000o + P_relative2[i][0]
            o000o0oo000o000o0o00o[i][1] = o00oo00ooooo00o0ooooo + P_relative2[i][1]
        o00000o0o0oo0o0o0ooo0 = [396 - 150 + oo00oo0o00000oooo000o, 11 - 100 + o00oo00ooooo00o0ooooo, 396 + 150 + oo00oo0o00000oooo000o,
                        11 + 100 + o00oo00ooooo00o0ooooo]
        o00oo000oo0oooo0oo0oo = [505 - 80 + oo00oo0o00000oooo000o, 68 - 50 + o00oo00ooooo00o0ooooo, 505 + 80 + oo00oo0o00000oooo000o,
                        68 + 50 + o00oo00ooooo00o0ooooo]
        o0000o0000oooo0o00o00 = [205 - 80 + oo00oo0o00000oooo000o, 68 - 50 + o00oo00ooooo00o0ooooo, 405 + 80 + oo00oo0o00000oooo000o,
                            68 + 50 + o00oo00ooooo00o0ooooo]
        o00000oo00oo0o00o0ooo = [192 - 344 + oo00oo0o00000oooo000o, 514 - 183 + o00oo00ooooo00o0ooooo]
        o000oooo00o0ooo00o00o = [o000o0oo000o000o0o00o[5][0] - 277, o000o0oo000o000o0o00o[5][1] - 65, o000o0oo000o000o0o00o[5][0] - 97,
                          o000o0oo000o000o0o00o[5][1] + 45]           
        o000oooo00o0ooo00o00oframe = [oo00oo0o00000oooo000o + 297, o00oo00ooooo00o0ooooo - 283]            
        global o0oo00o0000000000o0oo, oo000oooo0ooo0000o000
        o0oo00o0000000000o0oo = False        
        oo000oooo0ooo0000o000 = True        
        lowest = [oo00oo0o00000oooo000o, o00oo00ooooo00o0ooooo,  o0o00o0000o0oo0o00o00_sizex+oo00oo0o00000oooo000o, o0o00o0000o0oo0o00o00_sizey+o00oo00ooooo00o0ooooo]
        currenttime = [ooo00000o00oo000oo0oo,o0000o000oooooo000o0o,ooo00000o00oo000oo0oo+currenttime_sizex,o0000o000oooooo000o0o+currenttime_sizey]
        dis_x=50
        dis_y=100
        x1 = oo00oo0o00000oooo000o - dis_x         
        y1 = o00oo00ooooo00o0ooooo - dis_y
        cal_area = [lowest, o00000o0o0oo0o0o0ooo0, o00oo000oo0oooo0oo0oo, o000oooo00o0ooo00o00o, o0000o0000oooo0o00o00 , currenttime]          
        ooooo000o0o00oo00oo0o = []
        oo00oo0oo0oooooo00o00 = [oo00oo0o00000oooo000o - dis_x, o00oo00ooooo00o0ooooo - dis_y, oo00oo0o00000oooo000o + 600, o00oo00ooooo00o0ooooo + 120]
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            ooooo000o0o00oo00oo0o.append(temp)
def oo0ooooo0o00ooooo00o0(area):                          
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
    global ooooo000o0o00oo00oo0o, oo00oo0oo0oooooo00o00, oo000o0o0ooooo0oo0oo0, o00000o0ooooooo00o0o0, o00oo0o0ooooooo00000o, o0ooo0o0oo000000o000o, o00000o0ooooooo00o0o0confirm,oo00oo00o0oo00o000o00
    img = oo0ooooo0o00ooooo00o0(oo00oo0oo0oooooo00o00)           
    img = np.asarray(img)              
    oo000o0o0ooooo0oo0oo0 = img[ooooo000o0o00oo00oo0o[0][1]:ooooo000o0o00oo00oo0o[0][3], ooooo000o0o00oo00oo0o[0][0]:ooooo000o0o00oo00oo0o[0][2]]      
    o00oo0o0ooooooo00000o = img[ooooo000o0o00oo00oo0o[1][1]:ooooo000o0o00oo00oo0o[1][3], ooooo000o0o00oo00oo0o[1][0]:ooooo000o0o00oo00oo0o[1][2]]      
    o0ooo0o0oo000000o000o = img[ooooo000o0o00oo00oo0o[2][1]:ooooo000o0o00oo00oo0o[2][3], ooooo000o0o00oo00oo0o[2][0]:ooooo000o0o00oo00oo0o[2][2]]
    o00000o0ooooooo00o0o0 = img[ooooo000o0o00oo00oo0o[3][1]:ooooo000o0o00oo00oo0o[3][3], ooooo000o0o00oo00oo0o[3][0]:ooooo000o0o00oo00oo0o[3][2]]      
    o00000o0ooooooo00o0o0confirm = img[ooooo000o0o00oo00oo0o[4][1]:ooooo000o0o00oo00oo0o[4][3], ooooo000o0o00oo00oo0o[4][0]:ooooo000o0o00oo00oo0o[4][2]]      
    oo00oo00o0oo00o000o00 = img[ooooo000o0o00oo00oo0o[5][1]:ooooo000o0o00oo00oo0o[5][3], ooooo000o0o00oo00oo0o[5][0]:ooooo000o0o00oo00oo0o[5][2]]
def oo0o00oo000o0ooooooo0():
    global oooooo0o0o000ooooo0oo, oo0000ooooo000oo0o0o0, oo0o0o0o00000oo00o0oo, o000oo0o00oooooo000o0, o000o0oo000o000o0o00o, o00000o0o0oo0o0o0ooo0, o00oo000oo0oooo0oo0oo
    template = oooooo0o0o000ooooo0oo[0]
    global o00oo0o0ooooooo00000o
    sc = o00oo0o0ooooooo00000o
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    logging.info("查找刷新")
    if max_val >= 0.8:
        logging.info("刷新")
        TopFrame.o00oo00oo0o0oooo0oo0o()
        global ooooo0oo0oo0o0o0oooo0, oo00o00o00o0oo00o0000, o00o00o00000oooo00oo0
        ooooo0oo0oo0o0o0oooo0 = True         
        o00o00o00000oooo00oo0 = 0      
def oooo00o00o00ooo00oo00():
    global oooooo0o0o000ooooo0oo, oooo000o0ooo0o000oo0o, o000o0oo000o000o0o00o
    template = oooooo0o0o000ooooo0oo[1]
    global o0ooo0o0oo000000o000o
    sc = o0ooo0o0oo000000o000o
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.9:
        TopFrame.o000oo000o0oooo00000o()
    if oooo000o0ooo0o000oo0o and max_val < 0.9:
        print("暂停确认")
def o0o00oo000oooo0o00oo0():
    global oooooo0o0o000ooooo0oo, oooo000o0ooo0o000oo0o, o000o0oo000o000o0o00o, ooooo0oo0oo0o0o0oooo0, oo00o00o00o0oo00o0000
    template = oooooo0o0o000ooooo0oo[1]
    global o00000o0ooooooo00o0o0confirm
    sc = o00000o0ooooooo00o0o0confirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.9:
        ooooo0oo0oo0o0o0oooo0 = False
        oo00o00o00o0oo00o0000 = True
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
def o0000oo00oo0o000o00oo(area):                          
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
def oo00o00o0o0oo00o0oo00(area, size, name):
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
    global oooo00o00oo0000oo0o0o, oo00oo00o0oo00o000o00, o0oo0ooo000oo0oo00oo0
    currenttime = cv2.cvtColor(oo00oo00o0oo00o000o00, cv2.COLOR_BGR2GRAY)
    currenttime = readpic(currenttime)           
    cv2.imwrite("zp.png", oo00oo00o0oo00o000o00)
    print(currenttime)
    tem1 = time.time()
    a = time.strftime('%Y-%m-%d', time.localtime(tem1))
    b = a + ' ' + currenttime
    oooo00o00oo0000oo0o0o = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')) + 0.5                 
    try:
        o0oo0ooo000oo0oo00oo0 = int(currenttime.split(':')[2]) + 0.5
    except:
        pass
import winreg, re, subprocess
ooo00o00oo0o0ooo0o000 = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'
def o0ooooo0ooooo00oo0o0o():
    global ooo00o00oo0o0ooo0o000
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            ooo00o00oo0o0ooo0o000 = result[0]
    except:
        pass
    if not os.path.exists(ooo00o00oo0o0ooo0o000):
        if os.path.exists('C:\Program Files (x86)'):
            pass
def openweb(url):
    global ooo00o00oo0o0ooo0o000
    subprocess.Popen([ooo00o00oo0o0ooo0o000, url])
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
def o000oo0000o0oo0o000o0():
    try:
        target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % oo000oo0oooo00ooo000o + '&' + 'passwd=%s' % o0oooo0oooo0000oooo00
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
    global oo000oo0oooo00ooo000o
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
def ooo0ooooo0o00oooo0000():
    host = host_ali
    port = 8080
    global oo000oo0oooo00ooo000o
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
    data = ['keep', oo000oo0oooo00ooo000o, o0oooo0oooo0000oooo00]
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")           
    logging.info('发送信息 %s' % str(data, encoding="utf-8"))
    s.send(data)
    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")
def ooooooo000o000000oooo(subject, to_list, file_name):
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
def oo00ooooooo0o0oo0000o():
    pass
def ooo0000000o00oo00o0oo():
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
        self.Bind(wx.EVT_BUTTON, self.ooo00ooooooooooo0o00o, self.monibutton)
        self.o00oooooo00o00oo0oo0obutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.oooooo000o00o0oo0oo0o, self.o00oooooo00o00oo0oo0obutton)
        self.hbox1.Add(self.monibutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.o00oooooo00o00oo0oo0obutton, 0, wx.ALL | wx.CENTER, 5)
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
        self.Bind(wx.EVT_BUTTON, self.oo00oo00oo0o0o0o0oo0o, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.o00o0ooo0000o0oo0o0o0, self.posautoset)
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
        self.Bind(wx.EVT_TIMER, self.o00oo000oo0o000000o0o, self.timer2)                 
        self.timer2.Start(100)          
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.ooo000o0o0o00oo0oo00o, self.timer3)                   
        self.timer3.Start(50)
        self.Bind(wx.EVT_BUTTON, self.oo00o0o000oooo0o0oo00, self.timeautoreset)            
        pub.subscribe(self.oo000oooo00oo00ooo0oo, "open dianxin")        
        pub.subscribe(self.o0o0o00000oo0o0o0o0o0, "open nodianxin")         
        pub.subscribe(self.oo0ooooo0000o000ooo00, "open userweb")             
    def ooo00ooooooooooo0o00o(self, event):
        global oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, o000000000ooo0oooo00o, twice
        timer0 = threading.Timer(5, o00ooo0oo00o0oo00o0o0)
        oooooo000000ooo00oooo = True
        twice = False
        oo00ooo0o000o00oo00o0 = True
        ooo000o00oo00o0oo0000 = False
        oooo00oo00o0o00000o00 = 1       
        o000000000ooo0oooo00o = False
        global Px, Py, url1, oooo000ooooooooo00o0o, web_on, do, oooooo00o000o00o000oo, ooooo00o000o0o00oo0o0, oooo000o00000o0ooo0o0
        if oooooo00o000o00o000oo:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif ooooo00o000o0o00oo0o0:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                ooooo00o000o0o00oo0o0 = True        
                oooo000ooooooooo00o0o = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟')
                if o000oo000oo0ooooo00oo:
                    self.operationframe.oo0o0oooo0ooo0o0000o0()
                if not oooo000o00000o0ooo0o0:                
                    self.monio0ooo000000oo0oooo00othread = MoniTijiaoThread()            
                    self.o0ooo000000oo0oooo00othread = TijiaoThread()            
                    oooo000o00000o0ooo0o0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()
    def oooooo000o00o0oo0oo0o(self, event):
        o00oooooo00o00oo0oo0o = Guopaiframe("国拍")
    def oo000oooo00oo00ooo0oo(self):
        global oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, o000000000ooo0oooo00o, twice
        timer0 = threading.Timer(5, o00ooo0oo00o0oo00o0o0)
        oooooo000000ooo00oooo = True
        twice = False
        oo00ooo0o000o00oo00o0 = True
        ooo000o00oo00o0oo0000 = False
        oooo00oo00o0o00000o00 = 1       
        o000000000ooo0oooo00o = False
        global Px, Py, url2, oooo000ooooooooo00o0o, web_on, do, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo, oooo000o00000o0ooo0o0
        if ooooo00o000o0o00oo0o0:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooooo00o000o00o000oo:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                oooo000ooooooooo00o0o = True
                oooooo00o000o00o000oo = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o000oo000oo0ooooo00oo:
                    self.operationframe.oo0o0oooo0ooo0o0000o0()
                if not oooo000o00000o0ooo0o0:                
                    self.monio0ooo000000oo0oooo00othread = MoniTijiaoThread()            
                    self.o0ooo000000oo0oooo00othread = TijiaoThread()            
                    oooo000o00000o0ooo0o0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,  style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def o0o0o00000oo0o0o0o0o0(self):
        global oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, o000000000ooo0oooo00o, twice
        timer0 = threading.Timer(5, o00ooo0oo00o0oo00o0o0)
        oooooo000000ooo00oooo = True
        twice = False           
        oo00ooo0o000o00oo00o0 = True
        ooo000o00oo00o0oo0000 = False
        oooo00oo00o0o00000o00 = 1       
        o000000000ooo0oooo00o = False
        global Px, Py, url3, oooo000ooooooooo00o0o, web_on, do, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo, oooo000o00000o0ooo0o0
        if ooooo00o000o0o00oo0o0:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooooo00o000o00o000oo:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                oooo000ooooooooo00o0o = True
                oooooo00o000o00o000oo = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o000oo000oo0ooooo00oo:
                    self.operationframe.oo0o0oooo0ooo0o0000o0()
                if not oooo000o00000o0ooo0o0:                
                    self.monio0ooo000000oo0oooo00othread = MoniTijiaoThread()            
                    self.o0ooo000000oo0oooo00othread = TijiaoThread()            
                    oooo000o00000o0ooo0o0 = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos ,style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def oo0ooooo0000o000ooo00(self):
        global oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, o000000000ooo0oooo00o, twice
        timer0 = threading.Timer(5, o00ooo0oo00o0oo00o0o0)                
        oooooo000000ooo00oooo = True
        twice = False
        oo00ooo0o000o00oo00o0 = True
        ooo000o00oo00o0oo0000 = False
        oooo00oo00o0o00000o00 = 1       
        o000000000ooo0oooo00o = False
        global Px, Py, url3, oooo000ooooooooo00o0o, web_on, do, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo, oooo000o00000o0ooo0o0
        self.Open()
        if do:
            oooo000ooooooooo00o0o = True
            oooooo00o000o00o000oo = True
            if o000oo000oo0ooooo00oo:
                self.operationframe.oo0o0oooo0ooo0o0000o0()
            if not oooo000o00000o0ooo0o0:                
                self.monio0ooo000000oo0oooo00othread = MoniTijiaoThread()            
                self.o0ooo000000oo0oooo00othread = TijiaoThread()            
                oooo000o00000o0ooo0o0 = True
                openIE(url3)
                self.Listen()
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            self.Close()             
    def o0o00o000ooooo000o0o0(self, event):
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
    def oo0ooo0o0000000o0ooo0(self, event):
        pass
    def o0o000ooo00o00o00000o(self, event):
        pass
    def oo0oo0ooo00oo00ooo00o(self, event):
        pass
    def oo00oo00oo0o0o0o0oo0o(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)
    def o00o0ooo0000o0oo0o0o0(self, event):
        o00ooo0oo00o0oo00o0o0()
    def o000o0o0ooooo000oo0o0(self, event):
        pass
    def ooo000o0o0o00oo0oo00o(self, event):   
        global o0000o0o0000000o00o0o, o0oo00o0000000000o0oo, o00000000000o000oo000
        try:
            price = int(TopFrame.o0o000o00oo000ooooo00())           
            if price in pricelist:        
                o0oo00o0000000000o0oo = False
                if o0000o0o0000000o00o0o == price:
                    pass
                else:
                    o0000o0o0000000o00o0o = price
                    if ooooo00o000o0o00oo0o0:
                        o00000000000o000oo000 = o0oo0ooo000oo0oo00oo0
                    else:
                        o00000000000o000oo000 = oooo00o00oo0000oo0o0o
            else:
                print("重新查找")
                o0oo00o0000000000o0oo = True
        except:
            o0oo00o0000000000o0oo = True
    def oo00oooo00o0oo0o000oo(self, event):
        global o0oo00o0000000000o0oo
        if o0oo00o0000000000o0oo:
            try:
                o00ooo0oo00o0oo00o0o0()
            except:
                logging.error("oo00oooo00o0oo0o000oo error")
                print("oo00oooo00o0oo0o000oo error")
    def oo00o0o000oooo0o0oo00(self, event):
        timeset()          
    @staticmethod
    def Confirm():
        global oo0o0o00000o00o00000o, oooo000o0ooo0o000oo0o
        confirm_hash = TopFrame.Confirm_hash()          
        if confirm_hash == oo0o0o00000o00o00000o[0]:
            oooo000o0ooo0o000oo0o = True
    @staticmethod
    def Refresh():
        oo0o0000o000ooo0000oo_hash = TopFrame.Refresh_hash()          
        global oo0o0o00000o00o00000o, oo0000ooooo000oo0o0o0
        if oo0o0000o000ooo0000oo_hash == oo0o0o00000o00o00000o[1]:
            oo0000ooooo000oo0o0o0 = True
    @staticmethod
    def o0o000o00oo000ooooo00():
        global oo000o0o0ooooo0oo0oo0 , o0oo00o0000000000o0oo
        global num
        num+=1
        o0000o0o0000000o00o0o = cv2.cvtColor(oo000o0o0ooooo0oo0oo0, cv2.COLOR_BGR2GRAY)
        price = readpic(o0000o0o0000000o00o0o)
        print("price=",price)
        return price
    @staticmethod
    def oooo0oo0oo0o00o00o0oo():
        po = pg.position()
        o000o0oo000o000o0o00o[0][0] = po[0]
        o000o0oo000o000o0o00o[0][1] = po[1]
    @staticmethod
    def o0o00ooo00o000oo000o0():
        po = pg.position()
        o000o0oo000o000o0o00o[1][0] = po[0]
        o000o0oo000o000o0o00o[1][1] = po[1]
    @staticmethod
    def o00oo000o0o00o000o000():
        po = pg.position()
        o000o0oo000o000o0o00o[2][0] = po[0]
        o000o0oo000o000o0o00o[2][1] = po[1]
    @staticmethod
    def oo0ooo00o00oo0oo00ooo():
        po = pg.position()
        o000o0oo000o000o0o00o[3][0] = po[0]
        o000o0oo000o000o0o00o[3][1] = po[1]
    @staticmethod
    def o0o00o0oo0o0ooo00oo0o():
        po = pg.position()
        o000o0oo000o000o0o00o[4][0] = po[0]
        o000o0oo000o000o0o00o[4][1] = po[1]
    @staticmethod
    def ooo0o00o00o000o0oo00o():
        po = pg.position()
        o000o0oo000o000o0o00o[5][0] = po[0]
        o000o0oo000o000o0o00o[5][1] = po[1]
    @staticmethod
    def o0oooo00oo00ooo00o0oo():
        TopFrame.oooo0oo0oo0o00o00o0oo()
    @staticmethod
    def o00000oo0o0o0000000o0():
        TopFrame.o0o00ooo00o000oo000o0()
    @staticmethod
    def o0ooooo0oo0oo00000o00():
        x,y=win32api.GetCursorPos()
        print("x=",x," y=",y)
    @staticmethod
    def o0o0000oooo00000oooo0():
        TopFrame.oo0ooo00o00oo0oo00ooo()
    @staticmethod
    def o0ooo00o00oooo0o00o0o():
        TopFrame.o0o00o0oo0o0ooo00oo0o()
    @staticmethod
    def o0oo0000oo000o0o0o00o():
        TopFrame.ooo0o00o00o000o0oo00o()
    @classmethod
    def o0oo0ooooo000o0oooo00(cls):
        global web_on, ooo000o00oo00o0oo0000, oo0oo00o00000oo00o000, oo0ooo000o0oo0o00o0o0, oooo00oo00o0o00000o00
        global ooo000o00oo00o0oo0000, oo00ooo0o000o00oo00o0, oooo000o0ooo0o000oo0oe, o00oo0000o00o0o00o0oo
        o00oo0000o00o0o00o0oo = True
        if oooo00oo00o0o00000o00 == 1:
            timer = threading.Timer(oo0oo00o00000oo00o000, cls.Tijiao)
            timer.start()
            ooo000o00oo00o0oo0000 = False
            if twice:
                oooo00oo00o0o00000o00 = 2
        elif oooo00oo00o0o00000o00 == 2:
            oooo00oo00o0o00000o00 = 0
            timer = threading.Timer(oo0ooo000o0oo0o00o0o0, cls.Tijiao)
            timer.start()
            ooo000o00oo00o0oo0000 = False
        else:
            cls.Tijiao()
    @staticmethod
    def Tijiao():
        global ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, oooo00oo00o0o00000o00 ,oo00ooo0o000o00oo00o0
        Click(o000o0oo000o000o0o00o[2][0], o000o0oo000o000o0o00o[2][1])
        o000000000ooo0oooo00o = False               
        oo00ooo0o000o00oo00o0 = True        
        global oooo000o0ooo0o000oo0oe
        if not oooo000o0ooo0o000oo0oe:        
            pass
    @classmethod
    def oo0000o0oo0000o0o0o0o(cls):
        global ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, oooo00oo00o0o00000o00, o00oo0000o00o0o00o0oo
        o00oo0000o00o0o00o0oo = True
        if ooooo00o000o0o00oo0o0:
            interval = o0oo0ooo000oo0oo00oo0 - o00000000000o000oo000
        else:
            interval = oooo00o00oo0000oo0o0o - o00000000000o000oo000
        if oooo00oo00o0o00000o00 == 2:            
            if o0000o0o0000000o00o0o <= o0oo000o000000oo00000 - 600:
                print("触发延迟")
                oooo00oo00o0o00000o00 = 0
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                ooo000o00oo00o0oo0000 = False
            elif o0000o0o0000000o00o0o == o0oo000o000000oo00000 - 500 and interval < 0.95:
                oooo00oo00o0o00000o00 = 0
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                ooo000o00oo00o0oo0000 = False
            else:
                oooo00oo00o0o00000o00 = 0
                cls.Tijiao()
                ooo000o00oo00o0oo0000 = False
        elif oooo00oo00o0o00000o00 == 1:
            if o0000o0o0000000o00o0o <= o0ooo0ooo00o0o0o0o0oo - 600:
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                ooo000o00oo00o0oo0000 = False
                if twice:
                    oooo00oo00o0o00000o00 = 2
            elif o0000o0o0000000o00o0o == o0ooo0ooo00o0o0o0o0oo - 500 and interval < 0.95:
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                ooo000o00oo00o0oo0000 = False
                if twice:
                    oooo00oo00o0o00000o00 = 2
            else:
                cls.Tijiao()
                ooo000o00oo00o0oo0000 = False
                if twice:
                    oooo00oo00o0o00000o00 = 2
    @staticmethod
    def o00oo00oo0o0oooo0oo0o():
        Click(o000o0oo000o000o0o00o[3][0], o000o0oo000o000o0o00o[3][1])
        Click(o000o0oo000o000o0o00o[5][0], o000o0oo000o000o0o00o[5][1])
        global ooooo0oo0oo0o0o0oooo0, oo00o00o00o0oo00o0000, o00o00o00000oooo00oo0
        ooooo0oo0oo0o0o0oooo0 = True         
        o00o00o00000oooo00oo0 = 0      
    @staticmethod
    def o000oo000o0oooo00000o():
        Click(o000o0oo000o000o0o00o[4][0], o000o0oo000o000o0o00o[4][1])
    @staticmethod
    def o0ooo0oo00oooooo00000():
        global web_on, o0000o0o0000000o00o0o, o00o00o00000oooo00oo0
        global oooo00oo00o0o00000o00, o0ooo0ooo00o0o0o0o0oo, o0oo000o000000oo00000, o000ooooooooo000o00o0, ooo0000000000ooo00000
        global ooo000o00oo00o0oo0000, oo00ooo0o000o00oo00o0
        global oo0o0o0o00000oo00o0oo, o000oo0o00oooooo000o0, oo0ooo0o0o0oo000ooo00, ooooo0oo0oo0o0o0oooo0
        o00o00o00000oooo00oo0 = 0            
        ooooo0oo0oo0o0o0oooo0 = True            
        print("到这了")
        ooo000o00oo00o0oo0000 = True          
        oo0o0o0o00000oo00o0oo = True           
        if oooo00oo00o0o00000o00 == 1:
            o0ooo0ooo00o0o0o0o0oo = o0000o0o0000000o00o0o + o000ooooooooo000o00o0
            setText(str(o0ooo0ooo00o0o0o0o0oo))
            TopFrame.oo00oo00o0oo00o00o00o()
            Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
            Click(o000o0oo000o000o0o00o[5][0], o000o0oo000o000o0o00o[5][1])
            ooo000o00oo00o0oo0000 = True
            oo00ooo0o000o00oo00o0 = False
            oo0ooo0o0o0oo000ooo00 = False        
        elif oooo00oo00o0o00000o00 == 2 and twice:
            o0oo000o000000oo00000 = o0000o0o0000000o00o0o + ooo0000000000ooo00000
            setText(str(o0oo000o000000oo00000))
            TopFrame.oo00oo00o0oo00o00o00o()
            Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
            Click(o000o0oo000o000o0o00o[5][0], o000o0oo000o000o0o00o[5][1])
            ooo000o00oo00o0oo0000 = True
            oo00ooo0o000o00oo00o0 = False
            oo0ooo0o0o0oo000ooo00 = False        
    @staticmethod
    def o0o0000oo0oo0o0oo0o00():
        global ooooo0oo0oo0o0o0oooo0, o00o00o00000oooo00oo0
        ooooo0oo0oo0o0o0oooo0 = True
        o00o00o00000oooo00oo0 = 0
        o0ooo0ooo00o0o0o0o0oo = o0000o0o0000000o00o0o + o000ooooooooo000o00o0
        setText(str(o0ooo0ooo00o0o0o0o0oo))
        TopFrame.oo00oo00o0oo00o00o00o()
        Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
        Click(o000o0oo000o000o0o00o[5][0], o000o0oo000o000o0o00o[5][1])
    @staticmethod
    def oo00oo00o0oo00o00o00o():
        Click2(o000o0oo000o000o0o00o[6][0], o000o0oo000o000o0o00o[6][1] - 5)
        Click2(o000o0oo000o000o0o00o[6][0], o000o0oo000o000o0o00o[6][1])
        Click2(o000o0oo000o000o0o00o[6][0], o000o0oo000o000o0o00o[6][1])
        Delete()
        Delete()
        if ooooo00o000o0o00oo0o0:
            o0oo0000o000o0o0oo000()      
        else:
            Paste()       
    @staticmethod
    def o00000o0ooo00ooo0oo00():
        global o00ooooo00o00o0000o0o, oo0ooooo00oo0oo000o00, o00o00o00000oooo00oo0, ooooo0oo0oo0o0o0oooo0
        Click(o000o0oo000o000o0o00o[4][0], o000o0oo000o000o0o00o[4][1])
        Click(o000o0oo000o000o0o00o[0][0], o000o0oo000o000o0o00o[0][1])
        Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
        Click(o000o0oo000o000o0o00o[5][0], o000o0oo000o000o0o00o[5][1])
        o00ooooo00o00o0000o0o = True
        oo0ooooo00oo0oo000o00 = 0
        o00o00o00000oooo00oo0 = 0
        ooooo0oo0oo0o0o0oooo0 = True
    @staticmethod
    def o00o0o0o0oooo0o00oo00():
        OperationFrame.o0000oo0o0oooo0oo00o0()
        Click(o000o0oo000o000o0o00o[2][0], o000o0oo000o000o0o00o[2][1])
    @staticmethod
    def oo00o00000oo00000o0oo():
        pg.press('backspace')
    def o00oo000oo0o000000o0o(self, event):
        if not web_on and o000oo000oo0ooooo00oo:             
            self.operationframe.o00o0o0oo00o000oo0o0o()
    @staticmethod
    def oo0o0o000oo0oo00000o0():
        global o000000000ooo0oooo00o, oo0o0o0o00000oo00o0oo, ooo000o00oo00o0oo0000, oo00o00o00o0oo00o0000, ooooo0oo0oo0o0o0oooo0
        if e_on and ooo000o00oo00o0oo0000:
            print("oo0o0o000oo0oo00000o0")
            o000000000ooo0oooo00o = True
            ooooo0oo0oo0o0o0oooo0 = False
            oo00o00o00o0oo00o0000 = True
    @staticmethod
    def o0o0oo00ooo00ooooooo0():
        global o000000000ooo0oooo00o, oo0o0o0o00000oo00o0oo, oo00o00o00o0oo00o0000, ooooo0oo0oo0o0o0oooo0
        if oooo0oooo0ooo000o0oo0 and ooo000o00oo00o0oo0000:
            o000000000ooo0oooo00o = True
        if oooo0oooo0ooo000o0oo0:
            oo00o00o00o0oo00o0000 = True
            ooooo0oo0oo0o0o0oooo0 = False
    @classmethod
    def query(cls):
        global oo00ooo00000oo0o00o00, o0oo00oooo0o00o000o0o
        if not oo00ooo00000oo0o00o00 and not o0oo00oooo0o00o000o0o:
            o0oo00oooo0o00o000o0o = True
            oo00ooo00000oo0o00o00 = True
            setText(str(1000000))            
            TopFrame.oo00oo00o0oo00o00o00o()
            Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
            timer1 = threading.Timer(3, cls.oo000o00o0o00oo0o000o)
            timer1.start()
            timer2 = threading.Timer(5, cls.o00o0000o00ooo00ooo00)
            timer2.start()
        elif oo00ooo00000oo0o00o00 and o0oo00oooo0o00o000o0o:
            Click(o000o0oo000o000o0o00o[7][0], o000o0oo000o000o0o00o[7][1])
            o0oo00oooo0o00o000o0o = False
    @staticmethod
    def oo000o00o0o00oo0o000o():
        global oo00ooo00000oo0o00o00, o0oo00oooo0o00o000o0o
        if o0oo00oooo0o00o000o0o:
            Click(o000o0oo000o000o0o00o[7][0], o000o0oo000o000o0o00o[7][1])
            o0oo00oooo0o00o000o0o = False
    @staticmethod
    def o00o0000o00ooo00ooo00():
        global oo00ooo00000oo0o00o00
        oo00ooo00000oo0o00o00 = False
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
                1: TopFrame.o0oooo00oo00ooo00o0oo, 2: TopFrame.o00000oo0o0o0000000o0, 3: TopFrame.o0ooooo0oo0oo00000o00,
                4: TopFrame.o0o0000oooo00000oooo0, 5: TopFrame.o0ooo00o00oooo0o00o0o,
                6: TopFrame.o0oo0000oo000o0o0o00o, 7: TopFrame.o00oo00oo0o0oooo0oo0o, 8: TopFrame.o00o0o0o0oooo0o00oo00,
                9: (lambda: TopFrame.o00000o0ooo00ooo0oo00()), 10: TopFrame.oo00o00000oo00000o0oo, 11: TopFrame.oo0o0o000oo0oo00000o0,
                12: TopFrame.o0o0oo00ooo00ooooooo0,
                13: TopFrame.query, 14: TopFrame.o0o0000oo0oo0o0oo0o00}                  
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
    def ooo0000000o0oo0oo0o00ground(self, evt):
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
    def o0oo00o0ooo0o00oo0o00(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()
    @classmethod
    def o00oooo00o0o0ooo00o00(cls):
        cls.Close()
    def oo00ooo00o0oooo00oooo(self, event):
        wx.CallAfter(pub.sendMessage, "oo0o0000o000ooo0000oo")
        self.MovePos(event)
        global view
        if not view:
            view = True
            for i in range(len(o000o0oo000o000o0o00o)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(o000o0oo000o000o0o00o)):
                self.posframe[i].Hide()
    def oo0oo0o0o0000oo0o0000(self, event):
        self.MovePos(event)
        self.oo0oo00oo0oo0o00oo000()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)
    def MovePos(self, event):
        global ooo0o000o0o0o0o0o0ooo
        for i in range(5):
            posx, posy = o000o0oo000o000o0o00o[i]
            self.posframe[i].Move(posx - 10, posy - 5)
    def oo0oo00oo0oo0o00oo000(self):
        output = open('pos.log', 'wb')
        pickle.dump(o000o0oo000o000o0o00o, output)
        output.close()
    def o000o0o0o0000oo0oo0o0(self, event):
        ooo0ooooo0o00oooo0000()
    def o000oo00oo0ooo00ooo0o(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global o0ooooooo00o0000oo00o, o00oo0o00oooo00oo0000
        o0ooooooo00o0000oo00o = self.time_choice1.GetString(self.time_choice1.GetSelection())
        o00oo0o00oooo00oo0000 = self.time_choice2.GetString(self.time_choice2.GetSelection())
    def o00o00oo000o0o00000o0(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global o0ooooooo00o0000oo00o, o00oo0o00oooo00oo0000
        o0ooooooo00o0000oo00o = self.time_choice1.GetString(self.time_choice1.GetSelection())
        o00oo0o00oooo00oo0000 = self.time_choice2.GetString(self.time_choice2.GetSelection())
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global oooo00o00oo0000oo0o0o
        time_local = time.localtime(oooo00o00oo0000oo0o0o)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global oooo00o00oo0000oo0o0o, b_time
        if b_time < 9:
            b_time = b_time + 1
        else:
            b_time = 0
        time_local = time.localtime(oooo00o00oo0000oo0o0o)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=oo0o00ooo0oo0o0000o0o,
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
        global o0oo0ooo000oo0oo00oo0
        st = "%s:%s:%s" % (11, 29, o0oo0ooo000oo0oo00oo0)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global o0oo0ooo000oo0oo00oo0
        moni_s = int(o0oo0ooo000oo0oo00oo0)       
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=oo0o00ooo0oo0o0000o0o,
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
        wx.Frame.__init__(self, None, 18, 'Price', size=o0oo00oo000oo0o0oo0oo, pos=o000oooo00o0ooo00o00oframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
                          )
        self.panel = wx.Panel(self, size=o0oo00oo000oo0o0oo0oo)
        self.bmp = wx.StaticBitmap(self.panel, -1)
    def ooo0oooo0o0o000o0o0oo(self, bm):
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
        pub.subscribe(self.ooo0ooo0oo00oo00o0o0o, "close web")        
    def OnClose(self, event):
        global web_on, o0oo0ooo0oo0o0o0oo0oo, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo, oooo000o00000o0ooo0o0
        web_on = False
        o0oo0ooo0oo0o0o0oo0oo = False
        ooooo00o000o0o00oo0o0 = False
        oooooo00o000o00o000oo = False
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
    def ooo0ooo0oo00oo00o0o0o(self):
        global web_on, o0oo0ooo0oo0o0o0oo0oo, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo, oooo000o00000o0ooo0o0
        web_on = False
        o0oo0ooo0oo0o0o0oo0oo = False
        ooooo00o000o0o00oo0o0 = False
        oooooo00o000o00o000oo = False
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
    def ooo0o0oo0oo0oo00000oo(self, event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()
    def Timego(self, event):
        global o0000o0o0000000o00o0o, o0oo0ooo000oo0oo00oo0, oooo00o00oo0000oo0o0o
        self.price.SetLabel("%s" % o0000o0o0000000o00o0o)
        if ooooo00o000o0o00oo0o0:
            self.time.SetLabel("11:29:%s" % int(o0oo0ooo000oo0oo00oo0))
        else:
            timestr1 = time.localtime(oooo00o00oo0000oo0o0o)
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
        global ooo0o0o0o00o000ooo0oo, ooo0o0ooo0000000o0o0o, o0o00ooo0ooo0o0o00o0o, o000oo0oo0ooo0ooooooo
        ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)
        o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)
        ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)
        o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.oooo0oo00o00oo0oo000o, self.timer1)                 
        self.timer1.Start(10)          
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.o0o00ooo0o0oo00o0oo00, self.timer2)   
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
        self.Bind(wx.EVT_BUTTON, self.o0oo0o0000000oo0o0oo0, self.button1)
        self.button2 = wx.Button(panel, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.o00o0oooo000oo0oooooo, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.o0ooooo00ooo000ooo00o, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.ooo0o000o0000ooo00ooo, self.button4)
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
        self.oo0o000o00oo0000oo0o0_save = wx.Button(panel, label="保存策略", size=(60, 35))
        self.oo0o000o00oo0000oo0o0_load = wx.Button(panel, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(panel, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.oo0o000o00oo0000oo0o0_save)
        hbox4.Add(self.oo0o000o00oo0000oo0o0_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)
        oneshot = wx.StaticBox(panel, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajioooo00o00oo0000oo0o0o = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))                              
        self.jiajioooo00o00oo0000oo0o0o.SetRange(40, 55)
        self.jiajioooo00o00oo0000oo0o0o.SetValue(48)
        self.jiajioooo00o00oo0000oo0o0o.SetIncrement(0.1)
        gridsizer1.Add(self.jiajioooo00o00oo0000oo0o0o, pos=(0, 0))
        miao_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))
        o0ooo000000oo0oooo00o_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_o0ooo000000oo0oooo00o = wx.Choice(panel, -1, choices=o0ooo000000oo0oooo00o_choices, size=(68, 25))
        self.select_o0ooo000000oo0oooo00o.SetSelection(0)
        gridsizer1.Add(self.select_o0ooo000000oo0oooo00o, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)
        o0ooo000000oo0oooo00o_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(o0ooo000000oo0oooo00o_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.o0ooo000000oo0oooo00o_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.o0ooo000000oo0oooo00o_time.SetRange(40.0, 57.0)
        self.o0ooo000000oo0oooo00o_time.SetValue(55.0)
        self.o0ooo000000oo0oooo00o_time.SetIncrement(0.1)
        gridsizer1.Add(self.o0ooo000000oo0oooo00o_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)
        secondshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajioooo00o00oo0000oo0o0o2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajioooo00o00oo0000oo0o0o2.SetRange(40, 55)
        self.jiajioooo00o00oo0000oo0o0o2.SetValue(48)
        self.jiajioooo00o00oo0000oo0o0o2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajioooo00o00oo0000oo0o0o2, pos=(0, 0))
        miao_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(panel, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3))
        o0ooo000000oo0oooo00o_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_o0ooo000000oo0oooo00o2 = wx.Choice(panel, -1, choices=o0ooo000000oo0oooo00o_choices2, size=(68, 25))
        self.select_o0ooo000000oo0oooo00o2.SetSelection(0)
        gridsizer2.Add(self.select_o0ooo000000oo0oooo00o2, pos=(1, 0))
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)
        o0ooo000000oo0oooo00o_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(o0ooo000000oo0oooo00o_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.o0ooo000000oo0oooo00o_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.o0ooo000000oo0oooo00o_time2.SetRange(53.0, 57.0)
        self.o0ooo000000oo0oooo00o_time2.SetValue(55.0)
        self.o0ooo000000oo0oooo00o_time2.SetIncrement(0.1)
        gridsizer2.Add(self.o0ooo000000oo0oooo00o_time2, pos=(2, 1))
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
        self.Bind(wx.EVT_CHECKBOX, self.ooo00o0oo00o0o0o0oooo, self.timeview)
        self.Bind(wx.EVT_CHOICE, self.ooo000ooo0o0o00oo0o0o, self.confirm_choice)
        self.Bind(wx.EVT_BUTTON, self.o0o0o00oooooo0o0o0000, self.oo0o000o00oo0000oo0o0_save)
        self.Bind(wx.EVT_BUTTON, self.o000ooo0000oooo0ooooo, self.oo0o000o00oo0000oo0o0_load)
        self.Bind(wx.EVT_BUTTON, self.ooo00o0oo0oo00o00ooo0, self.save_info)
        self.Bind(wx.EVT_CHOICE, self.oo00o0oo0o0o0ooo00ooo, self.select_stractagy)
        self.Bind(wx.EVT_TEXT, self.o00oooooo0ooo0oo0oooo, self.jiajioooo00o00oo0000oo0o0o)
        self.Bind(wx.EVT_TEXT, self.o0o0o0oo0oo00oo0ooo00, self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.o0000oooooo0oo0oooo0o, self.select_o0ooo000000oo0oooo00o)
        self.Bind(wx.EVT_TEXT, self.oooooooooooooooooo000, self.yanchi_time)
        self.Bind(wx.EVT_TEXT, self.o0oo0000oooo00oo0oooo, self.o0ooo000000oo0oooo00o_time)
        self.Bind(wx.EVT_TEXT, self.o0o00o00oo0oooo00o000, self.jiajioooo00o00oo0000oo0o0o2)
        self.Bind(wx.EVT_TEXT, self.o0000oooo0o00o00000oo, self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.ooo0o000oo000o00o0000, self.select_o0ooo000000oo0oooo00o2)
        self.Bind(wx.EVT_TEXT, self.oooooo0oo0o0000oo0ooo, self.yanchi_time2)
        self.Bind(wx.EVT_TEXT, self.o0oo0o00o0000000000o0, self.o0ooo000000oo0oooo00o_time2)
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)
        self.o0o00oo0000oo00ooo0o0frame = YanzhengmaFrame()
    def OnClose(self, event):
        self.Show(False)
    def oooo0oo00o00oo0oo000o(self, event):
        global o00ooooo00o00o0000o0o, web_on, oo00ooo0ooo000oo0000o, o0oo0ooo0oo0o0o0oo0oo, ooooo0oo0oo0o0o0oooo0, o0oo0ooo00o00o0o00oo0, o0oo00oo000oo0o0oo0oo, oo00o00o00o0oo00o0000
        global o00o00o00000oooo00oo0, oo0ooooo00oo0oo000o00, oo000oooo0ooo0000o000
        global o00000o0ooooooo00o0o0 ,oo0000000oo0oooooo00o
        if oo000oooo0ooo0000o000:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(o000oooo00o0ooo00o00oframe)          
                    oo000oooo0ooo0000o000 = False        
                except:
                    pass
        if o00ooooo00o00o0000o0o and oo0ooooo00oo0oo000o00 >= 4:
            try:
                self.oooo0ooo0oo0o000o00oo()
            except:
                pass
            self.oo0000ooo00000000o00o(Pos_price, o0oo0ooo00o00o0o00oo0, "userprice.png")
            image = "userprice.png"
            self.priceframe = PriceFrame(image, o0oo0ooo00o00o0o00oo0, Pos_priceframe)
            self.priceframe.Show(True)
            o00ooooo00o00o0000o0o = False
            oo00ooo0ooo000oo0000o = True
        if o00o00o00000oooo00oo0 >= 5 and not oo00o00o00o0oo00o0000:                    
            o0o00oo000oooo0o00oo0()
        if oo00o00o00o0oo00o0000:
            try:
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        if ooooo0oo0oo0o0o0oooo0:
            oo00o00o00o0oo00o0000 = False
            cut_pic(o00000o0ooooooo00o0o0, o0oo00oo000oo0o0oo0oo, "o0o00oo0000oo00ooo0o0.png")              
            image = "o0o00oo0000oo00ooo0o0.png"
            global o000oo00oo0oo0oo0o0o0
            o000oo00oo0oo0oo0o0o0 = Image.open("o0o00oo0000oo00ooo0o0.png")
            yan_hash = imagehash.dhash(o000oo00oo0oo0oo0o0o0)
            if not oo0000000oo0oooooo00o:      
                oo0000000oo0oooooo00o = yan_hash
            elif yan_hash == oo0000000oo0oooooo00o:         
                pass
            else:
                oo0000000oo0oooooo00o = yan_hash
                try:
                    yan = self.FindWindowById(18)
                    yan.ooo0oooo0o0o000o0o0oo(image)
                    yan.Show()
                except:                 
                    pass
                finally:
                    pass
    def ooooooo00o00o0oooo0oo(self, event):
        global ooooo0oo0oo0o0o0oooo0, oo00o00o00o0oo00o0000
        o0o00oo000oooo0o00oo0()
    def o0o00ooo0o0oo00o0oo00(self, event):
        global oo0ooooo00oo0oo000o00, o00o00o00000oooo00oo0
        oo0ooooo00oo0oo000o00 += 1
        o00o00o00000oooo00oo0 += 1
        file = 'sc_new.png'
        if web_on and oooooo000000ooo00oooo:
            self.lowestframe.Show(True)
        if not os.path.exists(file):
            try:
                self.oooo0ooo0oo0o000o00oo()
            except:
                pass
        if not oooooo000000ooo00oooo or not web_on:
            self.lowestframe.Show(False)
    def oo0000ooo00000000o00o(self, box, size, name):
        global o0oo0ooo00o00o0o00oo0
        region = ImageGrab.grab(box)
        region.resize(size, Image.ANTIALIAS).save(name)
    def oo00ooo00o0oooo0oo00o(self, box, size, name):
        global o0oo0ooo00o00o0o00oo0
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)
    @staticmethod
    def o0000oo0o0oooo0oo00o0():
        try:
            os.remove("sc_new.png")
        except:
            pass
    def oooo0ooo0oo0o000o00oo(self):
        try:
            self.priceframe.Destroy()
        except:
            pass
    def opt(self, event):
        global oooo00oo00o0o00000o00, ooo000o00oo00o0oo0000e, oo00ooo0o000o00oo00o0
        global oooooo000000ooo00oooo        
        global twice, oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, ooo000o00oo00o0oo0000e            
        if o0oo0ooo000oo0oo00oo0 < o000oo0ooo0o0o000oo00 and ooooo00o000o0o00oo0o0 and not twice:        
            twice = False
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
        elif o0oo0ooo000oo0oo00oo0 < o000oo0ooo0o0o000oo00 and ooooo00o000o0o00oo0o0 and twice:        
            twice = True
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
    def o0ooooo00ooo000ooo00o(self, event):
        global oooo00o00oo0000oo0o0o, o0oo0ooo000oo0oo00oo0, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo
        if ooooo00o000o0o00oo0o0:
            o0oo0ooo000oo0oo00oo0 += 0.1
        else:
            oooo00o00oo0000oo0o0o += 0.1
    def ooo0o000o0000ooo00ooo(self, event):
        global oooo00o00oo0000oo0o0o, o0oo0ooo000oo0oo00oo0, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo
        if ooooo00o000o0o00oo0o0:
            o0oo0ooo000oo0oo00oo0 -= 0.1
        else:
            oooo00o00oo0000oo0o0o -= 0.1
    def o0oo0o0000000oo0o0oo0(self, event):
        global oooo00o00oo0000oo0o0o, o0oo0ooo000oo0oo00oo0, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo
        if ooooo00o000o0o00oo0o0:
            o0oo0ooo000oo0oo00oo0 += 1
            if o0oo0ooo000oo0oo00oo0 >= 60:
                o0oo0ooo000oo0oo00oo0 = 0
        else:
            oooo00o00oo0000oo0o0o += 1
    def o00o0oooo000oo0oooooo(self, event):
        global oooo00o00oo0000oo0o0o, o0oo0ooo000oo0oo00oo0, ooooo00o000o0o00oo0o0, oooooo00o000o00o000oo
        if ooooo00o000o0o00oo0o0:
            o0oo0ooo000oo0oo00oo0 -= 1
            if o0oo0ooo000oo0oo00oo0 <= 0:
                o0oo0ooo000oo0oo00oo0 = 60
        else:
            oooo00o00oo0000oo0o0o -= 1
    def ooo00o0oo00o0o0o0oooo(self, event):
        timeSelected = event.GetEventObject()
        global o0oo0ooo0oo0o0o0oo0oo, o000oo000oo0ooooo00oo
        if timeSelected.IsChecked():
            o0oo0ooo0oo0o0o0oo0oo = True
            o000oo000oo0ooooo00oo = True
            if oooooo00o000o00o000oo:
                self.timeframe1.Show(True)
            elif ooooo00o000o0o00oo0o0:
                self.timeframe2.Show(True)
        else:
            o0oo0ooo0oo0o0o0oo0oo = False
            o000oo000oo0ooooo00oo = False
            if oooooo00o000o00o000oo:
                self.timeframe1.Show(False)
            elif ooooo00o000o0o00oo0o0:
                self.timeframe2.Show(False)
    def oo0o0oooo0ooo0o0000o0(self):
        if ooooo00o000o0o00oo0o0:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif oooooo00o000o00o000oo:
            try:
                self.timeframe1.Show(True)
            except:
                pass
    def o00o0o0oo00o000oo0o0o(self):
        try:
            self.timeframe1.Show(False)
        except:
            pass
        try:
            self.timeframe2.Show(False)
        except:
            pass
    def ooo000ooo0o0o00oo0o0o(self, event):
        global e_on, oooo0oooo0ooo000o0oo0
        con = self.confirm_choice.GetSelection()
        if con == 0:
            e_on = True
            oooo0oooo0ooo000o0oo0 = False
        elif con == 1:
            e_on = False
            oooo0oooo0ooo000o0oo0 = True
    def o00oooooo0ooo0oo0oooo(self, event):
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, ooo0o0o0o00o000ooo0oo, o0o00ooo0ooo0o0o00o0o
        tem = self.jiajioooo00o00oo0000oo0o0o.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            o000oo0ooo0o0o000oo00 = tem
            o000oo0ooo0o0o000oo00 = float(o000oo0ooo0o0o000oo00)
            ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)            
        else:
            self.jiajioooo00o00oo0000oo0o0o.SetValue(o000oo0ooo0o0o000oo00)
    def o0o0o0oo0oo00oo0ooo00(self, event):
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            o000ooooooooo000o00o0 = int(tem)
        else:
            self.jiajia_price.SetValue(o000ooooooooo000o00o0)
    def o0000oooooo0oo0oooo0o(self, event):
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0
        select = self.select_o0ooo000000oo0oooo00o.GetString(self.select_o0ooo000000oo0oooo00o.GetSelection())
        if select == u"提前100":
            ooo0oooooo0o0ooo00ooo = 100
        elif select == u"提前200":
            ooo0oooooo0o0ooo00ooo = 200
        else:
            ooo0oooooo0o0ooo00ooo = 0
    def oooooooooooooooooo000(self, event):
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            oo0oo00o00000oo00o000 = float(tem)
        else:
            self.yanchi_time.SetValue(oo0oo00o00000oo00o000)
    def o0oo0000oooo00oo0oooo(self, event):
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, o0o00ooo0ooo0o0o00o0o
        tem = self.o0ooo000000oo0oooo00o_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            oo00000o0oo00o0o0o0o0 = float(tem)
            o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)            
        else:
            self.o0ooo000000oo0oooo00o_time.SetValue(oo00000o0oo00o0o0o0o0)
    def o0o00o00oo0oooo00o000(self, event):
        global ooo0ooo0ooo00oo0ooo0o, oo0ooo000o0oo0o00o0o0, ooo0000000000ooo00000, oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo, ooo0o0ooo0000000o0o0o
        tem = self.jiajioooo00o00oo0000oo0o0o2.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            oo0o0o0o000o0o00ooooo = float(tem)
            ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)            
        else:
            self.jiajioooo00o00oo0000oo0o0o2.SetValue(oo0o0o0o000o0o00ooooo)
    def o0000oooo0o00o00000oo(self, event):
        global ooo0ooo0ooo00oo0ooo0o, oo0ooo000o0oo0o00o0o0, ooo0000000000ooo00000, oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo
        global ooo0oooooo0o0ooo00ooo, oo0oo00o00000oo00o000, o000ooooooooo000o00o0, o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            ooo0000000000ooo00000 = int(tem)
        else:
            self.jiajia_price2.SetValue(ooo0000000000ooo00000)
    def ooo0o000oo000o00o0000(self, event):
        global ooo0ooo0ooo00oo0ooo0o, oo0ooo000o0oo0o00o0o0, ooo0000000000ooo00000, oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo
        select = self.select_o0ooo000000oo0oooo00o2.GetString(self.select_o0ooo000000oo0oooo00o2.GetSelection())
        if select == u"提前100":
            ooo0ooo0ooo00oo0ooo0o = 100
        elif select == u"提前200":
            ooo0ooo0ooo00oo0ooo0o = 200
        else:
            ooo0ooo0ooo00oo0ooo0o = 0
    def oooooo0oo0o0000oo0ooo(self, event):
        global ooo0ooo0ooo00oo0ooo0o, oo0ooo000o0oo0o00o0o0, ooo0000000000ooo00000, oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo
        templist = ['0.%d' % i for i in range(11)]            
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            oo0ooo000o0oo0o00o0o0 = float(tem)
        else:
            self.yanchi_time2.SetValue(oo0ooo000o0oo0o00o0o0)
    def o0oo0o00o0000000000o0(self, event):
        global ooo0ooo0ooo00oo0ooo0o, oo0ooo000o0oo0o00o0o0, ooo0000000000ooo00000, oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo, o000oo0oo0ooo0ooooooo
        tem = self.o0ooo000000oo0oooo00o_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            o00o0o0000oooo0000ooo = float(tem)
            o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)            
        else:
            self.o0ooo000000oo0oooo00o_time2.SetValue(o00o0o0000oooo0000ooo)
    def oo00o0oo0o0o0ooo00ooo(self, event):
        global oooooo000000ooo00oooo        
        global twice, oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, ooo000o00oo00o0oo0000e            
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice = False
            oooooo000000ooo00oooo = True
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
        elif stractagy_selection == u"双枪策略":
            self.oo000000o0ooo00000ooo()
            oooooo000000ooo00oooo = True
            twice = True
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
        else:
            self.o00ooo0o00o0oo0ooo0o0()
            oooooo000000ooo00oooo = False
            twice = False
    def oo000000o0ooo00000ooo(self):      
        if not self.secondsizer_Shown:             
            self.vbox1.Show(self.secondshotSizer)          
            self.secondsizer_Shown = True                
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)           
            self.oneshotsizer_Shown = True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))          
        self.oooo0o0o00oo0oooo000o()
        self.Layout()
    def ss_Hide(self):      
        if self.secondsizer_Shown:             
            self.vbox1.Hide(self.secondshotSizer)             
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))          
        self.oo0o0oooo000o0000o00o()
        self.Layout()
    def o00ooo0o00o0oo0ooo0o0(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)
        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()
    def oo0o0oooo000o0000o00o(self):
        global o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, o000ooooooooo000o00o0, oo0oo00o00000oo00o000, ooo0oooooo0o0ooo00ooo
        self.jiajioooo00o00oo0000oo0o0o.SetValue(48.0)
        self.o0ooo000000oo0oooo00o_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_o0ooo000000oo0oooo00o.SetSelection(0)
        self.yanchi_time.SetValue(0.5)
        o000oo0ooo0o0o000oo00 = 48           
        oo00000o0oo00o0o0o0o0 = 55           
        o000ooooooooo000o00o0 = 700           
        oo0oo00o00000oo00o000 = 0.5         
        ooo0oooooo0o0ooo00ooo = 100            
        global ooo0o0o0o00o000ooo0oo, ooo0o0ooo0000000o0o0o, o0o00ooo0ooo0o0o00o0o, o000oo0oo0ooo0ooooooo
        ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)
        o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)
        ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)
        o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)
    def oooo0o0o00oo0oooo000o(self):
        global o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, o000ooooooooo000o00o0, oo0oo00o00000oo00o000, ooo0oooooo0o0ooo00ooo
        global oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo, ooo0000000000ooo00000, oo0ooo000o0oo0o00o0o0, ooo0ooo0ooo00oo0ooo0o
        self.jiajioooo00o00oo0000oo0o0o.SetValue(40.0)
        self.o0ooo000000oo0oooo00o_time.SetValue(48.0)
        self.jiajia_price.SetValue(500)
        self.select_o0ooo000000oo0oooo00o.SetSelection(2)
        self.yanchi_time.SetValue(0.0)
        self.jiajioooo00o00oo0000oo0o0o2.SetValue(50.0)
        self.o0ooo000000oo0oooo00o_time2.SetValue(55.5)
        self.jiajia_price2.SetValue(700)
        self.select_o0ooo000000oo0oooo00o2.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)
        o000oo0ooo0o0o000oo00 = 40           
        oo00000o0oo00o0o0o0o0 = 48           
        o000ooooooooo000o00o0 = 500           
        oo0oo00o00000oo00o000 = 0.5         
        ooo0oooooo0o0ooo00ooo = 0            
        oo0o0o0o000o0o00ooooo = 50            
        o00o0o0000oooo0000ooo = 55.5           
        ooo0000000000ooo00000 = 700           
        oo0ooo000o0oo0o00o0o0 = 0.5           
        ooo0ooo0ooo00oo0ooo0o = 100              
        global ooo0o0o0o00o000ooo0oo, ooo0o0ooo0000000o0o0o, o0o00ooo0ooo0o0o00o0o, o000oo0oo0ooo0ooooooo
        ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)
        o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)
        ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)
        o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)
    def o0o0o00oooooo0o0o0000(self, event):
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
        global o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, o000ooooooooo000o00o0, oo0oo00o00000oo00o000, ooo0oooooo0o0ooo00ooo
        global oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo, ooo0000000000ooo00000, oo0ooo000o0oo0o00o0o0, ooo0ooo0ooo00oo0ooo0o
        global osl, e_on, oooo0oooo0ooo000o0oo0          
        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0] = 0
            osl[1] = o000oo0ooo0o0o000oo00
            osl[2] = oo00000o0oo00o0o0o0o0
            osl[3] = o000ooooooooo000o00o0
            osl[4] = oo0oo00o00000oo00o000
            osl[5] = ooo0oooooo0o0ooo00ooo
            osl[6] = oo0o0o0o000o0o00ooooo
            osl[7] = o00o0o0000oooo0000ooo
            osl[8] = ooo0000000000ooo00000
            osl[9] = oo0ooo000o0oo0o00o0o0
            osl[10] = ooo0ooo0ooo00oo0ooo0o
            osl[11] = e_on
            osl[12] = oooo0oooo0ooo000o0oo0
        elif self.select_stractagy.GetSelection() == 1:
            osl[0] = 1
            osl[0] = 1
            osl[1] = o000oo0ooo0o0o000oo00
            osl[2] = oo00000o0oo00o0o0o0o0
            osl[3] = o000ooooooooo000o00o0
            osl[4] = oo0oo00o00000oo00o000
            osl[5] = ooo0oooooo0o0ooo00ooo
            osl[6] = oo0o0o0o000o0o00ooooo
            osl[7] = o00o0o0000oooo0000ooo
            osl[8] = ooo0000000000ooo00000
            osl[9] = oo0ooo000o0oo0o00o0o0
            osl[10] = ooo0ooo0ooo00oo0ooo0o
            osl[11] = e_on
            osl[12] = oooo0oooo0ooo000o0oo0
        with open('%s.oo0o000o00oo0000oo0o0' % name, 'wb') as spk:
            pickle.dump(osl, spk)
    def o000ooo0000oooo0ooooo(self, event):
        import os
        path = os.getcwd()
        choice = self.ooo0o000o0ooo0000o0o0(path)
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
        global osl, e_on, oooo0oooo0ooo000o0oo0
        global o000oo0ooo0o0o000oo00, oo00000o0oo00o0o0o0o0, o000ooooooooo000o00o0, oo0oo00o00000oo00o000, ooo0oooooo0o0ooo00ooo
        global oo0o0o0o000o0o00ooooo, o00o0o0000oooo0000ooo, ooo0000000000ooo00000, oo0ooo000o0oo0o00o0o0, ooo0ooo0ooo00oo0ooo0o
        global oooooo000000ooo00oooo        
        global twice, oooo00oo00o0o00000o00, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, ooo000o00oo00o0oo0000e            
        global ooo0o0o0o00o000ooo0oo, o0o00ooo0ooo0o0o00o0o, ooo0o0ooo0000000o0o0o, o000oo0oo0ooo0ooooooo
        try:
            with open(path, 'rb') as loadstr:
                osl = pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:      
            self.ss_Hide()
            twice = False
            oooooo000000ooo00oooo = True
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
            self.select_stractagy.SetSelection(0)
            self.jiajioooo00o00oo0000oo0o0o.SetValue(osl[1])
            self.o0ooo000000oo0oooo00o_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_o0ooo000000oo0oooo00o.SetSelection(0)
            elif osl[5] == 200:
                self.select_o0ooo000000oo0oooo00o.SetSelection(1)
            else:
                self.select_o0ooo000000oo0oooo00o.SetSelection(2)
            o000oo0ooo0o0o000oo00 = osl[1]           
            oo00000o0oo00o0o0o0o0 = osl[2]           
            o000ooooooooo000o00o0 = osl[3]           
            oo0oo00o00000oo00o000 = osl[4]         
            ooo0oooooo0o0ooo00ooo = osl[5]            
            e_on = osl[11]
            oooo0oooo0ooo000o0oo0 = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif oooo0oooo0ooo000o0oo0:
                self.confirm_choice.SetSelection(1)
            ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)
            o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)
            ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)
            o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)
        elif osl[0] == 1:      
            oooooo000000ooo00oooo = True
            twice = True
            oo00ooo0o000o00oo00o0 = True
            ooo000o00oo00o0oo0000 = False
            oooo00oo00o0o00000o00 = 1       
            o000000000ooo0oooo00o = False
            ooo000o00oo00o0oo0000e = False        
            self.oo000000o0ooo00000ooo()
            self.select_stractagy.SetSelection(1)
            self.jiajioooo00o00oo0000oo0o0o.SetValue(osl[1])
            self.o0ooo000000oo0oooo00o_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_o0ooo000000oo0oooo00o.SetSelection(0)
            elif osl[5] == 200:
                self.select_o0ooo000000oo0oooo00o.SetSelection(1)
            else:
                self.select_o0ooo000000oo0oooo00o.SetSelection(2)
            self.jiajioooo00o00oo0000oo0o0o2.SetValue(osl[6])
            self.o0ooo000000oo0oooo00o_time2.SetValue(osl[7])
            self.jiajia_price2.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_o0ooo000000oo0oooo00o2.SetSelection(0)
            elif osl[10] == 200:
                self.select_o0ooo000000oo0oooo00o2.SetSelection(1)
            else:
                self.select_o0ooo000000oo0oooo00o2.SetSelection(2)
            o000oo0ooo0o0o000oo00 = osl[1]           
            oo00000o0oo00o0o0o0o0 = osl[2]           
            o000ooooooooo000o00o0 = osl[3]           
            oo0oo00o00000oo00o000 = osl[4]         
            ooo0oooooo0o0ooo00ooo = osl[5]            
            oo0o0o0o000o0o00ooooo = osl[6]            
            o00o0o0000oooo0000ooo = osl[7]           
            ooo0000000000ooo00000 = osl[8]           
            oo0ooo000o0oo0o00o0o0 = osl[9]           
            ooo0ooo0ooo00oo0ooo0o = osl[10]              
            e_on = osl[11]
            oooo0oooo0ooo000o0oo0 = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif oooo0oooo0ooo000o0oo0:
                self.confirm_choice.SetSelection(1)
            ooo0o0o0o00o000ooo0oo = self.gettime(o000oo0ooo0o0o000oo00)
            o0o00ooo0ooo0o0o00o0o = self.gettime(oo00000o0oo00o0o0o0o0)
            ooo0o0ooo0000000o0o0o = self.gettime(oo0o0o0o000o0o00ooooo)
            o000oo0oo0ooo0ooooooo = self.gettime(o00o0o0000oooo0000ooo)
    def ooo0o000o0ooo0000o0o0(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.oo0o000o00oo0000oo0o0':
                    L.append(os.path.join(root, file))
        return L
    def ooo00o0oo0oo00o00ooo0(self, event):
        pass
    def o00000000000o000oo000(self, a):          
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time          
    def oo000o0000ooo000000oo(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a             
    def gettime(self, choice):                          
        tem = self.oo000o0000ooo000000oo()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.o00000000000o000oo000(b) + float(choice) - int(choice)
        return c                 
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global o0000o0o0000000o00o0o
        st = str(o0000o0o0000000o00o0o)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global o0000o0o0000000o00o0o
        st = str(o0000o0o0000000o00o0o)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=o0o00o0000o0oo0o00o00frame_pos,
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
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.oo0o00o00o00o0o00o000)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()
        self.helplink = hyperlink.HyperLinkCtrl(self.panel, -1, u"查看帮助")
        self.helplink.UnsetToolTip()
        self.helplink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.oo0o00o00o00o0o00o000)
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
        pub.subscribe(self.o0oo0oooooooo0oo0o0o0, "connect")
        self.hashthread = HashThread()
    def o0oo0oooooooo0oo0o0o0(self):
        self.loginbtn.Enable()
        global o0o00o00ooo000o0o00o0, url2, url3          
        if o0o00o00ooo000o0o00o0['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)
            if oo000oo0oooo00ooo000o == 'helong' or oo000oo0oooo00ooo000o == 'yuanjunkai' or oo000oo0oooo00ooo000o == 'zs':
                url2 = 'http://moni.51hupai.org/'
            else:
                url2 = o0o00o00ooo000o0o00o0['url_dianxin']
            url3 = o0o00o00ooo000o0o00o0['url_nodianxin']
        elif o0o00o00ooo000o0o00o0['result'] == 'net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o0o00o00ooo000o0o00o0['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o0o00o00ooo000o0o00o0['result'] == 'wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o0o00o00ooo000o0o00o0['result'] == 'wrong password':
            wx.MessageBox('密码错误', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('登录失败', '用户登录', wx.OK | wx.ICON_ERROR)
    def ooo0000000o0oo0oo0o00(self, event):
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
        global oo000oo0oooo00ooo000o, o0oooo0oooo0000oooo00
        username = self.userText.GetValue()
        password = self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
        else:
            oo000oo0oooo00ooo000o = username               
            o0oooo0oooo0000oooo00 = password
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            event.GetEventObject().Disable()
    def oo0o00o00o00o0o00o000(self, event):
        print("购买")
class UserValidator(wx.Validator):
    ''' o0o00o000o0o00ooo00o0s data as it is entered into the text controls. '''
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)
    def o0o00o000o0o00ooo00o0(self, win):
        return True
    def o0o0o00oo000o0o000o00(self):
        return True
    def oo0o00ooo000oo000oo0o(self):
        return True
    def OnChar(self, event):
        pass
class PassValidator(wx.Validator):
    ''' o0o00o000o0o00ooo00o0s data as it is entered into the text controls. '''
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return PassValidator()
    def o0o00o000o0o00ooo00o0(self, win):
        return True
    def o0o0o00oo000o0o000o00(self):
        return True
    def oo0o00ooo000oo000oo0o(self):
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
        global oooo00o00oo0000oo0o0o, o0oo0ooo000oo0oo00oo0
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            oooo00o00oo0000oo0o0o += b - a                
            o0oo0ooo000oo0oo00oo0 += b - a
            if o0oo0ooo000oo0oo00oo0 >= 60:
                o0oo0ooo000oo0oo00oo0 = 0
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
        Click2(o000o0oo000o000o0o00o[6][0] + 17, o000o0oo000o000o0o00o[6][1])
        for i in range(15):
            Delete()
        if ooooo00o000o0o00oo0o0:
            o0oo0000o000o0o0oo000()
        else:
            Paste()      
        Click(o000o0oo000o000o0o00o[1][0], o000o0oo000o000o0o00o[1][1])
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
class o00ooo0oo00o0oo00o0o0Thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()
    def run(self):
        for i in range(1000000):
            global o0oo00o0000000000o0oo
            if o0oo00o0000000000o0oo:
                try:
                    print("找着呢")
                    o00ooo0oo00o0oo00o0o0()      
                    time.sleep(0.1)          
                except:
                    logging.error("o00ooo0oo00o0oo00o0o0thread error")
                    print("o00ooo0oo00o0oo00o0o0thread error")
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
            time.sleep(0.05)
            global oooo00oo00o0o00000o00
            if oooo00oo00o0o00000o00 == 2:
                try:
                    oooo00o00o00ooo00oo00()
                except:
                    print("查找确认出错")
    def pause(self):
        self.__flag.clear()                   
    def resume(self):
        self.__flag.set()                    
    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            
class oo0o0000o000ooo0000ooThread(Thread):
    def __init__(self, *args, **kwargs):
        super(oo0o0000o000ooo0000ooThread, self).__init__(*args, **kwargs)
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
            time.sleep(0.05)
            try:
                oo0o00oo000o0ooooooo0()
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
        global oo000oo0oooo00ooo000o, o0o00o00ooo000o0o00o0
        o0o00o00ooo000o0o00o0 = o000oo0000o0oo0o000o0()
        print(o0o00o00ooo000o0o00o0)
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
            ooo0ooooo0o00oooo0000()
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global oo0oo0oooo00oo00oo00o, oo0oo0oooo00oo0ooo00o, o0ooo00ooooo00ooooo0o, o0000o0o0000000o00o0o, o0ooo0ooo00o0o0o0o0oo, o0oo000o000000oo00000
        global o0oo0ooo000oo0oo00oo0, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, ooo000o00oo00o0oo0000, o000000000ooo0oooo00o, ooo0o0ooo0000000o0o0o, o000oo0oo0ooo0ooooooo
        global ooo0oooooo0o0ooo00ooo, ooo0ooo0ooo00oo0ooo0o, oooo00oo00o0o00000o00, o000000000ooo0oooo00o, oo00ooo0o000o00oo00o0, ooo000o00oo00o0oo0000, ooo000o00oo00o0oo0000e
        for i in range(10000000):
            time.sleep(0.05)              
            if ooo000o00oo00o0oo0000 and oooooo000000ooo00oooo and oooooo00o000o00o000oo and o000000000ooo0oooo00o:                       
                if oooo00oo00o0o00000o00 == 1 and oooo00o00oo0000oo0o0o >= o0o00ooo0ooo0o0o00o0o and not ooo000o00oo00o0oo0000e:            
                    ooo000o00oo00o0oo0000 = False
                    TopFrame.oo0000o0oo0000o0o0o0o()        
                    ooo000o00oo00o0oo0000 = False
                    logging.info("Rone_o0ooo000000oo0oooo00o %s%s%s%s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, oooooo00o000o00o000oo, o000000000ooo0oooo00o))
                    logging.info("Rone_o0ooo000000oo0oooo00o %s%s%s" % (oooo00oo00o0o00000o00, oooo00o00oo0000oo0o0o, o0o00ooo0ooo0o0o00o0o))
                    ooo000o00oo00o0oo0000e = True
                elif oooo00oo00o0o00000o00 == 2 and oooo00o00oo0000oo0o0o >= o000oo0oo0ooo0ooooooo:            
                    ooo000o00oo00o0oo0000 = False
                    TopFrame.oo0000o0oo0000o0o0o0o()        
                    ooo000o00oo00o0oo0000 = False
                    logging.info("Rsecond_o0ooo000000oo0oooo00o %s%s%s%s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, oooooo00o000o00o000oo, o000000000ooo0oooo00o))
                    logging.info("Rsecond_o0ooo000000oo0oooo00o %s%s%s" % (oooo00oo00o0o00000o00, oooo00o00oo0000oo0o0o, o000oo0oo0ooo0ooooooo))
                elif oooo00oo00o0o00000o00 == 1 and o0000o0o0000000o00o0o >= o0ooo0ooo00o0o0o0o0oo - 300 - ooo0oooooo0o0ooo00ooo and oooo00o00oo0000oo0o0o <= o0o00ooo0ooo0o0o00o0o - oo0oo00o00000oo00o000 and not ooo000o00oo00o0oo0000e:        
                    ooo000o00oo00o0oo0000 = False
                    ooo000o00oo00o0oo0000 = False                        
                    TopFrame.o0oo0ooooo000o0oooo00()        
                    logging.info("Rone_o0ooo000000oo0oooo00o %s%s%s%s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, oooooo00o000o00o000oo, o000000000ooo0oooo00o))
                    logging.info("Rone_o0ooo000000oo0oooo00o %s%s%s" % (oooo00oo00o0o00000o00, o0000o0o0000000o00o0o, o0ooo0ooo00o0o0o0o0oo))
                    ooo000o00oo00o0oo0000e = True
                elif oooo00oo00o0o00000o00 == 2 and o0000o0o0000000o00o0o >= o0oo000o000000oo00000 - 300 - ooo0ooo0ooo00oo0ooo0o and oooo00o00oo0000oo0o0o <= o000oo0oo0ooo0ooooooo - oo0ooo000o0oo0o00o0o0:        
                    ooo000o00oo00o0oo0000 = False
                    ooo000o00oo00o0oo0000 = False                        
                    TopFrame.o0oo0ooooo000o0oooo00()        
                    logging.info("Rsecond_o0ooo000000oo0oooo00o %s%s%s%s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, oooooo00o000o00o000oo, o000000000ooo0oooo00o))
                    logging.info("Rsecond_o0ooo000000oo0oooo00o %s%s%s" % (oooo00oo00o0o00000o00, o0000o0o0000000o00o0o, o0oo000o000000oo00000))
            if oooooo000000ooo00oooo and oooooo00o000o00o000oo and oo00ooo0o000o00oo00o0:                       
                if oooo00oo00o0o00000o00 == 1 and ooo0o0o0o00o000ooo0oo <= oooo00o00oo0000oo0o0o <= ooo0o0o0o00o000ooo0oo + 0.6:            
                    TopFrame.o0ooo0oo00oooooo00000()        
                    o0ooo0ooo00o0o0o0o0oo = o0000o0o0000000o00o0o + o000ooooooooo000o00o0
                    ooo000o00oo00o0oo0000 = True   
                    logging.info("Rone_oo000oo0o000000o0o0oo %s%s" % (oooooo000000ooo00oooo, oooooo00o000o00o000oo))
                    logging.info("Rone_oo000oo0o000000o0o0oo %s%s" % (o000oo0ooo0o0o000oo00, ooo0o0o0o00o000ooo0oo))
                elif oooo00oo00o0o00000o00 == 2 and twice and ooo0o0ooo0000000o0o0o <= oooo00o00oo0000oo0o0o:            
                    TopFrame.o0ooo0oo00oooooo00000()        
                    o0oo000o000000oo00000 = o0000o0o0000000o00o0o + ooo0000000000ooo00000
                    ooo000o00oo00o0oo0000 = True
                    logging.info("Rsecond_oo000oo0o000000o0o0oo %s%s" % (oooooo000000ooo00oooo, oooooo00o000o00o000oo))
                    logging.info("Rsecond_oo000oo0o000000o0o0oo %s%s" % (oo0o0o0o000o0o00ooooo, ooo0o0ooo0000000o0o0o))
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global o0oo0ooo000oo0oo00oo0, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, ooo000o00oo00o0oo0000, o0ooo0ooo00o0o0o0o0oo, o0oo000o000000oo00000, o000ooooooooo000o00o0, ooo0000000000ooo00000
        global oooo00oo00o0o00000o00, o000000000ooo0oooo00o, ooo0oooooo0o0ooo00ooo, ooo0ooo0ooo00oo0ooo0o, ooo000o00oo00o0oo0000e
        for i in range(10000000):
            time.sleep(0.05)              
            if ooo000o00oo00o0oo0000 and oooooo000000ooo00oooo and ooooo00o000o0o00oo0o0 and o000000000ooo0oooo00o:                     
                if oooo00oo00o0o00000o00 == 1 and o0oo0ooo000oo0oo00oo0 >= oo00000o0oo00o0o0o0o0 and not ooo000o00oo00o0oo0000e:            
                    TopFrame.oo0000o0oo0000o0o0o0o()        
                    logging.info("moni one_o0ooo000000oo0oooo00o %s %s %s %s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, o000000000ooo0oooo00o))
                    logging.info("moni one_o0ooo000000oo0oooo00o %s %s %s" % (oooo00oo00o0o00000o00, o0oo0ooo000oo0oo00oo0, oo00000o0oo00o0o0o0o0))
                    ooo000o00oo00o0oo0000 = False
                    ooo000o00oo00o0oo0000e = True         
                elif oooo00oo00o0o00000o00 == 2 and o0oo0ooo000oo0oo00oo0 >= o00o0o0000oooo0000ooo and twice:            
                    TopFrame.oo0000o0oo0000o0o0o0o()        
                    logging.info("moni1 second_o0ooo000000oo0oooo00o %s %s %s %s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, o000000000ooo0oooo00o))
                    logging.info("moni second_o0ooo000000oo0oooo00o %s %s %s" % (oooo00oo00o0o00000o00, o0oo0ooo000oo0oo00oo0, o00o0o0000oooo0000ooo))
                    ooo000o00oo00o0oo0000 = False
                elif oooo00oo00o0o00000o00 == 1 and o0000o0o0000000o00o0o >= o0ooo0ooo00o0o0o0o0oo - 300 - ooo0oooooo0o0ooo00ooo and not ooo000o00oo00o0oo0000e:        
                    ooo000o00oo00o0oo0000 = False                        
                    TopFrame.o0oo0ooooo000o0oooo00()        
                    logging.info("moni one_o0ooo000000oo0oooo00o %s %s %s %s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, o000000000ooo0oooo00o))
                    logging.info("moni one_o0ooo000000oo0oooo00o %s %s %s" % (oooo00oo00o0o00000o00, o0000o0o0000000o00o0o, o0ooo0ooo00o0o0o0o0oo))
                    ooo000o00oo00o0oo0000e = True         
                elif oooo00oo00o0o00000o00 == 2 and o0000o0o0000000o00o0o >= o0oo000o000000oo00000 - 300 - ooo0ooo0ooo00oo0ooo0o and twice:        
                    ooo000o00oo00o0oo0000 = False                        
                    TopFrame.o0oo0ooooo000o0oooo00()        
                    logging.info("moni2 second_o0ooo000000oo0oooo00o %s%s%s%s" % (ooo000o00oo00o0oo0000, oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0, o000000000ooo0oooo00o))
                    logging.info("moni second_o0ooo000000oo0oooo00o %s%s%s" % (oooo00oo00o0o00000o00, o0000o0o0000000o00o0o, o0oo000o000000oo00000))
            if oooooo000000ooo00oooo and ooooo00o000o0o00oo0o0 and oo00ooo0o000o00oo00o0:                     
                if oooo00oo00o0o00000o00 == 1 and o000oo0ooo0o0o000oo00 <= o0oo0ooo000oo0oo00oo0 <= o000oo0ooo0o0o000oo00 + 0.6:            
                    TopFrame.o0ooo0oo00oooooo00000()        
                    print("第一次")
                    o0ooo0ooo00o0o0o0o0oo = o0000o0o0000000o00o0o + o000ooooooooo000o00o0
                    ooo000o00oo00o0oo0000 = True
                    logging.info("moni one_oo000oo0o000000o0o0oo %s %s" % (oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0))
                    logging.info("moni one_oo000oo0o000000o0o0oo %s %s" % (o000oo0ooo0o0o000oo00, o0oo0ooo000oo0oo00oo0))
                elif oooo00oo00o0o00000o00 == 2 and twice and oo0o0o0o000o0o00ooooo < o0oo0ooo000oo0oo00oo0:
                    TopFrame.o0ooo0oo00oooooo00000()        
                    print("第二次")
                    o0oo000o000000oo00000 = o0000o0o0000000o00o0o + ooo0000000000ooo00000
                    ooo000o00oo00o0oo0000 = True
                    logging.info("moni second_oo000oo0o000000o0o0oo %s %s" % (oooooo000000ooo00oooo, ooooo00o000o0o00oo0o0))
                    logging.info("moni second_oo000oo0o000000o0o0oo %s %s" % (oo0o0o0o000o0o00ooooo, o0oo0ooo000oo0oo00oo0))
class Infoframe(wx.Frame):
    def __init__(self, name, user, psd):               
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
o000000oo0oo00o0o0000 = "本地IE"
class Guopaiframe(wx.Dialog):
    def __init__(self, name):               
        wx.Frame.__init__(self, None, -1, name, size=(195, 265), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(195, 270))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.o000000oo0oo00o0o0000 = o000000oo0oo00o0o0000
        self.dianxin = wx.Button(self.panel, label="上海电信", pos=(20, 10), size=(140, 60))
        self.nodianxin = wx.Button(self.panel, label="非电信", pos=(20, 80), size=(140, 60))
        self.userweb = wx.Button(self.panel, label=self.o000000oo0oo00o0o0000, pos=(20, 150), size=(140, 60))
        self.dianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.nodianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.userweb.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_BUTTON, self.Dianxin, self.dianxin)
        self.Bind(wx.EVT_BUTTON, self.o00o00ooo0o0o0oo0oooo, self.nodianxin)
        self.Bind(wx.EVT_BUTTON, self.UserWeb, self.userweb)
        self.Center()
        self.ShowModal()
    def Dianxin(self, event):
        wx.CallAfter(pub.sendMessage, "open dianxin")
        self.Destroy()
        event.Skip()
    def o00o00ooo0o0o0oo0oooo(self, event):
        wx.CallAfter(pub.sendMessage, "open nodianxin")
        self.Destroy()
        event.Skip()
    def UserWeb(self, event):
        global o000000oo0oo00o0o0000, oooooo00o000o00o000oo
        if o000000oo0oo00o0o0000 == '本地IE' and not oooooo00o000o00o000oo:
            oooooo00o000o00o000oo = True            
            o000000oo0oo00o0o0000 = '关闭辅助'
            wx.CallAfter(pub.sendMessage, "open userweb")
        else:
            o000000oo0oo00o0o0000 = '本地IE'
            oooooo00o000o00o000oo = False            
            TopFrame.Close()
            try:
                yan = self.FindWindowById(18)
                yan.Destroy()
                global ooo0o0oo00ooo0o0o0000
                print("关闭成功")
                ooo0o0oo00ooo0o0o0000 = False
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
    o00o0o0o000o00o0oo0o0()
    o0ooooo0ooooo00oo0o0o()            
    app = SketchApp()
    confirmthread = confirmThread()       
    oo0o0000o000ooo0000oothread = oo0o0000o000ooo0000ooThread()       
    finposthread = o00ooo0oo00o0oo00o0o0Thread()        
    cutimgthread = cutimgThread()        
    app.MainLoop()
