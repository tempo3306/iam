                 
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
ad_view = False        

zxco0o0o0o0_view = False             
sdfsnisdfafzxcv_view = False              
sdfsnisdfafzxcv_close = True            
sdfsnisdfafzxcv_move = True          

sdfsnisdfafzxcv_hash = 0                              

zxco0o0o0o0_on = False          
zxco0o0o0o0_count = 0               
sdfsnisdfafzxcv_count = 0               
web_on = False             
    
view_time = False           
operation_show = False           
time_on = False               
import time

a_time = time.time()          
b_time = 0          

o0sdofsfo0sodf0so0_minute = 29
o0sdofsfo0sodf0so0_ooo0O0o0oO0O = 0

oo0o0O0O0O0_time = 0        

Username = 0       
Password = 0      

o0sdofsfo0sodf0so0_on = False                          
ooweo0o0werwr_on = False

ghjo0o0o0o01 = 53          
ghjo0o0o0o02 = 0.0          

                                
                                 


ghjo0o0o0o0_on = True          
ghjo0o0o0o0_repeat = False                 
                             

delay = False        
delay_time = 0.5          

login_result = False          

findpos_on = True           

zxco0o0o0o0list = [80000 + i * 100 for i in range(400)]          
IDnumber = 0        
account = 0       
passwd = 0      

        
changetime = 0

                                                      
import pyautogui as pg


           
def Create_hash():
    with open('dick.dl', 'rb') as dick:
        global dick_hash
        dick_hash = pickle.load(dick)                 
    with open('cf.btn', 'rb') as cf:
        global cf_hash
        cf_hash = pickle.load(cf)                            

    with open("target.tkl", 'rb')  as tar:
        global dick_target
        dick_target = pickle.load(tar)            


                                       
        
OO00000o01 = 48           
OO00000o02 = 55           
one_oO0O0O0O0O0O0O0O01 = 1000000000000             
one_oO0O0O0O0O0O0O0O02 = 1000000000000             
one_diff = 700           
one_delay = 0.5         
one_advance = 100            

ooo0O0o0oO0O_time1 = 48            
ooo0O0o0oO0O_time2 = 55           
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = 1000000000000             
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = 1000000000000             
ooo0O0o0oO0O_diff = 600           
ooo0O0o0oO0O_delay = 0.5           
ooo0O0o0oO0O_advance = 100              

osl = [0] * 15                          

oo0o0O0O0O0_on = True                      
oOO0O0O0O0O0O0_on = False                  

O0O0O0O0O0O0O_zxco0o0o0o0 = 93400         
own_zxco0o0o0o01 = 0         
own_zxco0o0o0o02 = 0         
own_zxco0o0o0o0 = 0        

oOO0O0O0O0O0O0_OK = False           
e_on = True                  
enter_on = False                   

