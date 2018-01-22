'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
version = '5.11s'
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
oo0o0ooo00oo000ooo0oo = False        
o00o000o00oo00o00o0o0 = False             
oo0ooo00ooo0oo00o0000 = False              
o0o0o00oo0ooooo0ooo0o = True            
ooooo0ooo0oo00oo00000 = True          
oo0o0oo000o0oo0o000o0 = 0                              
oo0o0oo0oo000o0o0oooo = False          
o000000oo0ooo0ooo0000 = 0               
oo00000o000oooooo000o = 0               
web_on = False             
o00ooo0o0o0oooo00000o = False           
operation_show = False           
o0000ooo00o00000oo000 = False               
import time
o00000o0o00oooo0000oo = time.time()          
b_time = 0          
moni_minute = 29
oo000oo00o00oo0o00o0o = 0
oo0o0ooo00o0o0o0oo00o_time = 0        
o0oo0oo0o0o0o000o0o0o = 0       
oo0ooooo000o0oo00000o = 0      
oo00o00oo0o0oo0o0o0oo = False                          
oooo0oooo0000o0000o00 = False
oo0o00oooo000o0oo0o0o = 53          
ooo0000000000o0oo0o00 = 0.0          
o000000ooooo0oo00o0o0 = True          
oo00o0o0o0oo0000ooooo = False                 
delay = False        
delay_time = 0.5          
o00000o00o000oooo0oo0 = False          
ooo0oo00ooooo00o0o0oo = True           
pricelist = [80000 + i * 100 for i in range(400)]          
IDnumber = 0        
account = 0       
passwd = 0      
oo00000oooo0o0o0o00o0 = 0
import pyautogui as pg
def o0oo00o000oooooo00000():
    with open('dick.dl', 'rb') as dick:
        global oo0000o00oo0000ooooo0
        oo0000o00oo0000ooooo0 = pickle.load(dick)                 
    with open('cf.btn', 'rb') as cf:
        global ooooooo00oo0ooooo00oo
        ooooooo00oo0ooooo00oo = pickle.load(cf)                            
    with open("target.tkl", 'rb')  as tar:
        global o0oo000o00000o0oooooo
        o0oo000o00000o0oooooo = pickle.load(tar)            
