""#line:5
version ='1.5s'#line:8
num =0 #line:9
host_ali ="121.196.220.94"#line:11
url1 ="http://moni.51hupai.org/"#line:14
url2 ="https://paimai.alltobid.com/bid/2017052001/login.htm"#line:15
mainicon ='ico.ico'#line:17
view =False #line:20
do =False #line:21
ad_view =False #line:22
zxco0o0o0o0_view =False #line:24
zxco0o0o0o0_on =False #line:25
zxco0o0o0o0_count =0 #line:26
web_on =False #line:27
view_time =False #line:29
time_on =False #line:30
import time #line:31
a_time =time .time ()#line:32
b_time =0 #line:33
o0sdofsfo0sodf0so0_minute =29 #line:35
o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:36
oo0o0O0O0O0_time =0 #line:38
Username =0 #line:40
Password =0 #line:41
o0sdofsfo0sodf0so0_on =False #line:44
ooweo0o0werwr_on =False #line:45
ghjo0o0o0o01 =53 #line:48
ghjo0o0o0o02 =0.0 #line:49
ghjo0o0o0o0_on =True #line:55
ghjo0o0o0o0_repeat =False #line:56
delay =False #line:59
delay_time =0.5 #line:60
login_result =False #line:62
findpos_on =True #line:65
zxco0o0o0o0list =[80000 +O0OO0O000000000O0 *100 for O0OO0O000000000O0 in range (200 )]#line:67
IDnumber =0 #line:68
account =0 #line:69
passwd =0 #line:70
import pyautogui as pg #line:74
def Create_hash ():#line:76
    with open ('dick.dl','rb')as O0O0OOOO0000O00OO :#line:77
        global dick_hash #line:78
        dick_hash =pickle .load (O0O0OOOO0000O00OO )#line:79
    with open ('cf.btn','rb')as O0000OO0OO00O00O0 :#line:80
        global cf_hash #line:81
        cf_hash =pickle .load (O0000OO0OO00O00O0 )#line:82
    with open ("target.tkl",'rb')as OO0OOOOO0O000OOOO :#line:84
        global dick_target #line:85
        dick_target =pickle .load (OO0OOOOO0O000OOOO )#line:86
OO00000o01 =48 #line:91
OO00000o02 =55 #line:92
one_oO0O0O0O0O0O0O0O01 =1000000000000 #line:93
one_oO0O0O0O0O0O0O0O02 =1000000000000 #line:94
one_diff =700 #line:95
one_delay =0.5 #line:96
one_advance =100 #line:97
ooo0O0o0oO0O_time1 =48 #line:100
ooo0O0o0oO0O_time2 =55 #line:101
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =1000000000000 #line:102
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =1000000000000 #line:103
ooo0O0o0oO0O_diff =600 #line:104
ooo0O0o0oO0O_delay =0.5 #line:105
ooo0O0o0oO0O_advance =100 #line:106
osl =[0 ]*15 #line:108
oo0o0O0O0O0_on =True #line:110
oOO0O0O0O0O0O0_on =False #line:111
O0O0O0O0O0O0O_zxco0o0o0o0 =86000 #line:114
own_zxco0o0o0o01 =0 #line:115
own_zxco0o0o0o02 =0 #line:116
own_zxco0o0o0o0 =0 #line:117
oOO0O0O0O0O0O0_OK =False #line:119
e_on =True #line:120
enter_on =False #line:121
twice =False #line:123
oOO0O0O0O0O0O0_num =1 #line:124
oOO0O0O0O0O0O0_one =False #line:125
websize =[1024 ,768 ]#line:128
Pxy =pg .size ()#line:129
Px1 =Pxy [0 ]/2 #line:130
Py2 =Pxy [1 ]/2 #line:131
Px =(Pxy [0 ]-websize [0 ])/2 #line:132
Py =(Pxy [1 ]-websize [1 ])/2 #line:133
P_relative =[[343 ,-66 ],[346 ,40 ],[96 ,121 ],[92 ,43 ],[201 ,100 ],[281 ,40 ],[221 ,37 ],[282 ,118 ]]#line:136
P_relative2 =[[647 ,-98 ],[650 ,8 ],[400 ,89 ],[396 ,11 ],[505 ,68 ],[585 ,8 ],[525 ,5 ],[586 ,86 ]]#line:137
Oo0o0Oo0o0o0 =[[0 ,0 ]for OO00OO0OO00OO00OO in range (len (P_relative ))]#line:138
for i in range (len (Oo0o0Oo0o0o0 )):#line:139
    Oo0o0Oo0o0o0 [i ][0 ]=Px1 +P_relative [i ][0 ]#line:140
    Oo0o0Oo0o0o0 [i ][1 ]=Py2 +P_relative [i ][1 ]#line:141
px_ajust ,py_ajust =0 ,0 #line:144
for i in range (len (P_relative )):#line:145
    P_relative [i ][0 ]+=websize [0 ]/2 +px_ajust #line:146
    P_relative [i ][1 ]+=websize [1 ]/2 +py_ajust #line:147
px_zxco0o0o0o0 =770 -171 #line:149
py_zxco0o0o0o0 =260 #line:150
px_zxco0o0o0o0frame =220 -191 #line:152
py_zxco0o0o0o0frame =480 #line:153
px_timeframe =245 #line:155
py_timeframe =350 #line:156
px_O0O0O0O0O0O0Ozxco0o0o0o0frame =245 #line:158
py_O0O0O0O0O0O0Ozxco0o0o0o0frame =290 #line:159
O0O0O0O0O0O0Ozxco0o0o0o0frame_pos =[px_O0O0O0O0O0O0Ozxco0o0o0o0frame ,py_O0O0O0O0O0O0Ozxco0o0o0o0frame ]#line:160
px_sdfsnisdfafzxcvframe =400 -215 #line:163
py_sdfsnisdfafzxcvframe =460 #line:164
px_mini =200 #line:168
py_mini =40 #line:169
Pricesize =[400 ,80 ]#line:171
Timesize =[200 ,50 ]#line:173
uioo0o000oo_area =[396 -80 ,11 -50 ,396 +80 ,11 +50 ]#line:176
sdfsf24324297_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:177
Px_zxco0o0o0o0 =Px +px_zxco0o0o0o0 #line:196
Py_zxco0o0o0o0 =Py +py_zxco0o0o0o0 #line:197
Pos_zxco0o0o0o0 =[Px_zxco0o0o0o0 ,Py_zxco0o0o0o0 ,Px_zxco0o0o0o0 +px_mini ,Py_zxco0o0o0o0 +py_mini ]#line:198
Px_zxco0o0o0o0frame =Px +px_zxco0o0o0o0frame #line:201
Py_zxco0o0o0o0frame =Py +py_zxco0o0o0o0frame #line:202
Pos_zxco0o0o0o0frame =[Px_zxco0o0o0o0frame ,Py_zxco0o0o0o0frame ]#line:203
Px_timeframe =px_timeframe #line:206
Py_timeframe =py_timeframe #line:207
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:208
Px_sdfsnisdfafzxcvframe =Px +px_sdfsnisdfafzxcvframe #line:211
Py_sdfsnisdfafzxcvframe =Py +py_sdfsnisdfafzxcvframe #line:212
Pos_sdfsnisdfafzxcvframe =[Px_sdfsnisdfafzxcvframe ,Py_sdfsnisdfafzxcvframe ]#line:213
px_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:221
py_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:222
Px_O0O0O0O0O0O0Ozxco0o0o0o0 =Px +px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:225
Py_O0O0O0O0O0O0Ozxco0o0o0o0 =Py +py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:226
O0O0O0O0O0O0Ozxco0o0o0o0_sizex =41 #line:227
O0O0O0O0O0O0Ozxco0o0o0o0_sizey =16 #line:228
px_relative =49 #line:230
py_relative =0 #line:231
px_sdfsf24324297 =656 #line:233
py_sdfsf24324297 =475 #line:234
Px_sdfsf24324297 =Px +px_sdfsf24324297 #line:235
Py_sdfsf24324297 =Py +py_sdfsf24324297 #line:236
sdfsf24324297_sizex =113 #line:237
sdfsf24324297_sizey =28 #line:238
sdfsf24324297_on =False #line:239
sdfsf24324297_need =False #line:240
sdfsf24324297_one =False #line:241
px_uioo0o000oo =550 #line:243
py_uioo0o000oo =413 #line:244
Px_uioo0o000oo =Px +px_uioo0o000oo #line:245
Py_uioo0o000oo =Py +py_uioo0o000oo #line:246
uioo0o000oo_sizex =108 #line:247
uioo0o000oo_sizey =21 #line:248
uioo0o000oo_on =False #line:249
uioo0o000oo_need =False #line:250
uioo0o000oo_one =False #line:251
oo0o0O0O0O0_interval =False #line:253
oOO0O0O0O0O0O0_interval =False #line:254
query_interval =False #line:255
query_on =False #line:256
import sys #line:259
if sys .platform !='win32':#line:260
    exit ()#line:261
import pyautogui as pg #line:262
import ctypes #line:263
from ctypes import wintypes #line:264
import win32con #line:265
import wx .html2 #line:266
import wx #line:267
import pickle #line:268
import wx .adv #line:269
from PIL import Image #line:270
import imagehash #line:271
import logging #line:348
timenow =time .time ()#line:349
time_local =time .localtime (timenow )#line:351
myapplog =time .strftime ("%Y%m%d%H%M%S",time_local )#line:353
print (myapplog )#line:354
logging .basicConfig (level =logging .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:359
logging .debug ('This is debug message')#line:361
logging .info ('This is info message')#line:362
logging .warning ('This is warning message')#line:363
logging .error ('This is error message')#line:364
import win32gui ,win32api #line:367
import cv2 #line:368
from PIL import ImageGrab #line:369
def Click (O00000000O000000O ,O0OOO0000OO0O0OO0 ):#line:370
    OO00O0OOOO00OO0OO =win32gui .GetCursorPos ()#line:371
    O00000000O000000O =int (O00000000O000000O )#line:372
    O0OOO0000OO0O0OO0 =int (O0OOO0000OO0O0OO0 )#line:373
    win32api .SetCursorPos ((O00000000O000000O ,O0OOO0000OO0O0OO0 ))#line:374
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,O00000000O000000O ,O0OOO0000OO0O0OO0 ,0 ,0 )#line:375
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,O00000000O000000O ,O0OOO0000OO0O0OO0 ,0 ,0 )#line:376
    win32api .SetCursorPos (OO00O0OOOO00OO0OO )#line:377
import win32clipboard #line:380
def Paste ():#line:381
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:383
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:384
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:385
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:386
def setText (OO0O00O00000000O0 ):#line:388
    OO0O00O00000000O0 =OO0O00O00000000O0 .encode ('utf-8')#line:389
    win32clipboard .OpenClipboard ()#line:390
    win32clipboard .EmptyClipboard ()#line:391
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,OO0O00O00000000O0 )#line:392
    win32clipboard .CloseClipboard ()#line:393