twice = False          
oOO0O0O0O0O0O0_num = 1                         
oOO0O0O0O0O0O0_one = False             
                                                                 
              
websize = [902, 700]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2          
Py2 = Pxy[1] / 2
Px = (Pxy[0] - websize[0]) / 2 - 80
Py = (Pxy[1] - websize[1]) / 2
        
                                                            
P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]]               
P_relative2 = [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
Oo0o0Oo0o0o0 = [[0, 0] for i in range(len(P_relative))]
for i in range(len(Oo0o0Oo0o0o0)):
    Oo0o0Oo0o0o0[i][0] = Px1 + P_relative[i][0]
    Oo0o0Oo0o0o0[i][1] = Py2 + P_relative[i][1]
                   
                    
px_ajust, py_ajust = 0, 0
for i in range(len(P_relative)):
    P_relative[i][0] += websize[0] / 2 + px_ajust
    P_relative[i][1] += websize[1] / 2 + py_ajust      
         
px_zxco0o0o0o0 = 770 - 171
py_zxco0o0o0o0 = 260
            
px_zxco0o0o0o0frame = 220 - 191
py_zxco0o0o0o0frame = 480
          
px_timeframe = 22
py_timeframe = 350
            
px_O0O0O0O0O0O0Ozxco0o0o0o0frame = 245
py_O0O0O0O0O0O0Ozxco0o0o0o0frame = 290
O0O0O0O0O0O0Ozxco0o0o0o0frame_pos = [px_O0O0O0O0O0O0Ozxco0o0o0o0frame, py_O0O0O0O0O0O0Ozxco0o0o0o0frame]

       
px_sdfsnisdfafzxcvframe = 400 - 215
py_sdfsnisdfafzxcvframe = 460

        
px_mini = 200
py_mini = 40
       
Pricesize = [400, 80]
          
Yanzhengmasize = [400, 220]
       
Timesize = [200, 50]

                                                                        
O0O0O0O0O0O0Ozxco0o0o0o0_area = [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py]
uioo0o000oo_area = [396 - 150, 11 - 100, 396 + 150, 11 + 100]
confirm_area = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
yan_confirm_area = [505 - 300, 68 - 150, 505 + 300, 68 + 150]

          
ghostbutton_pos = [0,0]
webview_pos = [-25,0]                      
                                                                     
                      
        
      
                              
                               
         
                     
                                                                                        
                                                                                   


                                                              
                                                           

           
Px_zxco0o0o0o0 = Px + px_zxco0o0o0o0
Py_zxco0o0o0o0 = Py + py_zxco0o0o0o0
Pos_zxco0o0o0o0 = [Px_zxco0o0o0o0, Py_zxco0o0o0o0, Px_zxco0o0o0o0 + px_mini, Py_zxco0o0o0o0 + py_mini]               

Pos_sdfsnisdfafzxcv = []           

              
Px_zxco0o0o0o0frame = Px + px_zxco0o0o0o0frame
Py_zxco0o0o0o0frame = Py + py_zxco0o0o0o0frame
Pos_zxco0o0o0o0frame = [Px_zxco0o0o0o0frame, Py_zxco0o0o0o0frame]

            
Px_timeframe = px_timeframe + Px
Py_timeframe = py_timeframe + Py
Pos_timeframe = [Px_timeframe, Py_timeframe]
          
Pos_controlframe = [Px + 40, Py + 480]

         
Px_sdfsnisdfafzxcvframe = Px + px_sdfsnisdfafzxcvframe
Py_sdfsnisdfafzxcvframe = Py + py_sdfsnisdfafzxcvframe
Pos_sdfsnisdfafzxcvframe = [Px_sdfsnisdfafzxcvframe, Py_sdfsnisdfafzxcvframe]

                           
          
           
            
                                              
                                
px_O0O0O0O0O0O0Ozxco0o0o0o0 = 0                         
py_O0O0O0O0O0O0Ozxco0o0o0o0 = 0            



             
Px_O0O0O0O0O0O0Ozxco0o0o0o0 = Px + px_O0O0O0O0O0O0Ozxco0o0o0o0
Py_O0O0O0O0O0O0Ozxco0o0o0o0 = Py + py_O0O0O0O0O0O0Ozxco0o0o0o0
O0O0O0O0O0O0Ozxco0o0o0o0_sizex = 82           
                               
O0O0O0O0O0O0Ozxco0o0o0o0_sizey = 16
              

Px_currenttime =Px_O0O0O0O0O0O0Ozxco0o0o0o0-25             
Py_currenttime = Py_O0O0O0O0O0O0Ozxco0o0o0o0+17
currenttime_sizex = 132
currenttime_sizey = 16



px_relative = 49                
py_relative = 0
         
px_confirm = 656
py_confirm = 475
Px_confirm = Px + px_confirm
Py_confirm = Py + py_confirm
confirm_sizex = 113
confirm_sizey = 28
confirm_on = False          
confirm_need = False          
confirm_one = False             
        
px_uioo0o000oo = 550
py_uioo0o000oo = 413
Px_uioo0o000oo = Px + px_uioo0o000oo
Py_uioo0o000oo = Py + py_uioo0o000oo
uioo0o000oo_sizex = 108
uioo0o000oo_sizey = 21
uioo0o000oo_on = False          
uioo0o000oo_need = False          
uioo0o000oo_one = False             

oo0o0O0O0O0_interval = False        
oOO0O0O0O0O0O0_interval = False        
query_interval = False      
query_on = False            

        
import numpy as np

sc_area = [Px_O0O0O0O0O0O0Ozxco0o0o0o0 - 10, Py_O0O0O0O0O0O0Ozxco0o0o0o0 - 100, Px_O0O0O0O0O0O0Ozxco0o0o0o0 + 600, Py_O0O0O0O0O0O0Ozxco0o0o0o0 + 120]
use_area = []
nptemp = []
o0o0oo0oo0o0o000o_O0O0O0O0O0O0Ozxco0o0o0o0 = np.array(nptemp)       
o0o0oo0oo0o0o000o_uioo0o000oo = np.array(nptemp)       
o0o0oo0oo0o0o000o_confirm = np.array(nptemp)         
impos_sdfsnisdfafzxcv = np.array(nptemp)       
o0o0oo0oo0o0o000o_sdfsnisdfafzxcvconfirm = np.array(nptemp)         
o0o0oo0oo0o0o000o_currenttime = np.array(nptemp)        

                                                                  
                           
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

              
        
yimg = ImageGrab.grab().save("sdfsnisdfafzxcv.png")
sdfsnisdfafzxcv_img = Image.open("sdfsnisdfafzxcv.png")                         


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


                      
def Paste_o0sdofsfo0sodf0so0():
    global ghostbutton_pos
    Click(ghostbutton_pos[0],ghostbutton_pos[1])

                                  
                                                                      
                                                                    
                                            
                                                                      


       
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
                


      
def findpos():
                            
                                                         
    sc = ImageGrab.grab().convert('L')
    img = np.asarray(sc)
    global dick_target
    template = dick_target[2]
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
                    
                    
                    
    global px_O0O0O0O0O0O0Ozxco0o0o0o0, py_O0O0O0O0O0O0Ozxco0o0o0o0, px_relative, py_relative, Px_O0O0O0O0O0O0Ozxco0o0o0o0, Py_O0O0O0O0O0O0Ozxco0o0o0o0, Px, Py
    global uioo0o000oo_area, confirm_area, Pos_timeframe, Pos_controlframe, Pos_sdfsnisdfafzxcv, Pos_sdfsnisdfafzxcvframe, yan_confirm_area
    global use_area, sc_area          
    global Oo0o0Oo0o0o0, uioo0o000oo_area, confirm_area, Pos_timeframe, Pos_controlframe, Pos_sdfsnisdfafzxcv, Pos_sdfsnisdfafzxcvframe, yan_confirm_area
    global Px_currenttime,Py_currenttime           
    global ghostbutton_pos
    if max_val > 0.9:          
        px_O0O0O0O0O0O0Ozxco0o0o0o0 = max_loc[0] + px_relative
        py_O0O0O0O0O0O0Ozxco0o0o0o0 = max_loc[1] + py_relative
        Px_O0O0O0O0O0O0Ozxco0o0o0o0 = px_O0O0O0O0O0O0Ozxco0o0o0o0
        Py_O0O0O0O0O0O0Ozxco0o0o0o0 = py_O0O0O0O0O0O0Ozxco0o0o0o0

        Px_currenttime = Px_O0O0O0O0O0O0Ozxco0o0o0o0 -27             
        Py_currenttime = Py_O0O0O0O0O0O0Ozxco0o0o0o0 -16

               
        ghostbutton_pos = [px_O0O0O0O0O0O0Ozxco0o0o0o0-9,py_O0O0O0O0O0O0Ozxco0o0o0o0+84]


                                              

        for i in range(len(Oo0o0Oo0o0o0)):
            Oo0o0Oo0o0o0[i][0] = Px_O0O0O0O0O0O0Ozxco0o0o0o0 + P_relative2[i][0]
            Oo0o0Oo0o0o0[i][1] = Py_O0O0O0O0O0O0Ozxco0o0o0o0 + P_relative2[i][1]
        uioo0o000oo_area = [396 - 150 + Px_O0O0O0O0O0O0Ozxco0o0o0o0, 11 - 100 + Py_O0O0O0O0O0O0Ozxco0o0o0o0, 396 + 150 + Px_O0O0O0O0O0O0Ozxco0o0o0o0,
                        11 + 100 + Py_O0O0O0O0O0O0Ozxco0o0o0o0]
        confirm_area = [505 - 80 + Px_O0O0O0O0O0O0Ozxco0o0o0o0, 68 - 50 + Py_O0O0O0O0O0O0Ozxco0o0o0o0, 505 + 80 + Px_O0O0O0O0O0O0Ozxco0o0o0o0,
                        68 + 50 + Py_O0O0O0O0O0O0Ozxco0o0o0o0]
        yan_confirm_area = [205 - 80 + Px_O0O0O0O0O0O0Ozxco0o0o0o0, 68 - 50 + Py_O0O0O0O0O0O0Ozxco0o0o0o0, 405 + 80 + Px_O0O0O0O0O0O0Ozxco0o0o0o0,
                            68 + 50 + Py_O0O0O0O0O0O0Ozxco0o0o0o0]

        Pos_controlframe = [192 - 344 + Px_O0O0O0O0O0O0Ozxco0o0o0o0, 514 - 183 + Py_O0O0O0O0O0O0Ozxco0o0o0o0]

        Pos_sdfsnisdfafzxcv = [Oo0o0Oo0o0o0[5][0] - 277, Oo0o0Oo0o0o0[5][1] - 65, Oo0o0Oo0o0o0[5][0] - 97,
                          Oo0o0Oo0o0o0[5][1] + 45]           
                                                                                    
        Pos_sdfsnisdfafzxcvframe = [Px_O0O0O0O0O0O0Ozxco0o0o0o0 + 297, Py_O0O0O0O0O0O0Ozxco0o0o0o0 - 283]            
                                                                           
              
        global findpos_on, sdfsnisdfafzxcv_move
        findpos_on = False        
        sdfsnisdfafzxcv_move = True        
                                  
                  

        O0O0O0O0O0O0O = [Px_O0O0O0O0O0O0Ozxco0o0o0o0, Py_O0O0O0O0O0O0Ozxco0o0o0o0,  O0O0O0O0O0O0Ozxco0o0o0o0_sizex+Px_O0O0O0O0O0O0Ozxco0o0o0o0, O0O0O0O0O0O0Ozxco0o0o0o0_sizey+Py_O0O0O0O0O0O0Ozxco0o0o0o0]
        currenttime = [Px_currenttime,Py_currenttime,Px_currenttime+currenttime_sizex,Py_currenttime+currenttime_sizey]
        dis_x=50
        dis_y=100
        x1 = Px_O0O0O0O0O0O0Ozxco0o0o0o0 - dis_x         
        y1 = Py_O0O0O0O0O0O0Ozxco0o0o0o0 - dis_y

        cal_area = [O0O0O0O0O0O0O, uioo0o000oo_area, confirm_area, Pos_sdfsnisdfafzxcv, yan_confirm_area , currenttime]          
        use_area = []
        sc_area = [Px_O0O0O0O0O0O0Ozxco0o0o0o0 - dis_x, Py_O0O0O0O0O0O0Ozxco0o0o0o0 - dis_y, Px_O0O0O0O0O0O0Ozxco0o0o0o0 + 600, Py_O0O0O0O0O0O0Ozxco0o0o0o0 + 120]
        for i in range(len(cal_area)):
            temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
            use_area.append(temp)

                   




                                                         
def only_screenshot(area):                          
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
    global use_area, sc_area, o0o0oo0oo0o0o000o_O0O0O0O0O0O0Ozxco0o0o0o0, o0o0oo0oo0o0o000o_sdfsnisdfafzxcv, o0o0oo0oo0o0o000o_uioo0o000oo, o0o0oo0oo0o0o000o_confirm, o0o0oo0oo0o0o000o_sdfsnisdfafzxcvconfirm,o0o0oo0oo0o0o000o_currenttime
    img = only_screenshot(sc_area)           
        
    img = np.asarray(img)              

                                                                                                                
               
    o0o0oo0oo0o0o000o_O0O0O0O0O0O0Ozxco0o0o0o0 = img[use_area[0][1]:use_area[0][3], use_area[0][0]:use_area[0][2]]      
    o0o0oo0oo0o0o000o_uioo0o000oo = img[use_area[1][1]:use_area[1][3], use_area[1][0]:use_area[1][2]]      
    o0o0oo0oo0o0o000o_confirm = img[use_area[2][1]:use_area[2][3], use_area[2][0]:use_area[2][2]]
    o0o0oo0oo0o0o000o_sdfsnisdfafzxcv = img[use_area[3][1]:use_area[3][3], use_area[3][0]:use_area[3][2]]      
    o0o0oo0oo0o0o000o_sdfsnisdfafzxcvconfirm = img[use_area[4][1]:use_area[4][3], use_area[4][0]:use_area[4][2]]      
    o0o0oo0oo0o0o000o_currenttime = img[use_area[5][1]:use_area[5][3], use_area[5][0]:use_area[5][2]]

def finduioo0o000oo():
    global dick_target, uioo0o000oo_on, uioo0o000oo_need, uioo0o000oo_one, Oo0o0Oo0o0o0, uioo0o000oo_area, confirm_area
    template = dick_target[0]
    global o0o0oo0oo0o0o000o_uioo0o000oo
    sc = o0o0oo0oo0o0o000o_uioo0o000oo
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        

                                       
                                                    
                                        
                          
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    logging.info("查找刷新")
    if max_val >= 0.8:
        logging.info("刷新")
        TopFrame.OnClick_Shuaxin()
        global sdfsnisdfafzxcv_view, sdfsnisdfafzxcv_close, sdfsnisdfafzxcv_count
        sdfsnisdfafzxcv_view = True         
        sdfsnisdfafzxcv_count = 0      

                                   
                      
                                                    
                          


def findconfirm():
                   
    global dick_target, confirm_on, Oo0o0Oo0o0o0
    template = dick_target[1]
    global o0o0oo0oo0o0o000o_confirm
    sc = o0o0oo0oo0o0o000o_confirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        

                                       
                                                    
                          
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
    if max_val >= 0.9:
                       
                         
        TopFrame.OnClick_confirm()
    if confirm_on and max_val < 0.9:
        print("暂停确认")
                                    


                
def find_yan_confirm():
                   
    global dick_target, confirm_on, Oo0o0Oo0o0o0, sdfsnisdfafzxcv_view, sdfsnisdfafzxcv_close
    template = dick_target[1]
    global o0o0oo0oo0o0o000o_sdfsnisdfafzxcvconfirm
    sc = o0o0oo0oo0o0o000o_sdfsnisdfafzxcvconfirm
    img = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)        

                                           
                                                        
                          
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
    if max_val < 0.9:
        sdfsnisdfafzxcv_view = False
        sdfsnisdfafzxcv_close = True


        
                                                                                              
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


def new_screenshot(area):                          
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


def new_screenshot_getimg(area, size, name):
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
    zxco0o0o0o0 = "".join(list(result))
    print("zxco0o0o0o0==",zxco0o0o0o0)
    return zxco0o0o0o0                          

def timeset():
    global a_time, o0o0oo0oo0o0o000o_currenttime, o0sdofsfo0sodf0so0_ooo0O0o0oO0O
          
    currenttime = cv2.cvtColor(o0o0oo0oo0o0o000o_currenttime, cv2.COLOR_BGR2GRAY)
    currenttime = readpic(currenttime)           
    cv2.imwrite("zp.png", o0o0oo0oo0o0o000o_currenttime)
    print(currenttime)
    tem1 = time.time()
    a = time.strftime('%Y-%m-%d', time.localtime(tem1))
    b = a + ' ' + currenttime
    a_time = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S')) + 0.5                 
    try:
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O = int(currenttime.split(':')[2]) + 0.5
    except:
        pass

                                                                                  
          
           
               
               
               
             

                                            
                     
                   
 
 
                       
                                                
 
                                                                                    
                                        
                            
                                
 
 
                                           
                                                
                 
                                                  
                   
                                                        
                                                                        
                             
                                    
                               
 
                                                                     
                                                               
                                    
                                                                    
                                 
                       
                                  
                                                       
                                    
 
                                                
                                  
                     
                                      
                                                                      
                                                     
                                              
                        
 
                                         
                                                     
                                              
                                                                        
                                      
               
                                 
                                                        
                                                                                         
                                                  
 
                                                          
                                     
                        
 
                                    
             
                                      
             
                                                              
 
                         
 
                                                   
                                                                                 
                                                
                                              
                                                                             
 
                                                              
                                                       
                               
                                                                             
           
                                
                                               
 
                          
             
                                                            
             
                                              
              
                                                                         
                                    
                            
                                                             
                                                                                    
                                           
                                
                                           
 
 
                                      
 
                                     
                                                              
                      
                      
 
                     
             
                              
             
                                     
                                                         
                  
                                          
                                          
                                                                   
                                  
 
                               
                                                                                
                                  
 
                   
                                      
                                                        
                                   
           
                     

                                                                                   
       
