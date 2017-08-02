# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/2 12:37
'''
""#line:5
version ='1.3'#line:8
num =0 #line:9
host_ali ="121.196.220.94"#line:11
url1 ="http://moni.51hupai.org/"#line:14
url2 ="https://paimai.alltobid.com/bid/2017052001/login.htm"#line:15
mainicon ='ico.ico'#line:17
view =False #line:20
do =False #line:21
ad_view =False #line:22
price_view =False #line:24
price_on =False #line:25
price_count =0 #line:26
web_on =False #line:27
view_time =False #line:29
time_on =False #line:30
import time as O0000000OO0OO000O #line:31
a_time =O0000000OO0OO000O .time ()#line:32
b_time =0 #line:33
moni_minute =29 #line:35
moni_second =0 #line:36
chujia_time =0 #line:38
Username =0 #line:40
Password =0 #line:41
moni_on =False #line:44
guopai_on =False #line:45
strategy1 =53 #line:48
strategy2 =0.0 #line:49
strategy_on =True #line:55
strategy_repeat =False #line:56
delay =False #line:59
delay_time =0.5 #line:60
login_result =False #line:62
findpos_on =True #line:65
pricelist =[80000 +OO0O0OO0OO0OOO0OO *100 for OO0O0OO0OO0OOO0OO in range (200 )]#line:67
import pyautogui as O0OO0OOO0O0O00OO0 #line:70
def Create_hash ():#line:72
    with open ('dick.dl','rb')as O000O00O00OOOO0OO :#line:73
        global dick_hash #line:74
        dick_hash =O00OOOO0O00000O0O .load (O000O00O00OOOO0OO )#line:75
    with open ('cf.btn','rb')as O00000OO0O00O00OO :#line:76
        global cf_hash #line:77
        cf_hash =O00OOOO0O00000O0O .load (O00000OO0O00O00OO )#line:78
    with open ("target.tkl",'rb')as OO0OO0OOO00O00000 :#line:80
        global dick_target #line:81
        dick_target =O00OOOO0O00000O0O .load (OO0OO0OOO00O00000 )#line:82
one_time1 =48 #line:87
one_time2 =55 #line:88
one_real_time1 =1000000000000 #line:89
one_real_time2 =1000000000000 #line:90
one_diff =700 #line:91
one_delay =0.5 #line:92
one_advance =100 #line:93
second_time1 =48 #line:96
second_time2 =55 #line:97
second_real_time1 =1000000000000 #line:98
second_real_time2 =1000000000000 #line:99
second_diff =600 #line:100
second_delay =0.5 #line:101
second_advance =100 #line:102
osl =[0 ]*15 #line:104
chujia_on =True #line:106
tijiao_on =False #line:107
lowest_price =86000 #line:110
own_price1 =0 #line:111
own_price2 =0 #line:112
own_price =0 #line:113
tijiao_OK =False #line:115
e_on =True #line:116
enter_on =False #line:117
twice =False #line:119
tijiao_num =1 #line:120
tijiao_one =False #line:121
websize =[1024 ,768 ]#line:124
Pxy =O0OO0OOO0O0O00OO0 .size ()#line:125
Px1 =Pxy [0 ]/2 #line:126
Py2 =Pxy [1 ]/2 #line:127
Px =(Pxy [0 ]-websize [0 ])/2 #line:128
Py =(Pxy [1 ]-websize [1 ])/2 #line:129
P_relative =[[343 ,-66 ],[346 ,40 ],[96 ,121 ],[92 ,43 ],[201 ,100 ],[281 ,40 ],[221 ,37 ],[282 ,118 ]]#line:132
P_relative2 =[[647 ,-98 ],[650 ,8 ],[400 ,89 ],[396 ,11 ],[505 ,68 ],[585 ,8 ],[525 ,5 ],[586 ,86 ]]#line:133
Position =[[0 ,0 ]for O00OO0O00000O0OOO in range (len (P_relative ))]#line:134
for i in range (len (Position )):#line:135
    Position [i ][0 ]=Px1 +P_relative [i ][0 ]#line:136
    Position [i ][1 ]=Py2 +P_relative [i ][1 ]#line:137
px_ajust ,py_ajust =0 ,0 #line:140
for i in range (len (P_relative )):#line:141
    P_relative [i ][0 ]+=websize [0 ]/2 +px_ajust #line:142
    P_relative [i ][1 ]+=websize [1 ]/2 +py_ajust #line:143
px_price =770 -171 #line:145
py_price =260 #line:146
px_priceframe =220 -191 #line:148
py_priceframe =510 #line:149
px_timeframe =400 -35 #line:151
py_timeframe =460 #line:152
px_yanzhengmaframe =400 -215 #line:154
py_yanzhengmaframe =460 #line:155
px_mini =200 #line:159
py_mini =40 #line:160
Pricesize =[400 ,80 ]#line:162
Timesize =[200 ,50 ]#line:164
refresh_area =[396 -80 ,11 -50 ,396 +80 ,11 +50 ]#line:167
confirm_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:168
Px_price =Px +px_price #line:187
Py_price =Py +py_price #line:188
Pos_price =[Px_price ,Py_price ,Px_price +px_mini ,Py_price +py_mini ]#line:189
Px_priceframe =Px +px_priceframe #line:192
Py_priceframe =Py +py_priceframe #line:193
Pos_priceframe =[Px_priceframe ,Py_priceframe ]#line:194
Px_timeframe =px_timeframe #line:197
Py_timeframe =py_timeframe #line:198
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:199
Px_yanzhengmaframe =Px +px_yanzhengmaframe #line:202
Py_yanzhengmaframe =Py +py_yanzhengmaframe #line:203
Pos_yanzhengmaframe =[Px_yanzhengmaframe ,Py_yanzhengmaframe ]#line:204
px_lowestprice =0 #line:212
py_lowestprice =0 #line:213
Px_lowestprice =Px +px_lowestprice #line:216
Py_lowestprice =Py +py_lowestprice #line:217
lowestprice_sizex =41 #line:218
lowestprice_sizey =16 #line:219
px_relative =49 #line:221
py_relative =0 #line:222
px_confirm =656 #line:224
py_confirm =475 #line:225
Px_confirm =Px +px_confirm #line:226
Py_confirm =Py +py_confirm #line:227
confirm_sizex =113 #line:228
confirm_sizey =28 #line:229
confirm_on =False #line:230
confirm_need =False #line:231
confirm_one =False #line:232
px_refresh =550 #line:234
py_refresh =413 #line:235
Px_refresh =Px +px_refresh #line:236
Py_refresh =Py +py_refresh #line:237
refresh_sizex =108 #line:238
refresh_sizey =21 #line:239
refresh_on =False #line:240
refresh_need =False #line:241
refresh_one =False #line:242
chujia_interval =False #line:244
tijiao_interval =False #line:245
query_interval =False #line:246
query_on =False #line:247
import sys as OO0OO0OOOOOOO00OO #line:250
if OO0OO0OOOOOOO00OO .platform !='win32':#line:251
    exit ()#line:252
import pyautogui as O0OO0OOO0O0O00OO0 #line:253
import ctypes as O000O00OO00O0OOOO #line:254
from ctypes import wintypes as O00O00O00OOOOOO00 #line:255
import win32con as OO000O000OO0O00O0 #line:256
O0O0OOO0O0O0000OO =__import__ ('wx.html2',globals (),locals ())#line:257
import wx as O0O0OOO0O0O0000OO #line:258
import pickle as O00OOOO0O00000O0O #line:259
O0O0OOO0O0O0000OO =__import__ ('wx.adv',globals (),locals ())#line:260
from PIL import Image as OOO0OO0O000OO0O00 #line:261
import imagehash as OO0OO0OOO0OO00O00 #line:262
import logging as OOO0O0O000O0OOO00 #line:339
timenow =O0000000OO0OO000O .time ()#line:340
time_local =O0000000OO0OO000O .localtime (timenow )#line:342
myapplog =O0000000OO0OO000O .strftime ("%Y%m%d%H%M%S",time_local )#line:344
print (myapplog )#line:345
OOO0O0O000O0OOO00 .basicConfig (level =OOO0O0O000O0OOO00 .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:350
OOO0O0O000O0OOO00 .debug ('This is debug message')#line:352
OOO0O0O000O0OOO00 .info ('This is info message')#line:353
OOO0O0O000O0OOO00 .warning ('This is warning message')#line:354
OOO0O0O000O0OOO00 .error ('This is error message')#line:355
import win32gui as O0OO0O000OO00O00O ,win32api as O0OOOOOOOO000OOOO #line:358
import cv2 as OO00O00O0OO00O0OO #line:359
from PIL import ImageGrab as O000OOO00O00O00O0 #line:360
def Click (OO0O0O00O0OO000OO ,OO0O0O00OOO0O0O0O ):#line:361
    O00O000OO0O00O0OO =O0OO0O000OO00O00O .GetCursorPos ()#line:362
    OO0O0O00O0OO000OO =int (OO0O0O00O0OO000OO )#line:363
    OO0O0O00OOO0O0O0O =int (OO0O0O00OOO0O0O0O )#line:364
    O0OOOOOOOO000OOOO .SetCursorPos ((OO0O0O00O0OO000OO ,OO0O0O00OOO0O0O0O ))#line:365
    O0OOOOOOOO000OOOO .mouse_event (OO000O000OO0O00O0 .MOUSEEVENTF_LEFTDOWN ,OO0O0O00O0OO000OO ,OO0O0O00OOO0O0O0O ,0 ,0 )#line:366
    O0OOOOOOOO000OOOO .mouse_event (OO000O000OO0O00O0 .MOUSEEVENTF_LEFTUP ,OO0O0O00O0OO000OO ,OO0O0O00OOO0O0O0O ,0 ,0 )#line:367
    O0OOOOOOOO000OOOO .SetCursorPos (O00O000OO0O00O0OO )#line:368
import win32clipboard as O00O0OOO00O000OOO #line:371
def Paste ():#line:372
    O0OOOOOOOO000OOOO .keybd_event (17 ,0 ,0 ,0 )#line:374
    O0OOOOOOOO000OOOO .keybd_event (86 ,0 ,0 ,0 )#line:375
    O0OOOOOOOO000OOOO .keybd_event (86 ,0 ,OO000O000OO0O00O0 .KEYEVENTF_KEYUP ,0 )#line:376
    O0OOOOOOOO000OOOO .keybd_event (17 ,0 ,OO000O000OO0O00O0 .KEYEVENTF_KEYUP ,0 )#line:377
def setText (OOOOOO0000O000OO0 ):#line:379
    OOOOOO0000O000OO0 =OOOOOO0000O000OO0 .encode ('utf-8')#line:380
    O00O0OOO00O000OOO .OpenClipboard ()#line:381
    O00O0OOO00O000OOO .EmptyClipboard ()#line:382
    O00O0OOO00O000OOO .SetClipboardData (OO000O000OO0O00O0 .CF_TEXT ,OOOOOO0000O000OO0 )#line:383
    O00O0OOO00O000OOO .CloseClipboard ()#line:384
def findpos ():#line:387
    OO00OO00OOO00OOO0 =O000OOO00O00O00O0 .grab ().convert ('L')#line:389
    OOOOOOOOO00OO0O00 =O0O00OO00OO0OOOO0 .asarray (OO00OO00OOO00OOO0 )#line:390
    global dick_target #line:391
    OO000OO00OOO00OOO =dick_target [2 ]#line:392
    OOOOOOO0O00000000 ,O00000O0OOOOOOOO0 =OO000OO00OOO00OOO .shape [::-1 ]#line:393
    OOOOO00O00O0OO0O0 =OO00O00O0OO00O0OO .matchTemplate (OOOOOOOOO00OO0O00 ,OO000OO00OOO00OOO ,OO00O00O0OO00O0OO .TM_CCOEFF_NORMED )#line:395
    O000O00OO0O0000OO ,OOOOO0O0O0OO0O0O0 ,OOO00OO0O0O0OO00O ,O0O00OO00000O000O =OO00O00O0OO00O0OO .minMaxLoc (OOOOO00O00O0OO0O0 )#line:396
    global px_lowestprice ,py_lowestprice ,px_relative ,py_relative ,Px_lowestprice ,Py_lowestprice ,Px ,Py #line:401
    px_lowestprice =O0O00OO00000O000O [0 ]+px_relative #line:402
    py_lowestprice =O0O00OO00000O000O [1 ]+py_relative #line:403
    Px_lowestprice =px_lowestprice #line:404
    Py_lowestprice =py_lowestprice #line:405
    global Position ,refresh_area ,confirm_area #line:407
    for OOOOO0OO000000O0O in range (len (Position )):#line:408
        Position [OOOOO0OO000000O0O ][0 ]=Px_lowestprice +P_relative2 [OOOOO0OO000000O0O ][0 ]#line:409
        Position [OOOOO0OO000000O0O ][1 ]=Py_lowestprice +P_relative2 [OOOOO0OO000000O0O ][1 ]#line:410
    refresh_area =[396 -80 +Px_lowestprice ,11 -50 +Py_lowestprice ,396 +80 +Px_lowestprice ,11 +50 +Py_lowestprice ]#line:411
    confirm_area =[505 -80 +Px_lowestprice ,68 -50 +Py_lowestprice ,505 +80 +Px_lowestprice ,68 +50 +Py_lowestprice ]#line:412
    global findpos_on #line:414
    findpos_on =False #line:415
def findrefresh ():#line:417
    global dick_target ,refresh_on ,Position ,refresh_area ,confirm_area #line:418
    O00000OO0000000OO =dick_target [0 ]#line:419
    OO00OOOO0OO000O00 =O000OOO00O00O00O0 .grab (refresh_area ).convert ('L')#line:420
    OOOO0O000000OO000 =O0O00OO00OO0OOOO0 .asarray (OO00OOOO0OO000O00 )#line:421
    OO0OO0OOOOO00O00O ,O000O00OO0OO000OO =O00000OO0000000OO .shape [::-1 ]#line:422
    O000000000OO0OO0O =OO00O00O0OO00O0OO .matchTemplate (OOOO0O000000OO000 ,O00000OO0000000OO ,OO00O00O0OO00O0OO .TM_CCOEFF_NORMED )#line:423
    O0OO0O0O0000OO000 ,O000O0000OO0OOOO0 ,O00OOO00000OOO0O0 ,OO0OOO0OOOO0O0OO0 =OO00O00O0OO00O0OO .minMaxLoc (O000000000OO0OO0O )#line:424
    if O000O0000OO0OOOO0 >=0.9 :#line:426
        refresh_on =True #line:427
def findconfirm ():#line:430
    global dick_target ,confirm_on ,Position #line:431
    O0O00OO000O0O000O =dick_target [1 ]#line:432
    OO0OO000OO000OOO0 =O000OOO00O00O00O0 .grab (confirm_area ).convert ('L')#line:433
    O000O000O0OOOO00O =O0O00OO00OO0OOOO0 .asarray (OO0OO000OO000OOO0 )#line:434
    OO0O0O0OOO0000O0O ,O0OOOO00OOOO00O0O =O0O00OO000O0O000O .shape [::-1 ]#line:435
    OOO00O0O00OOOO00O =OO00O00O0OO00O0OO .matchTemplate (O000O000O0OOOO00O ,O0O00OO000O0O000O ,OO00O00O0OO00O0OO .TM_CCOEFF_NORMED )#line:436
    OO00O00O00O00O0OO ,O000O0OO0O0OOOOOO ,OOO0O0000O0O0OO00 ,O0OO0OO0O000OO000 =OO00O00O0OO00O0OO .minMaxLoc (OOO00O0O00OOOO00O )#line:437
    print (O000O0OO0O0OOOOOO )#line:438
    if O000O0OO0O0OOOOOO >=0.9 :#line:439
        confirm_on =True #line:440
SZ =20 #line:444
bin_n =16 #line:445
import numpy as O0O00OO00OO0OOOO0 #line:446
def hog (O0OO00O0000OOO000 ):#line:449
    O00O000O0O0OOOOOO =OO00O00O0OO00O0OO .Sobel (O0OO00O0000OOO000 ,OO00O00O0OO00O0OO .CV_32F ,1 ,0 )#line:450
    OO000O000O0OO00OO =OO00O00O0OO00O0OO .Sobel (O0OO00O0000OOO000 ,OO00O00O0OO00O0OO .CV_32F ,0 ,1 )#line:451
    O0OOOO00O000OO0O0 ,OO0O000OOO000000O =OO00O00O0OO00O0OO .cartToPolar (O00O000O0O0OOOOOO ,OO000O000O0OO00OO )#line:452
    O0O00000000OO00OO =O0O00OO00OO0OOOO0 .int32 (bin_n *OO0O000OOO000000O /(2 *O0O00OO00OO0OOOO0 .pi ))#line:453
    O000O00OOOOO0OOOO =O0O00000000OO00OO [:10 ,:10 ],O0O00000000OO00OO [10 :,:10 ],O0O00000000OO00OO [:10 ,10 :],O0O00000000OO00OO [10 :,10 :]#line:454
    O000O0O00OO00O0O0 =O0OOOO00O000OO0O0 [:10 ,:10 ],O0OOOO00O000OO0O0 [10 :,:10 ],O0OOOO00O000OO0O0 [:10 ,10 :],O0OOOO00O000OO0O0 [10 :,10 :]#line:455
    OOOOO0OO00O000OO0 =[O0O00OO00OO0OOOO0 .bincount (O0OOOO0O0000O00O0 .ravel (),OOOOO0OOO0O0OO0OO .ravel (),bin_n )for O0OOOO0O0000O00O0 ,OOOOO0OOO0O0OO0OO in zip (O000O00OOOOO0OOOO ,O000O0O00OO00O0O0 )]#line:456
    O000O0000OO0O00OO =O0O00OO00OO0OOOO0 .hstack (OOOOO0OO00O000OO0 )#line:457
    return O000O0000OO0O00OO #line:458
def cut (OO00OO0OOOOOOOOOO ):#line:462
    O00O00O0OO0OO0OOO ,O000OO0O0O000O00O =OO00O00O0OO00O0OO .threshold (OO00OO0OOOOOOOOOO ,127 ,255 ,OO00O00O0OO00O0OO .THRESH_BINARY_INV )#line:463
    OO0OOO0OO00OOOO0O ,O0OO0O0O0OOO00O0O ,OO000OOO0OO0OO0O0 =OO00O00O0OO00O0OO .findContours (O000OO0O0O000O00O ,OO00O00O0OO00O0OO .RETR_EXTERNAL ,OO00O00O0OO00O0OO .CHAIN_APPROX_NONE )#line:465
    O0OOOO0O0O00000OO =[]#line:466
    OO0OO0OOOO000OO00 =[]#line:467
    for O0000OOO000OO000O in range (len (O0OO0O0O0OOO00O0O )):#line:468
        OOOOOO0O000O0OO0O =O0OO0O0O0OOO00O0O [O0000OOO000OO000O ]#line:469
        OOOOO0OOO0O000OOO ,O00OOO0000O0OOO0O ,OO00000O000OOO0OO ,O0O00O000OO0OO0O0 =OO00O00O0OO00O0OO .boundingRect (OOOOOO0O000O0OO0O )#line:470
        OO0OO0OOOO000OO00 .append ([OOOOO0OOO0O000OOO ,O00OOO0000O0OOO0O ,OO00000O000OOO0OO ,O0O00O000OO0OO0O0 ])#line:472
    OO0OO0OOOO000OO00 =sorted (OO0OO0OOOO000OO00 )#line:474
    for O0000OOO000OO000O in range (len (O0OO0O0O0OOO00O0O )):#line:475
        OOOOO0OOO0O000OOO ,O00OOO0000O0OOO0O ,OO00000O000OOO0OO ,O0O00O000OO0OO0O0 =OO0OO0OOOO000OO00 [O0000OOO000OO000O ]#line:476
        O0OOOO0O0O00000OO .append (OO0OOO0OO00OOOO0O [O00OOO0000O0OOO0O :O00OOO0000O0OOO0O +O0O00O000OO0OO0O0 ,OOOOO0OOO0O000OOO :OOOOO0OOO0O000OOO +OO00000O000OOO0OO ])#line:477
    return O0OOOO0O0O00000OO #line:478
def readpic (O0OO000000000OO0O ):#line:480
    try :#line:481
        O0OOOOO0OOO0O000O =OO00O00O0OO00O0OO .ml .SVM_load ('maindata.xml')#line:482
        OOOO0O0O0O000O0O0 =cut (O0OO000000000OO0O )#line:483
        OOOO0O0O0O000O0O0 =list (map (hog ,OOOO0O0O0O000O0O0 ))#line:484
        OOOO0O0O0O000O0O0 =O0O00OO00OO0OOOO0 .float32 (OOOO0O0O0O000O0O0 ).reshape (-1 ,64 )#line:485
        OO0OO0OOO0OOOOOOO =O0OOOOO0OOO0O000O .predict (OOOO0O0O0O000O0O0 )#line:486
        OO0OO0OOO0OOOOOOO =OO0OO0OOO0OOOOOOO [1 ].reshape (-1 ).astype (int ).astype (str )#line:487
        O000O000O0O0O0O00 ="".join (list (OO0OO0OOO0OOOOOOO ))#line:488
        return O000O000O0O0O0O00 #line:489
    except :#line:490
        return False #line:491
import smtplib as O0OOOOOO0OO0O0000 #line:509
from email .mime .text import MIMEText as OO000OOOOOO00OO00 #line:512
import os as OO0O00O0O0O0O0OOO #line:513
import mimetypes as O0O00OOOO0O0O0000 #line:514
import email as O00OOOOOOO0O00000 #line:515
from email .mime .multipart import MIMEMultipart as OO0OOOOOO00O0000O #line:516
from threading import Thread as OO00O000000O0OOO0 #line:519
import threading as OOOOO0000OOOO0O00 #line:520
from wx .lib .pubsub import pub as OOOO0000OO0OOO0OO #line:521
import socket as O0OOOOO00O00000OO ,sys as OO0OO0OOOOOOO00OO ,json as O000OO00O00O0O000 #line:526
timeout =10 #line:527
O0OOOOO00O00000OO .setdefaulttimeout (timeout )#line:528
def ConfirmUser ():#line:530
    O0OOO000O0O000OO0 =host_ali #line:531
    OOO0O0O0O0OO00000 =8080 #line:534
    O00000O0O0O00OO0O =O0OOOOO00O00000OO .socket (O0OOOOO00O00000OO .AF_INET ,O0OOOOO00O00000OO .SOCK_STREAM )#line:536
    try :#line:538
        O00000O0O0O00OO0O .connect ((O0OOO000O0O000OO0 ,OOO0O0O0O0OO00000 ))#line:539
    except O0OOOOO00O00000OO .gaierror as OOO0000OO000000OO :#line:540
        OOO0O0O000O0OOO00 .error ('连接失败 %s'%OOO0000OO000000OO )#line:541
        OOO0O0O000O0OOO00 .error ("Address-related error connecting to server: %s"%OOO0000OO000000OO )#line:542
        return 'net error'#line:543
    except O0OOOOO00O00000OO .error as OOO0000OO000000OO :#line:545
        OOO0O0O000O0OOO00 .error ('连接失败 %s'%OOO0000OO000000OO )#line:546
        OOO0O0O000O0OOO00 .error ("Connection error: %s"%OOO0000OO000000OO )#line:547
        return 'net error'#line:548
    O0OO00OOOO0O0O0O0 =[Username ,Password ]#line:552
    O0OO00OOOO0O0O0O0 =O000OO00O00O0O000 .dumps (O0OO00OOOO0O0O0O0 )#line:553
    O0OO00OOOO0O0O0O0 =bytes (O0OO00OOOO0O0O0O0 ,encoding ="utf-8")#line:554
    OOO0O0O000O0OOO00 .info ('发送信息 %s'%str (O0OO00OOOO0O0O0O0 ,encoding ="utf-8"))#line:555
    O00000O0O0O00OO0O .send (O0OO00OOOO0O0O0O0 )#line:556
    O00000O0O0O00OO0O .shutdown (1 )#line:558
    OOO0O0O000O0OOO00 .info ("Submit Complete")#line:559
    print ("Submit Complete")#line:560
    try :#line:561
        OOOOO00OO000O00OO =O00000O0O0O00OO0O .recv (1024 )#line:562
        OOOOO00OO000O00OO =str (OOOOO00OO000O00OO ,encoding ="utf-8")#line:563
        OOOOO00OO000O00OO =O000OO00O00O0O000 .loads (OOOOO00OO000O00OO )#line:564
        O0OO0O000OOOO0OO0 =OOOOO00OO000O00OO [0 ]#line:566
        if O0OO0O000OOOO0OO0 =='success':#line:567
            OOO0O0O000O0OOO00 .info ('登录成功 %s'%O0OO0O000OOOO0OO0 )#line:568
            global url2 #line:569
            url2 =OOOOO00OO000O00OO [1 ]#line:570
            return 'login success'#line:571
        elif O0OO0O000OOOO0OO0 =='repeat':#line:572
            OOO0O0O000O0OOO00 .warning ('账号错误 %s'%O0OO0O000OOOO0OO0 )#line:573
            return 'repeat'#line:574
    except :#line:575
        OOO0O0O000O0OOO00 .warning ('连接失败 ')#line:576
        return False #line:577
def Logout ():#line:580
    OOO0O0OO0000O00OO =host_ali #line:581
    O00OO0OOOOO0000O0 =8080 #line:584
    global Username #line:585
    Username =Username #line:586
    OOOO0O000OO00OOO0 =O0OOOOO00O00000OO .socket (O0OOOOO00O00000OO .AF_INET ,O0OOOOO00O00000OO .SOCK_STREAM )#line:587
    try :#line:588
        OOOO0O000OO00OOO0 .connect ((OOO0O0OO0000O00OO ,O00OO0OOOOO0000O0 ))#line:589
    except O0OOOOO00O00000OO .gaierror as O000O0OOOOO00OO00 :#line:590
        print ("Address-related error connecting to server: %s"%O000O0OOOOO00OO00 )#line:591
        OOO0O0O000O0OOO00 .info ("Address-related error connecting to server: %s"%O000O0OOOOO00OO00 )#line:592
    except O0OOOOO00O00000OO .error as O000O0OOOOO00OO00 :#line:594
        print ("Connection error: %s"%O000O0OOOOO00OO00 )#line:595
        OOO0O0O000O0OOO00 .info ("Connection error: %s"%O000O0OOOOO00OO00 )#line:596
    OO0OO0O0OO0O0O0O0 ='logout'+Username #line:600
    OO0OO0O0OO0O0O0O0 =O000OO00O00O0O000 .dumps (OO0OO0O0OO0O0O0O0 )#line:601
    OO0OO0O0OO0O0O0O0 =bytes (OO0OO0O0OO0O0O0O0 ,encoding ="utf-8")#line:602
    OOOO0O000OO00OOO0 .send (OO0OO0O0OO0O0O0O0 )#line:603
    OOOO0O000OO00OOO0 .shutdown (1 )#line:604
    print ("Submit Log Out Complete")#line:605
    OOO0O0O000O0OOO00 .info ("Submit Log Out Complete")#line:606
def Keeplogin ():#line:609
    O0OOO0O00O00OOO00 =host_ali #line:610
    OO00O0OO0OO0O0OO0 =8080 #line:613
    global Username #line:614
    Username =Username #line:615
    OOOO0O0O0O0O00O0O =O0OOOOO00O00000OO .socket (O0OOOOO00O00000OO .AF_INET ,O0OOOOO00O00000OO .SOCK_STREAM )#line:616
    try :#line:617
        OOOO0O0O0O0O00O0O .connect ((O0OOO0O00O00OOO00 ,OO00O0OO0OO0O0OO0 ))#line:618
    except O0OOOOO00O00000OO .gaierror as O0O0O000OO0O0O000 :#line:619
        print ("Address-related error connecting to server: %s"%O0O0O000OO0O0O000 )#line:620
        OOO0O0O000O0OOO00 .info ("Address-related error connecting to server: %s"%O0O0O000OO0O0O000 )#line:621
    except O0OOOOO00O00000OO .error as O0O0O000OO0O0O000 :#line:623
        print ("Connection error: %s"%O0O0O000OO0O0O000 )#line:624
        OOO0O0O000O0OOO00 .info ("Connection error: %s"%O0O0O000OO0O0O000 )#line:625
    O0OOO0O0O00000O0O ='keep'+Username #line:629
    O0OOO0O0O00000O0O =O000OO00O00O0O000 .dumps (O0OOO0O0O00000O0O )#line:630
    O0OOO0O0O00000O0O =bytes (O0OOO0O0O00000O0O ,encoding ="utf-8")#line:631
    OOOO0O0O0O0O00O0O .send (O0OOO0O0O00000O0O )#line:632
    OOOO0O0O0O0O00O0O .shutdown (1 )#line:633
    print ("Submit keep Complete")#line:634
    OOO0O0O000O0OOO00 .info ("Submit keep Complete")#line:635
def send_mail (O00O0OOOO0O00OOO0 ,OOO0O0OOO0O0OOO00 ,O0O0O0OOOO00OO00O ):#line:638
    O0O00OOO0OOOOOOO0 =open (O0O0O0OOOO00OO00O ,'rb')#line:639
    OO000O00O0OO0O00O ,OOOO0000OO00OO0OO =O0O00OOOO0O0O0000 .guess_type (O0O0O0OOOO00OO00O )#line:640
    if OO000O00O0OO0O00O is None and OOOO0000OO00OO0OO is None :#line:641
        OO000O00O0OO0O00O ='application/octet-stream'#line:642
    OOOOO0O00OOOO00O0 ,O0OOO00O0OOOO0O0O =OO000O00O0OO0O00O .split ('/',1 )#line:643
    OO0O0O0O000OO00OO =O00OOOOOOO0O00000 .mime .base .MIMEBase (OOOOO0O00OOOO00O0 ,O0OOO00O0OOOO0O0O )#line:644
    OO0O0O0O000OO00OO .set_payload (O0O00OOO0OOOOOOO0 .read ())#line:645
    O0O00OOO0OOOOOOO0 .close ()#line:646
    O00OOOOOOO0O00000 .encoders .encode_base64 (OO0O0O0O000OO00OO )#line:647
    O0O0OO0O0O00O0O0O =OO0O00O0O0O0O0OOO .path .basename (O0O0O0OOOO00OO00O )#line:648
    OO0O0O0O000OO00OO .add_header ('Content-Disposition','attachment',filename =O0O0OO0O0O00O0O0O )#line:649
    OOO0O0OOO0O0OOO00 =OOO0O0OOO0O0OOO00 #line:650
    O00O0O0O0OO00O0O0 ='smtp.qq.com'#line:651
    OOOO00OO00O000O0O =OO0O00O0O0O0O0OOO .environ .get ('MAIL_USERNAME')#line:652
    OO0OO0O0000O0OOO0 =OO0O00O0O0O0O0OOO .environ .get ('MAIL_PASSWORD')#line:653
    O00O0O000O0OO0OO0 =OOOO00OO00O000O0O #line:654
    O00OOOO000OO00O0O =OO0OOOOOO00O0000O ()#line:655
    O00OOOO000OO00O0O .attach (OO0O0O0O000OO00OO )#line:656
    O00OOOO000OO00O0O ['Subject']=O00O0OOOO0O00OOO0 #line:657
    O00OOOO000OO00O0O ['From']=O00O0O000O0OO0OO0 #line:658
    O00OOOO000OO00O0O ['To']=";".join (OOO0O0OOO0O0OOO00 )#line:659
    OO0O000O0OOO0O000 =O0OOOOOO0OO0O0000 .SMTP_SSL (O00O0O0O0OO00O0O0 ,465 )#line:660
    OO0O000O0OOO0O000 .login (OOOO00OO00O000O0O ,OO0OO0O0000O0OOO0 )#line:661
    print ('login in  successfully')#line:662
    OO0O000O0OOO0O000 .sendmail (O00O0O000O0OO0OO0 ,OOO0O0OOO0O0OOO00 ,O00OOOO000OO00O0O .as_string ())#line:663
    OO0O000O0OOO0O000 .quit ()#line:664
    print ('send email  successfully')#line:665
def Upload ():#line:667
    pass #line:668
def Com_read ():#line:671
    pass #line:672
def Com_decision ():#line:676
    pass #line:677
class TopFrame (O0O0OOO0O0O0000OO .Frame ):#line:710
    def __init__ (OO00OOOO000OO00O0 ,OO0OO0O00O0O0OO00 ,OO000OOO0O0O0O0O0 ):#line:711
        O0O0OOO0O0O0000OO .Frame .__init__ (OO00OOOO000OO00O0 ,None ,-1 ,OO0OO0O00O0O0OO00 ,size =(520 ,320 ))#line:713
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CLOSE ,OO00OOOO000OO00O0 .OnClose )#line:714
        OOO00OOOOO000O00O =O0000000OO0OO000O .time ()#line:718
        OO00OOOO000OO00O0 .statusbar =OO00OOOO000OO00O0 .CreateStatusBar ()#line:722
        OO00OOOO000OO00O0 .statusbar .SetFieldsCount (3 )#line:724
        OO00OOOO000OO00O0 .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:725
        OO00OOOO000OO00O0 .icon =O0O0OOO0O0O0000OO .Icon (mainicon ,O0O0OOO0O0O0000OO .BITMAP_TYPE_ICO )#line:727
        OO00OOOO000OO00O0 .SetIcon (OO00OOOO000OO00O0 .icon )#line:728
        OO00OOOO000OO00O0 .statusbar .SetStatusText (u"版本号",0 )#line:730
        OO00OOOO000OO00O0 .statusbar .SetStatusText (u"%s"%OO000OOO0O0O0O0O0 ,1 )#line:733
        OO00OOOO000OO00O0 .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:736
        OO00OOOO000OO00O0 .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:737
        O00OO00000O000O00 =O0O0OOO0O0O0000OO .Panel (OO00OOOO000OO00O0 ,-1 )#line:739
        O00OO00000O000O00 .SetBackgroundColour ((240 ,255 ,255 ))#line:741
        OO00OOOO000OO00O0 .SetBackgroundColour ((240 ,255 ,255 ))#line:742
        OO00OOOO000OO00O0 .thread =TimeThread ()#line:770
        OO00OOOO000OO00O0 .keepthread =KeepThread ()#line:771
        OO00OOOO000OO00O0 .button5 =O0O0OOO0O0O0000OO .Button (O00OO00000O000O00 ,label ='打开模拟',pos =(190 ,190 ))#line:799
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OO00OOOO000OO00O0 .Openmoni ,OO00OOOO000OO00O0 .button5 )#line:800
        OO00OOOO000OO00O0 .button6 =O0O0OOO0O0O0000OO .Button (O00OO00000O000O00 ,label ='打开国拍',pos =(280 ,190 ))#line:802
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OO00OOOO000OO00O0 .OpenGuopai ,OO00OOOO000OO00O0 .button6 )#line:803
        OO00OOOO000OO00O0 .button16 =O0O0OOO0O0O0000OO .Button (O00OO00000O000O00 ,label ='修改国拍网址',pos =(370 ,190 ))#line:805
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OO00OOOO000OO00O0 .UrlGuopai ,OO00OOOO000OO00O0 .button16 )#line:806
        OO00OOOO000OO00O0 .urlText =O0O0OOO0O0O0000OO .TextCtrl (O00OO00000O000O00 ,-1 ,pos =(370 ,230 ),size =(120 ,25 ))#line:807
        OO00OOOO000OO00O0 .button7 =O0O0OOO0O0O0000OO .Button (O00OO00000O000O00 ,label ='显示帮助',pos =(10 ,190 ))#line:809
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OO00OOOO000OO00O0 .Help ,OO00OOOO000OO00O0 .button7 )#line:810
        OO00OOOO000OO00O0 .button8 =O0O0OOO0O0O0000OO .Button (O00OO00000O000O00 ,label ='验证码练习',pos =(100 ,190 ))#line:812
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OO00OOOO000OO00O0 .Yan_practice ,OO00OOOO000OO00O0 .button8 )#line:813
        OO00OOOO000OO00O0 .timer1 =O0O0OOO0O0O0000OO .Timer (OO00OOOO000OO00O0 )#line:848
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,OO00OOOO000OO00O0 .Price_view ,OO00OOOO000OO00O0 .timer1 )#line:849
        OO00OOOO000OO00O0 .timer1 .Start (500 )#line:850
        OO00OOOO000OO00O0 .timer2 =O0O0OOO0O0O0000OO .Timer (OO00OOOO000OO00O0 )#line:853
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,OO00OOOO000OO00O0 .MainControl ,OO00OOOO000OO00O0 .timer2 )#line:854
        OO00OOOO000OO00O0 .timer2 .Start (100 )#line:855
        OO00OOOO000OO00O0 .timer3 =O0O0OOO0O0O0000OO .Timer (OO00OOOO000OO00O0 )#line:863
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,OO00OOOO000OO00O0 .Lowest_price ,OO00OOOO000OO00O0 .timer3 )#line:864
        OO00OOOO000OO00O0 .timer3 .Start (100 )#line:865
        OO00OOOO000OO00O0 .timer4 =O0O0OOO0O0O0000OO .Timer (OO00OOOO000OO00O0 )#line:867
        OO00OOOO000OO00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,OO00OOOO000OO00O0 .Find_pos ,OO00OOOO000OO00O0 .timer4 )#line:868
        OO00OOOO000OO00O0 .timer4 .Start (150 )#line:869
        OO00OOOO000OO00O0 .lowestframe =LowestpriceFrame ()#line:872
        OO00OOOO000OO00O0 .lowestframe .Show (False )#line:873
        OO00OOOO000OO00O0 .operationframe =OperationFrame ()#line:880
        OO00OOOO000OO00O0 .operationframe .Show (False )#line:881
    def Lowest_price (OOOOO00000OOO0O0O ,OO0O00OOOOO0O0O00 ):#line:891
        global lowest_price ,findpos_on #line:892
        if not findpos_on :#line:893
            O00000O00O000O00O =int (TopFrame .Price_read ())#line:894
            if O00000O00O000O00O in pricelist :#line:896
                lowest_price =O00000O00O000O00O #line:897
            else :#line:898
                findpos_on =True #line:899
    def Find_pos (O00OOOO00O00O00OO ,O00OOO000O000O0O0 ):#line:916
        global findpos_on #line:917
        if findpos_on :#line:918
            findpos ()#line:919
    @staticmethod #line:925
    def Confirm ():#line:926
        global cf_hash ,confirm_on #line:927
        O00OOOO0O00OO0O0O =TopFrame .Confirm_hash ()#line:928
        if O00OOOO0O00OO0O0O ==cf_hash [0 ]:#line:929
            confirm_on =True #line:930
    @staticmethod #line:931
    def Refresh ():#line:932
        OOOOO00O0OO000OOO =TopFrame .Refresh_hash ()#line:933
        global cf_hash ,refresh_on #line:934
        if OOOOO00O0OO000OOO ==cf_hash [1 ]:#line:935
            refresh_on =True #line:936
    @staticmethod #line:945
    def Price_read ():#line:946
        O0O000O0OOO000OO0 =O000OOO00O00O00O0 .grab ((Px_lowestprice ,Py_lowestprice ,lowestprice_sizex +Px_lowestprice ,lowestprice_sizey +Py_lowestprice )).convert ('L')#line:948
        O0O000O0OOO000OO0 =O0O00OO00OO0OOOO0 .asarray (O0O000O0OOO000OO0 )#line:954
        O0OO00O0OOO0OOOOO =readpic (O0O000O0OOO000OO0 )#line:955
        return O0OO00O0OOO0OOOOO #line:957
    @staticmethod #line:960
    def Price_hash ():#line:961
        OOO00O0OO0000O0OO =O0OO0OOO0O0O00OO0 .screenshot (region =(Px_lowestprice ,Py_lowestprice ,lowestprice_sizex ,lowestprice_sizey ))#line:963
        global num #line:964
        num +=1 #line:965
        OO0OO0OO0OO0OO0OO =OO0OO0OOO0OO00O00 .dhash (OOO00O0OO0000O0OO )#line:967
        return OO0OO0OO0OO0OO0OO #line:970
    @staticmethod #line:972
    def Confirm_hash ():#line:973
        O00OO0O0O0O00000O =O0OO0OOO0O0O00OO0 .screenshot (region =(Px_confirm ,Py_confirm ,confirm_sizex ,confirm_sizey ))#line:975
        O00O00OOO000O0OO0 =OO0OO0OOO0OO00O00 .dhash (O00OO0O0O0O00000O )#line:978
        return O00O00OOO000O0OO0 #line:979
    @staticmethod #line:981
    def Refresh_hash ():#line:982
        OO00O0O0OOO0OO00O =O0OO0OOO0O0O00OO0 .screenshot (region =(Px_refresh ,Py_refresh ,refresh_sizex ,refresh_sizey ))#line:984
        OOO00O0OO0000O00O =OO0OO0OOO0OO00O00 .dhash (OO00O0O0OOO0OO00O )#line:986
        return OOO00O0OO0000O00O #line:987
    def OnEraseBackground (OO0000O0O0OOOO0OO ,O000O0OO00O0OOO00 ):#line:991
        ""#line:994
        O0O000O0O00OO0OO0 =O000O0OO00O0OOO00 .GetDC ()#line:995
        if not O0O000O0O00OO0OO0 :#line:996
            O0O000O0O00OO0OO0 =O0O0OOO0O0O0000OO .ClientDC (OO0000O0O0OOOO0OO )#line:997
            OOOOO0O0OOO000000 =OO0000O0O0OOOO0OO .GetUpdateRegion ().GetBox ()#line:998
            O0O000O0O00OO0OO0 .SetClippingRect (OOOOO0O0OOO000000 )#line:999
        O0O000O0O00OO0OO0 .Clear ()#line:1000
        OO0OO0O0O0000O00O =O0O0OOO0O0O0000OO .Bitmap ("blue.jpg")#line:1001
        O0O000O0O00OO0OO0 .DrawBitmap (OO0OO0O0O0000O00O ,0 ,0 )#line:1002
    def OnClose (OO0000000O0O0OO0O ,OOOOOOO0O0OO0O000 ):#line:1006
        OO0O0OO0OO0OO0O0O =O0O0OOO0O0O0000OO .MessageBox ('真的要退出第一枪吗?','确认',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .CANCEL )#line:1007
        if OO0O0OO0OO0OO0O0O ==O0O0OOO0O0O0000OO .OK :#line:1008
            import sys as O0O00OO0OOO000000 #line:1010
            OO0000000O0O0OO0O .Show (False )#line:1015
            try :#line:1017
                OO0000000O0O0OO0O .Close_time1 (OOOOOOO0O0OO0O000 )#line:1018
                OO0000000O0O0OO0O .Close_time2 (OOOOOOO0O0OO0O000 )#line:1019
            except :#line:1020
                pass #line:1021
            Logout ()#line:1023
            O0O0OOO0O0O0000OO .GetApp ().ExitMainLoop ()#line:1024
            OOOOOOO0O0OO0O000 .Skip ()#line:1025
            O0O00OO0OOO000000 .exit (None )#line:1026
    def OnOpenAssist (O000OO0O0O00O000O ):#line:1030
        O000OO0O0O00O000O .Open ()#line:1031
        global do #line:1032
        if do :#line:1033
            O0O0OOO0O0O0000OO .MessageBox ('启用成功','开启辅助',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_INFORMATION )#line:1034
        else :#line:1035
            O0O0OOO0O0O0000OO .MessageBox ('启用失败','开启辅助',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1036
        O000OO0O0O00O000O .Listen ()#line:1037
    @classmethod #line:1039
    def OnCloseAssist (OOO0O0O000OOOOOOO ):#line:1040
        OOO0O0O000OOOOOOO .Close ()#line:1041
    def OnViewPos (OOO0OOOO0O0OO0O00 ,OO0OO00OO0OOO000O ):#line:1048
        O0O0OOO0O0O0000OO .CallAfter (OOOO0000OO0OOO0OO .sendMessage ,"refresh")#line:1049
        OOO0OOOO0O0OO0O00 .MovePos (OO0OO00OO0OOO000O )#line:1050
        global view #line:1051
        if not view :#line:1052
            view =True #line:1053
            for OOOOO0OO0000OO0OO in range (len (Position )):#line:1054
                OOO0OOOO0O0OO0O00 .posframe [OOOOO0OO0000OO0OO ].Show (view )#line:1055
        else :#line:1056
            view =False #line:1057
            for OOOOO0OO0000OO0OO in range (len (Position )):#line:1058
                OOO0OOOO0O0OO0O00 .posframe [OOOOO0OO0000OO0OO ].Hide ()#line:1059
    def OnSavePos (OOO0O000000O00O0O ,OO000000OOO0000OO ):#line:1062
        OOO0O000000O00O0O .MovePos (OO000000OOO0000OO )#line:1063
        OOO0O000000O00O0O .Save_log ()#line:1064
        O0O0OOO0O0O0000OO .MessageBox ('保存成功','定位保存',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_INFORMATION )#line:1065
    def MovePos (O0OOOO00OOOO00000 ,OO00000O00OOOOOOO ):#line:1071
        global Positon #line:1072
        for OOO0O0OO00O0OO0OO in range (5 ):#line:1073
            O00OOOO0OO000000O ,O000OO0OO000OOO00 =Position [OOO0O0OO00O0OO0OO ]#line:1074
            O0OOOO00OOOO00000 .posframe [OOO0O0OO00O0OO0OO ].Move (O00OOOO0OO000000O -10 ,O000OO0OO000OOO00 -5 )#line:1075
    def Openmoni (O000OO0OO0OO00OOO ,OOO0O0OOO0O0OO0OO ):#line:1077
        global tijiao_num ,chujia_on ,tijiao_on ,strategy_on ,tijiao_OK #line:1079
        strategy_on =True #line:1080
        O00O0000O00O0OO00 =True #line:1081
        chujia_on =True #line:1082
        tijiao_on =False #line:1083
        tijiao_num =1 #line:1084
        tijiao_OK =False #line:1085
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,guopai_on ,moni_on ,strategy_repeat #line:1086
        if guopai_on :#line:1087
            O0O0OOO0O0O0000OO .MessageBox ('请关闭国拍页面','开启模拟失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1088
        elif moni_on :#line:1089
            O0O0OOO0O0O0000OO .MessageBox ('请关闭模拟页面','开启模拟失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1090
        else :#line:1091
            O000OO0OO0OO00OOO .Open ()#line:1096
            if do :#line:1097
                moni_on =True #line:1098
                ad_view =True #line:1099
                web_on =True #line:1100
                O000OO0OO0OO00OOO .fr =WebFrame (Px ,Py ,False ,'沪牌模拟')#line:1101
                O000OO0OO0OO00OOO .operationframe .Show (True )#line:1102
                if time_on :#line:1104
                    O000OO0OO0OO00OOO .operationframe .Opentime ()#line:1105
                if not strategy_repeat :#line:1106
                    O000OO0OO0OO00OOO .monitijiaothread =MoniTijiaoThread ()#line:1107
                    O000OO0OO0OO00OOO .tijiaothread =TijiaoThread ()#line:1108
                    strategy_repeat =True #line:1109
                OOOOO000OOO0OOO00 =O0O0OOO0O0O0000OO .html2 .WebView .New (O000OO0OO0OO00OOO .fr ,size =(websize [0 ],websize [1 ]),pos =(0 ,0 ))#line:1112
                OOOOO000OOO0OOO00 .LoadURL (url1 )#line:1113
                OOOOO000OOO0OOO00 .CanSetZoomType (False )#line:1114
                O000OO0OO0OO00OOO .fr .Show ()#line:1115
            else :#line:1119
                O0O0OOO0O0O0000OO .MessageBox ('请检查其它软件热键占用','辅助启用失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1120
                O000OO0OO0OO00OOO .Close ()#line:1121
            O000OO0OO0OO00OOO .Listen ()#line:1122
    def OpenGuopai (OO0000O00OOOOO0O0 ,O0O0O0OO00O0OO000 ):#line:1172
        global tijiao_num ,chujia_on ,tijiao_on ,strategy_on ,tijiao_OK #line:1174
        strategy_on =True #line:1175
        O0O0OOO0OOO00OO0O =True #line:1176
        chujia_on =True #line:1177
        tijiao_on =False #line:1178
        tijiao_num =1 #line:1179
        tijiao_OK =False #line:1180
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,moni_on ,guopai_on ,strategy_repeat #line:1181
        if moni_on :#line:1182
            O0O0OOO0O0O0000OO .MessageBox ('请关闭模拟页面','开启国拍失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1183
        elif guopai_on :#line:1184
            O0O0OOO0O0O0000OO .MessageBox ('国拍已经打开','开启国拍失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1185
        else :#line:1186
            OO0000O00OOOOO0O0 .Open ()#line:1188
            if do :#line:1192
                ad_view =True #line:1193
                guopai_on =True #line:1194
                OO0000O00OOOOO0O0 .fr =WebFrame (Px ,Py ,False ,'国拍网')#line:1195
                OO0000O00OOOOO0O0 .operationframe .Show (True )#line:1196
                if time_on :#line:1198
                    OO0000O00OOOOO0O0 .operationframe .Opentime ()#line:1199
                if not strategy_repeat :#line:1200
                    OO0000O00OOOOO0O0 .monitijiaothread =MoniTijiaoThread ()#line:1201
                    OO0000O00OOOOO0O0 .tijiaothread =TijiaoThread ()#line:1202
                    strategy_repeat =True #line:1203
                O00OO00OOO00O0OO0 =O0O0OOO0O0O0000OO .html2 .WebView .New (OO0000O00OOOOO0O0 .fr ,size =(websize [0 ],websize [1 ]))#line:1205
                O00OO00OOO00O0OO0 .LoadURL (url2 )#line:1206
                O00OO00OOO00O0OO0 .CanSetZoomType (False )#line:1207
                OO0000O00OOOOO0O0 .fr .Show ()#line:1208
            else :#line:1212
                O0O0OOO0O0O0000OO .MessageBox ('请检查其它软件热键占用','辅助启用失败',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1213
                OO0000O00OOOOO0O0 .Close ()#line:1214
            OO0000O00OOOOO0O0 .Listen ()#line:1215
    def UrlGuopai (O0O0O00OOOO0OOOO0 ,O0OOO00OO0O000OO0 ):#line:1217
        global url2 #line:1218
        try :#line:1219
            url2 =O0O0O00OOOO0OOOO0 .urlText .GetValue ()#line:1220
            O0O0OOO0O0O0000OO .MessageBox ('修改网址成功','修改国拍网址',O0O0OOO0O0O0000OO .OK )#line:1221
        except :#line:1222
            O0O0OOO0O0O0000OO .MessageBox ('请输入正确网址','修改国址网址',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:1223
    def Help (O0OOOOOO00O0OO0O0 ,OOO000OOO0OOOO0OO ):#line:1226
        OOO000OO0O000O0O0 ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1232
        OO000OO0000O0O00O =O0O0OOO0O0O0000OO .adv .AboutDialogInfo ()#line:1235
        OO000OO0000O0O00O .SetName ("沪牌第一枪")#line:1236
        OO000OO0000O0O00O .SetVersion (OOO000OO0O000O0O0 )#line:1237
        OO000OO0000O0O00O .AddDeveloper ("ZS")#line:1241
        O0O0OOO0O0O0000OO .adv .AboutBox (OO000OO0000O0O00O )#line:1242
    def Yan_practice (O00O0O00O0OOO0OOO ,O0000OO0O00O0OO00 ):#line:1244
        pass #line:1245
    def Time_adjust (OOOO000O00O0O0000 ,O0000O00OO00OOO0O ):#line:1247
        pass #line:1248
    @staticmethod #line:1258
    def OnJiajia ():#line:1259
        OOO0000O0OOOOOOOO =O0OO0OOO0O0O00OO0 .position ()#line:1260
        Position [0 ][0 ]=OOO0000O0OOOOOOOO [0 ]#line:1261
        Position [0 ][1 ]=OOO0000O0OOOOOOOO [1 ]#line:1262
        print (Position [0 ][0 ],"  ",Position [0 ][1 ])#line:1263
        findpos ()#line:1264
    @staticmethod #line:1267
    def OnChujia ():#line:1268
        O0000OOO0OO0O0OOO =O0OO0OOO0O0O00OO0 .position ()#line:1269
        Position [1 ][0 ]=O0000OOO0OO0O0OOO [0 ]#line:1270
        Position [1 ][1 ]=O0000OOO0OO0O0OOO [1 ]#line:1271
    @staticmethod #line:1272
    def OnTijiao ():#line:1273
        OO00OO0O00OO0O00O =O0OO0OOO0O0O00OO0 .position ()#line:1274
        Position [2 ][0 ]=OO00OO0O00OO0O00O [0 ]#line:1275
        Position [2 ][1 ]=OO00OO0O00OO0O00O [1 ]#line:1276
    @staticmethod #line:1277
    def OnShuaxin ():#line:1278
        OOOOOO0O000000OO0 =O0OO0OOO0O0O00OO0 .position ()#line:1279
        Position [3 ][0 ]=OOOOOO0O000000OO0 [0 ]#line:1280
        Position [3 ][1 ]=OOOOOO0O000000OO0 [1 ]#line:1281
    @staticmethod #line:1282
    def OnConfirm ():#line:1283
        O0OOO00OOOOOO000O =O0OO0OOO0O0O00OO0 .position ()#line:1284
        Position [4 ][0 ]=O0OOO00OOOOOO000O [0 ]#line:1285
        Position [4 ][1 ]=O0OOO00OOOOOO000O [1 ]#line:1286
    @staticmethod #line:1287
    def OnYanzhengma ():#line:1288
        OOO000OOOOO0OO000 =O0OO0OOO0O0O00OO0 .position ()#line:1289
        Position [5 ][0 ]=OOO000OOOOO0OO000 [0 ]#line:1290
        Position [5 ][1 ]=OOO000OOOOO0OO000 [1 ]#line:1291
    @staticmethod #line:1294
    def handle_Jiajia ():#line:1295
        TopFrame .OnJiajia ()#line:1296
    @staticmethod #line:1297
    def handle_Chujia ():#line:1298
        TopFrame .OnChujia ()#line:1299
    @staticmethod #line:1300
    def handle_Tijiao ():#line:1301
        TopFrame .OnTijiao ()#line:1302
    @staticmethod #line:1303
    def handle_Shuaxin ():#line:1304
        TopFrame .OnShuaxin ()#line:1305
    @staticmethod #line:1306
    def handle_Confirm ():#line:1307
        TopFrame .OnConfirm ()#line:1308
    @staticmethod #line:1309
    def handle_Yanzhengma ():#line:1310
        TopFrame .OnYanzhengma ()#line:1311
    @classmethod #line:1318
    def OnClick_Tijiao (OO0O00O000O0O0OOO ):#line:1319
        global web_on ,tijiao_on ,one_delay ,second_delay ,tijiao_num #line:1320
        global tijiao_on ,chujia_on ,confirm_one ,confirm_need #line:1321
        confirm_need =True #line:1322
        if tijiao_num ==1 :#line:1324
            O0OO0O00O00O0OO0O =OOOOO0000OOOO0O00 .Timer (one_delay ,OO0O00O000O0O0OOO .Tijiao )#line:1325
            O0OO0O00O00O0OO0O .start ()#line:1326
            tijiao_on =False #line:1327
            if twice :#line:1328
                print ("修改为2")#line:1329
                tijiao_num =2 #line:1330
            print ("成功提交")#line:1332
        elif tijiao_num ==2 :#line:1333
            tijiao_num =0 #line:1334
            O0OO0O00O00O0OO0O =OOOOO0000OOOO0O00 .Timer (second_delay ,OO0O00O000O0O0OOO .Tijiao )#line:1335
            O0OO0O00O00O0OO0O .start ()#line:1336
            tijiao_on =False #line:1337
        else :#line:1339
            OO0O00O000O0O0OOO .Tijiao ()#line:1340
    @staticmethod #line:1342
    def Tijiao ():#line:1343
        global tijiao_on ,tijiao_OK ,tijiao_num #line:1344
        Click (Position [2 ][0 ],Position [2 ][1 ])#line:1345
        tijiao_OK =False #line:1346
        global confirm_one #line:1347
        if not confirm_one :#line:1348
            O0O00OO000000O000 =confirmThread ()#line:1349
            confirm_one =False #line:1350
    @staticmethod #line:1357
    def OnClick_Shuaxin ():#line:1358
        global web_on #line:1359
        Click (Position [3 ][0 ],Position [3 ][1 ])#line:1360
        Click (Position [5 ][0 ],Position [5 ][1 ])#line:1361
    @staticmethod #line:1363
    def OnClick_confirm ():#line:1364
        print (Position [4 ][0 ],Position [4 ][1 ])#line:1365
        Click (Position [4 ][0 ],Position [4 ][1 ])#line:1366
    @staticmethod #line:1368
    def OnClick_chujia ():#line:1369
        global price_view ,price_count ,web_on ,lowest_price #line:1370
        global tijiao_num ,own_price1 ,own_price2 ,one_diff ,second_diff #line:1371
        global tijiao_on ,chujia_on #line:1372
        global refresh_need ,refresh_one ,chujia_interval #line:1373
        print (chujia_interval )#line:1374
        if not chujia_interval :#line:1375
            print (tijiao_num ,twice )#line:1376
            chujia_interval =True #line:1377
            tijiao_on =True #line:1378
            refresh_need =True #line:1379
            if tijiao_num ==1 :#line:1380
                own_price1 =lowest_price +one_diff #line:1381
                setText (str (own_price1 ))#line:1382
                Click (Position [6 ][0 ],Position [6 ][1 ])#line:1383
                Click (Position [6 ][0 ],Position [6 ][1 ])#line:1384
                Paste ()#line:1385
                Click (Position [1 ][0 ],Position [1 ][1 ])#line:1386
                tijiao_on =True #line:1387
                chujia_on =False #line:1388
                chujia_interval =False #line:1389
                print (chujia_interval )#line:1390
                if not refresh_one :#line:1392
                    O00O0O00000OOO000 =refreshThread ()#line:1393
                    refresh_one =True #line:1394
            elif tijiao_num ==2 and twice :#line:1395
                print ("第二次")#line:1396
                own_price2 =lowest_price +second_diff #line:1397
                setText (str (own_price2 ))#line:1398
                Click (Position [6 ][0 ],Position [6 ][1 ])#line:1399
                Click (Position [6 ][0 ],Position [6 ][1 ])#line:1400
                Paste ()#line:1401
                Click (Position [1 ][0 ],Position [1 ][1 ])#line:1402
                tijiao_on =True #line:1403
                chujia_on =False #line:1404
                chujia_interval =False #line:1405
                if not refresh_one :#line:1406
                    O00O0O00000OOO000 =refreshThread ()#line:1407
                    refresh_one =True #line:1408
    @staticmethod #line:1474
    def OnClick_Backspace ():#line:1475
        O0OO0OOO0O0O00OO0 .press ('backspace')#line:1476
    def Price_view (O00000OO0OOO00000 ,O000O000O000OOO00 ):#line:1479
        global price_view ,web_on ,price_on ,view_time #line:1480
        pass #line:1481
    def MainControl (O0O0OOOO0O0OO0OO0 ,OO000O0O0O0OO000O ):#line:1496
        if not web_on and price_on :#line:1497
            O0O0OOOO0O0OO0OO0 .Price_close ()#line:1498
        if price_on and not tijiao_on :#line:1499
            O0O0OOOO0O0OO0OO0 .Price_close ()#line:1500
        if not web_on and time_on :#line:1501
            O0O0OOOO0O0OO0OO0 .operationframe .Closetime ()#line:1502
        O0OOOOOOO0OO0O000 ='sc_new.png'#line:1503
        if not OO0O00O0O0O0O0OOO .path .exists (O0OOOOOOO0OO0O000 ):#line:1504
            try :#line:1505
                O0O0OOOO0O0OO0OO0 .Price_close ()#line:1506
            except :#line:1507
                pass #line:1508
        if web_on :#line:1509
            O0O0OOOO0O0OO0OO0 .lowestframe .Show (True )#line:1510
            try :#line:1511
                O0O0OOOO0O0OO0OO0 .operationframe .Show (True )#line:1512
            except :#line:1513
                pass #line:1514
        else :#line:1515
            O0O0OOOO0O0OO0OO0 .lowestframe .Show (False )#line:1516
            try :#line:1517
                O0O0OOOO0O0OO0OO0 .operationframe .Show (False )#line:1518
            except :#line:1519
                pass #line:1520
        if web_on :#line:1523
            O0O0OOOO0O0OO0OO0 .Show (False )#line:1524
        else :#line:1525
            O0O0OOOO0O0OO0OO0 .Show (True )#line:1526
    @staticmethod #line:1530
    def tijiao_ok ():#line:1531
        global tijiao_OK ,refresh_need ,tijiao_on #line:1532
        if e_on and tijiao_on :#line:1533
            tijiao_OK =True #line:1534
            refresh_need =False #line:1535
    @staticmethod #line:1537
    def tijiao_ok2 ():#line:1538
        global tijiao_OK ,refresh_need #line:1539
        if enter_on and tijiao_on :#line:1540
            tijiao_OK =True #line:1541
            refresh_need =False #line:1542
    @classmethod #line:1544
    def query (OOO00O0000OO0OOO0 ):#line:1545
        global query_interval ,query_on #line:1546
        if not query_interval and not query_on :#line:1547
            print ("执行")#line:1548
            query_on =True #line:1549
            query_interval =True #line:1550
            setText (str (1000000 ))#line:1551
            Click (Position [6 ][0 ],Position [6 ][1 ])#line:1552
            Click (Position [6 ][0 ],Position [6 ][1 ])#line:1553
            Paste ()#line:1554
            Click (Position [1 ][0 ],Position [1 ][1 ])#line:1555
            OO0O000OO0O0OO0O0 =OOOOO0000OOOO0O00 .Timer (3 ,OOO00O0000OO0OOO0 .query_sleep3 )#line:1556
            OO0O000OO0O0OO0O0 .start ()#line:1557
            O0OOO0OOO00O00OOO =OOOOO0000OOOO0O00 .Timer (5 ,OOO00O0000OO0OOO0 .query_sleep5 )#line:1558
            O0OOO0OOO00O00OOO .start ()#line:1559
        elif query_interval and query_on :#line:1560
            print (Position [7 ][0 ],Position [7 ][1 ])#line:1561
            Click (Position [7 ][0 ],Position [7 ][1 ])#line:1562
            query_on =False #line:1563
    @staticmethod #line:1566
    def query_sleep3 ():#line:1567
        print ("触发3+")#line:1568
        global query_interval ,query_on #line:1569
        if query_on :#line:1570
            print (Position [7 ][0 ],Position [7 ][1 ])#line:1571
            Click (Position [7 ][0 ],Position [7 ][1 ])#line:1572
            query_on =False #line:1573
    @staticmethod #line:1575
    def query_sleep5 ():#line:1576
        print ("触发5")#line:1577
        global query_interval #line:1578
        query_interval =False #line:1579
    def Price_close (O0OOOO0OOOOO0O0OO ):#line:1584
        try :#line:1585
            O0OOOO0OOOOO0O0OO .priceframe .Destroy ()#line:1586
        except :#line:1587
            pass #line:1588
    def Price_count (O0OOOOO000000O0O0 ,O0O0O000O0OO0OOOO ):#line:1592
        global price_count #line:1593
        price_count +=1 #line:1594
    @staticmethod #line:1600
    def Open ():#line:1601
        global do ,web_on #line:1602
        if not do :#line:1603
            do =True #line:1604
            OOOO0OO0000OO00O0 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1610
            OOO00OO0OOOOO0O0O =O000O00OO00O0OOOO .windll .user32 #line:1611
            O0O00O00000000000 ={1 :(OOOO0OO0000OO00O0 ['2'],OO000O000OO0O00O0 .MOD_ALT ),2 :(OOOO0OO0000OO00O0 ['3'],OO000O000OO0O00O0 .MOD_ALT ),3 :(OOOO0OO0000OO00O0 ['4'],OO000O000OO0O00O0 .MOD_ALT ),4 :(OOOO0OO0000OO00O0 ['5'],OO000O000OO0O00O0 .MOD_ALT ),5 :(OOOO0OO0000OO00O0 ['6'],OO000O000OO0O00O0 .MOD_ALT ),6 :(OOOO0OO0000OO00O0 ['7'],OO000O000OO0O00O0 .MOD_ALT ),}#line:1615
            OOO0O0OO0O0OOO00O ={7 :(OOOO0OO0000OO00O0 ['s'],0x4000 ),8 :(OOOO0OO0000OO00O0 ['f'],0x4000 ),9 :(OOOO0OO0000OO00O0 ['d'],0x4000 ),10 :(OO000O000OO0O00O0 .VK_SPACE ,0x4000 ),11 :(OOOO0OO0000OO00O0 ['e'],0x4000 ),12 :(OO000O000OO0O00O0 .VK_RETURN ,0x4000 ),13 :(OOOO0OO0000OO00O0 ['q'],0x4000 )}#line:1618
            for O00O00000O0O00O0O ,(OOOOO0OO0OO0000OO ,OO0OOO0OO0OOOO0OO )in O0O00O00000000000 .items ():#line:1620
                if not OOO00OO0OOOOO0O0O .RegisterHotKey (None ,O00O00000O0O00O0O ,OO0OOO0OO0OOOO0OO ,OOOOO0OO0OO0000OO ):#line:1621
                    print ("Unable to register id",O00O00000O0O00O0O )#line:1622
                    OOO0O0O000O0OOO00 .info ("Unable to register id",O00O00000O0O00O0O )#line:1623
                    do =False #line:1624
            for O00O00000O0O00O0O ,(OOOOO0OO0OO0000OO ,OO0OOO0OO0OOOO0OO )in OOO0O0OO0O0OOO00O .items ():#line:1625
                if not OOO00OO0OOOOO0O0O .RegisterHotKey (None ,O00O00000O0O00O0O ,OO0OOO0OO0OOOO0OO ,OOOOO0OO0OO0000OO ):#line:1626
                    print ("Unable to register id",O00O00000O0O00O0O )#line:1627
                    OOO0O0O000O0OOO00 .info ("Unable to register id",O00O00000O0O00O0O )#line:1628
                    do =False #line:1629
                web_on =True #line:1630
    @staticmethod #line:1633
    def Listen ():#line:1634
        try :#line:1635
            OO00OOO00O00OO0O0 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1640
            O0O0OO00O0O0OO00O ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .OnClick_Tijiao ,9 :TopFrame .OnClick_chujia ,10 :TopFrame .OnClick_Backspace ,11 :TopFrame .tijiao_ok ,12 :TopFrame .tijiao_ok2 ,13 :TopFrame .query }#line:1646
            OOOOO0O0OOO0OOOO0 =O000O00OO00O0OOOO .windll .user32 #line:1647
            OOO0O000O0000O0O0 =O00O00O00OOOOOO00 .MSG ()#line:1648
            OO0OO0O00O0O0O000 =O000O00OO00O0OOOO .byref #line:1649
            while OOOOO0O0OOO0OOOO0 .GetMessageA (OO0OO0O00O0O0O000 (OOO0O000O0000O0O0 ),None ,0 ,0 )!=0 :#line:1650
                if OOO0O000O0000O0O0 .message ==OO000O000OO0O00O0 .WM_HOTKEY :#line:1651
                    O0000OO0O000O0000 =O0O0OO00O0O0OO00O .get (OOO0O000O0000O0O0 .wParam )#line:1652
                    if O0000OO0O000O0000 :#line:1653
                        O0000OO0O000O0000 ()#line:1654
                OOOOO0O0OOO0OOOO0 .TranslateMessage (OO0OO0O00O0O0O000 (OOO0O000O0000O0O0 ))#line:1655
                OOOOO0O0OOO0OOOO0 .DispatchMessageA (OO0OO0O00O0O0O000 (OOO0O000O0000O0O0 ))#line:1656
        finally :#line:1657
            pass #line:1658
    @staticmethod #line:1665
    def Close ():#line:1666
        global do #line:1667
        if do :#line:1668
            do =False #line:1669
            O00OOOOO00O000OOO ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1673
            OO00O000OOO0O0O00 ={1 :(O00OOOOO00O000OOO ['2'],OO000O000OO0O00O0 .MOD_ALT ),2 :(O00OOOOO00O000OOO ['3'],OO000O000OO0O00O0 .MOD_ALT ),3 :(O00OOOOO00O000OOO ['4'],OO000O000OO0O00O0 .MOD_ALT ),4 :(O00OOOOO00O000OOO ['5'],OO000O000OO0O00O0 .MOD_ALT ),5 :(O00OOOOO00O000OOO ['6'],OO000O000OO0O00O0 .MOD_ALT ),6 :(O00OOOOO00O000OOO ['7'],OO000O000OO0O00O0 .MOD_ALT ),}#line:1677
            OOO0O0OOO0OOOOO00 =O000O00OO00O0OOOO .windll .user32 #line:1678
            O000O000O0O0OOOOO ={7 :(O00OOOOO00O000OOO ['s'],0x4000 ),8 :(O00OOOOO00O000OOO ['f'],0x4000 ),9 :(O00OOOOO00O000OOO ['d'],0x4000 ),10 :(OO000O000OO0O00O0 .VK_SPACE ,0x4000 ),11 :(O00OOOOO00O000OOO ['e'],0x4000 ),12 :(OO000O000OO0O00O0 .VK_RETURN ,0x4000 ),13 :(O00OOOOO00O000OOO ['q'],0x4000 )}#line:1681
            for OO00OOOO0OO000O0O in OO00O000OOO0O0O00 .keys ():#line:1682
                OOO0O0OOO0OOOOO00 .UnregisterHotKey (None ,OO00OOOO0OO000O0O )#line:1683
            for OO00OOOO0OO000O0O in O000O000O0O0OOOOO .keys ():#line:1684
                OOO0O0OOO0OOOOO00 .UnregisterHotKey (None ,OO00OOOO0OO000O0O )#line:1685
            OOO0O0O000O0OOO00 .info ("close assistant success")#line:1686
        else :#line:1687
            pass #line:1688
    def Save_log (O00O0OOO000OO00O0 ):#line:1690
        O000O000000OOOOO0 =open ('pos.log','wb')#line:1691
        O00OOOO0O00000O0O .dump (Position ,O000O000000OOOOO0 )#line:1692
        O000O000000OOOOO0 .close ()#line:1693
    def Screen_shot (O0OO0O0O0OOOOOOOO ):#line:1698
        global Pricesize #line:1699
        OOO00OOOO0OO0OOOO =Pos_price #line:1700
        OO0OOO0O0O0O0OOOO =O000OOO00O00O00O0 .grab (OOO00OOOO0OO0OOOO )#line:1701
        OO0OOO0O0O0O0OOOO .resize (Pricesize ,OOO0OO0O000OO0O00 .ANTIALIAS ).save ("sc_new.png")#line:1702
    def Del_shot (O000O0OOO00O00OO0 ):#line:1705
        try :#line:1706
            OO0O00O0O0O0O0OOO .remove ("sc_new.png")#line:1707
        finally :#line:1708
            pass #line:1709
    def Confirmlogin (O0000O0OO0000OOOO ,OO0OOO00OOOO00OOO ):#line:1785
        Keeplogin ()#line:1786
    def Choose_time1 (O00OO0O0OO0O0OOO0 ,O00O000O0O0000O0O ):#line:1791
        O00OO0O0OO0O0OOO0 .timelabel .SetLabel ("已设定截止时间"+O00OO0O0OO0O0OOO0 .time_choice1 .GetString (O00OO0O0OO0O0OOO0 .time_choice1 .GetSelection ())+'.'+str (O00OO0O0OO0O0OOO0 .time_choice2 .GetSelection ())+" 秒")#line:1794
        global strategy1 ,strategy2 #line:1795
        strategy1 =O00OO0O0OO0O0OOO0 .time_choice1 .GetString (O00OO0O0OO0O0OOO0 .time_choice1 .GetSelection ())#line:1796
        strategy2 =O00OO0O0OO0O0OOO0 .time_choice2 .GetString (O00OO0O0OO0O0OOO0 .time_choice2 .GetSelection ())#line:1797
    def Choose_time2 (O0000000OOO00OOOO ,O00000OOOO0OO0O00 ):#line:1800
        O0000000OOO00OOOO .timelabel .SetLabel ("已设定截止时间"+O0000000OOO00OOOO .time_choice1 .GetString (O0000000OOO00OOOO .time_choice1 .GetSelection ())+'.'+str (O0000000OOO00OOOO .time_choice2 .GetSelection ())+" 秒")#line:1803
        global strategy1 ,strategy2 #line:1804
        strategy1 =O0000000OOO00OOOO .time_choice1 .GetString (O0000000OOO00OOOO .time_choice1 .GetSelection ())#line:1805
        strategy2 =O0000000OOO00OOOO .time_choice2 .GetString (O0000000OOO00OOOO .time_choice2 .GetSelection ())#line:1806
class ClockWindow (O0O0OOO0O0O0000OO .Panel ):#line:1859
    def __init__ (O00OO0O000OOO0O0O ,OOOOOOO0O00O00000 ):#line:1860
        O0O0OOO0O0O0000OO .Window .__init__ (O00OO0O000OOO0O0O ,OOOOOOO0O00O00000 ,size =Timesize )#line:1861
        O00OO0O000OOO0O0O .Bind (O0O0OOO0O0O0000OO .EVT_PAINT ,O00OO0O000OOO0O0O .OnPaint )#line:1862
        O00OO0O000OOO0O0O .timer =O0O0OOO0O0O0000OO .Timer (O00OO0O000OOO0O0O )#line:1863
        O00OO0O000OOO0O0O .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,O00OO0O000OOO0O0O .OnTimer ,O00OO0O000OOO0O0O .timer )#line:1864
        O00OO0O000OOO0O0O .timer .Start (100 )#line:1865
    def Draw (OOO00O00O00OO00OO ,OOO0000000OOO0OO0 ):#line:1867
        global a_time #line:1868
        OOO0O000O00OO0O0O =O0000000OO0OO000O .localtime (a_time )#line:1869
        O0OO0O0OOO0OOOO0O =O0000000OO0OO000O .strftime ("%H:%M:%S",OOO0O000O00OO0O0O )#line:1870
        O000O0OOOO000OO00 ,OO0OO0O00O0O0OOO0 =OOO00O00O00OO00OO .GetClientSize ()#line:1871
        OOO0000000OOO0OO0 .SetBackground (O0O0OOO0O0O0000OO .Brush (OOO00O00O00OO00OO .GetBackgroundColour ()))#line:1872
        OOO0000000OOO0OO0 .Clear ()#line:1873
        OOO0000000OOO0OO0 .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:1874
        OOOOOOOO0O00O0O0O ,O000O00O0OO0OO0OO =OOO0000000OOO0OO0 .GetTextExtent (O0OO0O0OOO0OOOO0O )#line:1875
        OOO0000000OOO0OO0 .DrawText (O0OO0O0OOO0OOOO0O ,(O000O0OOOO000OO00 -OOOOOOOO0O00O0O0O )/2 ,(OO0OO0O00O0O0OOO0 )/2 -O000O00O0OO0OO0OO /2 )#line:1876
    def Modify (OO000O000O0OO00O0 ,OO0OO0O0O0O0O0OOO ):#line:1878
        global a_time ,b_time #line:1879
        if b_time <9 :#line:1881
            b_time =b_time +1 #line:1882
        else :#line:1883
            b_time =0 #line:1884
        O00000000OOO00O0O =O0000000OO0OO000O .localtime (a_time )#line:1885
        OO0O00OOOOOO0OOO0 =O0000000OO0OO000O .strftime ("%H:%M:%S",O00000000OOO00O0O )#line:1886
        OOO0O0O0O0O00O0O0 ,O0O0OOOO0OO00OO0O =OO000O000O0OO00O0 .GetClientSize ()#line:1888
        OO0OO0O0O0O0O0OOO .SetBackground (O0O0OOO0O0O0000OO .Brush (OO000O000O0OO00O0 .GetBackgroundColour ()))#line:1889
        OO0OO0O0O0O0O0OOO .Clear ()#line:1890
        OO0OO0O0O0O0O0OOO .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:1891
        O0O000000000000O0 ,O00OOOOO00O0OO000 =OO0OO0O0O0O0O0OOO .GetTextExtent (OO0O00OOOOOO0OOO0 )#line:1892
        OO0OO0O0O0O0O0OOO .DrawText (OO0O00OOOOOO0OOO0 ,(OOO0O0O0O0O00O0O0 -O0O000000000000O0 )/2 ,(O0O0OOOO0OO00OO0O )/2 -O00OOOOO00O0OO000 /2 )#line:1893
    def OnTimer (O000OOO00OOOOOOO0 ,OOOO0OO0OO00OO0OO ):#line:1895
        O0OO0000OOO0O0O0O =O0O0OOO0O0O0000OO .BufferedDC (O0O0OOO0O0O0000OO .ClientDC (O000OOO00OOOOOOO0 ))#line:1896
        O000OOO00OOOOOOO0 .Modify (O0OO0000OOO0O0O0O )#line:1897
    def OnPaint (O0O0O0OOO00OOOOO0 ,O0O00000O00O0OO00 ):#line:1899
        O00OOO00OO00O0000 =O0O0OOO0O0O0000OO .BufferedPaintDC (O0O0O0OOO00OOOOO0 )#line:1900
        O0O0O0OOO00OOOOO0 .Draw (O00OOO00OO00O0000 )#line:1901
class TimeFrame (O0O0OOO0O0O0000OO .Frame ):#line:1905
    def __init__ (OO00O0OO0O0OOOOO0 ):#line:1906
        O0O0OOO0O0O0000OO .Frame .__init__ (OO00O0OO0O0OOOOO0 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:1908
        ClockWindow (OO00O0OO0O0OOOOO0 )#line:1911
class MoniClockWindow (O0O0OOO0O0O0000OO .Panel ):#line:1916
    def __init__ (O00OO0OO0OOOOOO00 ,O0OO000OO00O0O0OO ):#line:1917
        O0O0OOO0O0O0000OO .Window .__init__ (O00OO0OO0OOOOOO00 ,O0OO000OO00O0O0OO ,size =Timesize )#line:1918
        O00OO0OO0OOOOOO00 .Bind (O0O0OOO0O0O0000OO .EVT_PAINT ,O00OO0OO0OOOOOO00 .OnPaint )#line:1919
        O00OO0OO0OOOOOO00 .timer =O0O0OOO0O0O0000OO .Timer (O00OO0OO0OOOOOO00 )#line:1920
        O00OO0OO0OOOOOO00 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,O00OO0OO0OOOOOO00 .OnTimer ,O00OO0OO0OOOOOO00 .timer )#line:1921
        O00OO0OO0OOOOOO00 .timer .Start (100 )#line:1922
    def Draw (O00OOOO00O0O00000 ,OOO0O00OO0O0O0OO0 ):#line:1924
        global moni_second #line:1925
        O00OO0O0O00O0OO0O ="%s:%s:%s"%(11 ,29 ,moni_second )#line:1926
        OOOO0OO00OOOOO000 ,O0000OOOO0O000OO0 =O00OOOO00O0O00000 .GetClientSize ()#line:1927
        OOO0O00OO0O0O0OO0 .SetBackground (O0O0OOO0O0O0000OO .Brush (O00OOOO00O0O00000 .GetBackgroundColour ()))#line:1928
        OOO0O00OO0O0O0OO0 .Clear ()#line:1929
        OOO0O00OO0O0O0OO0 .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:1930
        O0000OO00O000O0O0 ,O0O000O00O00OOO00 =OOO0O00OO0O0O0OO0 .GetTextExtent (O00OO0O0O00O0OO0O )#line:1931
        OOO0O00OO0O0O0OO0 .DrawText (O00OO0O0O00O0OO0O ,(OOOO0OO00OOOOO000 -O0000OO00O000O0O0 )/2 ,(O0000OOOO0O000OO0 )/2 -O0O000O00O00OOO00 /2 )#line:1932
    def Modify (O000OO0OO0O000OO0 ,O00000O0OOO00O0OO ):#line:1934
        global moni_second #line:1935
        moni_second +=0.1 #line:1936
        if moni_second >=60 :#line:1937
            moni_second =0 #line:1938
        O0000OOO000OOO0OO =int (moni_second )#line:1939
        O0O0O00OOO00OO00O ="%s:%s:%s"%(11 ,29 ,O0000OOO000OOO0OO )#line:1940
        O0O0O0O000000OO00 ,O00OOO000OOO0OOO0 =O000OO0OO0O000OO0 .GetClientSize ()#line:1941
        O00000O0OOO00O0OO .SetBackground (O0O0OOO0O0O0000OO .Brush (O000OO0OO0O000OO0 .GetBackgroundColour ()))#line:1942
        O00000O0OOO00O0OO .Clear ()#line:1943
        O00000O0OOO00O0OO .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:1944
        O000OOO000000O00O ,O00O0000000OOOO00 =O00000O0OOO00O0OO .GetTextExtent (O0O0O00OOO00OO00O )#line:1945
        O00000O0OOO00O0OO .DrawText (O0O0O00OOO00OO00O ,(O0O0O0O000000OO00 -O000OOO000000O00O )/2 ,(O00OOO000OOO0OOO0 )/2 -O00O0000000OOOO00 /2 )#line:1946
    def OnTimer (OOOOOO00OOOOO00O0 ,OO000O0O0OOOO0OOO ):#line:1948
        OO00O0O000OO00OOO =O0O0OOO0O0O0000OO .BufferedDC (O0O0OOO0O0O0000OO .ClientDC (OOOOOO00OOOOO00O0 ))#line:1949
        OOOOOO00OOOOO00O0 .Modify (OO00O0O000OO00OOO )#line:1950
    def OnPaint (O0O0O0OOO00OOOO00 ,O0O0O0OO0000000OO ):#line:1952
        OOO00O0OOOO00000O =O0O0OOO0O0O0000OO .BufferedPaintDC (O0O0O0OOO00OOOO00 )#line:1953
        O0O0O0OOO00OOOO00 .Draw (OOO00O0OOOO00000O )#line:1954
class MoniTimeFrame (O0O0OOO0O0O0000OO .Frame ):#line:1958
    def __init__ (OOOOOO000OO0O0OOO ):#line:1959
        O0O0OOO0O0O0000OO .Frame .__init__ (OOOOOO000OO0O0OOO ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:1961
        MoniClockWindow (OOOOOO000OO0O0OOO )#line:1964
class PosFrame (O0O0OOO0O0O0000OO .Frame ):#line:1969
    def __init__ (OO000O0O000O00OO0 ,O000OO000000OO0O0 ,OO0000O0OO0000000 ):#line:1970
        O000O00OOOO0O0O0O ,O0OOOOO000OO000O0 =O000OO000000OO0O0 #line:1971
        O0O0OOO0O0O0000OO .Frame .__init__ (OO000O0O000O00OO0 ,None ,-1 ,'POS',pos =(O000O00OOOO0O0O0O -20 ,O0OOOOO000OO000O0 -10 ),size =(30 ,20 ),style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW )#line:1973
        OOOOOO0OOO00OOO0O =O0O0OOO0O0O0000OO .Panel (OO000O0O000O00OO0 ,-1 ,size =(30 ,20 ))#line:1974
        OOOOOOO0O0OO00O0O =O0O0OOO0O0O0000OO .Font (10 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL )#line:1976
        O0OOO000OO0OO0000 =[]#line:1977
        O0OOO000OO0OO0000 .append (O0O0OOO0O0O0000OO .StaticText (OOOOOO0OOO00OOO0O ,-1 ,OO0000O0OO0000000 ,(0 ,0 )))#line:1979
        for O000O0O0O00O00OO0 in range (len (O0OOO000OO0OO0000 )):#line:1980
            O0OOO000OO0OO0000 [O000O0O0O00O00OO0 ].SetFont (OOOOOOO0O0OO00O0O )#line:1981
class PriceFrame (O0O0OOO0O0O0000OO .Frame ):#line:1983
    def __init__ (O000OO00O00OO000O ,OO0000OO00OOOOOO0 ):#line:1984
        O0O0OOO0O0O0000OO .Frame .__init__ (O000OO00O00OO000O ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_priceframe ,style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:1987
        O000OO00O00OO000O .panel =O0O0OOO0O0O0000OO .Panel (O000OO00O00OO000O ,size =Pricesize )#line:1988
        O0O0OOO0O0O0000OO .StaticBitmap (O000OO00O00OO000O .panel ,-1 ,O0O0OOO0O0O0000OO .BitmapFromImage (OO0000OO00OOOOOO0 ))#line:1990
class YanzhengmaFrame (O0O0OOO0O0O0000OO .Frame ):#line:1992
    def __init__ (O0OOO0O000000O000 ,O0O00000000000000 ):#line:1993
        O0O0OOO0O0O0000OO .Frame .__init__ (O0OOO0O000000O000 ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_yanzhengmaframe ,style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:1996
        O0OOO0O000000O000 .panel =O0O0OOO0O0O0000OO .Panel (O0OOO0O000000O000 ,size =(400 ,80 ))#line:1997
        O0O0OOO0O0O0000OO .StaticBitmap (O0OOO0O000000O000 .panel ,-1 ,O0O0OOO0O0O0000OO .BitmapFromImage (O0O00000000000000 ))#line:1999
class AdFrame (O0O0OOO0O0O0000OO .Frame ):#line:2003
    def __init__ (OO00O0O00000OOOOO ):#line:2004
        O0O0OOO0O0O0000OO .Frame .__init__ (OO00O0O00000OOOOO ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:2006
        OOOOO0O0OOOO00OO0 =O0O0OOO0O0O0000OO .Panel (OO00O0O00000OOOOO ,-1 ,size =(250 ,200 ))#line:2007
        OO0000000OO00O0OO =O0O0OOO0O0O0000OO .Font (20 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL )#line:2009
        O000O0000OO0OOOOO =[]#line:2010
        O000O0000OO0OOOOO .append (O0O0OOO0O0O0000OO .StaticText (OOOOO0O0OOOO00OO0 ,-1 ," 专业代拍软件",(15 ,10 )))#line:2012
        O000O0000OO0OOOOO .append (O0O0OOO0O0O0000OO .StaticText (OOOOO0O0OOOO00OO0 ,-1 ," 专业代拍团队",(15 ,60 )))#line:2014
        O000O0000OO0OOOOO .append (O0O0OOO0O0O0000OO .StaticText (OOOOO0O0OOOO00OO0 ,-1 ,"关注微信公众号",(15 ,110 )))#line:2016
        O000O0000OO0OOOOO .append (O0O0OOO0O0O0000OO .StaticText (OOOOO0O0OOOO00OO0 ,-1 ," 沪牌第一枪",(15 ,160 )))#line:2018
        for OO0OO0O0OOOOO00OO in range (len (O000O0000OO0OOOOO )):#line:2019
            O000O0000OO0OOOOO [OO0OO0O0OOOOO00OO ].SetFont (OO0000000OO00O0OO )#line:2020
class WebFrame (O0O0OOO0O0O0000OO .Frame ):#line:2022
    def __init__ (OOOO000O00OOOOO0O ,O0000O0000OOO0OOO ,O00OOOOOOO000O0OO ,OO00OO000O0O00O0O ,OO00000OO0O00O0OO ):#line:2023
        O0O0OOO0O0O0000OO .Frame .__init__ (OOOO000O00OOOOO0O ,None ,-1 ,OO00000OO0O00O0OO ,size =(websize [0 ],websize [1 ]),pos =(O0000O0000OOO0OOO ,O00OOOOOOO000O0OO ))#line:2024
        if OO00OO000O0O00O0O :#line:2029
            OOOO000O00OOOOO0O .adframe =AdFrame ()#line:2030
            OOOO000O00OOOOO0O .adframe .Show (True )#line:2031
        OOOO000O00OOOOO0O .Bind (O0O0OOO0O0O0000OO .EVT_CLOSE ,OOOO000O00OOOOO0O .OnClose )#line:2032
        OOOO000O00OOOOO0O .ad2 =OO00OO000O0O00O0O #line:2033
        OOOO000O00OOOOO0O .control =ControlFrame (OO00000OO0O00O0OO )#line:2034
        OOOO000O00OOOOO0O .control .Show (True )#line:2035
        OOOO0000OO0OOO0OO .subscribe (OOOO000O00OOOOO0O .OnClose2 ,"close web")#line:2060
    def OnClose (OO0OOOO000OO000O0 ,O0OOO0O00000OO0O0 ):#line:2061
        global web_on ,view_time ,moni_on ,guopai_on ,strategy_repeat #line:2062
        web_on =False #line:2063
        view_time =False #line:2064
        moni_on =False #line:2065
        guopai_on =False #line:2066
        TopFrame .Close ()#line:2067
        O00000OOOOO0O0000 ="sc_new.png"#line:2068
        if OO0O00O0O0O0O0OOO .path .exists (O00000OOOOO0O0000 ):#line:2069
            OO0O00O0O0O0O0OOO .remove (O00000OOOOO0O0000 )#line:2070
        OO0OOOO000OO000O0 .Destroy ()#line:2071
        if OO0OOOO000OO000O0 .ad2 :#line:2072
            OO0OOOO000OO000O0 .adframe .Destroy ()#line:2073
        O0OOO0O00000OO0O0 .Skip ()#line:2074
    def OnClose2 (O0OO00O0000O00OOO ):#line:2076
        global web_on ,view_time ,moni_on ,guopai_on ,strategy_repeat #line:2077
        web_on =False #line:2078
        view_time =False #line:2079
        moni_on =False #line:2080
        guopai_on =False #line:2081
        TopFrame .Close ()#line:2082
        OO0O0O00O00000OO0 ="sc_new.png"#line:2083
        if OO0O00O0O0O0O0OOO .path .exists (OO0O0O00O00000OO0 ):#line:2084
            OO0O00O0O0O0O0OOO .remove (OO0O0O00O00000OO0 )#line:2085
        O0OO00O0000O00OOO .Destroy ()#line:2086
        if O0OO00O0000O00OOO .ad2 :#line:2087
            O0OO00O0000O00OOO .adframe .Destroy ()#line:2088
class ControlFrame (O0O0OOO0O0O0000OO .Frame ):#line:2091
    def __init__ (OOO0O0OO0OO0O00OO ,OO0OO0O0O0000OO00 ):#line:2092
        O0O0OOO0O0O0000OO .Frame .__init__ (OOO0O0OO0OO0O00OO ,None ,-1 ,size =(50 ,35 ),style =O0O0OOO0O0O0000OO .NO_BORDER |O0O0OOO0O0O0000OO .STAY_ON_TOP |O0O0OOO0O0O0000OO .FRAME_NO_TASKBAR ,pos =(Px +websize [0 ]-50 ,0 ))#line:2094
        OOO0O0OO0OO0O00OO .panel =O0O0OOO0O0O0000OO .Panel (OOO0O0OO0OO0O00OO ,-1 ,size =(50 ,35 ))#line:2095
        OOO0O0OO0OO0O00OO .button1 =O0O0OOO0O0O0000OO .Button (OOO0O0OO0OO0O00OO .panel ,pos =(0 ,0 ),size =(50 ,25 ),label ="关闭")#line:2096
        OOO0O0OO0OO0O00OO .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,OOO0O0OO0OO0O00OO .o_closeweb ,OOO0O0OO0OO0O00OO .button1 )#line:2097
    def o_closeweb (O000O0O0O00OOO00O ,OOOO000000000000O ):#line:2098
        O0O0OOO0O0O0000OO .CallAfter (OOOO0000OO0OOO0OO .sendMessage ,"close web")#line:2099
        O000O0O0O00OOO00O .Destroy ()#line:2100
        OOOO000000000000O .Skip ()#line:2101
class OperationFrame (O0O0OOO0O0O0000OO .Frame ):#line:2104
    def __init__ (O000OOOOO0O0O00O0 ):#line:2105
        O0O0OOO0O0O0000OO .Frame .__init__ (O000OOOOO0O0O00O0 ,None ,-1 ,pos =(1070 ,100 ),size =(300 ,410 ),style =O0O0OOO0O0O0000OO .FRAME_NO_TASKBAR |O0O0OOO0O0O0000OO .CAPTION )#line:2107
        global one_real_time1 ,second_real_time1 ,one_real_time2 ,second_real_time2 #line:2109
        one_real_time1 =O000OOOOO0O0O00O0 .gettime (one_time1 )#line:2110
        one_real_time2 =O000OOOOO0O0O00O0 .gettime (one_time2 )#line:2111
        second_real_time1 =O000OOOOO0O0O00O0 .gettime (second_time1 )#line:2112
        second_real_time2 =O000OOOOO0O0O00O0 .gettime (second_time2 )#line:2113
        OOOOO000OOOOO00O0 =O0O0OOO0O0O0000OO .Panel (O000OOOOO0O0O00O0 ,-1 ,size =(300 ,380 ))#line:2115
        O00O0000O00O0O000 =O0O0OOO0O0O0000OO .StaticBox (OOOOO000OOOOO00O0 ,-1 ,u'选择策略:')#line:2117
        O000OOOOO0O0O00O0 .stractagySizer =O0O0OOO0O0O0000OO .StaticBoxSizer (O00O0000O00O0O000 ,O0O0OOO0O0O0000OO .VERTICAL )#line:2118
        O0OOOOO000OO00000 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2119
        OO0OOO0O0OO0O00O0 =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2120
        OO0OOO0O0OO0O00O0 .Add (O0OOOOO000OO00000 )#line:2121
        OO000O0OOO0O000O0 =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2125
        O000OOOOO0O0O00O0 .select_stractagy =O0O0OOO0O0O0000OO .Choice (OOOOO000OOOOO00O0 ,-1 ,choices =OO000O0OOO0O000O0 ,size =(100 ,50 ))#line:2126
        OO0OOO0O0OO0O00O0 .Add (O000OOOOO0O0O00O0 .select_stractagy )#line:2127
        O000OOOOO0O0O00O0 .select_stractagy .SetSelection (0 )#line:2128
        O000OOOOO0O0O00O0 .timeview =O0O0OOO0O0O0000OO .CheckBox (OOOOO000OOOOO00O0 ,-1 ,label =u'显示时间')#line:2130
        OOOO0O00O0000O0OO =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2131
        OOOO0O00O0000O0OO .Add (O000OOOOO0O0O00O0 .timeview )#line:2132
        O000OOOOO0O0O00O0 .button1 =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ='+1s',size =(35 ,25 ))#line:2135
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Add_second ,O000OOOOO0O0O00O0 .button1 )#line:2136
        O000OOOOO0O0O00O0 .button2 =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ='-1s',size =(35 ,25 ))#line:2137
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Minus_second ,O000OOOOO0O0O00O0 .button2 )#line:2138
        O000OOOOO0O0O00O0 .button3 =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ='+0.1s',size =(35 ,25 ))#line:2139
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Add_time ,O000OOOOO0O0O00O0 .button3 )#line:2140
        O000OOOOO0O0O00O0 .button4 =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ='-0.1s',size =(35 ,25 ))#line:2141
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Minus_time ,O000OOOOO0O0O00O0 .button4 )#line:2142
        OOOO0O00O0000O0OO .Add (O000OOOOO0O0O00O0 .button1 )#line:2144
        OOOO0O00O0000O0OO .Add (O000OOOOO0O0O00O0 .button2 )#line:2145
        OOOO0O00O0000O0OO .Add (O000OOOOO0O0O00O0 .button3 )#line:2146
        OOOO0O00O0000O0OO .Add (O000OOOOO0O0O00O0 .button4 )#line:2147
        O00000OO0OOO0O00O =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .VERTICAL )#line:2149
        O00000OO0OOO0O00O .Add (OO0OOO0O0OO0O00O0 )#line:2150
        O00000OO0OOO0O00O .Add (OOOO0O00O0000O0OO )#line:2151
        OOO0OOOOOOO000OO0 =["E键","回车"]#line:2154
        O000OOOOO0O0O00O0 .confirm_choice =O0O0OOO0O0O0000OO .Choice (OOOOO000OOOOO00O0 ,-1 ,choices =OOO0OOOOOOO000OO0 )#line:2155
        O000OOOOO0O0O00O0 .confirm_choice .SetSelection (0 )#line:2156
        O000OOOOO0O0O00O0 .confirm_label =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"确认提交方式     ")#line:2157
        OO00O0OOOO000OO0O =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2158
        OO00O0OOOO000OO0O .Add (O000OOOOO0O0O00O0 .confirm_label ,flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2159
        OO00O0OOOO000OO0O .Add (O000OOOOO0O0O00O0 .confirm_choice )#line:2160
        O00000OO0OOO0O00O .Add (OO00O0OOOO000OO0O )#line:2161
        O000OOOOO0O0O00O0 .strategy_save =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ="保存策略",size =(60 ,35 ))#line:2164
        O000OOOOO0O0O00O0 .strategy_load =O0O0OOO0O0O0000OO .Button (OOOOO000OOOOO00O0 ,label ="载入策略",size =(60 ,35 ))#line:2165
        O0O000OO00O0O0O00 =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2166
        O0O000OO00O0O0O00 .Add (O000OOOOO0O0O00O0 .strategy_save )#line:2167
        O0O000OO00O0O0O00 .Add (O000OOOOO0O0O00O0 .strategy_load )#line:2168
        O00000OO0OOO0O00O .Add (O0O000OO00O0O0O00 )#line:2169
        O0OO00OOO00OOOO00 =O0O0OOO0O0O0000OO .StaticBox (OOOOO000OOOOO00O0 ,-1 ,u'单枪策略:')#line:2173
        O000OOOOO0O0O00O0 .oneshotSizer =O0O0OOO0O0O0000OO .StaticBoxSizer (O0OO00OOO00OOOO00 ,O0O0OOO0O0O0000OO .VERTICAL )#line:2174
        O0OOO0000O0OO0OOO =O0O0OOO0O0O0000OO .GridBagSizer (4 ,4 )#line:2175
        O000OOOOO0O0O00O0 .jiajia_time =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2176
        O000OOOOO0O0O00O0 .jiajia_time .SetRange (40 ,55 )#line:2177
        O000OOOOO0O0O00O0 .jiajia_time .SetValue (48 )#line:2178
        O000OOOOO0O0O00O0 .jiajia_time .SetIncrement (0.1 )#line:2179
        O0OOO0000O0OO0OOO .Add (O000OOOOO0O0O00O0 .jiajia_time ,pos =(0 ,0 ))#line:2181
        O0OOOOO00OO0O000O =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2182
        O0OOO0000O0OO0OOO .Add (O0OOOOO00OO0O000O ,pos =(0 ,1 ),flag =O0O0OOO0O0O0000OO .TOP |O0O0OOO0O0O0000OO .ALIGN_LEFT ,border =4 )#line:2183
        O0OOOO0O000OOO0OO =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"加价",style =O0O0OOO0O0O0000OO .ALIGN_CENTER ,size =(25 ,25 ))#line:2184
        O0OOO0000O0OO0OOO .Add (O0OOOO0O000OOO0OO ,pos =(0 ,2 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2185
        O000OOOOO0O0O00O0 .jiajia_price =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2186
        O000OOOOO0O0O00O0 .jiajia_price .SetRange (300 ,1500 )#line:2187
        O000OOOOO0O0O00O0 .jiajia_price .SetValue (700 )#line:2188
        O000OOOOO0O0O00O0 .jiajia_price .SetIncrement (100 )#line:2189
        O0OOO0000O0OO0OOO .Add (O000OOOOO0O0O00O0 .jiajia_price ,pos =(0 ,3 ))#line:2190
        OOOOOO0O00OO0OO00 =[u"提前100",u"提前200",u"踩点"]#line:2193
        O000OOOOO0O0O00O0 .select_tijiao =O0O0OOO0O0O0000OO .Choice (OOOOO000OOOOO00O0 ,-1 ,choices =OOOOOO0O00OO0OO00 ,size =(68 ,25 ))#line:2194
        O000OOOOO0O0O00O0 .select_tijiao .SetSelection (0 )#line:2195
        O0OOO0000O0OO0OOO .Add (O000OOOOO0O0O00O0 .select_tijiao ,pos =(1 ,0 ))#line:2196
        OO0O000OOO00000OO =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"出价提交延迟")#line:2197
        O0OOO0000O0OO0OOO .Add (OO0O000OOO00000OO ,pos =(1 ,1 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2198
        O000OOOOO0O0O00O0 .yanchi_time =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2199
        O000OOOOO0O0O00O0 .yanchi_time .SetRange (0.0 ,1.0 )#line:2200
        O000OOOOO0O0O00O0 .yanchi_time .SetValue (0.5 )#line:2201
        O000OOOOO0O0O00O0 .yanchi_time .SetIncrement (0.1 )#line:2202
        O0OOO0000O0OO0OOO .Add (O000OOOOO0O0O00O0 .yanchi_time ,pos =(1 ,3 ))#line:2203
        O000000OOOOOO0O0O =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2204
        O0OOO0000O0OO0OOO .Add (O000000OOOOOO0O0O ,pos =(1 ,4 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2205
        O0OOO000OOOO0O000 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"强制提交时间")#line:2208
        O0OOO0000O0OO0OOO .Add (O0OOO000OOOO0O000 ,pos =(2 ,0 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2209
        O000OOOOO0O0O00O0 .tijiao_time =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2210
        O000OOOOO0O0O00O0 .tijiao_time .SetRange (40.0 ,57.0 )#line:2211
        O000OOOOO0O0O00O0 .tijiao_time .SetValue (55.0 )#line:2212
        O000OOOOO0O0O00O0 .tijiao_time .SetIncrement (0.1 )#line:2213
        O0OOO0000O0OO0OOO .Add (O000OOOOO0O0O00O0 .tijiao_time ,pos =(2 ,1 ))#line:2214
        O00OO00OO000OO000 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2215
        O0OOO0000O0OO0OOO .Add (O00OO00OO000OO000 ,pos =(2 ,2 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2216
        O000OOOOO0O0O00O0 .oneshotSizer .Add (O0OOO0000O0OO0OOO ,0 ,flag =O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2218
        OO000O0OO00OOOOO0 =O0O0OOO0O0O0000OO .StaticBox (OOOOO000OOOOO00O0 ,-1 ,u'双枪策略:')#line:2222
        O000OOOOO0O0O00O0 .secondshotSizer =O0O0OOO0O0O0000OO .StaticBoxSizer (OO000O0OO00OOOOO0 ,O0O0OOO0O0O0000OO .VERTICAL )#line:2223
        OOOO00OO0O000O0OO =O0O0OOO0O0O0000OO .GridBagSizer (4 ,4 )#line:2224
        O000OOOOO0O0O00O0 .jiajia_time2 =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2225
        O000OOOOO0O0O00O0 .jiajia_time2 .SetRange (40 ,55 )#line:2226
        O000OOOOO0O0O00O0 .jiajia_time2 .SetValue (48 )#line:2227
        O000OOOOO0O0O00O0 .jiajia_time2 .SetIncrement (0.1 )#line:2228
        OOOO00OO0O000O0OO .Add (O000OOOOO0O0O00O0 .jiajia_time2 ,pos =(0 ,0 ))#line:2229
        OO00OOO00O0O0OO00 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2230
        OOOO00OO0O000O0OO .Add (OO00OOO00O0O0OO00 ,pos =(0 ,1 ),flag =O0O0OOO0O0O0000OO .TOP |O0O0OOO0O0O0000OO .ALIGN_LEFT ,border =4 )#line:2231
        OO0OO00OOO000OO00 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"加价",size =(25 ,25 ),style =O0O0OOO0O0O0000OO .ALIGN_CENTER )#line:2232
        OOOO00OO0O000O0OO .Add (OO0OO00OOO000OO00 ,pos =(0 ,2 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2233
        O000OOOOO0O0O00O0 .jiajia_price2 =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2234
        O000OOOOO0O0O00O0 .jiajia_price2 .SetRange (300 ,1500 )#line:2235
        O000OOOOO0O0O00O0 .jiajia_price2 .SetValue (600 )#line:2236
        O000OOOOO0O0O00O0 .jiajia_price2 .SetIncrement (100 )#line:2237
        OOOO00OO0O000O0OO .Add (O000OOOOO0O0O00O0 .jiajia_price2 ,pos =(0 ,3 ))#line:2238
        O000000O000O00000 =[u"提前100",u"提前200",u"踩点"]#line:2240
        O000OOOOO0O0O00O0 .select_tijiao2 =O0O0OOO0O0O0000OO .Choice (OOOOO000OOOOO00O0 ,-1 ,choices =O000000O000O00000 ,size =(68 ,25 ))#line:2241
        O000OOOOO0O0O00O0 .select_tijiao2 .SetSelection (0 )#line:2242
        OOOO00OO0O000O0OO .Add (O000OOOOO0O0O00O0 .select_tijiao2 ,pos =(1 ,0 ))#line:2243
        O00O000OO000O00O0 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"出价提交延迟")#line:2244
        OOOO00OO0O000O0OO .Add (O00O000OO000O00O0 ,pos =(1 ,1 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2245
        O000OOOOO0O0O00O0 .yanchi_time2 =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2246
        O000OOOOO0O0O00O0 .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2247
        O000OOOOO0O0O00O0 .yanchi_time2 .SetValue (0.5 )#line:2248
        O000OOOOO0O0O00O0 .yanchi_time2 .SetIncrement (0.1 )#line:2249
        OOOO00OO0O000O0OO .Add (O000OOOOO0O0O00O0 .yanchi_time2 ,pos =(1 ,3 ))#line:2250
        O0OOO0OO0OO00O00O =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2251
        OOOO00OO0O000O0OO .Add (O0OOO0OO0OO00O00O ,pos =(1 ,4 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2252
        O0O00OO0OOO0O0000 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"强制提交时间")#line:2255
        OOOO00OO0O000O0OO .Add (O0O00OO0OOO0O0000 ,pos =(2 ,0 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2256
        O000OOOOO0O0O00O0 .tijiao_time2 =O0O0OOO0O0O0000OO .SpinCtrlDouble (OOOOO000OOOOO00O0 ,-1 ,"",size =(68 ,25 ))#line:2257
        O000OOOOO0O0O00O0 .tijiao_time2 .SetRange (53.0 ,57.0 )#line:2258
        O000OOOOO0O0O00O0 .tijiao_time2 .SetValue (55.0 )#line:2259
        O000OOOOO0O0O00O0 .tijiao_time2 .SetIncrement (0.1 )#line:2260
        OOOO00OO0O000O0OO .Add (O000OOOOO0O0O00O0 .tijiao_time2 ,pos =(2 ,1 ))#line:2261
        OOOO0O00O0OO0OO00 =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,label =u"秒")#line:2262
        OOOO00OO0O000O0OO .Add (OOOO0O00O0OO0OO00 ,pos =(2 ,2 ),flag =O0O0OOO0O0O0000OO .TOP ,border =4 )#line:2263
        O000OOOOO0O0O00O0 .secondshotSizer .Add (OOOO00OO0O000O0OO ,0 ,flag =O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2265
        O000OOOOO0O0O00O0 .stractagySizer .Add (O00000OO0OOO0O00O ,0 ,O0O0OOO0O0O0000OO .ALL |O0O0OOO0O0O0000OO .CENTER ,5 )#line:2267
        O000OOOOO0O0O00O0 .vbox1 =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .VERTICAL )#line:2268
        OO0000O00O0OOO00O =O0O0OOO0O0O0000OO .StaticText (OOOOO000OOOOO00O0 ,-1 ,label =u"拍牌功能设置")#line:2271
        OOOO00O000O0O00OO =O0O0OOO0O0O0000OO .StaticLine (OOOOO000OOOOO00O0 ,-1 )#line:2272
        O000OOOOO0O0O00O0 .vbox1 .Add (OO0000O00O0OOO00O ,0 ,O0O0OOO0O0O0000OO .ALL |O0O0OOO0O0O0000OO .LEFT ,10 )#line:2273
        O000OOOOO0O0O00O0 .vbox1 .Add (OOOO00O000O0O00OO ,flag =O0O0OOO0O0O0000OO .EXPAND |O0O0OOO0O0O0000OO .BOTTOM ,border =10 )#line:2274
        O000OOOOO0O0O00O0 .vbox1 .Add (O000OOOOO0O0O00O0 .stractagySizer ,0 ,O0O0OOO0O0O0000OO .ALL |O0O0OOO0O0O0000OO .CENTER ,5 )#line:2275
        O000OOOOO0O0O00O0 .vbox1 .Add (O000OOOOO0O0O00O0 .oneshotSizer ,0 ,O0O0OOO0O0O0000OO .ALL |O0O0OOO0O0O0000OO .CENTER ,5 )#line:2276
        O000OOOOO0O0O00O0 .vbox1 .Add (O000OOOOO0O0O00O0 .secondshotSizer ,0 ,O0O0OOO0O0O0000OO .ALL |O0O0OOO0O0O0000OO .CENTER ,5 )#line:2277
        OOOOO000OOOOO00O0 .SetSizer (O000OOOOO0O0O00O0 .vbox1 )#line:2278
        O000OOOOO0O0O00O0 .secondsizer_Shown =False #line:2281
        O000OOOOO0O0O00O0 .oneshotsizer_Shown =True #line:2282
        O000OOOOO0O0O00O0 .vbox1 .Hide (O000OOOOO0O0O00O0 .secondshotSizer )#line:2283
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CHECKBOX ,O000OOOOO0O0O00O0 .Timeview ,O000OOOOO0O0O00O0 .timeview )#line:2292
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CHOICE ,O000OOOOO0O0O00O0 .Confirmchoice ,O000OOOOO0O0O00O0 .confirm_choice )#line:2293
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Strategy_save ,O000OOOOO0O0O00O0 .strategy_save )#line:2294
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O000OOOOO0O0O00O0 .Strategy_load ,O000OOOOO0O0O00O0 .strategy_load )#line:2295
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CHOICE ,O000OOOOO0O0O00O0 .Refresh_panel ,O000OOOOO0O0O00O0 .select_stractagy )#line:2297
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Jiajia_time ,O000OOOOO0O0O00O0 .jiajia_time )#line:2299
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Jiajia_price ,O000OOOOO0O0O00O0 .jiajia_price )#line:2301
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CHOICE ,O000OOOOO0O0O00O0 .Select_tijiao ,O000OOOOO0O0O00O0 .select_tijiao )#line:2302
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Yanchi_time ,O000OOOOO0O0O00O0 .yanchi_time )#line:2304
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Tijiao_time ,O000OOOOO0O0O00O0 .tijiao_time )#line:2306
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Jiajia_time2 ,O000OOOOO0O0O00O0 .jiajia_time2 )#line:2309
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Jiajia_price2 ,O000OOOOO0O0O00O0 .jiajia_price2 )#line:2311
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_CHOICE ,O000OOOOO0O0O00O0 .Select_tijiao2 ,O000OOOOO0O0O00O0 .select_tijiao2 )#line:2312
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Yanchi_time2 ,O000OOOOO0O0O00O0 .yanchi_time2 )#line:2314
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT ,O000OOOOO0O0O00O0 .Tijiao_time2 ,O000OOOOO0O0O00O0 .tijiao_time2 )#line:2316
        O000OOOOO0O0O00O0 .timeframe1 =TimeFrame ()#line:2318
        O000OOOOO0O0O00O0 .timeframe1 .Show (False )#line:2319
        O000OOOOO0O0O00O0 .timeframe2 =MoniTimeFrame ()#line:2321
        O000OOOOO0O0O00O0 .timeframe2 .Show (False )#line:2322
        O000OOOOO0O0O00O0 .operationtimer =O0O0OOO0O0O0000OO .Timer (O000OOOOO0O0O00O0 )#line:2325
        O000OOOOO0O0O00O0 .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,O000OOOOO0O0O00O0 .opt ,O000OOOOO0O0O00O0 .operationtimer )#line:2326
        O000OOOOO0O0O00O0 .operationtimer .Start (3000 )#line:2327
    def opt (OO0O0OOOOOOO000OO ,O0O0O00OOO0O00O0O ):#line:2328
        global tijiao_num ,tijiao_one ,chujia_on #line:2329
        global strategy_on #line:2330
        global twice ,tijiao_num ,chujia_on ,tijiao_on ,tijiao_OK ,tijiao_one #line:2331
        if OO0O0OOOOOOO000OO .select_stractagy .GetSelection ==0 :#line:2332
            if moni_second <one_time1 and moni_on :#line:2333
                print ("触发1")#line:2334
                twice =False #line:2335
                strategy_on =True #line:2336
                chujia_on =True #line:2337
                tijiao_on =False #line:2338
                tijiao_num =1 #line:2339
                tijiao_OK =False #line:2340
                tijiao_one =False #line:2341
        elif OO0O0OOOOOOO000OO .select_stractagy .GetSelection ==1 :#line:2342
            if moni_second <one_time1 and moni_on :#line:2343
                print ("触发2")#line:2344
                strategy_on =True #line:2345
                twice =True #line:2346
                chujia_on =True #line:2347
                tijiao_on =False #line:2348
                tijiao_num =1 #line:2349
                tijiao_OK =False #line:2350
                tijiao_one =False #line:2351
    def Add_time (OO0000O00O0OOO000 ,O0O0000OOO0000OOO ):#line:2355
        global a_time ,moni_second ,moni_on ,guopai_on #line:2356
        if moni_on :#line:2357
            moni_second +=0.1 #line:2358
        else :#line:2359
            a_time +=0.1 #line:2360
    def Minus_time (OO000OO0OOO00OO00 ,O00O0O0OOO00OO0O0 ):#line:2362
        global a_time ,moni_second ,moni_on ,guopai_on #line:2363
        if moni_on :#line:2364
            moni_second -=0.1 #line:2365
        else :#line:2366
            a_time -=0.1 #line:2367
    def Add_second (O000OO0OO0OOOOO0O ,O00O0000OOO0OOOOO ):#line:2369
        global a_time ,moni_second ,moni_on ,guopai_on #line:2370
        if moni_on :#line:2371
            moni_second +=1 #line:2372
            if moni_second >=60 :#line:2373
                moni_second =0 #line:2374
        else :#line:2375
            a_time +=1 #line:2376
    def Minus_second (OO0000O00OOO00000 ,OOOOO00O0O0000OOO ):#line:2378
        global a_time ,moni_second ,moni_on ,guopai_on #line:2379
        if moni_on :#line:2380
            moni_second -=1 #line:2381
            if moni_second <=0 :#line:2382
                moni_second =60 #line:2383
        else :#line:2384
            a_time -=1 #line:2385
    def Timeview (O0O00O0O0O00OO0OO ,OOO000O0OOO00OOO0 ):#line:2387
        OO0O0OOOO0OOO00OO =OOO000O0OOO00OOO0 .GetEventObject ()#line:2388
        global view_time ,time_on #line:2389
        if OO0O0OOOO0OOO00OO .IsChecked ():#line:2390
            view_time =True #line:2391
            time_on =True #line:2392
            if guopai_on :#line:2393
                O0O00O0O0O00OO0OO .timeframe1 .Show (True )#line:2394
            elif moni_on :#line:2395
                O0O00O0O0O00OO0OO .timeframe2 .Show (True )#line:2396
        else :#line:2397
            view_time =False #line:2398
            time_on =False #line:2399
            if guopai_on :#line:2400
                O0O00O0O0O00OO0OO .timeframe1 .Show (False )#line:2401
            elif moni_on :#line:2402
                O0O00O0O0O00OO0OO .timeframe2 .Show (False )#line:2403
    def Opentime (O0O0OO0OO0OO00O0O ):#line:2405
        if moni_on :#line:2406
            try :#line:2407
                O0O0OO0OO0OO00O0O .timeframe2 .Show (True )#line:2408
            except :#line:2409
                pass #line:2410
        elif guopai_on :#line:2411
            try :#line:2412
                O0O0OO0OO0OO00O0O .timeframe1 .Show (True )#line:2413
            except :#line:2414
                pass #line:2415
    def Closetime (OOO0O0OO000OO00OO ):#line:2418
        try :#line:2419
            OOO0O0OO000OO00OO .timeframe1 .Show (False )#line:2420
        except :#line:2421
            pass #line:2422
        try :#line:2423
            OOO0O0OO000OO00OO .timeframe2 .Show (False )#line:2424
        except :#line:2425
            pass #line:2426
    def Confirmchoice (O000OOOOO0OO000OO ,OO00OOO000O00O00O ):#line:2428
        global e_on ,enter_on #line:2429
        OO000O000000OOO00 =O000OOOOO0OO000OO .confirm_choice .GetSelection ()#line:2430
        if OO000O000000OOO00 ==0 :#line:2431
            e_on =True #line:2432
            enter_on =False #line:2433
        elif OO000O000000OOO00 ==1 :#line:2434
            e_on =False #line:2435
            enter_on =True #line:2436
    def Jiajia_time (O000000OOOO0000O0 ,OO0OOO000OOO0O000 ):#line:2440
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 ,one_real_time1 ,one_real_time2 #line:2441
        O00O00OOOOO0000OO =O000000OOOO0000O0 .jiajia_time .GetValue ()#line:2442
        O00OOOOOO00OOOOOO =[40 +O0OOO0O0OOOO00OO0 *0.1 for O0OOO0O0OOOO00OO0 in range (151 )]#line:2443
        if O00O00OOOOO0000OO in O00OOOOOO00OOOOOO :#line:2444
            one_time1 =O00O00OOOOO0000OO #line:2445
            one_time1 =float (one_time1 )#line:2446
            one_real_time1 =O000000OOOO0000O0 .gettime (one_time1 )#line:2447
        else :#line:2448
            O000000OOOO0000O0 .jiajia_time .SetValue (one_time1 )#line:2449
    def Jiajia_price (O00O0O000O00O0000 ,OOO0OO0O0OO00O00O ):#line:2452
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 #line:2453
        OO0OO000O00OOOOOO =[300 +O000000O0OO0000OO *100 for O000000O0OO0000OO in range (13 )]#line:2454
        O0O00O00OOOO00O0O =O00O0O000O00O0000 .jiajia_price .GetValue ()#line:2455
        if O0O00O00OOOO00O0O in OO0OO000O00OOOOOO :#line:2456
            one_diff =int (O0O00O00OOOO00O0O )#line:2457
        else :#line:2458
            O00O0O000O00O0000 .jiajia_price .SetValue (one_diff )#line:2459
    def Select_tijiao (O00O0000O0OOOO000 ,OOOOO00000OOO0O00 ):#line:2462
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 #line:2463
        O0O0O000OOOOO00O0 =O00O0000O0OOOO000 .select_tijiao .GetString (O00O0000O0OOOO000 .select_tijiao .GetSelection ())#line:2464
        if O0O0O000OOOOO00O0 ==u"提前100":#line:2465
            one_advance =100 #line:2466
        elif O0O0O000OOOOO00O0 ==u"提前200":#line:2467
            one_advance =200 #line:2468
        else :#line:2469
            one_advance =0 #line:2470
    def Yanchi_time (O00OOO00O0OOO00OO ,O0OOOOOO0OO00O000 ):#line:2472
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 #line:2473
        OO0OO000000OO00O0 =['0.%d'%OO0O0O0OO00OOOO0O for OO0O0O0OO00OOOO0O in range (11 )]#line:2474
        OO0OO000000OO00O0 .append ('1.0')#line:2475
        O00OOOO0OOOOO0O0O =str (O00OOO00O0OOO00OO .yanchi_time .GetValue ())#line:2476
        if O00OOOO0OOOOO0O0O in OO0OO000000OO00O0 :#line:2477
            one_delay =float (O00OOOO0OOOOO0O0O )#line:2478
        else :#line:2479
            O00OOO00O0OOO00OO .yanchi_time .SetValue (one_delay )#line:2480
    def Tijiao_time (OO0O0OOOOO0000OOO ,O000OO0000O000O0O ):#line:2482
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 ,one_real_time2 #line:2483
        O00O0O0O00OO00O00 =OO0O0OOOOO0000OOO .tijiao_time .GetValue ()#line:2484
        O0OOO0OOO0O0OO00O =[40 +OOOO0000O0O0O0O0O *0.1 for OOOO0000O0O0O0O0O in range (171 )]#line:2485
        if O00O0O0O00OO00O00 in O0OOO0OOO0O0OO00O :#line:2486
            one_time2 =float (O00O0O0O00OO00O00 )#line:2487
            one_real_time2 =OO0O0OOOOO0000OOO .gettime (one_time2 )#line:2488
        else :#line:2489
            OO0O0OOOOO0000OOO .tijiao_time .SetValue (one_time2 )#line:2490
    def Jiajia_time2 (O0O0OOO00000O0OO0 ,O00O0000O000O0000 ):#line:2492
        global second_advance ,second_delay ,second_diff ,second_time1 ,second_time2 ,second_real_time1 #line:2493
        O000O000O0O0OOO00 =O0O0OOO00000O0OO0 .jiajia_time2 .GetValue ()#line:2494
        OO0O0O0OOO00OOOO0 =[40 +O0000OOOO0OO0O0OO *0.1 for O0000OOOO0OO0O0OO in range (151 )]#line:2495
        if O000O000O0O0OOO00 in OO0O0O0OOO00OOOO0 :#line:2496
            second_time1 =float (O000O000O0O0OOO00 )#line:2497
            second_real_time1 =O0O0OOO00000O0OO0 .gettime (second_time1 )#line:2498
        else :#line:2499
            O0O0OOO00000O0OO0 .jiajia_time2 .SetValue (second_time1 )#line:2500
    def Jiajia_price2 (OOO0OOO00O00000OO ,OO00OOO0OO0O0O0O0 ):#line:2502
        global second_advance ,second_delay ,second_diff ,second_time1 ,second_time2 #line:2503
        global one_advance ,one_delay ,one_diff ,one_time1 ,one_time2 #line:2504
        OOO00OO000OO00OO0 =[300 +O0OO0O0O0O0O00000 *100 for O0OO0O0O0O0O00000 in range (13 )]#line:2505
        O0000O0OO0O0OO0OO =OOO0OOO00O00000OO .jiajia_price2 .GetValue ()#line:2506
        if O0000O0OO0O0OO0OO in OOO00OO000OO00OO0 :#line:2507
            second_diff =int (O0000O0OO0O0OO0OO )#line:2508
        else :#line:2509
            OOO0OOO00O00000OO .jiajia_price2 .SetValue (second_diff )#line:2510
    def Select_tijiao2 (OOOOO00O000O0000O ,OOOOOOOOOO00O0O00 ):#line:2512
        global second_advance ,second_delay ,second_diff ,second_time1 ,second_time2 #line:2513
        O0O000OOOOOOO0OOO =OOOOO00O000O0000O .select_tijiao2 .GetString (OOOOO00O000O0000O .select_tijiao2 .GetSelection ())#line:2514
        if O0O000OOOOOOO0OOO ==u"提前100":#line:2515
            second_advance =100 #line:2516
        elif O0O000OOOOOOO0OOO ==u"提前200":#line:2517
            second_advance =200 #line:2518
        else :#line:2519
            second_advance =0 #line:2520
    def Yanchi_time2 (OO00O00OO0000000O ,OOOOO0O0O0O0O0O0O ):#line:2523
        global second_advance ,second_delay ,second_diff ,second_time1 ,second_time2 #line:2524
        O000000O000O0O000 =['0.%d'%OO00O0OO00OO000O0 for OO00O0OO00OO000O0 in range (11 )]#line:2525
        O000000O000O0O000 .append ('1.0')#line:2526
        OOOOOO000O0O000OO =str (OO00O00OO0000000O .yanchi_time2 .GetValue ())#line:2527
        if OOOOOO000O0O000OO in O000000O000O0O000 :#line:2528
            second_delay =float (OOOOOO000O0O000OO )#line:2529
        else :#line:2530
            OO00O00OO0000000O .yanchi_time2 .SetValue (second_delay )#line:2531
    def Tijiao_time2 (OO0OOO00OO00OO0O0 ,OOOO00O0O00OO0O0O ):#line:2534
        global second_advance ,second_delay ,second_diff ,second_time1 ,second_time2 ,second_real_time2 #line:2535
        OO0OOOOOOO0OOOO0O =OO0OOO00OO00OO0O0 .tijiao_time2 .GetValue ()#line:2536
        O0O00O0O0O0OOO0OO =[53 +OOO00O000OO0O000O *0.1 for OOO00O000OO0O000O in range (41 )]#line:2537
        if OO0OOOOOOO0OOOO0O in O0O00O0O0O0OOO0OO :#line:2538
            second_time2 =float (OO0OOOOOOO0OOOO0O )#line:2539
            second_real_time2 =OO0OOO00OO00OO0O0 .gettime (second_time2 )#line:2540
        else :#line:2541
            OO0OOO00OO00OO0O0 .tijiao_time2 .SetValue (second_time2 )#line:2542
    def Refresh_panel (O0O0OO0OO00O00O00 ,O0OOO000O0OO0O0OO ):#line:2546
        global strategy_on #line:2548
        global twice ,tijiao_num ,chujia_on ,tijiao_on ,tijiao_OK ,tijiao_one #line:2549
        OO0O0000OOOOO00OO =O0O0OO0OO00O00O00 .select_stractagy .GetString (O0O0OO0OO00O00O00 .select_stractagy .GetSelection ())#line:2550
        if OO0O0000OOOOO00OO ==u"单枪策略":#line:2551
            O0O0OO0OO00O00O00 .ss_Hide ()#line:2552
            twice =False #line:2553
            strategy_on =True #line:2554
            chujia_on =True #line:2555
            tijiao_on =False #line:2556
            tijiao_num =1 #line:2557
            tijiao_OK =False #line:2558
            tijiao_one =False #line:2559
        elif OO0O0000OOOOO00OO ==u"双枪策略":#line:2561
            O0O0OO0OO00O00O00 .ss_Shown ()#line:2562
            strategy_on =True #line:2563
            twice =True #line:2564
            chujia_on =True #line:2565
            tijiao_on =False #line:2566
            tijiao_num =1 #line:2567
            tijiao_OK =False #line:2568
            tijiao_one =False #line:2569
        else :#line:2570
            O0O0OO0OO00O00O00 .none_show ()#line:2571
            strategy_on =False #line:2572
            twice =False #line:2573
    def ss_Shown (O0O00O0O00O00OOO0 ):#line:2576
        if not O0O00O0O00O00OOO0 .secondsizer_Shown :#line:2577
            O0O00O0O00O00OOO0 .vbox1 .Show (O0O00O0O00O00OOO0 .secondshotSizer )#line:2578
            O0O00O0O00O00OOO0 .secondsizer_Shown =True #line:2579
        if not O0O00O0O00O00OOO0 .oneshotsizer_Shown :#line:2580
            O0O00O0O00O00OOO0 .vbox1 .Show (O0O00O0O00O00OOO0 .oneshotSizer )#line:2581
            O0O00O0O00O00OOO0 .oneshotsizer_Shown =True #line:2582
        O0O00O0O00O00OOO0 .secondsizer_Shown =True #line:2583
        O0O00O0O00O00OOO0 .oneshotSizer_Shown =True #line:2584
        O0O00O0O00O00OOO0 .SetClientSize ((280 ,560 ))#line:2585
        O0O00O0O00O00OOO0 .Secondshot_reset ()#line:2586
        O0O00O0O00O00OOO0 .Layout ()#line:2587
    def ss_Hide (O00O0OOOO00OOO00O ):#line:2589
        if O00O0OOOO00OOO00O .secondsizer_Shown :#line:2590
            O00O0OOOO00OOO00O .vbox1 .Hide (O00O0OOOO00OOO00O .secondshotSizer )#line:2591
        if not O00O0OOOO00OOO00O .oneshotsizer_Shown :#line:2594
            O00O0OOOO00OOO00O .vbox1 .Show (O00O0OOOO00OOO00O .oneshotSizer )#line:2595
        O00O0OOOO00OOO00O .secondsizer_Shown =False #line:2596
        O00O0OOOO00OOO00O .oneshotSizer_Shown =True #line:2597
        O00O0OOOO00OOO00O .SetClientSize ((280 ,360 ))#line:2598
        O00O0OOOO00OOO00O .Oneshot_reset ()#line:2599
        O00O0OOOO00OOO00O .Layout ()#line:2600
    def none_show (OOOOO0OOOOOO0OOO0 ):#line:2602
        if OOOOO0OOOOOO0OOO0 .oneshotsizer_Shown :#line:2603
            OOOOO0OOOOOO0OOO0 .vbox1 .Hide (OOOOO0OOOOOO0OOO0 .secondshotSizer )#line:2604
        if OOOOO0OOOOOO0OOO0 .secondsizer_Shown :#line:2605
            OOOOO0OOOOOO0OOO0 .vbox1 .Hide (OOOOO0OOOOOO0OOO0 .oneshotSizer )#line:2606
        OOOOO0OOOOOO0OOO0 .oneshotsizer_Shown =False #line:2608
        OOOOO0OOOOOO0OOO0 .secondsizer_Shown =False #line:2609
        OOOOO0OOOOOO0OOO0 .SetClientSize ((280 ,240 ))#line:2610
        OOOOO0OOOOOO0OOO0 .Layout ()#line:2611
    def Oneshot_reset (OOO000OO0O0OOOOO0 ):#line:2613
        global one_time1 ,one_time2 ,one_diff ,one_delay ,one_advance #line:2614
        OOO000OO0O0OOOOO0 .jiajia_time .SetValue (48.0 )#line:2615
        OOO000OO0O0OOOOO0 .tijiao_time .SetValue (55.0 )#line:2616
        OOO000OO0O0OOOOO0 .jiajia_price .SetValue (700 )#line:2617
        OOO000OO0O0OOOOO0 .select_tijiao .SetSelection (0 )#line:2618
        OOO000OO0O0OOOOO0 .yanchi_time .SetValue (0.5 )#line:2619
        one_time1 =48 #line:2621
        one_time2 =55 #line:2622
        one_diff =700 #line:2623
        one_delay =0.5 #line:2624
        one_advance =100 #line:2625
        global one_real_time1 ,second_real_time1 ,one_real_time2 ,second_real_time2 #line:2627
        one_real_time1 =OOO000OO0O0OOOOO0 .gettime (one_time1 )#line:2628
        one_real_time2 =OOO000OO0O0OOOOO0 .gettime (one_time2 )#line:2629
        second_real_time1 =OOO000OO0O0OOOOO0 .gettime (second_time1 )#line:2630
        second_real_time2 =OOO000OO0O0OOOOO0 .gettime (second_time2 )#line:2631
    def Secondshot_reset (O00O0O0000O0OOO0O ):#line:2634
        global one_time1 ,one_time2 ,one_diff ,one_delay ,one_advance #line:2635
        global second_time1 ,second_time2 ,second_diff ,second_delay ,second_advance #line:2636
        O00O0O0000O0OOO0O .jiajia_time .SetValue (40.0 )#line:2637
        O00O0O0000O0OOO0O .tijiao_time .SetValue (48.0 )#line:2638
        O00O0O0000O0OOO0O .jiajia_price .SetValue (500 )#line:2639
        O00O0O0000O0OOO0O .select_tijiao .SetSelection (2 )#line:2640
        O00O0O0000O0OOO0O .yanchi_time .SetValue (0.0 )#line:2641
        O00O0O0000O0OOO0O .jiajia_time2 .SetValue (50.0 )#line:2643
        O00O0O0000O0OOO0O .tijiao_time2 .SetValue (55.5 )#line:2644
        O00O0O0000O0OOO0O .jiajia_price2 .SetValue (700 )#line:2645
        O00O0O0000O0OOO0O .select_tijiao2 .SetSelection (0 )#line:2646
        O00O0O0000O0OOO0O .yanchi_time2 .SetValue (0.5 )#line:2647
        one_time1 =40 #line:2649
        one_time2 =48 #line:2650
        one_diff =500 #line:2651
        one_delay =0.5 #line:2652
        one_advance =100 #line:2653
        second_time1 =50 #line:2655
        second_time2 =55.5 #line:2656
        second_diff =700 #line:2657
        second_delay =0.5 #line:2658
        second_advance =100 #line:2659
        global one_real_time1 ,second_real_time1 ,one_real_time2 ,second_real_time2 #line:2661
        one_real_time1 =O00O0O0000O0OOO0O .gettime (one_time1 )#line:2662
        one_real_time2 =O00O0O0000O0OOO0O .gettime (one_time2 )#line:2663
        second_real_time1 =O00O0O0000O0OOO0O .gettime (second_time1 )#line:2664
        second_real_time2 =O00O0O0000O0OOO0O .gettime (second_time2 )#line:2665
    def Strategy_save (OOOOO00OO00O00O00 ,O0OO0OOOOO0O0O00O ):#line:2668
        OO0OO000O000000O0 =O0O0OOO0O0O0000OO .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =O0O0OOO0O0O0000OO .OK )#line:2670
        if OO0OO000O000000O0 .ShowModal ()==O0O0OOO0O0O0000OO .ID_OK :#line:2671
            O0O0OO0O000000000 =OO0OO000O000000O0 .GetValue ()#line:2672
            if O0O0OO0O000000000 :#line:2673
                O0OO0O0O0O0O000OO =O0O0OOO0O0O0000OO .MessageBox ('保存成功','策略保存',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_INFORMATION )#line:2674
                if O0OO0O0O0O0O000OO ==O0O0OOO0O0O0000OO .ID_OK :#line:2675
                    O0OO0O0O0O0O000OO .Destroy ()#line:2676
                    OO0OO000O000000O0 .Destroy ()#line:2677
                OOOOO00OO00O00O00 .save (O0O0OO0O000000000 )#line:2678
            else :#line:2679
                O0OO0O0O0O0O000OO =O0O0OOO0O0O0000OO .MessageBox ('名称不能为空','策略保存',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:2680
                if O0OO0O0O0O0O000OO ==O0O0OOO0O0O0000OO .ID_OK :#line:2681
                    O0OO0O0O0O0O000OO .Destroy ()#line:2682
                    OO0OO000O000000O0 .Destroy ()#line:2683
    def save (OOOOO0O0O0O0OO000 ,O0OO00OO0OO00OOOO ):#line:2685
        global one_time1 ,one_time2 ,one_diff ,one_delay ,one_advance #line:2686
        global second_time1 ,second_time2 ,second_diff ,second_delay ,second_advance #line:2687
        global osl ,e_on ,enter_on #line:2688
        if OOOOO0O0O0O0OO000 .select_stractagy .GetSelection ()==2 :#line:2690
            O0OOO0O0000000OOO =O0O0OOO0O0O0000OO .MessageBox ('请先制定一个策略','策略保存',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:2691
            if O0OOO0O0000000OOO ==O0O0OOO0O0O0000OO .ID_OK :#line:2692
                O0OOO0O0000000OOO .Destroy ()#line:2693
        elif OOOOO0O0O0O0OO000 .select_stractagy .GetSelection ()==0 :#line:2694
            osl [0 ]=0 #line:2695
            osl [1 ]=one_time1 #line:2696
            osl [2 ]=one_time2 #line:2697
            osl [3 ]=one_diff #line:2698
            osl [4 ]=one_delay #line:2699
            osl [5 ]=one_advance #line:2700
            osl [6 ]=second_time1 #line:2701
            osl [7 ]=second_time2 #line:2702
            osl [8 ]=second_diff #line:2703
            osl [9 ]=second_delay #line:2704
            osl [10 ]=second_advance #line:2705
            osl [11 ]=e_on #line:2706
            osl [12 ]=enter_on #line:2707
        elif OOOOO0O0O0O0OO000 .select_stractagy .GetSelection ()==1 :#line:2708
            osl [0 ]=1 #line:2709
            osl [0 ]=1 #line:2710
            osl [1 ]=one_time1 #line:2711
            osl [2 ]=one_time2 #line:2712
            osl [3 ]=one_diff #line:2713
            osl [4 ]=one_delay #line:2714
            osl [5 ]=one_advance #line:2715
            osl [6 ]=second_time1 #line:2716
            osl [7 ]=second_time2 #line:2717
            osl [8 ]=second_diff #line:2718
            osl [9 ]=second_delay #line:2719
            osl [10 ]=second_advance #line:2720
            osl [11 ]=e_on #line:2721
            osl [12 ]=enter_on #line:2722
        with open ('%s.strategy'%O0OO00OO0OO00OOOO ,'wb')as OO00O000O00000OOO :#line:2723
            O00OOOO0O00000O0O .dump (osl ,OO00O000O00000OOO )#line:2724
    def Strategy_load (O00OOOO00000OO0O0 ,O00OOO0000O0000O0 ):#line:2739
        import os as OOOOO0OO0000O00OO #line:2740
        O0OO00O000O0O0O0O =OOOOO0OO0000O00OO .getcwd ()#line:2741
        O0O0O0OOOO000O00O =O00OOOO00000OO0O0 .findfiles (O0OO00O000O0O0O0O )#line:2742
        if O0O0O0OOOO000O00O :#line:2743
            O000O0OOO0OO00O00 =O0O0OOO0O0O0000OO .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =O0O0O0OOOO000O00O )#line:2745
            if O000O0OOO0OO00O00 .ShowModal ()==O0O0OOO0O0O0000OO .ID_OK :#line:2746
                O0OO00O000O0O0O0O =O000O0OOO0OO00O00 .GetStringSelection ()#line:2747
                OOO0OO0OO000O00O0 =O0O0OOO0O0O0000OO .MessageDialog (None ,"载入成功",u"载入策略",O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_INFORMATION )#line:2748
                if OOO0OO0OO000O00O0 .ShowModal ()==O0O0OOO0O0O0000OO .ID_OK :#line:2749
                    OOO0OO0OO000O00O0 .Destroy ()#line:2750
                O00OOOO00000OO0O0 .load (O0OO00O000O0O0O0O )#line:2751
            print ("载入")#line:2752
            O000O0OOO0OO00O00 .Destroy ()#line:2753
        else :#line:2754
            OOO0OO0OO000O00O0 =O0O0OOO0O0O0000OO .MessageBox ('找不到任何保存的策略','策略载入',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:2755
            if OOO0OO0OO000O00O0 ==O0O0OOO0O0O0000OO .ID_OK :#line:2756
                OOO0OO0OO000O00O0 .Destroy ()#line:2757
                O000O0OOO0OO00O00 .Destroy ()#line:2758
    def load (OOO0OOO00O00OOOO0 ,O0O0O00OOOO000O00 ):#line:2760
        global osl ,e_on ,enter_on #line:2761
        global one_time1 ,one_time2 ,one_diff ,one_delay ,one_advance #line:2762
        global second_time1 ,second_time2 ,second_diff ,second_delay ,second_advance #line:2763
        global strategy_on #line:2765
        global twice ,tijiao_num ,chujia_on ,tijiao_on ,tijiao_OK ,tijiao_one #line:2766
        global one_real_time1 ,one_real_time2 ,second_real_time1 ,second_real_time2 #line:2767
        try :#line:2768
            with open (O0O0O00OOOO000O00 ,'rb')as OO0O00OOOOOOO0O0O :#line:2769
                osl =O00OOOO0O00000O0O .load (OO0O00OOOOOOO0O0O )#line:2770
        except :#line:2771
            pass #line:2772
        if osl [0 ]==0 :#line:2773
            OOO0OOO00O00OOOO0 .ss_Hide ()#line:2774
            twice =False #line:2777
            strategy_on =True #line:2778
            chujia_on =True #line:2779
            tijiao_on =False #line:2780
            tijiao_num =1 #line:2781
            tijiao_OK =False #line:2782
            tijiao_one =False #line:2783
            OOO0OOO00O00OOOO0 .select_stractagy .SetSelection (0 )#line:2785
            OOO0OOO00O00OOOO0 .jiajia_time .SetValue (osl [1 ])#line:2786
            OOO0OOO00O00OOOO0 .tijiao_time .SetValue (osl [2 ])#line:2787
            OOO0OOO00O00OOOO0 .jiajia_price .SetValue (osl [3 ])#line:2788
            OOO0OOO00O00OOOO0 .yanchi_time .SetValue (osl [4 ])#line:2789
            if osl [5 ]==100 :#line:2790
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (0 )#line:2791
            elif osl [5 ]==200 :#line:2792
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (1 )#line:2793
            else :#line:2794
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (2 )#line:2795
            one_time1 =osl [1 ]#line:2797
            one_time2 =osl [2 ]#line:2798
            one_diff =osl [3 ]#line:2799
            one_delay =osl [4 ]#line:2800
            one_advance =osl [5 ]#line:2801
            e_on =osl [11 ]#line:2803
            enter_on =osl [12 ]#line:2804
            if e_on :#line:2805
                OOO0OOO00O00OOOO0 .confirm_choice .SetSelection (0 )#line:2806
            elif enter_on :#line:2807
                OOO0OOO00O00OOOO0 .confirm_choice .SetSelection (1 )#line:2808
            one_real_time1 =OOO0OOO00O00OOOO0 .gettime (one_time1 )#line:2810
            one_real_time2 =OOO0OOO00O00OOOO0 .gettime (one_time2 )#line:2811
            second_real_time1 =OOO0OOO00O00OOOO0 .gettime (second_time1 )#line:2812
            second_real_time2 =OOO0OOO00O00OOOO0 .gettime (second_time2 )#line:2813
        elif osl [0 ]==1 :#line:2815
            strategy_on =True #line:2816
            twice =True #line:2817
            chujia_on =True #line:2818
            tijiao_on =False #line:2819
            tijiao_num =1 #line:2820
            tijiao_OK =False #line:2821
            tijiao_one =False #line:2822
            OOO0OOO00O00OOOO0 .ss_Shown ()#line:2823
            OOO0OOO00O00OOOO0 .select_stractagy .SetSelection (1 )#line:2824
            OOO0OOO00O00OOOO0 .jiajia_time .SetValue (osl [1 ])#line:2825
            OOO0OOO00O00OOOO0 .tijiao_time .SetValue (osl [2 ])#line:2826
            OOO0OOO00O00OOOO0 .jiajia_price .SetValue (osl [3 ])#line:2827
            OOO0OOO00O00OOOO0 .yanchi_time .SetValue (osl [4 ])#line:2828
            if osl [5 ]==100 :#line:2829
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (0 )#line:2830
            elif osl [5 ]==200 :#line:2831
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (1 )#line:2832
            else :#line:2833
                OOO0OOO00O00OOOO0 .select_tijiao .SetSelection (2 )#line:2834
            OOO0OOO00O00OOOO0 .jiajia_time2 .SetValue (osl [6 ])#line:2835
            OOO0OOO00O00OOOO0 .tijiao_time2 .SetValue (osl [7 ])#line:2836
            OOO0OOO00O00OOOO0 .jiajia_price2 .SetValue (osl [8 ])#line:2837
            OOO0OOO00O00OOOO0 .yanchi_time2 .SetValue (osl [9 ])#line:2838
            if osl [5 ]==100 :#line:2839
                OOO0OOO00O00OOOO0 .select_tijiao2 .SetSelection (0 )#line:2840
            elif osl [5 ]==200 :#line:2841
                OOO0OOO00O00OOOO0 .select_tijiao2 .SetSelection (1 )#line:2842
            else :#line:2843
                OOO0OOO00O00OOOO0 .select_tijiao2 .SetSelection (2 )#line:2844
            one_time1 =osl [1 ]#line:2847
            one_time2 =osl [2 ]#line:2848
            one_diff =osl [3 ]#line:2849
            one_delay =osl [4 ]#line:2850
            one_advance =osl [5 ]#line:2851
            second_time1 =osl [6 ]#line:2853
            second_time2 =osl [7 ]#line:2854
            second_diff =osl [8 ]#line:2855
            second_delay =osl [9 ]#line:2856
            second_advance =osl [10 ]#line:2857
            e_on =osl [11 ]#line:2859
            enter_on =osl [12 ]#line:2860
            if e_on :#line:2861
                OOO0OOO00O00OOOO0 .confirm_choice .SetSelection (0 )#line:2862
            elif enter_on :#line:2863
                OOO0OOO00O00OOOO0 .confirm_choice .SetSelection (1 )#line:2864
            one_real_time1 =OOO0OOO00O00OOOO0 .gettime (one_time1 )#line:2866
            one_real_time2 =OOO0OOO00O00OOOO0 .gettime (one_time2 )#line:2867
            second_real_time1 =OOO0OOO00O00OOOO0 .gettime (second_time1 )#line:2868
            second_real_time2 =OOO0OOO00O00OOOO0 .gettime (second_time2 )#line:2869
    def findfiles (O0O000OO000O00OO0 ,OOOOO000000OO00OO ):#line:2871
        O0OO0O0OOOOO0000O =[]#line:2872
        for OOO0O00OOOOOO0O00 ,O0O00OOO0OO0OO0OO ,OOOO000O00OO000O0 in OO0O00O0O0O0O0OOO .walk (OOOOO000000OO00OO ):#line:2873
            for OO0O00O0OO0OO00O0 in OOOO000O00OO000O0 :#line:2874
                if OO0O00O0O0O0O0OOO .path .splitext (OO0O00O0OO0OO00O0 )[1 ]=='.strategy':#line:2875
                    O0OO0O0OOOOO0000O .append (OO0O00O0O0O0O0OOO .path .join (OOO0O00OOOOOO0O00 ,OO0O00O0OO0OO00O0 ))#line:2876
        return O0OO0O0OOOOO0000O #line:2877
    def changetime (O0OOO0O00O000000O ,O00O00000OO00O0O0 ):#line:2883
        O00OO0000O00O00OO =O0000000OO0OO000O .mktime (O0000000OO0OO000O .strptime (O00O00000OO00O0O0 ,'%Y-%m-%d %H:%M:%S'))#line:2884
        return O00OO0000O00O00OO #line:2885
    def get_nowtime (OO0O0OO0O0OOOOO00 ):#line:2888
        O0OOO00O0OOO0O0OO =O0000000OO0OO000O .time ()#line:2889
        OOO0OOO00O00OOO00 =O0000000OO0OO000O .strftime ('%Y-%m-%d',O0000000OO0OO000O .localtime (O0OOO00O0OOO0O0OO ))#line:2890
        return OOO0OOO00O00OOO00 #line:2891
    def gettime (O0OOO00O00OOO0O00 ,O0OO00O0OOO0O00OO ):#line:2894
        OO00OOO0OO0O00OO0 =O0OOO00O00OOO0O00 .get_nowtime ()#line:2895
        O0O0000000OO0OO00 =OO00OOO0OO0O00OO0 +' 11:29:'+str (int (O0OO00O0OOO0O00OO ))#line:2896
        O0000OO000O0O00O0 =O0OOO00O00OOO0O00 .changetime (O0O0000000OO0OO00 )+float (O0OO00O0OOO0O00OO )-int (O0OO00O0OOO0O00OO )#line:2897
        return O0000OO000O0O00O0 #line:2898
class LowestpriceWindow (O0O0OOO0O0O0000OO .Panel ):#line:2901
    def __init__ (OOOO000OO00O0O0OO ,O0OO000O000O00OO0 ):#line:2902
        O0O0OOO0O0O0000OO .Window .__init__ (OOOO000OO00O0O0OO ,O0OO000O000O00OO0 ,size =Timesize )#line:2903
        OOOO000OO00O0O0OO .Bind (O0O0OOO0O0O0000OO .EVT_PAINT ,OOOO000OO00O0O0OO .OnPaint )#line:2904
        OOOO000OO00O0O0OO .timer =O0O0OOO0O0O0000OO .Timer (OOOO000OO00O0O0OO )#line:2905
        OOOO000OO00O0O0OO .Bind (O0O0OOO0O0O0000OO .EVT_TIMER ,OOOO000OO00O0O0OO .OnTimer ,OOOO000OO00O0O0OO .timer )#line:2906
        OOOO000OO00O0O0OO .timer .Start (100 )#line:2907
    def Draw (O0000O0OO000OOOOO ,O0O0000OOOO0OO0O0 ):#line:2909
        global lowest_price #line:2910
        O000000O0O0000O00 =str (lowest_price )#line:2911
        OO000O0O0000O0000 ,OO0OO00O0O000OOO0 =O0000O0OO000OOOOO .GetClientSize ()#line:2912
        O0O0000OOOO0OO0O0 .SetBackground (O0O0OOO0O0O0000OO .Brush (O0000O0OO000OOOOO .GetBackgroundColour ()))#line:2913
        O0O0000OOOO0OO0O0 .Clear ()#line:2914
        O0O0000OOOO0OO0O0 .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:2915
        O0O00OOOO00O0OO00 ,O000O0OOOO0O00000 =O0O0000OOOO0OO0O0 .GetTextExtent (O000000O0O0000O00 )#line:2916
        O0O0000OOOO0OO0O0 .DrawText (O000000O0O0000O00 ,(OO000O0O0000O0000 -O0O00OOOO00O0OO00 )/2 ,(OO0OO00O0O000OOO0 )/2 -O000O0OOOO0O00000 /2 )#line:2917
    def Modify (O0000O0O0O0OO00OO ,OOO0OO0000000O0OO ):#line:2919
        global lowest_price #line:2920
        O0000O000O0O0OO0O =str (lowest_price )#line:2921
        O00OOO0OO0OO0OOOO ,O000OOO00O0OOO0OO =O0000O0O0O0OO00OO .GetClientSize ()#line:2922
        OOO0OO0000000O0OO .SetBackground (O0O0OOO0O0O0000OO .Brush (O0000O0O0O0OO00OO .GetBackgroundColour ()))#line:2923
        OOO0OO0000000O0OO .Clear ()#line:2924
        OOO0OO0000000O0OO .SetFont (O0O0OOO0O0O0000OO .Font (30 ,O0O0OOO0O0O0000OO .SWISS ,O0O0OOO0O0O0000OO .NORMAL ,O0O0OOO0O0O0000OO .NORMAL ))#line:2925
        OO0OOO00O0O0O00OO ,OOOOOOO0OO0O0OOOO =OOO0OO0000000O0OO .GetTextExtent (O0000O000O0O0OO0O )#line:2926
        OOO0OO0000000O0OO .DrawText (O0000O000O0O0OO0O ,(O00OOO0OO0OO0OOOO -OO0OOO00O0O0O00OO )/2 ,(O000OOO00O0OOO0OO )/2 -OOOOOOO0OO0O0OOOO /2 )#line:2927
    def OnTimer (OOO0OOO00OO0OO000 ,O0000O0O0000O00OO ):#line:2929
        O0O0OO00O0OOO0OO0 =O0O0OOO0O0O0000OO .BufferedDC (O0O0OOO0O0O0000OO .ClientDC (OOO0OOO00OO0OO000 ))#line:2930
        OOO0OOO00OO0OO000 .Modify (O0O0OO00O0OOO0OO0 )#line:2931
    def OnPaint (O0O0O000000000O00 ,OO00O00OOOOO0OOOO ):#line:2933
        OO00OO0OOO000OO00 =O0O0OOO0O0O0000OO .BufferedPaintDC (O0O0O000000000O00 )#line:2934
        O0O0O000000000O00 .Draw (OO00OO0OOO000OO00 )#line:2935
class LowestpriceFrame (O0O0OOO0O0O0000OO .Frame ):#line:2937
    def __init__ (OOOOOOO000O000OO0 ):#line:2938
         O0O0OOO0O0O0000OO .Frame .__init__ (OOOOOOO000O000OO0 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =(300 ,300 ),style =O0O0OOO0O0O0000OO .FRAME_TOOL_WINDOW |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:2940
         LowestpriceWindow (OOOOOOO000O000OO0 )#line:2943
import string as O0OOO00OOOOO00000 #line:2961
import wx .lib .agw .hyperlink as O00O0OOO0OOO0OO00 #line:2962
class LoginFrame (O0O0OOO0O0O0000OO .Frame ):#line:2963
    def __init__ (O00OO00O0O00O0000 ,OOO0O0O0000OOOOOO ,O00OOOOO0O000OOOO ,O000O000O00OOOO0O ):#line:2964
        O0O0OOO0O0O0000OO .Frame .__init__ (O00OO00O0O00O0000 ,None ,-1 ,OOO0O0O0000OOOOOO ,size =(300 ,240 ),style =O0O0OOO0O0O0000OO .CAPTION |O0O0OOO0O0O0000OO .CLOSE_BOX )#line:2965
        O00OO00O0O00O0000 .Bind (O0O0OOO0O0O0000OO .EVT_CLOSE ,O00OO00O0O00O0000 .OnClose )#line:2966
        O00OO00O0O00O0000 .panel =O0O0OOO0O0O0000OO .Panel (O00OO00O0O00O0000 ,size =(300 ,220 ))#line:2967
        O00OO00O0O00O0000 .icon =O0O0OOO0O0O0000OO .Icon (mainicon ,O0O0OOO0O0O0000OO .BITMAP_TYPE_ICO )#line:2968
        O00OO00O0O00O0000 .SetIcon (O00OO00O0O00O0000 .icon )#line:2969
        O00OO00O0O00O0000 .sizer_v1 =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .VERTICAL )#line:2982
        O00OO00O0O00O0000 .welcomelabel =O0O0OOO0O0O0000OO .StaticText (O00OO00O0O00O0000 .panel ,-1 ,label ="请输入用户名和密码",style =O0O0OOO0O0O0000OO .ALIGN_CENTER )#line:2983
        O00OO00O0O00O0000 .sizer_v1 .Add (O00OO00O0O00O0000 .welcomelabel ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =10 )#line:2984
        O00OO00O0O00O0000 .userbox =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2987
        O00OO00O0O00O0000 .userlabel =O0O0OOO0O0O0000OO .StaticText (O00OO00O0O00O0000 .panel ,-1 ,label ="账号")#line:2988
        O00OO00O0O00O0000 .userText =O0O0OOO0O0O0000OO .TextCtrl (O00OO00O0O00O0000 .panel ,-1 ,size =(150 ,-1 ),style =O0O0OOO0O0O0000OO .TE_CENTER |O0O0OOO0O0O0000OO .TE_PROCESS_ENTER )#line:2990
        O00OO00O0O00O0000 .userbox .Add (O00OO00O0O00O0000 .userlabel ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2991
        O00OO00O0O00O0000 .userbox .Add (O00OO00O0O00O0000 .userText ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER_HORIZONTAL |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2992
        O00OO00O0O00O0000 .passbox =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:2994
        O00OO00O0O00O0000 .passlabel =O0O0OOO0O0O0000OO .StaticText (O00OO00O0O00O0000 .panel ,-1 ,label ="密码")#line:2995
        O00OO00O0O00O0000 .passText =O0O0OOO0O0O0000OO .TextCtrl (O00OO00O0O00O0000 .panel ,-1 ,size =(150 ,-1 ),style =O0O0OOO0O0O0000OO .TE_CENTER |O0O0OOO0O0O0000OO .TE_PROCESS_ENTER |O0O0OOO0O0O0000OO .TE_PASSWORD )#line:2997
        O00OO00O0O00O0000 .passbox .Add (O00OO00O0O00O0000 .passlabel ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2998
        O00OO00O0O00O0000 .passbox .Add (O00OO00O0O00O0000 .passText ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER_HORIZONTAL |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:2999
        if O00OOOOO0O000OOOO :#line:3000
            O00OO00O0O00O0000 .userText .SetValue (O00OOOOO0O000OOOO )#line:3001
        if O000O000O00OOOO0O :#line:3002
            O00OO00O0O00O0000 .passText .SetValue (O000O000O00OOOO0O )#line:3003
        O00OO00O0O00O0000 .sizer_v1 .Add (O00OO00O0O00O0000 .userbox ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:3004
        O00OO00O0O00O0000 .sizer_v1 .Add (O00OO00O0O00O0000 .passbox ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:3005
        O00OO00O0O00O0000 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT_ENTER ,O00OO00O0O00O0000 .OnLogin ,O00OO00O0O00O0000 .userText )#line:3007
        O00OO00O0O00O0000 .Bind (O0O0OOO0O0O0000OO .EVT_TEXT_ENTER ,O00OO00O0O00O0000 .OnLogin ,O00OO00O0O00O0000 .passText )#line:3008
        O00OO00O0O00O0000 .monibtn =O0O0OOO0O0O0000OO .Button (O00OO00O0O00O0000 .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3010
        O00OO00O0O00O0000 .loginbtn =O0O0OOO0O0O0000OO .Button (O00OO00O0O00O0000 .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3011
        O00OO00O0O00O0000 .btnSizer =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:3012
        O00OO00O0O00O0000 .btnSizer .Add (O00OO00O0O00O0000 .monibtn ,flag =O0O0OOO0O0O0000OO .ALIGN_LEFT |O0O0OOO0O0O0000OO .ALL ,border =3 )#line:3013
        O00OO00O0O00O0000 .btnSizer .Add (O00OO00O0O00O0000 .loginbtn ,flag =O0O0OOO0O0O0000OO .ALIGN_RIGHT |O0O0OOO0O0O0000OO .ALL ,border =3 )#line:3014
        O00OO00O0O00O0000 .sizer_v1 .Add (O00OO00O0O00O0000 .btnSizer ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:3015
        O00OO00O0O00O0000 .loginbtn .Bind (O0O0OOO0O0O0000OO .EVT_BUTTON ,O00OO00O0O00O0000 .OnLogin ,O00OO00O0O00O0000 .loginbtn )#line:3016
        O00OO00O0O00O0000 .purchaselink =O00O0OOO0OOO0OO00 .HyperLinkCtrl (O00OO00O0O00O0000 .panel ,-1 ,u"购买账号")#line:3018
        O00OO00O0O00O0000 .purchaselink .UnsetToolTip ()#line:3019
        O00OO00O0O00O0000 .purchaselink .Bind (O00O0OOO0OOO0OO00 .EVT_HYPERLINK_LEFT ,O00OO00O0O00O0000 .Purchase )#line:3020
        O00OO00O0O00O0000 .purchaselink .AutoBrowse (False )#line:3021
        O00OO00O0O00O0000 .purchaselink .EnableRollover (True )#line:3022
        O00OO00O0O00O0000 .purchaselink .SetUnderlines (False ,False ,True )#line:3023
        O00OO00O0O00O0000 .purchaselink .OpenInSameWindow (True )#line:3024
        O00OO00O0O00O0000 .purchaselink .UpdateLink ()#line:3025
        O00OO00O0O00O0000 .helplink =O00O0OOO0OOO0OO00 .HyperLinkCtrl (O00OO00O0O00O0000 .panel ,-1 ,u"查看帮助")#line:3027
        O00OO00O0O00O0000 .helplink .UnsetToolTip ()#line:3028
        O00OO00O0O00O0000 .helplink .Bind (O00O0OOO0OOO0OO00 .EVT_HYPERLINK_LEFT ,O00OO00O0O00O0000 .Purchase )#line:3029
        O00OO00O0O00O0000 .helplink .AutoBrowse (False )#line:3030
        O00OO00O0O00O0000 .helplink .EnableRollover (True )#line:3031
        O00OO00O0O00O0000 .helplink .SetUnderlines (False ,False ,True )#line:3032
        O00OO00O0O00O0000 .helplink .OpenInSameWindow (True )#line:3033
        O00OO00O0O00O0000 .helplink .UpdateLink ()#line:3034
        O00OO00O0O00O0000 .linkbox =O0O0OOO0O0O0000OO .BoxSizer (O0O0OOO0O0O0000OO .HORIZONTAL )#line:3036
        O00OO00O0O00O0000 .linkbox .Add (O00OO00O0O00O0000 .purchaselink ,flag =O0O0OOO0O0O0000OO .ALIGN_LEFT |O0O0OOO0O0O0000OO .RIGHT ,border =20 )#line:3037
        O00OO00O0O00O0000 .linkbox .Add (O00OO00O0O00O0000 .helplink ,flag =O0O0OOO0O0O0000OO .ALIGN_RIGHT |O0O0OOO0O0O0000OO .LEFT ,border =20 )#line:3038
        O00OO00O0O00O0000 .sizer_v1 .Add (O00OO00O0O00O0000 .linkbox ,flag =O0O0OOO0O0O0000OO .ALIGN_CENTER |O0O0OOO0O0O0000OO .ALL ,border =5 )#line:3039
        O00OO00O0O00O0000 .SetSizer (O00OO00O0O00O0000 .sizer_v1 )#line:3041
        O00OO00O0O00O0000 .Center ()#line:3042
        OOOO0000OO0OOO0OO .subscribe (O00OO00O0O00O0000 .connect_success ,"connect")#line:3044
        O00OO00O0O00O0000 .hashthread =HashThread ()#line:3047
    def connect_success (OOOO00O00000OOO00 ):#line:3049
        OOOO00O00000OOO00 .loginbtn .Enable ()#line:3050
        global login_result #line:3051
        if login_result =='login success':#line:3052
            OOOO00O00000OOO00 .Destroy ()#line:3053
            OOOO00O00000OOO00 .topframe =TopFrame ('沪牌第一枪',version )#line:3054
            OOOO00O00000OOO00 .topframe .Show (True )#line:3055
        elif login_result =='net error':#line:3057
            O0O0OOO0O0O0000OO .MessageBox ('连接服务器失败','用户登录',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:3058
        elif login_result =='repeat':#line:3059
            O0O0OOO0O0O0000OO .MessageBox ('重复登录，稍后再试','用户登录',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:3060
        else :#line:3061
            O0O0OOO0O0O0000OO .MessageBox ('登录失败','用户登录',O0O0OOO0O0O0000OO .OK |O0O0OOO0O0O0000OO .ICON_ERROR )#line:3062
    def OnEraseBack (O0OOOO000O0OO0OOO ,OOOO000000000O000 ):#line:3065
        OO000O0OOO00OOO0O =OOOO000000000O000 .GetDC ()#line:3066
        if not OO000O0OOO00OOO0O :#line:3067
            OO000O0OOO00OOO0O =O0O0OOO0O0O0000OO .ClientDC (O0OOOO000O0OO0OOO )#line:3068
            O000O00OO0OO0OO0O =O0OOOO000O0OO0OOO .GetUpdateRegion ().GetBox ()#line:3069
            OO000O0OOO00OOO0O .SetClippingRect (O000O00OO0OO0OO0O )#line:3070
        OO000O0OOO00OOO0O .Clear ()#line:3071
        O000OOO0O0000O00O =O0O0OOO0O0O0000OO .Bitmap ("blue.jpg")#line:3072
        OO000O0OOO00OOO0O .DrawBitmap (O000OOO0O0000O00O ,0 ,0 )#line:3073
    def OnClose (OOO00OOOO000OO000 ,OO0000O0000000OOO ):#line:3075
        OO0000O0000000OOO .Skip ()#line:3076
        OO0OO0OOOOOOO00OO .exit (None )#line:3077
    def OnLogin (O0OOO0OO00OO0O0O0 ,O00OOO0OOOO000O00 ):#line:3085
        global Username ,Password #line:3086
        O000000OOOO0OOO00 =O0OOO0OO00OO0O0O0 .userText .GetValue ()#line:3087
        O00O000000O0O000O =O0OOO0OO00OO0O0O0 .passText .GetValue ()#line:3088
        if O000000OOOO0OOO00 =="":#line:3089
            O0O0OOO0O0O0000OO .MessageBox ('请输入用户名！')#line:3090
            O0OOO0OO00OO0O0O0 .userText .SetFocus ()#line:3091
        elif O00O000000O0O000O =="":#line:3092
            O0O0OOO0O0O0000OO .MessageBox ('请输入密码！')#line:3093
            O0OOO0OO00OO0O0O0 .passText .SetFocus ()#line:3094
        else :#line:3096
            Username =O000000OOOO0OOO00 #line:3097
            Password =O00O000000O0O000O #line:3098
            O0OOO0OO00OO0O0O0 .loginthread =LoginThread ()#line:3099
            O0O00000OO0O0OO00 =[O000000OOOO0OOO00 ,O00O000000O0O000O ]#line:3100
            with open ('your.name','wb')as OOOOO0OO0O0O00OOO :#line:3101
                O00OOOO0O00000O0O .dump (O0O00000OO0O0OO00 ,OOOOO0OO0O0O00OOO )#line:3102
            O00OOO0OOOO000O00 .GetEventObject ().Disable ()#line:3104
    def Purchase (O00OO00O0O0O00O0O ,O00000OO0O0OOO0O0 ):#line:3106
        print ("购买")#line:3107
class UserValidator (O0O0OOO0O0O0000OO .Validator ):#line:3111
    ""#line:3112
    def __init__ (OO00000OOO00OO0OO ,OOOO0O00OO0O000O0 ):#line:3114
        O0O0OOO0O0O0000OO .Validator .__init__ (OO00000OOO00OO0OO )#line:3115
        OO00000OOO00OO0OO .flag =OOOO0O00OO0O000O0 #line:3116
        OO00000OOO00OO0OO .Bind (O0O0OOO0O0O0000OO .EVT_CHAR ,OO00000OOO00OO0OO .OnChar )#line:3117
    def Clone (O0O00OOOOO0000O0O ):#line:3120
        ""#line:3121
        return UserValidator (O0O00OOOOO0000O0O .flag )#line:3122
    def Validate (O0OO00O0O0OOOO0OO ,OOOOOO000OO0O0O0O ):#line:3125
        return True #line:3126
    def TransferToWindow (OOO0O00OO000O0000 ):#line:3129
        return True #line:3130
    def TransferFromWindow (OO0OO0O00000O0OO0 ):#line:3133
        return True #line:3134
    def OnChar (OO0O0O0000OO000OO ,O0000000O00O00OOO ):#line:3137
        pass #line:3138
class PassValidator (O0O0OOO0O0O0000OO .Validator ):#line:3152
    ""#line:3153
    def __init__ (O0OOO0OOO0O00OO0O ):#line:3156
        O0O0OOO0O0O0000OO .Validator .__init__ (O0OOO0OOO0O00OO0O )#line:3157
        O0OOO0OOO0O00OO0O .Bind (O0O0OOO0O0O0000OO .EVT_CHAR ,O0OOO0OOO0O00OO0O .OnChar )#line:3158
    def Clone (OO0OO00O00O00O0O0 ):#line:3161
        ""#line:3162
        return PassValidator ()#line:3163
    def Validate (OO00OOO0000O00O00 ,OO0OO0OO00OOO0OO0 ):#line:3166
        return True #line:3167
    def TransferToWindow (O00OOO0O00O000000 ):#line:3170
        return True #line:3171
    def TransferFromWindow (OOOO0OO00O00OO000 ):#line:3174
        return True #line:3175
    def OnChar (O0OOO0OOOOO00OOOO ,OOOO0O00OO00000OO ):#line:3178
        pass #line:3179
class ConfirmLogin (O0O0OOO0O0O0000OO .Frame ):#line:3193
    pass #line:3194
class TimeThread (OO00O000000O0OOO0 ):#line:3197
    def __init__ (O00OOO0O000OOO0OO ):#line:3198
        ""#line:3199
        OO00O000000O0OOO0 .__init__ (O00OOO0O000OOO0OO )#line:3200
        O00OOO0O000OOO0OO .setDaemon (True )#line:3201
        O00OOO0O000OOO0OO .start ()#line:3202
    def run (OO0O0O0O0000O00O0 ):#line:3204
        ""#line:3205
        global a_time #line:3207
        for OO0O0O0O00O000OOO in range (1000000 ):#line:3208
            OOOO0OO0OO0OO0O0O =O0000000OO0OO000O .clock ()#line:3209
            O0000000OO0OO000O .sleep (0.1 )#line:3210
            OO00000O0OO00O0OO =O0000000OO0OO000O .clock ()#line:3211
            a_time +=OO00000O0OO00O0OO -OOOO0OO0OO0OO0O0O #line:3212
class HashThread (OO00O000000O0OOO0 ):#line:3243
    def __init__ (OOOOOO0OO0OOO0000 ):#line:3244
        ""#line:3245
        OO00O000000O0OOO0 .__init__ (OOOOOO0OO0OOO0000 )#line:3246
        OOOOOO0OO0OOO0000 .setDaemon (True )#line:3247
        OOOOOO0OO0OOO0000 .start ()#line:3248
    def run (OOO0O0O0OOO00OOO0 ):#line:3250
        ""#line:3251
        Create_hash ()#line:3253
class findposThread (OO00O000000O0OOO0 ):#line:3259
    def __init__ (O0OOO000OOO0000O0 ):#line:3260
        OO00O000000O0OOO0 .__init__ (O0OOO000OOO0000O0 )#line:3261
        O0OOO000OOO0000O0 .setDaemon (True )#line:3262
        O0OOO000OOO0000O0 .start ()#line:3263
    def run (OO000O0O00OO0OO0O ):#line:3265
        findpos ()#line:3266
class confirmThread (OO00O000000O0OOO0 ):#line:3269
    def __init__ (OOOO00OO000OOOOO0 ):#line:3270
        OO00O000000O0OOO0 .__init__ (OOOO00OO000OOOOO0 )#line:3271
        OOOO00OO000OOOOO0 .setDaemon (True )#line:3272
        OOOO00OO000OOOOO0 .start ()#line:3273
    def run (OO00OO00O00OOO00O ):#line:3275
        global confirm_need ,confirm_on #line:3276
        global confirm_need ,confirm_on ,confirm_one ,chujia_on #line:3277
        for OOO0OOO0000OOO0OO in range (100 ):#line:3278
            O0O0OOO0O0O0000OO .Sleep (0.1 )#line:3279
            if confirm_need :#line:3281
                print ("开启查找")#line:3282
                findconfirm ()#line:3283
                if confirm_on :#line:3284
                    TopFrame .OnClick_confirm ()#line:3285
                    confirm_need =False #line:3286
                    confirm_on =False #line:3287
                    confirm_one =False #line:3288
                    chujia_on =True #line:3289
        confirm_one =False #line:3290
class refreshThread (OO00O000000O0OOO0 ):#line:3292
    def __init__ (OO00O0OO00O0OOOO0 ):#line:3293
        OO00O000000O0OOO0 .__init__ (OO00O0OO00O0OOOO0 )#line:3294
        OO00O0OO00O0OOOO0 .setDaemon (True )#line:3295
        OO00O0OO00O0OOOO0 .start ()#line:3296
    def run (OO000OO00O0000000 ):#line:3298
        global confirm_need ,confirm_on #line:3299
        global refresh_need ,refresh_on ,refresh_one #line:3300
        for O0O00000OOOO00OOO in range (50 ):#line:3301
            if refresh_need :#line:3302
                findrefresh ()#line:3303
                if refresh_on :#line:3304
                    TopFrame .OnClick_Shuaxin ()#line:3305
                    refresh_on =False #line:3306
                    refresh_need =False #line:3307
                    refresh_one =False #line:3308
        refresh_one =False #line:3309
class LoginThread (OO00O000000O0OOO0 ):#line:3314
    def __init__ (O000OOO0O00OO00OO ):#line:3315
        ""#line:3316
        OO00O000000O0OOO0 .__init__ (O000OOO0O00OO00OO )#line:3317
        O000OOO0O00OO00OO .setDaemon (True )#line:3318
        O000OOO0O00OO00OO .start ()#line:3319
    def run (O00O0OOOO0000OO0O ):#line:3321
        global Username ,login_result #line:3323
        login_result =ConfirmUser ()#line:3324
        print (login_result )#line:3325
        OOO0O0O000O0OOO00 .info ("%s"%login_result )#line:3326
        O0O0OOO0O0O0000OO .CallAfter (OOOO0000OO0OOO0OO .sendMessage ,"connect")#line:3327
class controlThread (OO00O000000O0OOO0 ):#line:3330
    def __init__ (O00OOOO0O0OOOOO0O ):#line:3331
        ""#line:3332
        OO00O000000O0OOO0 .__init__ (O00OOOO0O0OOOOO0O )#line:3333
        O00OOOO0O0OOOOO0O .setDaemon (True )#line:3334
        O00OOOO0O0OOOOO0O .start ()#line:3335
    def run (O0OOOO00O00OO0000 ):#line:3338
        O0O0OOO0O0O0000OO .Sleep (10 )#line:3339
        O0O0OOO0O0O0000OO .CallAfter (OOOO0000OO0OOO0OO .sendMessage ,"connect failure")#line:3340
class KeepThread (OO00O000000O0OOO0 ):#line:3345
    def __init__ (OO0O0O00OO0OO00OO ):#line:3346
        ""#line:3347
        OO00O000000O0OOO0 .__init__ (OO0O0O00OO0OO00OO )#line:3348
        OO0O0O00OO0OO00OO .setDaemon (True )#line:3349
        OO0O0O00OO0OO00OO .start ()#line:3350
    def run (O0O00OO0O0O00O0OO ):#line:3353
        for O0000000OOOO0000O in range (1000000 ):#line:3354
            O0000000OO0OO000O .sleep (90 )#line:3355
            Keeplogin ()#line:3356
class TijiaoThread (OO00O000000O0OOO0 ):#line:3362
    def __init__ (OO0000O0O00OOOO00 ):#line:3363
        ""#line:3364
        OO00O000000O0OOO0 .__init__ (OO0000O0O00OOOO00 )#line:3365
        OO0000O0O00OOOO00 .setDaemon (True )#line:3366
        OO0000O0O00OOOO00 .start ()#line:3367
    def run (O0OO0OO0OOO0O00OO ):#line:3370
        global tijiao_delay ,final_tijiao ,strategy_price ,lowest_price ,own_price1 ,own_price2 #line:3371
        global moni_second ,strategy_on ,moni_on ,tijiao_on ,tijiao_OK ,second_real_time1 ,second_real_time2 #line:3372
        global one_advance ,second_advance ,tijiao_num ,tijiao_OK ,chujia_on ,tijiao_on ,tijiao_one #line:3373
        for OOOOOOO000O0OO0O0 in range (10000000 ):#line:3374
            O0000000OO0OO000O .sleep (0.1 )#line:3375
            if tijiao_on and strategy_on and guopai_on and tijiao_OK :#line:3379
                if tijiao_num ==1 and a_time >=one_real_time2 and not tijiao_one :#line:3381
                    tijiao_on =False #line:3382
                    TopFrame .OnClick_Tijiao ()#line:3383
                    tijiao_on =False #line:3384
                    OOO0O0O000O0OOO00 .info ("Rone_tijiao %s%s%s%s"%(tijiao_on ,strategy_on ,guopai_on ,tijiao_OK ))#line:3385
                    OOO0O0O000O0OOO00 .info ("Rone_tijiao %s%s%s"%(tijiao_num ,a_time ,one_real_time2 ))#line:3386
                    tijiao_one =True #line:3387
                elif tijiao_num ==2 and a_time >=second_real_time2 :#line:3388
                    tijiao_on =False #line:3389
                    TopFrame .OnClick_Tijiao ()#line:3390
                    tijiao_on =False #line:3391
                    OOO0O0O000O0OOO00 .info ("Rsecond_tijiao %s%s%s%s"%(tijiao_on ,strategy_on ,guopai_on ,tijiao_OK ))#line:3392
                    OOO0O0O000O0OOO00 .info ("Rsecond_tijiao %s%s%s"%(tijiao_num ,a_time ,second_real_time2 ))#line:3393
                elif tijiao_num ==1 and lowest_price >=own_price1 -300 -one_advance and not tijiao_one :#line:3394
                    tijiao_on =False #line:3395
                    tijiao_on =False #line:3396
                    TopFrame .OnClick_Tijiao ()#line:3397
                    OOO0O0O000O0OOO00 .info ("Rone_tijiao %s%s%s%s"%(tijiao_on ,strategy_on ,guopai_on ,tijiao_OK ))#line:3398
                    OOO0O0O000O0OOO00 .info ("Rone_tijiao %s%s%s"%(tijiao_num ,lowest_price ,own_price1 ))#line:3399
                    tijiao_one =True #line:3400
                elif tijiao_num ==2 and lowest_price >=own_price2 -300 -second_advance :#line:3401
                    tijiao_on =False #line:3402
                    tijiao_on =False #line:3403
                    TopFrame .OnClick_Tijiao ()#line:3404
                    OOO0O0O000O0OOO00 .info ("Rsecond_tijiao %s%s%s%s"%(tijiao_on ,strategy_on ,guopai_on ,tijiao_OK ))#line:3405
                    OOO0O0O000O0OOO00 .info ("Rsecond_tijiao %s%s%s"%(tijiao_num ,lowest_price ,own_price2 ))#line:3406
            if strategy_on and guopai_on and chujia_on :#line:3408
                if tijiao_num ==1 and one_real_time1 <=a_time <=one_real_time1 +0.2 :#line:3410
                    TopFrame .OnClick_chujia ()#line:3411
                    own_price1 =lowest_price +one_diff #line:3412
                    tijiao_on =True #line:3413
                    OOO0O0O000O0OOO00 .info ("Rone_chujia %s%s"%(strategy_on ,guopai_on ))#line:3414
                    OOO0O0O000O0OOO00 .info ("Rone_chujia %s%s"%(one_time1 ,one_real_time1 ))#line:3415
                if tijiao_num ==2 and twice and second_real_time1 <=a_time :#line:3416
                    TopFrame .OnClick_chujia ()#line:3417
                    own_price2 =lowest_price +second_diff #line:3418
                    tijiao_on =True #line:3419
                    OOO0O0O000O0OOO00 .info ("Rsecond_chujia %s%s"%(strategy_on ,guopai_on ))#line:3420
                    OOO0O0O000O0OOO00 .info ("Rsecond_chujia %s%s"%(second_time1 ,second_real_time1 ))#line:3421
class MoniTijiaoThread (OO00O000000O0OOO0 ):#line:3425
    def __init__ (OOOO0OO0O0O00OO0O ):#line:3426
        ""#line:3427
        OO00O000000O0OOO0 .__init__ (OOOO0OO0O0O00OO0O )#line:3428
        OOOO0OO0O0O00OO0O .setDaemon (True )#line:3429
        OOOO0OO0O0O00OO0O .start ()#line:3430
    def run (O0O000O0O0OOO000O ):#line:3433
        global moni_second ,strategy_on ,moni_on ,tijiao_on ,own_price1 ,own_price2 ,one_diff ,second_diff #line:3434
        global tijiao_num ,tijiao_OK ,one_advance ,second_advance ,tijiao_one #line:3435
        for OOO0OOOO0OOO0O0O0 in range (10000000 ):#line:3436
            O0000000OO0OO000O .sleep (0.1 )#line:3437
            if tijiao_on and strategy_on and moni_on and tijiao_OK :#line:3439
                print (tijiao_on ,strategy_on ,moni_on ,tijiao_OK )#line:3440
                print (tijiao_num ,moni_second ,one_time2 ,tijiao_one )#line:3441
                print (lowest_price ,own_price1 ,own_price2 )#line:3442
                if tijiao_num ==1 and moni_second >=one_time2 and not tijiao_one :#line:3443
                    TopFrame .OnClick_Tijiao ()#line:3444
                    OOO0O0O000O0OOO00 .info ("moni one_tijiao %s %s %s %s"%(tijiao_on ,strategy_on ,moni_on ,tijiao_OK ))#line:3445
                    OOO0O0O000O0OOO00 .info ("moni one_tijiao %s %s %s"%(tijiao_num ,moni_second ,one_time2 ))#line:3446
                    tijiao_on =False #line:3447
                    tijiao_one =True #line:3448
                elif tijiao_num ==2 and moni_second >=second_time2 and twice :#line:3449
                    TopFrame .OnClick_Tijiao ()#line:3450
                    OOO0O0O000O0OOO00 .info ("moni1 second_tijiao %s %s %s %s"%(tijiao_on ,strategy_on ,moni_on ,tijiao_OK ))#line:3451
                    OOO0O0O000O0OOO00 .info ("moni second_tijiao %s %s %s"%(tijiao_num ,moni_second ,second_time2 ))#line:3452
                    tijiao_on =False #line:3453
                elif tijiao_num ==1 and lowest_price >=own_price1 -300 -one_advance and not tijiao_one :#line:3454
                    tijiao_on =False #line:3455
                    TopFrame .OnClick_Tijiao ()#line:3456
                    OOO0O0O000O0OOO00 .info ("moni one_tijiao %s %s %s %s"%(tijiao_on ,strategy_on ,moni_on ,tijiao_OK ))#line:3457
                    OOO0O0O000O0OOO00 .info ("moni one_tijiao %s %s %s"%(tijiao_num ,lowest_price ,own_price1 ))#line:3458
                    tijiao_one =True #line:3459
                elif tijiao_num ==2 and lowest_price >=own_price2 -300 -second_advance and twice :#line:3460
                    tijiao_on =False #line:3461
                    TopFrame .OnClick_Tijiao ()#line:3462
                    OOO0O0O000O0OOO00 .info ("moni2 second_tijiao %s%s%s%s"%(tijiao_on ,strategy_on ,moni_on ,tijiao_OK ))#line:3463
                    OOO0O0O000O0OOO00 .info ("moni second_tijiao %s%s%s"%(tijiao_num ,lowest_price ,own_price2 ))#line:3464
            if strategy_on and moni_on and chujia_on :#line:3469
                if tijiao_num ==1 and one_time1 <=moni_second <=one_time1 +0.2 :#line:3470
                    TopFrame .OnClick_chujia ()#line:3471
                    own_price1 =lowest_price +one_diff #line:3473
                    tijiao_on =True #line:3474
                    OOO0O0O000O0OOO00 .info ("moni one_chujia %s %s"%(strategy_on ,moni_on ))#line:3475
                    OOO0O0O000O0OOO00 .info ("moni one_chujia %s %s"%(one_time1 ,moni_second ))#line:3476
                elif tijiao_num ==2 and twice and second_time1 <moni_second :#line:3477
                    TopFrame .OnClick_chujia ()#line:3478
                    own_price2 =lowest_price +second_diff #line:3480
                    tijiao_on =True #line:3481
                    OOO0O0O000O0OOO00 .info ("moni second_chujia %s %s"%(strategy_on ,moni_on ))#line:3482
                    OOO0O0O000O0OOO00 .info ("moni second_chujia %s %s"%(second_time1 ,moni_second ))#line:3483
class SketchApp (O0O0OOO0O0O0000OO .App ):#line:3487
    def OnInit (OO0O00OOO0OOO000O ):#line:3488
        try :#line:3489
            O00OO0O0OOO0OOOO0 =O0O0OOO0O0O0000OO .Bitmap ('start.png',O0O0OOO0O0O0000OO .BITMAP_TYPE_PNG )#line:3490
            O0O0OOO0O0O0000OO .adv .SplashScreen (O00OO0O0OOO0OOOO0 ,O0O0OOO0O0O0000OO .adv .SPLASH_CENTRE_ON_SCREEN |O0O0OOO0O0O0000OO .adv .SPLASH_TIMEOUT ,1500 ,None ,-1 ,O0O0OOO0O0O0000OO .DefaultPosition ,size =(300 ,240 ),style =O0O0OOO0O0O0000OO .BORDER_SIMPLE |O0O0OOO0O0O0000OO .STAY_ON_TOP )#line:3494
            O0O0OOO0O0O0000OO .Yield ()#line:3496
        except :#line:3497
            pass #line:3498
        try :#line:3499
            with open ("your.name",'rb')as O0O00OOOO0OO000OO :#line:3500
                OOOOO000OO0OOO000 =O00OOOO0O00000O0O .load (O0O00OOOO0OO000OO )#line:3501
                OOO0OO00000OO00O0 =OOOOO000OO0OOO000 [0 ]#line:3502
                O0OO0O0000OOO00OO =OOOOO000OO0OOO000 [1 ]#line:3503
        except :#line:3504
            OOO0OO00000OO00O0 ='123456'#line:3505
            O0OO0O0000OOO00OO =0 #line:3506
        OO0O0OOOOO0OOOO00 =LoginFrame ('沪牌第一枪',OOO0OO00000OO00O0 ,O0OO0O0000OOO00OO )#line:3507
        OO0O0OOOOO0OOOO00 .Show (True )#line:3508
        return True #line:3509
if __name__ =='__main__':#line:3512
    app =SketchApp ()#line:3513
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9
