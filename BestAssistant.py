                 
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
                    
   
version='1.4'
num=0
                                 
host_ali="121.196.220.94"
                      
   
url1="http://moni.51hupai.org/"
url2="https://paimai.alltobid.com/bid/2017052001/login.htm"
       
mainicon='ico.ico'

                 
view=False        
do=False        
ad_view=False        

zxco0o0o0o0_view=False           
zxco0o0o0o0_on=False          
zxco0o0o0o0_count=0                
web_on=False               
   
view_time=False         
time_on=False              
import time
a_time = time.time()         
b_time=0                     

o0sdofsfo0sodf0so0_minute=29
o0sdofsfo0sodf0so0_ooo0O0o0oO0O=0

oo0o0O0O0O0_time=0              

Username=0                 
Password=0             


o0sdofsfo0sodf0so0_on=False                                    
ooweo0o0werwr_on=False


ghjo0o0o0o01=53                  
ghjo0o0o0o02=0.0                 

                                
                                 


ghjo0o0o0o0_on=True             
ghjo0o0o0o0_repeat=False                
                             

delay=False        
delay_time=0.5        

login_result=False        


findpos_on=True          

zxco0o0o0o0list=[80000+i*100  for i in range(200)]          
IDnumber=0       
account=0       
passwd=0       


                                                      
import pyautogui as pg
          
def Create_hash():
    with open('dick.dl','rb') as dick:
        global dick_hash
        dick_hash=pickle.load(dick)                
    with open('cf.btn','rb') as cf:
        global cf_hash
        cf_hash=pickle.load(cf)                            

    with open("target.tkl",'rb')  as tar:
        global dick_target
        dick_target=pickle.load(tar)            


                                       
       
OO00000o01=48         
OO00000o02=55         
one_oO0O0O0O0O0O0O0O01=1000000000000           
one_oO0O0O0O0O0O0O0O02=1000000000000           
one_diff=700         
one_delay=0.5       
one_advance=100          


ooo0O0o0oO0O_time1=48          
ooo0O0o0oO0O_time2=55         
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01=1000000000000           
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02=1000000000000           
ooo0O0o0oO0O_diff=600         
ooo0O0o0oO0O_delay=0.5         
ooo0O0o0oO0O_advance=100            

osl = [0] * 15                         

oo0o0O0O0O0_on=True                     
oOO0O0O0O0O0O0_on=False                 


O0O0O0O0O0O0O_zxco0o0o0o0=86000       
own_zxco0o0o0o01=0       
own_zxco0o0o0o02=0       
own_zxco0o0o0o0=0      

oOO0O0O0O0O0O0_OK=False         
e_on=True                
enter_on=False                 