import winreg, re, subprocess

needpath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
iepath = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
path1 = 'C:\Program Files (x86)'
path2 = 'C:\Program Files'


def getwebpath():
    global needpath
             
    try:
        key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"http\shell\open\command")
        name, value, type = winreg.EnumValue(key, 0)
        pattern = re.compile("\"*(.+\.exe)")
        result = re.findall(pattern, value)
        if result:
            needpath = result[0]
                                        
    except:
        pass
    if not os.path.exists(needpath):
        if os.path.exists('C:\Program Files (x86)'):
            pass
                       


def openweb(url):
    global needpath
                                                  
                                                                                 
    subprocess.Popen([needpath, url])


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


def ConfirmUser():
    try:
        target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
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
    global Username
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
                     
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
                     

            
                                         
                           
                                                    
                                                          
                  
                   
                                      
                                             


def Keeplogin():
    host = host_ali
                                                   
                                                            
    port = 8080
    global Username
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
                     
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
                     

            
    data = ['keep', Username, Password]
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")           
    logging.info('发送信息 %s' % str(data, encoding="utf-8"))
    s.send(data)

    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")


                                                                                  
def send_mail(subject, to_list, file_name):
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


                                                                                  
       
def Com_read():
    pass


                                                                                  
      
def Com_decision():
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
        self.o0sdofsfo0sodf0so0button = wx.Button(panel, label='打开模拟')
        self.Bind(wx.EVT_BUTTON, self.Openo0sdofsfo0sodf0so0, self.o0sdofsfo0sodf0so0button)
               
        self.ooweo0o0werwrbutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.Openurlchoice, self.ooweo0o0werwrbutton)
        self.hbox1.Add(self.o0sdofsfo0sodf0so0button, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.ooweo0o0werwrbutton, 0, wx.ALL | wx.CENTER, 5)
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
        self.Bind(wx.EVT_BUTTON, self.Advanceset, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.Posautoset, self.posautoset)
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
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)                 
        self.timer2.Start(100)          

                 
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Lowest_zxco0o0o0o0, self.timer3)                   
        self.timer3.Start(50)
              
                                    
                                                                      
                                

              
        self.Bind(wx.EVT_BUTTON, self.Time_autoajust, self.timeautoreset)            

                          
                                    
                                                   
                                                               

                     
        pub.subscribe(self.OpenGuopai_dianxin, "open dianxin")        
        pub.subscribe(self.OpenGuopai_nodianxin, "open nodianxin")         
        pub.subscribe(self.OpenGuopai_userweb, "open userweb")             

                                                                        
         
    def Openo0sdofsfo0sodf0so0(self, event):
             
        global oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, oOO0O0O0O0O0O0_OK, twice
        timer0 = threading.Timer(5, findpos)
        ghjo0o0o0o0_on = True
        twice = False
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px, Py, url1, ad_view, web_on, do, ooweo0o0werwr_on, o0sdofsfo0sodf0so0_on, ghjo0o0o0o0_repeat
        if ooweo0o0werwr_on:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif o0sdofsfo0sodf0so0_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:

                                                      
                                                                        
                                                 
            self.Open()
            if do:
                o0sdofsfo0sodf0so0_on = True        
                ad_view = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟')
                                                            
                             
                if time_on:
                    self.operationframe.Opentime()
                if not ghjo0o0o0o0_repeat:                
                    self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                    self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                    ghjo0o0o0o0_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                                                         
                                                           
                                                         
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()

    def Openurlchoice(self, event):
        ooweo0o0werwr = Guopaiframe("国拍")

    def OpenGuopai_dianxin(self):
             
        global oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, oOO0O0O0O0O0O0_OK, twice
        timer0 = threading.Timer(5, findpos)
        ghjo0o0o0o0_on = True
        twice = False
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px, Py, url2, ad_view, web_on, do, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on, ghjo0o0o0o0_repeat
        if o0sdofsfo0sodf0so0_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif ooweo0o0werwr_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
                                                      
                                                                        
                                                 
            if do:
                ad_view = True
                ooweo0o0werwr_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                                                            
                             
                if time_on:
                    self.operationframe.Opentime()
                if not ghjo0o0o0o0_repeat:                
                    self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                    self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                    ghjo0o0o0o0_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,  style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                      
                self.Listen()
                                                               
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             

    def OpenGuopai_nodianxin(self):
             
        global oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, oOO0O0O0O0O0O0_OK, twice
        timer0 = threading.Timer(5, findpos)
        ghjo0o0o0o0_on = True
        twice = False           
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px, Py, url3, ad_view, web_on, do, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on, ghjo0o0o0o0_repeat
        if o0sdofsfo0sodf0so0_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif ooweo0o0werwr_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
                                                      
                                                                        
                                                 
            if do:
                ad_view = True
                ooweo0o0werwr_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉代拍 国拍')          
                                                            
                             
                if time_on:
                    self.operationframe.Opentime()
                if not ghjo0o0o0o0_repeat:                
                    self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                    self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                    ghjo0o0o0o0_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos ,style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                      
                self.Listen()
                                                               
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()             

    def OpenGuopai_userweb(self):
             
        global oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, oOO0O0O0O0O0O0_OK, twice
        timer0 = threading.Timer(5, findpos)                
        ghjo0o0o0o0_on = True
        twice = False
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px, Py, url3, ad_view, web_on, do, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on, ghjo0o0o0o0_repeat

        self.Open()

                                                  
                                                                    
                                             
                   
        if do:
            ad_view = True
            ooweo0o0werwr_on = True
                                                                     
                                                        
                         
            if time_on:
                self.operationframe.Opentime()
            if not ghjo0o0o0o0_repeat:                
                self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                ghjo0o0o0o0_repeat = True
                 
                                                                                                                
                                       
                                               
                                     
                      
                openIE(url3)
                               
                self.Listen()
                                                           
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            self.Close()             

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
                                              
                                                 
                                                 
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)

             
    def rule(self, event):
        url = "http://hupai.pro/rules"
        OpenwebThread(url)

    def help(self, event):
        url = "http://hupai.pro/coursestudy"
        OpenwebThread(url)
               

    def Yan_practice(self, event):
        pass

    def Yan_test(self, event):
        pass
              

    def Time_adjust(self, event):
        pass

                                                                        
          
    def Advanceset(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)

    def Posautoset(self, event):
        findpos()

    def Timeautoset(self, event):
        pass

                                                                        
           
                   
    def Lowest_zxco0o0o0o0(self, event):   
        global O0O0O0O0O0O0O_zxco0o0o0o0, findpos_on, changetime
        try:
            zxco0o0o0o0 = int(TopFrame.Price_read())           
                  
            if zxco0o0o0o0 in zxco0o0o0o0list:        
                findpos_on = False
                if O0O0O0O0O0O0O_zxco0o0o0o0 == zxco0o0o0o0:
                    pass
                else:
                    O0O0O0O0O0O0O_zxco0o0o0o0 = zxco0o0o0o0
                                         
                    if o0sdofsfo0sodf0so0_on:
                        changetime = o0sdofsfo0sodf0so0_ooo0O0o0oO0O
                    else:
                        changetime = a_time
            else:
                print("重新查找")
                findpos_on = True
        except:
            findpos_on = True

            
                                       
                                        
                            
                                                               
                    
                                                 
                                                      
                   
                                 
                     

                              
          
          
    def Find_pos(self, event):
        global findpos_on
        if findpos_on:
            try:
                findpos()
            except:
                logging.error("Find_pos error")
                print("Find_pos error")

                      
    def Time_autoajust(self, event):
        timeset()          

    @staticmethod
    def Confirm():
        global cf_hash, confirm_on
        confirm_hash = TopFrame.Confirm_hash()          
        if confirm_hash == cf_hash[0]:
            confirm_on = True

    @staticmethod
    def Refresh():
        uioo0o000oo_hash = TopFrame.Refresh_hash()          
        global cf_hash, uioo0o000oo_on
        if uioo0o000oo_hash == cf_hash[1]:
            uioo0o000oo_on = True

                
    @staticmethod
    def Price_read():
                                                                     
                                                                                                                      

                                                                                                                                         

                                             



        global o0o0oo0oo0o0o000o_O0O0O0O0O0O0Ozxco0o0o0o0 , findpos_on
        global num
                       
                                                            
        num+=1

        O0O0O0O0O0O0O_zxco0o0o0o0 = cv2.cvtColor(o0o0oo0oo0o0o000o_O0O0O0O0O0O0Ozxco0o0o0o0, cv2.COLOR_BGR2GRAY)
        zxco0o0o0o0 = readpic(O0O0O0O0O0O0O_zxco0o0o0o0)
        print("zxco0o0o0o0=",zxco0o0o0o0)
        return zxco0o0o0o0


                   
                       
                                                                             
                                                                           
                    
                
                                          
                                                   
                            
                         
                           
     
                   
                         
                                                                 
                                                                   
                  
                                 
                                                 
                             
     
                   
                         
                                                                 
                                                                        
     
                                                 
                             

    @staticmethod
    def OnJiajia():
        po = pg.position()
        Oo0o0Oo0o0o0[0][0] = po[0]
        Oo0o0Oo0o0o0[0][1] = po[1]


    @staticmethod
    def OnChujia():
        po = pg.position()
        Oo0o0Oo0o0o0[1][0] = po[0]
        Oo0o0Oo0o0o0[1][1] = po[1]

    @staticmethod
    def OnTijiao():
        po = pg.position()
        Oo0o0Oo0o0o0[2][0] = po[0]
        Oo0o0Oo0o0o0[2][1] = po[1]

    @staticmethod
    def OnShuaxin():
        po = pg.position()
        Oo0o0Oo0o0o0[3][0] = po[0]
        Oo0o0Oo0o0o0[3][1] = po[1]

    @staticmethod
    def OnConfirm():
        po = pg.position()
        Oo0o0Oo0o0o0[4][0] = po[0]
        Oo0o0Oo0o0o0[4][1] = po[1]

    @staticmethod
    def OnYanzhengma():
        po = pg.position()
        Oo0o0Oo0o0o0[5][0] = po[0]
        Oo0o0Oo0o0o0[5][1] = po[1]

            
    @staticmethod
    def handle_Jiajia():
        TopFrame.OnJiajia()

    @staticmethod
    def handle_Chujia():
        TopFrame.OnChujia()

    @staticmethod
    def handle_Tijiao():
        x,y=win32api.GetCursorPos()
        print("x=",x," y=",y)

                   

                             

    @staticmethod
    def handle_Shuaxin():
        TopFrame.OnShuaxin()

    @staticmethod
    def handle_Confirm():
        TopFrame.OnConfirm()

    @staticmethod
    def handle_Yanzhengma():
        TopFrame.OnYanzhengma()

                                       

                
            
                
            

    @classmethod
    def OnClick_Tijiao(cls):
        global web_on, oOO0O0O0O0O0O0_on, one_delay, ooo0O0o0oO0O_delay, oOO0O0O0O0O0O0_num
        global oOO0O0O0O0O0O0_on, oo0o0O0O0O0_on, confirm_one, confirm_need
        confirm_need = True

        if oOO0O0O0O0O0O0_num == 1:
            timer = threading.Timer(one_delay, cls.Tijiao)
            timer.start()
            oOO0O0O0O0O0O0_on = False
            if twice:
                oOO0O0O0O0O0O0_num = 2
                            
        elif oOO0O0O0O0O0O0_num == 2:
            oOO0O0O0O0O0O0_num = 0
            timer = threading.Timer(ooo0O0o0oO0O_delay, cls.Tijiao)
            timer.start()
            oOO0O0O0O0O0O0_on = False
                            
        else:
            cls.Tijiao()

    @staticmethod
    def Tijiao():
        global oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on
        Click(Oo0o0Oo0o0o0[2][0], Oo0o0Oo0o0o0[2][1])
        oOO0O0O0O0O0O0_OK = False               
        oo0o0O0O0O0_on = True        
        global confirm_one
        if not confirm_one:        
            pass
                           
                                          

                                

                 
    @classmethod
    def SmartTijiao(cls):
        global oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_num, confirm_need

        confirm_need = True
        if o0sdofsfo0sodf0so0_on:
            interval = o0sdofsfo0sodf0so0_ooo0O0o0oO0O - changetime
        else:
            interval = a_time - changetime
        if oOO0O0O0O0O0O0_num == 2:            

            if O0O0O0O0O0O0O_zxco0o0o0o0 <= own_zxco0o0o0o02 - 600:
                print("触发延迟")
                oOO0O0O0O0O0O0_num = 0
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                oOO0O0O0O0O0O0_on = False
            elif O0O0O0O0O0O0O_zxco0o0o0o0 == own_zxco0o0o0o02 - 500 and interval < 0.95:
                oOO0O0O0O0O0O0_num = 0
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                oOO0O0O0O0O0O0_on = False
            else:
                oOO0O0O0O0O0O0_num = 0
                cls.Tijiao()
                oOO0O0O0O0O0O0_on = False
        elif oOO0O0O0O0O0O0_num == 1:
                                 
                               
                                 
                               
                             
            if O0O0O0O0O0O0O_zxco0o0o0o0 <= own_zxco0o0o0o01 - 600:
                               
                timer = threading.Timer(0.5, cls.Tijiao)
                timer.start()
                oOO0O0O0O0O0O0_on = False
                if twice:
                    oOO0O0O0O0O0O0_num = 2
            elif O0O0O0O0O0O0O_zxco0o0o0o0 == own_zxco0o0o0o01 - 500 and interval < 0.95:
                timesleep = (1 - interval) / 3 + 0.25
                timer = threading.Timer(timesleep, cls.Tijiao)
                timer.start()
                oOO0O0O0O0O0O0_on = False
                if twice:
                    oOO0O0O0O0O0O0_num = 2
            else:
                cls.Tijiao()
                oOO0O0O0O0O0O0_on = False
                if twice:
                    oOO0O0O0O0O0O0_num = 2

                   
                           
                       
                                                            
                                                            

    @staticmethod
    def OnClick_Shuaxin():
        Click(Oo0o0Oo0o0o0[3][0], Oo0o0Oo0o0o0[3][1])
        Click(Oo0o0Oo0o0o0[5][0], Oo0o0Oo0o0o0[5][1])
        global sdfsnisdfafzxcv_view, sdfsnisdfafzxcv_close, sdfsnisdfafzxcv_count
        sdfsnisdfafzxcv_view = True         
        sdfsnisdfafzxcv_count = 0      

    @staticmethod
    def OnClick_confirm():
                                               
        Click(Oo0o0Oo0o0o0[4][0], Oo0o0Oo0o0o0[4][1])

    @staticmethod
    def OnClick_oo0o0O0O0O0():
        global web_on, O0O0O0O0O0O0O_zxco0o0o0o0, sdfsnisdfafzxcv_count
        global oOO0O0O0O0O0O0_num, own_zxco0o0o0o01, own_zxco0o0o0o02, one_diff, ooo0O0o0oO0O_diff
        global oOO0O0O0O0O0O0_on, oo0o0O0O0O0_on
        global uioo0o000oo_need, uioo0o000oo_one, oo0o0O0O0O0_interval, sdfsnisdfafzxcv_view

        sdfsnisdfafzxcv_count = 0            
        sdfsnisdfafzxcv_view = True            
        print("到这了")
        oOO0O0O0O0O0O0_on = True          
        uioo0o000oo_need = True           
        if oOO0O0O0O0O0O0_num == 1:
            own_zxco0o0o0o01 = O0O0O0O0O0O0O_zxco0o0o0o0 + one_diff
            setText(str(own_zxco0o0o0o01))
            TopFrame.selfdelete()
            Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])
            Click(Oo0o0Oo0o0o0[5][0], Oo0o0Oo0o0o0[5][1])

            oOO0O0O0O0O0O0_on = True
            oo0o0O0O0O0_on = False
            oo0o0O0O0O0_interval = False        
                                    
                                         
                                             
                                            


        elif oOO0O0O0O0O0O0_num == 2 and twice:
                          
            own_zxco0o0o0o02 = O0O0O0O0O0O0O_zxco0o0o0o0 + ooo0O0o0oO0O_diff
            setText(str(own_zxco0o0o0o02))
            TopFrame.selfdelete()
            Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])
            Click(Oo0o0Oo0o0o0[5][0], Oo0o0Oo0o0o0[5][1])
            oOO0O0O0O0O0O0_on = True
            oo0o0O0O0O0_on = False
            oo0o0O0O0O0_interval = False        
                                    

                                         
             
                                                 
                                

            
    @staticmethod
    def OnH_oo0o0O0O0O0():
        global sdfsnisdfafzxcv_view, sdfsnisdfafzxcv_count
        sdfsnisdfafzxcv_view = True
        sdfsnisdfafzxcv_count = 0
        own_zxco0o0o0o01 = O0O0O0O0O0O0O_zxco0o0o0o0 + one_diff
        setText(str(own_zxco0o0o0o01))
        TopFrame.selfdelete()

        Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])
        Click(Oo0o0Oo0o0o0[5][0], Oo0o0Oo0o0o0[5][1])


    @staticmethod
    def selfdelete():
        Click2(Oo0o0Oo0o0o0[6][0], Oo0o0Oo0o0o0[6][1] - 5)
        Click2(Oo0o0Oo0o0o0[6][0], Oo0o0Oo0o0o0[6][1])
        Click2(Oo0o0Oo0o0o0[6][0], Oo0o0Oo0o0o0[6][1])
        Delete()
        Delete()
        if o0sdofsfo0sodf0so0_on:
            Paste_o0sdofsfo0sodf0so0()      
        else:
            Paste()       


                     
                          
                                                          
               
                           

    @staticmethod
    def selfChujia():
                             
                                                   
                      
                                
                      
        global zxco0o0o0o0_view, zxco0o0o0o0_count, sdfsnisdfafzxcv_count, sdfsnisdfafzxcv_view


        Click(Oo0o0Oo0o0o0[4][0], Oo0o0Oo0o0o0[4][1])
        Click(Oo0o0Oo0o0o0[0][0], Oo0o0Oo0o0o0[0][1])
        Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])
        Click(Oo0o0Oo0o0o0[5][0], Oo0o0Oo0o0o0[5][1])
        zxco0o0o0o0_view = True
        zxco0o0o0o0_count = 0
        sdfsnisdfafzxcv_count = 0
        sdfsnisdfafzxcv_view = True

    @staticmethod
    def selfTijiao():
        OperationFrame.Del_shot()
        Click(Oo0o0Oo0o0o0[2][0], Oo0o0Oo0o0o0[2][1])

    @staticmethod
    def OnClick_Backspace():
        pg.press('backspace')

    def MainControl(self, event):
             
        if not web_on and time_on:             
            self.operationframe.Closetime()

                    
                  
                                                
                     
                      
               
                  
                                                 
                     
                      

                  
                    
                              
               
                             

                               

    @staticmethod
    def oOO0O0O0O0O0O0_ok():
        global oOO0O0O0O0O0O0_OK, uioo0o000oo_need, oOO0O0O0O0O0O0_on, sdfsnisdfafzxcv_close, sdfsnisdfafzxcv_view
        if e_on and oOO0O0O0O0O0O0_on:
            print("oOO0O0O0O0O0O0_ok")
            oOO0O0O0O0O0O0_OK = True
                                   
            sdfsnisdfafzxcv_view = False
            sdfsnisdfafzxcv_close = True

    @staticmethod
    def oOO0O0O0O0O0O0_ok2():
        global oOO0O0O0O0O0O0_OK, uioo0o000oo_need, sdfsnisdfafzxcv_close, sdfsnisdfafzxcv_view
        if enter_on and oOO0O0O0O0O0O0_on:
            oOO0O0O0O0O0O0_OK = True
                                   
        if enter_on:
            sdfsnisdfafzxcv_close = True
            sdfsnisdfafzxcv_view = False
                                            

    @classmethod
    def query(cls):
        global query_interval, query_on
        if not query_interval and not query_on:
                         
            query_on = True
            query_interval = True
            setText(str(1000000))            
            TopFrame.selfdelete()
            Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])

            timer1 = threading.Timer(3, cls.query_sleep3)
            timer1.start()
            timer2 = threading.Timer(5, cls.query_sleep5)
            timer2.start()
        elif query_interval and query_on:
                                                   
            Click(Oo0o0Oo0o0o0[7][0], Oo0o0Oo0o0o0[7][1])
            query_on = False

    @staticmethod
    def query_sleep3():
                       
        global query_interval, query_on
        if query_on:
                                                   
            Click(Oo0o0Oo0o0o0[7][0], Oo0o0Oo0o0o0[7][1])
            query_on = False

    @staticmethod
    def query_sleep5():
                      
        global query_interval
        query_interval = False

              

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
                1: TopFrame.handle_Jiajia, 2: TopFrame.handle_Chujia, 3: TopFrame.handle_Tijiao,
                4: TopFrame.handle_Shuaxin, 5: TopFrame.handle_Confirm,
                6: TopFrame.handle_Yanzhengma, 7: TopFrame.OnClick_Shuaxin, 8: TopFrame.selfTijiao,
                9: (lambda: TopFrame.selfChujia()), 10: TopFrame.OnClick_Backspace, 11: TopFrame.oOO0O0O0O0O0O0_ok,
                12: TopFrame.oOO0O0O0O0O0O0_ok2,
                13: TopFrame.query, 14: TopFrame.OnH_oo0o0O0O0O0}                  
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

                                                                        
           
                 
    def OnOpenAssist(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()

          
    @classmethod
    def OnCloseAssist(cls):
        cls.Close()
                   
                    
                                                                        
               
                                                                  

          

                                                                        
           
    def OnViewPos(self, event):
        wx.CallAfter(pub.sendMessage, "uioo0o000oo")
        self.MovePos(event)
        global view
        if not view:
            view = True
            for i in range(len(Oo0o0Oo0o0o0)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(Oo0o0Oo0o0o0)):
                self.posframe[i].Hide()

          
    def OnSavePos(self, event):
        self.MovePos(event)
        self.Save_log()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)

          
    def MovePos(self, event):
        global Positon
        for i in range(5):
            posx, posy = Oo0o0Oo0o0o0[i]
            self.posframe[i].Move(posx - 10, posy - 5)

                                                                                    

                  
                              
                                                  
                                       
                        
                    
                                                      
                           
               
                          
     
                   
                   
                          
                                                 
     
                   
                    
                          
                                                     
                                               
                                 
     
     
     
                     
                             
                         
                                                 
                                                 
                  
                               
                       
                                                  
     
                   
                             
                                                   
                                               
                                               
     
                  
                              
                                                 
     
                   
                            
                                                        
                                    
                       
                         
                                                
                                                
                                                
                           
                         

             
                                      
                                
                            

                                                                            

    def Save_log(self):
        output = open('pos.log', 'wb')
        pickle.dump(Oo0o0Oo0o0o0, output)
        output.close()

               

                                  
                                    
                                                         
                         
                                  
                   
                               
     
                                      
                                                         
                         
                                  
                   
                               
     
                                      
                                                         
                         
                                  
                                     
                                   
                   
                           
     
                                        
                                                         
                         
                                  
                                    
                                    
                   
                           
     
             
                                      
                                        
                              
                            
                                       
                                         
                              
                             
             
                                      
                                        
                              
                            
                                       
                                         
                              
                             

                                      
           
                                           
                                                                          
                                                  
     
           
                                
                                
                                                                 
                                               
                     
                                                                               
                                      
                                                
                                                 
                                             

                                      
    def Confirmlogin(self, event):
        Keeplogin()

            
          
    def Choose_time1(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global ghjo0o0o0o01, ghjo0o0o0o02
        ghjo0o0o0o01 = self.time_choice1.GetString(self.time_choice1.GetSelection())
        ghjo0o0o0o02 = self.time_choice2.GetString(self.time_choice2.GetSelection())

    def Choose_time2(self, event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection()) + '.' +
                                str(self.time_choice2.GetSelection()) + " 秒")
        global ghjo0o0o0o01, ghjo0o0o0o02
        ghjo0o0o0o01 = self.time_choice1.GetString(self.time_choice1.GetSelection())
        ghjo0o0o0o02 = self.time_choice2.GetString(self.time_choice2.GetSelection())


        
                                       
                                                                                    
                                                   
                                      
                                                                        
                                                                        
 
                                      
             
                                                   
                         
                                                        
                                                      
                                                                        
                                                                
                                      
               
                               
                                 
                                                        
                    
                                                     
                                                 
                       
                        
                            

                             
                  
                                               
                                      
                    
           
                     


         
                                
                                               
                    
                       
                    
                                                   
           
                   
                                                   


                                                                         
                                         
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          

    def Draw(self, dc):          
        global a_time
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global a_time, b_time
                               
        if b_time < 9:
            b_time = b_time + 1
        else:
            b_time = 0
        time_local = time.localtime(a_time)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=Pos_timeframe,
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
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O
        st = "%s:%s:%s" % (11, 29, o0sdofsfo0sodf0so0_ooo0O0o0oO0O)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O

        o0sdofsfo0sodf0so0_s = int(o0sdofsfo0sodf0so0_ooo0O0o0oO0O)       
        st = "%s:%s:%s" % (11, 29, o0sdofsfo0sodf0so0_s)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=Pos_timeframe,
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
                                    
        wx.Frame.__init__(self, None, 18, 'Price', size=Yanzhengmasize, pos=Pos_sdfsnisdfafzxcvframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
                          )
        self.panel = wx.Panel(self, size=Yanzhengmasize)
                                                 
        self.bmp = wx.StaticBitmap(self.panel, -1)
                

    def ShowImage(self, bm):
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
              
                      
                                     

                                    
                                                     
                          
                                                     

                                     
                                          
                                      
                                      
                             
                   
                              
                        
                                                           
                        
                         
                                    
                    
         
         
                           
                                                
        pub.subscribe(self.OnClose2, "close web")        

    def OnClose(self, event):
        global web_on, view_time, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on, ghjo0o0o0o0_repeat
                        
        web_on = False
        view_time = False
        o0sdofsfo0sodf0so0_on = False
        ooweo0o0werwr_on = False
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

    def OnClose2(self):
        global web_on, view_time, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on, ghjo0o0o0o0_repeat
        web_on = False
        view_time = False
        o0sdofsfo0sodf0so0_on = False
        ooweo0o0werwr_on = False
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
        self.zxco0o0o0o0text = wx.StaticText(self.panel, label=u"最低成交价:", pos=(50, 90))
        self.zxco0o0o0o0text.SetFont(font2)
        self.zxco0o0o0o0 = wx.StaticText(self.panel, pos=(190, 90))
        self.zxco0o0o0o0.SetFont(font2)
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

    def o_closeweb(self, event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()

    def Timego(self, event):
        global O0O0O0O0O0O0O_zxco0o0o0o0, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, a_time
        self.zxco0o0o0o0.SetLabel("%s" % O0O0O0O0O0O0O_zxco0o0o0o0)
        if o0sdofsfo0sodf0so0_on:
            self.time.SetLabel("11:29:%s" % int(o0sdofsfo0sodf0so0_ooo0O0o0oO0O))
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


                  
       
class OperationFrame(wx.Frame):
    def __init__(self):               
        wx.Frame.__init__(self, None, 2, title="小鲜肉代拍", pos=(Px + 902, Py), size=(300, 425), \
                          style=wx.FRAME_NO_TASKBAR | wx.CAPTION | wx.CLOSE_BOX)                                           

        self.Bind(wx.EVT_CLOSE, self.OnClose)
              
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

                      
        global one_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
        one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)
              
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)                 
        self.timer1.Start(10)          
              
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_count, self.timer2)   
        self.timer2.Start(100)          

                 
        self.O0O0O0O0O0O0Oframe = Lowestzxco0o0o0o0Frame()
        self.O0O0O0O0O0O0Oframe.Show(False)

                                     
              
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
        self.Bind(wx.EVT_BUTTON, self.Add_ooo0O0o0oO0O, self.button1)
        self.button2 = wx.Button(panel, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_ooo0O0o0oO0O, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)

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

                 
        self.ghjo0o0o0o0_save = wx.Button(panel, label="保存策略", size=(60, 35))
        self.ghjo0o0o0o0_load = wx.Button(panel, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(panel, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.ghjo0o0o0o0_save)
        hbox4.Add(self.ghjo0o0o0o0_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)

                    
        oneshot = wx.StaticBox(panel, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajia_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))                              
        self.jiajia_time.SetRange(40, 55)
        self.jiajia_time.SetValue(48)
        self.jiajia_time.SetIncrement(0.1)

        gridsizer1.Add(self.jiajia_time, pos=(0, 0))
        miao_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_zxco0o0o0o0 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_zxco0o0o0o0.SetRange(300, 1500)
        self.jiajia_zxco0o0o0o0.SetValue(700)
        self.jiajia_zxco0o0o0o0.SetIncrement(100)
        gridsizer1.Add(self.jiajia_zxco0o0o0o0, pos=(0, 3))

                    
        oOO0O0O0O0O0O0_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_oOO0O0O0O0O0O0 = wx.Choice(panel, -1, choices=oOO0O0O0O0O0O0_choices, size=(68, 25))
        self.select_oOO0O0O0O0O0O0.SetSelection(0)
        gridsizer1.Add(self.select_oOO0O0O0O0O0O0, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)

                    
        oOO0O0O0O0O0O0_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(oOO0O0O0O0O0O0_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.oOO0O0O0O0O0O0_time = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.oOO0O0O0O0O0O0_time.SetRange(40.0, 57.0)
        self.oOO0O0O0O0O0O0_time.SetValue(55.0)
        self.oOO0O0O0O0O0O0_time.SetIncrement(0.1)
        gridsizer1.Add(self.oOO0O0O0O0O0O0_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
                    
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)

             
                    
        ooo0O0o0oO0Oshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.ooo0O0o0oO0OshotSizer = wx.StaticBoxSizer(ooo0O0o0oO0Oshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajia_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_time2.SetRange(40, 55)
        self.jiajia_time2.SetValue(48)
        self.jiajia_time2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajia_time2, pos=(0, 0))
        miao_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(panel, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_zxco0o0o0o02 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_zxco0o0o0o02.SetRange(300, 1500)
        self.jiajia_zxco0o0o0o02.SetValue(600)
        self.jiajia_zxco0o0o0o02.SetIncrement(100)
        gridsizer2.Add(self.jiajia_zxco0o0o0o02, pos=(0, 3))
                    
        oOO0O0O0O0O0O0_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_oOO0O0O0O0O0O02 = wx.Choice(panel, -1, choices=oOO0O0O0O0O0O0_choices2, size=(68, 25))
        self.select_oOO0O0O0O0O0O02.SetSelection(0)
        gridsizer2.Add(self.select_oOO0O0O0O0O0O02, pos=(1, 0))
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)

                    
        oOO0O0O0O0O0O0_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(oOO0O0O0O0O0O0_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.oOO0O0O0O0O0O0_time2 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.oOO0O0O0O0O0O0_time2.SetRange(53.0, 57.0)
        self.oOO0O0O0O0O0O0_time2.SetValue(55.0)
        self.oOO0O0O0O0O0O0_time2.SetIncrement(0.1)
        gridsizer2.Add(self.oOO0O0O0O0O0O0_time2, pos=(2, 1))
        miao3_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2), flag=wx.TOP, border=4)
                    
        self.ooo0O0o0oO0OshotSizer.Add(gridsizer2, 0, flag=wx.ALL, border=5)
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
        self.vbox1.Add(self.ooo0O0o0oO0OshotSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox1)

                
        self.ooo0O0o0oO0Osizer_Shown = False            
        self.oneshotsizer_Shown = True            
        self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)            

                                  

                                              

              
        self.Bind(wx.EVT_CHECKBOX, self.Timeview, self.timeview)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice, self.confirm_choice)
        self.Bind(wx.EVT_BUTTON, self.Strategy_save, self.ghjo0o0o0o0_save)
        self.Bind(wx.EVT_BUTTON, self.Strategy_load, self.ghjo0o0o0o0_load)
        self.Bind(wx.EVT_BUTTON, self.Save_info, self.save_info)

        self.Bind(wx.EVT_CHOICE, self.Refresh_panel, self.select_stractagy)
                                                                             
        self.Bind(wx.EVT_TEXT, self.Jiajia_time, self.jiajia_time)
                                                                                
        self.Bind(wx.EVT_TEXT, self.Jiajia_zxco0o0o0o0, self.jiajia_zxco0o0o0o0)
        self.Bind(wx.EVT_CHOICE, self.Select_oOO0O0O0O0O0O0, self.select_oOO0O0O0O0O0O0)
                                                                              
        self.Bind(wx.EVT_TEXT, self.Yanchi_time, self.yanchi_time)
                                                                              
        self.Bind(wx.EVT_TEXT, self.Tijiao_time, self.oOO0O0O0O0O0O0_time)

                                                                               
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2, self.jiajia_time2)
                                                                                  
        self.Bind(wx.EVT_TEXT, self.Jiajia_zxco0o0o0o02, self.jiajia_zxco0o0o0o02)
        self.Bind(wx.EVT_CHOICE, self.Select_oOO0O0O0O0O0O02, self.select_oOO0O0O0O0O0O02)
                                                                                
        self.Bind(wx.EVT_TEXT, self.Yanchi_time2, self.yanchi_time2)
                                                                                
        self.Bind(wx.EVT_TEXT, self.Tijiao_time2, self.oOO0O0O0O0O0O0_time2)
                   
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
                   
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)

                  
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)

        self.sdfsnisdfafzxcvframe = YanzhengmaFrame()

    def OnClose(self, event):
        self.Show(False)

                     
    def Price_view(self, event):
        global zxco0o0o0o0_view, web_on, zxco0o0o0o0_on, view_time, sdfsnisdfafzxcv_view, Pricesize, Yanzhengmasize, sdfsnisdfafzxcv_close
        global sdfsnisdfafzxcv_count, zxco0o0o0o0_count, sdfsnisdfafzxcv_move
        global o0o0oo0oo0o0o000o_sdfsnisdfafzxcv ,sdfsnisdfafzxcv_hash

        if sdfsnisdfafzxcv_move:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(Pos_sdfsnisdfafzxcvframe)          
                    sdfsnisdfafzxcv_move = False        
                except:
                    pass
        if zxco0o0o0o0_view and zxco0o0o0o0_count >= 4:
            try:
                self.Price_close()
            except:
                pass
            self.Screen_shot(Pos_zxco0o0o0o0, Pricesize, "userzxco0o0o0o0.png")
            image = "userzxco0o0o0o0.png"
            self.zxco0o0o0o0frame = PriceFrame(image, Pricesize, Pos_zxco0o0o0o0frame)
            self.zxco0o0o0o0frame.Show(True)
            zxco0o0o0o0_view = False
            zxco0o0o0o0_on = True
                          
                               
        if sdfsnisdfafzxcv_count >= 5 and not sdfsnisdfafzxcv_close:                    
                                  
            find_yan_confirm()
        if sdfsnisdfafzxcv_close:
            try:
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        if sdfsnisdfafzxcv_view:
            sdfsnisdfafzxcv_close = False
            cut_pic(o0o0oo0oo0o0o000o_sdfsnisdfafzxcv, Yanzhengmasize, "sdfsnisdfafzxcv.png")              
                                                                                   
                                                                                         
            image = "sdfsnisdfafzxcv.png"
            global sdfsnisdfafzxcv_img
            sdfsnisdfafzxcv_img = Image.open("sdfsnisdfafzxcv.png")
            yan_hash = imagehash.dhash(sdfsnisdfafzxcv_img)
            if not sdfsnisdfafzxcv_hash:      
                sdfsnisdfafzxcv_hash = yan_hash
            elif yan_hash == sdfsnisdfafzxcv_hash:         
                                  
                pass
            else:
                sdfsnisdfafzxcv_hash = yan_hash
                try:
                    yan = self.FindWindowById(18)
                    yan.ShowImage(image)
                    yan.Show()
                                      
                                          
                except:                 
                    pass
                finally:
                    pass

    def Yan_close(self, event):
                     
        global sdfsnisdfafzxcv_view, sdfsnisdfafzxcv_close
        find_yan_confirm()

    def Price_count(self, event):
                             
        global zxco0o0o0o0_count, sdfsnisdfafzxcv_count
        zxco0o0o0o0_count += 1
        sdfsnisdfafzxcv_count += 1
        file = 'sc_new.png'
        if web_on and ghjo0o0o0o0_on:
            self.O0O0O0O0O0O0Oframe.Show(True)
        if not os.path.exists(file):
            try:
                self.Price_close()
            except:
                pass
                   
        if not ghjo0o0o0o0_on or not web_on:
            self.O0O0O0O0O0O0Oframe.Show(False)

          
    def Screen_shot(self, box, size, name):
        global Pricesize
        region = ImageGrab.grab(box)
        region.resize(size, Image.ANTIALIAS).save(name)

    def Screen_shot_sdfsnisdfafzxcv(self, box, size, name):
        global Pricesize
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)
                                                         

          
    @staticmethod
    def Del_shot():
        try:
            os.remove("sc_new.png")
        except:
            pass
                  

    def Price_close(self):
        try:
            self.zxco0o0o0o0frame.Destroy()
        except:
            pass

             
    def opt(self, event):
        global oOO0O0O0O0O0O0_num, oOO0O0O0O0O0O0_one, oo0o0O0O0O0_on
        global ghjo0o0o0o0_on        
        global twice, oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_one            
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O < OO00000o01 and o0sdofsfo0sodf0so0_on and not twice:        
            twice = False
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        
        elif o0sdofsfo0sodf0so0_ooo0O0o0oO0O < OO00000o01 and o0sdofsfo0sodf0so0_on and twice:        
            twice = True
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        

            
    def Add_time(self, event):
        global a_time, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O += 0.1
        else:
            a_time += 0.1

    def Minus_time(self, event):
        global a_time, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -= 0.1
        else:
            a_time -= 0.1

    def Add_ooo0O0o0oO0O(self, event):
        global a_time, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O += 1
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >= 60:
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O = 0
        else:
            a_time += 1

    def Minus_ooo0O0o0oO0O(self, event):
        global a_time, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, o0sdofsfo0sodf0so0_on, ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -= 1
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <= 0:
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O = 60
        else:
            a_time -= 1

             
    def Timeview(self, event):
        timeSelected = event.GetEventObject()
        global view_time, time_on
        if timeSelected.IsChecked():
            view_time = True
            time_on = True
            if ooweo0o0werwr_on:
                self.timeframe1.Show(True)
            elif o0sdofsfo0sodf0so0_on:
                self.timeframe2.Show(True)
        else:
            view_time = False
            time_on = False
            if ooweo0o0werwr_on:
                self.timeframe1.Show(False)
            elif o0sdofsfo0sodf0so0_on:
                self.timeframe2.Show(False)

    def Opentime(self):
        if o0sdofsfo0sodf0so0_on:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif ooweo0o0werwr_on:
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

    def Confirmchoice(self, event):
        global e_on, enter_on
        con = self.confirm_choice.GetSelection()
        if con == 0:
            e_on = True
            enter_on = False
        elif con == 1:
            e_on = False
            enter_on = True

    def Jiajia_time(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02, one_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02
        tem = self.jiajia_time.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            OO00000o01 = tem
            OO00000o01 = float(OO00000o01)
            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)            
        else:
            self.jiajia_time.SetValue(OO00000o01)

    def Jiajia_zxco0o0o0o0(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_zxco0o0o0o0.GetValue()
        if tem in templist:
            one_diff = int(tem)
        else:
            self.jiajia_zxco0o0o0o0.SetValue(one_diff)

     
    def Select_oOO0O0O0O0O0O0(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        select = self.select_oOO0O0O0O0O0O0.GetString(self.select_oOO0O0O0O0O0O0.GetSelection())
        if select == u"提前100":
            one_advance = 100
        elif select == u"提前200":
            one_advance = 200
        else:
            one_advance = 0

    def Yanchi_time(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            one_delay = float(tem)
        else:
            self.yanchi_time.SetValue(one_delay)

    def Tijiao_time(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02, one_oO0O0O0O0O0O0O0O02
        tem = self.oOO0O0O0O0O0O0_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            OO00000o02 = float(tem)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)            
        else:
            self.oOO0O0O0O0O0O0_time.SetValue(OO00000o02)

          
    def Jiajia_time2(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01
        tem = self.jiajia_time2.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            ooo0O0o0oO0O_time1 = float(tem)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)            
        else:
            self.jiajia_time2.SetValue(ooo0O0o0oO0O_time1)

    def Jiajia_zxco0o0o0o02(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_zxco0o0o0o02.GetValue()
        if tem in templist:
            ooo0O0o0oO0O_diff = int(tem)
        else:
            self.jiajia_zxco0o0o0o02.SetValue(ooo0O0o0oO0O_diff)

    def Select_oOO0O0O0O0O0O02(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2
        select = self.select_oOO0O0O0O0O0O02.GetString(self.select_oOO0O0O0O0O0O02.GetSelection())
        if select == u"提前100":
            ooo0O0o0oO0O_advance = 100
        elif select == u"提前200":
            ooo0O0o0oO0O_advance = 200
        else:
            ooo0O0o0oO0O_advance = 0

    def Yanchi_time2(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2
        templist = ['0.%d' % i for i in range(11)]            
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            ooo0O0o0oO0O_delay = float(tem)
        else:
            self.yanchi_time2.SetValue(ooo0O0o0oO0O_delay)

    def Tijiao_time2(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        tem = self.oOO0O0O0O0O0O0_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            ooo0O0o0oO0O_time2 = float(tem)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)            
        else:
            self.oOO0O0O0O0O0O0_time2.SetValue(ooo0O0o0oO0O_time2)

                      
               
    def Refresh_panel(self, event):
                              
        global ghjo0o0o0o0_on        
        global twice, oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_one            
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice = False
            ghjo0o0o0o0_on = True
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        

        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            ghjo0o0o0o0_on = True
            twice = True
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        
        else:
            self.none_show()
            ghjo0o0o0o0_on = False
            twice = False

    def ss_Shown(self):      
        if not self.ooo0O0o0oO0Osizer_Shown:             
            self.vbox1.Show(self.ooo0O0o0oO0OshotSizer)          
            self.ooo0O0o0oO0Osizer_Shown = True                
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)           
            self.oneshotsizer_Shown = True
        self.ooo0O0o0oO0Osizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))          
        self.Secondshot_reset()
        self.Layout()

    def ss_Hide(self):      
        if self.ooo0O0o0oO0Osizer_Shown:             
            self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)             
                                                              
                          
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.ooo0O0o0oO0Osizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))          
        self.Oneshot_reset()
        self.Layout()

    def none_show(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)
        if self.ooo0O0o0oO0Osizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)

        self.oneshotsizer_Shown = False
        self.ooo0O0o0oO0Osizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()

    def Oneshot_reset(self):
        global OO00000o01, OO00000o02, one_diff, one_delay, one_advance
        self.jiajia_time.SetValue(48.0)
        self.oOO0O0O0O0O0O0_time.SetValue(55.0)
        self.jiajia_zxco0o0o0o0.SetValue(700)
        self.select_oOO0O0O0O0O0O0.SetSelection(0)
        self.yanchi_time.SetValue(0.5)

        OO00000o01 = 48           
        OO00000o02 = 55           
        one_diff = 700           
        one_delay = 0.5         
        one_advance = 100            
                      
        global one_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
        one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

    def Secondshot_reset(self):
        global OO00000o01, OO00000o02, one_diff, one_delay, one_advance
        global ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_advance
        self.jiajia_time.SetValue(40.0)
        self.oOO0O0O0O0O0O0_time.SetValue(48.0)
        self.jiajia_zxco0o0o0o0.SetValue(500)
        self.select_oOO0O0O0O0O0O0.SetSelection(2)
        self.yanchi_time.SetValue(0.0)

        self.jiajia_time2.SetValue(50.0)
        self.oOO0O0O0O0O0O0_time2.SetValue(55.5)
        self.jiajia_zxco0o0o0o02.SetValue(700)
        self.select_oOO0O0O0O0O0O02.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)

        OO00000o01 = 40           
        OO00000o02 = 48           
        one_diff = 500           
        one_delay = 0.5         
        one_advance = 0            

        ooo0O0o0oO0O_time1 = 50            
        ooo0O0o0oO0O_time2 = 55.5           
        ooo0O0o0oO0O_diff = 700           
        ooo0O0o0oO0O_delay = 0.5           
        ooo0O0o0oO0O_advance = 100              
                      
        global one_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
        one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

            
    def Strategy_save(self, event):
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
        global OO00000o01, OO00000o02, one_diff, one_delay, one_advance
        global ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_advance
        global osl, e_on, enter_on          

        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0] = 0
            osl[1] = OO00000o01
            osl[2] = OO00000o02
            osl[3] = one_diff
            osl[4] = one_delay
            osl[5] = one_advance
            osl[6] = ooo0O0o0oO0O_time1
            osl[7] = ooo0O0o0oO0O_time2
            osl[8] = ooo0O0o0oO0O_diff
            osl[9] = ooo0O0o0oO0O_delay
            osl[10] = ooo0O0o0oO0O_advance
            osl[11] = e_on
            osl[12] = enter_on
        elif self.select_stractagy.GetSelection() == 1:
            osl[0] = 1
            osl[0] = 1
            osl[1] = OO00000o01
            osl[2] = OO00000o02
            osl[3] = one_diff
            osl[4] = one_delay
            osl[5] = one_advance
            osl[6] = ooo0O0o0oO0O_time1
            osl[7] = ooo0O0o0oO0O_time2
            osl[8] = ooo0O0o0oO0O_diff
            osl[9] = ooo0O0o0oO0O_delay
            osl[10] = ooo0O0o0oO0O_advance
            osl[11] = e_on
            osl[12] = enter_on
        with open('%s.ghjo0o0o0o0' % name, 'wb') as spk:
            pickle.dump(osl, spk)

         
                        
                                                                          
                                               
                         
                                                     
                                         
                                       
                           

            

    def Strategy_load(self, event):
        import os
        path = os.getcwd()
        choice = self.findfiles(path)
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
        global osl, e_on, enter_on
        global OO00000o01, OO00000o02, one_diff, one_delay, one_advance
        global ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_advance

        global ghjo0o0o0o0_on        
        global twice, oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_one            
        global one_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        try:
            with open(path, 'rb') as loadstr:
                osl = pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:      
            self.ss_Hide()

            twice = False
            ghjo0o0o0o0_on = True
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        

            self.select_stractagy.SetSelection(0)
            self.jiajia_time.SetValue(osl[1])
            self.oOO0O0O0O0O0O0_time.SetValue(osl[2])
            self.jiajia_zxco0o0o0o0.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_oOO0O0O0O0O0O0.SetSelection(0)
            elif osl[5] == 200:
                self.select_oOO0O0O0O0O0O0.SetSelection(1)
            else:
                self.select_oOO0O0O0O0O0O0.SetSelection(2)

            OO00000o01 = osl[1]           
            OO00000o02 = osl[2]           
            one_diff = osl[3]           
            one_delay = osl[4]         
            one_advance = osl[5]            
                  
            e_on = osl[11]
            enter_on = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

        elif osl[0] == 1:      
            ghjo0o0o0o0_on = True
            twice = True
            oo0o0O0O0O0_on = True
            oOO0O0O0O0O0O0_on = False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK = False
            oOO0O0O0O0O0O0_one = False        
            self.ss_Shown()
            self.select_stractagy.SetSelection(1)
            self.jiajia_time.SetValue(osl[1])
            self.oOO0O0O0O0O0O0_time.SetValue(osl[2])
            self.jiajia_zxco0o0o0o0.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_oOO0O0O0O0O0O0.SetSelection(0)
            elif osl[5] == 200:
                self.select_oOO0O0O0O0O0O0.SetSelection(1)
            else:
                self.select_oOO0O0O0O0O0O0.SetSelection(2)
            self.jiajia_time2.SetValue(osl[6])
            self.oOO0O0O0O0O0O0_time2.SetValue(osl[7])
            self.jiajia_zxco0o0o0o02.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_oOO0O0O0O0O0O02.SetSelection(0)
            elif osl[10] == 200:
                self.select_oOO0O0O0O0O0O02.SetSelection(1)
            else:
                self.select_oOO0O0O0O0O0O02.SetSelection(2)

            OO00000o01 = osl[1]           
            OO00000o02 = osl[2]           
            one_diff = osl[3]           
            one_delay = osl[4]         
            one_advance = osl[5]            

            ooo0O0o0oO0O_time1 = osl[6]            
            ooo0O0o0oO0O_time2 = osl[7]           
            ooo0O0o0oO0O_diff = osl[8]           
            ooo0O0o0oO0O_delay = osl[9]           
            ooo0O0o0oO0O_advance = osl[10]              
                  
            e_on = osl[11]
            enter_on = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

    def findfiles(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.ghjo0o0o0o0':
                    L.append(os.path.join(root, file))
        return L

    def Save_info(self, event):
        pass

                                    
          
    def changetime(self, a):          
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time          

          
    def get_nowtime(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a             
                        

    def gettime(self, choice):                          
        tem = self.get_nowtime()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.changetime(b) + float(choice) - int(choice)
        return c                 


                                          
class Lowestzxco0o0o0o0Window(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          

    def Draw(self, dc):          
        global O0O0O0O0O0O0O_zxco0o0o0o0
        st = str(O0O0O0O0O0O0O_zxco0o0o0o0)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global O0O0O0O0O0O0O_zxco0o0o0o0
        st = str(O0O0O0O0O0O0O_zxco0o0o0o0)
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


class Lowestzxco0o0o0o0Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=O0O0O0O0O0O0Ozxco0o0o0o0frame_pos,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
                                                                                    
                                                                      
        Lowestzxco0o0o0o0Window(self)


                                                                
        
                         
                                                          
                                                                     
                                                                 
                                  
                                  
                                  
 
                    


                                                                
                      
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

        self.o0sdofsfo0sodf0so0btn = wx.Button(self.panel, -1, label="模拟", size=(90, 30))
        self.loginbtn = wx.Button(self.panel, -1, label="登录", size=(90, 30))
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.o0sdofsfo0sodf0so0btn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
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
        self.Center()         

        pub.subscribe(self.connect_success, "connect")
                                                                

        self.hashthread = HashThread()

    def connect_success(self):
        self.loginbtn.Enable()
        global login_result, url2, url3          

        if login_result['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)

                     
            if Username == 'helong' or Username == 'yuanjunkai' or Username == 'zs':
                url2 = 'http://moni.51hupai.org/'
            else:
                url2 = login_result['url_dianxin']
            url3 = login_result['url_nodianxin']
                          
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
                                      
        else:
            Username = username               
            Password = password
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
                                            
            event.GetEventObject().Disable()

    def Purchase(self, event):
        print("购买")


class UserValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''

                                                                            
    def __init__(self, flag):
        wx.Validator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

                                                                            
    def Clone(self):
        '''Required Validator method'''
        return UserValidator(self.flag)

                                                                            
    def Validate(self, win):
        return True

                                                                            
    def TransferToWindow(self):
        return True

                                                                            
    def TransferFromWindow(self):
        return True

                                                                            
    def OnChar(self, event):
        pass
                                           
                           
                            
                                
                        
                                                                              
                        
                                                                           
                          
                                                                    
                          
                      


class PassValidator(wx.Validator):
    ''' Validates data as it is entered into the text controls. '''

                                                                            
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)

                                                                            
    def Clone(self):
        '''Required Validator method'''
        return PassValidator()

                                                                            
    def Validate(self, win):
        return True

                                                                            
    def TransferToWindow(self):
        return True

                                                                            
    def TransferFromWindow(self):
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
                                                       
        global a_time, o0sdofsfo0sodf0so0_ooo0O0o0oO0O
        for i in range(1000000):
            a = time.clock()
            time.sleep(0.1)
            b = time.clock()
            a_time += b - a                
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O += b - a
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >= 60:
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O = 0
                            
                             
                         
                            
                        

                                      
                             
                         


                    
                                  
                                                         
                      
                                               
                       
 
                     
                        
 
                
                         
                 
 
                                        
                   

                                         
              
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
                                                       
        Click2(Oo0o0Oo0o0o0[6][0] + 17, Oo0o0Oo0o0o0[6][1])
        for i in range(15):
            Delete()
        if o0sdofsfo0sodf0so0_on:
            Paste_o0sdofsfo0sodf0so0()
                                                        
        else:
            Paste()      
        Click(Oo0o0Oo0o0o0[1][0], Oo0o0Oo0o0o0[1][1])


                        


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
            winreg.SetValueEx(key, '%s'%name, 0, winreg.REG_DWORD, 0x00001f40)                    
                                                                                 
        except:
                    
            print('error in set value!')

                   
                                               
                  
                              


          
                                                                                     
class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        for i in range(1000000):
            global findpos_on
                                            
            if findpos_on:
                try:
                    print("找着呢")
                    findpos()      
                    time.sleep(0.1)          
                except:
                    logging.error("findposthread error")
                    print("findposthread error")


          
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
            global oOO0O0O0O0O0O0_num
            if oOO0O0O0O0O0O0_num == 2:
                try:
                    findconfirm()
                except:
                    print("查找确认出错")

    def pause(self):
        self.__flag.clear()                   

    def resume(self):
        self.__flag.set()                    

    def stop(self):
        self.__flag.set()                        
        self.__running.clear()            


                              
                         
                               
                              
                      
 
                    
                                         
                                                                
                              
                           
                              
                               
                                
                                                  
                                        
                                      
                                       
                                    
                                        
          
class uioo0o000ooThread(Thread):
    def __init__(self, *args, **kwargs):
        super(uioo0o000ooThread, self).__init__(*args, **kwargs)
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
                finduioo0o000oo()
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
                                            
        global Username, login_result
        login_result = ConfirmUser()
        print(login_result)
                                         
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
            Keeplogin()


                                                                        
         
      
class TijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    

                                                                            
    def run(self):
        global oOO0O0O0O0O0O0_delay, final_oOO0O0O0O0O0O0, ghjo0o0o0o0_zxco0o0o0o0, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01, own_zxco0o0o0o02
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        global one_advance, ooo0O0o0oO0O_advance, oOO0O0O0O0O0O0_num, oOO0O0O0O0O0O0_OK, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_one
        for i in range(10000000):
            time.sleep(0.05)              
                                                    
                                         
                  
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK:                       
                                            
                if oOO0O0O0O0O0O0_num == 1 and a_time >= one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one:            
                    oOO0O0O0O0O0O0_on = False
                    TopFrame.SmartTijiao()        
                    oOO0O0O0O0O0O0_on = False
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, a_time, one_oO0O0O0O0O0O0O0O02))
                    oOO0O0O0O0O0O0_one = True
                elif oOO0O0O0O0O0O0_num == 2 and a_time >= ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02:            
                    oOO0O0O0O0O0O0_on = False
                    TopFrame.SmartTijiao()        
                    oOO0O0O0O0O0O0_on = False
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, a_time, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02))
                elif oOO0O0O0O0O0O0_num == 1 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o01 - 300 - one_advance and a_time <= one_oO0O0O0O0O0O0O0O02 - one_delay and not oOO0O0O0O0O0O0_one:        
                    oOO0O0O0O0O0O0_on = False
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01))
                    oOO0O0O0O0O0O0_one = True
                elif oOO0O0O0O0O0O0_num == 2 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o02 - 300 - ooo0O0o0oO0O_advance and a_time <= ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 - ooo0O0o0oO0O_delay:        
                    oOO0O0O0O0O0O0_on = False
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o02))
                  
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on:                       
                                            
                if oOO0O0O0O0O0O0_num == 1 and one_oO0O0O0O0O0O0O0O01 <= a_time <= one_oO0O0O0O0O0O0O0O01 + 0.6:            
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    own_zxco0o0o0o01 = O0O0O0O0O0O0O_zxco0o0o0o0 + one_diff
                    oOO0O0O0O0O0O0_on = True   
                    logging.info("Rone_oo0o0O0O0O0 %s%s" % (ghjo0o0o0o0_on, ooweo0o0werwr_on))
                    logging.info("Rone_oo0o0O0O0O0 %s%s" % (OO00000o01, one_oO0O0O0O0O0O0O0O01))
                elif oOO0O0O0O0O0O0_num == 2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <= a_time:            
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    own_zxco0o0o0o02 = O0O0O0O0O0O0O_zxco0o0o0o0 + ooo0O0o0oO0O_diff
                    oOO0O0O0O0O0O0_on = True
                    logging.info("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s" % (ghjo0o0o0o0_on, ooweo0o0werwr_on))
                    logging.info("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s" % (ooo0O0o0oO0O_time1, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01))


      
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    

                                                                            
    def run(self):
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_on, own_zxco0o0o0o01, own_zxco0o0o0o02, one_diff, ooo0O0o0oO0O_diff
        global oOO0O0O0O0O0O0_num, oOO0O0O0O0O0O0_OK, one_advance, ooo0O0o0oO0O_advance, oOO0O0O0O0O0O0_one
        for i in range(10000000):
            time.sleep(0.05)              

            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK:                     
                                                                   
                                                                    
                                                             
                if oOO0O0O0O0O0O0_num == 1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >= OO00000o02 and not oOO0O0O0O0O0O0_one:            
                    TopFrame.SmartTijiao()        
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, OO00000o02))
                    oOO0O0O0O0O0O0_on = False
                    oOO0O0O0O0O0O0_one = True         
                elif oOO0O0O0O0O0O0_num == 2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >= ooo0O0o0oO0O_time2 and twice:            
                    TopFrame.SmartTijiao()        
                    logging.info("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, ooo0O0o0oO0O_time2))
                    oOO0O0O0O0O0O0_on = False
                elif oOO0O0O0O0O0O0_num == 1 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o01 - 300 - one_advance and not oOO0O0O0O0O0O0_one:        
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01))
                    oOO0O0O0O0O0O0_one = True         
                elif oOO0O0O0O0O0O0_num == 2 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o02 - 300 - ooo0O0o0oO0O_advance and twice:        
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o02))
                  
                                        
                                                    
                                                     
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on:                     
                if oOO0O0O0O0O0O0_num == 1 and OO00000o01 <= o0sdofsfo0sodf0so0_ooo0O0o0oO0O <= OO00000o01 + 0.6:            
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    print("第一次")
                    own_zxco0o0o0o01 = O0O0O0O0O0O0O_zxco0o0o0o0 + one_diff
                    oOO0O0O0O0O0O0_on = True
                    logging.info("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s" % (ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on))
                    logging.info("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s" % (OO00000o01, o0sdofsfo0sodf0so0_ooo0O0o0oO0O))
                elif oOO0O0O0O0O0O0_num == 2 and twice and ooo0O0o0oO0O_time1 < o0sdofsfo0sodf0so0_ooo0O0o0oO0O:
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    print("第二次")
                    own_zxco0o0o0o02 = O0O0O0O0O0O0O_zxco0o0o0o0 + ooo0O0o0oO0O_diff
                    oOO0O0O0O0O0O0_on = True
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s" % (ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s" % (ooo0O0o0oO0O_time1, o0sdofsfo0sodf0so0_ooo0O0o0oO0O))


