                 
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/3/28 8:59
'''
                    
   
version='1.3'
num=0
                                 
host_ali="121.196.220.94"
                      
   
url1="http://moni.51hupai.org/"
url2="https://paimai.alltobid.com/bid/2017052001/login.htm"
       
mainicon='ico.ico'

                 
view=False        
do=False        
ad_view=False        

price_view=False           
price_on=False          
price_count=0                
web_on=False               
   
view_time=False         
time_on=False              
import time
a_time = time.time()         
b_time=0                     

moni_minute=29
moni_second=0

chujia_time=0              

Username=0                 
Password=0             


moni_on=False                                    
guopai_on=False


strategy1=53                  
strategy2=0.0                 

                                
                                 


strategy_on=True             
strategy_repeat=False                
                             

delay=False        
delay_time=0.5        

login_result=False        


findpos_on=True          

pricelist=[80000+i*100  for i in range(200)]

                                                      
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


                                       
       
one_time1=48         
one_time2=55         
one_real_time1=1000000000000           
one_real_time2=1000000000000           
one_diff=700         
one_delay=0.5       
one_advance=100          


second_time1=48          
second_time2=55         
second_real_time1=1000000000000           
second_real_time2=1000000000000           
second_diff=600         
second_delay=0.5         
second_advance=100            

osl = [0] * 15                         

chujia_on=True                     
tijiao_on=False                 


lowest_price=86000       
own_price1=0       
own_price2=0       
own_price=0      

tijiao_OK=False         
e_on=True                
enter_on=False                 

twice=False        
tijiao_num=1                          
tijiao_one=False           
                                                                
             
websize=[1024,768]         
Pxy = pg.size()       
Px1 = Pxy[0] / 2        
Py2 = Pxy[1] / 2
Px=(Pxy[0]-websize[0])/2
Py=(Pxy[1]-websize[1])/2
       
                                                           
P_relative=[[343, -66], [346, 40], [96, 121], [92, 43], [201, 100],[281, 40],[221,37],[282,118]]              
P_relative2=[[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [525, 5], [586, 86]]
Position=[[0,0] for i in range(len(P_relative))]
for i in range(len(Position)):
    Position[i][0] = Px1 + P_relative[i][0]
    Position[i][1] = Py2 + P_relative[i][1]
                  
                   
px_ajust,py_ajust=0,0
for i in range(len(P_relative)):
    P_relative[i][0]+=websize[0]/2+px_ajust
    P_relative[i][1]+=websize[1]/2+py_ajust     
        
px_price=770-171
py_price=260
           
px_priceframe=220-191
py_priceframe=510
         
px_timeframe=400-35
py_timeframe=460     
      
px_yanzhengmaframe=400-215
py_yanzhengmaframe=460


       
px_mini=200
py_mini=40
      
Pricesize=[400,80]
      
Timesize=[200,50]

                                
refresh_area=[396-80,11-50,396+80,11+50]
confirm_area=[505-80,68-50,505+80,68+50]


                                                                    
                      
       
      
                              
                               
         
                     
                                                                                        
                                                                                   


                                                              
                                                          

          
Px_price=Px+px_price
Py_price=Py+py_price
Pos_price=[Px_price,Py_price,Px_price+px_mini,Py_price+py_mini]              

             
Px_priceframe=Px+px_priceframe
Py_priceframe=Py+py_priceframe
Pos_priceframe=[Px_priceframe,Py_priceframe]

           
Px_timeframe=px_timeframe
Py_timeframe=py_timeframe
Pos_timeframe=[Px_timeframe,Py_timeframe]

        
Px_yanzhengmaframe=Px+px_yanzhengmaframe
Py_yanzhengmaframe=Py+py_yanzhengmaframe
Pos_yanzhengmaframe=[Px_yanzhengmaframe,Py_yanzhengmaframe]

                           
         
          
           
                                              
                                
px_lowestprice=0                          
py_lowestprice=0            


Px_lowestprice=Px+px_lowestprice
Py_lowestprice=Py+py_lowestprice
lowestprice_sizex=41         
lowestprice_sizey=16

px_relative=49               
py_relative=0
        
px_confirm=656
py_confirm=475
Px_confirm=Px+px_confirm
Py_confirm=Py+py_confirm
confirm_sizex=113
confirm_sizey=28
confirm_on=False        
confirm_need=False        
confirm_one=False           
       
px_refresh=550
py_refresh=413
Px_refresh=Px+px_refresh
Py_refresh=Py+py_refresh
refresh_sizex=108
refresh_sizey=21
refresh_on=False        
refresh_need=False        
refresh_one=False           

chujia_interval=False      
tijiao_interval=False      
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
                    
                    
                    
                    
    global px_lowestprice,py_lowestprice,px_relative,py_relative,Px_lowestprice,Py_lowestprice,Px,Py
    px_lowestprice = max_loc[0]+px_relative
    py_lowestprice = max_loc[1]+py_relative
    Px_lowestprice=px_lowestprice
    Py_lowestprice=py_lowestprice
                                          
    global Position,refresh_area,confirm_area
    for i in range(len(Position)):
        Position[i][0] = Px_lowestprice + P_relative2[i][0]
        Position[i][1] = Py_lowestprice + P_relative2[i][1]
    refresh_area = [396 - 80+Px_lowestprice, 11 - 50+Py_lowestprice, 396 + 80+Px_lowestprice, 11 + 50+Py_lowestprice]
    confirm_area = [505 - 80+Px_lowestprice, 68 - 50+Py_lowestprice, 505 + 80+Px_lowestprice, 68 + 50+Py_lowestprice]
         
    global findpos_on
    findpos_on=False

def findrefresh():
    global dick_target,refresh_on,Position,refresh_area,confirm_area
    template=dick_target[0]
    sc = ImageGrab.grab(refresh_area).convert('L')
    img = np.asarray(sc)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    
    if max_val>=0.9:
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
        price="".join(list(result))
        return price                 
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
                     

      
    data = [Username,Password]
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")          
    logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    s.send(data)                             

    s.shutdown(1)
    logging.info("Submit Complete")
    print("Submit Complete")
    try:
        login_reply = s.recv(1024)        
        login_reply = str(login_reply, encoding="utf-8")     
        login_reply = json.loads(login_reply)              
                            
        buf=login_reply[0]
        if buf == 'success':                         
            logging.info('登录成功 %s' % buf)
            global url2
            url2=login_reply[1]           
            return 'login success'             
        elif buf == 'repeat':
            logging.warning('账号错误 %s' % buf)
            return 'repeat'
    except:
        logging.warning('连接失败 ' )
        return False


def Logout():
    host = host_ali
                                                   
                                                            
    port = 8080
    global Username
    Username=Username                   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
                     
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
                     

            
    data = 'logout'+Username
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")           
    s.send(data)      
    s.shutdown(1)
    print("Submit Log Out Complete")
    logging.info("Submit Log Out Complete")


def Keeplogin():
    host = host_ali
                                                   
                                                            
    port = 8080
    global Username
    Username=Username                   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        logging.info("Address-related error connecting to server: %s" % e)
                     
    except socket.error as e:
        print("Connection error: %s" % e)
        logging.info("Connection error: %s" % e)
                     

            
    data = 'keep'+Username
    data=json.dumps(data)
    data = bytes(data, encoding="utf-8")           
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
        self.Bind(wx.EVT_BUTTON, self.Openmoni, self.button5)
               
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
        self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)         
        self.timer3.Start(100)
             
        self.timer4=wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Find_pos, self.timer4)         
        self.timer4.Start(150)

                
        self.lowestframe = LowestpriceFrame()
        self.lowestframe.Show(False)
                         
                                    
                                                   
                                                               

                 
        self.operationframe = OperationFrame()
        self.operationframe.Show(False)       







                                                                              
               
    def Lowest_price(self, event):   
        global lowest_price,findpos_on
        if not findpos_on:
            price = int(TopFrame.Price_read())               
                  
            if price in  pricelist:        
                lowest_price=price
            else:
                findpos_on=True

       
                                       
                                        
                            
                                                               
                    
                                                 
                                                      
                   
                                 
                             

                                      
                  
     
    def Find_pos(self,event):
        global findpos_on
        if findpos_on:
            findpos()




                             
    @staticmethod
    def Confirm():
        global cf_hash,confirm_on
        confirm_hash=TopFrame.Confirm_hash()        
        if confirm_hash == cf_hash[0]:
            confirm_on=True
    @staticmethod
    def Refresh():
        refresh_hash=TopFrame.Refresh_hash()         
        global cf_hash,refresh_on
        if refresh_hash == cf_hash[1]:
            refresh_on=True

                                                                               
      



                                                            
               
    @staticmethod
    def Price_read():
        lowestprice=ImageGrab.grab((Px_lowestprice, Py_lowestprice,
                                   lowestprice_sizex+Px_lowestprice, lowestprice_sizey+Py_lowestprice)).convert('L')

                    
                
                                        

        lowestprice=np.asarray(lowestprice)
        price=readpic(lowestprice)
                      
        return price


    @staticmethod
    def Price_hash():
        lowestprice = pg.screenshot(region=(Px_lowestprice, Py_lowestprice,
                                   lowestprice_sizex, lowestprice_sizey))
        global num
        num+=1
                                        
        price_hash = imagehash.dhash(lowestprice)
                          
                       
        return price_hash

    @staticmethod
    def Confirm_hash():
        confirm = pg.screenshot(region=(Px_confirm, Py_confirm,
                                   confirm_sizex, confirm_sizey))
                
                               
        confirm_hash = imagehash.dhash(confirm)
        return confirm_hash

    @staticmethod
    def Refresh_hash():
        refresh = pg.screenshot(region=(Px_refresh, Py_refresh,
                                        refresh_sizex, refresh_sizey))

        refresh_hash = imagehash.dhash(refresh)
        return refresh_hash

                                                
          
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

          
    def OnSavePos(self, event):
        self.MovePos(event)
        self.Save_log()
        wx.MessageBox('保存成功', '定位保存', wx.OK | wx.ICON_INFORMATION)




         
    def MovePos(self,event):
        global Positon
        for i in range(5):
            posx,posy = Position[i]
            self.posframe[i].Move(posx-10,posy-5)

    def Openmoni(self,event):
            
        global tijiao_num,chujia_on,tijiao_on,strategy_on,tijiao_OK
        strategy_on = True
        twice = True
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1       
        tijiao_OK = False
        global Px,Py,url1,ad_view,web_on,do,guopai_on,moni_on,strategy_repeat
        if  guopai_on:
            wx.MessageBox('请关闭国拍页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif moni_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:

                                                      
                                                                        
                                                 
            self.Open()
            if do:
                moni_on = True        
                ad_view=True
                web_on=True
                self.fr=WebFrame(Px,Py,False,'沪牌模拟')
                self.operationframe.Show(True)          
                            
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:                
                    self.monitijiaothread = MoniTijiaoThread()            
                    self.tijiaothread = TijiaoThread()            
                    strategy_repeat = True


                browser=wx.html2.WebView.New(self.fr,size=(websize[0],websize[1]),pos=(0,0))
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                                                         
                                                           
                                                         
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()
             
                          
                               
                                                      
                           
                               
                                                       
                          
                               
                                                      
     
              
                               
                        
                                                                
                                                                                          
                                            
                        
                      
         
               
                       
                       
                                        
                                                     
                                                          
                        
                                
                 
                                   
                                   
                                  
                                  
                                       
                                       
                         
                                            
                                            
                                           
                                           
                        
                                          
                                          
                                         
                                         
                                             
                                             


    def OpenGuopai(self,event):
            
        global tijiao_num,chujia_on,tijiao_on,strategy_on,tijiao_OK
        strategy_on = True
        twice = True
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1       
        tijiao_OK = False
        global Px,Py,url2,ad_view,web_on,do,moni_on,guopai_on,strategy_repeat
        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
                                                      
                                                                        
                                                 
            if do:
                ad_view=True
                guopai_on=True
                self.fr=WebFrame(Px,Py,False,'国拍网')           
                self.operationframe.Show(True)            
                            
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:                
                    self.monitijiaothread = MoniTijiaoThread()            
                    self.tijiaothread = TijiaoThread()            
                    strategy_repeat = True

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
        Position[0][0]=po[0]
        Position[0][1]=po[1]
        print(Position[0][0], "  ",Position[0][1])
        findpos()


    @staticmethod
    def OnChujia():
        po=pg.position()
        Position[1][0]=po[0]
        Position[1][1]=po[1]
    @staticmethod
    def OnTijiao():
        po=pg.position()
        Position[2][0]=po[0]
        Position[2][1]=po[1]
    @staticmethod
    def OnShuaxin():
        po=pg.position()
        Position[3][0]=po[0]
        Position[3][1]=po[1]
    @staticmethod
    def OnConfirm():
        po=pg.position()
        Position[4][0]=po[0]
        Position[4][1]=po[1]
    @staticmethod
    def OnYanzhengma():
        po=pg.position()
        Position[5][0]=po[0]
        Position[5][1]=po[1]

            
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
        global web_on,tijiao_on,one_delay,second_delay,tijiao_num
        global tijiao_on,chujia_on,confirm_one,confirm_need
        confirm_need=True

        if  tijiao_num == 1:
            timer = threading.Timer(one_delay,cls.Tijiao )
            timer.start()
            tijiao_on=False
            if twice:
                print("修改为2")
                tijiao_num = 2
                            
            print("成功提交")
        elif tijiao_num == 2:
            tijiao_num = 0
            timer = threading.Timer(second_delay, cls.Tijiao)
            timer.start()
            tijiao_on=False
                            
        else:
            cls.Tijiao()

    @staticmethod
    def Tijiao():
        global tijiao_on,tijiao_OK,tijiao_num
        Click(Position[2][0],Position[2][1])
        tijiao_OK=False              
        global confirm_one
        if not confirm_one:         
            confirmthread=confirmThread()
            confirm_one=False
                   
                           
                       
                                                            
                                                            

    @staticmethod
    def OnClick_Shuaxin():
        global web_on
        Click(Position[3][0],Position[3][1])
        Click(Position[5][0],Position[5][1])

    @staticmethod
    def OnClick_confirm():
        print(Position[4][0],Position[4][1])
        Click(Position[4][0], Position[4][1])

    @staticmethod
    def OnClick_chujia():
        global price_view,price_count,web_on,lowest_price
        global tijiao_num,own_price1,own_price2,one_diff,second_diff
        global tijiao_on,chujia_on
        global refresh_need,refresh_one,chujia_interval
        print(chujia_interval)
        if not chujia_interval:
            print(tijiao_num,twice)
            chujia_interval=True
            tijiao_on=True            
            refresh_need=True          
            if tijiao_num == 1:
                own_price1=lowest_price+one_diff
                setText(str(own_price1))
                Click(Position[6][0], Position[6][1])
                Click(Position[6][0], Position[6][1])
                Paste()
                Click(Position[1][0], Position[1][1])
                tijiao_on=True
                chujia_on=False
                chujia_interval=False       
                print(chujia_interval)

                if not refresh_one:        
                    refreshthread = refreshThread()
                    refresh_one = True
            elif tijiao_num == 2 and twice:
                print("第二次")
                own_price2=lowest_price+second_diff
                setText(str(own_price2))
                Click(Position[6][0], Position[6][1])
                Click(Position[6][0], Position[6][1])
                Paste()     
                Click(Position[1][0], Position[1][1])
                tijiao_on=True
                chujia_on=False
                chujia_interval = False      
                if not refresh_one:        
                    refreshthread = refreshThread()
                    refresh_one = True

                                                              
                                                              
                                                              
                           
                         


                  
                              
                                                  
                                       
                        
                    
                                                      
                           
               
                          
     
                   
                   
                          
                                                 
     
                   
                    
                          
                                                     
                                               
                                 
     
     
     
                     
                             
                         
                                                 
                                                 
                  
                               
                       
                                                  
     
                   
                             
                                                   
                                               
                                               
     
                  
                              
                                                 
     
                   
                            
                                                        
                                    
                       
                         
                                                
                                                
                                                
                           
                         

    @staticmethod
    def OnClick_Backspace():
        pg.press('backspace')

       
    def Price_view(self,event):
        global price_view,web_on,price_on,view_time
        pass
                                           
                  
                                    
                     
                      
                                
                                
                                               
                                        
                              
                           



    def MainControl(self,event):
        if not web_on and price_on:
            self.Price_close()
        if price_on and not tijiao_on:
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
            self.lowestframe.Show(True)
            try:
                self.operationframe.Show(True)
            except:
                pass
        else:
            self.lowestframe.Show(False)
            try:
                self.operationframe.Show(False)
            except:
                pass

                 
        if web_on:
            self.Show(False)
        else:
            self.Show(True)


                       
    @staticmethod
    def tijiao_ok():
        global tijiao_OK,refresh_need,tijiao_on
        if e_on and tijiao_on:
            tijiao_OK=True
            refresh_need=False        

    @staticmethod
    def tijiao_ok2():
        global tijiao_OK,refresh_need
        if enter_on and tijiao_on:
            tijiao_OK=True
            refresh_need = False          

    @classmethod
    def query(cls):
        global query_interval,query_on
        if not query_interval and not query_on:
            print("执行")
            query_on=True
            query_interval=True
            setText(str(1000000))          
            Click(Position[6][0], Position[6][1])
            Click(Position[6][0], Position[6][1])
            Paste()
            Click(Position[1][0], Position[1][1])
            timer1 = threading.Timer(3, cls.query_sleep3)
            timer1.start()
            timer2 = threading.Timer(5, cls.query_sleep5)
            timer2.start()
        elif  query_interval and query_on:
            print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False


    @staticmethod
    def query_sleep3():
        print("触发3+")
        global query_interval,query_on
        if query_on:
            print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False

    @staticmethod
    def query_sleep5():
        print("触发5")
        global query_interval
        query_interval=False



     
    def Price_close(self):
        try:
            self.priceframe.Destroy()
        except:
            pass


       
    def Price_count(self,event):
        global price_count
        price_count+=1



                                                                            
         
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
                9: TopFrame.OnClick_chujia, 10: TopFrame.OnClick_Backspace,11:TopFrame.tijiao_ok,12:TopFrame.tijiao_ok2,
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
        pickle.dump(Position,output)
        output.close()

               

            
    def Screen_shot(self):
        global Pricesize
        box = Pos_price
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
        global moni_second
        st = "%s:%s:%s" %(11,29,moni_second)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global moni_second
        moni_second+=0.1
        if moni_second>=60:
            moni_second=0
        moni_s=int(moni_second)       
        st ="%s:%s:%s" %(11,29,moni_s)
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

        wx.Frame.__init__(self, None, -1,'Price',size=Pricesize, pos=Pos_priceframe,
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
                      
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)
              
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
                
        vb1=wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)
        vb1.Add(hbox2)

               
        confirm_choice=["E键","回车"]
        self.confirm_choice=wx.Choice(panel,-1,choices=confirm_choice)
        self.confirm_choice.SetSelection(0)
        self.confirm_label=wx.StaticText(panel, label=u"确认提交方式     ")
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.confirm_label,flag=wx.TOP,  border=4)
        hbox3.Add(self.confirm_choice)
        vb1.Add(hbox3)

                
        self.strategy_save=wx.Button(panel,label="保存策略",size=(60,35))
        self.strategy_load=wx.Button(panel,label="载入策略",size=(60,35))
        hbox4= wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.strategy_save)
        hbox4.Add(self.strategy_load)
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
        self.jiajia_price = wx.SpinCtrlDouble(panel, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))

                    
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

                    
        tijiao_label = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer1.Add(tijiao_label, pos=(2, 0), flag=wx.TOP,  border=4)
        self.tijiao_time = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.tijiao_time.SetRange(40.0, 57.0)
        self.tijiao_time.SetValue(55.0)
        self.tijiao_time.SetIncrement(0.1)
        gridsizer1.Add(self.tijiao_time, pos=(2, 1))
        miao3_label = wx.StaticText(panel, label=u"秒")
        gridsizer1.Add(miao3_label,  pos=(2, 2), flag=wx.TOP,  border=4)
                    
        self.oneshotSizer.Add(gridsizer1, 0,flag=wx.ALL,border=5)

             
                    
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

                    
        tijiao_label2 = wx.StaticText(panel, label=u"强制提交时间")
        gridsizer2.Add(tijiao_label2, pos=(2, 0) ,flag=wx.TOP,  border=4)
        self.tijiao_time2 = wx.SpinCtrlDouble(panel, -1, "",size=(68, 25))
        self.tijiao_time2.SetRange(53.0, 57.0)
        self.tijiao_time2.SetValue(55.0)
        self.tijiao_time2.SetIncrement(0.1)
        gridsizer2.Add(self.tijiao_time2, pos=(2, 1) )
        miao3_label2 = wx.StaticText(panel, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2) ,flag=wx.TOP,  border=4)
                    
        self.secondshotSizer.Add(gridsizer2, 0,flag=wx.ALL,border=5)

        self.stractagySizer.Add(vb1, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL )

            
        title=wx.StaticText(panel,-1,label=u"拍牌功能设置")
        line=wx.StaticLine(panel, -1  )
        self.vbox1.Add(title,0,wx.ALL | wx.LEFT, 10)
        self.vbox1.Add(line,flag=wx.EXPAND|wx.BOTTOM,border=10)
        self.vbox1.Add(self.stractagySizer, 0 ,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.oneshotSizer, 0,wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.secondshotSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox1)

       
        self.secondsizer_Shown=False          
        self.oneshotsizer_Shown=True          
        self.vbox1.Hide(self.secondshotSizer)          



                          

                                     

     
        self.Bind(wx.EVT_CHECKBOX, self.Timeview,self.timeview)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice,self.confirm_choice)
        self.Bind(wx.EVT_BUTTON,self.Strategy_save,self.strategy_save)
        self.Bind(wx.EVT_BUTTON,self.Strategy_load,self.strategy_load)

        self.Bind(wx.EVT_CHOICE, self.Refresh_panel,self.select_stractagy)
                                                                             
        self.Bind(wx.EVT_TEXT, self.Jiajia_time,self.jiajia_time)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Jiajia_price,self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao,self.select_tijiao)
                                                                              
        self.Bind(wx.EVT_TEXT , self.Yanchi_time,self.yanchi_time)
                                                                              
        self.Bind(wx.EVT_TEXT , self.Tijiao_time,self.tijiao_time)

                                                                               
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2,self.jiajia_time2)
                                                                                  
        self.Bind(wx.EVT_TEXT , self.Jiajia_price2,self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao2,self.select_tijiao2)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Yanchi_time2,self.yanchi_time2)
                                                                                
        self.Bind(wx.EVT_TEXT , self.Tijiao_time2,self.tijiao_time2)
          
        self.timeframe1=TimeFrame()
        self.timeframe1.Show(False)
          
        self.timeframe2=MoniTimeFrame()
        self.timeframe2.Show(False)

                  
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(3000)
    def opt(self,event):
        global tijiao_num,tijiao_one,chujia_on
        global strategy_on        
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one            
        if self.select_stractagy.GetSelection == 0:
            if moni_second < one_time1 and moni_on:
                print("触发1")
                twice = False
                strategy_on = True
                chujia_on = True
                tijiao_on = False
                tijiao_num = 1       
                tijiao_OK = False
                tijiao_one = False        
        elif self.select_stractagy.GetSelection == 1:
            if moni_second < one_time1 and moni_on:
                print("触发2")
                strategy_on = True
                twice = True
                chujia_on = True
                tijiao_on = False
                tijiao_num = 1       
                tijiao_OK = False
                tijiao_one = False        


       
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
            one_real_time1 = self.gettime(one_time1)            
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
            one_real_time2 = self.gettime(one_time2)            
        else:
            self.tijiao_time.SetValue(one_time2)
     
    def Jiajia_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2,second_real_time1
        tem=self.jiajia_time2.GetValue()
        templist=[40+i*0.1 for i in range(151)]
        if tem in templist:
            second_time1=float(tem)
            second_real_time1 = self.gettime(second_time1)            
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
        templist=['0.%d' %i for i in range(11)]           
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
            second_real_time2 = self.gettime(second_time2)            
        else:
            self.tijiao_time2.SetValue(second_time2)

                  
          
    def Refresh_panel(self,event):
                             
        global strategy_on      
        global twice,tijiao_num,chujia_on,tijiao_on,tijiao_OK,tijiao_one          
        stractagy_selection=self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice=False
            strategy_on=True
            chujia_on=True
            tijiao_on=False
            tijiao_num = 1       
            tijiao_OK=False
            tijiao_one=False       

        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            strategy_on=True
            twice=True
            chujia_on=True
            tijiao_on=False
            tijiao_num=1      
            tijiao_OK=False
            tijiao_one = False        
        else:
            self.none_show()
            strategy_on=False
            twice=False


    def ss_Shown(self):    
        if not self.secondsizer_Shown:              
            self.vbox1.Show(self.secondshotSizer)           
            self.secondsizer_Shown = True                 
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)          
            self.oneshotsizer_Shown=True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 560))          
        self.Secondshot_reset()
        self.Layout()

    def ss_Hide(self):    
        if self.secondsizer_Shown:             
            self.vbox1.Hide(self.secondshotSizer)              
                                                              
                             
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 360))          
        self.Oneshot_reset()
        self.Layout()

    def none_show(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)

        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 240))
        self.Layout()

    def Oneshot_reset(self):
        global one_time1,one_time2,one_diff,one_delay,one_advance
        self.jiajia_time.SetValue(48.0)
        self.tijiao_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_tijiao.SetSelection(0)
        self.yanchi_time.SetValue(0.5)

        one_time1 = 48           
        one_time2 = 55           
        one_diff = 700           
        one_delay = 0.5         
        one_advance = 100            
                      
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

        one_time1 = 40           
        one_time2 = 48           
        one_diff = 500           
        one_delay = 0.5         
        one_advance = 100            

        second_time1 = 50            
        second_time2 = 55.5           
        second_diff = 700           
        second_delay = 0.5           
        second_advance = 100              
                      
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)

        
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
        global osl ,e_on,enter_on       

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
        global one_time1, one_time2, one_diff, one_delay, one_advance
        global second_time1, second_time2, second_diff, second_delay, second_advance

        global strategy_on        
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one            
        global one_real_time1,one_real_time2,second_real_time1,second_real_time2
        try:
            with open(path,'rb') as loadstr:
                osl=pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:     
            self.ss_Hide()


            twice = False
            strategy_on = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1       
            tijiao_OK = False
            tijiao_one = False        

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

            one_time1 = osl[1]           
            one_time2 = osl[2]           
            one_diff = osl[3]           
            one_delay = osl[4]         
            one_advance = osl[5]            
                 
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

        elif osl[0] == 1:      
            strategy_on=True
            twice=True
            chujia_on=True
            tijiao_on=False
            tijiao_num=1      
            tijiao_OK=False
            tijiao_one = False        
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
            if osl[5] == 100:
                self.select_tijiao2.SetSelection(0)
            elif osl[5] == 200:
                self.select_tijiao2.SetSelection(1)
            else:
                self.select_tijiao2.SetSelection(2)


            one_time1 = osl[1]           
            one_time2 = osl[2]           
            one_diff = osl[3]           
            one_delay = osl[4]         
            one_advance = osl[5]            

            second_time1 = osl[6]            
            second_time2 = osl[7]           
            second_diff = osl[8]           
            second_delay =osl[9]           
            second_advance = osl[10]              
                 
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

                                          
class LowestpriceWindow(wx.Panel):
    def __init__(self, parent):
        wx.Window.__init__(self, parent,size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)         
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)             
        self.timer.Start(100)          

    def Draw(self, dc):          
        global lowest_price
        st = str(lowest_price)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):      
        global lowest_price
        st = str(lowest_price)
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
         wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=(300,300),
                              style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
                                                                                        
                                                                          
         LowestpriceWindow(self)


                                                               
        
                         
                                                          
                                                                     
                                                                 
                                  
                                  
                                  
 
                    


                                                                
                      
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
                                 
            if confirm_need:
                print("开启查找")
                findconfirm()
                if confirm_on:
                    TopFrame.OnClick_confirm()
                    confirm_need=False
                    confirm_on=False
                    confirm_one=False
                    chujia_on=True
        confirm_one = False           
         
class refreshThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()

    def run(self):
        global confirm_need, confirm_on
        global refresh_need, refresh_on,refresh_one
        for i in range(50):
            if refresh_need:
                findrefresh()
                if refresh_on:
                    TopFrame.OnClick_Shuaxin()         
                    refresh_on = False
                    refresh_need = False
                    refresh_one=False
        refresh_one=False            


                                                                        
      
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
        global tijiao_delay,final_tijiao,strategy_price,lowest_price,own_price1,own_price2
        global moni_second,strategy_on,moni_on,tijiao_on,tijiao_OK,second_real_time1,second_real_time2
        global one_advance,second_advance,tijiao_num,tijiao_OK,chujia_on,tijiao_on,tijiao_one
        for i in range(10000000):
            time.sleep(0.1)             
                                                    
                                         
                 
            if tijiao_on and strategy_on and guopai_on  and tijiao_OK :                         
                                            
                if tijiao_num == 1 and a_time>=one_real_time2 and not tijiao_one:           
                    tijiao_on=False
                    TopFrame.OnClick_Tijiao()          
                    tijiao_on=False
                    logging.info("Rone_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rone_tijiao %s%s%s" % (tijiao_num, a_time, one_real_time2))
                    tijiao_one=True
                elif tijiao_num == 2 and a_time >= second_real_time2:            
                    tijiao_on = False
                    TopFrame.OnClick_Tijiao()        
                    tijiao_on = False
                    logging.info("Rsecond_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rsecond_tijiao %s%s%s" % (tijiao_num, a_time, second_real_time2))
                elif tijiao_num ==1 and   lowest_price >= own_price1-300-one_advance and not tijiao_one:        
                    tijiao_on = False
                    tijiao_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rone_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rone_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price1))
                    tijiao_one = True
                elif tijiao_num == 2 and lowest_price >= own_price2-300-second_advance:        
                    tijiao_on = False
                    tijiao_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("Rsecond_tijiao %s%s%s%s" % (tijiao_on,strategy_on, guopai_on, tijiao_OK))
                    logging.info("Rsecond_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price2))
                 
            if  strategy_on and guopai_on and chujia_on:                       
                                            
                if tijiao_num == 1 and  one_real_time1<=a_time<=one_real_time1+0.2:            
                    TopFrame.OnClick_chujia()        
                    own_price1=lowest_price+one_diff
                    tijiao_on=True    
                    logging.info("Rone_chujia %s%s" %(strategy_on,guopai_on))
                    logging.info("Rone_chujia %s%s" %(one_time1,one_real_time1))
                if tijiao_num == 2 and twice and   second_real_time1<=a_time:            
                    TopFrame.OnClick_chujia()        
                    own_price2=lowest_price+second_diff
                    tijiao_on=True
                    logging.info("Rsecond_chujia %s%s" % (strategy_on, guopai_on))
                    logging.info("Rsecond_chujia %s%s" % (second_time1, second_real_time1))


     
class MoniTijiaoThread(Thread):
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self.start()                    

                                                                            
    def run(self):
        global moni_second,strategy_on,moni_on,tijiao_on,own_price1,own_price2,one_diff,second_diff
        global tijiao_num, tijiao_OK,one_advance,second_advance,tijiao_one
        for i in range(10000000):
            time.sleep(0.1)             

            if tijiao_on and strategy_on and moni_on and tijiao_OK :                       
                print(tijiao_on, strategy_on, moni_on, tijiao_OK)
                print(tijiao_num,moni_second,one_time2,tijiao_one)
                print(lowest_price, own_price1, own_price2)
                if tijiao_num == 1 and moni_second>=one_time2 and not tijiao_one:           
                    TopFrame.OnClick_Tijiao()          
                    logging.info("moni one_tijiao %s %s %s %s" % (tijiao_on,strategy_on, moni_on,  tijiao_OK))
                    logging.info("moni one_tijiao %s %s %s" % (tijiao_num, moni_second, one_time2))
                    tijiao_on=False
                    tijiao_one=True       
                elif tijiao_num == 2 and moni_second>= second_time2 and twice:            
                    TopFrame.OnClick_Tijiao()        
                    logging.info("moni1 second_tijiao %s %s %s %s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni second_tijiao %s %s %s" % (tijiao_num, moni_second, second_time2))
                    tijiao_on = False
                elif tijiao_num ==1 and   lowest_price >= own_price1-300-one_advance and  not tijiao_one:        
                    tijiao_on = False                        
                    TopFrame.OnClick_Tijiao()        
                    logging.info("moni one_tijiao %s %s %s %s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni one_tijiao %s %s %s" % (tijiao_num, lowest_price, own_price1))
                    tijiao_one = True         
                elif tijiao_num == 2 and lowest_price >= own_price2-300-second_advance and twice:        
                    tijiao_on = False                        
                    TopFrame.OnClick_Tijiao()       
                    logging.info("moni2 second_tijiao %s%s%s%s" % (tijiao_on, strategy_on, moni_on, tijiao_OK))
                    logging.info("moni second_tijiao %s%s%s" % (tijiao_num, lowest_price, own_price2))
                 
                                        
                                                    
                                                     
            if strategy_on and moni_on and chujia_on :                     
                if tijiao_num == 1 and  one_time1<=moni_second<=one_time1+0.2:             
                    TopFrame.OnClick_chujia()        
                                  
                    own_price1=lowest_price+one_diff
                    tijiao_on=True
                    logging.info("moni one_chujia %s %s" %(strategy_on,moni_on))
                    logging.info("moni one_chujia %s %s" %(one_time1,moni_second))
                elif tijiao_num == 2 and  twice and  second_time1<moni_second:
                    TopFrame.OnClick_chujia()        
                                  
                    own_price2=lowest_price+second_diff
                    tijiao_on=True
                    logging.info("moni second_chujia %s %s" %(strategy_on,moni_on))
                    logging.info("moni second_chujia %s %s" %(second_time1,moni_second))



class SketchApp(wx.App):
    def OnInit(self):
        try:
            bitmap = wx.Bitmap('start.png', wx.BITMAP_TYPE_PNG)

            wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                         1500, None, -1, wx.DefaultPosition, size=(300,240),
                                        style=wx.BORDER_SIMPLE | wx.STAY_ON_TOP)

            wx.Yield()
        except:
            pass
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


                                           