def findpos ():#line:396
    O0O0000OO00O0000O =ImageGrab .grab ().convert ('L')#line:398
    O00OO0O0000OOO000 =np .asarray (O0O0000OO00O0000O )#line:399
    global dick_target #line:400
    O00O000O000OO00O0 =dick_target [2 ]#line:401
    OO0000OO000O0O0OO ,OO000OOO00OO0O0O0 =O00O000O000OO00O0 .shape [::-1 ]#line:402
    OOOOOO0O0O0OO00O0 =cv2 .matchTemplate (O00OO0O0000OOO000 ,O00O000O000OO00O0 ,cv2 .TM_CCOEFF_NORMED )#line:404
    O000OOOOO000O0O00 ,O0000OOO00OOOOOO0 ,O0OOOOOO000O00OO0 ,OOOOOO0O00O0O0000 =cv2 .minMaxLoc (OOOOOO0O0O0OO00O0 )#line:405
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:410
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =OOOOOO0O00O0O0000 [0 ]+px_relative #line:411
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =OOOOOO0O00O0O0000 [1 ]+py_relative #line:412
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:413
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:414
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:416
    for O0000OO00O00O0000 in range (len (Oo0o0Oo0o0o0 )):#line:417
        Oo0o0Oo0o0o0 [O0000OO00O00O0000 ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0000OO00O00O0000 ][0 ]#line:418
        Oo0o0Oo0o0o0 [O0000OO00O00O0000 ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0000OO00O00O0000 ][1 ]#line:419
    uioo0o000oo_area =[396 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:420
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:421
    global findpos_on #line:423
    findpos_on =False #line:424
def finduioo0o000oo ():#line:426
    global dick_target ,uioo0o000oo_on ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:427
    OO0O0000OOOO0OO0O =dick_target [0 ]#line:428
    O0O0O0O000O00OO0O =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:429
    OO00000O0O0O000O0 =np .asarray (O0O0O0O000O00OO0O )#line:430
    O00O0000O000O0OOO ,OOOO0000O0O000OO0 =OO0O0000OOOO0OO0O .shape [::-1 ]#line:431
    OO0OOOO000O0O00O0 =cv2 .matchTemplate (OO00000O0O0O000O0 ,OO0O0000OOOO0OO0O ,cv2 .TM_CCOEFF_NORMED )#line:432
    O0000000OOOOO000O ,O0O00OO0OOO0OOO00 ,O00O0000O00OOOOOO ,O00OO0O00O00O0OO0 =cv2 .minMaxLoc (OO0OOOO000O0O00O0 )#line:433
    if O0O00OO0OOO0OOO00 >=0.9 :#line:435
        uioo0o000oo_on =True #line:436
def findsdfsf24324297 ():#line:439
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:440
    OOOOOO0OO000OO000 =dick_target [1 ]#line:441
    O00O0O00O0OOO0000 =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:442
    O000OO0OO00OO0000 =np .asarray (O00O0O00O0OOO0000 )#line:443
    O0OO000OO000O0OO0 ,OO00O00000OO00OOO =OOOOOO0OO000OO000 .shape [::-1 ]#line:444
    OOO0O0O0OOOO0O000 =cv2 .matchTemplate (O000OO0OO00OO0000 ,OOOOOO0OO000OO000 ,cv2 .TM_CCOEFF_NORMED )#line:445
    OOOOO000O0O0000OO ,O0O0OOOOO00O0O0OO ,O0O0OOOOOOOOOOO0O ,OOOOOO0O000OO0OO0 =cv2 .minMaxLoc (OOO0O0O0OOOO0O000 )#line:446
    print (O0O0OOOOO00O0O0OO )#line:447
    if O0O0OOOOO00O0O0OO >=0.9 :#line:448
        sdfsf24324297_on =True #line:449
SZ =20 #line:453
bin_n =16 #line:454
import numpy as np #line:455
def hog (O0O0OOO0OOOO0OO00 ):#line:458
    OOO0000OOOO0O0O00 =cv2 .Sobel (O0O0OOO0OOOO0OO00 ,cv2 .CV_32F ,1 ,0 )#line:459
    O0000000OO0OO0OOO =cv2 .Sobel (O0O0OOO0OOOO0OO00 ,cv2 .CV_32F ,0 ,1 )#line:460
    O0OO0000000000OO0 ,O0O0O0OO0OOOO0O0O =cv2 .cartToPolar (OOO0000OOOO0O0O00 ,O0000000OO0OO0OOO )#line:461
    OO000OOO000OO0O00 =np .int32 (bin_n *O0O0O0OO0OOOO0O0O /(2 *np .pi ))#line:462
    OOOOOOOO0OO0OO000 =OO000OOO000OO0O00 [:10 ,:10 ],OO000OOO000OO0O00 [10 :,:10 ],OO000OOO000OO0O00 [:10 ,10 :],OO000OOO000OO0O00 [10 :,10 :]#line:463
    O00O0000OO00000OO =O0OO0000000000OO0 [:10 ,:10 ],O0OO0000000000OO0 [10 :,:10 ],O0OO0000000000OO0 [:10 ,10 :],O0OO0000000000OO0 [10 :,10 :]#line:464
    O0OOOO0OOO0O0O00O =[np .bincount (OO0OO00O000OO0O00 .ravel (),OOO0OO0O000O0O0OO .ravel (),bin_n )for OO0OO00O000OO0O00 ,OOO0OO0O000O0O0OO in zip (OOOOOOOO0OO0OO000 ,O00O0000OO00000OO )]#line:465
    OO000O0OO00O00OOO =np .hstack (O0OOOO0OOO0O0O00O )#line:466
    return OO000O0OO00O00OOO #line:467
def cut (O0OOOOOOOO0O0O0O0 ):#line:471
    O0O00OOOOOOOOO000 ,O00OOOOOO00O00O0O =cv2 .threshold (O0OOOOOOOO0O0O0O0 ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:472
    O0OO0O0O0O00OO0OO ,OO00000OOOOO0O000 ,O000000000O000O00 =cv2 .findContours (O00OOOOOO00O00O0O ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:474
    OOO0000O000OOOO0O =[]#line:475
    O0O000OOO00O00O00 =[]#line:476
    for O0OO0O00000O00OOO in range (len (OO00000OOOOO0O000 )):#line:477
        OO00OOO0OO000OOOO =OO00000OOOOO0O000 [O0OO0O00000O00OOO ]#line:478
        OOOO0O00OO00OO000 ,O000O0OOO0O00000O ,OO0O00OOOOO0OOOOO ,O0000OO0000OO0000 =cv2 .boundingRect (OO00OOO0OO000OOOO )#line:479
        O0O000OOO00O00O00 .append ([OOOO0O00OO00OO000 ,O000O0OOO0O00000O ,OO0O00OOOOO0OOOOO ,O0000OO0000OO0000 ])#line:481
    O0O000OOO00O00O00 =sorted (O0O000OOO00O00O00 )#line:483
    for O0OO0O00000O00OOO in range (len (OO00000OOOOO0O000 )):#line:484
        OOOO0O00OO00OO000 ,O000O0OOO0O00000O ,OO0O00OOOOO0OOOOO ,O0000OO0000OO0000 =O0O000OOO00O00O00 [O0OO0O00000O00OOO ]#line:485
        OOO0000O000OOOO0O .append (O0OO0O0O0O00OO0OO [O000O0OOO0O00000O :O000O0OOO0O00000O +O0000OO0000OO0000 ,OOOO0O00OO00OO000 :OOOO0O00OO00OO000 +OO0O00OOOOO0OOOOO ])#line:486
    return OOO0000O000OOOO0O #line:487
def readpic (O0O00OOO000O0OO0O ):#line:489
    try :#line:490
        O0000OO0000OOO000 =cv2 .ml .SVM_load ('maindata.xml')#line:491
        OO000O0O0000OOOOO =cut (O0O00OOO000O0OO0O )#line:492
        OO000O0O0000OOOOO =list (map (hog ,OO000O0O0000OOOOO ))#line:493
        OO000O0O0000OOOOO =np .float32 (OO000O0O0000OOOOO ).reshape (-1 ,64 )#line:494
        O00O0OO0OO00OO0O0 =O0000OO0000OOO000 .predict (OO000O0O0000OOOOO )#line:495
        O00O0OO0OO00OO0O0 =O00O0OO0OO00OO0O0 [1 ].reshape (-1 ).astype (int ).astype (str )#line:496
        OO00O00OO0000OO00 ="".join (list (O00O0OO0OO00OO0O0 ))#line:497
        return OO00O00OO0000OO00 #line:498
    except :#line:499
        return False #line:500
import smtplib #line:518
from email .mime .text import MIMEText #line:521
import os #line:522
import mimetypes #line:523
import email #line:524
from email .mime .multipart import MIMEMultipart #line:525
from threading import Thread #line:528
import threading #line:529
from wx .lib .pubsub import pub #line:530
import socket ,sys ,json #line:535
timeout =10 #line:536
socket .setdefaulttimeout (timeout )#line:537
def ConfirmUser ():#line:539
    OO0OO00OOOOO000OO =host_ali #line:540
    O0O0OO0O0O000O000 =8080 #line:543
    OO00OOO0O00O00OOO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:545
    try :#line:547
        OO00OOO0O00O00OOO .connect ((OO0OO00OOOOO000OO ,O0O0OO0O0O000O000 ))#line:548
    except socket .gaierror as OO000000OOOO0O0OO :#line:549
        logging .error ('连接失败 %s'%OO000000OOOO0O0OO )#line:550
        logging .error ("Address-related error connecting to server: %s"%OO000000OOOO0O0OO )#line:551
        return 'net error'#line:552
    except socket .error as OO000000OOOO0O0OO :#line:554
        logging .error ('连接失败 %s'%OO000000OOOO0O0OO )#line:555
        logging .error ("Connection error: %s"%OO000000OOOO0O0OO )#line:556
        return 'net error'#line:557
    OOO00000000O0OOOO =['login',Username ,Password ]#line:561
    OOO00000000O0OOOO =json .dumps (OOO00000000O0OOOO )#line:562
    OOO00000000O0OOOO =bytes (OOO00000000O0OOOO ,encoding ="utf-8")#line:563
    logging .info ('发送信息 %s'%str (OOO00000000O0OOOO ,encoding ="utf-8"))#line:564
    OO00OOO0O00O00OOO .send (OOO00000000O0OOOO )#line:565
    OO00OOO0O00O00OOO .shutdown (1 )#line:567
    logging .info ("Submit Complete")#line:568
    print ("Submit Complete")#line:569
    try :#line:570
        OO0000OOOOO0O0OO0 =OO00OOO0O00O00OOO .recv (1024 )#line:572
        print (OO0000OOOOO0O0OO0 )#line:573
        OO0000OOOOO0O0OO0 =str (OO0000OOOOO0O0OO0 ,encoding ="utf-8")#line:574
        OO0000OOOOO0O0OO0 =json .loads (OO0000OOOOO0O0OO0 )#line:575
        print (OO0000OOOOO0O0OO0 )#line:576
        O0O0OOO00O0OO0OOO =OO0000OOOOO0O0OO0 [0 ]#line:577
        if O0O0OOO00O0OO0OOO =='success':#line:578
            logging .info ('登录成功 %s'%O0O0OOO00O0OO0OOO )#line:579
            global url2 #line:580
            url2 =OO0000OOOOO0O0OO0 [1 ]#line:581
            return 'login success'#line:582
        elif O0O0OOO00O0OO0OOO =='wrong password':#line:583
            logging .warning ('密码错误 %s'%O0O0OOO00O0OO0OOO )#line:584
            return 'wrong password'#line:585
        elif O0O0OOO00O0OO0OOO =="wrong account":#line:586
            logging .warning ('账号错误 %s'%O0O0OOO00O0OO0OOO )#line:587
            return 'wrong account'#line:588
        elif O0O0OOO00O0OO0OOO =='repeat':#line:589
            logging .warning ('账号错误 %s'%O0O0OOO00O0OO0OOO )#line:590
            return 'repeat'#line:591
    except :#line:592
        print ("连接失败")#line:593
        logging .warning ('连接失败 ')#line:594
        return False #line:595
def Logout ():#line:598
    OOO0OOO0O0OO00O0O =host_ali #line:599
    O000000OOOOO0O000 =8080 #line:602
    global Username #line:603
    O0000O0O00OOO0OO0 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:604
    try :#line:605
        O0000O0O00OOO0OO0 .connect ((OOO0OOO0O0OO00O0O ,O000000OOOOO0O000 ))#line:606
    except socket .gaierror as O00O00O0OO0O0O000 :#line:607
        print ("Address-related error connecting to server: %s"%O00O00O0OO0O0O000 )#line:608
        logging .info ("Address-related error connecting to server: %s"%O00O00O0OO0O0O000 )#line:609
    except socket .error as O00O00O0OO0O0O000 :#line:611
        print ("Connection error: %s"%O00O00O0OO0O0O000 )#line:612
        logging .info ("Connection error: %s"%O00O00O0OO0O0O000 )#line:613
    OOOO000O000OO00OO =['logout',Username ,Password ]#line:617
    OOOO000O000OO00OO =json .dumps (OOOO000O000OO00OO )#line:618
    OOOO000O000OO00OO =bytes (OOOO000O000OO00OO ,encoding ="utf-8")#line:619
    logging .info ('发送信息 %s'%str (OOOO000O000OO00OO ,encoding ="utf-8"))#line:620
    O0000O0O00OOO0OO0 .send (OOOO000O000OO00OO )#line:621
    O0000O0O00OOO0OO0 .shutdown (1 )#line:622
    print ("Submit Log Out Complete")#line:623
    logging .info ("Submit Log Out Complete")#line:624
def Keeplogin ():#line:627
    OO000OOOO0OO0000O =host_ali #line:628
    OOO0OOOOOOO00O000 =8080 #line:631
    global Username #line:632
    OOOOO0O0O0O0O0O0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:633
    try :#line:634
        OOOOO0O0O0O0O0O0O .connect ((OO000OOOO0OO0000O ,OOO0OOOOOOO00O000 ))#line:635
    except socket .gaierror as OO0OOO0O000O000OO :#line:636
        print ("Address-related error connecting to server: %s"%OO0OOO0O000O000OO )#line:637
        logging .info ("Address-related error connecting to server: %s"%OO0OOO0O000O000OO )#line:638
    except socket .error as OO0OOO0O000O000OO :#line:640
        print ("Connection error: %s"%OO0OOO0O000O000OO )#line:641
        logging .info ("Connection error: %s"%OO0OOO0O000O000OO )#line:642
    OO0OO0OOO0000O00O =['keep',Username ,Password ]#line:646
    OO0OO0OOO0000O00O =json .dumps (OO0OO0OOO0000O00O )#line:647
    OO0OO0OOO0000O00O =bytes (OO0OO0OOO0000O00O ,encoding ="utf-8")#line:648
    logging .info ('发送信息 %s'%str (OO0OO0OOO0000O00O ,encoding ="utf-8"))#line:649
    OOOOO0O0O0O0O0O0O .send (OO0OO0OOO0000O00O )#line:650
    OOOOO0O0O0O0O0O0O .shutdown (1 )#line:652
    print ("Submit keep Complete")#line:653
    logging .info ("Submit keep Complete")#line:654
def send_mail (O0OOO000000O0OO00 ,O000O0OOO00000000 ,OOOO0000OOO0OO000 ):#line:657
    OOO00O0OOO000000O =open (OOOO0000OOO0OO000 ,'rb')#line:658
    OO00O0O0O00OO0O00 ,O00O0O00OO00OOOOO =mimetypes .guess_type (OOOO0000OOO0OO000 )#line:659
    if OO00O0O0O00OO0O00 is None and O00O0O00OO00OOOOO is None :#line:660
        OO00O0O0O00OO0O00 ='application/octet-stream'#line:661
    O00OO0O0000OO0O00 ,OOO00O000OO00O0O0 =OO00O0O0O00OO0O00 .split ('/',1 )#line:662
    OO0O0OOOO000O00OO =email .mime .base .MIMEBase (O00OO0O0000OO0O00 ,OOO00O000OO00O0O0 )#line:663
    OO0O0OOOO000O00OO .set_payload (OOO00O0OOO000000O .read ())#line:664
    OOO00O0OOO000000O .close ()#line:665
    email .encoders .encode_base64 (OO0O0OOOO000O00OO )#line:666
    OOOO000O00O00O00O =os .path .basename (OOOO0000OOO0OO000 )#line:667
    OO0O0OOOO000O00OO .add_header ('Content-Disposition','attachment',filename =OOOO000O00O00O00O )#line:668
    O000O0OOO00000000 =O000O0OOO00000000 #line:669
    O00OO0OO0OO0O0O0O ='smtp.qq.com'#line:670
    OOOOOOO0O0OOO0OO0 =os .environ .get ('MAIL_USERNAME')#line:671
    O0O0O000O0OOO00O0 =os .environ .get ('MAIL_PASSWORD')#line:672
    OO0OOO0OOO0OO00O0 =OOOOOOO0O0OOO0OO0 #line:673
    O00O0OOOO0O0O00OO =MIMEMultipart ()#line:674
    O00O0OOOO0O0O00OO .attach (OO0O0OOOO000O00OO )#line:675
    O00O0OOOO0O0O00OO ['Subject']=O0OOO000000O0OO00 #line:676
    O00O0OOOO0O0O00OO ['From']=OO0OOO0OOO0OO00O0 #line:677
    O00O0OOOO0O0O00OO ['To']=";".join (O000O0OOO00000000 )#line:678
    O00O0O0OOO00O0OOO =smtplib .SMTP_SSL (O00OO0OO0OO0O0O0O ,465 )#line:679
    O00O0O0OOO00O0OOO .login (OOOOOOO0O0OOO0OO0 ,O0O0O000O0OOO00O0 )#line:680
    print ('login in  successfully')#line:681
    O00O0O0OOO00O0OOO .sendmail (OO0OOO0OOO0OO00O0 ,O000O0OOO00000000 ,O00O0OOOO0O0O00OO .as_string ())#line:682
    O00O0O0OOO00O0OOO .quit ()#line:683
    print ('send email  successfully')#line:684
def Upload ():#line:686
    pass #line:687
def Com_read ():#line:690
    pass #line:691
def Com_decision ():#line:695
    pass #line:696
class TopFrame (wx .Frame ):#line:729
    def __init__ (O0OOO0OO00OO00OOO ,OOO00000OOOOOOOO0 ,O0OO00000OOOO0000 ):#line:730
        wx .Frame .__init__ (O0OOO0OO00OO00OOO ,None ,-1 ,OOO00000OOOOOOOO0 ,size =(520 ,320 ))#line:732
        O0OOO0OO00OO00OOO .Bind (wx .EVT_CLOSE ,O0OOO0OO00OO00OOO .OnClose )#line:733
        O00000OO0O0OO0OOO =time .time ()#line:737
        O0OOO0OO00OO00OOO .statusbar =O0OOO0OO00OO00OOO .CreateStatusBar ()#line:741
        O0OOO0OO00OO00OOO .statusbar .SetFieldsCount (3 )#line:743
        O0OOO0OO00OO00OOO .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:744
        O0OOO0OO00OO00OOO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:746
        O0OOO0OO00OO00OOO .SetIcon (O0OOO0OO00OO00OOO .icon )#line:747
        O0OOO0OO00OO00OOO .statusbar .SetStatusText (u"版本号",0 )#line:749
        O0OOO0OO00OO00OOO .statusbar .SetStatusText (u"%s"%O0OO00000OOOO0000 ,1 )#line:752
        O0OOO0OO00OO00OOO .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:755
        O0OOO0OO00OO00OOO .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:756
        O0O00OO00OO0OO0OO =wx .Panel (O0OOO0OO00OO00OOO ,-1 )#line:758
        O0O00OO00OO0OO0OO .SetBackgroundColour ((240 ,255 ,255 ))#line:760
        O0OOO0OO00OO00OOO .SetBackgroundColour ((240 ,255 ,255 ))#line:761
        O0OOO0OO00OO00OOO .thread =TimeThread ()#line:789
        O0OOO0OO00OO00OOO .keepthread =KeepThread ()#line:790
        O0OOO0OO00OO00OOO .button5 =wx .Button (O0O00OO00OO0OO0OO ,label ='打开模拟',pos =(190 ,190 ))#line:818
        O0OOO0OO00OO00OOO .Bind (wx .EVT_BUTTON ,O0OOO0OO00OO00OOO .Openo0sdofsfo0sodf0so0 ,O0OOO0OO00OO00OOO .button5 )#line:819
        O0OOO0OO00OO00OOO .button6 =wx .Button (O0O00OO00OO0OO0OO ,label ='打开国拍',pos =(280 ,190 ))#line:821
        O0OOO0OO00OO00OOO .Bind (wx .EVT_BUTTON ,O0OOO0OO00OO00OOO .OpenGuopai ,O0OOO0OO00OO00OOO .button6 )#line:822
        O0OOO0OO00OO00OOO .button16 =wx .Button (O0O00OO00OO0OO0OO ,label ='修改国拍网址',pos =(370 ,190 ))#line:824
        O0OOO0OO00OO00OOO .Bind (wx .EVT_BUTTON ,O0OOO0OO00OO00OOO .UrlGuopai ,O0OOO0OO00OO00OOO .button16 )#line:825
        O0OOO0OO00OO00OOO .urlText =wx .TextCtrl (O0O00OO00OO0OO0OO ,-1 ,pos =(370 ,230 ),size =(120 ,25 ))#line:826
        O0OOO0OO00OO00OOO .button7 =wx .Button (O0O00OO00OO0OO0OO ,label ='显示帮助',pos =(10 ,190 ))#line:828
        O0OOO0OO00OO00OOO .Bind (wx .EVT_BUTTON ,O0OOO0OO00OO00OOO .Help ,O0OOO0OO00OO00OOO .button7 )#line:829
        O0OOO0OO00OO00OOO .button8 =wx .Button (O0O00OO00OO0OO0OO ,label ='验证码练习',pos =(100 ,190 ))#line:831
        O0OOO0OO00OO00OOO .Bind (wx .EVT_BUTTON ,O0OOO0OO00OO00OOO .Yan_practice ,O0OOO0OO00OO00OOO .button8 )#line:832
        O0OOO0OO00OO00OOO .timer2 =wx .Timer (O0OOO0OO00OO00OOO )#line:872
        O0OOO0OO00OO00OOO .Bind (wx .EVT_TIMER ,O0OOO0OO00OO00OOO .MainControl ,O0OOO0OO00OO00OOO .timer2 )#line:873
        O0OOO0OO00OO00OOO .timer2 .Start (100 )#line:874
        O0OOO0OO00OO00OOO .timer3 =wx .Timer (O0OOO0OO00OO00OOO )#line:882
        O0OOO0OO00OO00OOO .Bind (wx .EVT_TIMER ,O0OOO0OO00OO00OOO .Lowest_zxco0o0o0o0 ,O0OOO0OO00OO00OOO .timer3 )#line:883
        O0OOO0OO00OO00OOO .timer3 .Start (100 )#line:884
        O0OOO0OO00OO00OOO .timer4 =wx .Timer (O0OOO0OO00OO00OOO )#line:886
        O0OOO0OO00OO00OOO .Bind (wx .EVT_TIMER ,O0OOO0OO00OO00OOO .Find_pos ,O0OOO0OO00OO00OOO .timer4 )#line:887
        O0OOO0OO00OO00OOO .timer4 .Start (150 )#line:888
        O0OOO0OO00OO00OOO .operationframe =OperationFrame ()#line:897
        O0OOO0OO00OO00OOO .operationframe .Show (False )#line:898
    def Lowest_zxco0o0o0o0 (OOOOOO00OO0OOO0O0 ,O000O00OOO00000O0 ):#line:908
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on #line:909
        if not findpos_on :#line:910
            OOO00OO000OO00OOO =int (TopFrame .Price_read ())#line:911
            if OOO00OO000OO00OOO in zxco0o0o0o0list :#line:913
                O0O0O0O0O0O0O_zxco0o0o0o0 =OOO00OO000OO00OOO #line:914
            else :#line:915
                findpos_on =True #line:916
    def Find_pos (OOO0OO0OO0000O00O ,O0O0OO0O00O00O000 ):#line:933
        global findpos_on #line:934
        if findpos_on :#line:935
            findpos ()#line:936
    @staticmethod #line:942
    def Confirm ():#line:943
        global cf_hash ,sdfsf24324297_on #line:944
        O0O000O0OO0000OO0 =TopFrame .Confirm_hash ()#line:945
        if O0O000O0OO0000OO0 ==cf_hash [0 ]:#line:946
            sdfsf24324297_on =True #line:947
    @staticmethod #line:948
    def Refresh ():#line:949
        OO0000000O00OOO00 =TopFrame .Refresh_hash ()#line:950
        global cf_hash ,uioo0o000oo_on #line:951
        if OO0000000O00OOO00 ==cf_hash [1 ]:#line:952
            uioo0o000oo_on =True #line:953
    @staticmethod #line:962
    def Price_read ():#line:963
        O0OOOO00O0O0OO000 =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:965
        O0OOOO00O0O0OO000 =np .asarray (O0OOOO00O0O0OO000 )#line:971
        OO0OOO00O0O000000 =readpic (O0OOOO00O0O0OO000 )#line:972
        return OO0OOO00O0O000000 #line:974
    @staticmethod #line:977
    def Price_hash ():#line:978
        O0O0OOO000OO00OO0 =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:980
        global num #line:981
        num +=1 #line:982
        O0O0O0OO0OO0000OO =imagehash .dhash (O0O0OOO000OO00OO0 )#line:984
        return O0O0O0OO0OO0000OO #line:987
    @staticmethod #line:989
    def Confirm_hash ():#line:990
        O0000OO0O000OOO00 =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:992
        O0O000OOOO0OOO00O =imagehash .dhash (O0000OO0O000OOO00 )#line:995
        return O0O000OOOO0OOO00O #line:996
    @staticmethod #line:998
    def Refresh_hash ():#line:999
        OOOOOOO0OO0OOO0OO =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:1001
        OO000OO0OO0000O0O =imagehash .dhash (OOOOOOO0OO0OOO0OO )#line:1003
        return OO000OO0OO0000O0O #line:1004
    def OnEraseBackground (O00000O00OO0O0OO0 ,OO00O000O0OO00O0O ):#line:1008
        ""#line:1011
        O0OO00O0OOO00O00O =OO00O000O0OO00O0O .GetDC ()#line:1012
        if not O0OO00O0OOO00O00O :#line:1013
            O0OO00O0OOO00O00O =wx .ClientDC (O00000O00OO0O0OO0 )#line:1014
            OOO0O0O0O000OO0O0 =O00000O00OO0O0OO0 .GetUpdateRegion ().GetBox ()#line:1015
            O0OO00O0OOO00O00O .SetClippingRect (OOO0O0O0O000OO0O0 )#line:1016
        O0OO00O0OOO00O00O .Clear ()#line:1017
        OO00O0O000OO00O0O =wx .Bitmap ("blue.jpg")#line:1018
        O0OO00O0OOO00O00O .DrawBitmap (OO00O0O000OO00O0O ,0 ,0 )#line:1019
    def OnClose (O00OO0O00OO0OOO00 ,O00OO0OO00OOO0O0O ):#line:1023
        OO0O0O0OOOO0OOO0O =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1024
        if OO0O0O0OOOO0OOO0O ==wx .OK :#line:1025
            import sys as OO000OO00OO0000O0 #line:1027
            O00OO0O00OO0OOO00 .Show (False )#line:1032
            try :#line:1034
                O00OO0O00OO0OOO00 .Close_time1 (O00OO0OO00OOO0O0O )#line:1035
                O00OO0O00OO0OOO00 .Close_time2 (O00OO0OO00OOO0O0O )#line:1036
            except :#line:1037
                pass #line:1038
            Logout ()#line:1040
            wx .GetApp ().ExitMainLoop ()#line:1041
            O00OO0OO00OOO0O0O .Skip ()#line:1042
            OO000OO00OO0000O0 .exit (None )#line:1043
    def OnOpenAssist (O000OO0O0OO0OO0O0 ):#line:1047
        O000OO0O0OO0OO0O0 .Open ()#line:1048
        global do #line:1049
        if do :#line:1050
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1051
        else :#line:1052
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1053
        O000OO0O0OO0OO0O0 .Listen ()#line:1054
    @classmethod #line:1056
    def OnCloseAssist (O0O00O000OO000000 ):#line:1057
        O0O00O000OO000000 .Close ()#line:1058
    def OnViewPos (OOOOO000O0O00O000 ,OOOOOO00O00000O0O ):#line:1065
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1066
        OOOOO000O0O00O000 .MovePos (OOOOOO00O00000O0O )#line:1067
        global view #line:1068
        if not view :#line:1069
            view =True #line:1070
            for O0O00O00OOO0O00O0 in range (len (Oo0o0Oo0o0o0 )):#line:1071
                OOOOO000O0O00O000 .posframe [O0O00O00OOO0O00O0 ].Show (view )#line:1072
        else :#line:1073
            view =False #line:1074
            for O0O00O00OOO0O00O0 in range (len (Oo0o0Oo0o0o0 )):#line:1075
                OOOOO000O0O00O000 .posframe [O0O00O00OOO0O00O0 ].Hide ()#line:1076
    def OnSavePos (O000O0O000O0OO0O0 ,OOO0O0OOOO000OO0O ):#line:1079
        O000O0O000O0OO0O0 .MovePos (OOO0O0OOOO000OO0O )#line:1080
        O000O0O000O0OO0O0 .Save_log ()#line:1081
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1082
    def MovePos (OO0O0O000O00O0000 ,O0OOOOOOOOO0OO000 ):#line:1088
        global Positon #line:1089
        for O00OOOO0O0OO0O0OO in range (5 ):#line:1090
            OO0OOOO0OOOO0O00O ,O0O0OO0O0OOOOOOOO =Oo0o0Oo0o0o0 [O00OOOO0O0OO0O0OO ]#line:1091
            OO0O0O000O00O0000 .posframe [O00OOOO0O0OO0O0OO ].Move (OO0OOOO0OOOO0O00O -10 ,O0O0OO0O0OOOOOOOO -5 )#line:1092
    def Openo0sdofsfo0sodf0so0 (O0OO0OO0OOOO0O0OO ,O00000000OOOOO0O0 ):#line:1094
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1096
        ghjo0o0o0o0_on =True #line:1097
        O00OO0O0OO0O00O00 =True #line:1098
        oo0o0O0O0O0_on =True #line:1099
        oOO0O0O0O0O0O0_on =False #line:1100
        oOO0O0O0O0O0O0_num =1 #line:1101
        oOO0O0O0O0O0O0_OK =False #line:1102
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,ooweo0o0werwr_on ,o0sdofsfo0sodf0so0_on ,ghjo0o0o0o0_repeat #line:1103
        if ooweo0o0werwr_on :#line:1104
            wx .MessageBox ('请关闭国拍页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1105
        elif o0sdofsfo0sodf0so0_on :#line:1106
            wx .MessageBox ('请关闭模拟页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1107
        else :#line:1108
            O0OO0OO0OOOO0O0OO .Open ()#line:1113
            if do :#line:1114
                o0sdofsfo0sodf0so0_on =True #line:1115
                ad_view =True #line:1116
                web_on =True #line:1117
                O0OO0OO0OOOO0O0OO .fr =WebFrame (Px ,Py ,False ,'小鲜肉模拟')#line:1118
                O0OO0OO0OOOO0O0OO .operationframe .Show (True )#line:1119
                if time_on :#line:1121
                    O0OO0OO0OOOO0O0OO .operationframe .Opentime ()#line:1122
                if not ghjo0o0o0o0_repeat :#line:1123
                    O0OO0OO0OOOO0O0OO .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1124
                    O0OO0OO0OOOO0O0OO .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1125
                    ghjo0o0o0o0_repeat =True #line:1126
                OOOOO0O0O0O000OOO =wx .html2 .WebView .New (O0OO0OO0OOOO0O0OO .fr ,size =(websize [0 ],websize [1 ]),pos =(0 ,0 ))#line:1129
                OOOOO0O0O0O000OOO .LoadURL (url1 )#line:1130
                OOOOO0O0O0O000OOO .CanSetZoomType (False )#line:1131
                O0OO0OO0OOOO0O0OO .fr .Show ()#line:1132
            else :#line:1136
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1137
                O0OO0OO0OOOO0O0OO .Close ()#line:1138
            O0OO0OO0OOOO0O0OO .Listen ()#line:1139
    def OpenGuopai (OO0O00OOO0O00O000 ,OOOOOO0OOO0O00O00 ):#line:1189
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1191
        ghjo0o0o0o0_on =True #line:1192
        O000OO0O00OO0O000 =True #line:1193
        oo0o0O0O0O0_on =True #line:1194
        oOO0O0O0O0O0O0_on =False #line:1195
        oOO0O0O0O0O0O0_num =1 #line:1196
        oOO0O0O0O0O0O0_OK =False #line:1197
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1198
        if o0sdofsfo0sodf0so0_on :#line:1199
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1200
        elif ooweo0o0werwr_on :#line:1201
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1202
        else :#line:1203
            OO0O00OOO0O00O000 .Open ()#line:1205
            if do :#line:1209
                ad_view =True #line:1210
                ooweo0o0werwr_on =True #line:1211
                OO0O00OOO0O00O000 .fr =WebFrame (Px ,Py ,False ,'小鲜肉代拍 国拍')#line:1212
                OO0O00OOO0O00O000 .operationframe .Show (True )#line:1213
                if time_on :#line:1215
                    OO0O00OOO0O00O000 .operationframe .Opentime ()#line:1216
                if not ghjo0o0o0o0_repeat :#line:1217
                    OO0O00OOO0O00O000 .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1218
                    OO0O00OOO0O00O000 .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1219
                    ghjo0o0o0o0_repeat =True #line:1220
                O000OO0O00O00O00O =wx .html2 .WebView .New (OO0O00OOO0O00O000 .fr ,size =(websize [0 ],websize [1 ]))#line:1222
                O000OO0O00O00O00O .LoadURL (url2 )#line:1223
                O000OO0O00O00O00O .CanSetZoomType (False )#line:1224
                OO0O00OOO0O00O000 .fr .Show ()#line:1225
            else :#line:1229
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1230
                OO0O00OOO0O00O000 .Close ()#line:1231
            OO0O00OOO0O00O000 .Listen ()#line:1232
    def UrlGuopai (OO0O000O0O0O0O000 ,O0O000OOOOOO0000O ):#line:1234
        global url2 #line:1235
        try :#line:1236
            url2 =OO0O000O0O0O0O000 .urlText .GetValue ()#line:1237
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1238
        except :#line:1239
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1240
    def Help (O000000O0OO0O0000 ,OOOOO0O00OO000O0O ):#line:1243
        OOOO0OOOO0O000O00 ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1249
        OO00O00OOO00OO0OO =wx .adv .AboutDialogInfo ()#line:1252
        OO00O00OOO00OO0OO .SetName ("小鲜肉拍牌")#line:1253
        OO00O00OOO00OO0OO .SetVersion (OOOO0OOOO0O000O00 )#line:1254
        OO00O00OOO00OO0OO .AddDeveloper ("ZS")#line:1258
        wx .adv .AboutBox (OO00O00OOO00OO0OO )#line:1259
    def Yan_practice (O0O0OOO0O0O0O0O0O ,OO00OO0000000O0O0 ):#line:1261
        pass #line:1262
    def Time_adjust (OOOO0OO0OO0OOOO0O ,OOOO0O0O00OO000OO ):#line:1264
        pass #line:1265
    @staticmethod #line:1275
    def OnJiajia ():#line:1276
        OO00O0OO00O000OOO =pg .position ()#line:1277
        Oo0o0Oo0o0o0 [0 ][0 ]=OO00O0OO00O000OOO [0 ]#line:1278
        Oo0o0Oo0o0o0 [0 ][1 ]=OO00O0OO00O000OOO [1 ]#line:1279
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1280
        findpos ()#line:1281
    @staticmethod #line:1284
    def OnChujia ():#line:1285
        O0OO0OOO0OOO000OO =pg .position ()#line:1286
        Oo0o0Oo0o0o0 [1 ][0 ]=O0OO0OOO0OOO000OO [0 ]#line:1287
        Oo0o0Oo0o0o0 [1 ][1 ]=O0OO0OOO0OOO000OO [1 ]#line:1288
    @staticmethod #line:1289
    def OnTijiao ():#line:1290
        OOO00O0000O0O0000 =pg .position ()#line:1291
        Oo0o0Oo0o0o0 [2 ][0 ]=OOO00O0000O0O0000 [0 ]#line:1292
        Oo0o0Oo0o0o0 [2 ][1 ]=OOO00O0000O0O0000 [1 ]#line:1293
    @staticmethod #line:1294
    def OnShuaxin ():#line:1295
        O0OOOO0O0OO0O0OO0 =pg .position ()#line:1296
        Oo0o0Oo0o0o0 [3 ][0 ]=O0OOOO0O0OO0O0OO0 [0 ]#line:1297
        Oo0o0Oo0o0o0 [3 ][1 ]=O0OOOO0O0OO0O0OO0 [1 ]#line:1298
    @staticmethod #line:1299
    def OnConfirm ():#line:1300
        OO0OOO0O00OOOOO00 =pg .position ()#line:1301
        Oo0o0Oo0o0o0 [4 ][0 ]=OO0OOO0O00OOOOO00 [0 ]#line:1302
        Oo0o0Oo0o0o0 [4 ][1 ]=OO0OOO0O00OOOOO00 [1 ]#line:1303
    @staticmethod #line:1304
    def OnYanzhengma ():#line:1305
        OO0O000O0O00O00O0 =pg .position ()#line:1306
        Oo0o0Oo0o0o0 [5 ][0 ]=OO0O000O0O00O00O0 [0 ]#line:1307
        Oo0o0Oo0o0o0 [5 ][1 ]=OO0O000O0O00O00O0 [1 ]#line:1308
    @staticmethod #line:1311
    def handle_Jiajia ():#line:1312
        TopFrame .OnJiajia ()#line:1313
    @staticmethod #line:1314
    def handle_Chujia ():#line:1315
        TopFrame .OnChujia ()#line:1316
    @staticmethod #line:1317
    def handle_Tijiao ():#line:1318
        TopFrame .OnTijiao ()#line:1319
    @staticmethod #line:1320
    def handle_Shuaxin ():#line:1321
        TopFrame .OnShuaxin ()#line:1322
    @staticmethod #line:1323
    def handle_Confirm ():#line:1324
        TopFrame .OnConfirm ()#line:1325
    @staticmethod #line:1326
    def handle_Yanzhengma ():#line:1327
        TopFrame .OnYanzhengma ()#line:1328
    @classmethod #line:1335
    def OnClick_Tijiao (O0O000O0OOO000O00 ):#line:1336
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1337
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1338
        sdfsf24324297_need =True #line:1339
        if oOO0O0O0O0O0O0_num ==1 :#line:1341
            O00O000000OO000O0 =threading .Timer (one_delay ,O0O000O0OOO000O00 .Tijiao )#line:1342
            O00O000000OO000O0 .start ()#line:1343
            oOO0O0O0O0O0O0_on =False #line:1344
            if twice :#line:1345
                print ("修改为2")#line:1346
                oOO0O0O0O0O0O0_num =2 #line:1347
            print ("成功提交")#line:1349
        elif oOO0O0O0O0O0O0_num ==2 :#line:1350
            oOO0O0O0O0O0O0_num =0 #line:1351
            O00O000000OO000O0 =threading .Timer (ooo0O0o0oO0O_delay ,O0O000O0OOO000O00 .Tijiao )#line:1352
            O00O000000OO000O0 .start ()#line:1353
            oOO0O0O0O0O0O0_on =False #line:1354
        else :#line:1356
            O0O000O0OOO000O00 .Tijiao ()#line:1357
    @staticmethod #line:1359
    def Tijiao ():#line:1360
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1361
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1362
        oOO0O0O0O0O0O0_OK =False #line:1363
        global sdfsf24324297_one #line:1364
        if not sdfsf24324297_one :#line:1365
            O00000O0OOOO000OO =sdfsf24324297Thread ()#line:1366
            sdfsf24324297_one =False #line:1367
    @staticmethod #line:1374
    def OnClick_Shuaxin ():#line:1375
        global web_on #line:1376
        Click (Oo0o0Oo0o0o0 [3 ][0 ],Oo0o0Oo0o0o0 [3 ][1 ])#line:1377
        Click (Oo0o0Oo0o0o0 [5 ][0 ],Oo0o0Oo0o0o0 [5 ][1 ])#line:1378
    @staticmethod #line:1380
    def OnClick_sdfsf24324297 ():#line:1381
        print (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1382
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1383
    @staticmethod #line:1385
    def OnClick_oo0o0O0O0O0 ():#line:1386
        global web_on ,O0O0O0O0O0O0O_zxco0o0o0o0 #line:1387
        global oOO0O0O0O0O0O0_num ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:1388
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on #line:1389
        global uioo0o000oo_need ,uioo0o000oo_one ,oo0o0O0O0O0_interval #line:1390
        print (oo0o0O0O0O0_interval )#line:1391
        if not oo0o0O0O0O0_interval :#line:1392
            print (oOO0O0O0O0O0O0_num ,twice )#line:1393
            oo0o0O0O0O0_interval =True #line:1394
            oOO0O0O0O0O0O0_on =True #line:1395
            uioo0o000oo_need =True #line:1396
            if oOO0O0O0O0O0O0_num ==1 :#line:1397
                own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:1398
                setText (str (own_zxco0o0o0o01 ))#line:1399
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1400
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1401
                Paste ()#line:1402
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1403
                oOO0O0O0O0O0O0_on =True #line:1404
                oo0o0O0O0O0_on =False #line:1405
                oo0o0O0O0O0_interval =False #line:1406
                print (oo0o0O0O0O0_interval )#line:1407
                if not uioo0o000oo_one :#line:1409
                    OOO0000O0OO0000O0 =uioo0o000ooThread ()#line:1410
                    uioo0o000oo_one =True #line:1411
            elif oOO0O0O0O0O0O0_num ==2 and twice :#line:1412
                print ("第二次")#line:1413
                own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:1414
                setText (str (own_zxco0o0o0o02 ))#line:1415
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1416
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1417
                Paste ()#line:1418
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1419
                oOO0O0O0O0O0O0_on =True #line:1420
                oo0o0O0O0O0_on =False #line:1421
                oo0o0O0O0O0_interval =False #line:1422
                if not uioo0o000oo_one :#line:1423
                    OOO0000O0OO0000O0 =uioo0o000ooThread ()#line:1424
                    uioo0o000oo_one =True #line:1425
    @staticmethod #line:1427
    def selfChujia ():#line:1428
        global zxco0o0o0o0_view ,zxco0o0o0o0_count #line:1429
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1430
        Click (Oo0o0Oo0o0o0 [0 ][0 ],Oo0o0Oo0o0o0 [0 ][1 ])#line:1431
        Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1432
        zxco0o0o0o0_view =True #line:1433
        zxco0o0o0o0_count =0 #line:1434
    @staticmethod #line:1435
    def selfTijiao ():#line:1436
        OperationFrame .Del_shot ()#line:1437
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1438
    @staticmethod #line:1498
    def OnClick_Backspace ():#line:1499
        pg .press ('backspace')#line:1500
    def MainControl (OO0OO00O0O00O00OO ,O0O0000O00O000OOO ):#line:1504
        if not web_on and time_on :#line:1506
            OO0OO00O0O00O00OO .operationframe .Closetime ()#line:1507
        if web_on :#line:1508
            try :#line:1509
                OO0OO00O0O00O00OO .operationframe .Show (True )#line:1510
            except :#line:1511
                pass #line:1512
        else :#line:1513
            try :#line:1514
                OO0OO00O0O00O00OO .operationframe .Show (False )#line:1515
            except :#line:1516
                pass #line:1517
        if web_on :#line:1520
            OO0OO00O0O00O00OO .Show (False )#line:1521
        else :#line:1522
            OO0OO00O0O00O00OO .Show (True )#line:1523
    @staticmethod #line:1527
    def oOO0O0O0O0O0O0_ok ():#line:1528
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need ,oOO0O0O0O0O0O0_on #line:1529
        if e_on and oOO0O0O0O0O0O0_on :#line:1530
            oOO0O0O0O0O0O0_OK =True #line:1531
            uioo0o000oo_need =False #line:1532
    @staticmethod #line:1534
    def oOO0O0O0O0O0O0_ok2 ():#line:1535
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need #line:1536
        if enter_on and oOO0O0O0O0O0O0_on :#line:1537
            oOO0O0O0O0O0O0_OK =True #line:1538
            uioo0o000oo_need =False #line:1539
    @classmethod #line:1541
    def query (O0OOOO000OOOOOOOO ):#line:1542
        global query_interval ,query_on #line:1543
        if not query_interval and not query_on :#line:1544
            print ("执行")#line:1545
            query_on =True #line:1546
            query_interval =True #line:1547
            setText (str (1000000 ))#line:1548
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1549
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1550
            Paste ()#line:1551
            Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1552
            O0OO0OO0O0000O0OO =threading .Timer (3 ,O0OOOO000OOOOOOOO .query_sleep3 )#line:1553
            O0OO0OO0O0000O0OO .start ()#line:1554
            O0O000000000O0OO0 =threading .Timer (5 ,O0OOOO000OOOOOOOO .query_sleep5 )#line:1555
            O0O000000000O0OO0 .start ()#line:1556
        elif query_interval and query_on :#line:1557
            print (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1558
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1559
            query_on =False #line:1560
    @staticmethod #line:1563
    def query_sleep3 ():#line:1564
        print ("触发3+")#line:1565
        global query_interval ,query_on #line:1566
        if query_on :#line:1567
            print (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1568
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1569
            query_on =False #line:1570
    @staticmethod #line:1572
    def query_sleep5 ():#line:1573
        print ("触发5")#line:1574
        global query_interval #line:1575
        query_interval =False #line:1576
    @staticmethod #line:1592
    def Open ():#line:1593
        global do ,web_on #line:1594
        if not do :#line:1595
            do =True #line:1596
            OOO00OO0O0OOOOOO0 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1602
            OO00OOOOOOOO0OOO0 =ctypes .windll .user32 #line:1603
            OOOOOOOOOOOOOOO00 ={1 :(OOO00OO0O0OOOOOO0 ['2'],win32con .MOD_ALT ),2 :(OOO00OO0O0OOOOOO0 ['3'],win32con .MOD_ALT ),3 :(OOO00OO0O0OOOOOO0 ['4'],win32con .MOD_ALT ),4 :(OOO00OO0O0OOOOOO0 ['5'],win32con .MOD_ALT ),5 :(OOO00OO0O0OOOOOO0 ['6'],win32con .MOD_ALT ),6 :(OOO00OO0O0OOOOOO0 ['7'],win32con .MOD_ALT ),}#line:1607
            O00O000OO00OO00OO ={7 :(OOO00OO0O0OOOOOO0 ['s'],0x4000 ),8 :(OOO00OO0O0OOOOOO0 ['f'],0x4000 ),9 :(OOO00OO0O0OOOOOO0 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OOO00OO0O0OOOOOO0 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OOO00OO0O0OOOOOO0 ['q'],0x4000 )}#line:1610
            for OO0OO0O00O0OOO0O0 ,(OOOOO00O00O0O0O00 ,OO000O0OO0O000O0O )in OOOOOOOOOOOOOOO00 .items ():#line:1612
                if not OO00OOOOOOOO0OOO0 .RegisterHotKey (None ,OO0OO0O00O0OOO0O0 ,OO000O0OO0O000O0O ,OOOOO00O00O0O0O00 ):#line:1613
                    print ("Unable to register id",OO0OO0O00O0OOO0O0 )#line:1614
                    logging .info ("Unable to register id",OO0OO0O00O0OOO0O0 )#line:1615
                    do =False #line:1616
            for OO0OO0O00O0OOO0O0 ,(OOOOO00O00O0O0O00 ,OO000O0OO0O000O0O )in O00O000OO00OO00OO .items ():#line:1617
                if not OO00OOOOOOOO0OOO0 .RegisterHotKey (None ,OO0OO0O00O0OOO0O0 ,OO000O0OO0O000O0O ,OOOOO00O00O0O0O00 ):#line:1618
                    print ("Unable to register id",OO0OO0O00O0OOO0O0 )#line:1619
                    logging .info ("Unable to register id",OO0OO0O00O0OOO0O0 )#line:1620
                    do =False #line:1621
                web_on =True #line:1622
    @staticmethod #line:1625
    def Listen ():#line:1626
        try :#line:1627
            OOO00OOO0O0O00O00 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1632
            O000OO0O0O0OOO0O0 ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .selfTijiao ,9 :TopFrame .selfChujia ,10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .query }#line:1638
            O00OOOOO0OOOOOO0O =ctypes .windll .user32 #line:1639
            OO00O0O0000OOO0OO =wintypes .MSG ()#line:1640
            O0O00000000O0O0O0 =ctypes .byref #line:1641
            while O00OOOOO0OOOOOO0O .GetMessageA (O0O00000000O0O0O0 (OO00O0O0000OOO0OO ),None ,0 ,0 )!=0 :#line:1642
                if OO00O0O0000OOO0OO .message ==win32con .WM_HOTKEY :#line:1643
                    O00O00OOO0OOO00OO =O000OO0O0O0OOO0O0 .get (OO00O0O0000OOO0OO .wParam )#line:1644
                    if O00O00OOO0OOO00OO :#line:1645
                        O00O00OOO0OOO00OO ()#line:1646
                O00OOOOO0OOOOOO0O .TranslateMessage (O0O00000000O0O0O0 (OO00O0O0000OOO0OO ))#line:1647
                O00OOOOO0OOOOOO0O .DispatchMessageA (O0O00000000O0O0O0 (OO00O0O0000OOO0OO ))#line:1648
        finally :#line:1649
            pass #line:1650
    @staticmethod #line:1657
    def Close ():#line:1658
        global do #line:1659
        if do :#line:1660
            do =False #line:1661
            O000OO00O0OOOO0O0 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1665
            O00OO0000OOOOOO00 ={1 :(O000OO00O0OOOO0O0 ['2'],win32con .MOD_ALT ),2 :(O000OO00O0OOOO0O0 ['3'],win32con .MOD_ALT ),3 :(O000OO00O0OOOO0O0 ['4'],win32con .MOD_ALT ),4 :(O000OO00O0OOOO0O0 ['5'],win32con .MOD_ALT ),5 :(O000OO00O0OOOO0O0 ['6'],win32con .MOD_ALT ),6 :(O000OO00O0OOOO0O0 ['7'],win32con .MOD_ALT ),}#line:1669
            O0O000OOOO000OO0O =ctypes .windll .user32 #line:1670
            O000O0O00O00000OO ={7 :(O000OO00O0OOOO0O0 ['s'],0x4000 ),8 :(O000OO00O0OOOO0O0 ['f'],0x4000 ),9 :(O000OO00O0OOOO0O0 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O000OO00O0OOOO0O0 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O000OO00O0OOOO0O0 ['q'],0x4000 )}#line:1673
            for O0O000OOO0O0OO00O in O00OO0000OOOOOO00 .keys ():#line:1674
                O0O000OOOO000OO0O .UnregisterHotKey (None ,O0O000OOO0O0OO00O )#line:1675
            for O0O000OOO0O0OO00O in O000O0O00O00000OO .keys ():#line:1676
                O0O000OOOO000OO0O .UnregisterHotKey (None ,O0O000OOO0O0OO00O )#line:1677
            logging .info ("close assistant success")#line:1678
        else :#line:1679
            pass #line:1680
    def Save_log (O0O00O0OO0OO00O00 ):#line:1682
        OOO00O000OOO0OO0O =open ('pos.log','wb')#line:1683
        pickle .dump (Oo0o0Oo0o0o0 ,OOO00O000OOO0OO0O )#line:1684
        OOO00O000OOO0OO0O .close ()#line:1685
    def Confirmlogin (OO00OOOOO000OO00O ,OO0O0OOOO00000000 ):#line:1765
        Keeplogin ()#line:1766
    def Choose_time1 (OOOOOOO00OO0OOOOO ,O0OOOOO000OOOO0O0 ):#line:1771
        OOOOOOO00OO0OOOOO .timelabel .SetLabel ("已设定截止时间"+OOOOOOO00OO0OOOOO .time_choice1 .GetString (OOOOOOO00OO0OOOOO .time_choice1 .GetSelection ())+'.'+str (OOOOOOO00OO0OOOOO .time_choice2 .GetSelection ())+" 秒")#line:1774
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1775
        ghjo0o0o0o01 =OOOOOOO00OO0OOOOO .time_choice1 .GetString (OOOOOOO00OO0OOOOO .time_choice1 .GetSelection ())#line:1776
        ghjo0o0o0o02 =OOOOOOO00OO0OOOOO .time_choice2 .GetString (OOOOOOO00OO0OOOOO .time_choice2 .GetSelection ())#line:1777
    def Choose_time2 (O0OO0OO0O00OO000O ,O0OO0OO00O0O00O0O ):#line:1780
        O0OO0OO0O00OO000O .timelabel .SetLabel ("已设定截止时间"+O0OO0OO0O00OO000O .time_choice1 .GetString (O0OO0OO0O00OO000O .time_choice1 .GetSelection ())+'.'+str (O0OO0OO0O00OO000O .time_choice2 .GetSelection ())+" 秒")#line:1783
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1784
        ghjo0o0o0o01 =O0OO0OO0O00OO000O .time_choice1 .GetString (O0OO0OO0O00OO000O .time_choice1 .GetSelection ())#line:1785
        ghjo0o0o0o02 =O0OO0OO0O00OO000O .time_choice2 .GetString (O0OO0OO0O00OO000O .time_choice2 .GetSelection ())#line:1786
class ClockWindow (wx .Panel ):#line:1839
    def __init__ (O00OO0OOOO0000000 ,OO000OO0O0O00OO00 ):#line:1840
        wx .Window .__init__ (O00OO0OOOO0000000 ,OO000OO0O0O00OO00 ,size =Timesize )#line:1841
        O00OO0OOOO0000000 .Bind (wx .EVT_PAINT ,O00OO0OOOO0000000 .OnPaint )#line:1842
        O00OO0OOOO0000000 .timer =wx .Timer (O00OO0OOOO0000000 )#line:1843
        O00OO0OOOO0000000 .Bind (wx .EVT_TIMER ,O00OO0OOOO0000000 .OnTimer ,O00OO0OOOO0000000 .timer )#line:1844
        O00OO0OOOO0000000 .timer .Start (100 )#line:1845
    def Draw (O00OO00OO00OO0O0O ,OOOO00000000O0OO0 ):#line:1847
        global a_time #line:1848
        OO0OO0O000000O000 =time .localtime (a_time )#line:1849
        OO00OOO0O0O000O00 =time .strftime ("%H:%M:%S",OO0OO0O000000O000 )#line:1850
        O00O0OOO000000O0O ,OOOOO00O0O0O00O0O =O00OO00OO00OO0O0O .GetClientSize ()#line:1851
        OOOO00000000O0OO0 .SetBackground (wx .Brush (O00OO00OO00OO0O0O .GetBackgroundColour ()))#line:1852
        OOOO00000000O0OO0 .Clear ()#line:1853
        OOOO00000000O0OO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1854
        OOOOOO00O0O0OOO0O ,OOOOO0OO0O00OO0O0 =OOOO00000000O0OO0 .GetTextExtent (OO00OOO0O0O000O00 )#line:1855
        OOOO00000000O0OO0 .DrawText (OO00OOO0O0O000O00 ,(O00O0OOO000000O0O -OOOOOO00O0O0OOO0O )/2 ,(OOOOO00O0O0O00O0O )/2 -OOOOO0OO0O00OO0O0 /2 )#line:1856
    def Modify (O00O0O00O000O00OO ,OOO0O00OOOO00OO00 ):#line:1858
        global a_time ,b_time #line:1859
        if b_time <9 :#line:1861
            b_time =b_time +1 #line:1862
        else :#line:1863
            b_time =0 #line:1864
        O00O000OOOOOO0000 =time .localtime (a_time )#line:1865
        O000O0O0OO00O000O =time .strftime ("%H:%M:%S",O00O000OOOOOO0000 )#line:1866
        OOOO0O0O000OOOOO0 ,OO000O000O00000O0 =O00O0O00O000O00OO .GetClientSize ()#line:1868
        OOO0O00OOOO00OO00 .SetBackground (wx .Brush (O00O0O00O000O00OO .GetBackgroundColour ()))#line:1869
        OOO0O00OOOO00OO00 .Clear ()#line:1870
        OOO0O00OOOO00OO00 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1871
        O000OO00OO0O0OOO0 ,O0OO0O00OOO0O0000 =OOO0O00OOOO00OO00 .GetTextExtent (O000O0O0OO00O000O )#line:1872
        OOO0O00OOOO00OO00 .DrawText (O000O0O0OO00O000O ,(OOOO0O0O000OOOOO0 -O000OO00OO0O0OOO0 )/2 ,(OO000O000O00000O0 )/2 -O0OO0O00OOO0O0000 /2 )#line:1873
    def OnTimer (O0OO0OO000OOO0OO0 ,O00O0OO0OO0OOOOO0 ):#line:1875
        O00000OO0O0O00OOO =wx .BufferedDC (wx .ClientDC (O0OO0OO000OOO0OO0 ))#line:1876
        O0OO0OO000OOO0OO0 .Modify (O00000OO0O0O00OOO )#line:1877
    def OnPaint (OO000OOOO00O0O000 ,OOO0O0OO000000000 ):#line:1879
        OOOO0O0O000O000O0 =wx .BufferedPaintDC (OO000OOOO00O0O000 )#line:1880
        OO000OOOO00O0O000 .Draw (OOOO0O0O000O000O0 )#line:1881
class TimeFrame (wx .Frame ):#line:1885
    def __init__ (O0OO00OOO00O00OO0 ):#line:1886
        wx .Frame .__init__ (O0OO00OOO00O00OO0 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1888
        ClockWindow (O0OO00OOO00O00OO0 )#line:1891
class MoniClockWindow (wx .Panel ):#line:1896
    def __init__ (OO000O0OO00O0OOO0 ,OOO00O00OO00O0O0O ):#line:1897
        wx .Window .__init__ (OO000O0OO00O0OOO0 ,OOO00O00OO00O0O0O ,size =Timesize )#line:1898
        OO000O0OO00O0OOO0 .Bind (wx .EVT_PAINT ,OO000O0OO00O0OOO0 .OnPaint )#line:1899
        OO000O0OO00O0OOO0 .timer =wx .Timer (OO000O0OO00O0OOO0 )#line:1900
        OO000O0OO00O0OOO0 .Bind (wx .EVT_TIMER ,OO000O0OO00O0OOO0 .OnTimer ,OO000O0OO00O0OOO0 .timer )#line:1901
        OO000O0OO00O0OOO0 .timer .Start (100 )#line:1902
    def Draw (OO000O0O0000OO0OO ,OO0OO0OOO0OOOO000 ):#line:1904
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1905
        OOO0O00O0OOOO000O ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1906
        O00O0OO0O0O000OOO ,O0O00O0OO000OOOO0 =OO000O0O0000OO0OO .GetClientSize ()#line:1907
        OO0OO0OOO0OOOO000 .SetBackground (wx .Brush (OO000O0O0000OO0OO .GetBackgroundColour ()))#line:1908
        OO0OO0OOO0OOOO000 .Clear ()#line:1909
        OO0OO0OOO0OOOO000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1910
        OOOOOOOOOO000O0OO ,O00O0O00000O0O0O0 =OO0OO0OOO0OOOO000 .GetTextExtent (OOO0O00O0OOOO000O )#line:1911
        OO0OO0OOO0OOOO000 .DrawText (OOO0O00O0OOOO000O ,(O00O0OO0O0O000OOO -OOOOOOOOOO000O0OO )/2 ,(O0O00O0OO000OOOO0 )/2 -O00O0O00000O0O0O0 /2 )#line:1912
    def Modify (OOO0OOOOO00000O00 ,O00O0OOOO00000000 ):#line:1914
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1915
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:1916
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:1917
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:1918
        OOOO0OO00OO000O00 =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1919
        O000O000OO00O0000 ="%s:%s:%s"%(11 ,29 ,OOOO0OO00OO000O00 )#line:1920
        OO0000O0OOOOO0O00 ,O0OO00O00O0O0OO0O =OOO0OOOOO00000O00 .GetClientSize ()#line:1921
        O00O0OOOO00000000 .SetBackground (wx .Brush (OOO0OOOOO00000O00 .GetBackgroundColour ()))#line:1922
        O00O0OOOO00000000 .Clear ()#line:1923
        O00O0OOOO00000000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1924
        OOOOOOO0OO0O0O0OO ,O0000OOO00OOO000O =O00O0OOOO00000000 .GetTextExtent (O000O000OO00O0000 )#line:1925
        O00O0OOOO00000000 .DrawText (O000O000OO00O0000 ,(OO0000O0OOOOO0O00 -OOOOOOO0OO0O0O0OO )/2 ,(O0OO00O00O0O0OO0O )/2 -O0000OOO00OOO000O /2 )#line:1926
    def OnTimer (OO00O00O0OOOOOO00 ,O0O00O0OOO0O00OOO ):#line:1928
        O0O00OOOOOO0000OO =wx .BufferedDC (wx .ClientDC (OO00O00O0OOOOOO00 ))#line:1929
        OO00O00O0OOOOOO00 .Modify (O0O00OOOOOO0000OO )#line:1930
    def OnPaint (OO000OO0OO00O0000 ,OO00O0OO0O0O0O0OO ):#line:1932
        O000O00O000O0O00O =wx .BufferedPaintDC (OO000OO0OO00O0000 )#line:1933
        OO000OO0OO00O0000 .Draw (O000O00O000O0O00O )#line:1934
class MoniTimeFrame (wx .Frame ):#line:1938
    def __init__ (OO00O000OO0O0O000 ):#line:1939
        wx .Frame .__init__ (OO00O000OO0O0O000 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1941
        MoniClockWindow (OO00O000OO0O0O000 )#line:1944
class PosFrame (wx .Frame ):#line:1949
    def __init__ (O00000OOO0000OO00 ,OOOO000OO0000OOOO ,O0O000OOOO000O000 ):#line:1950
        OOOOOOO0O000O0OO0 ,O0000OO00O00OO0O0 =OOOO000OO0000OOOO #line:1951
        wx .Frame .__init__ (O00000OOO0000OO00 ,None ,-1 ,'POS',pos =(OOOOOOO0O000O0OO0 -20 ,O0000OO00O00OO0O0 -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:1953
        O0000O0O000O00000 =wx .Panel (O00000OOO0000OO00 ,-1 ,size =(30 ,20 ))#line:1954
        OO000OOO0000O0O00 =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:1956
        OO0000OOO0O0000O0 =[]#line:1957
        OO0000OOO0O0000O0 .append (wx .StaticText (O0000O0O000O00000 ,-1 ,O0O000OOOO000O000 ,(0 ,0 )))#line:1959
        for O0OO0OO000OOOOO0O in range (len (OO0000OOO0O0000O0 )):#line:1960
            OO0000OOO0O0000O0 [O0OO0OO000OOOOO0O ].SetFont (OO000OOO0000O0O00 )#line:1961
class PriceFrame (wx .Frame ):#line:1963
    def __init__ (O00O0000OOO0O00O0 ,OO0O00000OOO0O000 ):#line:1964
        wx .Frame .__init__ (O00O0000OOO0O00O0 ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1967
        O00O0000OOO0O00O0 .panel =wx .Panel (O00O0000OOO0O00O0 ,size =Pricesize )#line:1968
        wx .StaticBitmap (O00O0000OOO0O00O0 .panel ,-1 ,wx .BitmapFromImage (OO0O00000OOO0O000 ))#line:1970
class YanzhengmaFrame (wx .Frame ):#line:1972
    def __init__ (OOOOO00OO00O0O00O ,OOOOO000OO0O00000 ):#line:1973
        wx .Frame .__init__ (OOOOO00OO00O0O00O ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1976
        OOOOO00OO00O0O00O .panel =wx .Panel (OOOOO00OO00O0O00O ,size =(400 ,80 ))#line:1977
        wx .StaticBitmap (OOOOO00OO00O0O00O .panel ,-1 ,wx .BitmapFromImage (OOOOO000OO0O00000 ))#line:1979
class AdFrame (wx .Frame ):#line:1983
    def __init__ (OOOO00OO0O00OO000 ):#line:1984
        wx .Frame .__init__ (OOOO00OO0O00OO000 ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1986
        O0OOOO0O0O0OO0OOO =wx .Panel (OOOO00OO0O00OO000 ,-1 ,size =(250 ,200 ))#line:1987
        O0OOO00O0O0000OO0 =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:1989
        O0O0OO0O00OOOOO0O =[]#line:1990
        O0O0OO0O00OOOOO0O .append (wx .StaticText (O0OOOO0O0O0OO0OOO ,-1 ," 专业代拍软件",(15 ,10 )))#line:1992
        O0O0OO0O00OOOOO0O .append (wx .StaticText (O0OOOO0O0O0OO0OOO ,-1 ," 专业代拍团队",(15 ,60 )))#line:1994
        O0O0OO0O00OOOOO0O .append (wx .StaticText (O0OOOO0O0O0OO0OOO ,-1 ,"关注微信公众号",(15 ,110 )))#line:1996
        O0O0OO0O00OOOOO0O .append (wx .StaticText (O0OOOO0O0O0OO0OOO ,-1 ," 小鲜肉拍牌",(15 ,160 )))#line:1998
        for OOO0000O0OOOOO000 in range (len (O0O0OO0O00OOOOO0O )):#line:1999
            O0O0OO0O00OOOOO0O [OOO0000O0OOOOO000 ].SetFont (O0OOO00O0O0000OO0 )#line:2000
class WebFrame (wx .Frame ):#line:2002
    def __init__ (OOOOO00OO00OOOO00 ,OO00OO0OOO000OOOO ,OOOOOOO00O0OO00OO ,O000O0O0000OOOO0O ,OOO0OO0OO00OOOOOO ):#line:2003
        wx .Frame .__init__ (OOOOO00OO00OOOO00 ,None ,-1 ,OOO0OO0OO00OOOOOO ,size =(websize [0 ],websize [1 ]),pos =(OO00OO0OOO000OOOO ,OOOOOOO00O0OO00OO ),style =wx .SIMPLE_BORDER )#line:2004
        if O000O0O0000OOOO0O :#line:2009
            OOOOO00OO00OOOO00 .adframe =AdFrame ()#line:2010
            OOOOO00OO00OOOO00 .adframe .Show (True )#line:2011
        OOOOO00OO00OOOO00 .Bind (wx .EVT_CLOSE ,OOOOO00OO00OOOO00 .OnClose )#line:2012
        OOOOO00OO00OOOO00 .ad2 =O000O0O0000OOOO0O #line:2013
        OOOOO00OO00OOOO00 .control =ControlFrame (OOO0OO0OO00OOOOOO )#line:2014
        OOOOO00OO00OOOO00 .control .Show (True )#line:2015
        pub .subscribe (OOOOO00OO00OOOO00 .OnClose2 ,"close web")#line:2040
    def OnClose (OO0O00O0OO00O0000 ,O0OOO00O00O000O0O ):#line:2041
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2042
        web_on =False #line:2043
        view_time =False #line:2044
        o0sdofsfo0sodf0so0_on =False #line:2045
        ooweo0o0werwr_on =False #line:2046
        TopFrame .Close ()#line:2047
        O00O0O00000OOO0OO ="sc_new.png"#line:2048
        if os .path .exists (O00O0O00000OOO0OO ):#line:2049
            os .remove (O00O0O00000OOO0OO )#line:2050
        OO0O00O0OO00O0000 .Destroy ()#line:2051
        if OO0O00O0OO00O0000 .ad2 :#line:2052
            OO0O00O0OO00O0000 .adframe .Destroy ()#line:2053
        O0OOO00O00O000O0O .Skip ()#line:2054
    def OnClose2 (OO0O0O0O00000O000 ):#line:2056
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2057
        web_on =False #line:2058
        view_time =False #line:2059
        o0sdofsfo0sodf0so0_on =False #line:2060
        ooweo0o0werwr_on =False #line:2061
        TopFrame .Close ()#line:2062
        OOOOO00OOO0OOOO00 ="sc_new.png"#line:2063
        if os .path .exists (OOOOO00OOO0OOOO00 ):#line:2064
            os .remove (OOOOO00OOO0OOOO00 )#line:2065
        OO0O0O0O00000O000 .Destroy ()#line:2066
        if OO0O0O0O00000O000 .ad2 :#line:2067
            OO0O0O0O00000O000 .adframe .Destroy ()#line:2068
class ControlFrame (wx .Frame ):#line:2071
    def __init__ (OO0000000000OO0O0 ,OOOOOO0000O000OO0 ):#line:2072
        wx .Frame .__init__ (OO0000000000OO0O0 ,None ,-1 ,size =(50 ,35 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +websize [0 ]-50 ,0 ))#line:2074
        OO0000000000OO0O0 .panel =wx .Panel (OO0000000000OO0O0 ,-1 ,size =(50 ,35 ))#line:2075
        OO0000000000OO0O0 .button1 =wx .Button (OO0000000000OO0O0 .panel ,pos =(0 ,0 ),size =(50 ,25 ),label ="关闭")#line:2076
        OO0000000000OO0O0 .Bind (wx .EVT_BUTTON ,OO0000000000OO0O0 .o_closeweb ,OO0000000000OO0O0 .button1 )#line:2077
    def o_closeweb (O0OOO0O000O0O0000 ,O0O00O0OOO0000O0O ):#line:2078
        wx .CallAfter (pub .sendMessage ,"close web")#line:2079
        O0OOO0O000O0O0000 .Destroy ()#line:2080
        O0O00O0OOO0000O0O .Skip ()#line:2081
class OperationFrame (wx .Frame ):#line:2084
    def __init__ (O0O00OO0O0000OO0O ):#line:2085
        wx .Frame .__init__ (O0O00OO0O0000OO0O ,None ,-1 ,title ="小鲜肉代拍",pos =(1070 ,100 ),size =(300 ,425 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION )#line:2087
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2089
        one_oO0O0O0O0O0O0O0O01 =O0O00OO0O0000OO0O .gettime (OO00000o01 )#line:2090
        one_oO0O0O0O0O0O0O0O02 =O0O00OO0O0000OO0O .gettime (OO00000o02 )#line:2091
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0O00OO0O0000OO0O .gettime (ooo0O0o0oO0O_time1 )#line:2092
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0O00OO0O0000OO0O .gettime (ooo0O0o0oO0O_time2 )#line:2093
        O0O00OO0O0000OO0O .timer1 =wx .Timer (O0O00OO0O0000OO0O )#line:2095
        O0O00OO0O0000OO0O .Bind (wx .EVT_TIMER ,O0O00OO0O0000OO0O .Price_view ,O0O00OO0O0000OO0O .timer1 )#line:2096
        O0O00OO0O0000OO0O .timer1 .Start (500 )#line:2097
        O0O00OO0O0000OO0O .timer2 =wx .Timer (O0O00OO0O0000OO0O )#line:2099
        O0O00OO0O0000OO0O .Bind (wx .EVT_TIMER ,O0O00OO0O0000OO0O .Price_count ,O0O00OO0O0000OO0O .timer2 )#line:2100
        O0O00OO0O0000OO0O .timer2 .Start (100 )#line:2101
        O0O00OO0O0000OO0O .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:2103
        O0O00OO0O0000OO0O .O0O0O0O0O0O0Oframe .Show (False )#line:2104
        OOOOOO0O0OOOO0000 =wx .Panel (O0O00OO0O0000OO0O ,-1 ,size =(300 ,380 ))#line:2108
        OOO000OO000000O0O =wx .StaticBox (OOOOOO0O0OOOO0000 ,-1 ,u'选择策略:')#line:2110
        O0O00OO0O0000OO0O .stractagySizer =wx .StaticBoxSizer (OOO000OO000000O0O ,wx .VERTICAL )#line:2111
        OO0OOO0OO0O00O0O0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2112
        OO0000O00OO00O00O =wx .BoxSizer (wx .HORIZONTAL )#line:2113
        OO0000O00OO00O00O .Add (OO0OOO0OO0O00O0O0 )#line:2114
        O0OOOOOO0O00O0O0O =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2118
        O0O00OO0O0000OO0O .select_stractagy =wx .Choice (OOOOOO0O0OOOO0000 ,-1 ,choices =O0OOOOOO0O00O0O0O ,size =(100 ,50 ))#line:2119
        OO0000O00OO00O00O .Add (O0O00OO0O0000OO0O .select_stractagy )#line:2120
        O0O00OO0O0000OO0O .select_stractagy .SetSelection (0 )#line:2121
        O0O00OO0O0000OO0O .timeview =wx .CheckBox (OOOOOO0O0OOOO0000 ,-1 ,label =u'显示时间')#line:2123
        OOO00OO0O00000OOO =wx .BoxSizer (wx .HORIZONTAL )#line:2124
        OOO00OO0O00000OOO .Add (O0O00OO0O0000OO0O .timeview )#line:2125
        O0O00OO0O0000OO0O .button1 =wx .Button (OOOOOO0O0OOOO0000 ,label ='+1s',size =(35 ,25 ))#line:2128
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Add_ooo0O0o0oO0O ,O0O00OO0O0000OO0O .button1 )#line:2129
        O0O00OO0O0000OO0O .button2 =wx .Button (OOOOOO0O0OOOO0000 ,label ='-1s',size =(35 ,25 ))#line:2130
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Minus_ooo0O0o0oO0O ,O0O00OO0O0000OO0O .button2 )#line:2131
        O0O00OO0O0000OO0O .button3 =wx .Button (OOOOOO0O0OOOO0000 ,label ='+0.1s',size =(35 ,25 ))#line:2132
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Add_time ,O0O00OO0O0000OO0O .button3 )#line:2133
        O0O00OO0O0000OO0O .button4 =wx .Button (OOOOOO0O0OOOO0000 ,label ='-0.1s',size =(35 ,25 ))#line:2134
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Minus_time ,O0O00OO0O0000OO0O .button4 )#line:2135
        OOO00OO0O00000OOO .Add (O0O00OO0O0000OO0O .button1 )#line:2137
        OOO00OO0O00000OOO .Add (O0O00OO0O0000OO0O .button2 )#line:2138
        OOO00OO0O00000OOO .Add (O0O00OO0O0000OO0O .button3 )#line:2139
        OOO00OO0O00000OOO .Add (O0O00OO0O0000OO0O .button4 )#line:2140
        OOO000O0OO0000000 =wx .BoxSizer (wx .VERTICAL )#line:2142
        OOO000O0OO0000000 .Add (OO0000O00OO00O00O )#line:2143
        OOO000O0OO0000000 .Add (OOO00OO0O00000OOO )#line:2144
        OOOOOO00OOOOO00O0 =["E键","回车"]#line:2147
        O0O00OO0O0000OO0O .sdfsf24324297_choice =wx .Choice (OOOOOO0O0OOOO0000 ,-1 ,choices =OOOOOO00OOOOO00O0 )#line:2148
        O0O00OO0O0000OO0O .sdfsf24324297_choice .SetSelection (0 )#line:2149
        O0O00OO0O0000OO0O .sdfsf24324297_label =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"确认提交方式     ")#line:2150
        O00OOOO00OO00000O =wx .BoxSizer (wx .HORIZONTAL )#line:2151
        O00OOOO00OO00000O .Add (O0O00OO0O0000OO0O .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2152
        O00OOOO00OO00000O .Add (O0O00OO0O0000OO0O .sdfsf24324297_choice )#line:2153
        OOO000O0OO0000000 .Add (O00OOOO00OO00000O )#line:2154
        O0O00OO0O0000OO0O .ghjo0o0o0o0_save =wx .Button (OOOOOO0O0OOOO0000 ,label ="保存策略",size =(60 ,35 ))#line:2157
        O0O00OO0O0000OO0O .ghjo0o0o0o0_load =wx .Button (OOOOOO0O0OOOO0000 ,label ="载入策略",size =(60 ,35 ))#line:2158
        O0O00OO0O0000OO0O .save_info =wx .Button (OOOOOO0O0OOOO0000 ,label ="用户信息",size =(60 ,35 ))#line:2159
        OOO0O00O0O00O00OO =wx .BoxSizer (wx .HORIZONTAL )#line:2160
        OOO0O00O0O00O00OO .Add (O0O00OO0O0000OO0O .ghjo0o0o0o0_save )#line:2161
        OOO0O00O0O00O00OO .Add (O0O00OO0O0000OO0O .ghjo0o0o0o0_load )#line:2162
        OOO0O00O0O00O00OO .Add (O0O00OO0O0000OO0O .save_info )#line:2163
        OOO000O0OO0000000 .Add (OOO0O00O0O00O00OO )#line:2164
        O0000O0OOOOOO0000 =wx .StaticBox (OOOOOO0O0OOOO0000 ,-1 ,u'单枪策略:')#line:2168
        O0O00OO0O0000OO0O .oneshotSizer =wx .StaticBoxSizer (O0000O0OOOOOO0000 ,wx .VERTICAL )#line:2169
        O0OO0OOO00OO00000 =wx .GridBagSizer (4 ,4 )#line:2170
        O0O00OO0O0000OO0O .jiajia_time =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2171
        O0O00OO0O0000OO0O .jiajia_time .SetRange (40 ,55 )#line:2172
        O0O00OO0O0000OO0O .jiajia_time .SetValue (48 )#line:2173
        O0O00OO0O0000OO0O .jiajia_time .SetIncrement (0.1 )#line:2174
        O0OO0OOO00OO00000 .Add (O0O00OO0O0000OO0O .jiajia_time ,pos =(0 ,0 ))#line:2176
        OO00O0OOO0O00OO0O =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2177
        O0OO0OOO00OO00000 .Add (OO00O0OOO0O00OO0O ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2178
        OO0O0OO00O0000OOO =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2179
        O0OO0OOO00OO00000 .Add (OO0O0OO00O0000OOO ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2180
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2181
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2182
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2183
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2184
        O0OO0OOO00OO00000 .Add (O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2185
        OOOOOOOO0O00000O0 =[u"提前100",u"提前200",u"踩点"]#line:2188
        O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O0 =wx .Choice (OOOOOO0O0OOOO0000 ,-1 ,choices =OOOOOOOO0O00000O0 ,size =(68 ,25 ))#line:2189
        O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2190
        O0OO0OOO00OO00000 .Add (O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2191
        O0OO0OOOO00O00OO0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"出价提交延迟")#line:2192
        O0OO0OOO00OO00000 .Add (O0OO0OOOO00O00OO0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2193
        O0O00OO0O0000OO0O .yanchi_time =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2194
        O0O00OO0O0000OO0O .yanchi_time .SetRange (0.0 ,1.0 )#line:2195
        O0O00OO0O0000OO0O .yanchi_time .SetValue (0.5 )#line:2196
        O0O00OO0O0000OO0O .yanchi_time .SetIncrement (0.1 )#line:2197
        O0OO0OOO00OO00000 .Add (O0O00OO0O0000OO0O .yanchi_time ,pos =(1 ,3 ))#line:2198
        O0OOO00OO0O000OO0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2199
        O0OO0OOO00OO00000 .Add (O0OOO00OO0O000OO0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2200
        O000O000O0O0OO000 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"强制提交时间")#line:2203
        O0OO0OOO00OO00000 .Add (O000O000O0O0OO000 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2204
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2205
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2206
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2207
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2208
        O0OO0OOO00OO00000 .Add (O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2209
        O000OOO0OOO0OOOOO =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2210
        O0OO0OOO00OO00000 .Add (O000OOO0OOO0OOOOO ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2211
        O0O00OO0O0000OO0O .oneshotSizer .Add (O0OO0OOO00OO00000 ,0 ,flag =wx .ALL ,border =5 )#line:2213
        OOOOOOOOO00OO0O0O =wx .StaticBox (OOOOOO0O0OOOO0000 ,-1 ,u'双枪策略:')#line:2217
        O0O00OO0O0000OO0O .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (OOOOOOOOO00OO0O0O ,wx .VERTICAL )#line:2218
        O0OO0OO000OOO00O0 =wx .GridBagSizer (4 ,4 )#line:2219
        O0O00OO0O0000OO0O .jiajia_time2 =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2220
        O0O00OO0O0000OO0O .jiajia_time2 .SetRange (40 ,55 )#line:2221
        O0O00OO0O0000OO0O .jiajia_time2 .SetValue (48 )#line:2222
        O0O00OO0O0000OO0O .jiajia_time2 .SetIncrement (0.1 )#line:2223
        O0OO0OO000OOO00O0 .Add (O0O00OO0O0000OO0O .jiajia_time2 ,pos =(0 ,0 ))#line:2224
        OOO0O000000OOOO0O =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2225
        O0OO0OO000OOO00O0 .Add (OOO0O000000OOOO0O ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2226
        OOO00OOO0O0O00OO0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2227
        O0OO0OO000OOO00O0 .Add (OOO00OOO0O0O00OO0 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2228
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2229
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2230
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2231
        O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2232
        O0OO0OO000OOO00O0 .Add (O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2233
        OOO00O0OOO0O00000 =[u"提前100",u"提前200",u"踩点"]#line:2235
        O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O02 =wx .Choice (OOOOOO0O0OOOO0000 ,-1 ,choices =OOO00O0OOO0O00000 ,size =(68 ,25 ))#line:2236
        O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2237
        O0OO0OO000OOO00O0 .Add (O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2238
        O0O0OOOOO0OOOOOO0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"出价提交延迟")#line:2239
        O0OO0OO000OOO00O0 .Add (O0O0OOOOO0OOOOOO0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2240
        O0O00OO0O0000OO0O .yanchi_time2 =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2241
        O0O00OO0O0000OO0O .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2242
        O0O00OO0O0000OO0O .yanchi_time2 .SetValue (0.5 )#line:2243
        O0O00OO0O0000OO0O .yanchi_time2 .SetIncrement (0.1 )#line:2244
        O0OO0OO000OOO00O0 .Add (O0O00OO0O0000OO0O .yanchi_time2 ,pos =(1 ,3 ))#line:2245
        O0O0O0OOO000OO000 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2246
        O0OO0OO000OOO00O0 .Add (O0O0O0OOO000OO000 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2247
        OOOOOOO000O0OO0OO =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"强制提交时间")#line:2250
        O0OO0OO000OOO00O0 .Add (OOOOOOO000O0OO0OO ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2251
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (OOOOOO0O0OOOO0000 ,-1 ,"",size =(68 ,25 ))#line:2252
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2253
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2254
        O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2255
        O0OO0OO000OOO00O0 .Add (O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2256
        O000O0OOO0OO00OO0 =wx .StaticText (OOOOOO0O0OOOO0000 ,label =u"秒")#line:2257
        O0OO0OO000OOO00O0 .Add (O000O0OOO0OO00OO0 ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2258
        O0O00OO0O0000OO0O .ooo0O0o0oO0OshotSizer .Add (O0OO0OO000OOO00O0 ,0 ,flag =wx .ALL ,border =5 )#line:2260
        O0O00OO0O0000OO0O .stractagySizer .Add (OOO000O0OO0000000 ,0 ,wx .ALL |wx .CENTER ,5 )#line:2262
        O0O00OO0O0000OO0O .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2263
        OOO000O00O00OO00O =wx .StaticText (OOOOOO0O0OOOO0000 ,-1 ,label =u"拍牌功能设置")#line:2266
        OO0O0O0O000O0O000 =wx .StaticText (OOOOOO0O0OOOO0000 ,-1 ,label =u"10点半需要进行第一次出价")#line:2267
        OO0O0O0O000O0O000 .SetForegroundColour ('red')#line:2268
        O0000O0OO0OO00OO0 =wx .StaticLine (OOOOOO0O0OOOO0000 ,-1 )#line:2269
        O0O00OO0O0000OO0O .vbox1 .Add (OOO000O00O00OO00O ,0 ,wx .ALL |wx .LEFT ,10 )#line:2270
        O0O00OO0O0000OO0O .vbox1 .Add (OO0O0O0O000O0O000 ,0 ,wx .LEFT ,10 )#line:2271
        O0O00OO0O0000OO0O .vbox1 .Add (O0000O0OO0OO00OO0 ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2272
        O0O00OO0O0000OO0O .vbox1 .Add (O0O00OO0O0000OO0O .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2273
        O0O00OO0O0000OO0O .vbox1 .Add (O0O00OO0O0000OO0O .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2274
        O0O00OO0O0000OO0O .vbox1 .Add (O0O00OO0O0000OO0O .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2275
        OOOOOO0O0OOOO0000 .SetSizer (O0O00OO0O0000OO0O .vbox1 )#line:2276
        O0O00OO0O0000OO0O .ooo0O0o0oO0Osizer_Shown =False #line:2279
        O0O00OO0O0000OO0O .oneshotsizer_Shown =True #line:2280
        O0O00OO0O0000OO0O .vbox1 .Hide (O0O00OO0O0000OO0O .ooo0O0o0oO0OshotSizer )#line:2281
        O0O00OO0O0000OO0O .Bind (wx .EVT_CHECKBOX ,O0O00OO0O0000OO0O .Timeview ,O0O00OO0O0000OO0O .timeview )#line:2290
        O0O00OO0O0000OO0O .Bind (wx .EVT_CHOICE ,O0O00OO0O0000OO0O .Confirmchoice ,O0O00OO0O0000OO0O .sdfsf24324297_choice )#line:2291
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Strategy_save ,O0O00OO0O0000OO0O .ghjo0o0o0o0_save )#line:2292
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Strategy_load ,O0O00OO0O0000OO0O .ghjo0o0o0o0_load )#line:2293
        O0O00OO0O0000OO0O .Bind (wx .EVT_BUTTON ,O0O00OO0O0000OO0O .Save_info ,O0O00OO0O0000OO0O .save_info )#line:2294
        O0O00OO0O0000OO0O .Bind (wx .EVT_CHOICE ,O0O00OO0O0000OO0O .Refresh_panel ,O0O00OO0O0000OO0O .select_stractagy )#line:2296
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Jiajia_time ,O0O00OO0O0000OO0O .jiajia_time )#line:2298
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Jiajia_zxco0o0o0o0 ,O0O00OO0O0000OO0O .jiajia_zxco0o0o0o0 )#line:2300
        O0O00OO0O0000OO0O .Bind (wx .EVT_CHOICE ,O0O00OO0O0000OO0O .Select_oOO0O0O0O0O0O0 ,O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O0 )#line:2301
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Yanchi_time ,O0O00OO0O0000OO0O .yanchi_time )#line:2303
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Tijiao_time ,O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time )#line:2305
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Jiajia_time2 ,O0O00OO0O0000OO0O .jiajia_time2 )#line:2308
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Jiajia_zxco0o0o0o02 ,O0O00OO0O0000OO0O .jiajia_zxco0o0o0o02 )#line:2310
        O0O00OO0O0000OO0O .Bind (wx .EVT_CHOICE ,O0O00OO0O0000OO0O .Select_oOO0O0O0O0O0O02 ,O0O00OO0O0000OO0O .select_oOO0O0O0O0O0O02 )#line:2311
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Yanchi_time2 ,O0O00OO0O0000OO0O .yanchi_time2 )#line:2313
        O0O00OO0O0000OO0O .Bind (wx .EVT_TEXT ,O0O00OO0O0000OO0O .Tijiao_time2 ,O0O00OO0O0000OO0O .oOO0O0O0O0O0O0_time2 )#line:2315
        O0O00OO0O0000OO0O .timeframe1 =TimeFrame ()#line:2317
        O0O00OO0O0000OO0O .timeframe1 .Show (False )#line:2318
        O0O00OO0O0000OO0O .timeframe2 =MoniTimeFrame ()#line:2320
        O0O00OO0O0000OO0O .timeframe2 .Show (False )#line:2321
        O0O00OO0O0000OO0O .operationtimer =wx .Timer (O0O00OO0O0000OO0O )#line:2324
        O0O00OO0O0000OO0O .Bind (wx .EVT_TIMER ,O0O00OO0O0000OO0O .opt ,O0O00OO0O0000OO0O .operationtimer )#line:2325
        O0O00OO0O0000OO0O .operationtimer .Start (3000 )#line:2326
    def Price_view (O0O0O0O0OOOOO0O00 ,O00000O00OOO0O000 ):#line:2329
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:2330
        print (zxco0o0o0o0_view ,zxco0o0o0o0_count )#line:2331
        if zxco0o0o0o0_view and zxco0o0o0o0_count >=4 :#line:2332
            try :#line:2333
                O0O0O0O0OOOOO0O00 .Price_close ()#line:2334
            except :#line:2335
                pass #line:2336
            O0O0O0O0OOOOO0O00 .Screen_shot ()#line:2337
            O0O0OO000OOOOOOO0 ="sc_new.png"#line:2338
            O0O0O0O0OOOOO0O00 .zxco0o0o0o0frame =PriceFrame (O0O0OO000OOOOOOO0 )#line:2339
            O0O0O0O0OOOOO0O00 .zxco0o0o0o0frame .Show (True )#line:2340
            zxco0o0o0o0_view =False #line:2341
            zxco0o0o0o0_on =True #line:2342
            print ("到这5")#line:2343
    def Price_count (OO00O00O0OOOO000O ,OOO000O0O0OO00OO0 ):#line:2345
        global zxco0o0o0o0_count #line:2347
        zxco0o0o0o0_count +=1 #line:2348
        OOOOO0O0O0O0OOOO0 ='sc_new.png'#line:2349
        if web_on and ghjo0o0o0o0_on :#line:2350
            OO00O00O0OOOO000O .O0O0O0O0O0O0Oframe .Show (True )#line:2351
        if not os .path .exists (OOOOO0O0O0O0OOOO0 ):#line:2352
            try :#line:2353
                OO00O00O0OOOO000O .Price_close ()#line:2354
            except :#line:2355
                pass #line:2356
        if not ghjo0o0o0o0_on or not web_on :#line:2358
            OO00O00O0OOOO000O .O0O0O0O0O0O0Oframe .Show (False )#line:2359
    def Screen_shot (OOOO0OO000OOOOO00 ):#line:2364
        global Pricesize #line:2365
        O0O00O0OOOOO00000 =Pos_zxco0o0o0o0 #line:2366
        O0OOO0O0O00000O0O =ImageGrab .grab (O0O00O0OOOOO00000 )#line:2367
        O0OOO0O0O00000O0O .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:2368
    @staticmethod #line:2371
    def Del_shot ():#line:2372
        try :#line:2373
            os .remove ("sc_new.png")#line:2374
        except :#line:2375
            pass #line:2376
    def Price_close (O0O000O0O0000OO00 ):#line:2379
        try :#line:2380
            O0O000O0O0000OO00 .zxco0o0o0o0frame .Destroy ()#line:2381
        except :#line:2382
            pass #line:2383
    def opt (OOOOOOO0O0OO00O00 ,OOO0O0OOOOOO0OOO0 ):#line:2387
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2388
        global ghjo0o0o0o0_on #line:2389
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2390
        if OOOOOOO0O0OO00O00 .select_stractagy .GetSelection ==0 :#line:2391
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2392
                print ("触发1")#line:2393
                twice =False #line:2394
                ghjo0o0o0o0_on =True #line:2395
                oo0o0O0O0O0_on =True #line:2396
                oOO0O0O0O0O0O0_on =False #line:2397
                oOO0O0O0O0O0O0_num =1 #line:2398
                oOO0O0O0O0O0O0_OK =False #line:2399
                oOO0O0O0O0O0O0_one =False #line:2400
        elif OOOOOOO0O0OO00O00 .select_stractagy .GetSelection ==1 :#line:2401
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2402
                print ("触发2")#line:2403
                ghjo0o0o0o0_on =True #line:2404
                twice =True #line:2405
                oo0o0O0O0O0_on =True #line:2406
                oOO0O0O0O0O0O0_on =False #line:2407
                oOO0O0O0O0O0O0_num =1 #line:2408
                oOO0O0O0O0O0O0_OK =False #line:2409
                oOO0O0O0O0O0O0_one =False #line:2410
    def Add_time (OOOO00OOOOOO0OO00 ,O000O00OO000O000O ):#line:2414
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2415
        if o0sdofsfo0sodf0so0_on :#line:2416
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2417
        else :#line:2418
            a_time +=0.1 #line:2419
    def Minus_time (OO0000O000O0O00OO ,O00O0O0O00OOOO0OO ):#line:2421
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2422
        if o0sdofsfo0sodf0so0_on :#line:2423
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2424
        else :#line:2425
            a_time -=0.1 #line:2426
    def Add_ooo0O0o0oO0O (O0OO0O00O000O000O ,O0OOOOO00O000OO0O ):#line:2428
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2429
        if o0sdofsfo0sodf0so0_on :#line:2430
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2431
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2432
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2433
        else :#line:2434
            a_time +=1 #line:2435
    def Minus_ooo0O0o0oO0O (OOOO00000OO0OOO00 ,OO0000O0OO0O0O000 ):#line:2437
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2438
        if o0sdofsfo0sodf0so0_on :#line:2439
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2440
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2441
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2442
        else :#line:2443
            a_time -=1 #line:2444
    def Timeview (OOO0O0O0O0O0OO0O0 ,OO00000O0O000OO0O ):#line:2446
        OO000O00O0OO00O0O =OO00000O0O000OO0O .GetEventObject ()#line:2447
        global view_time ,time_on #line:2448
        if OO000O00O0OO00O0O .IsChecked ():#line:2449
            view_time =True #line:2450
            time_on =True #line:2451
            if ooweo0o0werwr_on :#line:2452
                OOO0O0O0O0O0OO0O0 .timeframe1 .Show (True )#line:2453
            elif o0sdofsfo0sodf0so0_on :#line:2454
                OOO0O0O0O0O0OO0O0 .timeframe2 .Show (True )#line:2455
        else :#line:2456
            view_time =False #line:2457
            time_on =False #line:2458
            if ooweo0o0werwr_on :#line:2459
                OOO0O0O0O0O0OO0O0 .timeframe1 .Show (False )#line:2460
            elif o0sdofsfo0sodf0so0_on :#line:2461
                OOO0O0O0O0O0OO0O0 .timeframe2 .Show (False )#line:2462
    def Opentime (OOOOOO0OOOOO0OOO0 ):#line:2464
        if o0sdofsfo0sodf0so0_on :#line:2465
            try :#line:2466
                OOOOOO0OOOOO0OOO0 .timeframe2 .Show (True )#line:2467
            except :#line:2468
                pass #line:2469
        elif ooweo0o0werwr_on :#line:2470
            try :#line:2471
                OOOOOO0OOOOO0OOO0 .timeframe1 .Show (True )#line:2472
            except :#line:2473
                pass #line:2474
    def Closetime (OOOO0OOOOOOOO0OO0 ):#line:2477
        try :#line:2478
            OOOO0OOOOOOOO0OO0 .timeframe1 .Show (False )#line:2479
        except :#line:2480
            pass #line:2481
        try :#line:2482
            OOOO0OOOOOOOO0OO0 .timeframe2 .Show (False )#line:2483
        except :#line:2484
            pass #line:2485
    def Confirmchoice (OOOO000OOOO00000O ,O00O0OOOOO0OOO0OO ):#line:2487
        global e_on ,enter_on #line:2488
        OO0OO0O0000O0O00O =OOOO000OOOO00000O .sdfsf24324297_choice .GetSelection ()#line:2489
        if OO0OO0O0000O0O00O ==0 :#line:2490
            e_on =True #line:2491
            enter_on =False #line:2492
        elif OO0OO0O0000O0O00O ==1 :#line:2493
            e_on =False #line:2494
            enter_on =True #line:2495
    def Jiajia_time (OO0OOO0000000OO00 ,O0O00OO0OO00O000O ):#line:2499
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2500
        OOO0O0O000O00O000 =OO0OOO0000000OO00 .jiajia_time .GetValue ()#line:2501
        OOO0OOO0OOOOOO0O0 =[40 +OO000OOOO000O0000 *0.1 for OO000OOOO000O0000 in range (151 )]#line:2502
        if OOO0O0O000O00O000 in OOO0OOO0OOOOOO0O0 :#line:2503
            OO00000o01 =OOO0O0O000O00O000 #line:2504
            OO00000o01 =float (OO00000o01 )#line:2505
            one_oO0O0O0O0O0O0O0O01 =OO0OOO0000000OO00 .gettime (OO00000o01 )#line:2506
        else :#line:2507
            OO0OOO0000000OO00 .jiajia_time .SetValue (OO00000o01 )#line:2508
    def Jiajia_zxco0o0o0o0 (OOOO0OOO00000OO0O ,O00OO00OOO000O0OO ):#line:2511
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2512
        O0OO0OO00O00OO000 =[300 +OOOOO0OOOOO000O0O *100 for OOOOO0OOOOO000O0O in range (13 )]#line:2513
        OOO0O0OOO0OO0O0OO =OOOO0OOO00000OO0O .jiajia_zxco0o0o0o0 .GetValue ()#line:2514
        if OOO0O0OOO0OO0O0OO in O0OO0OO00O00OO000 :#line:2515
            one_diff =int (OOO0O0OOO0OO0O0OO )#line:2516
        else :#line:2517
            OOOO0OOO00000OO0O .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2518
    def Select_oOO0O0O0O0O0O0 (O00O0OOO0OOO0O0O0 ,OOOOO000OOOO0OO00 ):#line:2521
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2522
        O000O0O0O00O0O0OO =O00O0OOO0OOO0O0O0 .select_oOO0O0O0O0O0O0 .GetString (O00O0OOO0OOO0O0O0 .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2523
        if O000O0O0O00O0O0OO ==u"提前100":#line:2524
            one_advance =100 #line:2525
        elif O000O0O0O00O0O0OO ==u"提前200":#line:2526
            one_advance =200 #line:2527
        else :#line:2528
            one_advance =0 #line:2529
    def Yanchi_time (O0OOOOOO0OO000OOO ,O00O0O0OO0O0O0OOO ):#line:2531
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2532
        O00OOO0OOOOO0OOOO =['0.%d'%OO0000OOOOOO0O000 for OO0000OOOOOO0O000 in range (11 )]#line:2533
        O00OOO0OOOOO0OOOO .append ('1.0')#line:2534
        O0OO0OOO00000OO00 =str (O0OOOOOO0OO000OOO .yanchi_time .GetValue ())#line:2535
        if O0OO0OOO00000OO00 in O00OOO0OOOOO0OOOO :#line:2536
            one_delay =float (O0OO0OOO00000OO00 )#line:2537
        else :#line:2538
            O0OOOOOO0OO000OOO .yanchi_time .SetValue (one_delay )#line:2539
    def Tijiao_time (O000OO000O000000O ,O000O00OO00OO00OO ):#line:2541
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2542
        OO0O0OO0OO0O00OO0 =O000OO000O000000O .oOO0O0O0O0O0O0_time .GetValue ()#line:2543
        O0O0O0OO00O00OOOO =[40 +OO0O0O0000O000O0O *0.1 for OO0O0O0000O000O0O in range (171 )]#line:2544
        if OO0O0OO0OO0O00OO0 in O0O0O0OO00O00OOOO :#line:2545
            OO00000o02 =float (OO0O0OO0OO0O00OO0 )#line:2546
            one_oO0O0O0O0O0O0O0O02 =O000OO000O000000O .gettime (OO00000o02 )#line:2547
        else :#line:2548
            O000OO000O000000O .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2549
    def Jiajia_time2 (O000O000O0OO000OO ,OO0O0OOO0O000OOO0 ):#line:2551
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2552
        OO0OO0O00O0OOO000 =O000O000O0OO000OO .jiajia_time2 .GetValue ()#line:2553
        O00O00000OOO0O0O0 =[40 +O0O0O0OOOO000OO0O *0.1 for O0O0O0OOOO000OO0O in range (151 )]#line:2554
        if OO0OO0O00O0OOO000 in O00O00000OOO0O0O0 :#line:2555
            ooo0O0o0oO0O_time1 =float (OO0OO0O00O0OOO000 )#line:2556
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O000O000O0OO000OO .gettime (ooo0O0o0oO0O_time1 )#line:2557
        else :#line:2558
            O000O000O0OO000OO .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2559
    def Jiajia_zxco0o0o0o02 (OOOO00OO00O000OOO ,O00OOOOOO000O00O0 ):#line:2561
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2562
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2563
        OOOO00OOO0OOO0O0O =[300 +OO0OOO0OO0O000O0O *100 for OO0OOO0OO0O000O0O in range (13 )]#line:2564
        OO0000O000O00O000 =OOOO00OO00O000OOO .jiajia_zxco0o0o0o02 .GetValue ()#line:2565
        if OO0000O000O00O000 in OOOO00OOO0OOO0O0O :#line:2566
            ooo0O0o0oO0O_diff =int (OO0000O000O00O000 )#line:2567
        else :#line:2568
            OOOO00OO00O000OOO .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2569
    def Select_oOO0O0O0O0O0O02 (O0O00OO0000OO0O00 ,OO000OOOOO00O0O00 ):#line:2571
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2572
        OOOO000000O0OO0OO =O0O00OO0000OO0O00 .select_oOO0O0O0O0O0O02 .GetString (O0O00OO0000OO0O00 .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2573
        if OOOO000000O0OO0OO ==u"提前100":#line:2574
            ooo0O0o0oO0O_advance =100 #line:2575
        elif OOOO000000O0OO0OO ==u"提前200":#line:2576
            ooo0O0o0oO0O_advance =200 #line:2577
        else :#line:2578
            ooo0O0o0oO0O_advance =0 #line:2579
    def Yanchi_time2 (O0OOO0OO00OO0O0OO ,O000O0OOOO0000OO0 ):#line:2582
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2583
        OOO0OOO00000O00O0 =['0.%d'%O0OO00OO0OOO0OO00 for O0OO00OO0OOO0OO00 in range (11 )]#line:2584
        OOO0OOO00000O00O0 .append ('1.0')#line:2585
        O000OO0OOO0000OOO =str (O0OOO0OO00OO0O0OO .yanchi_time2 .GetValue ())#line:2586
        if O000OO0OOO0000OOO in OOO0OOO00000O00O0 :#line:2587
            ooo0O0o0oO0O_delay =float (O000OO0OOO0000OOO )#line:2588
        else :#line:2589
            O0OOO0OO00OO0O0OO .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2590
    def Tijiao_time2 (O0OO0000000O0OOOO ,O0OO0O000OOOOOOO0 ):#line:2593
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2594
        O0O00O00OOO000000 =O0OO0000000O0OOOO .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2595
        OOO00OOOOOO0OO0OO =[53 +OO0OO0O0OOO0OOOOO *0.1 for OO0OO0O0OOO0OOOOO in range (41 )]#line:2596
        if O0O00O00OOO000000 in OOO00OOOOOO0OO0OO :#line:2597
            ooo0O0o0oO0O_time2 =float (O0O00O00OOO000000 )#line:2598
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0OO0000000O0OOOO .gettime (ooo0O0o0oO0O_time2 )#line:2599
        else :#line:2600
            O0OO0000000O0OOOO .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2601
    def Refresh_panel (O00OOO00O0O0O0OOO ,O0000OO0OOO0O00O0 ):#line:2605
        global ghjo0o0o0o0_on #line:2607
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2608
        O000O0OO00OO0O0O0 =O00OOO00O0O0O0OOO .select_stractagy .GetString (O00OOO00O0O0O0OOO .select_stractagy .GetSelection ())#line:2609
        if O000O0OO00OO0O0O0 ==u"单枪策略":#line:2610
            O00OOO00O0O0O0OOO .ss_Hide ()#line:2611
            twice =False #line:2612
            ghjo0o0o0o0_on =True #line:2613
            oo0o0O0O0O0_on =True #line:2614
            oOO0O0O0O0O0O0_on =False #line:2615
            oOO0O0O0O0O0O0_num =1 #line:2616
            oOO0O0O0O0O0O0_OK =False #line:2617
            oOO0O0O0O0O0O0_one =False #line:2618
        elif O000O0OO00OO0O0O0 ==u"双枪策略":#line:2620
            O00OOO00O0O0O0OOO .ss_Shown ()#line:2621
            ghjo0o0o0o0_on =True #line:2622
            twice =True #line:2623
            oo0o0O0O0O0_on =True #line:2624
            oOO0O0O0O0O0O0_on =False #line:2625
            oOO0O0O0O0O0O0_num =1 #line:2626
            oOO0O0O0O0O0O0_OK =False #line:2627
            oOO0O0O0O0O0O0_one =False #line:2628
        else :#line:2629
            O00OOO00O0O0O0OOO .none_show ()#line:2630
            ghjo0o0o0o0_on =False #line:2631
            twice =False #line:2632
    def ss_Shown (O0000O000O0000O0O ):#line:2635
        if not O0000O000O0000O0O .ooo0O0o0oO0Osizer_Shown :#line:2636
            O0000O000O0000O0O .vbox1 .Show (O0000O000O0000O0O .ooo0O0o0oO0OshotSizer )#line:2637
            O0000O000O0000O0O .ooo0O0o0oO0Osizer_Shown =True #line:2638
        if not O0000O000O0000O0O .oneshotsizer_Shown :#line:2639
            O0000O000O0000O0O .vbox1 .Show (O0000O000O0000O0O .oneshotSizer )#line:2640
            O0000O000O0000O0O .oneshotsizer_Shown =True #line:2641
        O0000O000O0000O0O .ooo0O0o0oO0Osizer_Shown =True #line:2642
        O0000O000O0000O0O .oneshotSizer_Shown =True #line:2643
        O0000O000O0000O0O .SetClientSize ((280 ,575 ))#line:2644
        O0000O000O0000O0O .Secondshot_reset ()#line:2645
        O0000O000O0000O0O .Layout ()#line:2646
    def ss_Hide (OOOO0OOO0OO00OO0O ):#line:2648
        if OOOO0OOO0OO00OO0O .ooo0O0o0oO0Osizer_Shown :#line:2649
            OOOO0OOO0OO00OO0O .vbox1 .Hide (OOOO0OOO0OO00OO0O .ooo0O0o0oO0OshotSizer )#line:2650
        if not OOOO0OOO0OO00OO0O .oneshotsizer_Shown :#line:2653
            OOOO0OOO0OO00OO0O .vbox1 .Show (OOOO0OOO0OO00OO0O .oneshotSizer )#line:2654
        OOOO0OOO0OO00OO0O .ooo0O0o0oO0Osizer_Shown =False #line:2655
        OOOO0OOO0OO00OO0O .oneshotSizer_Shown =True #line:2656
        OOOO0OOO0OO00OO0O .SetClientSize ((280 ,375 ))#line:2657
        OOOO0OOO0OO00OO0O .Oneshot_reset ()#line:2658
        OOOO0OOO0OO00OO0O .Layout ()#line:2659
    def none_show (O0O0O0OOOO0O0O0OO ):#line:2661
        if O0O0O0OOOO0O0O0OO .oneshotsizer_Shown :#line:2662
            O0O0O0OOOO0O0O0OO .vbox1 .Hide (O0O0O0OOOO0O0O0OO .ooo0O0o0oO0OshotSizer )#line:2663
        if O0O0O0OOOO0O0O0OO .ooo0O0o0oO0Osizer_Shown :#line:2664
            O0O0O0OOOO0O0O0OO .vbox1 .Hide (O0O0O0OOOO0O0O0OO .oneshotSizer )#line:2665
        O0O0O0OOOO0O0O0OO .oneshotsizer_Shown =False #line:2667
        O0O0O0OOOO0O0O0OO .ooo0O0o0oO0Osizer_Shown =False #line:2668
        O0O0O0OOOO0O0O0OO .SetClientSize ((280 ,255 ))#line:2669
        O0O0O0OOOO0O0O0OO .Layout ()#line:2670
    def Oneshot_reset (OOOOO0O0000000O0O ):#line:2672
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2673
        OOOOO0O0000000O0O .jiajia_time .SetValue (48.0 )#line:2674
        OOOOO0O0000000O0O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2675
        OOOOO0O0000000O0O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2676
        OOOOO0O0000000O0O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2677
        OOOOO0O0000000O0O .yanchi_time .SetValue (0.5 )#line:2678
        OO00000o01 =48 #line:2680
        OO00000o02 =55 #line:2681
        one_diff =700 #line:2682
        one_delay =0.5 #line:2683
        one_advance =100 #line:2684
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2686
        one_oO0O0O0O0O0O0O0O01 =OOOOO0O0000000O0O .gettime (OO00000o01 )#line:2687
        one_oO0O0O0O0O0O0O0O02 =OOOOO0O0000000O0O .gettime (OO00000o02 )#line:2688
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOOOO0O0000000O0O .gettime (ooo0O0o0oO0O_time1 )#line:2689
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOOOO0O0000000O0O .gettime (ooo0O0o0oO0O_time2 )#line:2690
    def Secondshot_reset (OOO0OOOO0O0OO0OOO ):#line:2693
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2694
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2695
        OOO0OOOO0O0OO0OOO .jiajia_time .SetValue (40.0 )#line:2696
        OOO0OOOO0O0OO0OOO .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:2697
        OOO0OOOO0O0OO0OOO .jiajia_zxco0o0o0o0 .SetValue (500 )#line:2698
        OOO0OOOO0O0OO0OOO .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2699
        OOO0OOOO0O0OO0OOO .yanchi_time .SetValue (0.0 )#line:2700
        OOO0OOOO0O0OO0OOO .jiajia_time2 .SetValue (50.0 )#line:2702
        OOO0OOOO0O0OO0OOO .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:2703
        OOO0OOOO0O0OO0OOO .jiajia_zxco0o0o0o02 .SetValue (700 )#line:2704
        OOO0OOOO0O0OO0OOO .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2705
        OOO0OOOO0O0OO0OOO .yanchi_time2 .SetValue (0.5 )#line:2706
        OO00000o01 =40 #line:2708
        OO00000o02 =48 #line:2709
        one_diff =500 #line:2710
        one_delay =0.5 #line:2711
        one_advance =100 #line:2712
        ooo0O0o0oO0O_time1 =50 #line:2714
        ooo0O0o0oO0O_time2 =55.5 #line:2715
        ooo0O0o0oO0O_diff =700 #line:2716
        ooo0O0o0oO0O_delay =0.5 #line:2717
        ooo0O0o0oO0O_advance =100 #line:2718
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2720
        one_oO0O0O0O0O0O0O0O01 =OOO0OOOO0O0OO0OOO .gettime (OO00000o01 )#line:2721
        one_oO0O0O0O0O0O0O0O02 =OOO0OOOO0O0OO0OOO .gettime (OO00000o02 )#line:2722
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOO0OOOO0O0OO0OOO .gettime (ooo0O0o0oO0O_time1 )#line:2723
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOO0OOOO0O0OO0OOO .gettime (ooo0O0o0oO0O_time2 )#line:2724
    def Strategy_save (OOO0000OOO00O0OOO ,OO00O00O0OOO00OOO ):#line:2727
        OOOOO00OO0O0OOOOO =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:2729
        if OOOOO00OO0O0OOOOO .ShowModal ()==wx .ID_OK :#line:2730
            O0O0O000OO000OOO0 =OOOOO00OO0O0OOOOO .GetValue ()#line:2731
            if O0O0O000OO000OOO0 :#line:2732
                OOOO0OOO0O0OOO00O =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:2733
                if OOOO0OOO0O0OOO00O ==wx .ID_OK :#line:2734
                    OOOO0OOO0O0OOO00O .Destroy ()#line:2735
                    OOOOO00OO0O0OOOOO .Destroy ()#line:2736
                OOO0000OOO00O0OOO .save (O0O0O000OO000OOO0 )#line:2737
            else :#line:2738
                OOOO0OOO0O0OOO00O =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:2739
                if OOOO0OOO0O0OOO00O ==wx .ID_OK :#line:2740
                    OOOO0OOO0O0OOO00O .Destroy ()#line:2741
                    OOOOO00OO0O0OOOOO .Destroy ()#line:2742
    def save (OOOO00O0000O00O0O ,O00O00O0000OOOOO0 ):#line:2744
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2745
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2746
        global osl ,e_on ,enter_on #line:2747
        if OOOO00O0000O00O0O .select_stractagy .GetSelection ()==2 :#line:2749
            OO0O000O000000OO0 =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:2750
            if OO0O000O000000OO0 ==wx .ID_OK :#line:2751
                OO0O000O000000OO0 .Destroy ()#line:2752
        elif OOOO00O0000O00O0O .select_stractagy .GetSelection ()==0 :#line:2753
            osl [0 ]=0 #line:2754
            osl [1 ]=OO00000o01 #line:2755
            osl [2 ]=OO00000o02 #line:2756
            osl [3 ]=one_diff #line:2757
            osl [4 ]=one_delay #line:2758
            osl [5 ]=one_advance #line:2759
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2760
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2761
            osl [8 ]=ooo0O0o0oO0O_diff #line:2762
            osl [9 ]=ooo0O0o0oO0O_delay #line:2763
            osl [10 ]=ooo0O0o0oO0O_advance #line:2764
            osl [11 ]=e_on #line:2765
            osl [12 ]=enter_on #line:2766
        elif OOOO00O0000O00O0O .select_stractagy .GetSelection ()==1 :#line:2767
            osl [0 ]=1 #line:2768
            osl [0 ]=1 #line:2769
            osl [1 ]=OO00000o01 #line:2770
            osl [2 ]=OO00000o02 #line:2771
            osl [3 ]=one_diff #line:2772
            osl [4 ]=one_delay #line:2773
            osl [5 ]=one_advance #line:2774
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2775
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2776
            osl [8 ]=ooo0O0o0oO0O_diff #line:2777
            osl [9 ]=ooo0O0o0oO0O_delay #line:2778
            osl [10 ]=ooo0O0o0oO0O_advance #line:2779
            osl [11 ]=e_on #line:2780
            osl [12 ]=enter_on #line:2781
        with open ('%s.ghjo0o0o0o0'%O00O00O0000OOOOO0 ,'wb')as OOO0OOOOO0O000O00 :#line:2782
            pickle .dump (osl ,OOO0OOOOO0O000O00 )#line:2783
    def Strategy_load (O0OO000OO00O0O00O ,O0O000OO0O0O0O0O0 ):#line:2798
        import os as O0000OO00O0OOOO00 #line:2799
        OO0000OOO0O0OOO00 =O0000OO00O0OOOO00 .getcwd ()#line:2800
        O000OO00OO0000O00 =O0OO000OO00O0O00O .findfiles (OO0000OOO0O0OOO00 )#line:2801
        if O000OO00OO0000O00 :#line:2802
            OO000O00OOOOOOO00 =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =O000OO00OO0000O00 )#line:2804
            if OO000O00OOOOOOO00 .ShowModal ()==wx .ID_OK :#line:2805
                OO0000OOO0O0OOO00 =OO000O00OOOOOOO00 .GetStringSelection ()#line:2806
                OO0O000OOOOOOOO00 =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:2807
                if OO0O000OOOOOOOO00 .ShowModal ()==wx .ID_OK :#line:2808
                    OO0O000OOOOOOOO00 .Destroy ()#line:2809
                O0OO000OO00O0O00O .load (OO0000OOO0O0OOO00 )#line:2810
            print ("载入")#line:2811
            OO000O00OOOOOOO00 .Destroy ()#line:2812
        else :#line:2813
            OO0O000OOOOOOOO00 =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:2814
            if OO0O000OOOOOOOO00 ==wx .ID_OK :#line:2815
                OO0O000OOOOOOOO00 .Destroy ()#line:2816
                OO000O00OOOOOOO00 .Destroy ()#line:2817
    def load (O0OOOOOO0OO0O0000 ,OO0O0OO000O0O00O0 ):#line:2819
        global osl ,e_on ,enter_on #line:2820
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2821
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2822
        global ghjo0o0o0o0_on #line:2824
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2825
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2826
        try :#line:2827
            with open (OO0O0OO000O0O00O0 ,'rb')as O0OOO0OO0000000OO :#line:2828
                osl =pickle .load (O0OOO0OO0000000OO )#line:2829
        except :#line:2830
            pass #line:2831
        if osl [0 ]==0 :#line:2832
            O0OOOOOO0OO0O0000 .ss_Hide ()#line:2833
            twice =False #line:2836
            ghjo0o0o0o0_on =True #line:2837
            oo0o0O0O0O0_on =True #line:2838
            oOO0O0O0O0O0O0_on =False #line:2839
            oOO0O0O0O0O0O0_num =1 #line:2840
            oOO0O0O0O0O0O0_OK =False #line:2841
            oOO0O0O0O0O0O0_one =False #line:2842
            O0OOOOOO0OO0O0000 .select_stractagy .SetSelection (0 )#line:2844
            O0OOOOOO0OO0O0000 .jiajia_time .SetValue (osl [1 ])#line:2845
            O0OOOOOO0OO0O0000 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2846
            O0OOOOOO0OO0O0000 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2847
            O0OOOOOO0OO0O0000 .yanchi_time .SetValue (osl [4 ])#line:2848
            if osl [5 ]==100 :#line:2849
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2850
            elif osl [5 ]==200 :#line:2851
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2852
            else :#line:2853
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2854
            OO00000o01 =osl [1 ]#line:2856
            OO00000o02 =osl [2 ]#line:2857
            one_diff =osl [3 ]#line:2858
            one_delay =osl [4 ]#line:2859
            one_advance =osl [5 ]#line:2860
            e_on =osl [11 ]#line:2862
            enter_on =osl [12 ]#line:2863
            if e_on :#line:2864
                O0OOOOOO0OO0O0000 .sdfsf24324297_choice .SetSelection (0 )#line:2865
            elif enter_on :#line:2866
                O0OOOOOO0OO0O0000 .sdfsf24324297_choice .SetSelection (1 )#line:2867
            one_oO0O0O0O0O0O0O0O01 =O0OOOOOO0OO0O0000 .gettime (OO00000o01 )#line:2869
            one_oO0O0O0O0O0O0O0O02 =O0OOOOOO0OO0O0000 .gettime (OO00000o02 )#line:2870
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0OOOOOO0OO0O0000 .gettime (ooo0O0o0oO0O_time1 )#line:2871
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0OOOOOO0OO0O0000 .gettime (ooo0O0o0oO0O_time2 )#line:2872
        elif osl [0 ]==1 :#line:2874
            ghjo0o0o0o0_on =True #line:2875
            twice =True #line:2876
            oo0o0O0O0O0_on =True #line:2877
            oOO0O0O0O0O0O0_on =False #line:2878
            oOO0O0O0O0O0O0_num =1 #line:2879
            oOO0O0O0O0O0O0_OK =False #line:2880
            oOO0O0O0O0O0O0_one =False #line:2881
            O0OOOOOO0OO0O0000 .ss_Shown ()#line:2882
            O0OOOOOO0OO0O0000 .select_stractagy .SetSelection (1 )#line:2883
            O0OOOOOO0OO0O0000 .jiajia_time .SetValue (osl [1 ])#line:2884
            O0OOOOOO0OO0O0000 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2885
            O0OOOOOO0OO0O0000 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2886
            O0OOOOOO0OO0O0000 .yanchi_time .SetValue (osl [4 ])#line:2887
            if osl [5 ]==100 :#line:2888
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2889
            elif osl [5 ]==200 :#line:2890
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2891
            else :#line:2892
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2893
            O0OOOOOO0OO0O0000 .jiajia_time2 .SetValue (osl [6 ])#line:2894
            O0OOOOOO0OO0O0000 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:2895
            O0OOOOOO0OO0O0000 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:2896
            O0OOOOOO0OO0O0000 .yanchi_time2 .SetValue (osl [9 ])#line:2897
            if osl [10 ]==100 :#line:2898
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2899
            elif osl [10 ]==200 :#line:2900
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:2901
            else :#line:2902
                O0OOOOOO0OO0O0000 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:2903
            OO00000o01 =osl [1 ]#line:2906
            OO00000o02 =osl [2 ]#line:2907
            one_diff =osl [3 ]#line:2908
            one_delay =osl [4 ]#line:2909
            one_advance =osl [5 ]#line:2910
            ooo0O0o0oO0O_time1 =osl [6 ]#line:2912
            ooo0O0o0oO0O_time2 =osl [7 ]#line:2913
            ooo0O0o0oO0O_diff =osl [8 ]#line:2914
            ooo0O0o0oO0O_delay =osl [9 ]#line:2915
            ooo0O0o0oO0O_advance =osl [10 ]#line:2916
            e_on =osl [11 ]#line:2918
            enter_on =osl [12 ]#line:2919
            if e_on :#line:2920
                O0OOOOOO0OO0O0000 .sdfsf24324297_choice .SetSelection (0 )#line:2921
            elif enter_on :#line:2922
                O0OOOOOO0OO0O0000 .sdfsf24324297_choice .SetSelection (1 )#line:2923
            one_oO0O0O0O0O0O0O0O01 =O0OOOOOO0OO0O0000 .gettime (OO00000o01 )#line:2925
            one_oO0O0O0O0O0O0O0O02 =O0OOOOOO0OO0O0000 .gettime (OO00000o02 )#line:2926
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0OOOOOO0OO0O0000 .gettime (ooo0O0o0oO0O_time1 )#line:2927
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0OOOOOO0OO0O0000 .gettime (ooo0O0o0oO0O_time2 )#line:2928
    def findfiles (OOOOOO00OOO00O0O0 ,O0O0OO00OO00OO000 ):#line:2930
        OO0OOOOO000000O0O =[]#line:2931
        for OOO00O0O0OO000O0O ,OO0OO00O00000OO0O ,O0000OOO0O00O0O0O in os .walk (O0O0OO00OO00OO000 ):#line:2932
            for OOOO00O00O00OO0OO in O0000OOO0O00O0O0O :#line:2933
                if os .path .splitext (OOOO00O00O00OO0OO )[1 ]=='.ghjo0o0o0o0':#line:2934
                    OO0OOOOO000000O0O .append (os .path .join (OOO00O0O0OO000O0O ,OOOO00O00O00OO0OO ))#line:2935
        return OO0OOOOO000000O0O #line:2936
    def Save_info (OOO0O0OOO0O0OO00O ,OO000OO00OOO0O0O0 ):#line:2938
        pass #line:2939
    def changetime (OOOOO0OOO0OO00000 ,O00O00OOOO00O0O0O ):#line:2944
        OO0OO00OO0OO0OO00 =time .mktime (time .strptime (O00O00OOOO00O0O0O ,'%Y-%m-%d %H:%M:%S'))#line:2945
        return OO0OO00OO0OO0OO00 #line:2946
    def get_nowtime (O00O0OOOO00O0O0O0 ):#line:2949
        O00O0OO000O00OOOO =time .time ()#line:2950
        OOOO0O000O0O00O0O =time .strftime ('%Y-%m-%d',time .localtime (O00O0OO000O00OOOO ))#line:2951
        return OOOO0O000O0O00O0O #line:2952
    def gettime (OOOOO0OO0000O0O0O ,OO0O0OO00OOOOO000 ):#line:2955
        O00OOOOO000OO00O0 =OOOOO0OO0000O0O0O .get_nowtime ()#line:2956
        OOO0OO0OO0OO00OO0 =O00OOOOO000OO00O0 +' 11:29:'+str (int (OO0O0OO00OOOOO000 ))#line:2957
        OO000OOO00O0O0000 =OOOOO0OO0000O0O0O .changetime (OOO0OO0OO0OO00OO0 )+float (OO0O0OO00OOOOO000 )-int (OO0O0OO00OOOOO000 )#line:2958
        return OO000OOO00O0O0000 #line:2959
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:2962
    def __init__ (OO0OOOOO00O00O00O ,O000O0OOO00OO000O ):#line:2963
        wx .Window .__init__ (OO0OOOOO00O00O00O ,O000O0OOO00OO000O ,size =Timesize )#line:2964
        OO0OOOOO00O00O00O .Bind (wx .EVT_PAINT ,OO0OOOOO00O00O00O .OnPaint )#line:2965
        OO0OOOOO00O00O00O .timer =wx .Timer (OO0OOOOO00O00O00O )#line:2966
        OO0OOOOO00O00O00O .Bind (wx .EVT_TIMER ,OO0OOOOO00O00O00O .OnTimer ,OO0OOOOO00O00O00O .timer )#line:2967
        OO0OOOOO00O00O00O .timer .Start (100 )#line:2968
    def Draw (OO00000OO0O000000 ,O0O0O0OO000O0OOO0 ):#line:2970
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2971
        OOO0OO0OO0O0O000O =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2972
        OOOOOOOOO00O0OOOO ,O00000OO00O0000OO =OO00000OO0O000000 .GetClientSize ()#line:2973
        O0O0O0OO000O0OOO0 .SetBackground (wx .Brush (OO00000OO0O000000 .GetBackgroundColour ()))#line:2974
        O0O0O0OO000O0OOO0 .Clear ()#line:2975
        O0O0O0OO000O0OOO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2976
        O00OOO00OOO0O0O00 ,O0OOOO0OO0O0OO0OO =O0O0O0OO000O0OOO0 .GetTextExtent (OOO0OO0OO0O0O000O )#line:2977
        O0O0O0OO000O0OOO0 .DrawText (OOO0OO0OO0O0O000O ,(OOOOOOOOO00O0OOOO -O00OOO00OOO0O0O00 )/2 ,(O00000OO00O0000OO )/2 -O0OOOO0OO0O0OO0OO /2 )#line:2978
    def Modify (O0O0000OOO00O00O0 ,O000OO0OO00OOOOO0 ):#line:2980
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2981
        O00O000O000OO000O =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2982
        O0OO0000O0000OO00 ,OO0O00000000OOOO0 =O0O0000OOO00O00O0 .GetClientSize ()#line:2983
        O000OO0OO00OOOOO0 .SetBackground (wx .Brush (O0O0000OOO00O00O0 .GetBackgroundColour ()))#line:2984
        O000OO0OO00OOOOO0 .Clear ()#line:2985
        O000OO0OO00OOOOO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2986
        OO00OO000O000OO00 ,O000O00OO0OO0O0OO =O000OO0OO00OOOOO0 .GetTextExtent (O00O000O000OO000O )#line:2987
        O000OO0OO00OOOOO0 .DrawText (O00O000O000OO000O ,(O0OO0000O0000OO00 -OO00OO000O000OO00 )/2 ,(OO0O00000000OOOO0 )/2 -O000O00OO0OO0O0OO /2 )#line:2988
    def OnTimer (O0OO0000OO0OO00OO ,OO00O0O0OOO0OOO00 ):#line:2990
        OO0OOO0O0OO000OOO =wx .BufferedDC (wx .ClientDC (O0OO0000OO0OO00OO ))#line:2991
        O0OO0000OO0OO00OO .Modify (OO0OOO0O0OO000OOO )#line:2992
    def OnPaint (OO0OOO0O00O00OOO0 ,OOO0OOO00O0OO0O00 ):#line:2994
        OO000000OOOOOOOO0 =wx .BufferedPaintDC (OO0OOO0O00O00OOO0 )#line:2995
        OO0OOO0O00O00OOO0 .Draw (OO000000OOOOOOOO0 )#line:2996
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:2998
    def __init__ (O00O00OO000OOO0O0 ):#line:2999
         wx .Frame .__init__ (O00O00OO000OOO0O0 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =O0O0O0O0O0O0Ozxco0o0o0o0frame_pos ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:3001
         Lowestzxco0o0o0o0Window (O00O00OO000OOO0O0 )#line:3004
import string #line:3022
import wx .lib .agw .hyperlink as hyperlink #line:3023
class LoginFrame (wx .Frame ):#line:3024
    def __init__ (O0O00OO0OO0O0OOO0 ,OOOOO000OOO0OO0OO ,OOOOO0O0OO0000OO0 ,OO000O0OOOOO000OO ):#line:3025
        wx .Frame .__init__ (O0O00OO0OO0O0OOO0 ,None ,-1 ,OOOOO000OOO0OO0OO ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3026
        O0O00OO0OO0O0OOO0 .Bind (wx .EVT_CLOSE ,O0O00OO0OO0O0OOO0 .OnClose )#line:3027
        O0O00OO0OO0O0OOO0 .panel =wx .Panel (O0O00OO0OO0O0OOO0 ,size =(300 ,220 ))#line:3028
        O0O00OO0OO0O0OOO0 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3029
        O0O00OO0OO0O0OOO0 .SetIcon (O0O00OO0OO0O0OOO0 .icon )#line:3030
        O0O00OO0OO0O0OOO0 .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3043
        O0O00OO0OO0O0OOO0 .welcomelabel =wx .StaticText (O0O00OO0OO0O0OOO0 .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3044
        O0O00OO0OO0O0OOO0 .sizer_v1 .Add (O0O00OO0OO0O0OOO0 .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3045
        O0O00OO0OO0O0OOO0 .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3048
        O0O00OO0OO0O0OOO0 .userlabel =wx .StaticText (O0O00OO0OO0O0OOO0 .panel ,-1 ,label ="账号")#line:3049
        O0O00OO0OO0O0OOO0 .userText =wx .TextCtrl (O0O00OO0OO0O0OOO0 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3051
        O0O00OO0OO0O0OOO0 .userbox .Add (O0O00OO0OO0O0OOO0 .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3052
        O0O00OO0OO0O0OOO0 .userbox .Add (O0O00OO0OO0O0OOO0 .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3053
        O0O00OO0OO0O0OOO0 .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3055
        O0O00OO0OO0O0OOO0 .passlabel =wx .StaticText (O0O00OO0OO0O0OOO0 .panel ,-1 ,label ="密码")#line:3056
        O0O00OO0OO0O0OOO0 .passText =wx .TextCtrl (O0O00OO0OO0O0OOO0 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3058
        O0O00OO0OO0O0OOO0 .passbox .Add (O0O00OO0OO0O0OOO0 .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3059
        O0O00OO0OO0O0OOO0 .passbox .Add (O0O00OO0OO0O0OOO0 .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3060
        if OOOOO0O0OO0000OO0 :#line:3061
            O0O00OO0OO0O0OOO0 .userText .SetValue (OOOOO0O0OO0000OO0 )#line:3062
        if OO000O0OOOOO000OO :#line:3063
            O0O00OO0OO0O0OOO0 .passText .SetValue (OO000O0OOOOO000OO )#line:3064
        O0O00OO0OO0O0OOO0 .sizer_v1 .Add (O0O00OO0OO0O0OOO0 .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3065
        O0O00OO0OO0O0OOO0 .sizer_v1 .Add (O0O00OO0OO0O0OOO0 .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3066
        O0O00OO0OO0O0OOO0 .Bind (wx .EVT_TEXT_ENTER ,O0O00OO0OO0O0OOO0 .OnLogin ,O0O00OO0OO0O0OOO0 .userText )#line:3068
        O0O00OO0OO0O0OOO0 .Bind (wx .EVT_TEXT_ENTER ,O0O00OO0OO0O0OOO0 .OnLogin ,O0O00OO0OO0O0OOO0 .passText )#line:3069
        O0O00OO0OO0O0OOO0 .o0sdofsfo0sodf0so0btn =wx .Button (O0O00OO0OO0O0OOO0 .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3071
        O0O00OO0OO0O0OOO0 .loginbtn =wx .Button (O0O00OO0OO0O0OOO0 .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3072
        O0O00OO0OO0O0OOO0 .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3073
        O0O00OO0OO0O0OOO0 .btnSizer .Add (O0O00OO0OO0O0OOO0 .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3074
        O0O00OO0OO0O0OOO0 .btnSizer .Add (O0O00OO0OO0O0OOO0 .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3075
        O0O00OO0OO0O0OOO0 .sizer_v1 .Add (O0O00OO0OO0O0OOO0 .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3076
        O0O00OO0OO0O0OOO0 .loginbtn .Bind (wx .EVT_BUTTON ,O0O00OO0OO0O0OOO0 .OnLogin ,O0O00OO0OO0O0OOO0 .loginbtn )#line:3077
        O0O00OO0OO0O0OOO0 .purchaselink =hyperlink .HyperLinkCtrl (O0O00OO0OO0O0OOO0 .panel ,-1 ,u"购买账号")#line:3079
        O0O00OO0OO0O0OOO0 .purchaselink .UnsetToolTip ()#line:3080
        O0O00OO0OO0O0OOO0 .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O0O00OO0OO0O0OOO0 .Purchase )#line:3081
        O0O00OO0OO0O0OOO0 .purchaselink .AutoBrowse (False )#line:3082
        O0O00OO0OO0O0OOO0 .purchaselink .EnableRollover (True )#line:3083
        O0O00OO0OO0O0OOO0 .purchaselink .SetUnderlines (False ,False ,True )#line:3084
        O0O00OO0OO0O0OOO0 .purchaselink .OpenInSameWindow (True )#line:3085
        O0O00OO0OO0O0OOO0 .purchaselink .UpdateLink ()#line:3086
        O0O00OO0OO0O0OOO0 .helplink =hyperlink .HyperLinkCtrl (O0O00OO0OO0O0OOO0 .panel ,-1 ,u"查看帮助")#line:3088
        O0O00OO0OO0O0OOO0 .helplink .UnsetToolTip ()#line:3089
        O0O00OO0OO0O0OOO0 .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O0O00OO0OO0O0OOO0 .Purchase )#line:3090
        O0O00OO0OO0O0OOO0 .helplink .AutoBrowse (False )#line:3091
        O0O00OO0OO0O0OOO0 .helplink .EnableRollover (True )#line:3092
        O0O00OO0OO0O0OOO0 .helplink .SetUnderlines (False ,False ,True )#line:3093
        O0O00OO0OO0O0OOO0 .helplink .OpenInSameWindow (True )#line:3094
        O0O00OO0OO0O0OOO0 .helplink .UpdateLink ()#line:3095
        O0O00OO0OO0O0OOO0 .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3097
        O0O00OO0OO0O0OOO0 .linkbox .Add (O0O00OO0OO0O0OOO0 .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3098
        O0O00OO0OO0O0OOO0 .linkbox .Add (O0O00OO0OO0O0OOO0 .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3099
        O0O00OO0OO0O0OOO0 .sizer_v1 .Add (O0O00OO0OO0O0OOO0 .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3100
        O0O00OO0OO0O0OOO0 .SetSizer (O0O00OO0OO0O0OOO0 .sizer_v1 )#line:3102
        O0O00OO0OO0O0OOO0 .Center ()#line:3103
        pub .subscribe (O0O00OO0OO0O0OOO0 .connect_success ,"connect")#line:3105
        O0O00OO0OO0O0OOO0 .hashthread =HashThread ()#line:3108
    def connect_success (O0O00OOO0O00O0OOO ):#line:3110
        O0O00OOO0O00O0OOO .loginbtn .Enable ()#line:3111
        global login_result #line:3112
        if login_result =='login success':#line:3113
            O0O00OOO0O00O0OOO .Destroy ()#line:3114
            O0O00OOO0O00O0OOO .topframe =TopFrame ('小鲜肉拍牌',version )#line:3115
            O0O00OOO0O00O0OOO .topframe .Show (True )#line:3116
        elif login_result =='net error':#line:3118
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3119
        elif login_result =='repeat':#line:3120
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3121
        elif login_result =='wrong account':#line:3122
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3123
        elif login_result =='wrong password':#line:3124
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3125
        else :#line:3126
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3127
    def OnEraseBack (O000OO0O0O000000O ,O000OO0OO0O0OO000 ):#line:3130
        OO000000OOO0OOO0O =O000OO0OO0O0OO000 .GetDC ()#line:3131
        if not OO000000OOO0OOO0O :#line:3132
            OO000000OOO0OOO0O =wx .ClientDC (O000OO0O0O000000O )#line:3133
            OOO000O0OO0O0OOOO =O000OO0O0O000000O .GetUpdateRegion ().GetBox ()#line:3134
            OO000000OOO0OOO0O .SetClippingRect (OOO000O0OO0O0OOOO )#line:3135
        OO000000OOO0OOO0O .Clear ()#line:3136
        OOOOOOOOO0O0OO0OO =wx .Bitmap ("blue.jpg")#line:3137
        OO000000OOO0OOO0O .DrawBitmap (OOOOOOOOO0O0OO0OO ,0 ,0 )#line:3138
    def OnClose (O0OOOO000OOOOO0O0 ,OO0OO0000000O0O00 ):#line:3140
        OO0OO0000000O0O00 .Skip ()#line:3141
        sys .exit (None )#line:3142
    def OnLogin (OO00O000OO00OO000 ,O0OOO0OOOOO000OOO ):#line:3150
        global Username ,Password #line:3151
        O0OO0OO0OOO000O00 =OO00O000OO00OO000 .userText .GetValue ()#line:3152
        O0O0O00OO00000O0O =OO00O000OO00OO000 .passText .GetValue ()#line:3153
        if O0OO0OO0OOO000O00 =="":#line:3154
            wx .MessageBox ('请输入用户名！')#line:3155
            OO00O000OO00OO000 .userText .SetFocus ()#line:3156
        elif O0O0O00OO00000O0O =="":#line:3157
            wx .MessageBox ('请输入密码！')#line:3158
            OO00O000OO00OO000 .passText .SetFocus ()#line:3159
        else :#line:3161
            Username =O0OO0OO0OOO000O00 #line:3162
            Password =O0O0O00OO00000O0O #line:3163
            OO00O000OO00OO000 .loginthread =LoginThread ()#line:3164
            O0OO00OOOOOO0OOOO =[O0OO0OO0OOO000O00 ,O0O0O00OO00000O0O ]#line:3165
            with open ('your.name','wb')as OOOOOOOO000OO00O0 :#line:3166
                pickle .dump (O0OO00OOOOOO0OOOO ,OOOOOOOO000OO00O0 )#line:3167
            O0OOO0OOOOO000OOO .GetEventObject ().Disable ()#line:3169
    def Purchase (OOO000000O0O00O0O ,OO0O0OO000000O00O ):#line:3171
        print ("购买")#line:3172
class UserValidator (wx .Validator ):#line:3176
    ""#line:3177
    def __init__ (OOOO000OO0O0OOO0O ,O0000O000OO0OOO00 ):#line:3179
        wx .Validator .__init__ (OOOO000OO0O0OOO0O )#line:3180
        OOOO000OO0O0OOO0O .flag =O0000O000OO0OOO00 #line:3181
        OOOO000OO0O0OOO0O .Bind (wx .EVT_CHAR ,OOOO000OO0O0OOO0O .OnChar )#line:3182
    def Clone (OOO0OOO0O00000OOO ):#line:3185
        ""#line:3186
        return UserValidator (OOO0OOO0O00000OOO .flag )#line:3187
    def Validate (OO00O0O000OO0O0O0 ,OOOO0OO0OO00OO0OO ):#line:3190
        return True #line:3191
    def TransferToWindow (OO000000O0O0OO0O0 ):#line:3194
        return True #line:3195
    def TransferFromWindow (O000O0O0OO00000O0 ):#line:3198
        return True #line:3199
    def OnChar (O0OO0O0OO0000OOO0 ,OOO0O00OOOOOOO00O ):#line:3202
        pass #line:3203
class PassValidator (wx .Validator ):#line:3217
    ""#line:3218
    def __init__ (O00000OOOO0000000 ):#line:3221
        wx .Validator .__init__ (O00000OOOO0000000 )#line:3222
        O00000OOOO0000000 .Bind (wx .EVT_CHAR ,O00000OOOO0000000 .OnChar )#line:3223
    def Clone (O0OO00OOO0OOO00OO ):#line:3226
        ""#line:3227
        return PassValidator ()#line:3228
    def Validate (O0O000000O00O0OO0 ,O00OO00OO0O00000O ):#line:3231
        return True #line:3232
    def TransferToWindow (OOOOO00OO0OOO0000 ):#line:3235
        return True #line:3236
    def TransferFromWindow (O0O00000OOO0O00O0 ):#line:3239
        return True #line:3240
    def OnChar (OO00OOOO0OO00O00O ,OOOO00O0000OOOOOO ):#line:3243
        pass #line:3244
class ConfirmLogin (wx .Frame ):#line:3258
    pass #line:3259
class TimeThread (Thread ):#line:3262
    def __init__ (O00000O0OO00O00OO ):#line:3263
        ""#line:3264
        Thread .__init__ (O00000O0OO00O00OO )#line:3265
        O00000O0OO00O00OO .setDaemon (True )#line:3266
        O00000O0OO00O00OO .start ()#line:3267
    def run (OO00O00000O0O0OOO ):#line:3269
        ""#line:3270
        global a_time #line:3272
        for O0OOO0O000O0OO00O in range (1000000 ):#line:3273
            O000O00000OO0000O =time .clock ()#line:3274
            time .sleep (0.1 )#line:3275
            OOO0OO0O0OO000O00 =time .clock ()#line:3276
            a_time +=OOO0OO0O0OO000O00 -O000O00000OO0000O #line:3277
class HashThread (Thread ):#line:3308
    def __init__ (OOOO0OOO0OOOO0O00 ):#line:3309
        ""#line:3310
        Thread .__init__ (OOOO0OOO0OOOO0O00 )#line:3311
        OOOO0OOO0OOOO0O00 .setDaemon (True )#line:3312
        OOOO0OOO0OOOO0O00 .start ()#line:3313
    def run (OOO0O0000O00O0000 ):#line:3315
        ""#line:3316
        Create_hash ()#line:3318


class findposThread (Thread ):#line:3324
    def __init__ (O0O00O00OOOOO0000 ):#line:3325
        Thread .__init__ (O0O00O00OOOOO0000 )#line:3326
        O0O00O00OOOOO0000 .setDaemon (True )#line:3327
        O0O00O00OOOOO0000 .start ()#line:3328
    def run (OOO000OOO00O00OO0 ):#line:3330
        findpos ()#line:3331
class sdfsf24324297Thread (Thread ):#line:3334
    def __init__ (O0OO00O0OO0000OO0 ):#line:3335
        Thread .__init__ (O0OO00O0OO0000OO0 )#line:3336
        O0OO00O0OO0000OO0 .setDaemon (True )#line:3337
        O0OO00O0OO0000OO0 .start ()#line:3338
    def run (O00000OOO0000OOO0 ):#line:3340
        global sdfsf24324297_need ,sdfsf24324297_on #line:3341
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3342
        for O0OOOO00O00O00000 in range (100 ):#line:3343
            wx .Sleep (0.1 )#line:3344
            if sdfsf24324297_need :#line:3346
                print ("开启查找")#line:3347
                findsdfsf24324297 ()#line:3348
                if sdfsf24324297_on :#line:3349
                    TopFrame .OnClick_sdfsf24324297 ()#line:3350
                    sdfsf24324297_need =False #line:3351
                    sdfsf24324297_on =False #line:3352
                    sdfsf24324297_one =False #line:3353
                    oo0o0O0O0O0_on =True #line:3354
        sdfsf24324297_one =False #line:3355
class uioo0o000ooThread (Thread ):#line:3357
    def __init__ (OOOO0O0OOOO0OO0O0 ):#line:3358
        Thread .__init__ (OOOO0O0OOOO0OO0O0 )#line:3359
        OOOO0O0OOOO0OO0O0 .setDaemon (True )#line:3360
        OOOO0O0OOOO0OO0O0 .start ()#line:3361
    def run (OO0O0O0O00OOO000O ):#line:3363
        global sdfsf24324297_need ,sdfsf24324297_on #line:3364
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3365
        for O0OO0O0O0O000O000 in range (50 ):#line:3366
            if uioo0o000oo_need :#line:3367
                finduioo0o000oo ()#line:3368
                if uioo0o000oo_on :#line:3369
                    TopFrame .OnClick_Shuaxin ()#line:3370
                    uioo0o000oo_on =False #line:3371
                    uioo0o000oo_need =False #line:3372
                    uioo0o000oo_one =False #line:3373
        uioo0o000oo_one =False #line:3374
class LoginThread (Thread ):#line:3379
    def __init__ (OOO00000O0O0OOOO0 ):#line:3380
        ""#line:3381
        Thread .__init__ (OOO00000O0O0OOOO0 )#line:3382
        OOO00000O0O0OOOO0 .setDaemon (True )#line:3383
        OOO00000O0O0OOOO0 .start ()#line:3384
    def run (OOO0OO0OO0OOOO0O0 ):#line:3386
        global Username ,login_result #line:3388
        login_result =ConfirmUser ()#line:3389
        print (login_result )#line:3390
        logging .info ("%s"%login_result )#line:3391
        wx .CallAfter (pub .sendMessage ,"connect")#line:3392
class controlThread (Thread ):#line:3395
    def __init__ (OOO0O00OOOO0OOOOO ):#line:3396
        ""#line:3397
        Thread .__init__ (OOO0O00OOOO0OOOOO )#line:3398
        OOO0O00OOOO0OOOOO .setDaemon (True )#line:3399
        OOO0O00OOOO0OOOOO .start ()#line:3400
    def run (OOO00OOOOO00O0O00 ):#line:3403
        wx .Sleep (10 )#line:3404
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3405
class KeepThread (Thread ):#line:3410
    def __init__ (O00OO00O0O0000O0O ):#line:3411
        ""#line:3412
        Thread .__init__ (O00OO00O0O0000O0O )#line:3413
        O00OO00O0O0000O0O .setDaemon (True )#line:3414
        O00OO00O0O0000O0O .start ()#line:3415
    def run (O000O0OO000O0000O ):#line:3418
        for O0O0OOO000OO00O00 in range (1000000 ):#line:3419
            time .sleep (90 )#line:3420
            Keeplogin ()#line:3421
class TijiaoThread (Thread ):#line:3427
    def __init__ (OOO0O00O000000OOO ):#line:3428
        ""#line:3429
        Thread .__init__ (OOO0O00O000000OOO )#line:3430
        OOO0O00O000000OOO .setDaemon (True )#line:3431
        OOO0O00O000000OOO .start ()#line:3432
    def run (OOOO0OOOOOOO000O0 ):#line:3435
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3436
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3437
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3438
        for O000000OO000OO0OO in range (10000000 ):#line:3439
            time .sleep (0.1 )#line:3440
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3444
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3446
                    oOO0O0O0O0O0O0_on =False #line:3447
                    TopFrame .OnClick_Tijiao ()#line:3448
                    oOO0O0O0O0O0O0_on =False #line:3449
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3450
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3451
                    oOO0O0O0O0O0O0_one =True #line:3452
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3453
                    oOO0O0O0O0O0O0_on =False #line:3454
                    TopFrame .OnClick_Tijiao ()#line:3455
                    oOO0O0O0O0O0O0_on =False #line:3456
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3457
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3458
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3459
                    oOO0O0O0O0O0O0_on =False #line:3460
                    oOO0O0O0O0O0O0_on =False #line:3461
                    TopFrame .OnClick_Tijiao ()#line:3462
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3463
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3464
                    oOO0O0O0O0O0O0_one =True #line:3465
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance :#line:3466
                    oOO0O0O0O0O0O0_on =False #line:3467
                    oOO0O0O0O0O0O0_on =False #line:3468
                    TopFrame .OnClick_Tijiao ()#line:3469
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3470
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3471
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3473
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time <=one_oO0O0O0O0O0O0O0O01 +0.2 :#line:3475
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3476
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3477
                    oOO0O0O0O0O0O0_on =True #line:3478
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3479
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3480
                if oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3481
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3482
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3483
                    oOO0O0O0O0O0O0_on =True #line:3484
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3485
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3486
class MoniTijiaoThread (Thread ):#line:3490
    def __init__ (O00O00OO000OO0O00 ):#line:3491
        ""#line:3492
        Thread .__init__ (O00O00OO000OO0O00 )#line:3493
        O00O00OO000OO0O00 .setDaemon (True )#line:3494
        O00O00OO000OO0O00 .start ()#line:3495
    def run (O0OO0O0O00OOO0OOO ):#line:3498
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3499
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3500
        for OO0O0OOOO0OOOOOO0 in range (10000000 ):#line:3501
            time .sleep (0.1 )#line:3502
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3504
                print (oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK )#line:3505
                print (oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ,oOO0O0O0O0O0O0_one )#line:3506
                print (O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 )#line:3507
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3508
                    TopFrame .OnClick_Tijiao ()#line:3509
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3510
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3511
                    oOO0O0O0O0O0O0_on =False #line:3512
                    oOO0O0O0O0O0O0_one =True #line:3513
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3514
                    TopFrame .OnClick_Tijiao ()#line:3515
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3516
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3517
                    oOO0O0O0O0O0O0_on =False #line:3518
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3519
                    oOO0O0O0O0O0O0_on =False #line:3520
                    TopFrame .OnClick_Tijiao ()#line:3521
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3522
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3523
                    oOO0O0O0O0O0O0_one =True #line:3524
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3525
                    oOO0O0O0O0O0O0_on =False #line:3526
                    TopFrame .OnClick_Tijiao ()#line:3527
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3528
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3529
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3534
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=OO00000o01 +0.2 :#line:3535
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3536
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3538
                    oOO0O0O0O0O0O0_on =True #line:3539
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3540
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3541
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3542
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3543
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3545
                    oOO0O0O0O0O0O0_on =True #line:3546
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3547
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3548
class Infoframe (wx .Frame ):#line:3551
    def __init__ (O0OOOO0O0OO00OOOO ,O000000O00OO00OOO ,OO0OO00O00000OOOO ,O00O0O000OOOO000O ):#line:3552
        wx .Frame .__init__ (O0OOOO0O0OO00OOOO ,None ,-1 ,O000000O00OO00OOO ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3553
        O0OOOO0O0OO00OOOO .Bind (wx .EVT_CLOSE ,O0OOOO0O0OO00OOOO .OnClose )#line:3554
        O0OOOO0O0OO00OOOO .panel =wx .Panel (O0OOOO0O0OO00OOOO ,size =(300 ,220 ))#line:3555
        O0OOOO0O0OO00OOOO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3556
        O0OOOO0O0OO00OOOO .SetIcon (O0OOOO0O0OO00OOOO .icon )#line:3557
class SketchApp (wx .App ):#line:3560
    def OnInit (O0O00OO00O00O0000 ):#line:3561
        try :#line:3572
            with open ("your.name",'rb')as OO00O0000OOOO0O0O :#line:3573
                O0OO00O00OOOOOOOO =pickle .load (OO00O0000OOOO0O0O )#line:3574
                OOO0OOOO00OO0O0OO =O0OO00O00OOOOOOOO [0 ]#line:3575
                OOO0OOO0OO0OO0O0O =O0OO00O00OOOOOOOO [1 ]#line:3576
        except :#line:3577
            OOO0OOOO00OO0O0OO ='123456'#line:3578
            OOO0OOO0OO0OO0O0O =0 #line:3579
        OO0000O0OOO0OOOOO =LoginFrame ('小鲜肉拍牌',OOO0OOOO00OO0O0OO ,OOO0OOO0OO0OO0O0O )#line:3580
        OO0000O0OOO0OOOOO .Show (True )#line:3581
        return True #line:3582
if __name__ =='__main__':#line:3585
    app =SketchApp ()#line:3586
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