class Infoframe(wx.Frame):
    def __init__(self, name, user, psd):               
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)


userweb_label = "本地IE"


class Guopaiframe(wx.Dialog):
    def __init__(self, name):               
        wx.Frame.__init__(self, None, -1, name, size=(195, 265), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(195, 270))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

                    
        self.userweb_label = userweb_label
        self.dianxin = wx.Button(self.panel, label="上海电信", pos=(20, 10), size=(140, 60))
        self.nodianxin = wx.Button(self.panel, label="非电信", pos=(20, 80), size=(140, 60))
        self.userweb = wx.Button(self.panel, label=self.userweb_label, pos=(20, 150), size=(140, 60))
        self.dianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.nodianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.userweb.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_BUTTON, self.Dianxin, self.dianxin)
        self.Bind(wx.EVT_BUTTON, self.NoDianxin, self.nodianxin)
        self.Bind(wx.EVT_BUTTON, self.UserWeb, self.userweb)
        self.Center()
        self.ShowModal()

    def Dianxin(self, event):
        wx.CallAfter(pub.sendMessage, "open dianxin")
        self.Destroy()
        event.Skip()

    def NoDianxin(self, event):
        wx.CallAfter(pub.sendMessage, "open nodianxin")
        self.Destroy()
        event.Skip()

    def UserWeb(self, event):
        global userweb_label, ooweo0o0werwr_on
        if userweb_label == '本地IE' and not ooweo0o0werwr_on:
            ooweo0o0werwr_on = True            
            userweb_label = '关闭辅助'
            wx.CallAfter(pub.sendMessage, "open userweb")
        else:
            userweb_label = '本地IE'
            ooweo0o0werwr_on = False            
            TopFrame.Close()
                       
            try:
                yan = self.FindWindowById(18)
                yan.Destroy()
                global sdfsnisdfafzxcv_exist
                print("关闭成功")
                sdfsnisdfafzxcv_exist = False
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
    Create_hash()
    getwebpath()            
    app = SketchApp()
               
    confirmthread = confirmThread()       
                                 
      
    uioo0o000oothread = uioo0o000ooThread()       
                           
    finposthread = findposThread()        
    cutimgthread = cutimgThread()        
    app.MainLoop()

                                            