o0oo0o000o0ooo0000oo0 = 48           
o0oo000o0oooo0oooooo0 = 55           
oo000o0o00o00o0o0ooo0 = 1000000000000             
o00ooo00oo000000o0000 = 1000000000000             
oo00oo0o00000000ooo0o = 700           
oo0oo000ooooo0oo00ooo = 0.5         
o0ooooooo0oo00ooooo0o = 100            
ooooo0ooo0o00ooo0o00o = 48            
ooo0oo0o0o00o0o0ooo0o = 55           
o00o0o0oo0oooo0ooo0o0 = 1000000000000             
o0o0ooo00o0o0000oo0o0 = 1000000000000             
ooo000000o0o0o0ooo00o = 600           
o0000ooo0oooo0000oooo = 0.5           
ooo0000o0oo0o0000oo00 = 100              
osl = [0] * 15                          
o0oo0000oo00o0o00o000 = True                      
o0oooooo0000ooo0o0o0o = False                  
ooo0oo0000000o0oo000o = 93400         
o00oo000oo00oooo0o000 = 0         
ooo00o00oooo0o000o0oo = 0         
own_price = 0        
o0oo000o00oooo00000o0 = False           
e_on = True                  
o000ooo0000ooo0o0o0oo = False                   
twice = False          
o0oo00oooo0ooooo00o0o = 1                         
oo0o000000o0o0o0000oo = False             
websize = [902, 700]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2          
Py2 = Pxy[1] / 2
Px = (Pxy[0] - websize[0]) / 2 - 80
Py = (Pxy[1] - websize[1]) / 2
P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]]               
P_relative2 = [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
oo0oo0o0o00o0000oooo0 = [[0, 0] for i in range(len(P_relative))]
for i in range(len(oo0oo0o0o00o0000oooo0)):
    oo0oo0o0o00o0000oooo0[i][0] = Px1 + P_relative[i][0]
    oo0oo0o0o00o0000oooo0[i][1] = Py2 + P_relative[i][1]
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
ooooooo000o000oooooo0frame = 245
oo0oo00o00o0ooo0000ooframe = 290
oooo0oo00o0oo0oo0oo0oframe_pos = [ooooooo000o000oooooo0frame, oo0oo00o00o0ooo0000ooframe]
px_ooo0oo00ooooooooo0o00frame = 400 - 215
py_ooo0oo00ooooooooo0o00frame = 460
px_mini = 200
py_mini = 40
o0oo0oo0o00oo0oo00000 = [400, 80]
oooooo0ooo0o0o0o0000o = [400, 220]
Timesize = [200, 50]
oooo0oo00o0oo0oo0oo0o_area = [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py]
o00o000000ooo00oo00o0 = [396 - 150, 11 - 100, 396 + 150, 11 + 100]
oo0000000oooooo0oo0o0 = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
yan_oo0000000oooooo0oo0o0 = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
oo00oo0o00o0oo000o000 = [0,0]
webview_pos = [-25,0]                      
Px_price = Px + px_price
Py_price = Py + py_price
Pos_price = [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini]               
oo0oooo0oo0ooooo00oo0 = []           
Px_priceframe = Px + px_priceframe
Py_priceframe = Py + py_priceframe
Pos_priceframe = [Px_priceframe, Py_priceframe]
Px_timeframe = px_timeframe + Px
Py_timeframe = py_timeframe + Py
o0o0o00ooo0o00oo00o0o = [Px_timeframe, Py_timeframe]
o0oo00o000o000ooo0o00 = [Px + 40, Py + 480]
Px_ooo0oo00ooooooooo0o00frame = Px + px_ooo0oo00ooooooooo0o00frame
Py_ooo0oo00ooooooooo0o00frame = Py + py_ooo0oo00ooooooooo0o00frame
oo0oooo0oo0ooooo00oo0frame = [Px_ooo0oo00ooooooooo0o00frame, Py_ooo0oo00ooooooooo0o00frame]
ooooooo000o000oooooo0 = 0                         
oo0oo00o00o0ooo0000oo = 0            
oo0ooooo0oo000ooo0ooo = Px + ooooooo000o000oooooo0
o0ooo0o0o0000oo00o0oo = Py + oo0oo00o00o0ooo0000oo
oooo0oo00o0oo0oo0oo0o_sizex = 82           
oooo0oo00o0oo0oo0oo0o_sizey = 16
oo0o00000o00oo000oooo =oo0ooooo0oo000ooo0ooo-25             
o0oo00o0000oo00o0oooo = o0ooo0o0o0000oo00o0oo+17
currenttime_sizex = 132
currenttime_sizey = 13
o0o0000oooooo00o00ooo = 49                
oo0o0o0o0o0oo0o0oo0oo = 0
px_confirm = 656
py_confirm = 475
Px_confirm = Px + px_confirm
Py_confirm = Py + py_confirm
confirm_sizex = 113
confirm_sizey = 28
oooo0o000o0oo0ooooooo = False          
ooo0o0o00o000o0000000 = False          
oooo0o000o0oo0oooooooe = False             
px_ooo000oo0o0ooo0o0o0o0 = 550
py_ooo000oo0o0ooo0o0o0o0 = 413
Px_ooo000oo0o0ooo0o0o0o0 = Px + px_ooo000oo0o0ooo0o0o0o0
Py_ooo000oo0o0ooo0o0o0o0 = Py + py_ooo000oo0o0ooo0o0o0o0
ooo000oo0o0ooo0o0o0o0_sizex = 108
ooo000oo0o0ooo0o0o0o0_sizey = 21
o000o0o0000o00o00o0o0 = False          
oo0o00ooo0oo0oooo0o00 = False          
o000o0o0000o00o00o0o0e = False             
oo0o0oo0oooo0oo00oo0o = False        
o0o000o0oooo00o00o0oo_interval = False        
oo00ooooo000000o0o000 = False      
o0000o000o00oo0oo000o = False            
import numpy as np
o0o0o000o00ooo00o00oo = [oo0ooooo0oo000ooo0ooo - 10, o0ooo0o0o0000oo00o0oo - 100, oo0ooooo0oo000ooo0ooo + 600, o0ooo0o0o0000oo00o0oo + 120]
oo0o0o000o0oo0o0o0oo0 = []
nptemp = []
ooo00000ooo0ooo000o0o = np.array(nptemp)       
o00oooooo00o0o0o0o000 = np.array(nptemp)       
o0oo0ooo00o00oo000o00 = np.array(nptemp)         
impos_ooo0oo00ooooooooo0o00 = np.array(nptemp)       
o00o00000o0oo000o0o00 = np.array(nptemp)         
o0o00oo0oo00o0000oo00 = np.array(nptemp)        
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
yimg = ImageGrab.grab().save("ooo0oo00ooooooooo0o00.png")
o0oooo0ooo0o0oo000o00 = Image.open("ooo0oo00ooooooooo0o00.png")                         
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
def o00000000oooo0000ooo0():
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
def oo000o0oooo00oo0ooo0o():
    sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    global o0oo000o00000o0oooooo
    template = o0oo000o00000o0oooooo[2]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    global ooooooo000o000oooooo0, oo0oo00o00o0ooo0000oo, o0o0000oooooo00o00ooo, oo0o0o0o0o0oo0o0oo0oo, oo0ooooo0oo000ooo0ooo, o0ooo0o0o0000oo00o0oo, Px, Py
    global o00o000000ooo00oo00o0, oo0000000oooooo0oo0o0, o0o0o00ooo0o00oo00o0o, o0oo00o000o000ooo0o00, oo0oooo0oo0ooooo00oo0, oo0oooo0oo0ooooo00oo0frame, yan_oo0000000oooooo0oo0o0
    global oo0o0o000o0oo0o0o0oo0, o0o0o000o00ooo00o00oo          
    global oo0oo0o0o00o0000oooo0, o00o000000ooo00oo00o0, oo0000000oooooo0oo0o0, o0o0o00ooo0o00oo00o0o, o0oo00o000o000ooo0o00, oo0oooo0oo0ooooo00oo0, oo0oooo0oo0ooooo00oo0frame, yan_oo0000000oooooo0oo0o0
    global oo0o00000o00oo000oooo,o0oo00o0000oo00o0oooo           
    global oo00oo0o00o0oo000o000
    if max_val > 0.9:          
        ooooooo000o000oooooo0 = max_loc[0] + o0o0000oooooo00o00ooo
        oo0oo00o00o0ooo0000oo = max_loc[1] + oo0o0o0o0o0oo0o0oo0oo
        oo0ooooo0oo000ooo0ooo = ooooooo000o000oooooo0
        o0ooo0o0o0000oo00o0oo = oo0oo00o00o0ooo0000oo
        oo0o00000o00oo000oooo = oo0ooooo0oo000ooo0ooo -27             
        o0oo00o0000oo00o0oooo = o0ooo0o0o0000oo00o0oo -14
        oo00oo0o00o0oo000o000 = [ooooooo000o000oooooo0-9,oo0oo00o00o0ooo0000oo+84]
        for i in range(len(oo0oo0o0o00o0000oooo0)):
            oo0oo0o0o00o0000oooo0[i][0] = oo0ooooo0oo000ooo0ooo + P_relative2[i][0]
            oo0oo0o0o00o0000oooo0[i][1] = o0ooo0o0o0000oo00o0oo + P_relative2[i][1]
        o00o000000ooo00oo00o0 = [396 - 150 + oo0ooooo0oo000ooo0ooo, 11 - 100 + o0ooo0o0o0000oo00o0oo, 396 + 150 + oo0ooooo0oo000ooo0ooo,
                        11 + 100 + o0ooo0o0o0000oo00o0oo]
        oo0000000oooooo0oo0o0 = [505 - 80 + oo0ooooo0oo000ooo0ooo, 68 - 50 + o0ooo0o0o0000oo00o0oo, 505 + 80 + oo0ooooo0oo000ooo0ooo,
                        68 + 50 + o0ooo0o0o0000oo00o0oo]
        yan_oo0000000oooooo0oo0o0 = [205 - 80 + oo0ooooo0oo000ooo0ooo, 68 - 50 + o0ooo0o0o0000oo00o0oo, 405 + 80 + oo0ooooo0oo000ooo0ooo,
                            68 + 50 + o0ooo0o0o0000oo00o0oo]
        o0oo00o000o000ooo0o00 = [192 - 344 + oo0ooooo0oo000ooo0ooo, 514 - 183 + o0ooo0o0o0000oo00o0oo]
        oo0oooo0oo0ooooo00oo0 = [oo0oo0o0o00o0000oooo0[5][0] - 277, oo0oo0o0o00o0000oooo0[5][1] - 65, oo0oo0o0o00o0000oooo0[5][0] - 97,
                          oo0oo0o0o00o0000oooo0[5][1] + 45]           
        oo0oooo0oo0ooooo00oo0frame = [oo0ooooo0oo000ooo0ooo + 297, o0ooo0o0o0000oo00o0oo - 283]            
        global ooo0oo00ooooo00o0o0oo, ooooo0ooo0oo00oo00000
        ooo0oo00ooooo00o0o0oo = False        
        ooooo0ooo0oo00oo00000 = True        
        lowest = [oo0ooooo0oo000ooo0ooo, o0ooo0o0o0000oo00o0oo,  oooo0oo00o0oo0oo0oo0o_sizex+oo0ooooo0oo000ooo0ooo, oooo0oo00o0oo0oo0oo0o_sizey+o0ooo0o0o0000oo00o0oo]
        currenttime = [oo0o00000o00oo000oooo,o0oo00o0000oo00o0oooo,oo0o00000o00oo000oooo+currenttime_sizex,o0oo00o0000oo00o0oooo+currenttime_sizey]
        dis_x=50
        dis_y=100
        x1 = oo0ooooo0oo000ooo0ooo - dis_x         
        y1 = o0ooo0o0o0000oo00o0oo - dis_y
        cal_area = [lowest, o00o000000ooo00oo00o0, oo0000000oooooo0oo0o0, oo0oooo0oo0ooooo00oo0, yan_oo0000000oooooo0oo0o0 , currenttime]          
        oo0o0o000o0oo0o0o0oo0 = []
        o0o0o000o00ooo00o00oo = [oo0ooooo0oo000ooo0ooo - dis_x, o0ooo0o0o0000oo00o0oo - dis_y, oo0ooooo0oo000ooo0ooo + 600, o0ooo0o0o0000oo00o0oo + 120]
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            oo0o0o000o0oo0o0o0oo0.append(temp)
def oo0oo0o0oo00000oooo00(area):                          
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
    global oo0o0o000o0oo0o0o0oo0, o0o0o000o00ooo00o00oo, ooo00000ooo0ooo000o0o, ooo0oooooooo0000oo0o0, o00oooooo00o0o0o0o000, o0oo0ooo00o00oo000o00, o00o00000o0oo000o0o00,o0o00oo0oo00o0000oo00
    img = oo0oo0o0oo00000oooo00(o0o0o000o00ooo00o00oo)           
    img = np.asarray(img)              
    ooo00000ooo0ooo000o0o = img[oo0o0o000o0oo0o0o0oo0[0][1]:oo0o0o000o0oo0o0o0oo0[0][3], oo0o0o000o0oo0o0o0oo0[0][0]:oo0o0o000o0oo0o0o0oo0[0][2]]      
    o00oooooo00o0o0o0o000 = img[oo0o0o000o0oo0o0o0oo0[1][1]:oo0o0o000o0oo0o0o0oo0[1][3], oo0o0o000o0oo0o0o0oo0[1][0]:oo0o0o000o0oo0o0o0oo0[1][2]]      
    o0oo0ooo00o00oo000o00 = img[oo0o0o000o0oo0o0o0oo0[2][1]:oo0o0o000o0oo0o0o0oo0[2][3], oo0o0o000o0oo0o0o0oo0[2][0]:oo0o0o000o0oo0o0o0oo0[2][2]]
    ooo0oooooooo0000oo0o0 = img[oo0o0o000o0oo0o0o0oo0[3][1]:oo0o0o000o0oo0o0o0oo0[3][3], oo0o0o000o0oo0o0o0oo0[3][0]:oo0o0o000o0oo0o0o0oo0[3][2]]      
    o00o00000o0oo000o0o00 = img[oo0o0o000o0oo0o0o0oo0[4][1]:oo0o0o000o0oo0o0o0oo0[4][3], oo0o0o000o0oo0o0o0oo0[4][0]:oo0o0o000o0oo0o0o0oo0[4][2]]      
    o0o00oo0oo00o0000oo00 = img[oo0o0o000o0oo0o0o0oo0[5][1]:oo0o0o000o0oo0o0o0oo0[5][3], oo0o0o000o0oo0o0o0oo0[5][0]:oo0o0o000o0oo0o0o0oo0[5][2]]
def o000o00oo0o000o000o0o():
    global o0oo000o00000o0oooooo, o000o0o0000o00o00o0o0, oo0o00ooo0oo0oooo0o00, o000o0o0000o00o00o0o0e, oo0oo0o0o00o0000oooo0, o00o000000ooo00oo00o0, oo0000000oooooo0oo0o0
    template = o0oo000o00000o0oooooo[0]
    global o00oooooo00o0o0o0o000
    sc = o00oooooo00o0o0o0o000
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    logging.info("查找刷新")
    if max_val >= 0.8:
        logging.info("刷新")
        TopFrame.ooooooo0oooooo00o00oo()
        global oo0ooo00ooo0oo00o0000, o0o0o00oo0ooooo0ooo0o, oo00000o000oooooo000o
        oo0ooo00ooo0oo00o0000 = True         
        oo00000o000oooooo000o = 0      
def o0oo000o00ooo0oooooo0():
    global o0oo000o00000o0oooooo, oooo0o000o0oo0ooooooo, oo0oo0o0o00o0000oooo0
    template = o0oo000o00000o0oooooo[1]
    global o0oo0ooo00o00oo000o00
    sc = o0oo0ooo00o00oo000o00
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val >= 0.9:
        TopFrame.ooo00oo0oooooo00oooo0()
    if oooo0o000o0oo0ooooooo and max_val < 0.9:
        print("暂停确认")
def oooo00oo0o000o0ooooo0():
    global o0oo000o00000o0oooooo, oooo0o000o0oo0ooooooo, oo0oo0o0o00o0000oooo0, oo0ooo00ooo0oo00o0000, o0o0o00oo0ooooo0ooo0o
    template = o0oo000o00000o0oooooo[1]
    global o00o00000o0oo000o0o00
    sc = o00o00000o0oo000o0o00
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.9:
        oo0ooo00ooo0oo00o0000 = False
        o0o0o00oo0ooooo0ooo0o = True
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
def o0oo0o00oo0oo0oo000oo(area):                          
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
def o0oo0o00oo0oo0oo000oo_getimg(area, size, name):
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
    return price                          
def timeset():
    global o00000o0o00oooo0000oo, o0o00oo0oo00o0000oo00, oo000oo00o00oo0o00o0o
    try:
        currenttime = cv2.cvtColor(o0o00oo0oo00o0000oo00, cv2.COLOR_BGR2GRAY)
        currenttime = readpic(currenttime)           
        cv2.imwrite("zp.png", o0o00oo0oo00o0000oo00)
        print(currenttime)
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        b = a + ' ' + currenttime
        print(b)
        global oooo0oooo0000o0000o00,oo00o00oo0o0oo0o0o0oo
        if oooo0oooo0000o0000o00:
            print(time.strptime(b, '%Y-%m-%d %H:%M:%S'))
            o00000o0o00oooo0000oo = time.mktime(time.strptime(b,'%Y-%m-%d %H:%M:%S')) + 0.5                 
        if oo00o00oo0o0oo0o0o0oo:
            try:
                oo000oo00o00oo0o00o0o = int(currenttime.split(':')[2]) + 0.5
            except:
                pass
    except:
        pass
import winreg, re, subprocess
oo00o000oo000o0000000 = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'
def o0oo000oo0o0oooooooo0():
    global oo00o000oo000o0000000
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            oo00o000oo000o0000000 = result[0]
    except:
        pass
    if not os.path.exists(oo00o000oo000o0000000):
        if os.path.exists('C:\Program Files (x86)'):
            pass
def openweb(url):
    global oo00o000oo000o0000000
    subprocess.Popen([oo00o000oo000o0000000, url])
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
def oo0o00o00000o00oo000o():
    try:
        target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % o0oo0oo0o0o0o000o0o0o + '&' + 'passwd=%s' % oo0ooooo000o0oo00000o+'&'+'version=%s' %version
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
    global o0oo0oo0o0o0o000o0o0o
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
def o0000000oooo000o000oo():
    host = host_ali
    port = 8080
    global o0oo0oo0o0o0o000o0o0o
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
    data = ['keep', o0oo0oo0o0o0o000o0o0o, oo0ooooo000o0oo00000o]
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")           
    logging.info('发送信息 %s' % str(data, encoding="utf-8"))
    s.send(data)
    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")
def oo000o00ooo0o0ooo0o0o(subject, to_list, file_name):
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
def o0oo000000000oo00oo0o():
    pass
def o000o0o0o0o0o0oooo00o():
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
        self.Bind(wx.EVT_BUTTON, self.ooo00000ooooooo000o00, self.monibutton)
        self.o00o00o0oo0o0oo000ooobutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.o0ooooo0o0o00ooo0o0o0, self.o00o00o0oo0o0oo000ooobutton)
        self.hbox1.Add(self.monibutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.o00o00o0oo0o0oo000ooobutton, 0, wx.ALL | wx.CENTER, 5)
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
        self.Bind(wx.EVT_BUTTON, self.o0oooo0o00o00000o00o0, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.oo0oo0ooo00o000000oo0, self.posautoset)
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
        self.Bind(wx.EVT_TIMER, self.oo0000oooo000o0ooo0o0, self.timer2)                 
        self.timer2.Start(100)          
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.o0o0ooo0oo0o00oooo000, self.timer3)                   
        self.timer3.Start(50)
        self.Bind(wx.EVT_BUTTON, self.oooo00o0o00o00o0o000o, self.timeautoreset)            
        pub.subscribe(self.o0o0oo0oo000o0oo00o0o, "open dianxin")        
        pub.subscribe(self.o0o0ooooo0oo0o0000o00, "open nodianxin")         
        pub.subscribe(self.o000o00o0o0o0o0ooo00o, "open userweb")             
    def ooo00000ooooooo000o00(self, event):
        global o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, o0oo000o00oooo00000o0, twice
        timer0 = threading.Timer(5, oo000o0oooo00oo0ooo0o)
        o000000ooooo0oo00o0o0 = True
        twice = False
        o0oo0000oo00o0o00o000 = True
        o0oooooo0000ooo0o0o0o = False
        o0oo00oooo0ooooo00o0o = 1       
        o0oo000o00oooo00000o0 = False
        global Px, Py, url1, oo0o0ooo00oo000ooo0oo, web_on, do, oooo0oooo0000o0000o00, oo00o00oo0o0oo0o0o0oo, oo00o0o0o0oo0000ooooo
        if oooo0oooo0000o0000o00:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif oo00o00oo0o0oo0o0o0oo:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                oo00o00oo0o0oo0o0o0oo = True        
                oo0o0ooo00oo000ooo0oo = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟')
                if o0000ooo00o00000oo000:
                    self.operationframe.ooooo0o0o0oooooo0ooo0()
                if not oo00o0o0o0oo0000ooooo:                
                    self.monio0o000o0oooo00o00o0oothread = MoniTijiaoThread()            
                    self.o0o000o0oooo00o00o0oothread = TijiaoThread()            
                    oo00o0o0o0oo0000ooooo = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()
    def o0ooooo0o0o00ooo0o0o0(self, event):
        o00o00o0oo0o0oo000ooo = Guopaiframe("国拍")
    def o0o0oo0oo000o0oo00o0o(self):
        global o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, o0oo000o00oooo00000o0, twice
        timer0 = threading.Timer(5, oo000o0oooo00oo0ooo0o)
        o000000ooooo0oo00o0o0 = True
        twice = False
        o0oo0000oo00o0o00o000 = True
        o0oooooo0000ooo0o0o0o = False
        o0oo00oooo0ooooo00o0o = 1       
        o0oo000o00oooo00000o0 = False
        global Px, Py, url2, oo0o0ooo00oo000ooo0oo, web_on, do, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00, oo00o0o0o0oo0000ooooo
        if oo00o00oo0o0oo0o0o0oo:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooo0oooo0000o0000o00:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                oo0o0ooo00oo000ooo0oo = True
                oooo0oooo0000o0000o00 = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o0000ooo00o00000oo000:
                    self.operationframe.ooooo0o0o0oooooo0ooo0()
                if not oo00o0o0o0oo0000ooooo:                
                    self.monio0o000o0oooo00o00o0oothread = MoniTijiaoThread()            
                    self.o0o000o0oooo00o00o0oothread = TijiaoThread()            
                    oo00o0o0o0oo0000ooooo = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,  style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def o0o0ooooo0oo0o0000o00(self):
        global o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, o0oo000o00oooo00000o0, twice
        timer0 = threading.Timer(5, oo000o0oooo00oo0ooo0o)
        o000000ooooo0oo00o0o0 = True
        twice = False           
        o0oo0000oo00o0o00o000 = True
        o0oooooo0000ooo0o0o0o = False
        o0oo00oooo0ooooo00o0o = 1       
        o0oo000o00oooo00000o0 = False
        global Px, Py, url3, oo0o0ooo00oo000ooo0oo, web_on, do, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00, oo00o0o0o0oo0000ooooo
        if oo00o00oo0o0oo0o0o0oo:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif oooo0oooo0000o0000o00:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            self.Open()
            if do:
                oo0o0ooo00oo000ooo0oo = True
                oooo0oooo0000o0000o00 = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                if o0000ooo00o00000oo000:
                    self.operationframe.ooooo0o0o0oooooo0ooo0()
                if not oo00o0o0o0oo0000ooooo:                
                    self.monio0o000o0oooo00o00o0oothread = MoniTijiaoThread()            
                    self.o0o000o0oooo00o00o0oothread = TijiaoThread()            
                    oo00o0o0o0oo0000ooooo = True
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos ,style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                self.Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             
    def o000o00o0o0o0o0ooo00o(self):
        global o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, o0oo000o00oooo00000o0, twice
        timer0 = threading.Timer(5, oo000o0oooo00oo0ooo0o)                
        o000000ooooo0oo00o0o0 = True
        twice = False
        o0oo0000oo00o0o00o000 = True
        o0oooooo0000ooo0o0o0o = False
        o0oo00oooo0ooooo00o0o = 1       
        o0oo000o00oooo00000o0 = False
        global Px, Py, url3, oo0o0ooo00oo000ooo0oo, web_on, do, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00, oo00o0o0o0oo0000ooooo
        self.Open()
        if do:
            oo0o0ooo00oo000ooo0oo = True
            oooo0oooo0000o0000o00 = True
            if o0000ooo00o00000oo000:
                self.operationframe.ooooo0o0o0oooooo0ooo0()
            if not oo00o0o0o0oo0000ooooo:                
                self.monio0o000o0oooo00o00o0oothread = MoniTijiaoThread()            
                self.o0o000o0oooo00o00o0oothread = TijiaoThread()            
                oo00o0o0o0oo0000ooooo = True
                openIE(url3)
                self.Listen()
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            self.Close()             
    def ooooo00o00oooo0000000(self, event):
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
    def ooo000ooooo000o000ooo(self, event):
        pass
    def o0oooo000o0oo0ooo00oo(self, event):
        pass
    def oo000oooo0ooo00o0oo0o(self, event):
        pass
    def o0oooo0o00o00000o00o0(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)
    def oo0oo0ooo00o000000oo0(self, event):
        oo000o0oooo00oo0ooo0o()
    def o00000ooo0o0000000000(self, event):
        pass
    def o0o0ooo0oo0o00oooo000(self, event):   
        global ooo0oo0000000o0oo000o, ooo0oo00ooooo00o0o0oo, oo00000oooo0o0o0o00o0
        try:
            price = int(TopFrame.oo00000o0ooo0ooo000o0())           
            if price in pricelist:        
                ooo0oo00ooooo00o0o0oo = False
                if ooo0oo0000000o0oo000o == price:
                    pass
                else:
                    ooo0oo0000000o0oo000o = price
                    if oo00o00oo0o0oo0o0o0oo:
                        oo00000oooo0o0o0o00o0 = oo000oo00o00oo0o00o0o
                    else:
                        oo00000oooo0o0o0o00o0 = o00000o0o00oooo0000oo
            else:
                ooo0oo00ooooo00o0o0oo = True
        except:
            ooo0oo00ooooo00o0o0oo = True
    def oo0ooo0o00ooo0o0o00o0(self, event):
        global ooo0oo00ooooo00o0o0oo
        if ooo0oo00ooooo00o0o0oo:
            try:
                oo000o0oooo00oo0ooo0o()
            except:
                logging.error("oo0ooo0o00ooo0o0o00o0 error")
                print("oo0ooo0o00ooo0o0o00o0 error")
    def oooo00o0o00o00o0o000o(self, event):
        timeset()          
    @staticmethod
    def Confirm():
        global ooooooo00oo0ooooo00oo, oooo0o000o0oo0ooooooo
        confirm_hash = TopFrame.Confirm_hash()          
        if confirm_hash == ooooooo00oo0ooooo00oo[0]:
            oooo0o000o0oo0ooooooo = True
    @staticmethod
    def Refresh():
        ooo000oo0o0ooo0o0o0o0_hash = TopFrame.Refresh_hash()          
        global ooooooo00oo0ooooo00oo, o000o0o0000o00o00o0o0
        if ooo000oo0o0ooo0o0o0o0_hash == ooooooo00oo0ooooo00oo[1]:
            o000o0o0000o00o00o0o0 = True
    @staticmethod
    def oo00000o0ooo0ooo000o0():
        global ooo00000ooo0ooo000o0o , ooo0oo00ooooo00o0o0oo
        global num
        num+=1
        ooo0oo0000000o0oo000o = cv2.cvtColor(ooo00000ooo0ooo000o0o, cv2.COLOR_BGR2GRAY)
        price = readpic(ooo0oo0000000o0oo000o)
        return price
    @staticmethod
    def oooo00o000o0000oo0000():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[0][0] = po[0]
        oo0oo0o0o00o0000oooo0[0][1] = po[1]
    @staticmethod
    def ooo000o00o000o0oo0000():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[1][0] = po[0]
        oo0oo0o0o00o0000oooo0[1][1] = po[1]
    @staticmethod
    def oo00o000oooooo00ooooo():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[2][0] = po[0]
        oo0oo0o0o00o0000oooo0[2][1] = po[1]
    @staticmethod
    def oooo0o0o0o00o0o000o00():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[3][0] = po[0]
        oo0oo0o0o00o0000oooo0[3][1] = po[1]
    @staticmethod
    def o0o0o0ooo0000oooo00o0():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[4][0] = po[0]
        oo0oo0o0o00o0000oooo0[4][1] = po[1]
    @staticmethod
    def oo0oo0oo0oo00oo0oo000():
        po = pg.position()
        oo0oo0o0o00o0000oooo0[5][0] = po[0]
        oo0oo0o0o00o0000oooo0[5][1] = po[1]
    @staticmethod
    def o00o0000o0o0oo0oo0oo0():
        TopFrame.oooo00o000o0000oo0000()
    @staticmethod
    def o0o00000o0oo000000000():
        TopFrame.ooo000o00o000o0oo0000()
    @staticmethod
    def o0ooo0oo0oooo00oo0000():
        x,y=win32api.GetCursorPos()
        print("x=",x," y=",y)
    @staticmethod
    def ooo00o000o0o00000oooo():
        TopFrame.oooo0o0o0o00o0o000o00()
    @staticmethod
    def o0oo0o0o00o00ooooooo0():
        TopFrame.o0o0o0ooo0000oooo00o0()
    @staticmethod
    def ooooo00o0o0ooo0o00ooo():
        TopFrame.oo0oo0oo0oo00oo0oo000()
    @classmethod
    def ooo0oo0oo000000oo0oo0(cls):
        global web_on, o0oooooo0000ooo0o0o0o, oo0oo000ooooo0oo00ooo, o0000ooo0oooo0000oooo, o0oo00oooo0ooooo00o0o
        global o0oooooo0000ooo0o0o0o, o0oo0000oo00o0o00o000, oooo0o000o0oo0oooooooe, ooo0o0o00o000o0000000
        ooo0o0o00o000o0000000 = True
        if o0oo00oooo0ooooo00o0o == 1:
            timer = threading.Timer(oo0oo000ooooo0oo00ooo, cls.Tijiao)
            timer.start()
            o0oooooo0000ooo0o0o0o = False
            if twice:
                o0oo00oooo0ooooo00o0o = 2
        elif o0oo00oooo0ooooo00o0o == 2:
            o0oo00oooo0ooooo00o0o = 0
            timer = threading.Timer(o0000ooo0oooo0000oooo, cls.Tijiao)
            timer.start()
            o0oooooo0000ooo0o0o0o = False
        else:
            cls.Tijiao()
    @staticmethod
    def Tijiao():
        global o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, o0oo00oooo0ooooo00o0o ,o0oo0000oo00o0o00o000
        Click(oo0oo0o0o00o0000oooo0[2][0], oo0oo0o0o00o0000oooo0[2][1])
        o0oo000o00oooo00000o0 = False               
        o0oo0000oo00o0o00o000 = True        
        global oooo0o000o0oo0oooooooe
        if not oooo0o000o0oo0oooooooe:        
            pass
    @classmethod
    def oo00o0000oooooo0o0oo0(cls):
        global o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, o0oo00oooo0ooooo00o0o, ooo0o0o00o000o0000000
        ooo0o0o00o000o0000000 = True
        if oo00o00oo0o0oo0o0o0oo:
            interval = oo000oo00o00oo0o00o0o - oo00000oooo0o0o0o00o0
        else:
            interval = o00000o0o00oooo0000oo - oo00000oooo0o0o0o00o0
        if o0oo00oooo0ooooo00o0o == 2:            
            if ooo0oo0000000o0oo000o <= ooo00o00oooo0o000o0oo - 600:
                print("触发延迟")
                o0oo00oooo0ooooo00o0o = 0
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                o0oooooo0000ooo0o0o0o = False
            elif ooo0oo0000000o0oo000o == ooo00o00oooo0o000o0oo - 500 and interval < 0.95:
                o0oo00oooo0ooooo00o0o = 0
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                o0oooooo0000ooo0o0o0o = False
            else:
                o0oo00oooo0ooooo00o0o = 0
                cls.Tijiao()
                o0oooooo0000ooo0o0o0o = False
        elif o0oo00oooo0ooooo00o0o == 1:
            if ooo0oo0000000o0oo000o <= o00oo000oo00oooo0o000 - 600:
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                o0oooooo0000ooo0o0o0o = False
                if twice:
                    o0oo00oooo0ooooo00o0o = 2
            elif ooo0oo0000000o0oo000o == o00oo000oo00oooo0o000 - 500 and interval < 0.95:
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                o0oooooo0000ooo0o0o0o = False
                if twice:
                    o0oo00oooo0ooooo00o0o = 2
            else:
                cls.Tijiao()
                o0oooooo0000ooo0o0o0o = False
                if twice:
                    o0oo00oooo0ooooo00o0o = 2
    @staticmethod
    def ooooooo0oooooo00o00oo():
        Click(oo0oo0o0o00o0000oooo0[3][0], oo0oo0o0o00o0000oooo0[3][1])
        Click(oo0oo0o0o00o0000oooo0[5][0], oo0oo0o0o00o0000oooo0[5][1])
        global oo0ooo00ooo0oo00o0000, o0o0o00oo0ooooo0ooo0o, oo00000o000oooooo000o
        oo0ooo00ooo0oo00o0000 = True         
        oo00000o000oooooo000o = 0      
    @staticmethod
    def ooo00oo0oooooo00oooo0():
        Click(oo0oo0o0o00o0000oooo0[4][0], oo0oo0o0o00o0000oooo0[4][1])
    @staticmethod
    def ooo000o0o00o00ooo00o0():
        global web_on, ooo0oo0000000o0oo000o, oo00000o000oooooo000o
        global o0oo00oooo0ooooo00o0o, o00oo000oo00oooo0o000, ooo00o00oooo0o000o0oo, oo00oo0o00000000ooo0o, ooo000000o0o0o0ooo00o
        global o0oooooo0000ooo0o0o0o, o0oo0000oo00o0o00o000
        global oo0o00ooo0oo0oooo0o00, o000o0o0000o00o00o0o0e, oo0o0oo0oooo0oo00oo0o, oo0ooo00ooo0oo00o0000
        oo00000o000oooooo000o = 0            
        oo0ooo00ooo0oo00o0000 = True            
        print("到这了")
        o0oooooo0000ooo0o0o0o = True          
        oo0o00ooo0oo0oooo0o00 = True           
        if o0oo00oooo0ooooo00o0o == 1:
            o00oo000oo00oooo0o000 = ooo0oo0000000o0oo000o + oo00oo0o00000000ooo0o
            setText(str(o00oo000oo00oooo0o000))
            TopFrame.o0ooo0o0o0000o0o000o0()
            Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
            Click(oo0oo0o0o00o0000oooo0[5][0], oo0oo0o0o00o0000oooo0[5][1])
            o0oooooo0000ooo0o0o0o = True
            o0oo0000oo00o0o00o000 = False
            oo0o0oo0oooo0oo00oo0o = False        
        elif o0oo00oooo0ooooo00o0o == 2 and twice:
            ooo00o00oooo0o000o0oo = ooo0oo0000000o0oo000o + ooo000000o0o0o0ooo00o
            setText(str(ooo00o00oooo0o000o0oo))
            TopFrame.o0ooo0o0o0000o0o000o0()
            Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
            Click(oo0oo0o0o00o0000oooo0[5][0], oo0oo0o0o00o0000oooo0[5][1])
            o0oooooo0000ooo0o0o0o = True
            o0oo0000oo00o0o00o000 = False
            oo0o0oo0oooo0oo00oo0o = False        
    @staticmethod
    def oo00o0o0ooo00ooo00o0o():
        global oo0ooo00ooo0oo00o0000, oo00000o000oooooo000o
        oo0ooo00ooo0oo00o0000 = True
        oo00000o000oooooo000o = 0
        o00oo000oo00oooo0o000 = ooo0oo0000000o0oo000o + oo00oo0o00000000ooo0o
        setText(str(o00oo000oo00oooo0o000))
        TopFrame.o0ooo0o0o0000o0o000o0()
        Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
        Click(oo0oo0o0o00o0000oooo0[5][0], oo0oo0o0o00o0000oooo0[5][1])
    @staticmethod
    def o0ooo0o0o0000o0o000o0():
        Click2(oo0oo0o0o00o0000oooo0[6][0], oo0oo0o0o00o0000oooo0[6][1] - 5)
        Click2(oo0oo0o0o00o0000oooo0[6][0], oo0oo0o0o00o0000oooo0[6][1])
        Click2(oo0oo0o0o00o0000oooo0[6][0], oo0oo0o0o00o0000oooo0[6][1])
        Delete()
        Delete()
        if oo00o00oo0o0oo0o0o0oo:
            o00000000oooo0000ooo0()      
        else:
            Paste()       
    @staticmethod
    def o000o0oooo0000o0oo000():
        global o00o000o00oo00o00o0o0, o000000oo0ooo0ooo0000, oo00000o000oooooo000o, oo0ooo00ooo0oo00o0000
        Click(oo0oo0o0o00o0000oooo0[4][0], oo0oo0o0o00o0000oooo0[4][1])
        Click(oo0oo0o0o00o0000oooo0[0][0], oo0oo0o0o00o0000oooo0[0][1])
        Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
        Click(oo0oo0o0o00o0000oooo0[5][0], oo0oo0o0o00o0000oooo0[5][1])
        o00o000o00oo00o00o0o0 = True
        o000000oo0ooo0ooo0000 = 0
        oo00000o000oooooo000o = 0
        oo0ooo00ooo0oo00o0000 = True
    @staticmethod
    def oooo00o000o0o000o00o0():
        OperationFrame.o000oo00o00oo0oooooo0()
        Click(oo0oo0o0o00o0000oooo0[2][0], oo0oo0o0o00o0000oooo0[2][1])
    @staticmethod
    def o000oo0o0oo00o00000o0():
        pg.press('backspace')
    def oo0000oooo000o0ooo0o0(self, event):
        if not web_on and o0000ooo00o00000oo000:             
            self.operationframe.ooo0o0oooo0ooo0o00oo0()
    @staticmethod
    def o000000oo00oo0o0000o0():
        global o0oo000o00oooo00000o0, oo0o00ooo0oo0oooo0o00, o0oooooo0000ooo0o0o0o, o0o0o00oo0ooooo0ooo0o, oo0ooo00ooo0oo00o0000
        if e_on and o0oooooo0000ooo0o0o0o:
            print("o000000oo00oo0o0000o0")
            o0oo000o00oooo00000o0 = True
            oo0ooo00ooo0oo00o0000 = False
            o0o0o00oo0ooooo0ooo0o = True
    @staticmethod
    def o000000oo00oo0o0000o02():
        global o0oo000o00oooo00000o0, oo0o00ooo0oo0oooo0o00, o0o0o00oo0ooooo0ooo0o, oo0ooo00ooo0oo00o0000
        if o000ooo0000ooo0o0o0oo and o0oooooo0000ooo0o0o0o:
            o0oo000o00oooo00000o0 = True
        if o000ooo0000ooo0o0o0oo:
            o0o0o00oo0ooooo0ooo0o = True
            oo0ooo00ooo0oo00o0000 = False
    @classmethod
    def query(cls):
        global oo00ooooo000000o0o000, o0000o000o00oo0oo000o
        if not oo00ooooo000000o0o000 and not o0000o000o00oo0oo000o:
            o0000o000o00oo0oo000o = True
            oo00ooooo000000o0o000 = True
            setText(str(1000000))            
            TopFrame.o0ooo0o0o0000o0o000o0()
            Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
            timer1 = threading.Timer(3, cls.oo0o0oooo0o00oo0o0000)
            timer1.start()
            timer2 = threading.Timer(5, cls.o00000o0o0000oo00o00o)
            timer2.start()
        elif oo00ooooo000000o0o000 and o0000o000o00oo0oo000o:
            Click(oo0oo0o0o00o0000oooo0[7][0], oo0oo0o0o00o0000oooo0[7][1])
            o0000o000o00oo0oo000o = False
    @staticmethod
    def oo0o0oooo0o00oo0o0000():
        global oo00ooooo000000o0o000, o0000o000o00oo0oo000o
        if o0000o000o00oo0oo000o:
            Click(oo0oo0o0o00o0000oooo0[7][0], oo0oo0o0o00o0000oooo0[7][1])
            o0000o000o00oo0oo000o = False
    @staticmethod
    def o00000o0o0000oo00o00o():
        global oo00ooooo000000o0o000
        oo00ooooo000000o0o000 = False
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
                1: TopFrame.o00o0000o0o0oo0oo0oo0, 2: TopFrame.o0o00000o0oo000000000, 3: TopFrame.o0ooo0oo0oooo00oo0000,
                4: TopFrame.ooo00o000o0o00000oooo, 5: TopFrame.o0oo0o0o00o00ooooooo0,
                6: TopFrame.ooooo00o0o0ooo0o00ooo, 7: TopFrame.ooooooo0oooooo00o00oo, 8: TopFrame.oooo00o000o0o000o00o0,
                9: (lambda: TopFrame.o000o0oooo0000o0oo000()), 10: TopFrame.o000oo0o0oo00o00000o0, 11: TopFrame.o000000oo00oo0o0000o0,
                12: TopFrame.o000000oo00oo0o0000o02,
                13: TopFrame.query, 14: TopFrame.oo00o0o0ooo00ooo00o0o}                  
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
    def ooo00o0o000o00000o000ground(self, evt):
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
    def o0ooo00000o00ooo0o00o(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()
    @classmethod
    def ooo00o00o00oo0o0o00oo(cls):
        cls.Close()
    def o0o0ooo000o0o00o0oooo(self, event):
        wx.CallAfter(pub.sendMessage, "ooo000oo0o0ooo0o0o0o0")
        self.MovePos(event)
        global view
        if not view:
            view = True
            for i in range(len(oo0oo0o0o00o0000oooo0)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(oo0oo0o0o00o0000oooo0)):
                self.posframe[i].Hide()
    def o0o00000o0o0oo0o000oo(self, event):
        self.MovePos(event)
        self.oo000ooo0000o00o0ooo0()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)
    def MovePos(self, event):
        global oo0o000o000000o0oooo0
        for i in range(5):
            posx, posy = oo0oo0o0o00o0000oooo0[i]
            self.posframe[i].Move(posx - 10, posy - 5)
    def oo000ooo0000o00o0ooo0(self):
        output = open('pos.log', 'wb')
        pickle.dump(oo0oo0o0o00o0000oooo0, output)
        output.close()
    def o00oo0o000o0ooooooooo(self, event):
        o0000000oooo000o000oo()
    def oo0oo0o00o0ooo0o0oo0o(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global oo0o00oooo000o0oo0o0o, ooo0000000000o0oo0o00
        oo0o00oooo000o0oo0o0o = self.time_choice1.GetString(self.time_choice1.GetSelection())
        ooo0000000000o0oo0o00 = self.time_choice2.GetString(self.time_choice2.GetSelection())
    def o000o000o00oo00o0o0o0(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global oo0o00oooo000o0oo0o0o, ooo0000000000o0oo0o00
        oo0o00oooo000o0oo0o0o = self.time_choice1.GetString(self.time_choice1.GetSelection())
        ooo0000000000o0oo0o00 = self.time_choice2.GetString(self.time_choice2.GetSelection())
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global o00000o0o00oooo0000oo
        time_local = time.localtime(o00000o0o00oooo0000oo)
        print(time_local)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global o00000o0o00oooo0000oo, b_time
        if b_time < 9:
            b_time = b_time + 1
        else:
            b_time = 0
        time_local = time.localtime(o00000o0o00oooo0000oo)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=o0o0o00ooo0o00oo00o0o,
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
        global oo000oo00o00oo0o00o0o
        st = "%s:%s:%s" % (11, 29, oo000oo00o00oo0o00o0o)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global oo000oo00o00oo0o00o0o
        moni_s = int(oo000oo00o00oo0o00o0o)       
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=o0o0o00ooo0o00oo00o0o,
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
        wx.Frame.__init__(self, None, 18, 'Price', size=oooooo0ooo0o0o0o0000o, pos=oo0oooo0oo0ooooo00oo0frame,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
                          )
        self.panel = wx.Panel(self, size=oooooo0ooo0o0o0o0000o)
        self.bmp = wx.StaticBitmap(self.panel, -1)
    def o0oo0ooooo0o0ooo0oooo(self, bm):
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
        pub.subscribe(self.o00o0ooo00oo000ooo0oo, "close web")        
    def OnClose(self, event):
        global web_on, o00ooo0o0o0oooo00000o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00, oo00o0o0o0oo0000ooooo
        web_on = False
        o00ooo0o0o0oooo00000o = False
        oo00o00oo0o0oo0o0o0oo = False
        oooo0oooo0000o0000o00 = False
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
    def o00o0ooo00oo000ooo0oo(self):
        global web_on, o00ooo0o0o0oooo00000o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00, oo00o0o0o0oo0000ooooo
        web_on = False
        o00ooo0o0o0oooo00000o = False
        oo00o00oo0o0oo0o0o0oo = False
        oooo0oooo0000o0000o00 = False
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
    def oo00oo0o00ooo0o0000o0(self, event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()
    def Timego(self, event):
        global ooo0oo0000000o0oo000o, oo000oo00o00oo0o00o0o, o00000o0o00oooo0000oo
        self.price.SetLabel("%s" % ooo0oo0000000o0oo000o)
        if oo00o00oo0o0oo0o0o0oo:
            self.time.SetLabel("11:29:%s" % int(oo000oo00o00oo0o00o0o))
        else:
            timestr1 = time.localtime(o00000o0o00oooo0000oo)
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
        global oo000o0o00o00o0o0ooo0, o00o0o0oo0oooo0ooo0o0, o00ooo00oo000000o0000, o0o0ooo00o0o0000oo0o0
        oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)
        o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)
        o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)
        o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.oooo00000o000o00o0oo0, self.timer1)                 
        self.timer1.Start(10)          
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.oooooo0o000o000oooo0o, self.timer2)   
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
        self.Bind(wx.EVT_BUTTON, self.oo0o0000o00o00o00oooo, self.button1)
        self.button2 = wx.Button(panel, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.ooo0oo00o0o0000oooo00, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.oo0000000o0oo0ooo0o00, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.o00ooo0oo000o0o000o0o, self.button4)
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
        self.o0o00ooo00ooo0o00o0oo_save = wx.Button(panel, label="保存策略", size=(60, 35))
        self.o0o00ooo00ooo0o00o0oo_load = wx.Button(panel, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(panel, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.o0o00ooo00ooo0o00o0oo_save)
        hbox4.Add(self.o0o00ooo00ooo0o00o0oo_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)
        oneshot = wx.StaticBox(panel, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajio00000o0o00oooo0000oo = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))                              
        self.jiajio00000o0o00oooo0000oo.SetRange(40, 55)
        self.jiajio00000o0o00oooo0000oo.SetValue(48)
        self.jiajio00000o0o00oooo0000oo.SetIncrement(0.1)
        gridsizer1.Add(self.jiajio00000o0o00oooo0000oo, pos=(0, 0))
        miao_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))
        o0o000o0oooo00o00o0oo_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_o0o000o0oooo00o00o0oo = wx.Choice(panel, -1, choices=o0o000o0oooo00o00o0oo_choices, size=(68, 25))
        self.select_o0o000o0oooo00o00o0oo.SetSelection(0)
        gridsizer1.Add(self.select_o0o000o0oooo00o00o0oo, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)
        o0o000o0oooo00o00o0oo_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(o0o000o0oooo00o00o0oo_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.o0o000o0oooo00o00o0oo_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.o0o000o0oooo00o00o0oo_time.SetRange(40.0, 57.0)
        self.o0o000o0oooo00o00o0oo_time.SetValue(55.0)
        self.o0o000o0oooo00o00o0oo_time.SetIncrement(0.1)
        gridsizer1.Add(self.o0o000o0oooo00o00o0oo_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)
        secondshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajio00000o0o00oooo0000oo2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajio00000o0o00oooo0000oo2.SetRange(40, 55)
        self.jiajio00000o0o00oooo0000oo2.SetValue(48)
        self.jiajio00000o0o00oooo0000oo2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajio00000o0o00oooo0000oo2, pos=(0, 0))
        miao_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(panel, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3))
        o0o000o0oooo00o00o0oo_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_o0o000o0oooo00o00o0oo2 = wx.Choice(panel, -1, choices=o0o000o0oooo00o00o0oo_choices2, size=(68, 25))
        self.select_o0o000o0oooo00o00o0oo2.SetSelection(0)
        gridsizer2.Add(self.select_o0o000o0oooo00o00o0oo2, pos=(1, 0))
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)
        o0o000o0oooo00o00o0oo_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(o0o000o0oooo00o00o0oo_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.o0o000o0oooo00o00o0oo_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.o0o000o0oooo00o00o0oo_time2.SetRange(53.0, 57.0)
        self.o0o000o0oooo00o00o0oo_time2.SetValue(55.0)
        self.o0o000o0oooo00o00o0oo_time2.SetIncrement(0.1)
        gridsizer2.Add(self.o0o000o0oooo00o00o0oo_time2, pos=(2, 1))
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
        self.Bind(wx.EVT_CHECKBOX, self.oooo0000o0000oo00o0oo, self.timeview)
        self.Bind(wx.EVT_CHOICE, self.o0oo000o0oo00o000000o, self.confirm_choice)
        self.Bind(wx.EVT_BUTTON, self.oo000oo00o0000o0oooo0, self.o0o00ooo00ooo0o00o0oo_save)
        self.Bind(wx.EVT_BUTTON, self.oo00oo0oo000ooo00o0oo, self.o0o00ooo00ooo0o00o0oo_load)
        self.Bind(wx.EVT_BUTTON, self.o000ooo00oo00000o0o00, self.save_info)
        self.Bind(wx.EVT_CHOICE, self.o000ooo0oo00oooo0oo0o, self.select_stractagy)
        self.Bind(wx.EVT_TEXT, self.ooooo0oo0o0o0o0o0oooo, self.jiajio00000o0o00oooo0000oo)
        self.Bind(wx.EVT_TEXT, self.o00oooo0o000ooooo0000, self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.o0ooo0o0o0ooooo00o0oo, self.select_o0o000o0oooo00o00o0oo)
        self.Bind(wx.EVT_TEXT, self.o0o0000o000000o0o0000, self.yanchi_time)
        self.Bind(wx.EVT_TEXT, self.o00oo00o0o0o0oo00o00o, self.o0o000o0oooo00o00o0oo_time)
        self.Bind(wx.EVT_TEXT, self.ooooo0oo0o0o0o0o0oooo2, self.jiajio00000o0o00oooo0000oo2)
        self.Bind(wx.EVT_TEXT, self.o00oooo0o000ooooo00002, self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.o0oooo000o000oooo0oo0, self.select_o0o000o0oooo00o00o0oo2)
        self.Bind(wx.EVT_TEXT, self.o0o000o000o0o000oo0oo, self.yanchi_time2)
        self.Bind(wx.EVT_TEXT, self.o0oo000o0oo00o0oo0o0o, self.o0o000o0oooo00o00o0oo_time2)
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)
        self.ooo0oo00ooooooooo0o00frame = YanzhengmaFrame()
    def OnClose(self, event):
        self.Show(False)
    def oooo00000o000o00o0oo0(self, event):
        global o00o000o00oo00o00o0o0, web_on, oo0o0oo0oo000o0o0oooo, o00ooo0o0o0oooo00000o, oo0ooo00ooo0oo00o0000, o0oo0oo0o00oo0oo00000, oooooo0ooo0o0o0o0000o, o0o0o00oo0ooooo0ooo0o
        global oo00000o000oooooo000o, o000000oo0ooo0ooo0000, ooooo0ooo0oo00oo00000
        global ooo0oooooooo0000oo0o0 ,oo0o0oo000o0oo0o000o0
        if ooooo0ooo0oo00oo00000:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(oo0oooo0oo0ooooo00oo0frame)          
                    ooooo0ooo0oo00oo00000 = False        
                except:
                    pass
        if o00o000o00oo00o00o0o0 and o000000oo0ooo0ooo0000 >= 4:
            try:
                self.oo000oo0o0oo0o00o00oo()
            except:
                pass
            self.oooo0o00o000ooo000ooo(Pos_price, o0oo0oo0o00oo0oo00000, "userprice.png")
            image = "userprice.png"
            self.priceframe = PriceFrame(image, o0oo0oo0o00oo0oo00000, Pos_priceframe)
            self.priceframe.Show(True)
            o00o000o00oo00o00o0o0 = False
            oo0o0oo0oo000o0o0oooo = True
        if oo00000o000oooooo000o >= 5 and not o0o0o00oo0ooooo0ooo0o:                    
            oooo00oo0o000o0ooooo0()
        if o0o0o00oo0ooooo0ooo0o:
            try:
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        if oo0ooo00ooo0oo00o0000:
            o0o0o00oo0ooooo0ooo0o = False
            cut_pic(ooo0oooooooo0000oo0o0, oooooo0ooo0o0o0o0000o, "ooo0oo00ooooooooo0o00.png")              
            image = "ooo0oo00ooooooooo0o00.png"
            global o0oooo0ooo0o0oo000o00
            o0oooo0ooo0o0oo000o00 = Image.open("ooo0oo00ooooooooo0o00.png")
            yan_hash = imagehash.dhash(o0oooo0ooo0o0oo000o00)
            if not oo0o0oo000o0oo0o000o0:      
                oo0o0oo000o0oo0o000o0 = yan_hash
            elif yan_hash == oo0o0oo000o0oo0o000o0:         
                pass
            else:
                oo0o0oo000o0oo0o000o0 = yan_hash
                try:
                    yan = self.FindWindowById(18)
                    yan.o0oo0ooooo0o0ooo0oooo(image)
                    yan.Show()
                except:                 
                    pass
                finally:
                    pass
    def oooo00o0oo0o0ooo0000o(self, event):
        global oo0ooo00ooo0oo00o0000, o0o0o00oo0ooooo0ooo0o
        oooo00oo0o000o0ooooo0()
    def oooooo0o000o000oooo0o(self, event):
        global o000000oo0ooo0ooo0000, oo00000o000oooooo000o
        o000000oo0ooo0ooo0000 += 1
        oo00000o000oooooo000o += 1
        file = 'sc_new.png'
        if web_on and o000000ooooo0oo00o0o0:
            self.lowestframe.Show(True)
        if not os.path.exists(file):
            try:
                self.oo000oo0o0oo0o00o00oo()
            except:
                pass
        if not o000000ooooo0oo00o0o0 or not web_on:
            self.lowestframe.Show(False)
    def oooo0o00o000ooo000ooo(self, box, size, name):
        global o0oo0oo0o00oo0oo00000
        region = ImageGrab.grab(box)
        region.resize(size, Image.ANTIALIAS).save(name)
    def oooo0o00o000ooo000ooo_ooo0oo00ooooooooo0o00(self, box, size, name):
        global o0oo0oo0o00oo0oo00000
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)
    @staticmethod
    def o000oo00o00oo0oooooo0():
        try:
            os.remove("sc_new.png")
        except:
            pass
    def oo000oo0o0oo0o00o00oo(self):
        try:
            self.priceframe.Destroy()
        except:
            pass
    def opt(self, event):
        global o0oo00oooo0ooooo00o0o, oo0o000000o0o0o0000oo, o0oo0000oo00o0o00o000
        global o000000ooooo0oo00o0o0        
        global twice, o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, oo0o000000o0o0o0000oo            
        if oo000oo00o00oo0o00o0o < o0oo0o000o0ooo0000oo0 and oo00o00oo0o0oo0o0o0oo and not twice:        
            twice = False
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
        elif oo000oo00o00oo0o00o0o < o0oo0o000o0ooo0000oo0 and oo00o00oo0o0oo0o0o0oo and twice:        
            twice = True
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
    def oo0000000o0oo0ooo0o00(self, event):
        global o00000o0o00oooo0000oo, oo000oo00o00oo0o00o0o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00
        if oo00o00oo0o0oo0o0o0oo:
            oo000oo00o00oo0o00o0o += 0.1
        else:
            o00000o0o00oooo0000oo += 0.1
    def o00ooo0oo000o0o000o0o(self, event):
        global o00000o0o00oooo0000oo, oo000oo00o00oo0o00o0o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00
        if oo00o00oo0o0oo0o0o0oo:
            oo000oo00o00oo0o00o0o -= 0.1
        else:
            o00000o0o00oooo0000oo -= 0.1
    def oo0o0000o00o00o00oooo(self, event):
        global o00000o0o00oooo0000oo, oo000oo00o00oo0o00o0o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00
        if oo00o00oo0o0oo0o0o0oo:
            oo000oo00o00oo0o00o0o += 1
            if oo000oo00o00oo0o00o0o >= 60:
                oo000oo00o00oo0o00o0o = 0
        else:
            o00000o0o00oooo0000oo += 1
    def ooo0oo00o0o0000oooo00(self, event):
        global o00000o0o00oooo0000oo, oo000oo00o00oo0o00o0o, oo00o00oo0o0oo0o0o0oo, oooo0oooo0000o0000o00
        if oo00o00oo0o0oo0o0o0oo:
            oo000oo00o00oo0o00o0o -= 1
            if oo000oo00o00oo0o00o0o <= 0:
                oo000oo00o00oo0o00o0o = 60
        else:
            o00000o0o00oooo0000oo -= 1
    def oooo0000o0000oo00o0oo(self, event):
        timeSelected = event.GetEventObject()
        global o00ooo0o0o0oooo00000o, o0000ooo00o00000oo000
        if timeSelected.IsChecked():
            o00ooo0o0o0oooo00000o = True
            o0000ooo00o00000oo000 = True
            if oooo0oooo0000o0000o00:
                self.timeframe1.Show(True)
            elif oo00o00oo0o0oo0o0o0oo:
                self.timeframe2.Show(True)
        else:
            o00ooo0o0o0oooo00000o = False
            o0000ooo00o00000oo000 = False
            if oooo0oooo0000o0000o00:
                self.timeframe1.Show(False)
            elif oo00o00oo0o0oo0o0o0oo:
                self.timeframe2.Show(False)
    def ooooo0o0o0oooooo0ooo0(self):
        if oo00o00oo0o0oo0o0o0oo:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif oooo0oooo0000o0000o00:
            try:
                self.timeframe1.Show(True)
            except:
                pass
    def ooo0o0oooo0ooo0o00oo0(self):
        try:
            self.timeframe1.Show(False)
        except:
            pass
        try:
            self.timeframe2.Show(False)
        except:
            pass
    def o0oo000o0oo00o000000o(self, event):
        global e_on, o000ooo0000ooo0o0o0oo
        con = self.confirm_choice.GetSelection()
        if con == 0:
            e_on = True
            o000ooo0000ooo0o0o0oo = False
        elif con == 1:
            e_on = False
            o000ooo0000ooo0o0o0oo = True
    def ooooo0oo0o0o0o0o0oooo(self, event):
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, oo000o0o00o00o0o0ooo0, o00ooo00oo000000o0000
        tem = self.jiajio00000o0o00oooo0000oo.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            o0oo0o000o0ooo0000oo0 = tem
            o0oo0o000o0ooo0000oo0 = float(o0oo0o000o0ooo0000oo0)
            oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)            
        else:
            self.jiajio00000o0o00oooo0000oo.SetValue(o0oo0o000o0ooo0000oo0)
    def o00oooo0o000ooooo0000(self, event):
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            oo00oo0o00000000ooo0o = int(tem)
        else:
            self.jiajia_price.SetValue(oo00oo0o00000000ooo0o)
    def o0ooo0o0o0ooooo00o0oo(self, event):
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0
        select = self.select_o0o000o0oooo00o00o0oo.GetString(self.select_o0o000o0oooo00o00o0oo.GetSelection())
        if select == u"提前100":
            o0ooooooo0oo00ooooo0o = 100
        elif select == u"提前200":
            o0ooooooo0oo00ooooo0o = 200
        else:
            o0ooooooo0oo00ooooo0o = 0
    def o0o0000o000000o0o0000(self, event):
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            oo0oo000ooooo0oo00ooo = float(tem)
        else:
            self.yanchi_time.SetValue(oo0oo000ooooo0oo00ooo)
    def o00oo00o0o0o0oo00o00o(self, event):
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, o00ooo00oo000000o0000
        tem = self.o0o000o0oooo00o00o0oo_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            o0oo000o0oooo0oooooo0 = float(tem)
            o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)            
        else:
            self.o0o000o0oooo00o00o0oo_time.SetValue(o0oo000o0oooo0oooooo0)
    def ooooo0oo0o0o0o0o0oooo2(self, event):
        global ooo0000o0oo0o0000oo00, o0000ooo0oooo0000oooo, ooo000000o0o0o0ooo00o, ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o, o00o0o0oo0oooo0ooo0o0
        tem = self.jiajio00000o0o00oooo0000oo2.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            ooooo0ooo0o00ooo0o00o = float(tem)
            o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)            
        else:
            self.jiajio00000o0o00oooo0000oo2.SetValue(ooooo0ooo0o00ooo0o00o)
    def o00oooo0o000ooooo00002(self, event):
        global ooo0000o0oo0o0000oo00, o0000ooo0oooo0000oooo, ooo000000o0o0o0ooo00o, ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o
        global o0ooooooo0oo00ooooo0o, oo0oo000ooooo0oo00ooo, oo00oo0o00000000ooo0o, o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            ooo000000o0o0o0ooo00o = int(tem)
        else:
            self.jiajia_price2.SetValue(ooo000000o0o0o0ooo00o)
    def o0oooo000o000oooo0oo0(self, event):
        global ooo0000o0oo0o0000oo00, o0000ooo0oooo0000oooo, ooo000000o0o0o0ooo00o, ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o
        select = self.select_o0o000o0oooo00o00o0oo2.GetString(self.select_o0o000o0oooo00o00o0oo2.GetSelection())
        if select == u"提前100":
            ooo0000o0oo0o0000oo00 = 100
        elif select == u"提前200":
            ooo0000o0oo0o0000oo00 = 200
        else:
            ooo0000o0oo0o0000oo00 = 0
    def o0o000o000o0o000oo0oo(self, event):
        global ooo0000o0oo0o0000oo00, o0000ooo0oooo0000oooo, ooo000000o0o0o0ooo00o, ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o
        templist = ['0.%d' % i for i in range(11)]            
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            o0000ooo0oooo0000oooo = float(tem)
        else:
            self.yanchi_time2.SetValue(o0000ooo0oooo0000oooo)
    def o0oo000o0oo00o0oo0o0o(self, event):
        global ooo0000o0oo0o0000oo00, o0000ooo0oooo0000oooo, ooo000000o0o0o0ooo00o, ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o, o0o0ooo00o0o0000oo0o0
        tem = self.o0o000o0oooo00o00o0oo_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            ooo0oo0o0o00o0o0ooo0o = float(tem)
            o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)            
        else:
            self.o0o000o0oooo00o00o0oo_time2.SetValue(ooo0oo0o0o00o0o0ooo0o)
    def o000ooo0oo00oooo0oo0o(self, event):
        global o000000ooooo0oo00o0o0        
        global twice, o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, oo0o000000o0o0o0000oo            
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice = False
            o000000ooooo0oo00o0o0 = True
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
        elif stractagy_selection == u"双枪策略":
            self.oo000oo0000oo000oo00o()
            o000000ooooo0oo00o0o0 = True
            twice = True
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
        else:
            self.o0ooo00oo0o0o0oo0000o()
            o000000ooooo0oo00o0o0 = False
            twice = False
    def oo000oo0000oo000oo00o(self):      
        if not self.secondsizer_Shown:             
            self.vbox1.Show(self.secondshotSizer)          
            self.secondsizer_Shown = True                
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)           
            self.oneshotsizer_Shown = True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))          
        self.oo00o0000oo000ooo0o00()
        self.Layout()
    def ss_Hide(self):      
        if self.secondsizer_Shown:             
            self.vbox1.Hide(self.secondshotSizer)             
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))          
        self.o0oo00ooo0ooo0oo0oo00()
        self.Layout()
    def o0ooo00oo0o0o0oo0000o(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)
        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()
    def o0oo00ooo0ooo0oo0oo00(self):
        global o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, oo00oo0o00000000ooo0o, oo0oo000ooooo0oo00ooo, o0ooooooo0oo00ooooo0o
        self.jiajio00000o0o00oooo0000oo.SetValue(48.0)
        self.o0o000o0oooo00o00o0oo_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_o0o000o0oooo00o00o0oo.SetSelection(0)
        self.yanchi_time.SetValue(0.5)
        o0oo0o000o0ooo0000oo0 = 48           
        o0oo000o0oooo0oooooo0 = 55           
        oo00oo0o00000000ooo0o = 700           
        oo0oo000ooooo0oo00ooo = 0.5         
        o0ooooooo0oo00ooooo0o = 100            
        global oo000o0o00o00o0o0ooo0, o00o0o0oo0oooo0ooo0o0, o00ooo00oo000000o0000, o0o0ooo00o0o0000oo0o0
        oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)
        o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)
        o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)
        o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)
    def oo00o0000oo000ooo0o00(self):
        global o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, oo00oo0o00000000ooo0o, oo0oo000ooooo0oo00ooo, o0ooooooo0oo00ooooo0o
        global ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o, ooo000000o0o0o0ooo00o, o0000ooo0oooo0000oooo, ooo0000o0oo0o0000oo00
        self.jiajio00000o0o00oooo0000oo.SetValue(40.0)
        self.o0o000o0oooo00o00o0oo_time.SetValue(48.0)
        self.jiajia_price.SetValue(500)
        self.select_o0o000o0oooo00o00o0oo.SetSelection(2)
        self.yanchi_time.SetValue(0.0)
        self.jiajio00000o0o00oooo0000oo2.SetValue(50.0)
        self.o0o000o0oooo00o00o0oo_time2.SetValue(55.5)
        self.jiajia_price2.SetValue(700)
        self.select_o0o000o0oooo00o00o0oo2.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)
        o0oo0o000o0ooo0000oo0 = 40           
        o0oo000o0oooo0oooooo0 = 48           
        oo00oo0o00000000ooo0o = 500           
        oo0oo000ooooo0oo00ooo = 0.5         
        o0ooooooo0oo00ooooo0o = 0            
        ooooo0ooo0o00ooo0o00o = 50            
        ooo0oo0o0o00o0o0ooo0o = 55.5           
        ooo000000o0o0o0ooo00o = 700           
        o0000ooo0oooo0000oooo = 0.5           
        ooo0000o0oo0o0000oo00 = 100              
        global oo000o0o00o00o0o0ooo0, o00o0o0oo0oooo0ooo0o0, o00ooo00oo000000o0000, o0o0ooo00o0o0000oo0o0
        oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)
        o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)
        o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)
        o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)
    def oo000oo00o0000o0oooo0(self, event):
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
        global o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, oo00oo0o00000000ooo0o, oo0oo000ooooo0oo00ooo, o0ooooooo0oo00ooooo0o
        global ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o, ooo000000o0o0o0ooo00o, o0000ooo0oooo0000oooo, ooo0000o0oo0o0000oo00
        global osl, e_on, o000ooo0000ooo0o0o0oo          
        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0] = 0
            osl[1] = o0oo0o000o0ooo0000oo0
            osl[2] = o0oo000o0oooo0oooooo0
            osl[3] = oo00oo0o00000000ooo0o
            osl[4] = oo0oo000ooooo0oo00ooo
            osl[5] = o0ooooooo0oo00ooooo0o
            osl[6] = ooooo0ooo0o00ooo0o00o
            osl[7] = ooo0oo0o0o00o0o0ooo0o
            osl[8] = ooo000000o0o0o0ooo00o
            osl[9] = o0000ooo0oooo0000oooo
            osl[10] = ooo0000o0oo0o0000oo00
            osl[11] = e_on
            osl[12] = o000ooo0000ooo0o0o0oo
        elif self.select_stractagy.GetSelection() == 1:
            osl[0] = 1
            osl[0] = 1
            osl[1] = o0oo0o000o0ooo0000oo0
            osl[2] = o0oo000o0oooo0oooooo0
            osl[3] = oo00oo0o00000000ooo0o
            osl[4] = oo0oo000ooooo0oo00ooo
            osl[5] = o0ooooooo0oo00ooooo0o
            osl[6] = ooooo0ooo0o00ooo0o00o
            osl[7] = ooo0oo0o0o00o0o0ooo0o
            osl[8] = ooo000000o0o0o0ooo00o
            osl[9] = o0000ooo0oooo0000oooo
            osl[10] = ooo0000o0oo0o0000oo00
            osl[11] = e_on
            osl[12] = o000ooo0000ooo0o0o0oo
        with open('%s.o0o00ooo00ooo0o00o0oo' % name, 'wb') as spk:
            pickle.dump(osl, spk)
    def oo00oo0oo000ooo00o0oo(self, event):
        import os
        path = os.getcwd()
        choice = self.o000ooo0oooo000000oo0(path)
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
        global osl, e_on, o000ooo0000ooo0o0o0oo
        global o0oo0o000o0ooo0000oo0, o0oo000o0oooo0oooooo0, oo00oo0o00000000ooo0o, oo0oo000ooooo0oo00ooo, o0ooooooo0oo00ooooo0o
        global ooooo0ooo0o00ooo0o00o, ooo0oo0o0o00o0o0ooo0o, ooo000000o0o0o0ooo00o, o0000ooo0oooo0000oooo, ooo0000o0oo0o0000oo00
        global o000000ooooo0oo00o0o0        
        global twice, o0oo00oooo0ooooo00o0o, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, oo0o000000o0o0o0000oo            
        global oo000o0o00o00o0o0ooo0, o00ooo00oo000000o0000, o00o0o0oo0oooo0ooo0o0, o0o0ooo00o0o0000oo0o0
        try:
            with open(path, 'rb') as loadstr:
                osl = pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:      
            self.ss_Hide()
            twice = False
            o000000ooooo0oo00o0o0 = True
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
            self.select_stractagy.SetSelection(0)
            self.jiajio00000o0o00oooo0000oo.SetValue(osl[1])
            self.o0o000o0oooo00o00o0oo_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(0)
            elif osl[5] == 200:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(1)
            else:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(2)
            o0oo0o000o0ooo0000oo0 = osl[1]           
            o0oo000o0oooo0oooooo0 = osl[2]           
            oo00oo0o00000000ooo0o = osl[3]           
            oo0oo000ooooo0oo00ooo = osl[4]         
            o0ooooooo0oo00ooooo0o = osl[5]            
            e_on = osl[11]
            o000ooo0000ooo0o0o0oo = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif o000ooo0000ooo0o0o0oo:
                self.confirm_choice.SetSelection(1)
            oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)
            o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)
            o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)
            o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)
        elif osl[0] == 1:      
            o000000ooooo0oo00o0o0 = True
            twice = True
            o0oo0000oo00o0o00o000 = True
            o0oooooo0000ooo0o0o0o = False
            o0oo00oooo0ooooo00o0o = 1       
            o0oo000o00oooo00000o0 = False
            oo0o000000o0o0o0000oo = False        
            self.oo000oo0000oo000oo00o()
            self.select_stractagy.SetSelection(1)
            self.jiajio00000o0o00oooo0000oo.SetValue(osl[1])
            self.o0o000o0oooo00o00o0oo_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(0)
            elif osl[5] == 200:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(1)
            else:
                self.select_o0o000o0oooo00o00o0oo.SetSelection(2)
            self.jiajio00000o0o00oooo0000oo2.SetValue(osl[6])
            self.o0o000o0oooo00o00o0oo_time2.SetValue(osl[7])
            self.jiajia_price2.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_o0o000o0oooo00o00o0oo2.SetSelection(0)
            elif osl[10] == 200:
                self.select_o0o000o0oooo00o00o0oo2.SetSelection(1)
            else:
                self.select_o0o000o0oooo00o00o0oo2.SetSelection(2)
            o0oo0o000o0ooo0000oo0 = osl[1]           
            o0oo000o0oooo0oooooo0 = osl[2]           
            oo00oo0o00000000ooo0o = osl[3]           
            oo0oo000ooooo0oo00ooo = osl[4]         
            o0ooooooo0oo00ooooo0o = osl[5]            
            ooooo0ooo0o00ooo0o00o = osl[6]            
            ooo0oo0o0o00o0o0ooo0o = osl[7]           
            ooo000000o0o0o0ooo00o = osl[8]           
            o0000ooo0oooo0000oooo = osl[9]           
            ooo0000o0oo0o0000oo00 = osl[10]              
            e_on = osl[11]
            o000ooo0000ooo0o0o0oo = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif o000ooo0000ooo0o0o0oo:
                self.confirm_choice.SetSelection(1)
            oo000o0o00o00o0o0ooo0 = self.gettime(o0oo0o000o0ooo0000oo0)
            o00ooo00oo000000o0000 = self.gettime(o0oo000o0oooo0oooooo0)
            o00o0o0oo0oooo0ooo0o0 = self.gettime(ooooo0ooo0o00ooo0o00o)
            o0o0ooo00o0o0000oo0o0 = self.gettime(ooo0oo0o0o00o0o0ooo0o)
    def o000ooo0oooo000000oo0(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.o0o00ooo00ooo0o00o0oo':
                    L.append(os.path.join(root, file))
        return L
    def o000ooo00oo00000o0o00(self, event):
        pass
    def oo00000oooo0o0o0o00o0(self, a):          
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time          
    def o0oo0o0ooo0oo0oo0oooo(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a             
    def gettime(self, choice):                          
        tem = self.o0oo0o0ooo0oo0oo0oooo()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.oo00000oooo0o0o0o00o0(b) + float(choice) - int(choice)
        return c                 
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          
    def Draw(self, dc):          
        global ooo0oo0000000o0oo000o
        st = str(ooo0oo0000000o0oo000o)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
    def Modify(self, dc):      
        global ooo0oo0000000o0oo000o
        st = str(ooo0oo0000000o0oo000o)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=oooo0oo00o0oo0oo0oo0oframe_pos,
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
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.o0ooooo000o000o0oo000)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()
        self.helplink = hyperlink.HyperLinkCtrl(self.panel, -1, u"查看帮助")
        self.helplink.UnsetToolTip()
        self.helplink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.o0ooooo000o000o0oo000)
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
        pub.subscribe(self.o0ooooo0o0o0o000oooo0, "connect")
        self.hashthread = HashThread()
    def o0ooooo0o0o0o000oooo0(self):
        self.loginbtn.Enable()
        global o00000o00o000oooo0oo0, url2, url3          
        if o00000o00o000oooo0oo0['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)
            if o0oo0oo0o0o0o000o0o0o == 'helong' or o0oo0oo0o0o0o000o0o0o == 'yuanjunkai' or o0oo0oo0o0o0o000o0o0o == 'zs':
                url2 = 'http://moni.51hupai.org/'
            else:
                url2 = o00000o00o000oooo0oo0['url_dianxin']
            url3 = o00000o00o000oooo0oo0['url_nodianxin']
        elif o00000o00o000oooo0oo0['result'] == 'net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o00000o00o000oooo0oo0['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o00000o00o000oooo0oo0['result'] == 'wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif o00000o00o000oooo0oo0['result'] == 'wrong password':
            wx.MessageBox('密码错误', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('登录失败', '用户登录', wx.OK | wx.ICON_ERROR)
    def ooo00o0o000o00000o000(self, event):
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
        global o0oo0oo0o0o0o000o0o0o, oo0ooooo000o0oo00000o
        username = self.userText.GetValue()
        password = self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
        else:
            o0oo0oo0o0o0o000o0o0o = username               
            oo0ooooo000o0oo00000o = password
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            event.GetEventObject().Disable()
    def o0ooooo000o000o0oo000(self, event):
        print("购买")
class UserValidator(wx.Validator):
    ''' o0o00o0o00o00o0oo0ooos data as it is entered into the text controls. '''
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)
    def o0o00o0o00o00o0oo0ooo(self, win):
        return True
    def ooooo0000o0o00o0oo0o0(self):
        return True
    def o00oo0oooo00o0o0o000o(self):
        return True
    def OnChar(self, event):
        pass
class PassValidator(wx.Validator):
    ''' o0o00o0o00o00o0oo0ooos data as it is entered into the text controls. '''
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        '''Required Validator method'''
        return PassValidator()
    def o0o00o0o00o00o0oo0ooo(self, win):
        return True
    def ooooo0000o0o00o0oo0o0(self):
        return True
    def o00oo0oooo00o0o0o000o(self):
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
        global o00000o0o00oooo0000oo, oo000oo00o00oo0o00o0o
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            o00000o0o00oooo0000oo += b - a                
            oo000oo00o00oo0o00o0o += b - a
            if oo000oo00o00oo0o00o0o >= 60:
                oo000oo00o00oo0o00o0o = 0
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
        Click2(oo0oo0o0o00o0000oooo0[6][0] + 17, oo0oo0o0o00o0000oooo0[6][1])
        for i in range(15):
            Delete()
        if oo00o00oo0o0oo0o0o0oo:
            o00000000oooo0000ooo0()
        else:
            Paste()      
        Click(oo0oo0o0o00o0000oooo0[1][0], oo0oo0o0o00o0000oooo0[1][1])
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
class oo000o0oooo00oo0ooo0oThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()
    def run(self):
        for i in range(1000000):
            global ooo0oo00ooooo00o0o0oo
            if ooo0oo00ooooo00o0o0oo:
                try:
                    print("找着呢")
                    oo000o0oooo00oo0ooo0o()      
                    time.sleep(0.1)          
                except:
                    logging.error("oo000o0oooo00oo0ooo0othread error")
                    print("oo000o0oooo00oo0ooo0othread error")
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
            global o0oo00oooo0ooooo00o0o
            if o0oo00oooo0ooooo00o0o == 2:
                try:
                    o0oo000o00ooo0oooooo0()
                except:
                    print("查找确认出错")
    def pause(self):
        self.__flag.clear()                   
    def resume(self):
        self.__flag.set()                    
    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            
class ooo000oo0o0ooo0o0o0o0Thread(Thread):
    def __init__(self, *args, **kwargs):
        super(ooo000oo0o0ooo0o0o0o0Thread, self).__init__(*args, **kwargs)
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
                o000o00oo0o000o000o0o()
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
        global o0oo0oo0o0o0o000o0o0o, o00000o00o000oooo0oo0
        o00000o00o000oooo0oo0 = oo0o00o00000o00oo000o()
        print(o00000o00o000oooo0oo0)
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
            o0000000oooo000o000oo()
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global oo00000o00ooo00o0000o, ooooo00oo000o00o0oo00, o0o00000ooo00ooo00o0o, ooo0oo0000000o0oo000o, o00oo000oo00oooo0o000, ooo00o00oooo0o000o0oo
        global oo000oo00o00oo0o00o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oooooo0000ooo0o0o0o, o0oo000o00oooo00000o0, o00o0o0oo0oooo0ooo0o0, o0o0ooo00o0o0000oo0o0
        global o0ooooooo0oo00ooooo0o, ooo0000o0oo0o0000oo00, o0oo00oooo0ooooo00o0o, o0oo000o00oooo00000o0, o0oo0000oo00o0o00o000, o0oooooo0000ooo0o0o0o, oo0o000000o0o0o0000oo
        for i in range(10000000):
            time.sleep(0.05)              
            if o0oooooo0000ooo0o0o0o and o000000ooooo0oo00o0o0 and oooo0oooo0000o0000o00 and o0oo000o00oooo00000o0:                       
                if o0oo00oooo0ooooo00o0o == 1 and o00000o0o00oooo0000oo >= o00ooo00oo000000o0000 and not oo0o000000o0o0o0000oo:            
                    o0oooooo0000ooo0o0o0o = False
                    TopFrame.oo00o0000oooooo0o0oo0()        
                    o0oooooo0000ooo0o0o0o = False
                    logging.info("Rone_o0o000o0oooo00o00o0oo %s%s%s%s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00, o0oo000o00oooo00000o0))
                    logging.info("Rone_o0o000o0oooo00o00o0oo %s%s%s" % (o0oo00oooo0ooooo00o0o, o00000o0o00oooo0000oo, o00ooo00oo000000o0000))
                    oo0o000000o0o0o0000oo = True
                elif o0oo00oooo0ooooo00o0o == 2 and o00000o0o00oooo0000oo >= o0o0ooo00o0o0000oo0o0:            
                    o0oooooo0000ooo0o0o0o = False
                    TopFrame.oo00o0000oooooo0o0oo0()        
                    o0oooooo0000ooo0o0o0o = False
                    logging.info("Rsecond_o0o000o0oooo00o00o0oo %s%s%s%s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00, o0oo000o00oooo00000o0))
                    logging.info("Rsecond_o0o000o0oooo00o00o0oo %s%s%s" % (o0oo00oooo0ooooo00o0o, o00000o0o00oooo0000oo, o0o0ooo00o0o0000oo0o0))
                elif o0oo00oooo0ooooo00o0o == 1 and ooo0oo0000000o0oo000o >= o00oo000oo00oooo0o000 - 300 - o0ooooooo0oo00ooooo0o and o00000o0o00oooo0000oo <= o00ooo00oo000000o0000 - oo0oo000ooooo0oo00ooo and not oo0o000000o0o0o0000oo:        
                    o0oooooo0000ooo0o0o0o = False
                    o0oooooo0000ooo0o0o0o = False                        
                    TopFrame.ooo0oo0oo000000oo0oo0()        
                    logging.info("Rone_o0o000o0oooo00o00o0oo %s%s%s%s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00, o0oo000o00oooo00000o0))
                    logging.info("Rone_o0o000o0oooo00o00o0oo %s%s%s" % (o0oo00oooo0ooooo00o0o, ooo0oo0000000o0oo000o, o00oo000oo00oooo0o000))
                    oo0o000000o0o0o0000oo = True
                elif o0oo00oooo0ooooo00o0o == 2 and ooo0oo0000000o0oo000o >= ooo00o00oooo0o000o0oo - 300 - ooo0000o0oo0o0000oo00 and o00000o0o00oooo0000oo <= o0o0ooo00o0o0000oo0o0 - o0000ooo0oooo0000oooo:        
                    o0oooooo0000ooo0o0o0o = False
                    o0oooooo0000ooo0o0o0o = False                        
                    TopFrame.ooo0oo0oo000000oo0oo0()        
                    logging.info("Rsecond_o0o000o0oooo00o00o0oo %s%s%s%s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00, o0oo000o00oooo00000o0))
                    logging.info("Rsecond_o0o000o0oooo00o00o0oo %s%s%s" % (o0oo00oooo0ooooo00o0o, ooo0oo0000000o0oo000o, ooo00o00oooo0o000o0oo))
            if o000000ooooo0oo00o0o0 and oooo0oooo0000o0000o00 and o0oo0000oo00o0o00o000:                       
                if o0oo00oooo0ooooo00o0o == 1 and oo000o0o00o00o0o0ooo0 <= o00000o0o00oooo0000oo <= oo000o0o00o00o0o0ooo0 + 0.6:            
                    TopFrame.ooo000o0o00o00ooo00o0()        
                    o00oo000oo00oooo0o000 = ooo0oo0000000o0oo000o + oo00oo0o00000000ooo0o
                    o0oooooo0000ooo0o0o0o = True   
                    logging.info("Rone_oo0o0ooo00o0o0o0oo00o %s%s" % (o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00))
                    logging.info("Rone_oo0o0ooo00o0o0o0oo00o %s%s" % (o0oo0o000o0ooo0000oo0, oo000o0o00o00o0o0ooo0))
                elif o0oo00oooo0ooooo00o0o == 2 and twice and o00o0o0oo0oooo0ooo0o0 <= o00000o0o00oooo0000oo:            
                    TopFrame.ooo000o0o00o00ooo00o0()        
                    ooo00o00oooo0o000o0oo = ooo0oo0000000o0oo000o + ooo000000o0o0o0ooo00o
                    o0oooooo0000ooo0o0o0o = True
                    logging.info("Rsecond_oo0o0ooo00o0o0o0oo00o %s%s" % (o000000ooooo0oo00o0o0, oooo0oooo0000o0000o00))
                    logging.info("Rsecond_oo0o0ooo00o0o0o0oo00o %s%s" % (ooooo0ooo0o00ooo0o00o, o00o0o0oo0oooo0ooo0o0))
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
    def run(self):
        global oo000oo00o00oo0o00o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oooooo0000ooo0o0o0o, o00oo000oo00oooo0o000, ooo00o00oooo0o000o0oo, oo00oo0o00000000ooo0o, ooo000000o0o0o0ooo00o
        global o0oo00oooo0ooooo00o0o, o0oo000o00oooo00000o0, o0ooooooo0oo00ooooo0o, ooo0000o0oo0o0000oo00, oo0o000000o0o0o0000oo
        for i in range(10000000):
            time.sleep(0.05)              
            if o0oooooo0000ooo0o0o0o and o000000ooooo0oo00o0o0 and oo00o00oo0o0oo0o0o0oo and o0oo000o00oooo00000o0:                     
                if o0oo00oooo0ooooo00o0o == 1 and oo000oo00o00oo0o00o0o >= o0oo000o0oooo0oooooo0 and not oo0o000000o0o0o0000oo:            
                    TopFrame.oo00o0000oooooo0o0oo0()        
                    logging.info("moni one_o0o000o0oooo00o00o0oo %s %s %s %s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oo000o00oooo00000o0))
                    logging.info("moni one_o0o000o0oooo00o00o0oo %s %s %s" % (o0oo00oooo0ooooo00o0o, oo000oo00o00oo0o00o0o, o0oo000o0oooo0oooooo0))
                    o0oooooo0000ooo0o0o0o = False
                    oo0o000000o0o0o0000oo = True         
                elif o0oo00oooo0ooooo00o0o == 2 and oo000oo00o00oo0o00o0o >= ooo0oo0o0o00o0o0ooo0o and twice:            
                    TopFrame.oo00o0000oooooo0o0oo0()        
                    logging.info("moni1 second_o0o000o0oooo00o00o0oo %s %s %s %s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oo000o00oooo00000o0))
                    logging.info("moni second_o0o000o0oooo00o00o0oo %s %s %s" % (o0oo00oooo0ooooo00o0o, oo000oo00o00oo0o00o0o, ooo0oo0o0o00o0o0ooo0o))
                    o0oooooo0000ooo0o0o0o = False
                elif o0oo00oooo0ooooo00o0o == 1 and ooo0oo0000000o0oo000o >= o00oo000oo00oooo0o000 - 300 - o0ooooooo0oo00ooooo0o and not oo0o000000o0o0o0000oo:        
                    o0oooooo0000ooo0o0o0o = False                        
                    TopFrame.ooo0oo0oo000000oo0oo0()        
                    logging.info("moni one_o0o000o0oooo00o00o0oo %s %s %s %s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oo000o00oooo00000o0))
                    logging.info("moni one_o0o000o0oooo00o00o0oo %s %s %s" % (o0oo00oooo0ooooo00o0o, ooo0oo0000000o0oo000o, o00oo000oo00oooo0o000))
                    oo0o000000o0o0o0000oo = True         
                elif o0oo00oooo0ooooo00o0o == 2 and ooo0oo0000000o0oo000o >= ooo00o00oooo0o000o0oo - 300 - ooo0000o0oo0o0000oo00 and twice:        
                    o0oooooo0000ooo0o0o0o = False                        
                    TopFrame.ooo0oo0oo000000oo0oo0()        
                    logging.info("moni2 second_o0o000o0oooo00o00o0oo %s%s%s%s" % (o0oooooo0000ooo0o0o0o, o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo, o0oo000o00oooo00000o0))
                    logging.info("moni second_o0o000o0oooo00o00o0oo %s%s%s" % (o0oo00oooo0ooooo00o0o, ooo0oo0000000o0oo000o, ooo00o00oooo0o000o0oo))
            if o000000ooooo0oo00o0o0 and oo00o00oo0o0oo0o0o0oo and o0oo0000oo00o0o00o000:                     
                if o0oo00oooo0ooooo00o0o == 1 and o0oo0o000o0ooo0000oo0 <= oo000oo00o00oo0o00o0o <= o0oo0o000o0ooo0000oo0 + 0.6:            
                    TopFrame.ooo000o0o00o00ooo00o0()        
                    print("第一次")
                    o00oo000oo00oooo0o000 = ooo0oo0000000o0oo000o + oo00oo0o00000000ooo0o
                    o0oooooo0000ooo0o0o0o = True
                    logging.info("moni one_oo0o0ooo00o0o0o0oo00o %s %s" % (o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo))
                    logging.info("moni one_oo0o0ooo00o0o0o0oo00o %s %s" % (o0oo0o000o0ooo0000oo0, oo000oo00o00oo0o00o0o))
                elif o0oo00oooo0ooooo00o0o == 2 and twice and ooooo0ooo0o00ooo0o00o < oo000oo00o00oo0o00o0o:
                    TopFrame.ooo000o0o00o00ooo00o0()        
                    print("第二次")
                    ooo00o00oooo0o000o0oo = ooo0oo0000000o0oo000o + ooo000000o0o0o0ooo00o
                    o0oooooo0000ooo0o0o0o = True
                    logging.info("moni second_oo0o0ooo00o0o0o0oo00o %s %s" % (o000000ooooo0oo00o0o0, oo00o00oo0o0oo0o0o0oo))
                    logging.info("moni second_oo0o0ooo00o0o0o0oo00o %s %s" % (ooooo0ooo0o00ooo0o00o, oo000oo00o00oo0o00o0o))
class Infoframe(wx.Frame):
    def __init__(self, name, user, psd):               
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
oo0oo0000oo0o00o0o000 = "本地IE"
class Guopaiframe(wx.Dialog):
    def __init__(self, name):               
        wx.Frame.__init__(self, None, -1, name, size=(195, 265), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(195, 270))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.oo0oo0000oo0o00o0o000 = oo0oo0000oo0o00o0o000
        self.dianxin = wx.Button(self.panel, label="上海电信", pos=(20, 10), size=(140, 60))
        self.nodianxin = wx.Button(self.panel, label="非电信", pos=(20, 80), size=(140, 60))
        self.userweb = wx.Button(self.panel, label=self.oo0oo0000oo0o00o0o000, pos=(20, 150), size=(140, 60))
        self.dianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.nodianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.userweb.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_BUTTON, self.Dianxin, self.dianxin)
        self.Bind(wx.EVT_BUTTON, self.oo00o0o00o0o0o0o00o00, self.nodianxin)
        self.Bind(wx.EVT_BUTTON, self.UserWeb, self.userweb)
        self.Center()
        self.ShowModal()
    def Dianxin(self, event):
        wx.CallAfter(pub.sendMessage, "open dianxin")
        self.Destroy()
        event.Skip()
    def oo00o0o00o0o0o0o00o00(self, event):
        wx.CallAfter(pub.sendMessage, "open nodianxin")
        self.Destroy()
        event.Skip()
    def UserWeb(self, event):
        global oo0oo0000oo0o00o0o000, oooo0oooo0000o0000o00
        if oo0oo0000oo0o00o0o000 == '本地IE' and not oooo0oooo0000o0000o00:
            oooo0oooo0000o0000o00 = True            
            oo0oo0000oo0o00o0o000 = '关闭辅助'
            wx.CallAfter(pub.sendMessage, "open userweb")
        else:
            oo0oo0000oo0o00o0o000 = '本地IE'
            oooo0oooo0000o0000o00 = False            
            TopFrame.Close()
            try:
                yan = self.FindWindowById(18)
                yan.Destroy()
                global oo0oooo0o00oo00000000
                print("关闭成功")
                oo0oooo0o00oo00000000 = False
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
    o0oo00o000oooooo00000()
    o0oo000oo0o0oooooooo0()            
    app = SketchApp()
    confirmthread = confirmThread()       
    ooo000oo0o0ooo0o0o0o0thread = ooo000oo0o0ooo0o0o0o0Thread()       
    finposthread = oo000o0oooo00oo0ooo0oThread()        
    cutimgthread = cutimgThread()        
    app.MainLoop()