twice=False        
oOO0O0O0O0O0O0_num=1                          
oOO0O0O0O0O0O0_one=False           
                                                                
             
websize=[1024,768]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2        
Py2 = Pxy[1] / 2
Px=(Pxy[0]-websize[0])/2
Py=(Pxy[1]-websize[1])/2
       
                                                           
P_relative=[[343, -66], [346, 40], [96, 121], [92, 43], [201, 100],[281, 40],[221,37],[282,118]]              
P_relative2=[[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [525, 5], [586, 86]]
asd0o0o0o0=[[0,0] for i in range(len(P_relative))]
for i in range(len(asd0o0o0o0)):
    asd0o0o0o0[i][0] = Px1 + P_relative[i][0]
    asd0o0o0o0[i][1] = Py2 + P_relative[i][1]
                  
                   
px_ajust,py_ajust=0,0
for i in range(len(P_relative)):
    P_relative[i][0]+=websize[0]/2+px_ajust
    P_relative[i][1]+=websize[1]/2+py_ajust     
        
px_zxco0o0o0o0=770-171
py_zxco0o0o0o0=260
           
px_zxco0o0o0o0frame=220-191
py_zxco0o0o0o0frame=510
         
px_timeframe=400-35
py_timeframe=460     
      
px_yanzhengmaframe=400-215
py_yanzhengmaframe=460


       
px_mini=200
py_mini=40
      
Pricesize=[400,80]
      
Timesize=[200,50]

                                
uioo0o000oo_area=[396-80,11-50,396+80,11+50]
sdfsf24324297_area=[505-80,68-50,505+80,68+50]


                                                                    
                      
       
      
                              
                               
         
                     
                                                                                        
                                                                                   


                                                              
                                                          

          
Px_zxco0o0o0o0=Px+px_zxco0o0o0o0
Py_zxco0o0o0o0=Py+py_zxco0o0o0o0
Pos_zxco0o0o0o0=[Px_zxco0o0o0o0,Py_zxco0o0o0o0,Px_zxco0o0o0o0+px_mini,Py_zxco0o0o0o0+py_mini]              

             
Px_zxco0o0o0o0frame=Px+px_zxco0o0o0o0frame
Py_zxco0o0o0o0frame=Py+py_zxco0o0o0o0frame
Pos_zxco0o0o0o0frame=[Px_zxco0o0o0o0frame,Py_zxco0o0o0o0frame]

           
Px_timeframe=px_timeframe
Py_timeframe=py_timeframe
Pos_timeframe=[Px_timeframe,Py_timeframe]

        
Px_yanzhengmaframe=Px+px_yanzhengmaframe
Py_yanzhengmaframe=Py+py_yanzhengmaframe
Pos_yanzhengmaframe=[Px_yanzhengmaframe,Py_yanzhengmaframe]

                           
         
          
           
                                              
                                
px_O0O0O0O0O0O0Ozxco0o0o0o0=0                          
py_O0O0O0O0O0O0Ozxco0o0o0o0=0            


Px_O0O0O0O0O0O0Ozxco0o0o0o0=Px+px_O0O0O0O0O0O0Ozxco0o0o0o0
Py_O0O0O0O0O0O0Ozxco0o0o0o0=Py+py_O0O0O0O0O0O0Ozxco0o0o0o0
O0O0O0O0O0O0Ozxco0o0o0o0_sizex=41         
O0O0O0O0O0O0Ozxco0o0o0o0_sizey=16

px_relative=49               
py_relative=0
        
px_sdfsf24324297=656
py_sdfsf24324297=475
Px_sdfsf24324297=Px+px_sdfsf24324297
Py_sdfsf24324297=Py+py_sdfsf24324297
sdfsf24324297_sizex=113
sdfsf24324297_sizey=28
sdfsf24324297_on=False        
sdfsf24324297_need=False        
sdfsf24324297_one=False           
       
px_uioo0o000oo=550
py_uioo0o000oo=413
Px_uioo0o000oo=Px+px_uioo0o000oo
Py_uioo0o000oo=Py+py_uioo0o000oo
uioo0o000oo_sizex=108
uioo0o000oo_sizey=21
uioo0o000oo_on=False        
uioo0o000oo_need=False        
uioo0o000oo_one=False           

oo0o0O0O0O0_interval=False      
oOO0O0O0O0O0O0_interval=False      
query_interval=False    
query_on=False          
                                                                 
                          
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
         
                                
      
                                                                
 
                                                                  
                                                                                  
                                                                                          
                                                                          
      
        
         
                                        
         
                    
                    
                                       
          
                    
 
 
                          
      
                                                                       
      
                                    
                            
 
                     
                                                    
 
                      
                          
 
                            
                     
                                                    
                                         
                                                                                                 
                                                       
 
                           
                     
                 
                                                                       
 
                           
                     
                 
                                                                           
 
                      
                                                                            
                                                                            
   
 
                                
         
                                  
 
                                                                                               
 
                                       
 
                                    
         
                                             
                                                                                    
                                                                                                  
                                           
                                           
                            


                                                                                  
                          
import logging
timenow=time.time()
             
time_local = time.localtime(timenow)
                               
myapplog = time.strftime("%Y%m%d%H%M%S",time_local)
print(myapplog)           
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='%s.log'%myapplog,
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
                                                                                 
     
import win32gui,win32api
import cv2
from PIL import ImageGrab
def Click(x, y):        
    a = win32gui.GetCursorPos()
    x=int(x)
    y=int(y)
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
      
def setText(aString):
    aString=aString.encode('utf-8')
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()

     
def findpos():
                            
    sc = ImageGrab.grab().convert('L')
    img=np.asarray(sc)
    global dick_target
    template=dick_target[2]
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
                    
                    
                    
    global px_O0O0O0O0O0O0Ozxco0o0o0o0,py_O0O0O0O0O0O0Ozxco0o0o0o0,px_relative,py_relative,Px_O0O0O0O0O0O0Ozxco0o0o0o0,Py_O0O0O0O0O0O0Ozxco0o0o0o0,Px,Py
    px_O0O0O0O0O0O0Ozxco0o0o0o0 = max_loc[0]+px_relative
    py_O0O0O0O0O0O0Ozxco0o0o0o0 = max_loc[1]+py_relative
    Px_O0O0O0O0O0O0Ozxco0o0o0o0=px_O0O0O0O0O0O0Ozxco0o0o0o0
    Py_O0O0O0O0O0O0Ozxco0o0o0o0=py_O0O0O0O0O0O0Ozxco0o0o0o0
                                          
    global asd0o0o0o0,uioo0o000oo_area,sdfsf24324297_area
    for i in range(len(asd0o0o0o0)):
        asd0o0o0o0[i][0] = Px_O0O0O0O0O0O0Ozxco0o0o0o0 + P_relative2[i][0]
        asd0o0o0o0[i][1] = Py_O0O0O0O0O0O0Ozxco0o0o0o0 + P_relative2[i][1]
    uioo0o000oo_area = [396 - 80+Px_O0O0O0O0O0O0Ozxco0o0o0o0, 11 - 50+Py_O0O0O0O0O0O0Ozxco0o0o0o0, 396 + 80+Px_O0O0O0O0O0O0Ozxco0o0o0o0, 11 + 50+Py_O0O0O0O0O0O0Ozxco0o0o0o0]
    sdfsf24324297_area = [505 - 80+Px_O0O0O0O0O0O0Ozxco0o0o0o0, 68 - 50+Py_O0O0O0O0O0O0Ozxco0o0o0o0, 505 + 80+Px_O0O0O0O0O0O0Ozxco0o0o0o0, 68 + 50+Py_O0O0O0O0O0O0Ozxco0o0o0o0]
         
    global findpos_on
    findpos_on=False

def finduioo0o000oo():
    global dick_target,uioo0o000oo_on,asd0o0o0o0,uioo0o000oo_area,sdfsf24324297_area
    template=dick_target[0]
    sc = ImageGrab.grab(uioo0o000oo_area).convert('L')
    img = np.asarray(sc)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
    if max_val>=0.9:
        uioo0o000oo_on=True


def findsdfsf24324297():
    global dick_target,sdfsf24324297_on,asd0o0o0o0
    template=dick_target[1]
    sc = ImageGrab.grab(sdfsf24324297_area).convert('L')
    img = np.asarray(sc)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val>=0.9:
        sdfsf24324297_on=True


                       
SZ=20
bin_n = 16                 
import numpy as np

      
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
    ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
                                                                                                  
    image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgn=[]
    xy=[]
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
                           
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
        zxco0o0o0o0="".join(list(result))
        return zxco0o0o0o0                 
    except:
        return False



                                                                                  
         
       
                      
                             
                               
                     
                     
                        
                           
                                                                  

                                                                                  
       
import smtplib
             
               
from email.mime.text import MIMEText
import os
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
                                                                                 
     
from threading import Thread
import threading
from wx.lib.pubsub import pub                
                                                                                  

        
                    
import socket, sys ,json
timeout = 10
socket.setdefaulttimeout(timeout)         

def ConfirmUser():
    host = host_ali
                                                   
                                                            
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except socket.gaierror as e:
        logging.error('连接失败 %s' %e)
        logging.error("Address-related error connecting to server: %s" % e)
        return 'net error'
                     
    except socket.error as e:
        logging.error('连接失败 %s' %e)
        logging.error("Connection error: %s" % e)
        return 'net error'
                     

      
    data = ['login',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")          
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)                             

    s.shutdown(1)
    logging.info("Submit Complete")
    print("Submit Complete")
    try:

        login_reply = s.recv(1024)        
        print(login_reply)
        login_reply = str(login_reply, encoding="utf-8")     
        login_reply = json.loads(login_reply)              
        print(login_reply)
        buf=login_reply[0]
        if buf == 'success':                         
            logging.info('登录成功 %s' % buf)
            global url2
            url2=login_reply[1]           
            return 'login success'             
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
                     

            
    data = ['logout',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")          
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)
    s.shutdown(1)
    print("Submit Log Out Complete")
    logging.info("Submit Log Out Complete")


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
                     

            
    data = ['keep',Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")          
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)

    s.shutdown(1)
    print("Submit keep Complete")
    logging.info("Submit keep Complete")

                                                                                  
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
    server=smtplib.SMTP_SSL(mail_host,465)                       
    server.login(mail_user,mail_pass)
    print('login in  successfully')
    server.sendmail(me,to_list,msg.as_string())
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
        wx.Frame.__init__(self, None, -1, name,
                          size=(520, 320))
        self.Bind(wx.EVT_CLOSE, self.OnClose)


              
        a_time=time.time()

             

        self.statusbar = self.CreateStatusBar()
                              
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.statusbar.SetStatusText(u"版本号", 0)

                  
        self.statusbar.SetStatusText(u"%s" % rev, 1)

                  
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        self.statusbar.SetBackgroundColour((240,255,255))
               
        panel = wx.Panel(self, -1)
                                                                     
        panel.SetBackgroundColour((240,255,255))
        self.SetBackgroundColour((240,255,255))

                     
                                                           
                 
                                                                
                                            
                                                                 
                                             
                                                                
                                             
                                                                
                                             
                                                                
                                             
                                                                 
                                             
                                                            
                                             
                                                             
                                              
                                                           
                                              
                                                          
                                              
                                  
                                 

        self.thread=TimeThread()             
        self.keepthread=KeepThread()

         
                                                                       
                                                           
                                                               
                                                                        
                                                                 
                                                                       
                                                                  
                                                                        
                                                                   
         
                                                                      
                                                                  
                                                                       
                                                                    
                         
                                                                           
                                                                    
                                                                                                              

                   
                                                                      
                                                                
                                                                      
                                                                
               
        self.button5 = wx.Button(panel, label='打开模拟', pos=(190, 190))
        self.Bind(wx.EVT_BUTTON, self.Openo0sdofsfo0sodf0so0, self.button5)
               
        self.button6 = wx.Button(panel, label='打开国拍', pos=(280, 190))
        self.Bind(wx.EVT_BUTTON, self.OpenGuopai, self.button6)
                 
        self.button16 = wx.Button(panel, label='修改国拍网址', pos=(370, 190))
        self.Bind(wx.EVT_BUTTON, self.UrlGuopai, self.button16)
        self.urlText = wx.TextCtrl(panel, -1, pos=(370, 230),size=(120,25))
               
        self.button7 = wx.Button(panel, label='显示帮助', pos=(10, 190))
        self.Bind(wx.EVT_BUTTON, self.Help, self.button7)
                
        self.button8 = wx.Button(panel, label='验证码练习', pos=(100, 190))
        self.Bind(wx.EVT_BUTTON, self.Yan_practice, self.button8)
                 
                                                                       
                                                                  
               
                           
                                                                                     
                                                                        
                                                                                                                 
                                                                                              
                                                     
         
                 
                                                   
                                                                                        
                                                                                                      
                                                                                                          
                                                                        
                                           
                                                                        
                                           
                                                                                                  

                  
                          
                                                        
                                        
                                                                            

            
                                                                   
                                                         
                                                                 
            
             
        self.timer1=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)              
        self.timer1.Start(500)         

               
        self.timer2=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)              
        self.timer2.Start(100)         

             
                                    
                                                                         
                                

                
        self.timer3=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Lowest_zxco0o0o0o0, self.timer3)         
        self.timer3.Start(100)
             
        self.timer4=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Find_pos, self.timer4)         
        self.timer4.Start(150)

                
        self.O0O0O0O0O0O0Oframe = Lowestzxco0o0o0o0Frame()
        self.O0O0O0O0O0O0Oframe.Show(False)
                         
                                    
                                                   
                                                               

                 
        self.operationframe = OperationFrame()
        self.operationframe.Show(False)       







                                                                              
               
    def Lowest_zxco0o0o0o0(self, event):   
        global O0O0O0O0O0O0O_zxco0o0o0o0,findpos_on
        if not findpos_on:
            zxco0o0o0o0 = int(TopFrame.Price_read())               
                  
            if zxco0o0o0o0 in  zxco0o0o0o0list:        
                O0O0O0O0O0O0O_zxco0o0o0o0=zxco0o0o0o0
            else:
                findpos_on=True

       
                                       
                                        
                            
                                                               
                    
                                                 
                                                      
                   
                                 
                             

                                      
                  
     
    def Find_pos(self,event):
        global findpos_on
        if findpos_on:
            findpos()




                             
    @staticmethod
    def Confirm():
        global cf_hash,sdfsf24324297_on
        sdfsf24324297_hash=TopFrame.Confirm_hash()        
        if sdfsf24324297_hash == cf_hash[0]:
            sdfsf24324297_on=True
    @staticmethod
    def Refresh():
        uioo0o000oo_hash=TopFrame.Refresh_hash()         
        global cf_hash,uioo0o000oo_on
        if uioo0o000oo_hash == cf_hash[1]:
            uioo0o000oo_on=True

                                                                               
      



                                                            
               
    @staticmethod
    def Price_read():
        O0O0O0O0O0O0Ozxco0o0o0o0=ImageGrab.grab((Px_O0O0O0O0O0O0Ozxco0o0o0o0, Py_O0O0O0O0O0O0Ozxco0o0o0o0,
                                   O0O0O0O0O0O0Ozxco0o0o0o0_sizex+Px_O0O0O0O0O0O0Ozxco0o0o0o0, O0O0O0O0O0O0Ozxco0o0o0o0_sizey+Py_O0O0O0O0O0O0Ozxco0o0o0o0)).convert('L')

                    
                
                                        

        O0O0O0O0O0O0Ozxco0o0o0o0=np.asarray(O0O0O0O0O0O0Ozxco0o0o0o0)
        zxco0o0o0o0=readpic(O0O0O0O0O0O0Ozxco0o0o0o0)
                      
        return zxco0o0o0o0


    @staticmethod
    def Price_hash():
        O0O0O0O0O0O0Ozxco0o0o0o0 = pg.screenshot(region=(Px_O0O0O0O0O0O0Ozxco0o0o0o0, Py_O0O0O0O0O0O0Ozxco0o0o0o0,
                                   O0O0O0O0O0O0Ozxco0o0o0o0_sizex, O0O0O0O0O0O0Ozxco0o0o0o0_sizey))
        global num
        num+=1
                                        
        zxco0o0o0o0_hash = imagehash.dhash(O0O0O0O0O0O0Ozxco0o0o0o0)
                          
                       
        return zxco0o0o0o0_hash

    @staticmethod
    def Confirm_hash():
        sdfsf24324297 = pg.screenshot(region=(Px_sdfsf24324297, Py_sdfsf24324297,
                                   sdfsf24324297_sizex, sdfsf24324297_sizey))
                
                               
        sdfsf24324297_hash = imagehash.dhash(sdfsf24324297)
        return sdfsf24324297_hash

    @staticmethod
    def Refresh_hash():
        uioo0o000oo = pg.screenshot(region=(Px_uioo0o000oo, Py_uioo0o000oo,
                                        uioo0o000oo_sizex, uioo0o000oo_sizey))

        uioo0o000oo_hash = imagehash.dhash(uioo0o000oo)
        return uioo0o000oo_hash

                                                
          
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
        ret = wx.MessageBox('真的要退出第一枪吗?', '确认', wx.OK | wx.CANCEL)
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
            for i in range(len(asd0o0o0o0)):
                self.posframe[i].Show(view)
        else:
            view = False
            for i in range(len(asd0o0o0o0)):
                self.posframe[i].Hide()

          
    def OnSavePos(self, event):
        self.MovePos(event)
        self.Save_log()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)




         
    def MovePos(self,event):
        global Positon
        for i in range(5):
            posx,posy = asd0o0o0o0[i]
            self.posframe[i].Move(posx-10,posy-5)

    def Openo0sdofsfo0sodf0so0(self,event):
            
        global oOO0O0O0O0O0O0_num,oo0o0O0O0O0_on,oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on,oOO0O0O0O0O0O0_OK
        ghjo0o0o0o0_on = True
        twice = True
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px,Py,url1,ad_view,web_on,do,ooweo0o0werwr_on,o0sdofsfo0sodf0so0_on,ghjo0o0o0o0_repeat
        if  ooweo0o0werwr_on:
            wx.MessageBox('请关闭国拍页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif o0sdofsfo0sodf0so0_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:

                                                      
                                                                        
                                                 
            self.Open()
            if do:
                o0sdofsfo0sodf0so0_on = True        
                ad_view=True
                web_on=True
                self.fr=WebFrame(Px,Py,False,'沪牌模拟')
                self.operationframe.Show(True)          
                            
                if time_on:
                    self.operationframe.Opentime()
                if not ghjo0o0o0o0_repeat:                
                    self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                    self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                    ghjo0o0o0o0_repeat = True


                browser=wx.html2.WebView.New(self.fr,size=(websize[0],websize[1]),pos=(0,0))
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                                                         
                                                           
                                                         
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()
             
                          
                               
                                                      
                           
                               
                                                       
                          
                               
                                                      
     
              
                               
                        
                                                                
                                                                                          
                                            
                        
                      
         
               
                       
                       
                                        
                                                     
                                                          
                        
                                
                 
                                   
                                   
                                  
                                  
                                       
                                       
                         
                                            
                                            
                                           
                                           
                        
                                          
                                          
                                         
                                         
                                             
                                             


    def OpenGuopai(self,event):
            
        global oOO0O0O0O0O0O0_num,oo0o0O0O0O0_on,oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on,oOO0O0O0O0O0O0_OK
        ghjo0o0o0o0_on = True
        twice = True
        oo0o0O0O0O0_on = True
        oOO0O0O0O0O0O0_on = False
        oOO0O0O0O0O0O0_num = 1       
        oOO0O0O0O0O0O0_OK = False
        global Px,Py,url2,ad_view,web_on,do,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on,ghjo0o0o0o0_repeat
        if o0sdofsfo0sodf0so0_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif ooweo0o0werwr_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
                                                      
                                                                        
                                                 
            if do:
                ad_view=True
                ooweo0o0werwr_on=True
                self.fr=WebFrame(Px,Py,False,'国拍网')           
                self.operationframe.Show(True)            
                            
                if time_on:
                    self.operationframe.Opentime()
                if not ghjo0o0o0o0_repeat:                
                    self.o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread = MoniTijiaoThread()            
                    self.oOO0O0O0O0O0O0thread = TijiaoThread()            
                    ghjo0o0o0o0_repeat = True

                browser=wx.html2.WebView.New(self.fr,size=(websize[0],websize[1]))
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
             

                                                               
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()           
            self.Listen()

    def UrlGuopai(self,event):
        global url2
        try:
            url2=self.urlText.GetValue()
            wx.MessageBox('修改网址成功', '修改国拍网址', wx.OK )
        except:
            wx.MessageBox('请输入正确网址', '修改国址网址', wx.OK | wx.ICON_ERROR)


    def Help(self, event):
        licence = """%s

 谁帮我写个帮助啊
 啊
 啊
 啊""" %version


        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetName("沪牌第一枪")
        aboutInfo.SetVersion(licence)
                                             
                                                 
                                                 
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)
      
    def Yan_practice(self,event):
        pass
     
    def Time_adjust(self,event):
        pass


                                                                               
            
                           
                           
                           
                            
                            
    @staticmethod
    def OnJiajia():
        po=pg.position()
        asd0o0o0o0[0][0]=po[0]
        asd0o0o0o0[0][1]=po[1]
        print(asd0o0o0o0[0][0], "  ",asd0o0o0o0[0][1])
        findpos()


    @staticmethod
    def OnChujia():
        po=pg.position()
        asd0o0o0o0[1][0]=po[0]
        asd0o0o0o0[1][1]=po[1]
    @staticmethod
    def OnTijiao():
        po=pg.position()
        asd0o0o0o0[2][0]=po[0]
        asd0o0o0o0[2][1]=po[1]
    @staticmethod
    def OnShuaxin():
        po=pg.position()
        asd0o0o0o0[3][0]=po[0]
        asd0o0o0o0[3][1]=po[1]
    @staticmethod
    def OnConfirm():
        po=pg.position()
        asd0o0o0o0[4][0]=po[0]
        asd0o0o0o0[4][1]=po[1]
    @staticmethod
    def OnYanzhengma():
        po=pg.position()
        asd0o0o0o0[5][0]=po[0]
        asd0o0o0o0[5][1]=po[1]

            
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

                               
            
        
            
        
    @classmethod
    def OnClick_Tijiao(cls):
        global web_on,oOO0O0O0O0O0O0_on,one_delay,ooo0O0o0oO0O_delay,oOO0O0O0O0O0O0_num
        global oOO0O0O0O0O0O0_on,oo0o0O0O0O0_on,sdfsf24324297_one,sdfsf24324297_need
        sdfsf24324297_need=True

        if  oOO0O0O0O0O0O0_num == 1:
            timer = threading.Timer(one_delay,cls.Tijiao )
            timer.start()
            oOO0O0O0O0O0O0_on=False
            if twice:
                print("修改为2")
                oOO0O0O0O0O0O0_num = 2
                            
            print("成功提交")
        elif oOO0O0O0O0O0O0_num == 2:
            oOO0O0O0O0O0O0_num = 0
            timer = threading.Timer(ooo0O0o0oO0O_delay, cls.Tijiao)
            timer.start()
            oOO0O0O0O0O0O0_on=False
                            
        else:
            cls.Tijiao()

    @staticmethod
    def Tijiao():
        global oOO0O0O0O0O0O0_on,oOO0O0O0O0O0O0_OK,oOO0O0O0O0O0O0_num
        Click(asd0o0o0o0[2][0],asd0o0o0o0[2][1])
        oOO0O0O0O0O0O0_OK=False              
        global sdfsf24324297_one
        if not sdfsf24324297_one:         
            sdfsf24324297thread=sdfsf24324297Thread()
            sdfsf24324297_one=False
                   
                           
                       
                                                            
                                                            

    @staticmethod
    def OnClick_Shuaxin():
        global web_on
        Click(asd0o0o0o0[3][0],asd0o0o0o0[3][1])
        Click(asd0o0o0o0[5][0],asd0o0o0o0[5][1])

    @staticmethod
    def OnClick_sdfsf24324297():
        print(asd0o0o0o0[4][0],asd0o0o0o0[4][1])
        Click(asd0o0o0o0[4][0], asd0o0o0o0[4][1])

    @staticmethod
    def OnClick_oo0o0O0O0O0():
        global zxco0o0o0o0_view,zxco0o0o0o0_count,web_on,O0O0O0O0O0O0O_zxco0o0o0o0
        global oOO0O0O0O0O0O0_num,own_zxco0o0o0o01,own_zxco0o0o0o02,one_diff,ooo0O0o0oO0O_diff
        global oOO0O0O0O0O0O0_on,oo0o0O0O0O0_on
        global uioo0o000oo_need,uioo0o000oo_one,oo0o0O0O0O0_interval
        print(oo0o0O0O0O0_interval)
        if not oo0o0O0O0O0_interval:
            print(oOO0O0O0O0O0O0_num,twice)
            oo0o0O0O0O0_interval=True
            oOO0O0O0O0O0O0_on=True            
            uioo0o000oo_need=True          
            if oOO0O0O0O0O0O0_num == 1:
                own_zxco0o0o0o01=O0O0O0O0O0O0O_zxco0o0o0o0+one_diff
                setText(str(own_zxco0o0o0o01))
                Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
                Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
                Paste()
                Click(asd0o0o0o0[1][0], asd0o0o0o0[1][1])
                oOO0O0O0O0O0O0_on=True
                oo0o0O0O0O0_on=False
                oo0o0O0O0O0_interval=False       
                print(oo0o0O0O0O0_interval)

                if not uioo0o000oo_one:        
                    uioo0o000oothread = uioo0o000ooThread()
                    uioo0o000oo_one = True
            elif oOO0O0O0O0O0O0_num == 2 and twice:
                print("第二次")
                own_zxco0o0o0o02=O0O0O0O0O0O0O_zxco0o0o0o0+ooo0O0o0oO0O_diff
                setText(str(own_zxco0o0o0o02))
                Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
                Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
                Paste()     
                Click(asd0o0o0o0[1][0], asd0o0o0o0[1][1])
                oOO0O0O0O0O0O0_on=True
                oo0o0O0O0O0_on=False
                oo0o0O0O0O0_interval = False      
                if not uioo0o000oo_one:        
                    uioo0o000oothread = uioo0o000ooThread()
                    uioo0o000oo_one = True

                                                              
                                                              
                                                              
                           
                         


                  
                              
                                                  
                                       
                        
                    
                                                      
                           
               
                          
     
                   
                   
                          
                                                 
     
                   
                    
                          
                                                     
                                               
                                 
     
     
     
                     
                             
                         
                                                 
                                                 
                  
                               
                       
                                                  
     
                   
                             
                                                   
                                               
                                               
     
                  
                              
                                                 
     
                   
                            
                                                        
                                    
                       
                         
                                                
                                                
                                                
                           
                         

    @staticmethod
    def OnClick_Backspace():
        pg.press('backspace')

       
    def Price_view(self,event):
        global zxco0o0o0o0_view,web_on,zxco0o0o0o0_on,view_time
        pass
                                           
                  
                                    
                     
                      
                                
                                
                                               
                                        
                              
                           



    def MainControl(self,event):
        if not web_on and zxco0o0o0o0_on:
            self.Price_close()
        if zxco0o0o0o0_on and not oOO0O0O0O0O0O0_on:
            self.Price_close()
        if not web_on and time_on:            
            self.operationframe.Closetime()
        file='sc_new.png'
        if not os.path.exists(file):
            try:
                self.Price_close()
            except:
                pass
        if web_on:
            self.O0O0O0O0O0O0Oframe.Show(True)
            try:
                self.operationframe.Show(True)
            except:
                pass
        else:
            self.O0O0O0O0O0O0Oframe.Show(False)
            try:
                self.operationframe.Show(False)
            except:
                pass

                 
        if web_on:
            self.Show(False)
        else:
            self.Show(True)


                       
    @staticmethod
    def oOO0O0O0O0O0O0_ok():
        global oOO0O0O0O0O0O0_OK,uioo0o000oo_need,oOO0O0O0O0O0O0_on
        if e_on and oOO0O0O0O0O0O0_on:
            oOO0O0O0O0O0O0_OK=True
            uioo0o000oo_need=False        

    @staticmethod
    def oOO0O0O0O0O0O0_ok2():
        global oOO0O0O0O0O0O0_OK,uioo0o000oo_need
        if enter_on and oOO0O0O0O0O0O0_on:
            oOO0O0O0O0O0O0_OK=True
            uioo0o000oo_need = False          

    @classmethod
    def query(cls):
        global query_interval,query_on
        if not query_interval and not query_on:
            print("执行")
            query_on=True
            query_interval=True
            setText(str(1000000))          
            Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
            Click(asd0o0o0o0[6][0], asd0o0o0o0[6][1])
            Paste()
            Click(asd0o0o0o0[1][0], asd0o0o0o0[1][1])
            timer1 = threading.Timer(3, cls.query_sleep3)
            timer1.start()
            timer2 = threading.Timer(5, cls.query_sleep5)
            timer2.start()
        elif  query_interval and query_on:
            print(asd0o0o0o0[7][0], asd0o0o0o0[7][1])
            Click(asd0o0o0o0[7][0], asd0o0o0o0[7][1])
            query_on = False


    @staticmethod
    def query_sleep3():
        print("触发3+")
        global query_interval,query_on
        if query_on:
            print(asd0o0o0o0[7][0], asd0o0o0o0[7][1])
            Click(asd0o0o0o0[7][0], asd0o0o0o0[7][1])
            query_on = False

    @staticmethod
    def query_sleep5():
        print("触发5")
        global query_interval
        query_interval=False



     
    def Price_close(self):
        try:
            self.zxco0o0o0o0frame.Destroy()
        except:
            pass


       
    def Price_count(self,event):
        global zxco0o0o0o0_count
        zxco0o0o0o0_count+=1



                                                                            
         
    @staticmethod
    def Open():
        global do,web_on
        if not do:
            do=True
                   
                                        
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            user32=ctypes.windll.user32
            HOTKEYS1={1: (VK_CODE['2'],win32con.MOD_ALT),2: (VK_CODE['3'],win32con.MOD_ALT),
                  3: (VK_CODE['4'],win32con.MOD_ALT),4: (VK_CODE['5'],win32con.MOD_ALT),
                  5: (VK_CODE['6'],win32con.MOD_ALT),6: (VK_CODE['7'],win32con.MOD_ALT),
                  }
            HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                        10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                        13: (VK_CODE['q'], 0x4000)}
               
            for id,(vk,modifiers) in HOTKEYS1.items():
                if not user32.RegisterHotKey(None,id,modifiers,vk):
                    print("Unable to register id",id)
                    logging.info("Unable to register id",id)
                    do=False
            for id,(vk,modifiers) in HOTKEYS2.items():
                if not user32.RegisterHotKey(None,id,modifiers,vk):
                    print("Unable to register id",id)
                    logging.info("Unable to register id",id)
                    do=False
                web_on = True

          
    @staticmethod
    def Listen():
        try:
                                                    
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            HOTKEY_ACTIONS = {
                1: TopFrame.handle_Jiajia, 2: TopFrame.handle_Chujia, 3: TopFrame.handle_Tijiao,
                4: TopFrame.handle_Shuaxin, 5: TopFrame.handle_Confirm,
                6: TopFrame.handle_Yanzhengma, 7: TopFrame.OnClick_Shuaxin, 8: TopFrame.OnClick_Tijiao,
                9: TopFrame.OnClick_oo0o0O0O0O0, 10: TopFrame.OnClick_Backspace,11:TopFrame.oOO0O0O0O0O0O0_ok,12:TopFrame.oOO0O0O0O0O0O0_ok2,
                 13:TopFrame.query}
            user32 = ctypes.windll.user32
            msg = wintypes.MSG()
            byref=ctypes.byref
            while user32.GetMessageA(byref(msg),None,0,0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    action_to_take=HOTKEY_ACTIONS.get(msg.wParam)
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
            do=False
            VK_CODE = {'0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, '5': 0x35, '6': 0x36, '7': 0x37,
                       '8': 0x38,
                       '9': 0x39, 'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46, 's': 0x53,
                       'q': 0x51}
            HOTKEYS1={1: (VK_CODE['2'],win32con.MOD_ALT),2: (VK_CODE['3'],win32con.MOD_ALT),
                  3: (VK_CODE['4'],win32con.MOD_ALT),4: (VK_CODE['5'],win32con.MOD_ALT),
                  5: (VK_CODE['6'],win32con.MOD_ALT),6: (VK_CODE['7'],win32con.MOD_ALT),
                  }
            user32=ctypes.windll.user32
            HOTKEYS2 = {7: (VK_CODE['s'], 0x4000), 8: (VK_CODE['f'], 0x4000), 9: (VK_CODE['d'], 0x4000),
                        10: (win32con.VK_SPACE, 0x4000), 11: (VK_CODE['e'], 0x4000), 12: (win32con.VK_RETURN, 0x4000),
                        13: (VK_CODE['q'], 0x4000)}
            for id in HOTKEYS1.keys():
                user32.UnregisterHotKey(None,id)
            for id in HOTKEYS2.keys():
                user32.UnregisterHotKey(None,id)
            logging.info("close assistant success")
        else:
            pass

    def Save_log(self):
        output=open('pos.log','wb')
        pickle.dump(asd0o0o0o0,output)
        output.close()

               

            
    def Screen_shot(self):
        global Pricesize
        box = Pos_zxco0o0o0o0
        region = ImageGrab.grab(box)
        region.resize(Pricesize, Image.ANTIALIAS).save("sc_new.png")

          
    def Del_shot(self):
        try:
            os.remove("sc_new.png")
        finally:
            pass


                              
                                
                                                     
                     
                              
               
                           
 
                                  
                                                     
                     
                              
               
                           
 
                                  
                                                     
                     
                              
                                 
                               
               
                       
 
                                    
                                                     
                     
                              
                                
                                
               
                       
 
         
                                  
                                    
                          
                        
                                   
                                     
                          
                         
         
                                  
                                    
                          
                        
                                   
                                     
                          
                         

                                  
       
                                       
                                                                      
                                              
 
       
                            
                            
                                                             
                                           
                 
                                                                           
                                  
                                            
                                             
                                         



                                  
    def Confirmlogin(self,event):
        Keeplogin()


        
     
    def Choose_time1(self,event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection())+'.'+
        str(self.time_choice2.GetSelection())+ " 秒")
        global ghjo0o0o0o01,ghjo0o0o0o02
        ghjo0o0o0o01=self.time_choice1.GetString(self.time_choice1.GetSelection())
        ghjo0o0o0o02=self.time_choice2.GetString(self.time_choice2.GetSelection())


    def Choose_time2(self,event):
        self.timelabel.SetLabel("已设定截止时间" + self.time_choice1.GetString
        (self.time_choice1.GetSelection())+'.'+
        str(self.time_choice2.GetSelection())+ " 秒")
        global ghjo0o0o0o01,ghjo0o0o0o02
        ghjo0o0o0o01=self.time_choice1.GetString(self.time_choice1.GetSelection())
        ghjo0o0o0o02=self.time_choice2.GetString(self.time_choice2.GetSelection())

        
                                       
                                                                                    
                                                   
                                      
                                                                        
                                                                        
 
                                      
             
                                                   
                         
                                                        
                                                      
                                                                        
                                                                
                                      
               
                               
                                 
                                                        
                    
                                                     
                                                 
                       
                        
                            

                                 
                      
                                                   
                                          
                        
               
                         


         
                                    
                                                   
                        
                           
                        
                                                       
               
                       
                                                       


                                                                             
                                         
class ClockWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
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
        wx.Window.__init__(self, parent,size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          

    def Draw(self, dc):          
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O
        st = "%s:%s:%s" %(11,29,o0sdofsfo0sodf0so0_ooo0O0o0oO0O)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O+=0.1
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O>=60:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O=0
        o0sdofsfo0sodf0so0_s=int(o0sdofsfo0sodf0so0_ooo0O0o0oO0O)       
        st ="%s:%s:%s" %(11,29,o0sdofsfo0sodf0so0_s)
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
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200,50), pos=Pos_timeframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
                                                                                    
                                                                      
        MoniClockWindow(self)



                                                                        
class PosFrame(wx.Frame):
    def __init__(self,pos,pos_name):
        x,y=pos
        wx.Frame.__init__(self, None, -1, 'POS',
                          pos=(x-20,y-10), size=(30, 20), style=wx.FRAME_TOOL_WINDOW )
        panel = wx.Panel(self, -1,size=(30,20))
                     
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        t1 = []
        t1.append(wx.StaticText(panel, -1, pos_name,
                                (0, 0)))
        for i in range(len(t1)):
            t1[i].SetFont(font)

class PriceFrame(wx.Frame):
    def __init__(self,image):

        wx.Frame.__init__(self, None, -1,'Price',size=Pricesize, pos=Pos_zxco0o0o0o0frame,
                          style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        self.panel=wx.Panel(self,size=Pricesize)
                                                
        wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(image))

class YanzhengmaFrame(wx.Frame):
    def __init__(self,image):

        wx.Frame.__init__(self, None, -1,'Price',size=(400,80), pos=Pos_yanzhengmaframe,
                          style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        self.panel=wx.Panel(self,size=(400,80))
                                                
        wx.StaticBitmap(self.panel,-1,wx.BitmapFromImage(image))



class AdFrame(wx.Frame):
    def __init__(self):               
        wx.Frame.__init__(self, None, -1, "广告",
                         pos=(0,250), size=(250, 200),style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        panel = wx.Panel(self, -1,size=(250,200))
                     
        font = wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL)
        t1 = []
        t1.append(wx.StaticText(panel, -1, " 专业代拍软件",
                                (15, 10)))
        t1.append(wx.StaticText(panel, -1, " 专业代拍团队",
                                (15, 60)))
        t1.append(wx.StaticText(panel, -1, "关注微信公众号",
                                (15, 110)))
        t1.append(wx.StaticText(panel, -1, " 沪牌第一枪",
                                (15, 160)))
        for i in range(len(t1)):
            t1[i].SetFont(font)

class WebFrame(wx.Frame):
    def __init__(self,px,py,ad,name):               
        wx.Frame.__init__(self, None, -1, name, size=(websize[0], websize[1]), pos=(px, py))

                                                                                                           
                                                                                        
                                                                                                
        if ad:
            self.adframe=AdFrame()
            self.adframe.Show(True)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ad2=ad
        self.control=ControlFrame(name)
        self.control.Show(True)
                                    
                                                     
                          
                                                     



                                 
                                      
                                  
                                  
                         
               
                          
                    
                                                       
                    
                     
                                
                
     
     
                       
                                            
        pub.subscribe(self.OnClose2, "close web")       
    def OnClose(self,event):
        global web_on,view_time,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on,ghjo0o0o0o0_repeat
        web_on=False
        view_time=False
        o0sdofsfo0sodf0so0_on=False
        ooweo0o0werwr_on=False
        TopFrame.Close()
        file="sc_new.png"
        if  os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()
        event.Skip()

    def OnClose2(self):
        global web_on,view_time,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on,ghjo0o0o0o0_repeat
        web_on=False
        view_time=False
        o0sdofsfo0sodf0so0_on=False
        ooweo0o0werwr_on=False
        TopFrame.Close()
        file="sc_new.png"
        if  os.path.exists(file):
            os.remove(file)
        self.Destroy()
        if self.ad2:
            self.adframe.Destroy()

     
class ControlFrame(wx.Frame):                  
    def __init__(self,name):               
        wx.Frame.__init__(self, None, -1, size=(50, 35), style=wx.NO_BORDER|wx.STAY_ON_TOP|wx.FRAME_NO_TASKBAR, \
                          pos=(Px+websize[0]-50, 0) )
        self.panel=wx.Panel(self,-1,size=(50,35))
        self.button1=wx.Button(self.panel,pos=(0,0),size=(50,25),label="关闭")
        self.Bind(wx.EVT_BUTTON, self.o_closeweb, self.button1)
    def o_closeweb(self,event):
        wx.CallAfter(pub.sendMessage, "close web")
        self.Destroy()
        event.Skip()
                  
      
class OperationFrame(wx.Frame):
    def __init__(self):               
        wx.Frame.__init__(self, None, -1, pos=(1070,100),size=(300, 410),\
                          style=wx.FRAME_NO_TASKBAR|wx.CAPTION)                                           
                      
        global one_oO0O0O0O0O0O0O0O01, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01, one_oO0O0O0O0O0O0O0O02, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
        one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)
              
        panel = wx.Panel(self, -1, size=(300, 380))

        stractagy = wx.StaticBox(panel, -1, u'选择策略:')
        self.stractagySizer = wx.StaticBoxSizer(stractagy, wx.VERTICAL)
        stractagy_label = wx.StaticText(panel, label=u"设定拍牌策略",size=(100,50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(stractagy_label )


              
        stractagy_choices = [u'单枪策略', u'双枪策略',u'手动操作（热键辅助）' ]
        self.select_stractagy = wx.Choice(panel, -1, choices=stractagy_choices,size=(100,50))
        hbox1.Add(self.select_stractagy)
        self.select_stractagy.SetSelection(0)
             
        self.timeview = wx.CheckBox(panel, -1, label=u'显示时间')         
        hbox2=wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.timeview)


        self.button1 = wx.Button(panel, label='+1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Add_ooo0O0o0oO0O, self.button1)
        self.button2 = wx.Button(panel, label='-1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Minus_ooo0O0o0oO0O, self.button2)
        self.button3 = wx.Button(panel, label='+0.1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(panel, label='-0.1s',size=(35,25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)

        hbox2.Add(self.button1)
        hbox2.Add(self.button2)
        hbox2.Add(self.button3)
        hbox2.Add(self.button4)
                
        vb1=wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)
        vb1.Add(hbox2)

               
        sdfsf24324297_choice=["E键","回车"]
        self.sdfsf24324297_choice=wx.Choice(panel,-1,choices=sdfsf24324297_choice)
        self.sdfsf24324297_choice.SetSelection(0)
        self.sdfsf24324297_label=wx.StaticText(panel, label=u"确认提交方式     ")
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.sdfsf24324297_label,flag=wx.TOP,  border=4)
        hbox3.Add(self.sdfsf24324297_choice)
        vb1.Add(hbox3)

                
        self.ghjo0o0o0o0_save=wx.Button(panel,label="保存策略",size=(60,35))
        self.ghjo0o0o0o0_load=wx.Button(panel,label="载入策略",size=(60,35))
        self.save_info=wx.Button(panel,label="用户信息",size=(60,35))
        hbox4= wx.BoxSizer(wx.HORIZONTAL)
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
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP|wx.ALIGN_LEFT,  border=4)
        jiahao_label = wx.StaticText(panel, label=u"加价",style=wx.ALIGN_CENTER,size=(25,25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP,  border=4)
        self.jiajia_zxco0o0o0o0 = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_zxco0o0o0o0.SetRange(300, 1500)
        self.jiajia_zxco0o0o0o0.SetValue(700)
        self.jiajia_zxco0o0o0o0.SetIncrement(100)
        gridsizer1.Add(self.jiajia_zxco0o0o0o0, pos=(0, 3))

                    
        oOO0O0O0O0O0O0_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_oOO0O0O0O0O0O0 = wx.Choice(panel, -1, choices=oOO0O0O0O0O0O0_choices,size=(68, 25))
        self.select_oOO0O0O0O0O0O0.SetSelection(0)
        gridsizer1.Add(self.select_oOO0O0O0O0O0O0, pos=(1, 0))
        yanchi_label = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP,  border=4)
        self.yanchi_time = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP,  border=4)

                    
        oOO0O0O0O0O0O0_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(oOO0O0O0O0O0O0_label, pos=(2, 0), flag=wx.TOP,  border=4)
        self.oOO0O0O0O0O0O0_time = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.oOO0O0O0O0O0O0_time.SetRange(40.0, 57.0)
        self.oOO0O0O0O0O0O0_time.SetValue(55.0)
        self.oOO0O0O0O0O0O0_time.SetIncrement(0.1)
        gridsizer1.Add(self.oOO0O0O0O0O0O0_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label,  pos=(2, 2), flag=wx.TOP,  border=4)
                    
        self.oneshotSizer.Add(gridsizer1, 0,flag=wx.ALL,border=5)

             
                    
        ooo0O0o0oO0Oshot = wx.StaticBox(panel, -1, u'双枪策略:')
        self.ooo0O0o0oO0OshotSizer = wx.StaticBoxSizer(ooo0O0o0oO0Oshot, wx.VERTICAL)
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
        self.jiajia_zxco0o0o0o02 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.jiajia_zxco0o0o0o02.SetRange(300, 1500)
        self.jiajia_zxco0o0o0o02.SetValue(600)
        self.jiajia_zxco0o0o0o02.SetIncrement(100)
        gridsizer2.Add(self.jiajia_zxco0o0o0o02, pos=(0, 3) )
                    
        oOO0O0O0O0O0O0_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_oOO0O0O0O0O0O02 = wx.Choice(panel, -1, choices=oOO0O0O0O0O0O0_choices2,size=(68, 25))
        self.select_oOO0O0O0O0O0O02.SetSelection(0)
        gridsizer2.Add(self.select_oOO0O0O0O0O0O02, pos=(1, 0) )
        yanchi_label2 = wx.StaticText(panel, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1) ,flag=wx.TOP,  border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2,  pos=(1, 3) )
        miao2_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao2_label2,  pos=(1, 4) ,flag=wx.TOP,  border=4)

                    
        oOO0O0O0O0O0O0_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(oOO0O0O0O0O0O0_label2, pos=(2, 0) ,flag=wx.TOP,  border=4)
        self.oOO0O0O0O0O0O0_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.oOO0O0O0O0O0O0_time2.SetRange(53.0, 57.0)
        self.oOO0O0O0O0O0O0_time2.SetValue(55.0)
        self.oOO0O0O0O0O0O0_time2.SetIncrement(0.1)
        gridsizer2.Add(self.oOO0O0O0O0O0O0_time2, pos=(2, 1) )
        miao3_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2) ,flag=wx.TOP,  border=4)
                    
        self.ooo0O0o0oO0OshotSizer.Add(gridsizer2, 0,flag=wx.ALL,border=5)

        self.stractagySizer.Add(vb1, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL )

            
        title=wx.StaticText(panel,-1,label=u"拍牌功能设置")
        line=wx.StaticLine(panel, -1  )
        self.vbox1.Add(title,0,wx.ALL | wx.LEFT, 10)
        self.vbox1.Add(line,flag=wx.EXPAND|wx.BOTTOM,border=10)
        self.vbox1.Add(self.stractagySizer, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.oneshotSizer, 0,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.ooo0O0o0oO0OshotSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox1)

       
        self.ooo0O0o0oO0Osizer_Shown=False          
        self.oneshotsizer_Shown=True          
        self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)          



                          

                                     

     
        self.Bind(wx.EVT_CHECKBOX, self.Timeview,self.timeview)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice,self.sdfsf24324297_choice)
        self.Bind(wx.EVT_BUTTON,self.Strategy_save,self.ghjo0o0o0o0_save)
        self.Bind(wx.EVT_BUTTON,self.Strategy_load,self.ghjo0o0o0o0_load)
        self.Bind(wx.EVT_BUTTON,self.Save_info,self.save_info)

        self.Bind(wx.EVT_CHOICE, self.Refresh_panel,self.select_stractagy)
                                                                             
        self.Bind(wx.EVT_TEXT, self.Jiajia_time,self.jiajia_time)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Jiajia_zxco0o0o0o0,self.jiajia_zxco0o0o0o0)
        self.Bind(wx.EVT_CHOICE, self.Select_oOO0O0O0O0O0O0,self.select_oOO0O0O0O0O0O0)
                                                                              
        self.Bind(wx.EVT_TEXT , self.Yanchi_time,self.yanchi_time)
                                                                              
        self.Bind(wx.EVT_TEXT , self.Tijiao_time,self.oOO0O0O0O0O0O0_time)

                                                                               
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2,self.jiajia_time2)
                                                                                  
        self.Bind(wx.EVT_TEXT , self.Jiajia_zxco0o0o0o02,self.jiajia_zxco0o0o0o02)
        self.Bind(wx.EVT_CHOICE, self.Select_oOO0O0O0O0O0O02,self.select_oOO0O0O0O0O0O02)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Yanchi_time2,self.yanchi_time2)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Tijiao_time2,self.oOO0O0O0O0O0O0_time2)
          
        self.timeframe1=TimeFrame()
        self.timeframe1.Show(False)
          
        self.timeframe2=MoniTimeFrame()
        self.timeframe2.Show(False)

                  
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(3000)
    def opt(self,event):
        global oOO0O0O0O0O0O0_num,oOO0O0O0O0O0O0_one,oo0o0O0O0O0_on
        global ghjo0o0o0o0_on        
        global twice, oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_one            
        if self.select_stractagy.GetSelection == 0:
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O < OO00000o01 and o0sdofsfo0sodf0so0_on:
                print("触发1")
                twice = False
                ghjo0o0o0o0_on = True
                oo0o0O0O0O0_on = True
                oOO0O0O0O0O0O0_on = False
                oOO0O0O0O0O0O0_num = 1       
                oOO0O0O0O0O0O0_OK = False
                oOO0O0O0O0O0O0_one = False        
        elif self.select_stractagy.GetSelection == 1:
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O < OO00000o01 and o0sdofsfo0sodf0so0_on:
                print("触发2")
                ghjo0o0o0o0_on = True
                twice = True
                oo0o0O0O0O0_on = True
                oOO0O0O0O0O0O0_on = False
                oOO0O0O0O0O0O0_num = 1       
                oOO0O0O0O0O0O0_OK = False
                oOO0O0O0O0O0O0_one = False        


       
    def Add_time(self, event):
        global a_time,o0sdofsfo0sodf0so0_ooo0O0o0oO0O,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O+=0.1
        else:
            a_time += 0.1

    def Minus_time(self, event):
        global a_time,o0sdofsfo0sodf0so0_ooo0O0o0oO0O,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O-=0.1
        else:
            a_time -= 0.1

    def Add_ooo0O0o0oO0O(self, event):
        global a_time,o0sdofsfo0sodf0so0_ooo0O0o0oO0O,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O += 1
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O>=60:
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O=0
        else:
            a_time+=1

    def Minus_ooo0O0o0oO0O(self, event):
        global a_time,o0sdofsfo0sodf0so0_ooo0O0o0oO0O,o0sdofsfo0sodf0so0_on,ooweo0o0werwr_on
        if o0sdofsfo0sodf0so0_on:
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -= 1
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O<=0:
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O=60
        else:
            a_time-=1
        
    def Timeview(self,event):
        timeSelected = event.GetEventObject()
        global view_time,time_on
        if timeSelected.IsChecked():
            view_time=True
            time_on=True
            if ooweo0o0werwr_on:
                self.timeframe1.Show(True)
            elif o0sdofsfo0sodf0so0_on:
                self.timeframe2.Show(True)
        else:
            view_time=False
            time_on=False
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

    def Confirmchoice(self,event):
        global e_on,enter_on
        con=self.sdfsf24324297_choice.GetSelection()
        if con == 0:
            e_on=True
            enter_on=False
        elif con==1:
            e_on=False
            enter_on=True



    def Jiajia_time(self,event):
        global one_advance,one_delay,one_diff,OO00000o01,OO00000o02,one_oO0O0O0O0O0O0O0O01,one_oO0O0O0O0O0O0O0O02
        tem=self.jiajia_time.GetValue()
        templist=[40+i*0.1 for i in range(151)]
        if tem in templist:
            OO00000o01=tem
            OO00000o01=float(OO00000o01)
            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)            
        else:
            self.jiajia_time.SetValue(OO00000o01)


    def Jiajia_zxco0o0o0o0(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist=[300+i*100 for i in range(13)]
        tem = self.jiajia_zxco0o0o0o0.GetValue()
        if tem in templist:
            one_diff=int(tem)
        else:
            self.jiajia_zxco0o0o0o0.SetValue(one_diff)

 
    def Select_oOO0O0O0O0O0O0(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        select = self.select_oOO0O0O0O0O0O0.GetString(self.select_oOO0O0O0O0O0O0.GetSelection())
        if select == u"提前100":
            one_advance=100
        elif select == u"提前200":
            one_advance=200
        else:
            one_advance=0

    def Yanchi_time(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist=['0.%d' %i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            one_delay = float(tem)
        else:
            self.yanchi_time.SetValue(one_delay)

    def Tijiao_time(self, event):
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02,one_oO0O0O0O0O0O0O0O02
        tem=self.oOO0O0O0O0O0O0_time.GetValue()
        templist=[40+i*0.1 for i in range(171)]
        if tem in templist:
            OO00000o02=float(tem)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)            
        else:
            self.oOO0O0O0O0O0O0_time.SetValue(OO00000o02)
     
    def Jiajia_time2(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01
        tem=self.jiajia_time2.GetValue()
        templist=[40+i*0.1 for i in range(151)]
        if tem in templist:
            ooo0O0o0oO0O_time1=float(tem)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)            
        else:
            self.jiajia_time2.SetValue(ooo0O0o0oO0O_time1)

    def Jiajia_zxco0o0o0o02(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2
        global one_advance, one_delay, one_diff, OO00000o01, OO00000o02
        templist=[300+i*100 for i in range(13)]
        tem = self.jiajia_zxco0o0o0o02.GetValue()
        if tem in templist:
            ooo0O0o0oO0O_diff=int(tem)
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
        templist=['0.%d' %i for i in range(11)]           
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            ooo0O0o0oO0O_delay = float(tem)
        else:
            self.yanchi_time2.SetValue(ooo0O0o0oO0O_delay)


    def Tijiao_time2(self, event):
        global ooo0O0o0oO0O_advance, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        tem=self.oOO0O0O0O0O0O0_time2.GetValue()
        templist=[53+i*0.1 for i in range(41)]
        if tem in templist:
            ooo0O0o0oO0O_time2=float(tem)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)            
        else:
            self.oOO0O0O0O0O0O0_time2.SetValue(ooo0O0o0oO0O_time2)

                  
          
    def Refresh_panel(self,event):
                             
        global ghjo0o0o0o0_on      
        global twice,oOO0O0O0O0O0O0_num,oo0o0O0O0O0_on,oOO0O0O0O0O0O0_on,oOO0O0O0O0O0O0_OK,oOO0O0O0O0O0O0_one          
        stractagy_selection=self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice=False
            ghjo0o0o0o0_on=True
            oo0o0O0O0O0_on=True
            oOO0O0O0O0O0O0_on=False
            oOO0O0O0O0O0O0_num = 1       
            oOO0O0O0O0O0O0_OK=False
            oOO0O0O0O0O0O0_one=False       

        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            ghjo0o0o0o0_on=True
            twice=True
            oo0o0O0O0O0_on=True
            oOO0O0O0O0O0O0_on=False
            oOO0O0O0O0O0O0_num=1      
            oOO0O0O0O0O0O0_OK=False
            oOO0O0O0O0O0O0_one = False        
        else:
            self.none_show()
            ghjo0o0o0o0_on=False
            twice=False


    def ss_Shown(self):    
        if not self.ooo0O0o0oO0Osizer_Shown:              
            self.vbox1.Show(self.ooo0O0o0oO0OshotSizer)           
            self.ooo0O0o0oO0Osizer_Shown = True                 
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)          
            self.oneshotsizer_Shown=True
        self.ooo0O0o0oO0Osizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 560))          
        self.Secondshot_reset()
        self.Layout()

    def ss_Hide(self):    
        if self.ooo0O0o0oO0Osizer_Shown:             
            self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)              
                                                              
                             
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.ooo0O0o0oO0Osizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 360))          
        self.Oneshot_reset()
        self.Layout()

    def none_show(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.ooo0O0o0oO0OshotSizer)
        if self.ooo0O0o0oO0Osizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)

        self.oneshotsizer_Shown = False
        self.ooo0O0o0oO0Osizer_Shown = False
        self.SetClientSize((280, 240))
        self.Layout()

    def Oneshot_reset(self):
        global OO00000o01,OO00000o02,one_diff,one_delay,one_advance
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
        global OO00000o01,OO00000o02,one_diff,one_delay,one_advance
        global ooo0O0o0oO0O_time1,ooo0O0o0oO0O_time2,ooo0O0o0oO0O_diff,ooo0O0o0oO0O_delay,ooo0O0o0oO0O_advance
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
        one_advance = 100            

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
        global OO00000o01,OO00000o02,one_diff,one_delay,one_advance
        global ooo0O0o0oO0O_time1,ooo0O0o0oO0O_time2,ooo0O0o0oO0O_diff,ooo0O0o0oO0O_delay,ooo0O0o0oO0O_advance
        global osl ,e_on,enter_on       

        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0]=0
            osl[1]=OO00000o01
            osl[2]=OO00000o02
            osl[3]=one_diff
            osl[4]=one_delay
            osl[5]=one_advance
            osl[6]=ooo0O0o0oO0O_time1
            osl[7]=ooo0O0o0oO0O_time2
            osl[8]=ooo0O0o0oO0O_diff
            osl[9]=ooo0O0o0oO0O_delay
            osl[10]=ooo0O0o0oO0O_advance
            osl[11]=e_on
            osl[12]=enter_on
        elif self.select_stractagy.GetSelection() == 1:
            osl[0]=1
            osl[0]=1
            osl[1]=OO00000o01
            osl[2]=OO00000o02
            osl[3]=one_diff
            osl[4]=one_delay
            osl[5]=one_advance
            osl[6]=ooo0O0o0oO0O_time1
            osl[7]=ooo0O0o0oO0O_time2
            osl[8]=ooo0O0o0oO0O_diff
            osl[9]=ooo0O0o0oO0O_delay
            osl[10]=ooo0O0o0oO0O_advance
            osl[11]=e_on
            osl[12]=enter_on
        with open('%s.ghjo0o0o0o0'%name,'wb') as spk:
            pickle.dump(osl,spk)

    
                        
                                                                          
                                               
                         
                                                     
                                         
                                       
                           

               


    def Strategy_load(self,event):
        import os
        path=os.getcwd()
        choice=self.findfiles(path)
        if choice:
            dlg = wx.SingleChoiceDialog(None, u"请选择策略:", u"策略载入",
                                       choices=choice)
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetStringSelection()           
                dlg_tip = wx.MessageDialog(None, "载入成功", u"载入策略", wx.OK | wx.ICON_INFORMATION)
                if dlg_tip.ShowModal() == wx.ID_OK:
                    dlg_tip.Destroy()
                self.load(path)
            print("载入")
            dlg.Destroy()
        else:
            dlg_tip = wx.MessageBox('找不到任何保存的策略', '策略载入', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
                dlg.Destroy()

    def load(self,path):
        global  osl,e_on,enter_on
        global OO00000o01, OO00000o02, one_diff, one_delay, one_advance
        global ooo0O0o0oO0O_time1, ooo0O0o0oO0O_time2, ooo0O0o0oO0O_diff, ooo0O0o0oO0O_delay, ooo0O0o0oO0O_advance

        global ghjo0o0o0o0_on        
        global twice, oOO0O0O0O0O0O0_num, oo0o0O0O0O0_on, oOO0O0O0O0O0O0_on, oOO0O0O0O0O0O0_OK, oOO0O0O0O0O0O0_one            
        global one_oO0O0O0O0O0O0O0O01,one_oO0O0O0O0O0O0O0O02,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        try:
            with open(path,'rb') as loadstr:
                osl=pickle.load(loadstr)
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
                 
            e_on=osl[11]
            enter_on=osl[12]
            if e_on:
                self.sdfsf24324297_choice.SetSelection(0)
            elif enter_on:
                self.sdfsf24324297_choice.SetSelection(1)

            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

        elif osl[0] == 1:      
            ghjo0o0o0o0_on=True
            twice=True
            oo0o0O0O0O0_on=True
            oOO0O0O0O0O0O0_on=False
            oOO0O0O0O0O0O0_num=1      
            oOO0O0O0O0O0O0_OK=False
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
            ooo0O0o0oO0O_delay =osl[9]           
            ooo0O0o0oO0O_advance = osl[10]              
                 
            e_on=osl[11]
            enter_on=osl[12]
            if e_on:
                self.sdfsf24324297_choice.SetSelection(0)
            elif enter_on:
                self.sdfsf24324297_choice.SetSelection(1)

            one_oO0O0O0O0O0O0O0O01 = self.gettime(OO00000o01)
            one_oO0O0O0O0O0O0O0O02 = self.gettime(OO00000o02)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 = self.gettime(ooo0O0o0oO0O_time1)
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 = self.gettime(ooo0O0o0oO0O_time2)

    def findfiles(self,path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.ghjo0o0o0o0':
                    L.append(os.path.join(root, file))
        return L

    def Save_info(self,event):
        pass


                                
      
    def changetime(self, a):          
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time          

          
    def get_nowtime(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a             
                        

    def gettime(self,choice):                          
        tem = self.get_nowtime()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.changetime(b) + float(choice)-int(choice)
        return c                 

                                          
class Lowestzxco0o0o0o0Window(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
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
         wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=(300,300),
                              style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
                                                                                        
                                                                          
         Lowestzxco0o0o0o0Window(self)


                                                               
        
                         
                                                          
                                                                     
                                                                 
                                  
                                  
                                  
 
                    


                                                                
                      
import string
import wx.lib.agw.hyperlink as hyperlink
class LoginFrame(wx.Frame):
    def __init__(self, name, user,psd):               
        wx.Frame.__init__(self, None, -1, name,size=(300, 240), style= wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)


                                                      
                                                                    

                
                                                                  
                                                              
                                                                
                                                                         

                
        self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.welcomelabel = wx.StaticText(self.panel, -1, label="请输入用户名和密码", style=wx.ALIGN_CENTER)
        self.sizer_v1.Add(self.welcomelabel,  flag=wx.ALIGN_CENTER | wx.ALL, border=10)

                                                   
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

        self.o0sdofsfo0sodf0so0btn = wx.Button(self.panel, -1, label="模拟",size=(90,30))
        self.loginbtn = wx.Button(self.panel, -1, label="登录",size=(90,30))
        self.btnSizer=wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.o0sdofsfo0sodf0so0btn,flag=wx.ALIGN_LEFT | wx.ALL, border=3)
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
        self.Center()         

        pub.subscribe(self.connect_success, "connect")
                                                                

        self.hashthread=HashThread()

    def connect_success(self):
        self.loginbtn.Enable()
        global login_result
        if login_result=='login success':
            self.Destroy()
            self.topframe = TopFrame('沪牌第一枪', version)
            self.topframe.Show(True)
                          
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
                                      
        else:
            Username=username                 
            Password=password
            self.loginthread=LoginThread()
            namepsd=[username,password]
            with open('your.name','wb') as userfile:
                pickle.dump(namepsd,userfile)
                                            
            event.GetEventObject().Disable()

    def Purchase(self,event):
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
                                                       
        global a_time
        for i in range(1000000):
            a=time.clock()
            time.sleep(0.1)
            b=time.clock()
            a_time+=b-a               
                            
                             
                         
                            
                        

                                      
                                 
                             


                    
                                  
                                                         
                      
                                               
                       
 
                     
                        
 
                
                         
                 
 
                                        
                   

                                        
             
class HashThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)                            
        self.start()                    
                                                                            
    def run(self):
        """Run Worker Thread."""
                                                       
        Create_hash()
                      
                                 


         
class findposThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        findpos()

         
class sdfsf24324297Thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        global sdfsf24324297_need, sdfsf24324297_on
        global sdfsf24324297_need, sdfsf24324297_on ,sdfsf24324297_one,oo0o0O0O0O0_on
        for i in range(100):
            wx.Sleep(0.1)
                                 
            if sdfsf24324297_need:
                print("开启查找")
                findsdfsf24324297()
                if sdfsf24324297_on:
                    TopFrame.OnClick_sdfsf24324297()
                    sdfsf24324297_need=False
                    sdfsf24324297_on=False
                    sdfsf24324297_one=False
                    oo0o0O0O0O0_on=True
        sdfsf24324297_one = False           
         
class uioo0o000ooThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        global sdfsf24324297_need, sdfsf24324297_on
        global uioo0o000oo_need, uioo0o000oo_on,uioo0o000oo_one
        for i in range(50):
            if uioo0o000oo_need:
                finduioo0o000oo()
                if uioo0o000oo_on:
                    TopFrame.OnClick_Shuaxin()         
                    uioo0o000oo_on = False
                    uioo0o000oo_need = False
                    uioo0o000oo_one=False
        uioo0o000oo_one=False            


                                                                        
      
class LoginThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    
                                                                            
    def run(self):
                                            
        global Username,login_result
        login_result=ConfirmUser()
        print(login_result)
        logging.info("%s"%login_result)
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
        global oOO0O0O0O0O0O0_delay,final_oOO0O0O0O0O0O0,ghjo0o0o0o0_zxco0o0o0o0,O0O0O0O0O0O0O_zxco0o0o0o0,own_zxco0o0o0o01,own_zxco0o0o0o02
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O,ghjo0o0o0o0_on,o0sdofsfo0sodf0so0_on,oOO0O0O0O0O0O0_on,oOO0O0O0O0O0O0_OK,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02
        global one_advance,ooo0O0o0oO0O_advance,oOO0O0O0O0O0O0_num,oOO0O0O0O0O0O0_OK,oo0o0O0O0O0_on,oOO0O0O0O0O0O0_on,oOO0O0O0O0O0O0_one
        for i in range(10000000):
            time.sleep(0.1)             
                                                    
                                         
                 
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on  and oOO0O0O0O0O0O0_OK :                         
                                            
                if oOO0O0O0O0O0O0_num == 1 and a_time>=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one:           
                    oOO0O0O0O0O0O0_on=False
                    TopFrame.OnClick_Tijiao()          
                    oOO0O0O0O0O0O0_on=False
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, a_time, one_oO0O0O0O0O0O0O0O02))
                    oOO0O0O0O0O0O0_one=True
                elif oOO0O0O0O0O0O0_num == 2 and a_time >= ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02:            
                    oOO0O0O0O0O0O0_on = False
                    TopFrame.OnClick_Tijiao()        
                    oOO0O0O0O0O0O0_on = False
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, a_time, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02))
                elif oOO0O0O0O0O0O0_num ==1 and   O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o01-300-one_advance and not oOO0O0O0O0O0O0_one:        
                    oOO0O0O0O0O0O0_on = False
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rone_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01))
                    oOO0O0O0O0O0O0_one = True
                elif oOO0O0O0O0O0O0_num == 2 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o02-300-ooo0O0o0oO0O_advance:        
                    oOO0O0O0O0O0O0_on = False
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on, ooweo0o0werwr_on, oOO0O0O0O0O0O0_OK))
                    logging.info("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o02))
                 
            if  ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on:                       
                                            
                if oOO0O0O0O0O0O0_num == 1 and  one_oO0O0O0O0O0O0O0O01<=a_time<=one_oO0O0O0O0O0O0O0O01+0.2:            
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    own_zxco0o0o0o01=O0O0O0O0O0O0O_zxco0o0o0o0+one_diff
                    oOO0O0O0O0O0O0_on=True    
                    logging.info("Rone_oo0o0O0O0O0 %s%s" %(ghjo0o0o0o0_on,ooweo0o0werwr_on))
                    logging.info("Rone_oo0o0O0O0O0 %s%s" %(OO00000o01,one_oO0O0O0O0O0O0O0O01))
                if oOO0O0O0O0O0O0_num == 2 and twice and   ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01<=a_time:            
                    TopFrame.OnClick_oo0o0O0O0O0()        
                    own_zxco0o0o0o02=O0O0O0O0O0O0O_zxco0o0o0o0+ooo0O0o0oO0O_diff
                    oOO0O0O0O0O0O0_on=True
                    logging.info("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s" % (ghjo0o0o0o0_on, ooweo0o0werwr_on))
                    logging.info("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s" % (ooo0O0o0oO0O_time1, ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01))


     
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    

                                                                            
    def run(self):
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O,ghjo0o0o0o0_on,o0sdofsfo0sodf0so0_on,oOO0O0O0O0O0O0_on,own_zxco0o0o0o01,own_zxco0o0o0o02,one_diff,ooo0O0o0oO0O_diff
        global oOO0O0O0O0O0O0_num, oOO0O0O0O0O0O0_OK,one_advance,ooo0O0o0oO0O_advance,oOO0O0O0O0O0O0_one
        for i in range(10000000):
            time.sleep(0.1)             

            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :                       
                print(oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK)
                print(oOO0O0O0O0O0O0_num,o0sdofsfo0sodf0so0_ooo0O0o0oO0O,OO00000o02,oOO0O0O0O0O0O0_one)
                print(O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01, own_zxco0o0o0o02)
                if oOO0O0O0O0O0O0_num == 1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O>=OO00000o02 and not oOO0O0O0O0O0O0_one:           
                    TopFrame.OnClick_Tijiao()          
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on,ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on,  oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, OO00000o02))
                    oOO0O0O0O0O0O0_on=False
                    oOO0O0O0O0O0O0_one=True       
                elif oOO0O0O0O0O0O0_num == 2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O>= ooo0O0o0oO0O_time2 and twice:            
                    TopFrame.OnClick_Tijiao()        
                    logging.info("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, o0sdofsfo0sodf0so0_ooo0O0o0oO0O, ooo0O0o0oO0O_time2))
                    oOO0O0O0O0O0O0_on = False
                elif oOO0O0O0O0O0O0_num ==1 and   O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o01-300-one_advance and  not oOO0O0O0O0O0O0_one:        
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o01))
                    oOO0O0O0O0O0O0_one = True         
                elif oOO0O0O0O0O0O0_num == 2 and O0O0O0O0O0O0O_zxco0o0o0o0 >= own_zxco0o0o0o02-300-ooo0O0o0oO0O_advance and twice:        
                    oOO0O0O0O0O0O0_on = False                        
                    TopFrame.OnClick_Tijiao()       
                    logging.info("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s" % (oOO0O0O0O0O0O0_on, ghjo0o0o0o0_on, o0sdofsfo0sodf0so0_on, oOO0O0O0O0O0O0_OK))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s" % (oOO0O0O0O0O0O0_num, O0O0O0O0O0O0O_zxco0o0o0o0, own_zxco0o0o0o02))
                 
                                        
                                                    
                                                     
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :                     
                if oOO0O0O0O0O0O0_num == 1 and  OO00000o01<=o0sdofsfo0sodf0so0_ooo0O0o0oO0O<=OO00000o01+0.2:             
                    TopFrame.OnClick_oo0o0O0O0O0()        
                                  
                    own_zxco0o0o0o01=O0O0O0O0O0O0O_zxco0o0o0o0+one_diff
                    oOO0O0O0O0O0O0_on=True
                    logging.info("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s" %(ghjo0o0o0o0_on,o0sdofsfo0sodf0so0_on))
                    logging.info("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s" %(OO00000o01,o0sdofsfo0sodf0so0_ooo0O0o0oO0O))
                elif oOO0O0O0O0O0O0_num == 2 and  twice and  ooo0O0o0oO0O_time1<o0sdofsfo0sodf0so0_ooo0O0o0oO0O:
                    TopFrame.OnClick_oo0o0O0O0O0()        
                                  
                    own_zxco0o0o0o02=O0O0O0O0O0O0O_zxco0o0o0o0+ooo0O0o0oO0O_diff
                    oOO0O0O0O0O0O0_on=True
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s" %(ghjo0o0o0o0_on,o0sdofsfo0sodf0so0_on))
                    logging.info("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s" %(ooo0O0o0oO0O_time1,o0sdofsfo0sodf0so0_ooo0O0o0oO0O))


class Infoframe(wx.Frame):
    def __init__(self, name, user,psd):               
        wx.Frame.__init__(self, None, -1, name,size=(300, 240), style= wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)


class SketchApp(wx.App):
    def OnInit(self):
              
                                                                 
         
                                                                                                 
                                                                                              
                                                                                  
         
                        
                 
                  
        try:
            with open("your.name", 'rb') as name:
                namepsd = pickle.load(name)
                user = namepsd[0]
                psd = namepsd[1]
        except:
            user = '123456'      
            psd = 0
        loginframe = LoginFrame('沪牌第一枪', user, psd)
        loginframe.Show(True)
        return True


if __name__ == '__main__':
    app = SketchApp()

    app.MainLoop()


                                           
