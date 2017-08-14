""#line:5
version ='1.4'#line:8
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
zxco0o0o0o0list =[80000 +O000O000000000OO0 *100 for O000O000000000OO0 in range (200 )]#line:67
IDnumber =0 #line:68
account =0 #line:69
passwd =0 #line:70
import pyautogui as pg #line:74
def Create_hash ():#line:76
    with open ('dick.dl','rb')as O0OO0O0O0O0OO0O00 :#line:77
        global dick_hash #line:78
        dick_hash =pickle .load (O0OO0O0O0O0OO0O00 )#line:79
    with open ('cf.btn','rb')as O0O0OOO0OO0000OO0 :#line:80
        global cf_hash #line:81
        cf_hash =pickle .load (O0O0OOO0OO0000OO0 )#line:82
    with open ("target.tkl",'rb')as OO0O0O0O00O000O0O :#line:84
        global dick_target #line:85
        dick_target =pickle .load (OO0O0O0O00O000O0O )#line:86
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
Oo0o0Oo0o0o0 =[[0 ,0 ]for OO00O0OOOO00OO0OO in range (len (P_relative ))]#line:138
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
py_zxco0o0o0o0frame =510 #line:153
px_timeframe =400 -35 #line:155
py_timeframe =460 #line:156
px_sdfsnisdfafzxcvframe =400 -215 #line:158
py_sdfsnisdfafzxcvframe =460 #line:159
px_mini =200 #line:163
py_mini =40 #line:164
Pricesize =[400 ,80 ]#line:166
Timesize =[200 ,50 ]#line:168
uioo0o000oo_area =[396 -80 ,11 -50 ,396 +80 ,11 +50 ]#line:171
sdfsf24324297_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:172
Px_zxco0o0o0o0 =Px +px_zxco0o0o0o0 #line:191
Py_zxco0o0o0o0 =Py +py_zxco0o0o0o0 #line:192
Pos_zxco0o0o0o0 =[Px_zxco0o0o0o0 ,Py_zxco0o0o0o0 ,Px_zxco0o0o0o0 +px_mini ,Py_zxco0o0o0o0 +py_mini ]#line:193
Px_zxco0o0o0o0frame =Px +px_zxco0o0o0o0frame #line:196
Py_zxco0o0o0o0frame =Py +py_zxco0o0o0o0frame #line:197
Pos_zxco0o0o0o0frame =[Px_zxco0o0o0o0frame ,Py_zxco0o0o0o0frame ]#line:198
Px_timeframe =px_timeframe #line:201
Py_timeframe =py_timeframe #line:202
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:203
Px_sdfsnisdfafzxcvframe =Px +px_sdfsnisdfafzxcvframe #line:206
Py_sdfsnisdfafzxcvframe =Py +py_sdfsnisdfafzxcvframe #line:207
Pos_sdfsnisdfafzxcvframe =[Px_sdfsnisdfafzxcvframe ,Py_sdfsnisdfafzxcvframe ]#line:208
px_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:216
py_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:217
Px_O0O0O0O0O0O0Ozxco0o0o0o0 =Px +px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:220
Py_O0O0O0O0O0O0Ozxco0o0o0o0 =Py +py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:221
O0O0O0O0O0O0Ozxco0o0o0o0_sizex =41 #line:222
O0O0O0O0O0O0Ozxco0o0o0o0_sizey =16 #line:223
px_relative =49 #line:225
py_relative =0 #line:226
px_sdfsf24324297 =656 #line:228
py_sdfsf24324297 =475 #line:229
Px_sdfsf24324297 =Px +px_sdfsf24324297 #line:230
Py_sdfsf24324297 =Py +py_sdfsf24324297 #line:231
sdfsf24324297_sizex =113 #line:232
sdfsf24324297_sizey =28 #line:233
sdfsf24324297_on =False #line:234
sdfsf24324297_need =False #line:235
sdfsf24324297_one =False #line:236
px_uioo0o000oo =550 #line:238
py_uioo0o000oo =413 #line:239
Px_uioo0o000oo =Px +px_uioo0o000oo #line:240
Py_uioo0o000oo =Py +py_uioo0o000oo #line:241
uioo0o000oo_sizex =108 #line:242
uioo0o000oo_sizey =21 #line:243
uioo0o000oo_on =False #line:244
uioo0o000oo_need =False #line:245
uioo0o000oo_one =False #line:246
oo0o0O0O0O0_interval =False #line:248
oOO0O0O0O0O0O0_interval =False #line:249
query_interval =False #line:250
query_on =False #line:251
import sys #line:254
if sys .platform !='win32':#line:255
    exit ()#line:256
import pyautogui as pg #line:257
import ctypes #line:258
from ctypes import wintypes #line:259
import win32con #line:260
import wx .html2 #line:261
import wx #line:262
import pickle #line:263
import wx .adv #line:264
from PIL import Image #line:265
import imagehash #line:266
import logging #line:343
timenow =time .time ()#line:344
time_local =time .localtime (timenow )#line:346
myapplog =time .strftime ("%Y%m%d%H%M%S",time_local )#line:348
print (myapplog )#line:349
logging .basicConfig (level =logging .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:354
logging .debug ('This is debug message')#line:356
logging .info ('This is info message')#line:357
logging .warning ('This is warning message')#line:358
logging .error ('This is error message')#line:359
import win32gui ,win32api #line:362
import cv2 #line:363
from PIL import ImageGrab #line:364
def Click (O0OOOO0OO00OOO000 ,OO0OOO000O00OO0OO ):#line:365
    O00OOOO0O0O0000O0 =win32gui .GetCursorPos ()#line:366
    O0OOOO0OO00OOO000 =int (O0OOOO0OO00OOO000 )#line:367
    OO0OOO000O00OO0OO =int (OO0OOO000O00OO0OO )#line:368
    win32api .SetCursorPos ((O0OOOO0OO00OOO000 ,OO0OOO000O00OO0OO ))#line:369
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,O0OOOO0OO00OOO000 ,OO0OOO000O00OO0OO ,0 ,0 )#line:370
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,O0OOOO0OO00OOO000 ,OO0OOO000O00OO0OO ,0 ,0 )#line:371
    win32api .SetCursorPos (O00OOOO0O0O0000O0 )#line:372
import win32clipboard #line:375
def Paste ():#line:376
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:378
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:379
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:380
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:381
def setText (O0000000OOO0O0000 ):#line:383
    O0000000OOO0O0000 =O0000000OOO0O0000 .encode ('utf-8')#line:384
    win32clipboard .OpenClipboard ()#line:385
    win32clipboard .EmptyClipboard ()#line:386
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,O0000000OOO0O0000 )#line:387
    win32clipboard .CloseClipboard ()#line:388
def findpos ():#line:391
    OO000O00O00OOO0OO =ImageGrab .grab ().convert ('L')#line:393
    OO00OO00OO0O0O00O =np .asarray (OO000O00O00OOO0OO )#line:394
    global dick_target #line:395
    O0OO0OOOOO0O0OOO0 =dick_target [2 ]#line:396
    OO0OO00000O00OO00 ,OOO00OO00O0OOO00O =O0OO0OOOOO0O0OOO0 .shape [::-1 ]#line:397
    O00000OOOOO0OO0OO =cv2 .matchTemplate (OO00OO00OO0O0O00O ,O0OO0OOOOO0O0OOO0 ,cv2 .TM_CCOEFF_NORMED )#line:399
    OO0O00O00O0O00O00 ,OOO0OOOOO0OO0OOOO ,OOOOOOO0O0000OOO0 ,OO00OO0000OOOOO0O =cv2 .minMaxLoc (O00000OOOOO0OO0OO )#line:400
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:405
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =OO00OO0000OOOOO0O [0 ]+px_relative #line:406
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =OO00OO0000OOOOO0O [1 ]+py_relative #line:407
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:408
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:409
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:411
    for O0OO0O000O0000O0O in range (len (Oo0o0Oo0o0o0 )):#line:412
        Oo0o0Oo0o0o0 [O0OO0O000O0000O0O ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0OO0O000O0000O0O ][0 ]#line:413
        Oo0o0Oo0o0o0 [O0OO0O000O0000O0O ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0OO0O000O0000O0O ][1 ]#line:414
    uioo0o000oo_area =[396 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:415
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:416
    global findpos_on #line:418
    findpos_on =False #line:419
def finduioo0o000oo ():#line:421
    global dick_target ,uioo0o000oo_on ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:422
    OOOOO00OOO0O00O0O =dick_target [0 ]#line:423
    O000OO0OO00O0OO00 =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:424
    OO000O000000O0O0O =np .asarray (O000OO0OO00O0OO00 )#line:425
    OO0O0O0OOO0O0OO0O ,OO0O00O0O0O00000O =OOOOO00OOO0O00O0O .shape [::-1 ]#line:426
    O0O00OOOOO0O0O0O0 =cv2 .matchTemplate (OO000O000000O0O0O ,OOOOO00OOO0O00O0O ,cv2 .TM_CCOEFF_NORMED )#line:427
    OOO00O00000OOO0O0 ,O00O000OO00OO000O ,O0O0000OOO00O00O0 ,OO000O00O0O00O0OO =cv2 .minMaxLoc (O0O00OOOOO0O0O0O0 )#line:428
    if O00O000OO00OO000O >=0.9 :#line:430
        uioo0o000oo_on =True #line:431
def findsdfsf24324297 ():#line:434
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:435
    OO000O000OOOO0000 =dick_target [1 ]#line:436
    O00O0OOO000OO00O0 =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:437
    O0000OOOO0OO0OO0O =np .asarray (O00O0OOO000OO00O0 )#line:438
    O000O00OO00O00OO0 ,O000OO0O00O00OOO0 =OO000O000OOOO0000 .shape [::-1 ]#line:439
    OO0O0OOO0000O00O0 =cv2 .matchTemplate (O0000OOOO0OO0OO0O ,OO000O000OOOO0000 ,cv2 .TM_CCOEFF_NORMED )#line:440
    OO0O0000O0000OOO0 ,OO0O0OOO0O00000OO ,O0OO0O0000O0000OO ,OO00O0O0OOOO0O00O =cv2 .minMaxLoc (OO0O0OOO0000O00O0 )#line:441
    print (OO0O0OOO0O00000OO )#line:442
    if OO0O0OOO0O00000OO >=0.9 :#line:443
        sdfsf24324297_on =True #line:444
SZ =20 #line:448
bin_n =16 #line:449
import numpy as np #line:450
def hog (OOO00OO000OOOOO00 ):#line:453
    O0OO0OO00O000O0O0 =cv2 .Sobel (OOO00OO000OOOOO00 ,cv2 .CV_32F ,1 ,0 )#line:454
    O0000O0O000OOO000 =cv2 .Sobel (OOO00OO000OOOOO00 ,cv2 .CV_32F ,0 ,1 )#line:455
    OOOO0OO0OOOOOOO0O ,OOOOOOOOOOOO0OO0O =cv2 .cartToPolar (O0OO0OO00O000O0O0 ,O0000O0O000OOO000 )#line:456
    OO000OO0OOOO0OOOO =np .int32 (bin_n *OOOOOOOOOOOO0OO0O /(2 *np .pi ))#line:457
    OOOOO0000000O00OO =OO000OO0OOOO0OOOO [:10 ,:10 ],OO000OO0OOOO0OOOO [10 :,:10 ],OO000OO0OOOO0OOOO [:10 ,10 :],OO000OO0OOOO0OOOO [10 :,10 :]#line:458
    O00O0000O0000O0OO =OOOO0OO0OOOOOOO0O [:10 ,:10 ],OOOO0OO0OOOOOOO0O [10 :,:10 ],OOOO0OO0OOOOOOO0O [:10 ,10 :],OOOO0OO0OOOOOOO0O [10 :,10 :]#line:459
    O0O00O00OO000O0OO =[np .bincount (OOOO0OOO000OOOOOO .ravel (),OO0OOO0000O0OO000 .ravel (),bin_n )for OOOO0OOO000OOOOOO ,OO0OOO0000O0OO000 in zip (OOOOO0000000O00OO ,O00O0000O0000O0OO )]#line:460
    OOOOO0O0O00O0OOOO =np .hstack (O0O00O00OO000O0OO )#line:461
    return OOOOO0O0O00O0OOOO #line:462
def cut (O0O0000O0O0000O00 ):#line:466
    OOOO000OO0O000000 ,OOO00OOO0O0O0OO0O =cv2 .threshold (O0O0000O0O0000O00 ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:467
    O000O0000O0OO0OOO ,OO000000OO0OOOOO0 ,O00O0O00OO0O0OOO0 =cv2 .findContours (OOO00OOO0O0O0OO0O ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:469
    O0O0O0000OOOO0OOO =[]#line:470
    O0O000OO0O0OOO0OO =[]#line:471
    for OOOOOO000O0O000OO in range (len (OO000000OO0OOOOO0 )):#line:472
        OO0000OOO00O0O0O0 =OO000000OO0OOOOO0 [OOOOOO000O0O000OO ]#line:473
        OOOOOOO0000OO00OO ,O0OO000OOO000O00O ,OOO00OOOO00OO0000 ,OO0OOOO0OOOOO0O00 =cv2 .boundingRect (OO0000OOO00O0O0O0 )#line:474
        O0O000OO0O0OOO0OO .append ([OOOOOOO0000OO00OO ,O0OO000OOO000O00O ,OOO00OOOO00OO0000 ,OO0OOOO0OOOOO0O00 ])#line:476
    O0O000OO0O0OOO0OO =sorted (O0O000OO0O0OOO0OO )#line:478
    for OOOOOO000O0O000OO in range (len (OO000000OO0OOOOO0 )):#line:479
        OOOOOOO0000OO00OO ,O0OO000OOO000O00O ,OOO00OOOO00OO0000 ,OO0OOOO0OOOOO0O00 =O0O000OO0O0OOO0OO [OOOOOO000O0O000OO ]#line:480
        O0O0O0000OOOO0OOO .append (O000O0000O0OO0OOO [O0OO000OOO000O00O :O0OO000OOO000O00O +OO0OOOO0OOOOO0O00 ,OOOOOOO0000OO00OO :OOOOOOO0000OO00OO +OOO00OOOO00OO0000 ])#line:481
    return O0O0O0000OOOO0OOO #line:482
def readpic (OOO0O0O0O00OOO000 ):#line:484
    try :#line:485
        OOO0OO000OOOO0000 =cv2 .ml .SVM_load ('maindata.xml')#line:486
        OO00OOO00OO0O00OO =cut (OOO0O0O0O00OOO000 )#line:487
        OO00OOO00OO0O00OO =list (map (hog ,OO00OOO00OO0O00OO ))#line:488
        OO00OOO00OO0O00OO =np .float32 (OO00OOO00OO0O00OO ).reshape (-1 ,64 )#line:489
        OO00O00OO0O000000 =OOO0OO000OOOO0000 .predict (OO00OOO00OO0O00OO )#line:490
        OO00O00OO0O000000 =OO00O00OO0O000000 [1 ].reshape (-1 ).astype (int ).astype (str )#line:491
        O0OO0OOO00O00O00O ="".join (list (OO00O00OO0O000000 ))#line:492
        return O0OO0OOO00O00O00O #line:493
    except :#line:494
        return False #line:495
import smtplib #line:513
from email .mime .text import MIMEText #line:516
import os #line:517
import mimetypes #line:518
import email #line:519
from email .mime .multipart import MIMEMultipart #line:520
from threading import Thread #line:523
import threading #line:524
from wx .lib .pubsub import pub #line:525
import socket ,sys ,json #line:530
timeout =10 #line:531
socket .setdefaulttimeout (timeout )#line:532
def ConfirmUser ():#line:534
    O000OOOOO0O00O000 =host_ali #line:535
    O00O0O0000OO0OO00 =8080 #line:538
    OO0O00000OO000000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:540
    try :#line:542
        OO0O00000OO000000 .connect ((O000OOOOO0O00O000 ,O00O0O0000OO0OO00 ))#line:543
    except socket .gaierror as O0O0O0OOOOO0O0000 :#line:544
        logging .error ('连接失败 %s'%O0O0O0OOOOO0O0000 )#line:545
        logging .error ("Address-related error connecting to server: %s"%O0O0O0OOOOO0O0000 )#line:546
        return 'net error'#line:547
    except socket .error as O0O0O0OOOOO0O0000 :#line:549
        logging .error ('连接失败 %s'%O0O0O0OOOOO0O0000 )#line:550
        logging .error ("Connection error: %s"%O0O0O0OOOOO0O0000 )#line:551
        return 'net error'#line:552
    O00OOO0000O00O0OO =['login',Username ,Password ]#line:556
    O00OOO0000O00O0OO =json .dumps (O00OOO0000O00O0OO )#line:557
    O00OOO0000O00O0OO =bytes (O00OOO0000O00O0OO ,encoding ="utf-8")#line:558
    logging .info ('发送信息 %s'%str (O00OOO0000O00O0OO ,encoding ="utf-8"))#line:559
    OO0O00000OO000000 .send (O00OOO0000O00O0OO )#line:560
    OO0O00000OO000000 .shutdown (1 )#line:562
    logging .info ("Submit Complete")#line:563
    print ("Submit Complete")#line:564
    try :#line:565
        O0000OOOOO00O0OOO =OO0O00000OO000000 .recv (1024 )#line:567
        print (O0000OOOOO00O0OOO )#line:568
        O0000OOOOO00O0OOO =str (O0000OOOOO00O0OOO ,encoding ="utf-8")#line:569
        O0000OOOOO00O0OOO =json .loads (O0000OOOOO00O0OOO )#line:570
        print (O0000OOOOO00O0OOO )#line:571
        OOOO00OO0000O0O0O =O0000OOOOO00O0OOO [0 ]#line:572
        if OOOO00OO0000O0O0O =='success':#line:573
            logging .info ('登录成功 %s'%OOOO00OO0000O0O0O )#line:574
            global url2 #line:575
            url2 =O0000OOOOO00O0OOO [1 ]#line:576
            return 'login success'#line:577
        elif OOOO00OO0000O0O0O =='wrong password':#line:578
            logging .warning ('密码错误 %s'%OOOO00OO0000O0O0O )#line:579
            return 'wrong password'#line:580
        elif OOOO00OO0000O0O0O =="wrong account":#line:581
            logging .warning ('账号错误 %s'%OOOO00OO0000O0O0O )#line:582
            return 'wrong account'#line:583
        elif OOOO00OO0000O0O0O =='repeat':#line:584
            logging .warning ('账号错误 %s'%OOOO00OO0000O0O0O )#line:585
            return 'repeat'#line:586
    except :#line:587
        print ("连接失败")#line:588
        logging .warning ('连接失败 ')#line:589
        return False #line:590
def Logout ():#line:593
    O00OO0OO00OO000O0 =host_ali #line:594
    O00OO00O00OO0000O =8080 #line:597
    global Username #line:598
    OOO0O0O0OO0OOOOOO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:599
    try :#line:600
        OOO0O0O0OO0OOOOOO .connect ((O00OO0OO00OO000O0 ,O00OO00O00OO0000O ))#line:601
    except socket .gaierror as O0OOO0O0OOO0OOO0O :#line:602
        print ("Address-related error connecting to server: %s"%O0OOO0O0OOO0OOO0O )#line:603
        logging .info ("Address-related error connecting to server: %s"%O0OOO0O0OOO0OOO0O )#line:604
    except socket .error as O0OOO0O0OOO0OOO0O :#line:606
        print ("Connection error: %s"%O0OOO0O0OOO0OOO0O )#line:607
        logging .info ("Connection error: %s"%O0OOO0O0OOO0OOO0O )#line:608
    O00O000OO00OO0000 =['logout',Username ,Password ]#line:612
    O00O000OO00OO0000 =json .dumps (O00O000OO00OO0000 )#line:613
    O00O000OO00OO0000 =bytes (O00O000OO00OO0000 ,encoding ="utf-8")#line:614
    logging .info ('发送信息 %s'%str (O00O000OO00OO0000 ,encoding ="utf-8"))#line:615
    OOO0O0O0OO0OOOOOO .send (O00O000OO00OO0000 )#line:616
    OOO0O0O0OO0OOOOOO .shutdown (1 )#line:617
    print ("Submit Log Out Complete")#line:618
    logging .info ("Submit Log Out Complete")#line:619
def Keeplogin ():#line:622
    O0O000O0O00OOOOO0 =host_ali #line:623
    O0O0O00OO0OO0OOOO =8080 #line:626
    global Username #line:627
    O00OO000OOOOO0O0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:628
    try :#line:629
        O00OO000OOOOO0O0O .connect ((O0O000O0O00OOOOO0 ,O0O0O00OO0OO0OOOO ))#line:630
    except socket .gaierror as O0OOO0OOO0O000O00 :#line:631
        print ("Address-related error connecting to server: %s"%O0OOO0OOO0O000O00 )#line:632
        logging .info ("Address-related error connecting to server: %s"%O0OOO0OOO0O000O00 )#line:633
    except socket .error as O0OOO0OOO0O000O00 :#line:635
        print ("Connection error: %s"%O0OOO0OOO0O000O00 )#line:636
        logging .info ("Connection error: %s"%O0OOO0OOO0O000O00 )#line:637
    O000O000O0O00OO00 =['keep',Username ,Password ]#line:641
    O000O000O0O00OO00 =json .dumps (O000O000O0O00OO00 )#line:642
    O000O000O0O00OO00 =bytes (O000O000O0O00OO00 ,encoding ="utf-8")#line:643
    logging .info ('发送信息 %s'%str (O000O000O0O00OO00 ,encoding ="utf-8"))#line:644
    O00OO000OOOOO0O0O .send (O000O000O0O00OO00 )#line:645
    O00OO000OOOOO0O0O .shutdown (1 )#line:647
    print ("Submit keep Complete")#line:648
    logging .info ("Submit keep Complete")#line:649
def send_mail (OO0OO0OO0000OO0OO ,OOO0OO00O0O00OOO0 ,OOOOOOO000OOO00OO ):#line:652
    OOO00OOO00000OO0O =open (OOOOOOO000OOO00OO ,'rb')#line:653
    O0OOO00OOOO0000O0 ,O0000O0OO00OOOOOO =mimetypes .guess_type (OOOOOOO000OOO00OO )#line:654
    if O0OOO00OOOO0000O0 is None and O0000O0OO00OOOOOO is None :#line:655
        O0OOO00OOOO0000O0 ='application/octet-stream'#line:656
    OOOOO0000OO0OO0OO ,OO0O0000O0OOO00O0 =O0OOO00OOOO0000O0 .split ('/',1 )#line:657
    O0O00O0O000OO0O00 =email .mime .base .MIMEBase (OOOOO0000OO0OO0OO ,OO0O0000O0OOO00O0 )#line:658
    O0O00O0O000OO0O00 .set_payload (OOO00OOO00000OO0O .read ())#line:659
    OOO00OOO00000OO0O .close ()#line:660
    email .encoders .encode_base64 (O0O00O0O000OO0O00 )#line:661
    OOOOOOO0O0OO0O0O0 =os .path .basename (OOOOOOO000OOO00OO )#line:662
    O0O00O0O000OO0O00 .add_header ('Content-Disposition','attachment',filename =OOOOOOO0O0OO0O0O0 )#line:663
    OOO0OO00O0O00OOO0 =OOO0OO00O0O00OOO0 #line:664
    O0O000O0O0OOOOOOO ='smtp.qq.com'#line:665
    OOOO0OO0O0O0OOO00 =os .environ .get ('MAIL_USERNAME')#line:666
    OOO0O0000000O0000 =os .environ .get ('MAIL_PASSWORD')#line:667
    O0000O00O0OO0O0OO =OOOO0OO0O0O0OOO00 #line:668
    O0O0OO0O000000000 =MIMEMultipart ()#line:669
    O0O0OO0O000000000 .attach (O0O00O0O000OO0O00 )#line:670
    O0O0OO0O000000000 ['Subject']=OO0OO0OO0000OO0OO #line:671
    O0O0OO0O000000000 ['From']=O0000O00O0OO0O0OO #line:672
    O0O0OO0O000000000 ['To']=";".join (OOO0OO00O0O00OOO0 )#line:673
    OOOOOOO0O0OOOO000 =smtplib .SMTP_SSL (O0O000O0O0OOOOOOO ,465 )#line:674
    OOOOOOO0O0OOOO000 .login (OOOO0OO0O0O0OOO00 ,OOO0O0000000O0000 )#line:675
    print ('login in  successfully')#line:676
    OOOOOOO0O0OOOO000 .sendmail (O0000O00O0OO0O0OO ,OOO0OO00O0O00OOO0 ,O0O0OO0O000000000 .as_string ())#line:677
    OOOOOOO0O0OOOO000 .quit ()#line:678
    print ('send email  successfully')#line:679
def Upload ():#line:681
    pass #line:682
def Com_read ():#line:685
    pass #line:686
def Com_decision ():#line:690
    pass #line:691
class TopFrame (wx .Frame ):#line:724
    def __init__ (O0O000OO000000O0O ,OO0OO0OOO000O00O0 ,O0OOOO00OO0O00OO0 ):#line:725
        wx .Frame .__init__ (O0O000OO000000O0O ,None ,-1 ,OO0OO0OOO000O00O0 ,size =(520 ,320 ))#line:727
        O0O000OO000000O0O .Bind (wx .EVT_CLOSE ,O0O000OO000000O0O .OnClose )#line:728
        OO00OOO00OO0OOOOO =time .time ()#line:732
        O0O000OO000000O0O .statusbar =O0O000OO000000O0O .CreateStatusBar ()#line:736
        O0O000OO000000O0O .statusbar .SetFieldsCount (3 )#line:738
        O0O000OO000000O0O .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:739
        O0O000OO000000O0O .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:741
        O0O000OO000000O0O .SetIcon (O0O000OO000000O0O .icon )#line:742
        O0O000OO000000O0O .statusbar .SetStatusText (u"版本号",0 )#line:744
        O0O000OO000000O0O .statusbar .SetStatusText (u"%s"%O0OOOO00OO0O00OO0 ,1 )#line:747
        O0O000OO000000O0O .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:750
        O0O000OO000000O0O .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:751
        OOO000OOO0OOO0OOO =wx .Panel (O0O000OO000000O0O ,-1 )#line:753
        OOO000OOO0OOO0OOO .SetBackgroundColour ((240 ,255 ,255 ))#line:755
        O0O000OO000000O0O .SetBackgroundColour ((240 ,255 ,255 ))#line:756
        O0O000OO000000O0O .thread =TimeThread ()#line:784
        O0O000OO000000O0O .keepthread =KeepThread ()#line:785
        O0O000OO000000O0O .button5 =wx .Button (OOO000OOO0OOO0OOO ,label ='打开模拟',pos =(190 ,190 ))#line:813
        O0O000OO000000O0O .Bind (wx .EVT_BUTTON ,O0O000OO000000O0O .Openo0sdofsfo0sodf0so0 ,O0O000OO000000O0O .button5 )#line:814
        O0O000OO000000O0O .button6 =wx .Button (OOO000OOO0OOO0OOO ,label ='打开国拍',pos =(280 ,190 ))#line:816
        O0O000OO000000O0O .Bind (wx .EVT_BUTTON ,O0O000OO000000O0O .OpenGuopai ,O0O000OO000000O0O .button6 )#line:817
        O0O000OO000000O0O .button16 =wx .Button (OOO000OOO0OOO0OOO ,label ='修改国拍网址',pos =(370 ,190 ))#line:819
        O0O000OO000000O0O .Bind (wx .EVT_BUTTON ,O0O000OO000000O0O .UrlGuopai ,O0O000OO000000O0O .button16 )#line:820
        O0O000OO000000O0O .urlText =wx .TextCtrl (OOO000OOO0OOO0OOO ,-1 ,pos =(370 ,230 ),size =(120 ,25 ))#line:821
        O0O000OO000000O0O .button7 =wx .Button (OOO000OOO0OOO0OOO ,label ='显示帮助',pos =(10 ,190 ))#line:823
        O0O000OO000000O0O .Bind (wx .EVT_BUTTON ,O0O000OO000000O0O .Help ,O0O000OO000000O0O .button7 )#line:824
        O0O000OO000000O0O .button8 =wx .Button (OOO000OOO0OOO0OOO ,label ='验证码练习',pos =(100 ,190 ))#line:826
        O0O000OO000000O0O .Bind (wx .EVT_BUTTON ,O0O000OO000000O0O .Yan_practice ,O0O000OO000000O0O .button8 )#line:827
        O0O000OO000000O0O .timer1 =wx .Timer (O0O000OO000000O0O )#line:862
        O0O000OO000000O0O .Bind (wx .EVT_TIMER ,O0O000OO000000O0O .Price_view ,O0O000OO000000O0O .timer1 )#line:863
        O0O000OO000000O0O .timer1 .Start (500 )#line:864
        O0O000OO000000O0O .timer2 =wx .Timer (O0O000OO000000O0O )#line:867
        O0O000OO000000O0O .Bind (wx .EVT_TIMER ,O0O000OO000000O0O .MainControl ,O0O000OO000000O0O .timer2 )#line:868
        O0O000OO000000O0O .timer2 .Start (100 )#line:869
        O0O000OO000000O0O .timer3 =wx .Timer (O0O000OO000000O0O )#line:877
        O0O000OO000000O0O .Bind (wx .EVT_TIMER ,O0O000OO000000O0O .Lowest_zxco0o0o0o0 ,O0O000OO000000O0O .timer3 )#line:878
        O0O000OO000000O0O .timer3 .Start (100 )#line:879
        O0O000OO000000O0O .timer4 =wx .Timer (O0O000OO000000O0O )#line:881
        O0O000OO000000O0O .Bind (wx .EVT_TIMER ,O0O000OO000000O0O .Find_pos ,O0O000OO000000O0O .timer4 )#line:882
        O0O000OO000000O0O .timer4 .Start (150 )#line:883
        O0O000OO000000O0O .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:886
        O0O000OO000000O0O .O0O0O0O0O0O0Oframe .Show (False )#line:887
        O0O000OO000000O0O .operationframe =OperationFrame ()#line:894
        O0O000OO000000O0O .operationframe .Show (False )#line:895
    def Lowest_zxco0o0o0o0 (O0O0O00O0O0OOOOO0 ,O000O0OO0OOOOO000 ):#line:905
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on #line:906
        if not findpos_on :#line:907
            OO0OO00OO0000OO00 =int (TopFrame .Price_read ())#line:908
            if OO0OO00OO0000OO00 in zxco0o0o0o0list :#line:910
                O0O0O0O0O0O0O_zxco0o0o0o0 =OO0OO00OO0000OO00 #line:911
            else :#line:912
                findpos_on =True #line:913
    def Find_pos (O00OOOO0OOOO0000O ,OOOOO0O0O0O0OO000 ):#line:930
        global findpos_on #line:931
        if findpos_on :#line:932
            findpos ()#line:933
    @staticmethod #line:939
    def Confirm ():#line:940
        global cf_hash ,sdfsf24324297_on #line:941
        OOOO00000O00O0O0O =TopFrame .Confirm_hash ()#line:942
        if OOOO00000O00O0O0O ==cf_hash [0 ]:#line:943
            sdfsf24324297_on =True #line:944
    @staticmethod #line:945
    def Refresh ():#line:946
        O0OOO000O000OO000 =TopFrame .Refresh_hash ()#line:947
        global cf_hash ,uioo0o000oo_on #line:948
        if O0OOO000O000OO000 ==cf_hash [1 ]:#line:949
            uioo0o000oo_on =True #line:950
    @staticmethod #line:959
    def Price_read ():#line:960
        OO0OO00O00OOO0O00 =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:962
        OO0OO00O00OOO0O00 =np .asarray (OO0OO00O00OOO0O00 )#line:968
        OOOOO00OOO0OOOOOO =readpic (OO0OO00O00OOO0O00 )#line:969
        return OOOOO00OOO0OOOOOO #line:971
    @staticmethod #line:974
    def Price_hash ():#line:975
        OO00OO000OOOO0O00 =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:977
        global num #line:978
        num +=1 #line:979
        O0OOOO000000OO0OO =imagehash .dhash (OO00OO000OOOO0O00 )#line:981
        return O0OOOO000000OO0OO #line:984
    @staticmethod #line:986
    def Confirm_hash ():#line:987
        O00O000OOO000O0O0 =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:989
        O00O00OOO0OO0OOO0 =imagehash .dhash (O00O000OOO000O0O0 )#line:992
        return O00O00OOO0OO0OOO0 #line:993
    @staticmethod #line:995
    def Refresh_hash ():#line:996
        OO0O00OOO0O000OOO =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:998
        OOOOOOOO00OO0O0OO =imagehash .dhash (OO0O00OOO0O000OOO )#line:1000
        return OOOOOOOO00OO0O0OO #line:1001
    def OnEraseBackground (OO0OO000000O0OO00 ,OO0OOOO0OOOOO000O ):#line:1005
        ""#line:1008
        OOOOOO0OO00OOO000 =OO0OOOO0OOOOO000O .GetDC ()#line:1009
        if not OOOOOO0OO00OOO000 :#line:1010
            OOOOOO0OO00OOO000 =wx .ClientDC (OO0OO000000O0OO00 )#line:1011
            OO000000O0O000000 =OO0OO000000O0OO00 .GetUpdateRegion ().GetBox ()#line:1012
            OOOOOO0OO00OOO000 .SetClippingRect (OO000000O0O000000 )#line:1013
        OOOOOO0OO00OOO000 .Clear ()#line:1014
        OOO000O0O0O00000O =wx .Bitmap ("blue.jpg")#line:1015
        OOOOOO0OO00OOO000 .DrawBitmap (OOO000O0O0O00000O ,0 ,0 )#line:1016
    def OnClose (OO00OOOOOOOO0OO0O ,O00OO0OOO0OO0000O ):#line:1020
        OOO0OOO0O00O0OOO0 =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1021
        if OOO0OOO0O00O0OOO0 ==wx .OK :#line:1022
            import sys as OOOOO00000000OO00 #line:1024
            OO00OOOOOOOO0OO0O .Show (False )#line:1029
            try :#line:1031
                OO00OOOOOOOO0OO0O .Close_time1 (O00OO0OOO0OO0000O )#line:1032
                OO00OOOOOOOO0OO0O .Close_time2 (O00OO0OOO0OO0000O )#line:1033
            except :#line:1034
                pass #line:1035
            Logout ()#line:1037
            wx .GetApp ().ExitMainLoop ()#line:1038
            O00OO0OOO0OO0000O .Skip ()#line:1039
            OOOOO00000000OO00 .exit (None )#line:1040
    def OnOpenAssist (O0O0OO00000O0OOOO ):#line:1044
        O0O0OO00000O0OOOO .Open ()#line:1045
        global do #line:1046
        if do :#line:1047
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1048
        else :#line:1049
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1050
        O0O0OO00000O0OOOO .Listen ()#line:1051
    @classmethod #line:1053
    def OnCloseAssist (O0O00O00OO00O00O0 ):#line:1054
        O0O00O00OO00O00O0 .Close ()#line:1055
    def OnViewPos (OOOO00000O0OO0OO0 ,OOO0O00000O00OOOO ):#line:1062
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1063
        OOOO00000O0OO0OO0 .MovePos (OOO0O00000O00OOOO )#line:1064
        global view #line:1065
        if not view :#line:1066
            view =True #line:1067
            for O000OO0O0O0O0O00O in range (len (Oo0o0Oo0o0o0 )):#line:1068
                OOOO00000O0OO0OO0 .posframe [O000OO0O0O0O0O00O ].Show (view )#line:1069
        else :#line:1070
            view =False #line:1071
            for O000OO0O0O0O0O00O in range (len (Oo0o0Oo0o0o0 )):#line:1072
                OOOO00000O0OO0OO0 .posframe [O000OO0O0O0O0O00O ].Hide ()#line:1073
    def OnSavePos (O00O0O00O0000OO00 ,OO0O000O00OOOOOO0 ):#line:1076
        O00O0O00O0000OO00 .MovePos (OO0O000O00OOOOOO0 )#line:1077
        O00O0O00O0000OO00 .Save_log ()#line:1078
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1079
    def MovePos (OOO0O0O0O0O00O0OO ,OO0OOO0OO0OO00000 ):#line:1085
        global Positon #line:1086
        for OOO00O0O0O00OO0OO in range (5 ):#line:1087
            OOOO0O00OOO00OOOO ,O00O00OOO00000O0O =Oo0o0Oo0o0o0 [OOO00O0O0O00OO0OO ]#line:1088
            OOO0O0O0O0O00O0OO .posframe [OOO00O0O0O00OO0OO ].Move (OOOO0O00OOO00OOOO -10 ,O00O00OOO00000O0O -5 )#line:1089
    def Openo0sdofsfo0sodf0so0 (OOO0O00000O0OOO0O ,OO0OOO0O0OOOOO0OO ):#line:1091
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1093
        ghjo0o0o0o0_on =True #line:1094
        O0O000O0O0000O0OO =True #line:1095
        oo0o0O0O0O0_on =True #line:1096
        oOO0O0O0O0O0O0_on =False #line:1097
        oOO0O0O0O0O0O0_num =1 #line:1098
        oOO0O0O0O0O0O0_OK =False #line:1099
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,ooweo0o0werwr_on ,o0sdofsfo0sodf0so0_on ,ghjo0o0o0o0_repeat #line:1100
        if ooweo0o0werwr_on :#line:1101
            wx .MessageBox ('请关闭国拍页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1102
        elif o0sdofsfo0sodf0so0_on :#line:1103
            wx .MessageBox ('请关闭模拟页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1104
        else :#line:1105
            OOO0O00000O0OOO0O .Open ()#line:1110
            if do :#line:1111
                o0sdofsfo0sodf0so0_on =True #line:1112
                ad_view =True #line:1113
                web_on =True #line:1114
                OOO0O00000O0OOO0O .fr =WebFrame (Px ,Py ,False ,'沪牌模拟')#line:1115
                OOO0O00000O0OOO0O .operationframe .Show (True )#line:1116
                if time_on :#line:1118
                    OOO0O00000O0OOO0O .operationframe .Opentime ()#line:1119
                if not ghjo0o0o0o0_repeat :#line:1120
                    OOO0O00000O0OOO0O .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1121
                    OOO0O00000O0OOO0O .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1122
                    ghjo0o0o0o0_repeat =True #line:1123
                O0O00O0OOO00OO00O =wx .html2 .WebView .New (OOO0O00000O0OOO0O .fr ,size =(websize [0 ],websize [1 ]),pos =(0 ,0 ))#line:1126
                O0O00O0OOO00OO00O .LoadURL (url1 )#line:1127
                O0O00O0OOO00OO00O .CanSetZoomType (False )#line:1128
                OOO0O00000O0OOO0O .fr .Show ()#line:1129
            else :#line:1133
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1134
                OOO0O00000O0OOO0O .Close ()#line:1135
            OOO0O00000O0OOO0O .Listen ()#line:1136
    def OpenGuopai (O0O000000OOOOO0O0 ,OO0000OO00OO0O00O ):#line:1186
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1188
        ghjo0o0o0o0_on =True #line:1189
        OOOO0O000000O00O0 =True #line:1190
        oo0o0O0O0O0_on =True #line:1191
        oOO0O0O0O0O0O0_on =False #line:1192
        oOO0O0O0O0O0O0_num =1 #line:1193
        oOO0O0O0O0O0O0_OK =False #line:1194
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1195
        if o0sdofsfo0sodf0so0_on :#line:1196
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1197
        elif ooweo0o0werwr_on :#line:1198
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1199
        else :#line:1200
            O0O000000OOOOO0O0 .Open ()#line:1202
            if do :#line:1206
                ad_view =True #line:1207
                ooweo0o0werwr_on =True #line:1208
                O0O000000OOOOO0O0 .fr =WebFrame (Px ,Py ,False ,'国拍网')#line:1209
                O0O000000OOOOO0O0 .operationframe .Show (True )#line:1210
                if time_on :#line:1212
                    O0O000000OOOOO0O0 .operationframe .Opentime ()#line:1213
                if not ghjo0o0o0o0_repeat :#line:1214
                    O0O000000OOOOO0O0 .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1215
                    O0O000000OOOOO0O0 .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1216
                    ghjo0o0o0o0_repeat =True #line:1217
                O00OO0O00OOOO0OO0 =wx .html2 .WebView .New (O0O000000OOOOO0O0 .fr ,size =(websize [0 ],websize [1 ]))#line:1219
                O00OO0O00OOOO0OO0 .LoadURL (url2 )#line:1220
                O00OO0O00OOOO0OO0 .CanSetZoomType (False )#line:1221
                O0O000000OOOOO0O0 .fr .Show ()#line:1222
            else :#line:1226
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1227
                O0O000000OOOOO0O0 .Close ()#line:1228
            O0O000000OOOOO0O0 .Listen ()#line:1229
    def UrlGuopai (OOOOO00OO0O0O0OOO ,O00O00O0O0OO0O000 ):#line:1231
        global url2 #line:1232
        try :#line:1233
            url2 =OOOOO00OO0O0O0OOO .urlText .GetValue ()#line:1234
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1235
        except :#line:1236
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1237
    def Help (OOOOO000OO00000O0 ,OO0O0OO000000O0O0 ):#line:1240
        OO0O00OOOO00OOO00 ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1246
        O00O000OOOOO000OO =wx .adv .AboutDialogInfo ()#line:1249
        O00O000OOOOO000OO .SetName ("沪牌第一枪")#line:1250
        O00O000OOOOO000OO .SetVersion (OO0O00OOOO00OOO00 )#line:1251
        O00O000OOOOO000OO .AddDeveloper ("ZS")#line:1255
        wx .adv .AboutBox (O00O000OOOOO000OO )#line:1256
    def Yan_practice (OOOOOO00OOOOOOO0O ,OO00O0000O0O0O0OO ):#line:1258
        pass #line:1259
    def Time_adjust (O0O00OO000O0OOO00 ,O00000OO0O0OO0OOO ):#line:1261
        pass #line:1262
    @staticmethod #line:1272
    def OnJiajia ():#line:1273
        O0OO000O0OO0O000O =pg .position ()#line:1274
        Oo0o0Oo0o0o0 [0 ][0 ]=O0OO000O0OO0O000O [0 ]#line:1275
        Oo0o0Oo0o0o0 [0 ][1 ]=O0OO000O0OO0O000O [1 ]#line:1276
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1277
        findpos ()#line:1278
    @staticmethod #line:1281
    def OnChujia ():#line:1282
        O0O00OO00O0OOOO00 =pg .position ()#line:1283
        Oo0o0Oo0o0o0 [1 ][0 ]=O0O00OO00O0OOOO00 [0 ]#line:1284
        Oo0o0Oo0o0o0 [1 ][1 ]=O0O00OO00O0OOOO00 [1 ]#line:1285
    @staticmethod #line:1286
    def OnTijiao ():#line:1287
        OO0OOOO0OO000OOO0 =pg .position ()#line:1288
        Oo0o0Oo0o0o0 [2 ][0 ]=OO0OOOO0OO000OOO0 [0 ]#line:1289
        Oo0o0Oo0o0o0 [2 ][1 ]=OO0OOOO0OO000OOO0 [1 ]#line:1290
    @staticmethod #line:1291
    def OnShuaxin ():#line:1292
        OO0OOO000OOOOO000 =pg .position ()#line:1293
        Oo0o0Oo0o0o0 [3 ][0 ]=OO0OOO000OOOOO000 [0 ]#line:1294
        Oo0o0Oo0o0o0 [3 ][1 ]=OO0OOO000OOOOO000 [1 ]#line:1295
    @staticmethod #line:1296
    def OnConfirm ():#line:1297
        O0O0OO000O0OO0OOO =pg .position ()#line:1298
        Oo0o0Oo0o0o0 [4 ][0 ]=O0O0OO000O0OO0OOO [0 ]#line:1299
        Oo0o0Oo0o0o0 [4 ][1 ]=O0O0OO000O0OO0OOO [1 ]#line:1300
    @staticmethod #line:1301
    def OnYanzhengma ():#line:1302
        O00OO0OOO00O0O0O0 =pg .position ()#line:1303
        Oo0o0Oo0o0o0 [5 ][0 ]=O00OO0OOO00O0O0O0 [0 ]#line:1304
        Oo0o0Oo0o0o0 [5 ][1 ]=O00OO0OOO00O0O0O0 [1 ]#line:1305
    @staticmethod #line:1308
    def handle_Jiajia ():#line:1309
        TopFrame .OnJiajia ()#line:1310
    @staticmethod #line:1311
    def handle_Chujia ():#line:1312
        TopFrame .OnChujia ()#line:1313
    @staticmethod #line:1314
    def handle_Tijiao ():#line:1315
        TopFrame .OnTijiao ()#line:1316
    @staticmethod #line:1317
    def handle_Shuaxin ():#line:1318
        TopFrame .OnShuaxin ()#line:1319
    @staticmethod #line:1320
    def handle_Confirm ():#line:1321
        TopFrame .OnConfirm ()#line:1322
    @staticmethod #line:1323
    def handle_Yanzhengma ():#line:1324
        TopFrame .OnYanzhengma ()#line:1325
    @classmethod #line:1332
    def OnClick_Tijiao (OOO0O00OO00000O00 ):#line:1333
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1334
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1335
        sdfsf24324297_need =True #line:1336
        if oOO0O0O0O0O0O0_num ==1 :#line:1338
            O0OOOOO00OO00OOOO =threading .Timer (one_delay ,OOO0O00OO00000O00 .Tijiao )#line:1339
            O0OOOOO00OO00OOOO .start ()#line:1340
            oOO0O0O0O0O0O0_on =False #line:1341
            if twice :#line:1342
                print ("修改为2")#line:1343
                oOO0O0O0O0O0O0_num =2 #line:1344
            print ("成功提交")#line:1346
        elif oOO0O0O0O0O0O0_num ==2 :#line:1347
            oOO0O0O0O0O0O0_num =0 #line:1348
            O0OOOOO00OO00OOOO =threading .Timer (ooo0O0o0oO0O_delay ,OOO0O00OO00000O00 .Tijiao )#line:1349
            O0OOOOO00OO00OOOO .start ()#line:1350
            oOO0O0O0O0O0O0_on =False #line:1351
        else :#line:1353
            OOO0O00OO00000O00 .Tijiao ()#line:1354
    @staticmethod #line:1356
    def Tijiao ():#line:1357
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1358
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1359
        oOO0O0O0O0O0O0_OK =False #line:1360
        global sdfsf24324297_one #line:1361
        if not sdfsf24324297_one :#line:1362
            O00000OOO0O0OO0OO =sdfsf24324297Thread ()#line:1363
            sdfsf24324297_one =False #line:1364
    @staticmethod #line:1371
    def OnClick_Shuaxin ():#line:1372
        global web_on #line:1373
        Click (Oo0o0Oo0o0o0 [3 ][0 ],Oo0o0Oo0o0o0 [3 ][1 ])#line:1374
        Click (Oo0o0Oo0o0o0 [5 ][0 ],Oo0o0Oo0o0o0 [5 ][1 ])#line:1375
    @staticmethod #line:1377
    def OnClick_sdfsf24324297 ():#line:1378
        print (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1379
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1380
    @staticmethod #line:1382
    def OnClick_oo0o0O0O0O0 ():#line:1383
        global zxco0o0o0o0_view ,zxco0o0o0o0_count ,web_on ,O0O0O0O0O0O0O_zxco0o0o0o0 #line:1384
        global oOO0O0O0O0O0O0_num ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:1385
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on #line:1386
        global uioo0o000oo_need ,uioo0o000oo_one ,oo0o0O0O0O0_interval #line:1387
        print (oo0o0O0O0O0_interval )#line:1388
        if not oo0o0O0O0O0_interval :#line:1389
            print (oOO0O0O0O0O0O0_num ,twice )#line:1390
            oo0o0O0O0O0_interval =True #line:1391
            oOO0O0O0O0O0O0_on =True #line:1392
            uioo0o000oo_need =True #line:1393
            if oOO0O0O0O0O0O0_num ==1 :#line:1394
                own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:1395
                setText (str (own_zxco0o0o0o01 ))#line:1396
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1397
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1398
                Paste ()#line:1399
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1400
                oOO0O0O0O0O0O0_on =True #line:1401
                oo0o0O0O0O0_on =False #line:1402
                oo0o0O0O0O0_interval =False #line:1403
                print (oo0o0O0O0O0_interval )#line:1404
                if not uioo0o000oo_one :#line:1406
                    O00OO00OOOO0O0000 =uioo0o000ooThread ()#line:1407
                    uioo0o000oo_one =True #line:1408
            elif oOO0O0O0O0O0O0_num ==2 and twice :#line:1409
                print ("第二次")#line:1410
                own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:1411
                setText (str (own_zxco0o0o0o02 ))#line:1412
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1413
                Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1414
                Paste ()#line:1415
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1416
                oOO0O0O0O0O0O0_on =True #line:1417
                oo0o0O0O0O0_on =False #line:1418
                oo0o0O0O0O0_interval =False #line:1419
                if not uioo0o000oo_one :#line:1420
                    O00OO00OOOO0O0000 =uioo0o000ooThread ()#line:1421
                    uioo0o000oo_one =True #line:1422
    @staticmethod #line:1488
    def OnClick_Backspace ():#line:1489
        pg .press ('backspace')#line:1490
    def Price_view (OOO0OOOO00OO0O0OO ,OOO00OOO00O0000OO ):#line:1493
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:1494
        pass #line:1495
    def MainControl (OOOOO0O000O00OO00 ,OO000OOOOO0OOO000 ):#line:1510
        if not web_on and zxco0o0o0o0_on :#line:1511
            OOOOO0O000O00OO00 .Price_close ()#line:1512
        if zxco0o0o0o0_on and not oOO0O0O0O0O0O0_on :#line:1513
            OOOOO0O000O00OO00 .Price_close ()#line:1514
        if not web_on and time_on :#line:1515
            OOOOO0O000O00OO00 .operationframe .Closetime ()#line:1516
        O00OOOOOO000O000O ='sc_new.png'#line:1517
        if not os .path .exists (O00OOOOOO000O000O ):#line:1518
            try :#line:1519
                OOOOO0O000O00OO00 .Price_close ()#line:1520
            except :#line:1521
                pass #line:1522
        if web_on :#line:1523
            OOOOO0O000O00OO00 .O0O0O0O0O0O0Oframe .Show (True )#line:1524
            try :#line:1525
                OOOOO0O000O00OO00 .operationframe .Show (True )#line:1526
            except :#line:1527
                pass #line:1528
        else :#line:1529
            OOOOO0O000O00OO00 .O0O0O0O0O0O0Oframe .Show (False )#line:1530
            try :#line:1531
                OOOOO0O000O00OO00 .operationframe .Show (False )#line:1532
            except :#line:1533
                pass #line:1534
        if web_on :#line:1537
            OOOOO0O000O00OO00 .Show (False )#line:1538
        else :#line:1539
            OOOOO0O000O00OO00 .Show (True )#line:1540
    @staticmethod #line:1544
    def oOO0O0O0O0O0O0_ok ():#line:1545
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need ,oOO0O0O0O0O0O0_on #line:1546
        if e_on and oOO0O0O0O0O0O0_on :#line:1547
            oOO0O0O0O0O0O0_OK =True #line:1548
            uioo0o000oo_need =False #line:1549
    @staticmethod #line:1551
    def oOO0O0O0O0O0O0_ok2 ():#line:1552
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need #line:1553
        if enter_on and oOO0O0O0O0O0O0_on :#line:1554
            oOO0O0O0O0O0O0_OK =True #line:1555
            uioo0o000oo_need =False #line:1556
    @classmethod #line:1558
    def query (O0O0O0O0O00O00OO0 ):#line:1559
        global query_interval ,query_on #line:1560
        if not query_interval and not query_on :#line:1561
            print ("执行")#line:1562
            query_on =True #line:1563
            query_interval =True #line:1564
            setText (str (1000000 ))#line:1565
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1566
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1567
            Paste ()#line:1568
            Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1569
            OO000OOOOO000O00O =threading .Timer (3 ,O0O0O0O0O00O00OO0 .query_sleep3 )#line:1570
            OO000OOOOO000O00O .start ()#line:1571
            OO0000O00OO000000 =threading .Timer (5 ,O0O0O0O0O00O00OO0 .query_sleep5 )#line:1572
            OO0000O00OO000000 .start ()#line:1573
        elif query_interval and query_on :#line:1574
            print (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1575
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1576
            query_on =False #line:1577
    @staticmethod #line:1580
    def query_sleep3 ():#line:1581
        print ("触发3+")#line:1582
        global query_interval ,query_on #line:1583
        if query_on :#line:1584
            print (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1585
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1586
            query_on =False #line:1587
    @staticmethod #line:1589
    def query_sleep5 ():#line:1590
        print ("触发5")#line:1591
        global query_interval #line:1592
        query_interval =False #line:1593
    def Price_close (OOOO0O000OOO0O000 ):#line:1598
        try :#line:1599
            OOOO0O000OOO0O000 .zxco0o0o0o0frame .Destroy ()#line:1600
        except :#line:1601
            pass #line:1602
    def Price_count (O0O0000O0O0OOOOO0 ,O0O0OOO00OO0OO0O0 ):#line:1606
        global zxco0o0o0o0_count #line:1607
        zxco0o0o0o0_count +=1 #line:1608
    @staticmethod #line:1614
    def Open ():#line:1615
        global do ,web_on #line:1616
        if not do :#line:1617
            do =True #line:1618
            OO00000OOO00OO00O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1624
            OO0O000OO0O0O0000 =ctypes .windll .user32 #line:1625
            O00000OO0O0O000O0 ={1 :(OO00000OOO00OO00O ['2'],win32con .MOD_ALT ),2 :(OO00000OOO00OO00O ['3'],win32con .MOD_ALT ),3 :(OO00000OOO00OO00O ['4'],win32con .MOD_ALT ),4 :(OO00000OOO00OO00O ['5'],win32con .MOD_ALT ),5 :(OO00000OOO00OO00O ['6'],win32con .MOD_ALT ),6 :(OO00000OOO00OO00O ['7'],win32con .MOD_ALT ),}#line:1629
            OOOOO0000OOO00000 ={7 :(OO00000OOO00OO00O ['s'],0x4000 ),8 :(OO00000OOO00OO00O ['f'],0x4000 ),9 :(OO00000OOO00OO00O ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OO00000OOO00OO00O ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OO00000OOO00OO00O ['q'],0x4000 )}#line:1632
            for OOO0O000OO0OO00OO ,(OO000000O000O0O0O ,OOOO0O00O000O0000 )in O00000OO0O0O000O0 .items ():#line:1634
                if not OO0O000OO0O0O0000 .RegisterHotKey (None ,OOO0O000OO0OO00OO ,OOOO0O00O000O0000 ,OO000000O000O0O0O ):#line:1635
                    print ("Unable to register id",OOO0O000OO0OO00OO )#line:1636
                    logging .info ("Unable to register id",OOO0O000OO0OO00OO )#line:1637
                    do =False #line:1638
            for OOO0O000OO0OO00OO ,(OO000000O000O0O0O ,OOOO0O00O000O0000 )in OOOOO0000OOO00000 .items ():#line:1639
                if not OO0O000OO0O0O0000 .RegisterHotKey (None ,OOO0O000OO0OO00OO ,OOOO0O00O000O0000 ,OO000000O000O0O0O ):#line:1640
                    print ("Unable to register id",OOO0O000OO0OO00OO )#line:1641
                    logging .info ("Unable to register id",OOO0O000OO0OO00OO )#line:1642
                    do =False #line:1643
                web_on =True #line:1644
    @staticmethod #line:1647
    def Listen ():#line:1648
        try :#line:1649
            O0O0O0O00O0OOOO00 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1654
            O0O00O0OOOO000OOO ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .OnClick_Tijiao ,9 :TopFrame .OnClick_oo0o0O0O0O0 ,10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .query }#line:1660
            O00OOOOOOOO000000 =ctypes .windll .user32 #line:1661
            OO000O0O00000O0O0 =wintypes .MSG ()#line:1662
            OOOOOO00O0000O0O0 =ctypes .byref #line:1663
            while O00OOOOOOOO000000 .GetMessageA (OOOOOO00O0000O0O0 (OO000O0O00000O0O0 ),None ,0 ,0 )!=0 :#line:1664
                if OO000O0O00000O0O0 .message ==win32con .WM_HOTKEY :#line:1665
                    OO0OO0OOO00O0O000 =O0O00O0OOOO000OOO .get (OO000O0O00000O0O0 .wParam )#line:1666
                    if OO0OO0OOO00O0O000 :#line:1667
                        OO0OO0OOO00O0O000 ()#line:1668
                O00OOOOOOOO000000 .TranslateMessage (OOOOOO00O0000O0O0 (OO000O0O00000O0O0 ))#line:1669
                O00OOOOOOOO000000 .DispatchMessageA (OOOOOO00O0000O0O0 (OO000O0O00000O0O0 ))#line:1670
        finally :#line:1671
            pass #line:1672
    @staticmethod #line:1679
    def Close ():#line:1680
        global do #line:1681
        if do :#line:1682
            do =False #line:1683
            OOO0OO000OOOO00OO ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1687
            O000000OOOOOOOO00 ={1 :(OOO0OO000OOOO00OO ['2'],win32con .MOD_ALT ),2 :(OOO0OO000OOOO00OO ['3'],win32con .MOD_ALT ),3 :(OOO0OO000OOOO00OO ['4'],win32con .MOD_ALT ),4 :(OOO0OO000OOOO00OO ['5'],win32con .MOD_ALT ),5 :(OOO0OO000OOOO00OO ['6'],win32con .MOD_ALT ),6 :(OOO0OO000OOOO00OO ['7'],win32con .MOD_ALT ),}#line:1691
            O0O00O00O0000000O =ctypes .windll .user32 #line:1692
            OOOO0O00O0O00O0OO ={7 :(OOO0OO000OOOO00OO ['s'],0x4000 ),8 :(OOO0OO000OOOO00OO ['f'],0x4000 ),9 :(OOO0OO000OOOO00OO ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OOO0OO000OOOO00OO ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OOO0OO000OOOO00OO ['q'],0x4000 )}#line:1695
            for O0OO00O0OO00OO0O0 in O000000OOOOOOOO00 .keys ():#line:1696
                O0O00O00O0000000O .UnregisterHotKey (None ,O0OO00O0OO00OO0O0 )#line:1697
            for O0OO00O0OO00OO0O0 in OOOO0O00O0O00O0OO .keys ():#line:1698
                O0O00O00O0000000O .UnregisterHotKey (None ,O0OO00O0OO00OO0O0 )#line:1699
            logging .info ("close assistant success")#line:1700
        else :#line:1701
            pass #line:1702
    def Save_log (OOOOOOO00O0O0OOO0 ):#line:1704
        OOOO0OOOOOO00O0OO =open ('pos.log','wb')#line:1705
        pickle .dump (Oo0o0Oo0o0o0 ,OOOO0OOOOOO00O0OO )#line:1706
        OOOO0OOOOOO00O0OO .close ()#line:1707
    def Screen_shot (OOO0OO0OOO0OO0000 ):#line:1712
        global Pricesize #line:1713
        OOOOOO00OO0OO0O0O =Pos_zxco0o0o0o0 #line:1714
        OOOO00OOO000OOOO0 =ImageGrab .grab (OOOOOO00OO0OO0O0O )#line:1715
        OOOO00OOO000OOOO0 .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:1716
    def Del_shot (OOO0OOO0OOO00O00O ):#line:1719
        try :#line:1720
            os .remove ("sc_new.png")#line:1721
        finally :#line:1722
            pass #line:1723
    def Confirmlogin (O00OOO0O00O0OOO00 ,O00OO0OOOOO0000O0 ):#line:1799
        Keeplogin ()#line:1800
    def Choose_time1 (O000OOO0000OOO0O0 ,O0O00O000OOO0OO00 ):#line:1805
        O000OOO0000OOO0O0 .timelabel .SetLabel ("已设定截止时间"+O000OOO0000OOO0O0 .time_choice1 .GetString (O000OOO0000OOO0O0 .time_choice1 .GetSelection ())+'.'+str (O000OOO0000OOO0O0 .time_choice2 .GetSelection ())+" 秒")#line:1808
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1809
        ghjo0o0o0o01 =O000OOO0000OOO0O0 .time_choice1 .GetString (O000OOO0000OOO0O0 .time_choice1 .GetSelection ())#line:1810
        ghjo0o0o0o02 =O000OOO0000OOO0O0 .time_choice2 .GetString (O000OOO0000OOO0O0 .time_choice2 .GetSelection ())#line:1811
    def Choose_time2 (O00OO0OOO00O00O0O ,OO0OO0000OOO0O0OO ):#line:1814
        O00OO0OOO00O00O0O .timelabel .SetLabel ("已设定截止时间"+O00OO0OOO00O00O0O .time_choice1 .GetString (O00OO0OOO00O00O0O .time_choice1 .GetSelection ())+'.'+str (O00OO0OOO00O00O0O .time_choice2 .GetSelection ())+" 秒")#line:1817
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1818
        ghjo0o0o0o01 =O00OO0OOO00O00O0O .time_choice1 .GetString (O00OO0OOO00O00O0O .time_choice1 .GetSelection ())#line:1819
        ghjo0o0o0o02 =O00OO0OOO00O00O0O .time_choice2 .GetString (O00OO0OOO00O00O0O .time_choice2 .GetSelection ())#line:1820
class ClockWindow (wx .Panel ):#line:1873
    def __init__ (OO00000OOOO0O00OO ,OOO0O00O00000O0OO ):#line:1874
        wx .Window .__init__ (OO00000OOOO0O00OO ,OOO0O00O00000O0OO ,size =Timesize )#line:1875
        OO00000OOOO0O00OO .Bind (wx .EVT_PAINT ,OO00000OOOO0O00OO .OnPaint )#line:1876
        OO00000OOOO0O00OO .timer =wx .Timer (OO00000OOOO0O00OO )#line:1877
        OO00000OOOO0O00OO .Bind (wx .EVT_TIMER ,OO00000OOOO0O00OO .OnTimer ,OO00000OOOO0O00OO .timer )#line:1878
        OO00000OOOO0O00OO .timer .Start (100 )#line:1879
    def Draw (O0OOO000000O0O00O ,OO0OO0O000O00O00O ):#line:1881
        global a_time #line:1882
        OOOO00OO00O0O0O00 =time .localtime (a_time )#line:1883
        OOOOO000O00O00OO0 =time .strftime ("%H:%M:%S",OOOO00OO00O0O0O00 )#line:1884
        O00000O0OO00O000O ,OO000OOO0O000OOO0 =O0OOO000000O0O00O .GetClientSize ()#line:1885
        OO0OO0O000O00O00O .SetBackground (wx .Brush (O0OOO000000O0O00O .GetBackgroundColour ()))#line:1886
        OO0OO0O000O00O00O .Clear ()#line:1887
        OO0OO0O000O00O00O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1888
        O0OO000O00O0O000O ,OO0OO0000OOO0O00O =OO0OO0O000O00O00O .GetTextExtent (OOOOO000O00O00OO0 )#line:1889
        OO0OO0O000O00O00O .DrawText (OOOOO000O00O00OO0 ,(O00000O0OO00O000O -O0OO000O00O0O000O )/2 ,(OO000OOO0O000OOO0 )/2 -OO0OO0000OOO0O00O /2 )#line:1890
    def Modify (OOOOO0O0OOO00O0OO ,O0OOO000O0O0O0000 ):#line:1892
        global a_time ,b_time #line:1893
        if b_time <9 :#line:1895
            b_time =b_time +1 #line:1896
        else :#line:1897
            b_time =0 #line:1898
        O00O0OO0000OO0O0O =time .localtime (a_time )#line:1899
        OOO000OOOOOOOO000 =time .strftime ("%H:%M:%S",O00O0OO0000OO0O0O )#line:1900
        OOO00O00OOO00OO0O ,O00O000O000OOOOOO =OOOOO0O0OOO00O0OO .GetClientSize ()#line:1902
        O0OOO000O0O0O0000 .SetBackground (wx .Brush (OOOOO0O0OOO00O0OO .GetBackgroundColour ()))#line:1903
        O0OOO000O0O0O0000 .Clear ()#line:1904
        O0OOO000O0O0O0000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1905
        OO000OO0OOO0OO0O0 ,OOOO0OO00O00OOO00 =O0OOO000O0O0O0000 .GetTextExtent (OOO000OOOOOOOO000 )#line:1906
        O0OOO000O0O0O0000 .DrawText (OOO000OOOOOOOO000 ,(OOO00O00OOO00OO0O -OO000OO0OOO0OO0O0 )/2 ,(O00O000O000OOOOOO )/2 -OOOO0OO00O00OOO00 /2 )#line:1907
    def OnTimer (O00O0O0OO0000000O ,O0OOO0000O00O0OO0 ):#line:1909
        O0O00O00OO0O0O0OO =wx .BufferedDC (wx .ClientDC (O00O0O0OO0000000O ))#line:1910
        O00O0O0OO0000000O .Modify (O0O00O00OO0O0O0OO )#line:1911
    def OnPaint (O00000OO000OO00O0 ,O0O000OO00000OOO0 ):#line:1913
        O000O0O0000OO000O =wx .BufferedPaintDC (O00000OO000OO00O0 )#line:1914
        O00000OO000OO00O0 .Draw (O000O0O0000OO000O )#line:1915
class TimeFrame (wx .Frame ):#line:1919
    def __init__ (OOO00000OOO00O000 ):#line:1920
        wx .Frame .__init__ (OOO00000OOO00O000 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1922
        ClockWindow (OOO00000OOO00O000 )#line:1925
class MoniClockWindow (wx .Panel ):#line:1930
    def __init__ (OO0O000OOO0OO000O ,OOO0OO00OO0OO0O0O ):#line:1931
        wx .Window .__init__ (OO0O000OOO0OO000O ,OOO0OO00OO0OO0O0O ,size =Timesize )#line:1932
        OO0O000OOO0OO000O .Bind (wx .EVT_PAINT ,OO0O000OOO0OO000O .OnPaint )#line:1933
        OO0O000OOO0OO000O .timer =wx .Timer (OO0O000OOO0OO000O )#line:1934
        OO0O000OOO0OO000O .Bind (wx .EVT_TIMER ,OO0O000OOO0OO000O .OnTimer ,OO0O000OOO0OO000O .timer )#line:1935
        OO0O000OOO0OO000O .timer .Start (100 )#line:1936
    def Draw (O0O0OO0O00O0O0OO0 ,O00OO0OOO0O00OOOO ):#line:1938
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1939
        OOOO0OOOOOOO0OO00 ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1940
        OOOO0OOO0000OOO0O ,O0O0O0O0O000O000O =O0O0OO0O00O0O0OO0 .GetClientSize ()#line:1941
        O00OO0OOO0O00OOOO .SetBackground (wx .Brush (O0O0OO0O00O0O0OO0 .GetBackgroundColour ()))#line:1942
        O00OO0OOO0O00OOOO .Clear ()#line:1943
        O00OO0OOO0O00OOOO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1944
        O0O0OO000OO0O00O0 ,O0OO00O0OOO0OOOO0 =O00OO0OOO0O00OOOO .GetTextExtent (OOOO0OOOOOOO0OO00 )#line:1945
        O00OO0OOO0O00OOOO .DrawText (OOOO0OOOOOOO0OO00 ,(OOOO0OOO0000OOO0O -O0O0OO000OO0O00O0 )/2 ,(O0O0O0O0O000O000O )/2 -O0OO00O0OOO0OOOO0 /2 )#line:1946
    def Modify (O000OO0OOO00000OO ,O00O0000OO00OOO0O ):#line:1948
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1949
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:1950
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:1951
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:1952
        O0O00O0OO00OO00O0 =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1953
        O0OOO0000000OOO0O ="%s:%s:%s"%(11 ,29 ,O0O00O0OO00OO00O0 )#line:1954
        OOOO000OO00OOOOO0 ,OOO0000000O00OOOO =O000OO0OOO00000OO .GetClientSize ()#line:1955
        O00O0000OO00OOO0O .SetBackground (wx .Brush (O000OO0OOO00000OO .GetBackgroundColour ()))#line:1956
        O00O0000OO00OOO0O .Clear ()#line:1957
        O00O0000OO00OOO0O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1958
        OOOO00OOO0000OOOO ,O0O0OO0000OOO000O =O00O0000OO00OOO0O .GetTextExtent (O0OOO0000000OOO0O )#line:1959
        O00O0000OO00OOO0O .DrawText (O0OOO0000000OOO0O ,(OOOO000OO00OOOOO0 -OOOO00OOO0000OOOO )/2 ,(OOO0000000O00OOOO )/2 -O0O0OO0000OOO000O /2 )#line:1960
    def OnTimer (OOO000OO00O00O0OO ,OO00O0000OOO00O00 ):#line:1962
        O0O0OOOO0O0O0O0OO =wx .BufferedDC (wx .ClientDC (OOO000OO00O00O0OO ))#line:1963
        OOO000OO00O00O0OO .Modify (O0O0OOOO0O0O0O0OO )#line:1964
    def OnPaint (O00OOOOOO0OO0O000 ,O000000OO000O0OO0 ):#line:1966
        OOOO0O0O0OOOO0OOO =wx .BufferedPaintDC (O00OOOOOO0OO0O000 )#line:1967
        O00OOOOOO0OO0O000 .Draw (OOOO0O0O0OOOO0OOO )#line:1968
class MoniTimeFrame (wx .Frame ):#line:1972
    def __init__ (O0OOOO0O00OO0OOO0 ):#line:1973
        wx .Frame .__init__ (O0OOOO0O00OO0OOO0 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1975
        MoniClockWindow (O0OOOO0O00OO0OOO0 )#line:1978
class PosFrame (wx .Frame ):#line:1983
    def __init__ (O00O000OOOOOOO0OO ,OO0OOOO0OO0OOO0OO ,OO00OO0OOO00O0000 ):#line:1984
        O0OO000O000O00O00 ,OOO000000O0O00000 =OO0OOOO0OO0OOO0OO #line:1985
        wx .Frame .__init__ (O00O000OOOOOOO0OO ,None ,-1 ,'POS',pos =(O0OO000O000O00O00 -20 ,OOO000000O0O00000 -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:1987
        OOO00OOO0OO0O0O0O =wx .Panel (O00O000OOOOOOO0OO ,-1 ,size =(30 ,20 ))#line:1988
        O00000OO0OO00O0OO =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:1990
        OO00O0O0O000OO0O0 =[]#line:1991
        OO00O0O0O000OO0O0 .append (wx .StaticText (OOO00OOO0OO0O0O0O ,-1 ,OO00OO0OOO00O0000 ,(0 ,0 )))#line:1993
        for O0O0O0OO00OO0OO0O in range (len (OO00O0O0O000OO0O0 )):#line:1994
            OO00O0O0O000OO0O0 [O0O0O0OO00OO0OO0O ].SetFont (O00000OO0OO00O0OO )#line:1995
class PriceFrame (wx .Frame ):#line:1997
    def __init__ (O000OOOOOO00O0OOO ,OO000O00O0000000O ):#line:1998
        wx .Frame .__init__ (O000OOOOOO00O0OOO ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2001
        O000OOOOOO00O0OOO .panel =wx .Panel (O000OOOOOO00O0OOO ,size =Pricesize )#line:2002
        wx .StaticBitmap (O000OOOOOO00O0OOO .panel ,-1 ,wx .BitmapFromImage (OO000O00O0000000O ))#line:2004
class YanzhengmaFrame (wx .Frame ):#line:2006
    def __init__ (O0OOO0OOOO00O000O ,OOO0OOOO00OOOOOO0 ):#line:2007
        wx .Frame .__init__ (O0OOO0OOOO00O000O ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2010
        O0OOO0OOOO00O000O .panel =wx .Panel (O0OOO0OOOO00O000O ,size =(400 ,80 ))#line:2011
        wx .StaticBitmap (O0OOO0OOOO00O000O .panel ,-1 ,wx .BitmapFromImage (OOO0OOOO00OOOOOO0 ))#line:2013
class AdFrame (wx .Frame ):#line:2017
    def __init__ (OOO00OOOO00O000O0 ):#line:2018
        wx .Frame .__init__ (OOO00OOOO00O000O0 ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2020
        OO0O0OOOOOOO0O0OO =wx .Panel (OOO00OOOO00O000O0 ,-1 ,size =(250 ,200 ))#line:2021
        O00O0OO000O0000O0 =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2023
        O0O00O00O0OOOOO00 =[]#line:2024
        O0O00O00O0OOOOO00 .append (wx .StaticText (OO0O0OOOOOOO0O0OO ,-1 ," 专业代拍软件",(15 ,10 )))#line:2026
        O0O00O00O0OOOOO00 .append (wx .StaticText (OO0O0OOOOOOO0O0OO ,-1 ," 专业代拍团队",(15 ,60 )))#line:2028
        O0O00O00O0OOOOO00 .append (wx .StaticText (OO0O0OOOOOOO0O0OO ,-1 ,"关注微信公众号",(15 ,110 )))#line:2030
        O0O00O00O0OOOOO00 .append (wx .StaticText (OO0O0OOOOOOO0O0OO ,-1 ," 沪牌第一枪",(15 ,160 )))#line:2032
        for O000000O0O0OO000O in range (len (O0O00O00O0OOOOO00 )):#line:2033
            O0O00O00O0OOOOO00 [O000000O0O0OO000O ].SetFont (O00O0OO000O0000O0 )#line:2034
class WebFrame (wx .Frame ):#line:2036
    def __init__ (O000OOOOO0OOOOOO0 ,OO000O00O0OOO0O00 ,O0O0O00O000O0O000 ,O0O0000O000OOO000 ,O000000OO00O0OOOO ):#line:2037
        wx .Frame .__init__ (O000OOOOO0OOOOOO0 ,None ,-1 ,O000000OO00O0OOOO ,size =(websize [0 ],websize [1 ]),pos =(OO000O00O0OOO0O00 ,O0O0O00O000O0O000 ))#line:2038
        if O0O0000O000OOO000 :#line:2043
            O000OOOOO0OOOOOO0 .adframe =AdFrame ()#line:2044
            O000OOOOO0OOOOOO0 .adframe .Show (True )#line:2045
        O000OOOOO0OOOOOO0 .Bind (wx .EVT_CLOSE ,O000OOOOO0OOOOOO0 .OnClose )#line:2046
        O000OOOOO0OOOOOO0 .ad2 =O0O0000O000OOO000 #line:2047
        O000OOOOO0OOOOOO0 .control =ControlFrame (O000000OO00O0OOOO )#line:2048
        O000OOOOO0OOOOOO0 .control .Show (True )#line:2049
        pub .subscribe (O000OOOOO0OOOOOO0 .OnClose2 ,"close web")#line:2074
    def OnClose (OOOOOO0O0O00O0OO0 ,O0OO000OO0000OO0O ):#line:2075
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2076
        web_on =False #line:2077
        view_time =False #line:2078
        o0sdofsfo0sodf0so0_on =False #line:2079
        ooweo0o0werwr_on =False #line:2080
        TopFrame .Close ()#line:2081
        OO00OOO00000OOO00 ="sc_new.png"#line:2082
        if os .path .exists (OO00OOO00000OOO00 ):#line:2083
            os .remove (OO00OOO00000OOO00 )#line:2084
        OOOOOO0O0O00O0OO0 .Destroy ()#line:2085
        if OOOOOO0O0O00O0OO0 .ad2 :#line:2086
            OOOOOO0O0O00O0OO0 .adframe .Destroy ()#line:2087
        O0OO000OO0000OO0O .Skip ()#line:2088
    def OnClose2 (OO0OOO0O00O00O0O0 ):#line:2090
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2091
        web_on =False #line:2092
        view_time =False #line:2093
        o0sdofsfo0sodf0so0_on =False #line:2094
        ooweo0o0werwr_on =False #line:2095
        TopFrame .Close ()#line:2096
        OOO0OO0O00OOO00OO ="sc_new.png"#line:2097
        if os .path .exists (OOO0OO0O00OOO00OO ):#line:2098
            os .remove (OOO0OO0O00OOO00OO )#line:2099
        OO0OOO0O00O00O0O0 .Destroy ()#line:2100
        if OO0OOO0O00O00O0O0 .ad2 :#line:2101
            OO0OOO0O00O00O0O0 .adframe .Destroy ()#line:2102
class ControlFrame (wx .Frame ):#line:2105
    def __init__ (OO0OOOO00O00O00O0 ,O0O000OO0O0O000OO ):#line:2106
        wx .Frame .__init__ (OO0OOOO00O00O00O0 ,None ,-1 ,size =(50 ,35 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +websize [0 ]-50 ,0 ))#line:2108
        OO0OOOO00O00O00O0 .panel =wx .Panel (OO0OOOO00O00O00O0 ,-1 ,size =(50 ,35 ))#line:2109
        OO0OOOO00O00O00O0 .button1 =wx .Button (OO0OOOO00O00O00O0 .panel ,pos =(0 ,0 ),size =(50 ,25 ),label ="关闭")#line:2110
        OO0OOOO00O00O00O0 .Bind (wx .EVT_BUTTON ,OO0OOOO00O00O00O0 .o_closeweb ,OO0OOOO00O00O00O0 .button1 )#line:2111
    def o_closeweb (O0OOOO0O0O00O0000 ,O000000OO0O0O00OO ):#line:2112
        wx .CallAfter (pub .sendMessage ,"close web")#line:2113
        O0OOOO0O0O00O0000 .Destroy ()#line:2114
        O000000OO0O0O00OO .Skip ()#line:2115
class OperationFrame (wx .Frame ):#line:2118
    def __init__ (O000OOO00O000O0OO ):#line:2119
        wx .Frame .__init__ (O000OOO00O000O0OO ,None ,-1 ,pos =(1070 ,100 ),size =(300 ,410 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION )#line:2121
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2123
        one_oO0O0O0O0O0O0O0O01 =O000OOO00O000O0OO .gettime (OO00000o01 )#line:2124
        one_oO0O0O0O0O0O0O0O02 =O000OOO00O000O0OO .gettime (OO00000o02 )#line:2125
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O000OOO00O000O0OO .gettime (ooo0O0o0oO0O_time1 )#line:2126
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O000OOO00O000O0OO .gettime (ooo0O0o0oO0O_time2 )#line:2127
        O0O0O00O00OO000O0 =wx .Panel (O000OOO00O000O0OO ,-1 ,size =(300 ,380 ))#line:2129
        OOOOO0OOOOOO0OO00 =wx .StaticBox (O0O0O00O00OO000O0 ,-1 ,u'选择策略:')#line:2131
        O000OOO00O000O0OO .stractagySizer =wx .StaticBoxSizer (OOOOO0OOOOOO0OO00 ,wx .VERTICAL )#line:2132
        O00O00OO0OO00O0O0 =wx .StaticText (O0O0O00O00OO000O0 ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2133
        O0O00OO0OOOOO0O00 =wx .BoxSizer (wx .HORIZONTAL )#line:2134
        O0O00OO0OOOOO0O00 .Add (O00O00OO0OO00O0O0 )#line:2135
        OOO0000OOOO0O0O0O =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2139
        O000OOO00O000O0OO .select_stractagy =wx .Choice (O0O0O00O00OO000O0 ,-1 ,choices =OOO0000OOOO0O0O0O ,size =(100 ,50 ))#line:2140
        O0O00OO0OOOOO0O00 .Add (O000OOO00O000O0OO .select_stractagy )#line:2141
        O000OOO00O000O0OO .select_stractagy .SetSelection (0 )#line:2142
        O000OOO00O000O0OO .timeview =wx .CheckBox (O0O0O00O00OO000O0 ,-1 ,label =u'显示时间')#line:2144
        O0O0O0O0OOOOOOO0O =wx .BoxSizer (wx .HORIZONTAL )#line:2145
        O0O0O0O0OOOOOOO0O .Add (O000OOO00O000O0OO .timeview )#line:2146
        O000OOO00O000O0OO .button1 =wx .Button (O0O0O00O00OO000O0 ,label ='+1s',size =(35 ,25 ))#line:2149
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Add_ooo0O0o0oO0O ,O000OOO00O000O0OO .button1 )#line:2150
        O000OOO00O000O0OO .button2 =wx .Button (O0O0O00O00OO000O0 ,label ='-1s',size =(35 ,25 ))#line:2151
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Minus_ooo0O0o0oO0O ,O000OOO00O000O0OO .button2 )#line:2152
        O000OOO00O000O0OO .button3 =wx .Button (O0O0O00O00OO000O0 ,label ='+0.1s',size =(35 ,25 ))#line:2153
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Add_time ,O000OOO00O000O0OO .button3 )#line:2154
        O000OOO00O000O0OO .button4 =wx .Button (O0O0O00O00OO000O0 ,label ='-0.1s',size =(35 ,25 ))#line:2155
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Minus_time ,O000OOO00O000O0OO .button4 )#line:2156
        O0O0O0O0OOOOOOO0O .Add (O000OOO00O000O0OO .button1 )#line:2158
        O0O0O0O0OOOOOOO0O .Add (O000OOO00O000O0OO .button2 )#line:2159
        O0O0O0O0OOOOOOO0O .Add (O000OOO00O000O0OO .button3 )#line:2160
        O0O0O0O0OOOOOOO0O .Add (O000OOO00O000O0OO .button4 )#line:2161
        OOOO00O00OO00OO0O =wx .BoxSizer (wx .VERTICAL )#line:2163
        OOOO00O00OO00OO0O .Add (O0O00OO0OOOOO0O00 )#line:2164
        OOOO00O00OO00OO0O .Add (O0O0O0O0OOOOOOO0O )#line:2165
        OOO0OOO0O0O00000O =["E键","回车"]#line:2168
        O000OOO00O000O0OO .sdfsf24324297_choice =wx .Choice (O0O0O00O00OO000O0 ,-1 ,choices =OOO0OOO0O0O00000O )#line:2169
        O000OOO00O000O0OO .sdfsf24324297_choice .SetSelection (0 )#line:2170
        O000OOO00O000O0OO .sdfsf24324297_label =wx .StaticText (O0O0O00O00OO000O0 ,label =u"确认提交方式     ")#line:2171
        OO0O00000O0O0O0O0 =wx .BoxSizer (wx .HORIZONTAL )#line:2172
        OO0O00000O0O0O0O0 .Add (O000OOO00O000O0OO .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2173
        OO0O00000O0O0O0O0 .Add (O000OOO00O000O0OO .sdfsf24324297_choice )#line:2174
        OOOO00O00OO00OO0O .Add (OO0O00000O0O0O0O0 )#line:2175
        O000OOO00O000O0OO .ghjo0o0o0o0_save =wx .Button (O0O0O00O00OO000O0 ,label ="保存策略",size =(60 ,35 ))#line:2178
        O000OOO00O000O0OO .ghjo0o0o0o0_load =wx .Button (O0O0O00O00OO000O0 ,label ="载入策略",size =(60 ,35 ))#line:2179
        O000OOO00O000O0OO .save_info =wx .Button (O0O0O00O00OO000O0 ,label ="用户信息",size =(60 ,35 ))#line:2180
        OO00O0OOO0O000000 =wx .BoxSizer (wx .HORIZONTAL )#line:2181
        OO00O0OOO0O000000 .Add (O000OOO00O000O0OO .ghjo0o0o0o0_save )#line:2182
        OO00O0OOO0O000000 .Add (O000OOO00O000O0OO .ghjo0o0o0o0_load )#line:2183
        OO00O0OOO0O000000 .Add (O000OOO00O000O0OO .save_info )#line:2184
        OOOO00O00OO00OO0O .Add (OO00O0OOO0O000000 )#line:2185
        OOOOO0OOOO0O0O0OO =wx .StaticBox (O0O0O00O00OO000O0 ,-1 ,u'单枪策略:')#line:2189
        O000OOO00O000O0OO .oneshotSizer =wx .StaticBoxSizer (OOOOO0OOOO0O0O0OO ,wx .VERTICAL )#line:2190
        O000OO0OOO000OOO0 =wx .GridBagSizer (4 ,4 )#line:2191
        O000OOO00O000O0OO .jiajia_time =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2192
        O000OOO00O000O0OO .jiajia_time .SetRange (40 ,55 )#line:2193
        O000OOO00O000O0OO .jiajia_time .SetValue (48 )#line:2194
        O000OOO00O000O0OO .jiajia_time .SetIncrement (0.1 )#line:2195
        O000OO0OOO000OOO0 .Add (O000OOO00O000O0OO .jiajia_time ,pos =(0 ,0 ))#line:2197
        O0OO000000OOO0OOO =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2198
        O000OO0OOO000OOO0 .Add (O0OO000000OOO0OOO ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2199
        O0000O00O0000O0O0 =wx .StaticText (O0O0O00O00OO000O0 ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2200
        O000OO0OOO000OOO0 .Add (O0000O00O0000O0O0 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2201
        O000OOO00O000O0OO .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2202
        O000OOO00O000O0OO .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2203
        O000OOO00O000O0OO .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2204
        O000OOO00O000O0OO .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2205
        O000OO0OOO000OOO0 .Add (O000OOO00O000O0OO .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2206
        O0OO0OOO0OOOO0000 =[u"提前100",u"提前200",u"踩点"]#line:2209
        O000OOO00O000O0OO .select_oOO0O0O0O0O0O0 =wx .Choice (O0O0O00O00OO000O0 ,-1 ,choices =O0OO0OOO0OOOO0000 ,size =(68 ,25 ))#line:2210
        O000OOO00O000O0OO .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2211
        O000OO0OOO000OOO0 .Add (O000OOO00O000O0OO .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2212
        O0O0O0O0O0O0OO00O =wx .StaticText (O0O0O00O00OO000O0 ,label =u"出价提交延迟")#line:2213
        O000OO0OOO000OOO0 .Add (O0O0O0O0O0O0OO00O ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2214
        O000OOO00O000O0OO .yanchi_time =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2215
        O000OOO00O000O0OO .yanchi_time .SetRange (0.0 ,1.0 )#line:2216
        O000OOO00O000O0OO .yanchi_time .SetValue (0.5 )#line:2217
        O000OOO00O000O0OO .yanchi_time .SetIncrement (0.1 )#line:2218
        O000OO0OOO000OOO0 .Add (O000OOO00O000O0OO .yanchi_time ,pos =(1 ,3 ))#line:2219
        O00OOOO00O00OOO0O =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2220
        O000OO0OOO000OOO0 .Add (O00OOOO00O00OOO0O ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2221
        O0OO00OOO00O0O0OO =wx .StaticText (O0O0O00O00OO000O0 ,label =u"强制提交时间")#line:2224
        O000OO0OOO000OOO0 .Add (O0OO00OOO00O0O0OO ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2225
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2226
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2227
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2228
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2229
        O000OO0OOO000OOO0 .Add (O000OOO00O000O0OO .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2230
        O0OOOOO0OO00O0OOO =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2231
        O000OO0OOO000OOO0 .Add (O0OOOOO0OO00O0OOO ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2232
        O000OOO00O000O0OO .oneshotSizer .Add (O000OO0OOO000OOO0 ,0 ,flag =wx .ALL ,border =5 )#line:2234
        OO0000OO000000O00 =wx .StaticBox (O0O0O00O00OO000O0 ,-1 ,u'双枪策略:')#line:2238
        O000OOO00O000O0OO .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (OO0000OO000000O00 ,wx .VERTICAL )#line:2239
        O0O0O00OO00OO0OOO =wx .GridBagSizer (4 ,4 )#line:2240
        O000OOO00O000O0OO .jiajia_time2 =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2241
        O000OOO00O000O0OO .jiajia_time2 .SetRange (40 ,55 )#line:2242
        O000OOO00O000O0OO .jiajia_time2 .SetValue (48 )#line:2243
        O000OOO00O000O0OO .jiajia_time2 .SetIncrement (0.1 )#line:2244
        O0O0O00OO00OO0OOO .Add (O000OOO00O000O0OO .jiajia_time2 ,pos =(0 ,0 ))#line:2245
        OOO0000O0O00O0OOO =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2246
        O0O0O00OO00OO0OOO .Add (OOO0000O0O00O0OOO ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2247
        O0OOOOO00O00OO0O0 =wx .StaticText (O0O0O00O00OO000O0 ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2248
        O0O0O00OO00OO0OOO .Add (O0OOOOO00O00OO0O0 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2249
        O000OOO00O000O0OO .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2250
        O000OOO00O000O0OO .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2251
        O000OOO00O000O0OO .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2252
        O000OOO00O000O0OO .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2253
        O0O0O00OO00OO0OOO .Add (O000OOO00O000O0OO .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2254
        O0O000O0OO0000O0O =[u"提前100",u"提前200",u"踩点"]#line:2256
        O000OOO00O000O0OO .select_oOO0O0O0O0O0O02 =wx .Choice (O0O0O00O00OO000O0 ,-1 ,choices =O0O000O0OO0000O0O ,size =(68 ,25 ))#line:2257
        O000OOO00O000O0OO .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2258
        O0O0O00OO00OO0OOO .Add (O000OOO00O000O0OO .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2259
        OOO0000OO0O0O0OOO =wx .StaticText (O0O0O00O00OO000O0 ,label =u"出价提交延迟")#line:2260
        O0O0O00OO00OO0OOO .Add (OOO0000OO0O0O0OOO ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2261
        O000OOO00O000O0OO .yanchi_time2 =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2262
        O000OOO00O000O0OO .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2263
        O000OOO00O000O0OO .yanchi_time2 .SetValue (0.5 )#line:2264
        O000OOO00O000O0OO .yanchi_time2 .SetIncrement (0.1 )#line:2265
        O0O0O00OO00OO0OOO .Add (O000OOO00O000O0OO .yanchi_time2 ,pos =(1 ,3 ))#line:2266
        OOOO0OOOO0O00000O =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2267
        O0O0O00OO00OO0OOO .Add (OOOO0OOOO0O00000O ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2268
        O00O00O00000OOOO0 =wx .StaticText (O0O0O00O00OO000O0 ,label =u"强制提交时间")#line:2271
        O0O0O00OO00OO0OOO .Add (O00O00O00000OOOO0 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2272
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (O0O0O00O00OO000O0 ,-1 ,"",size =(68 ,25 ))#line:2273
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2274
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2275
        O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2276
        O0O0O00OO00OO0OOO .Add (O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2277
        O000000000O000000 =wx .StaticText (O0O0O00O00OO000O0 ,label =u"秒")#line:2278
        O0O0O00OO00OO0OOO .Add (O000000000O000000 ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2279
        O000OOO00O000O0OO .ooo0O0o0oO0OshotSizer .Add (O0O0O00OO00OO0OOO ,0 ,flag =wx .ALL ,border =5 )#line:2281
        O000OOO00O000O0OO .stractagySizer .Add (OOOO00O00OO00OO0O ,0 ,wx .ALL |wx .CENTER ,5 )#line:2283
        O000OOO00O000O0OO .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2284
        O0OOO0O0OOO0OO00O =wx .StaticText (O0O0O00O00OO000O0 ,-1 ,label =u"拍牌功能设置")#line:2287
        OOOO0O0O00OO0O000 =wx .StaticLine (O0O0O00O00OO000O0 ,-1 )#line:2288
        O000OOO00O000O0OO .vbox1 .Add (O0OOO0O0OOO0OO00O ,0 ,wx .ALL |wx .LEFT ,10 )#line:2289
        O000OOO00O000O0OO .vbox1 .Add (OOOO0O0O00OO0O000 ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2290
        O000OOO00O000O0OO .vbox1 .Add (O000OOO00O000O0OO .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2291
        O000OOO00O000O0OO .vbox1 .Add (O000OOO00O000O0OO .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2292
        O000OOO00O000O0OO .vbox1 .Add (O000OOO00O000O0OO .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2293
        O0O0O00O00OO000O0 .SetSizer (O000OOO00O000O0OO .vbox1 )#line:2294
        O000OOO00O000O0OO .ooo0O0o0oO0Osizer_Shown =False #line:2297
        O000OOO00O000O0OO .oneshotsizer_Shown =True #line:2298
        O000OOO00O000O0OO .vbox1 .Hide (O000OOO00O000O0OO .ooo0O0o0oO0OshotSizer )#line:2299
        O000OOO00O000O0OO .Bind (wx .EVT_CHECKBOX ,O000OOO00O000O0OO .Timeview ,O000OOO00O000O0OO .timeview )#line:2308
        O000OOO00O000O0OO .Bind (wx .EVT_CHOICE ,O000OOO00O000O0OO .Confirmchoice ,O000OOO00O000O0OO .sdfsf24324297_choice )#line:2309
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Strategy_save ,O000OOO00O000O0OO .ghjo0o0o0o0_save )#line:2310
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Strategy_load ,O000OOO00O000O0OO .ghjo0o0o0o0_load )#line:2311
        O000OOO00O000O0OO .Bind (wx .EVT_BUTTON ,O000OOO00O000O0OO .Save_info ,O000OOO00O000O0OO .save_info )#line:2312
        O000OOO00O000O0OO .Bind (wx .EVT_CHOICE ,O000OOO00O000O0OO .Refresh_panel ,O000OOO00O000O0OO .select_stractagy )#line:2314
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Jiajia_time ,O000OOO00O000O0OO .jiajia_time )#line:2316
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Jiajia_zxco0o0o0o0 ,O000OOO00O000O0OO .jiajia_zxco0o0o0o0 )#line:2318
        O000OOO00O000O0OO .Bind (wx .EVT_CHOICE ,O000OOO00O000O0OO .Select_oOO0O0O0O0O0O0 ,O000OOO00O000O0OO .select_oOO0O0O0O0O0O0 )#line:2319
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Yanchi_time ,O000OOO00O000O0OO .yanchi_time )#line:2321
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Tijiao_time ,O000OOO00O000O0OO .oOO0O0O0O0O0O0_time )#line:2323
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Jiajia_time2 ,O000OOO00O000O0OO .jiajia_time2 )#line:2326
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Jiajia_zxco0o0o0o02 ,O000OOO00O000O0OO .jiajia_zxco0o0o0o02 )#line:2328
        O000OOO00O000O0OO .Bind (wx .EVT_CHOICE ,O000OOO00O000O0OO .Select_oOO0O0O0O0O0O02 ,O000OOO00O000O0OO .select_oOO0O0O0O0O0O02 )#line:2329
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Yanchi_time2 ,O000OOO00O000O0OO .yanchi_time2 )#line:2331
        O000OOO00O000O0OO .Bind (wx .EVT_TEXT ,O000OOO00O000O0OO .Tijiao_time2 ,O000OOO00O000O0OO .oOO0O0O0O0O0O0_time2 )#line:2333
        O000OOO00O000O0OO .timeframe1 =TimeFrame ()#line:2335
        O000OOO00O000O0OO .timeframe1 .Show (False )#line:2336
        O000OOO00O000O0OO .timeframe2 =MoniTimeFrame ()#line:2338
        O000OOO00O000O0OO .timeframe2 .Show (False )#line:2339
        O000OOO00O000O0OO .operationtimer =wx .Timer (O000OOO00O000O0OO )#line:2342
        O000OOO00O000O0OO .Bind (wx .EVT_TIMER ,O000OOO00O000O0OO .opt ,O000OOO00O000O0OO .operationtimer )#line:2343
        O000OOO00O000O0OO .operationtimer .Start (3000 )#line:2344
    def opt (O0OO00OO00OO0O0O0 ,OOO00O00O0O00OO00 ):#line:2345
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2346
        global ghjo0o0o0o0_on #line:2347
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2348
        if O0OO00OO00OO0O0O0 .select_stractagy .GetSelection ==0 :#line:2349
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2350
                print ("触发1")#line:2351
                twice =False #line:2352
                ghjo0o0o0o0_on =True #line:2353
                oo0o0O0O0O0_on =True #line:2354
                oOO0O0O0O0O0O0_on =False #line:2355
                oOO0O0O0O0O0O0_num =1 #line:2356
                oOO0O0O0O0O0O0_OK =False #line:2357
                oOO0O0O0O0O0O0_one =False #line:2358
        elif O0OO00OO00OO0O0O0 .select_stractagy .GetSelection ==1 :#line:2359
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2360
                print ("触发2")#line:2361
                ghjo0o0o0o0_on =True #line:2362
                twice =True #line:2363
                oo0o0O0O0O0_on =True #line:2364
                oOO0O0O0O0O0O0_on =False #line:2365
                oOO0O0O0O0O0O0_num =1 #line:2366
                oOO0O0O0O0O0O0_OK =False #line:2367
                oOO0O0O0O0O0O0_one =False #line:2368
    def Add_time (O000000000O00OO00 ,O0OO00000OOO0000O ):#line:2372
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2373
        if o0sdofsfo0sodf0so0_on :#line:2374
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2375
        else :#line:2376
            a_time +=0.1 #line:2377
    def Minus_time (O000O0000O0OOOOO0 ,O00OOO000OO0OO0O0 ):#line:2379
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2380
        if o0sdofsfo0sodf0so0_on :#line:2381
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2382
        else :#line:2383
            a_time -=0.1 #line:2384
    def Add_ooo0O0o0oO0O (OO00O0OOO0OO00OOO ,OOOOOOOOOOOOO0OO0 ):#line:2386
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2387
        if o0sdofsfo0sodf0so0_on :#line:2388
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2389
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2390
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2391
        else :#line:2392
            a_time +=1 #line:2393
    def Minus_ooo0O0o0oO0O (O00O00OOO0OO0O0OO ,O0O0OOOO000OOOOO0 ):#line:2395
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2396
        if o0sdofsfo0sodf0so0_on :#line:2397
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2398
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2399
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2400
        else :#line:2401
            a_time -=1 #line:2402
    def Timeview (OOOO00O0O00O0O0OO ,O0O0000000O00O000 ):#line:2404
        OOOOOO000O0O00OOO =O0O0000000O00O000 .GetEventObject ()#line:2405
        global view_time ,time_on #line:2406
        if OOOOOO000O0O00OOO .IsChecked ():#line:2407
            view_time =True #line:2408
            time_on =True #line:2409
            if ooweo0o0werwr_on :#line:2410
                OOOO00O0O00O0O0OO .timeframe1 .Show (True )#line:2411
            elif o0sdofsfo0sodf0so0_on :#line:2412
                OOOO00O0O00O0O0OO .timeframe2 .Show (True )#line:2413
        else :#line:2414
            view_time =False #line:2415
            time_on =False #line:2416
            if ooweo0o0werwr_on :#line:2417
                OOOO00O0O00O0O0OO .timeframe1 .Show (False )#line:2418
            elif o0sdofsfo0sodf0so0_on :#line:2419
                OOOO00O0O00O0O0OO .timeframe2 .Show (False )#line:2420
    def Opentime (OO0O0O000O0O00000 ):#line:2422
        if o0sdofsfo0sodf0so0_on :#line:2423
            try :#line:2424
                OO0O0O000O0O00000 .timeframe2 .Show (True )#line:2425
            except :#line:2426
                pass #line:2427
        elif ooweo0o0werwr_on :#line:2428
            try :#line:2429
                OO0O0O000O0O00000 .timeframe1 .Show (True )#line:2430
            except :#line:2431
                pass #line:2432
    def Closetime (OO000O0OO00000OO0 ):#line:2435
        try :#line:2436
            OO000O0OO00000OO0 .timeframe1 .Show (False )#line:2437
        except :#line:2438
            pass #line:2439
        try :#line:2440
            OO000O0OO00000OO0 .timeframe2 .Show (False )#line:2441
        except :#line:2442
            pass #line:2443
    def Confirmchoice (O00OO0O0O0OOOOO00 ,OOO000000OOO000OO ):#line:2445
        global e_on ,enter_on #line:2446
        O000O00OO00O00OOO =O00OO0O0O0OOOOO00 .sdfsf24324297_choice .GetSelection ()#line:2447
        if O000O00OO00O00OOO ==0 :#line:2448
            e_on =True #line:2449
            enter_on =False #line:2450
        elif O000O00OO00O00OOO ==1 :#line:2451
            e_on =False #line:2452
            enter_on =True #line:2453
    def Jiajia_time (O0OO0OO00O0OO000O ,OOOOO00O00O0O00OO ):#line:2457
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2458
        OO0O00O0000O0OO0O =O0OO0OO00O0OO000O .jiajia_time .GetValue ()#line:2459
        OO00O0O0OO0OO00O0 =[40 +OO00OO00000OO00OO *0.1 for OO00OO00000OO00OO in range (151 )]#line:2460
        if OO0O00O0000O0OO0O in OO00O0O0OO0OO00O0 :#line:2461
            OO00000o01 =OO0O00O0000O0OO0O #line:2462
            OO00000o01 =float (OO00000o01 )#line:2463
            one_oO0O0O0O0O0O0O0O01 =O0OO0OO00O0OO000O .gettime (OO00000o01 )#line:2464
        else :#line:2465
            O0OO0OO00O0OO000O .jiajia_time .SetValue (OO00000o01 )#line:2466
    def Jiajia_zxco0o0o0o0 (O0OO0OO0O00O0O0O0 ,OOO000O000O0OO0O0 ):#line:2469
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2470
        OOO0OOOOO0O0O0O0O =[300 +O00O0OOO0O00O00OO *100 for O00O0OOO0O00O00OO in range (13 )]#line:2471
        O0000OO0000OOOO00 =O0OO0OO0O00O0O0O0 .jiajia_zxco0o0o0o0 .GetValue ()#line:2472
        if O0000OO0000OOOO00 in OOO0OOOOO0O0O0O0O :#line:2473
            one_diff =int (O0000OO0000OOOO00 )#line:2474
        else :#line:2475
            O0OO0OO0O00O0O0O0 .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2476
    def Select_oOO0O0O0O0O0O0 (OOOO0OO0000O00OO0 ,O000000OO000O0OOO ):#line:2479
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2480
        OOOOOOO0OOO0OO000 =OOOO0OO0000O00OO0 .select_oOO0O0O0O0O0O0 .GetString (OOOO0OO0000O00OO0 .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2481
        if OOOOOOO0OOO0OO000 ==u"提前100":#line:2482
            one_advance =100 #line:2483
        elif OOOOOOO0OOO0OO000 ==u"提前200":#line:2484
            one_advance =200 #line:2485
        else :#line:2486
            one_advance =0 #line:2487
    def Yanchi_time (OO00O000OO0OO0O00 ,OO0O0OOO0OOOOOO00 ):#line:2489
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2490
        O00O0O0OOO000O0O0 =['0.%d'%OOO0OO0OO0OOOOO0O for OOO0OO0OO0OOOOO0O in range (11 )]#line:2491
        O00O0O0OOO000O0O0 .append ('1.0')#line:2492
        O00OO0O000O0OOOOO =str (OO00O000OO0OO0O00 .yanchi_time .GetValue ())#line:2493
        if O00OO0O000O0OOOOO in O00O0O0OOO000O0O0 :#line:2494
            one_delay =float (O00OO0O000O0OOOOO )#line:2495
        else :#line:2496
            OO00O000OO0OO0O00 .yanchi_time .SetValue (one_delay )#line:2497
    def Tijiao_time (O0OO000O0OO0OOOOO ,OOO00000000000O00 ):#line:2499
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2500
        O0O00OO00OOO00OOO =O0OO000O0OO0OOOOO .oOO0O0O0O0O0O0_time .GetValue ()#line:2501
        OOOO00O0OO00O000O =[40 +O0OO0O000O00OO00O *0.1 for O0OO0O000O00OO00O in range (171 )]#line:2502
        if O0O00OO00OOO00OOO in OOOO00O0OO00O000O :#line:2503
            OO00000o02 =float (O0O00OO00OOO00OOO )#line:2504
            one_oO0O0O0O0O0O0O0O02 =O0OO000O0OO0OOOOO .gettime (OO00000o02 )#line:2505
        else :#line:2506
            O0OO000O0OO0OOOOO .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2507
    def Jiajia_time2 (O0OOO00000OOOO00O ,O000OO000O0O0000O ):#line:2509
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2510
        OO00OO0OOOO00O00O =O0OOO00000OOOO00O .jiajia_time2 .GetValue ()#line:2511
        O0OO0000OO0OO000O =[40 +O0OO0O0OOOOOO0O0O *0.1 for O0OO0O0OOOOOO0O0O in range (151 )]#line:2512
        if OO00OO0OOOO00O00O in O0OO0000OO0OO000O :#line:2513
            ooo0O0o0oO0O_time1 =float (OO00OO0OOOO00O00O )#line:2514
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0OOO00000OOOO00O .gettime (ooo0O0o0oO0O_time1 )#line:2515
        else :#line:2516
            O0OOO00000OOOO00O .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2517
    def Jiajia_zxco0o0o0o02 (O0O000000000OO00O ,OO00O0O0O00OO0000 ):#line:2519
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2520
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2521
        OOO00OOOO0OO00000 =[300 +O0O0OOO00O00000OO *100 for O0O0OOO00O00000OO in range (13 )]#line:2522
        OO000OOO0000OO000 =O0O000000000OO00O .jiajia_zxco0o0o0o02 .GetValue ()#line:2523
        if OO000OOO0000OO000 in OOO00OOOO0OO00000 :#line:2524
            ooo0O0o0oO0O_diff =int (OO000OOO0000OO000 )#line:2525
        else :#line:2526
            O0O000000000OO00O .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2527
    def Select_oOO0O0O0O0O0O02 (OO00OOO0O0OOO0OO0 ,OO0O0OOO000O0O0O0 ):#line:2529
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2530
        OOO000OO0OO00O000 =OO00OOO0O0OOO0OO0 .select_oOO0O0O0O0O0O02 .GetString (OO00OOO0O0OOO0OO0 .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2531
        if OOO000OO0OO00O000 ==u"提前100":#line:2532
            ooo0O0o0oO0O_advance =100 #line:2533
        elif OOO000OO0OO00O000 ==u"提前200":#line:2534
            ooo0O0o0oO0O_advance =200 #line:2535
        else :#line:2536
            ooo0O0o0oO0O_advance =0 #line:2537
    def Yanchi_time2 (O0O0OOO00O0O0OOOO ,O0O0O0000O0O00OO0 ):#line:2540
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2541
        OO00O0OOO00O0O0OO =['0.%d'%OOOOOOOOO00O0O0OO for OOOOOOOOO00O0O0OO in range (11 )]#line:2542
        OO00O0OOO00O0O0OO .append ('1.0')#line:2543
        O000OO0O0O0O000OO =str (O0O0OOO00O0O0OOOO .yanchi_time2 .GetValue ())#line:2544
        if O000OO0O0O0O000OO in OO00O0OOO00O0O0OO :#line:2545
            ooo0O0o0oO0O_delay =float (O000OO0O0O0O000OO )#line:2546
        else :#line:2547
            O0O0OOO00O0O0OOOO .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2548
    def Tijiao_time2 (O000OOO00OO0OOO0O ,O00OO0O00O0OOOO00 ):#line:2551
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2552
        OOO0O000O000O0OO0 =O000OOO00OO0OOO0O .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2553
        O000OO0OOO0O00OO0 =[53 +OO0000OO0O0000OO0 *0.1 for OO0000OO0O0000OO0 in range (41 )]#line:2554
        if OOO0O000O000O0OO0 in O000OO0OOO0O00OO0 :#line:2555
            ooo0O0o0oO0O_time2 =float (OOO0O000O000O0OO0 )#line:2556
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O000OOO00OO0OOO0O .gettime (ooo0O0o0oO0O_time2 )#line:2557
        else :#line:2558
            O000OOO00OO0OOO0O .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2559
    def Refresh_panel (O00OO0O00O0OOO000 ,O0000OOOOOO000O00 ):#line:2563
        global ghjo0o0o0o0_on #line:2565
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2566
        OO000O0OOO0O0000O =O00OO0O00O0OOO000 .select_stractagy .GetString (O00OO0O00O0OOO000 .select_stractagy .GetSelection ())#line:2567
        if OO000O0OOO0O0000O ==u"单枪策略":#line:2568
            O00OO0O00O0OOO000 .ss_Hide ()#line:2569
            twice =False #line:2570
            ghjo0o0o0o0_on =True #line:2571
            oo0o0O0O0O0_on =True #line:2572
            oOO0O0O0O0O0O0_on =False #line:2573
            oOO0O0O0O0O0O0_num =1 #line:2574
            oOO0O0O0O0O0O0_OK =False #line:2575
            oOO0O0O0O0O0O0_one =False #line:2576
        elif OO000O0OOO0O0000O ==u"双枪策略":#line:2578
            O00OO0O00O0OOO000 .ss_Shown ()#line:2579
            ghjo0o0o0o0_on =True #line:2580
            twice =True #line:2581
            oo0o0O0O0O0_on =True #line:2582
            oOO0O0O0O0O0O0_on =False #line:2583
            oOO0O0O0O0O0O0_num =1 #line:2584
            oOO0O0O0O0O0O0_OK =False #line:2585
            oOO0O0O0O0O0O0_one =False #line:2586
        else :#line:2587
            O00OO0O00O0OOO000 .none_show ()#line:2588
            ghjo0o0o0o0_on =False #line:2589
            twice =False #line:2590
    def ss_Shown (OOO0OOO0OO0OO0OOO ):#line:2593
        if not OOO0OOO0OO0OO0OOO .ooo0O0o0oO0Osizer_Shown :#line:2594
            OOO0OOO0OO0OO0OOO .vbox1 .Show (OOO0OOO0OO0OO0OOO .ooo0O0o0oO0OshotSizer )#line:2595
            OOO0OOO0OO0OO0OOO .ooo0O0o0oO0Osizer_Shown =True #line:2596
        if not OOO0OOO0OO0OO0OOO .oneshotsizer_Shown :#line:2597
            OOO0OOO0OO0OO0OOO .vbox1 .Show (OOO0OOO0OO0OO0OOO .oneshotSizer )#line:2598
            OOO0OOO0OO0OO0OOO .oneshotsizer_Shown =True #line:2599
        OOO0OOO0OO0OO0OOO .ooo0O0o0oO0Osizer_Shown =True #line:2600
        OOO0OOO0OO0OO0OOO .oneshotSizer_Shown =True #line:2601
        OOO0OOO0OO0OO0OOO .SetClientSize ((280 ,560 ))#line:2602
        OOO0OOO0OO0OO0OOO .Secondshot_reset ()#line:2603
        OOO0OOO0OO0OO0OOO .Layout ()#line:2604
    def ss_Hide (OO00OO00OO0OO00OO ):#line:2606
        if OO00OO00OO0OO00OO .ooo0O0o0oO0Osizer_Shown :#line:2607
            OO00OO00OO0OO00OO .vbox1 .Hide (OO00OO00OO0OO00OO .ooo0O0o0oO0OshotSizer )#line:2608
        if not OO00OO00OO0OO00OO .oneshotsizer_Shown :#line:2611
            OO00OO00OO0OO00OO .vbox1 .Show (OO00OO00OO0OO00OO .oneshotSizer )#line:2612
        OO00OO00OO0OO00OO .ooo0O0o0oO0Osizer_Shown =False #line:2613
        OO00OO00OO0OO00OO .oneshotSizer_Shown =True #line:2614
        OO00OO00OO0OO00OO .SetClientSize ((280 ,360 ))#line:2615
        OO00OO00OO0OO00OO .Oneshot_reset ()#line:2616
        OO00OO00OO0OO00OO .Layout ()#line:2617
    def none_show (OO0OO0OOOOO0OO000 ):#line:2619
        if OO0OO0OOOOO0OO000 .oneshotsizer_Shown :#line:2620
            OO0OO0OOOOO0OO000 .vbox1 .Hide (OO0OO0OOOOO0OO000 .ooo0O0o0oO0OshotSizer )#line:2621
        if OO0OO0OOOOO0OO000 .ooo0O0o0oO0Osizer_Shown :#line:2622
            OO0OO0OOOOO0OO000 .vbox1 .Hide (OO0OO0OOOOO0OO000 .oneshotSizer )#line:2623
        OO0OO0OOOOO0OO000 .oneshotsizer_Shown =False #line:2625
        OO0OO0OOOOO0OO000 .ooo0O0o0oO0Osizer_Shown =False #line:2626
        OO0OO0OOOOO0OO000 .SetClientSize ((280 ,240 ))#line:2627
        OO0OO0OOOOO0OO000 .Layout ()#line:2628
    def Oneshot_reset (OO0OO0O00O00O0O00 ):#line:2630
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2631
        OO0OO0O00O00O0O00 .jiajia_time .SetValue (48.0 )#line:2632
        OO0OO0O00O00O0O00 .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2633
        OO0OO0O00O00O0O00 .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2634
        OO0OO0O00O00O0O00 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2635
        OO0OO0O00O00O0O00 .yanchi_time .SetValue (0.5 )#line:2636
        OO00000o01 =48 #line:2638
        OO00000o02 =55 #line:2639
        one_diff =700 #line:2640
        one_delay =0.5 #line:2641
        one_advance =100 #line:2642
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2644
        one_oO0O0O0O0O0O0O0O01 =OO0OO0O00O00O0O00 .gettime (OO00000o01 )#line:2645
        one_oO0O0O0O0O0O0O0O02 =OO0OO0O00O00O0O00 .gettime (OO00000o02 )#line:2646
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0OO0O00O00O0O00 .gettime (ooo0O0o0oO0O_time1 )#line:2647
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0OO0O00O00O0O00 .gettime (ooo0O0o0oO0O_time2 )#line:2648
    def Secondshot_reset (OOOOOOOOOO0OO00O0 ):#line:2651
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2652
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2653
        OOOOOOOOOO0OO00O0 .jiajia_time .SetValue (40.0 )#line:2654
        OOOOOOOOOO0OO00O0 .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:2655
        OOOOOOOOOO0OO00O0 .jiajia_zxco0o0o0o0 .SetValue (500 )#line:2656
        OOOOOOOOOO0OO00O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2657
        OOOOOOOOOO0OO00O0 .yanchi_time .SetValue (0.0 )#line:2658
        OOOOOOOOOO0OO00O0 .jiajia_time2 .SetValue (50.0 )#line:2660
        OOOOOOOOOO0OO00O0 .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:2661
        OOOOOOOOOO0OO00O0 .jiajia_zxco0o0o0o02 .SetValue (700 )#line:2662
        OOOOOOOOOO0OO00O0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2663
        OOOOOOOOOO0OO00O0 .yanchi_time2 .SetValue (0.5 )#line:2664
        OO00000o01 =40 #line:2666
        OO00000o02 =48 #line:2667
        one_diff =500 #line:2668
        one_delay =0.5 #line:2669
        one_advance =100 #line:2670
        ooo0O0o0oO0O_time1 =50 #line:2672
        ooo0O0o0oO0O_time2 =55.5 #line:2673
        ooo0O0o0oO0O_diff =700 #line:2674
        ooo0O0o0oO0O_delay =0.5 #line:2675
        ooo0O0o0oO0O_advance =100 #line:2676
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2678
        one_oO0O0O0O0O0O0O0O01 =OOOOOOOOOO0OO00O0 .gettime (OO00000o01 )#line:2679
        one_oO0O0O0O0O0O0O0O02 =OOOOOOOOOO0OO00O0 .gettime (OO00000o02 )#line:2680
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOOOOOOOOO0OO00O0 .gettime (ooo0O0o0oO0O_time1 )#line:2681
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOOOOOOOOO0OO00O0 .gettime (ooo0O0o0oO0O_time2 )#line:2682
    def Strategy_save (O0OOOOO0OOO0O0OO0 ,O0OOOOO00O0OOO0OO ):#line:2685
        OOOOO00O0O0O0O00O =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:2687
        if OOOOO00O0O0O0O00O .ShowModal ()==wx .ID_OK :#line:2688
            O0OO0OO000O000O00 =OOOOO00O0O0O0O00O .GetValue ()#line:2689
            if O0OO0OO000O000O00 :#line:2690
                O0000OO0OOO000OOO =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:2691
                if O0000OO0OOO000OOO ==wx .ID_OK :#line:2692
                    O0000OO0OOO000OOO .Destroy ()#line:2693
                    OOOOO00O0O0O0O00O .Destroy ()#line:2694
                O0OOOOO0OOO0O0OO0 .save (O0OO0OO000O000O00 )#line:2695
            else :#line:2696
                O0000OO0OOO000OOO =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:2697
                if O0000OO0OOO000OOO ==wx .ID_OK :#line:2698
                    O0000OO0OOO000OOO .Destroy ()#line:2699
                    OOOOO00O0O0O0O00O .Destroy ()#line:2700
    def save (OOO0O00O0000O0OOO ,O0000O0000000OOO0 ):#line:2702
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2703
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2704
        global osl ,e_on ,enter_on #line:2705
        if OOO0O00O0000O0OOO .select_stractagy .GetSelection ()==2 :#line:2707
            O0O00OOO00O0OO0O0 =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:2708
            if O0O00OOO00O0OO0O0 ==wx .ID_OK :#line:2709
                O0O00OOO00O0OO0O0 .Destroy ()#line:2710
        elif OOO0O00O0000O0OOO .select_stractagy .GetSelection ()==0 :#line:2711
            osl [0 ]=0 #line:2712
            osl [1 ]=OO00000o01 #line:2713
            osl [2 ]=OO00000o02 #line:2714
            osl [3 ]=one_diff #line:2715
            osl [4 ]=one_delay #line:2716
            osl [5 ]=one_advance #line:2717
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2718
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2719
            osl [8 ]=ooo0O0o0oO0O_diff #line:2720
            osl [9 ]=ooo0O0o0oO0O_delay #line:2721
            osl [10 ]=ooo0O0o0oO0O_advance #line:2722
            osl [11 ]=e_on #line:2723
            osl [12 ]=enter_on #line:2724
        elif OOO0O00O0000O0OOO .select_stractagy .GetSelection ()==1 :#line:2725
            osl [0 ]=1 #line:2726
            osl [0 ]=1 #line:2727
            osl [1 ]=OO00000o01 #line:2728
            osl [2 ]=OO00000o02 #line:2729
            osl [3 ]=one_diff #line:2730
            osl [4 ]=one_delay #line:2731
            osl [5 ]=one_advance #line:2732
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2733
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2734
            osl [8 ]=ooo0O0o0oO0O_diff #line:2735
            osl [9 ]=ooo0O0o0oO0O_delay #line:2736
            osl [10 ]=ooo0O0o0oO0O_advance #line:2737
            osl [11 ]=e_on #line:2738
            osl [12 ]=enter_on #line:2739
        with open ('%s.ghjo0o0o0o0'%O0000O0000000OOO0 ,'wb')as OO0O00O00OOO0OOOO :#line:2740
            pickle .dump (osl ,OO0O00O00OOO0OOOO )#line:2741
    def Strategy_load (OO00O0O0O00OO00O0 ,OO00OOOOO000OOO0O ):#line:2756
        import os as OO0OOO000OO00OO0O #line:2757
        O0OOO00O00O0OOO0O =OO0OOO000OO00OO0O .getcwd ()#line:2758
        OOO00OO00OO00O00O =OO00O0O0O00OO00O0 .findfiles (O0OOO00O00O0OOO0O )#line:2759
        if OOO00OO00OO00O00O :#line:2760
            OO0O00O00O00O0000 =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =OOO00OO00OO00O00O )#line:2762
            if OO0O00O00O00O0000 .ShowModal ()==wx .ID_OK :#line:2763
                O0OOO00O00O0OOO0O =OO0O00O00O00O0000 .GetStringSelection ()#line:2764
                OOO00OO00OOOO0OO0 =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:2765
                if OOO00OO00OOOO0OO0 .ShowModal ()==wx .ID_OK :#line:2766
                    OOO00OO00OOOO0OO0 .Destroy ()#line:2767
                OO00O0O0O00OO00O0 .load (O0OOO00O00O0OOO0O )#line:2768
            print ("载入")#line:2769
            OO0O00O00O00O0000 .Destroy ()#line:2770
        else :#line:2771
            OOO00OO00OOOO0OO0 =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:2772
            if OOO00OO00OOOO0OO0 ==wx .ID_OK :#line:2773
                OOO00OO00OOOO0OO0 .Destroy ()#line:2774
                OO0O00O00O00O0000 .Destroy ()#line:2775
    def load (O00OOOO0OO00O00O0 ,OO00O00OO0OOOO00O ):#line:2777
        global osl ,e_on ,enter_on #line:2778
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2779
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2780
        global ghjo0o0o0o0_on #line:2782
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2783
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2784
        try :#line:2785
            with open (OO00O00OO0OOOO00O ,'rb')as OOO0O0OOOO00000O0 :#line:2786
                osl =pickle .load (OOO0O0OOOO00000O0 )#line:2787
        except :#line:2788
            pass #line:2789
        if osl [0 ]==0 :#line:2790
            O00OOOO0OO00O00O0 .ss_Hide ()#line:2791
            twice =False #line:2794
            ghjo0o0o0o0_on =True #line:2795
            oo0o0O0O0O0_on =True #line:2796
            oOO0O0O0O0O0O0_on =False #line:2797
            oOO0O0O0O0O0O0_num =1 #line:2798
            oOO0O0O0O0O0O0_OK =False #line:2799
            oOO0O0O0O0O0O0_one =False #line:2800
            O00OOOO0OO00O00O0 .select_stractagy .SetSelection (0 )#line:2802
            O00OOOO0OO00O00O0 .jiajia_time .SetValue (osl [1 ])#line:2803
            O00OOOO0OO00O00O0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2804
            O00OOOO0OO00O00O0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2805
            O00OOOO0OO00O00O0 .yanchi_time .SetValue (osl [4 ])#line:2806
            if osl [5 ]==100 :#line:2807
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2808
            elif osl [5 ]==200 :#line:2809
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2810
            else :#line:2811
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2812
            OO00000o01 =osl [1 ]#line:2814
            OO00000o02 =osl [2 ]#line:2815
            one_diff =osl [3 ]#line:2816
            one_delay =osl [4 ]#line:2817
            one_advance =osl [5 ]#line:2818
            e_on =osl [11 ]#line:2820
            enter_on =osl [12 ]#line:2821
            if e_on :#line:2822
                O00OOOO0OO00O00O0 .sdfsf24324297_choice .SetSelection (0 )#line:2823
            elif enter_on :#line:2824
                O00OOOO0OO00O00O0 .sdfsf24324297_choice .SetSelection (1 )#line:2825
            one_oO0O0O0O0O0O0O0O01 =O00OOOO0OO00O00O0 .gettime (OO00000o01 )#line:2827
            one_oO0O0O0O0O0O0O0O02 =O00OOOO0OO00O00O0 .gettime (OO00000o02 )#line:2828
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00OOOO0OO00O00O0 .gettime (ooo0O0o0oO0O_time1 )#line:2829
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00OOOO0OO00O00O0 .gettime (ooo0O0o0oO0O_time2 )#line:2830
        elif osl [0 ]==1 :#line:2832
            ghjo0o0o0o0_on =True #line:2833
            twice =True #line:2834
            oo0o0O0O0O0_on =True #line:2835
            oOO0O0O0O0O0O0_on =False #line:2836
            oOO0O0O0O0O0O0_num =1 #line:2837
            oOO0O0O0O0O0O0_OK =False #line:2838
            oOO0O0O0O0O0O0_one =False #line:2839
            O00OOOO0OO00O00O0 .ss_Shown ()#line:2840
            O00OOOO0OO00O00O0 .select_stractagy .SetSelection (1 )#line:2841
            O00OOOO0OO00O00O0 .jiajia_time .SetValue (osl [1 ])#line:2842
            O00OOOO0OO00O00O0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2843
            O00OOOO0OO00O00O0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2844
            O00OOOO0OO00O00O0 .yanchi_time .SetValue (osl [4 ])#line:2845
            if osl [5 ]==100 :#line:2846
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2847
            elif osl [5 ]==200 :#line:2848
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2849
            else :#line:2850
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2851
            O00OOOO0OO00O00O0 .jiajia_time2 .SetValue (osl [6 ])#line:2852
            O00OOOO0OO00O00O0 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:2853
            O00OOOO0OO00O00O0 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:2854
            O00OOOO0OO00O00O0 .yanchi_time2 .SetValue (osl [9 ])#line:2855
            if osl [10 ]==100 :#line:2856
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2857
            elif osl [10 ]==200 :#line:2858
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:2859
            else :#line:2860
                O00OOOO0OO00O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:2861
            OO00000o01 =osl [1 ]#line:2864
            OO00000o02 =osl [2 ]#line:2865
            one_diff =osl [3 ]#line:2866
            one_delay =osl [4 ]#line:2867
            one_advance =osl [5 ]#line:2868
            ooo0O0o0oO0O_time1 =osl [6 ]#line:2870
            ooo0O0o0oO0O_time2 =osl [7 ]#line:2871
            ooo0O0o0oO0O_diff =osl [8 ]#line:2872
            ooo0O0o0oO0O_delay =osl [9 ]#line:2873
            ooo0O0o0oO0O_advance =osl [10 ]#line:2874
            e_on =osl [11 ]#line:2876
            enter_on =osl [12 ]#line:2877
            if e_on :#line:2878
                O00OOOO0OO00O00O0 .sdfsf24324297_choice .SetSelection (0 )#line:2879
            elif enter_on :#line:2880
                O00OOOO0OO00O00O0 .sdfsf24324297_choice .SetSelection (1 )#line:2881
            one_oO0O0O0O0O0O0O0O01 =O00OOOO0OO00O00O0 .gettime (OO00000o01 )#line:2883
            one_oO0O0O0O0O0O0O0O02 =O00OOOO0OO00O00O0 .gettime (OO00000o02 )#line:2884
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00OOOO0OO00O00O0 .gettime (ooo0O0o0oO0O_time1 )#line:2885
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00OOOO0OO00O00O0 .gettime (ooo0O0o0oO0O_time2 )#line:2886
    def findfiles (OOOOOO00OO00OO000 ,O00000OOO00OO00O0 ):#line:2888
        OOOO0O0O0O00O00O0 =[]#line:2889
        for OO0000O0000O0OO00 ,O0OO000OOO000O0O0 ,OO0000OO0OOOOOOOO in os .walk (O00000OOO00OO00O0 ):#line:2890
            for O00O00000O000O0OO in OO0000OO0OOOOOOOO :#line:2891
                if os .path .splitext (O00O00000O000O0OO )[1 ]=='.ghjo0o0o0o0':#line:2892
                    OOOO0O0O0O00O00O0 .append (os .path .join (OO0000O0000O0OO00 ,O00O00000O000O0OO ))#line:2893
        return OOOO0O0O0O00O00O0 #line:2894
    def Save_info (O000O00O00OOO00O0 ,OO00O000O0O0OOO0O ):#line:2896
        pass #line:2897
    def changetime (O0000OOO0OOOOO0O0 ,O000OOOO0OO0OOO00 ):#line:2902
        O0OOOOO00OOOOOOOO =time .mktime (time .strptime (O000OOOO0OO0OOO00 ,'%Y-%m-%d %H:%M:%S'))#line:2903
        return O0OOOOO00OOOOOOOO #line:2904
    def get_nowtime (O00OOO0000OO000O0 ):#line:2907
        O00O00OO0OO0000O0 =time .time ()#line:2908
        O0O00O00OO000O000 =time .strftime ('%Y-%m-%d',time .localtime (O00O00OO0OO0000O0 ))#line:2909
        return O0O00O00OO000O000 #line:2910
    def gettime (OO00O0O0OOO00O000 ,OOO0O0O0000OOO0O0 ):#line:2913
        O00OOOO0O0O000000 =OO00O0O0OOO00O000 .get_nowtime ()#line:2914
        O0OO00000OO0OOOOO =O00OOOO0O0O000000 +' 11:29:'+str (int (OOO0O0O0000OOO0O0 ))#line:2915
        OO0OOOO00OO00O000 =OO00O0O0OOO00O000 .changetime (O0OO00000OO0OOOOO )+float (OOO0O0O0000OOO0O0 )-int (OOO0O0O0000OOO0O0 )#line:2916
        return OO0OOOO00OO00O000 #line:2917
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:2920
    def __init__ (OO000O00OO0OOO000 ,OO0OO0O00O00OO0O0 ):#line:2921
        wx .Window .__init__ (OO000O00OO0OOO000 ,OO0OO0O00O00OO0O0 ,size =Timesize )#line:2922
        OO000O00OO0OOO000 .Bind (wx .EVT_PAINT ,OO000O00OO0OOO000 .OnPaint )#line:2923
        OO000O00OO0OOO000 .timer =wx .Timer (OO000O00OO0OOO000 )#line:2924
        OO000O00OO0OOO000 .Bind (wx .EVT_TIMER ,OO000O00OO0OOO000 .OnTimer ,OO000O00OO0OOO000 .timer )#line:2925
        OO000O00OO0OOO000 .timer .Start (100 )#line:2926
    def Draw (O0OO0O00O0O0O0OOO ,OOO000OO0O000OO0O ):#line:2928
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2929
        O000OO000000OOOOO =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2930
        OOOO00000OOO0OO0O ,OO000OOO00OO0O00O =O0OO0O00O0O0O0OOO .GetClientSize ()#line:2931
        OOO000OO0O000OO0O .SetBackground (wx .Brush (O0OO0O00O0O0O0OOO .GetBackgroundColour ()))#line:2932
        OOO000OO0O000OO0O .Clear ()#line:2933
        OOO000OO0O000OO0O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2934
        OOOO0OOOO00OO0OOO ,O00OO00OO0000O0OO =OOO000OO0O000OO0O .GetTextExtent (O000OO000000OOOOO )#line:2935
        OOO000OO0O000OO0O .DrawText (O000OO000000OOOOO ,(OOOO00000OOO0OO0O -OOOO0OOOO00OO0OOO )/2 ,(OO000OOO00OO0O00O )/2 -O00OO00OO0000O0OO /2 )#line:2936
    def Modify (OOOOOOOO00OOO0O0O ,O0O0O00OOOOOO0OOO ):#line:2938
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2939
        OOOO0O0OO000OO000 =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2940
        O0OO0O0000O0O0OOO ,O0000OO0O000O0OOO =OOOOOOOO00OOO0O0O .GetClientSize ()#line:2941
        O0O0O00OOOOOO0OOO .SetBackground (wx .Brush (OOOOOOOO00OOO0O0O .GetBackgroundColour ()))#line:2942
        O0O0O00OOOOOO0OOO .Clear ()#line:2943
        O0O0O00OOOOOO0OOO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2944
        OO000OOOO0OO0O0OO ,OO00O000O0O00O0O0 =O0O0O00OOOOOO0OOO .GetTextExtent (OOOO0O0OO000OO000 )#line:2945
        O0O0O00OOOOOO0OOO .DrawText (OOOO0O0OO000OO000 ,(O0OO0O0000O0O0OOO -OO000OOOO0OO0O0OO )/2 ,(O0000OO0O000O0OOO )/2 -OO00O000O0O00O0O0 /2 )#line:2946
    def OnTimer (O00000OO0OO0O0000 ,OO0O0OOOO00OO0O00 ):#line:2948
        O0000OO0O00O000O0 =wx .BufferedDC (wx .ClientDC (O00000OO0OO0O0000 ))#line:2949
        O00000OO0OO0O0000 .Modify (O0000OO0O00O000O0 )#line:2950
    def OnPaint (OOOOOO00OO0OOO0O0 ,O00O00OO0000O0000 ):#line:2952
        OOOOOOOO0O00OOO0O =wx .BufferedPaintDC (OOOOOO00OO0OOO0O0 )#line:2953
        OOOOOO00OO0OOO0O0 .Draw (OOOOOOOO0O00OOO0O )#line:2954
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:2956
    def __init__ (O0O0OOOOO00OOOO0O ):#line:2957
         wx .Frame .__init__ (O0O0OOOOO00OOOO0O ,None ,title ="wx.Timer",size =(200 ,50 ),pos =(300 ,300 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2959
         Lowestzxco0o0o0o0Window (O0O0OOOOO00OOOO0O )#line:2962
import string #line:2980
import wx .lib .agw .hyperlink as hyperlink #line:2981
class LoginFrame (wx .Frame ):#line:2982
    def __init__ (OO0O0O0OO0O0OO000 ,OOOO0OOO000O00OO0 ,OO0OO00O0OO0000OO ,OO00O00O00OOO0OOO ):#line:2983
        wx .Frame .__init__ (OO0O0O0OO0O0OO000 ,None ,-1 ,OOOO0OOO000O00OO0 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:2984
        OO0O0O0OO0O0OO000 .Bind (wx .EVT_CLOSE ,OO0O0O0OO0O0OO000 .OnClose )#line:2985
        OO0O0O0OO0O0OO000 .panel =wx .Panel (OO0O0O0OO0O0OO000 ,size =(300 ,220 ))#line:2986
        OO0O0O0OO0O0OO000 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:2987
        OO0O0O0OO0O0OO000 .SetIcon (OO0O0O0OO0O0OO000 .icon )#line:2988
        OO0O0O0OO0O0OO000 .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3001
        OO0O0O0OO0O0OO000 .welcomelabel =wx .StaticText (OO0O0O0OO0O0OO000 .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3002
        OO0O0O0OO0O0OO000 .sizer_v1 .Add (OO0O0O0OO0O0OO000 .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3003
        OO0O0O0OO0O0OO000 .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3006
        OO0O0O0OO0O0OO000 .userlabel =wx .StaticText (OO0O0O0OO0O0OO000 .panel ,-1 ,label ="账号")#line:3007
        OO0O0O0OO0O0OO000 .userText =wx .TextCtrl (OO0O0O0OO0O0OO000 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3009
        OO0O0O0OO0O0OO000 .userbox .Add (OO0O0O0OO0O0OO000 .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3010
        OO0O0O0OO0O0OO000 .userbox .Add (OO0O0O0OO0O0OO000 .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3011
        OO0O0O0OO0O0OO000 .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3013
        OO0O0O0OO0O0OO000 .passlabel =wx .StaticText (OO0O0O0OO0O0OO000 .panel ,-1 ,label ="密码")#line:3014
        OO0O0O0OO0O0OO000 .passText =wx .TextCtrl (OO0O0O0OO0O0OO000 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3016
        OO0O0O0OO0O0OO000 .passbox .Add (OO0O0O0OO0O0OO000 .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3017
        OO0O0O0OO0O0OO000 .passbox .Add (OO0O0O0OO0O0OO000 .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3018
        if OO0OO00O0OO0000OO :#line:3019
            OO0O0O0OO0O0OO000 .userText .SetValue (OO0OO00O0OO0000OO )#line:3020
        if OO00O00O00OOO0OOO :#line:3021
            OO0O0O0OO0O0OO000 .passText .SetValue (OO00O00O00OOO0OOO )#line:3022
        OO0O0O0OO0O0OO000 .sizer_v1 .Add (OO0O0O0OO0O0OO000 .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3023
        OO0O0O0OO0O0OO000 .sizer_v1 .Add (OO0O0O0OO0O0OO000 .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3024
        OO0O0O0OO0O0OO000 .Bind (wx .EVT_TEXT_ENTER ,OO0O0O0OO0O0OO000 .OnLogin ,OO0O0O0OO0O0OO000 .userText )#line:3026
        OO0O0O0OO0O0OO000 .Bind (wx .EVT_TEXT_ENTER ,OO0O0O0OO0O0OO000 .OnLogin ,OO0O0O0OO0O0OO000 .passText )#line:3027
        OO0O0O0OO0O0OO000 .o0sdofsfo0sodf0so0btn =wx .Button (OO0O0O0OO0O0OO000 .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3029
        OO0O0O0OO0O0OO000 .loginbtn =wx .Button (OO0O0O0OO0O0OO000 .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3030
        OO0O0O0OO0O0OO000 .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3031
        OO0O0O0OO0O0OO000 .btnSizer .Add (OO0O0O0OO0O0OO000 .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3032
        OO0O0O0OO0O0OO000 .btnSizer .Add (OO0O0O0OO0O0OO000 .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3033
        OO0O0O0OO0O0OO000 .sizer_v1 .Add (OO0O0O0OO0O0OO000 .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3034
        OO0O0O0OO0O0OO000 .loginbtn .Bind (wx .EVT_BUTTON ,OO0O0O0OO0O0OO000 .OnLogin ,OO0O0O0OO0O0OO000 .loginbtn )#line:3035
        OO0O0O0OO0O0OO000 .purchaselink =hyperlink .HyperLinkCtrl (OO0O0O0OO0O0OO000 .panel ,-1 ,u"购买账号")#line:3037
        OO0O0O0OO0O0OO000 .purchaselink .UnsetToolTip ()#line:3038
        OO0O0O0OO0O0OO000 .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OO0O0O0OO0O0OO000 .Purchase )#line:3039
        OO0O0O0OO0O0OO000 .purchaselink .AutoBrowse (False )#line:3040
        OO0O0O0OO0O0OO000 .purchaselink .EnableRollover (True )#line:3041
        OO0O0O0OO0O0OO000 .purchaselink .SetUnderlines (False ,False ,True )#line:3042
        OO0O0O0OO0O0OO000 .purchaselink .OpenInSameWindow (True )#line:3043
        OO0O0O0OO0O0OO000 .purchaselink .UpdateLink ()#line:3044
        OO0O0O0OO0O0OO000 .helplink =hyperlink .HyperLinkCtrl (OO0O0O0OO0O0OO000 .panel ,-1 ,u"查看帮助")#line:3046
        OO0O0O0OO0O0OO000 .helplink .UnsetToolTip ()#line:3047
        OO0O0O0OO0O0OO000 .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OO0O0O0OO0O0OO000 .Purchase )#line:3048
        OO0O0O0OO0O0OO000 .helplink .AutoBrowse (False )#line:3049
        OO0O0O0OO0O0OO000 .helplink .EnableRollover (True )#line:3050
        OO0O0O0OO0O0OO000 .helplink .SetUnderlines (False ,False ,True )#line:3051
        OO0O0O0OO0O0OO000 .helplink .OpenInSameWindow (True )#line:3052
        OO0O0O0OO0O0OO000 .helplink .UpdateLink ()#line:3053
        OO0O0O0OO0O0OO000 .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3055
        OO0O0O0OO0O0OO000 .linkbox .Add (OO0O0O0OO0O0OO000 .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3056
        OO0O0O0OO0O0OO000 .linkbox .Add (OO0O0O0OO0O0OO000 .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3057
        OO0O0O0OO0O0OO000 .sizer_v1 .Add (OO0O0O0OO0O0OO000 .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3058
        OO0O0O0OO0O0OO000 .SetSizer (OO0O0O0OO0O0OO000 .sizer_v1 )#line:3060
        OO0O0O0OO0O0OO000 .Center ()#line:3061
        pub .subscribe (OO0O0O0OO0O0OO000 .connect_success ,"connect")#line:3063
        OO0O0O0OO0O0OO000 .hashthread =HashThread ()#line:3066
    def connect_success (O000OO0O0OO00000O ):#line:3068
        O000OO0O0OO00000O .loginbtn .Enable ()#line:3069
        global login_result #line:3070
        if login_result =='login success':#line:3071
            O000OO0O0OO00000O .Destroy ()#line:3072
            O000OO0O0OO00000O .topframe =TopFrame ('沪牌第一枪',version )#line:3073
            O000OO0O0OO00000O .topframe .Show (True )#line:3074
        elif login_result =='net error':#line:3076
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3077
        elif login_result =='repeat':#line:3078
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3079
        elif login_result =='wrong account':#line:3080
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3081
        elif login_result =='wrong password':#line:3082
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3083
        else :#line:3084
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3085
    def OnEraseBack (OOO00OO0O000OO0O0 ,OOOOOOO00OOOO0O00 ):#line:3088
        OOOOOOO0O00OO0OOO =OOOOOOO00OOOO0O00 .GetDC ()#line:3089
        if not OOOOOOO0O00OO0OOO :#line:3090
            OOOOOOO0O00OO0OOO =wx .ClientDC (OOO00OO0O000OO0O0 )#line:3091
            OOO000OO0OO0O0OO0 =OOO00OO0O000OO0O0 .GetUpdateRegion ().GetBox ()#line:3092
            OOOOOOO0O00OO0OOO .SetClippingRect (OOO000OO0OO0O0OO0 )#line:3093
        OOOOOOO0O00OO0OOO .Clear ()#line:3094
        O0000OO0O00000O00 =wx .Bitmap ("blue.jpg")#line:3095
        OOOOOOO0O00OO0OOO .DrawBitmap (O0000OO0O00000O00 ,0 ,0 )#line:3096
    def OnClose (O0OO0O000O0O0OOOO ,OOOOO000OOOO0OO0O ):#line:3098
        OOOOO000OOOO0OO0O .Skip ()#line:3099
        sys .exit (None )#line:3100
    def OnLogin (O000OOOO000OOO0O0 ,OO0OO000OO0OO0O00 ):#line:3108
        global Username ,Password #line:3109
        O00O00O0O0O0000O0 =O000OOOO000OOO0O0 .userText .GetValue ()#line:3110
        O0O00O00O00O0O00O =O000OOOO000OOO0O0 .passText .GetValue ()#line:3111
        if O00O00O0O0O0000O0 =="":#line:3112
            wx .MessageBox ('请输入用户名！')#line:3113
            O000OOOO000OOO0O0 .userText .SetFocus ()#line:3114
        elif O0O00O00O00O0O00O =="":#line:3115
            wx .MessageBox ('请输入密码！')#line:3116
            O000OOOO000OOO0O0 .passText .SetFocus ()#line:3117
        else :#line:3119
            Username =O00O00O0O0O0000O0 #line:3120
            Password =O0O00O00O00O0O00O #line:3121
            O000OOOO000OOO0O0 .loginthread =LoginThread ()#line:3122
            O0OO0OOO0O0O00O00 =[O00O00O0O0O0000O0 ,O0O00O00O00O0O00O ]#line:3123
            with open ('your.name','wb')as O00O0000OO00OOOOO :#line:3124
                pickle .dump (O0OO0OOO0O0O00O00 ,O00O0000OO00OOOOO )#line:3125
            OO0OO000OO0OO0O00 .GetEventObject ().Disable ()#line:3127
    def Purchase (O000OO0000OO0OOOO ,O0OO000O0O00OOOOO ):#line:3129
        print ("购买")#line:3130
class UserValidator (wx .Validator ):#line:3134
    ""#line:3135
    def __init__ (O00O0O00OO00OOOOO ,OO0O0000OOOO00OO0 ):#line:3137
        wx .Validator .__init__ (O00O0O00OO00OOOOO )#line:3138
        O00O0O00OO00OOOOO .flag =OO0O0000OOOO00OO0 #line:3139
        O00O0O00OO00OOOOO .Bind (wx .EVT_CHAR ,O00O0O00OO00OOOOO .OnChar )#line:3140
    def Clone (OOO0OO0OO0000000O ):#line:3143
        ""#line:3144
        return UserValidator (OOO0OO0OO0000000O .flag )#line:3145
    def Validate (OOOO0OOOO0OO000OO ,O00O0OOO00OO0O00O ):#line:3148
        return True #line:3149
    def TransferToWindow (OO0000OO000O000O0 ):#line:3152
        return True #line:3153
    def TransferFromWindow (O000OO0000O0000O0 ):#line:3156
        return True #line:3157
    def OnChar (OO0OOOOOO00OOOOOO ,O000O0OOOO00O0O0O ):#line:3160
        pass #line:3161
class PassValidator (wx .Validator ):#line:3175
    ""#line:3176
    def __init__ (OOO000OO0OOOO0OO0 ):#line:3179
        wx .Validator .__init__ (OOO000OO0OOOO0OO0 )#line:3180
        OOO000OO0OOOO0OO0 .Bind (wx .EVT_CHAR ,OOO000OO0OOOO0OO0 .OnChar )#line:3181
    def Clone (OO0O000O0OOOO00OO ):#line:3184
        ""#line:3185
        return PassValidator ()#line:3186
    def Validate (O0OO0000O0000O0O0 ,OO0OO000O00000000 ):#line:3189
        return True #line:3190
    def TransferToWindow (OO000OO0O00OOOO00 ):#line:3193
        return True #line:3194
    def TransferFromWindow (OOO0000OOOOO0O00O ):#line:3197
        return True #line:3198
    def OnChar (O0O000O0OO00O0O0O ,O0O0000OO0O0O0O0O ):#line:3201
        pass #line:3202
class ConfirmLogin (wx .Frame ):#line:3216
    pass #line:3217
class TimeThread (Thread ):#line:3220
    def __init__ (O0O0000O00OOOO0OO ):#line:3221
        ""#line:3222
        Thread .__init__ (O0O0000O00OOOO0OO )#line:3223
        O0O0000O00OOOO0OO .setDaemon (True )#line:3224
        O0O0000O00OOOO0OO .start ()#line:3225
    def run (O00OO0O00OOO00000 ):#line:3227
        ""#line:3228
        global a_time #line:3230
        for O00O00O00O00O0O00 in range (1000000 ):#line:3231
            OO0O0OOO0OOO000OO =time .clock ()#line:3232
            time .sleep (0.1 )#line:3233
            O000OOO00O00OOO00 =time .clock ()#line:3234
            a_time +=O000OOO00O00OOO00 -OO0O0OOO0OOO000OO #line:3235
class HashThread (Thread ):#line:3266
    def __init__ (OO00O0O0OO000OOO0 ):#line:3267
        ""#line:3268
        Thread .__init__ (OO00O0O0OO000OOO0 )#line:3269
        OO00O0O0OO000OOO0 .setDaemon (True )#line:3270
        OO00O0O0OO000OOO0 .start ()#line:3271
    def run (O0OO00OOO00OOOO0O ):#line:3273
        ""#line:3274
        Create_hash ()#line:3276
class findposThread (Thread ):#line:3282
    def __init__ (OO00OOO00O0O00O00 ):#line:3283
        Thread .__init__ (OO00OOO00O0O00O00 )#line:3284
        OO00OOO00O0O00O00 .setDaemon (True )#line:3285
        OO00OOO00O0O00O00 .start ()#line:3286
    def run (O00O0OO0OOOOO00OO ):#line:3288
        findpos ()#line:3289
class sdfsf24324297Thread (Thread ):#line:3292
    def __init__ (O0OOO0OO0O00OO0O0 ):#line:3293
        Thread .__init__ (O0OOO0OO0O00OO0O0 )#line:3294
        O0OOO0OO0O00OO0O0 .setDaemon (True )#line:3295
        O0OOO0OO0O00OO0O0 .start ()#line:3296
    def run (OOOOOO00000000OO0 ):#line:3298
        global sdfsf24324297_need ,sdfsf24324297_on #line:3299
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3300
        for OO000000OOO00O0O0 in range (100 ):#line:3301
            wx .Sleep (0.1 )#line:3302
            if sdfsf24324297_need :#line:3304
                print ("开启查找")#line:3305
                findsdfsf24324297 ()#line:3306
                if sdfsf24324297_on :#line:3307
                    TopFrame .OnClick_sdfsf24324297 ()#line:3308
                    sdfsf24324297_need =False #line:3309
                    sdfsf24324297_on =False #line:3310
                    sdfsf24324297_one =False #line:3311
                    oo0o0O0O0O0_on =True #line:3312
        sdfsf24324297_one =False #line:3313
class uioo0o000ooThread (Thread ):#line:3315
    def __init__ (OOOOOOOO00O00OO0O ):#line:3316
        Thread .__init__ (OOOOOOOO00O00OO0O )#line:3317
        OOOOOOOO00O00OO0O .setDaemon (True )#line:3318
        OOOOOOOO00O00OO0O .start ()#line:3319
    def run (O0O0O0O0OO000OO0O ):#line:3321
        global sdfsf24324297_need ,sdfsf24324297_on #line:3322
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3323
        for OO0OO0OO0000OOO00 in range (50 ):#line:3324
            if uioo0o000oo_need :#line:3325
                finduioo0o000oo ()#line:3326
                if uioo0o000oo_on :#line:3327
                    TopFrame .OnClick_Shuaxin ()#line:3328
                    uioo0o000oo_on =False #line:3329
                    uioo0o000oo_need =False #line:3330
                    uioo0o000oo_one =False #line:3331
        uioo0o000oo_one =False #line:3332
class LoginThread (Thread ):#line:3337
    def __init__ (OO00000OOO00OOOOO ):#line:3338
        ""#line:3339
        Thread .__init__ (OO00000OOO00OOOOO )#line:3340
        OO00000OOO00OOOOO .setDaemon (True )#line:3341
        OO00000OOO00OOOOO .start ()#line:3342
    def run (OO0000000O00O0OOO ):#line:3344
        global Username ,login_result #line:3346
        login_result =ConfirmUser ()#line:3347
        print (login_result )#line:3348
        logging .info ("%s"%login_result )#line:3349
        wx .CallAfter (pub .sendMessage ,"connect")#line:3350
class controlThread (Thread ):#line:3353
    def __init__ (OOOO000O00OOO0000 ):#line:3354
        ""#line:3355
        Thread .__init__ (OOOO000O00OOO0000 )#line:3356
        OOOO000O00OOO0000 .setDaemon (True )#line:3357
        OOOO000O00OOO0000 .start ()#line:3358
    def run (O0OO00OO0000OO00O ):#line:3361
        wx .Sleep (10 )#line:3362
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3363
class KeepThread (Thread ):#line:3368
    def __init__ (OO0OOO0O00O00OO00 ):#line:3369
        ""#line:3370
        Thread .__init__ (OO0OOO0O00O00OO00 )#line:3371
        OO0OOO0O00O00OO00 .setDaemon (True )#line:3372
        OO0OOO0O00O00OO00 .start ()#line:3373
    def run (O0000OOOOOO00O000 ):#line:3376
        for OOO0O0OO00O0O0OOO in range (1000000 ):#line:3377
            time .sleep (90 )#line:3378
            Keeplogin ()#line:3379
class TijiaoThread (Thread ):#line:3385
    def __init__ (OOO0O0OOOOO0OOOOO ):#line:3386
        ""#line:3387
        Thread .__init__ (OOO0O0OOOOO0OOOOO )#line:3388
        OOO0O0OOOOO0OOOOO .setDaemon (True )#line:3389
        OOO0O0OOOOO0OOOOO .start ()#line:3390
    def run (O0OOO0OO0O00O00OO ):#line:3393
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3394
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3395
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3396
        for O0O0O00O0OO000O0O in range (10000000 ):#line:3397
            time .sleep (0.1 )#line:3398
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3402
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3404
                    oOO0O0O0O0O0O0_on =False #line:3405
                    TopFrame .OnClick_Tijiao ()#line:3406
                    oOO0O0O0O0O0O0_on =False #line:3407
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3408
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3409
                    oOO0O0O0O0O0O0_one =True #line:3410
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3411
                    oOO0O0O0O0O0O0_on =False #line:3412
                    TopFrame .OnClick_Tijiao ()#line:3413
                    oOO0O0O0O0O0O0_on =False #line:3414
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3415
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3416
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3417
                    oOO0O0O0O0O0O0_on =False #line:3418
                    oOO0O0O0O0O0O0_on =False #line:3419
                    TopFrame .OnClick_Tijiao ()#line:3420
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3421
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3422
                    oOO0O0O0O0O0O0_one =True #line:3423
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance :#line:3424
                    oOO0O0O0O0O0O0_on =False #line:3425
                    oOO0O0O0O0O0O0_on =False #line:3426
                    TopFrame .OnClick_Tijiao ()#line:3427
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3428
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3429
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3431
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time <=one_oO0O0O0O0O0O0O0O01 +0.2 :#line:3433
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3434
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3435
                    oOO0O0O0O0O0O0_on =True #line:3436
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3437
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3438
                if oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3439
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3440
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3441
                    oOO0O0O0O0O0O0_on =True #line:3442
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3443
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3444
class MoniTijiaoThread (Thread ):#line:3448
    def __init__ (OOOO0O00OO00OO00O ):#line:3449
        ""#line:3450
        Thread .__init__ (OOOO0O00OO00OO00O )#line:3451
        OOOO0O00OO00OO00O .setDaemon (True )#line:3452
        OOOO0O00OO00OO00O .start ()#line:3453
    def run (O0OOOOOO0OO000O00 ):#line:3456
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3457
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3458
        for OOO000OO000OO0OOO in range (10000000 ):#line:3459
            time .sleep (0.1 )#line:3460
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3462
                print (oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK )#line:3463
                print (oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ,oOO0O0O0O0O0O0_one )#line:3464
                print (O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 )#line:3465
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3466
                    TopFrame .OnClick_Tijiao ()#line:3467
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3468
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3469
                    oOO0O0O0O0O0O0_on =False #line:3470
                    oOO0O0O0O0O0O0_one =True #line:3471
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3472
                    TopFrame .OnClick_Tijiao ()#line:3473
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3474
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3475
                    oOO0O0O0O0O0O0_on =False #line:3476
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3477
                    oOO0O0O0O0O0O0_on =False #line:3478
                    TopFrame .OnClick_Tijiao ()#line:3479
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3480
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3481
                    oOO0O0O0O0O0O0_one =True #line:3482
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3483
                    oOO0O0O0O0O0O0_on =False #line:3484
                    TopFrame .OnClick_Tijiao ()#line:3485
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3486
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3487
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3492
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=OO00000o01 +0.2 :#line:3493
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3494
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3496
                    oOO0O0O0O0O0O0_on =True #line:3497
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3498
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3499
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3500
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3501
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3503
                    oOO0O0O0O0O0O0_on =True #line:3504
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3505
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3506
class Infoframe (wx .Frame ):#line:3509
    def __init__ (O00O000OOOO0O0O00 ,OO0O00O0OO0OO0O00 ,OO00OOOO00OOO00O0 ,OO00OOOO00OO00OO0 ):#line:3510
        wx .Frame .__init__ (O00O000OOOO0O0O00 ,None ,-1 ,OO0O00O0OO0OO0O00 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3511
        O00O000OOOO0O0O00 .Bind (wx .EVT_CLOSE ,O00O000OOOO0O0O00 .OnClose )#line:3512
        O00O000OOOO0O0O00 .panel =wx .Panel (O00O000OOOO0O0O00 ,size =(300 ,220 ))#line:3513
        O00O000OOOO0O0O00 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3514
        O00O000OOOO0O0O00 .SetIcon (O00O000OOOO0O0O00 .icon )#line:3515
class SketchApp (wx .App ):#line:3518
    def OnInit (OO0O0000O00O0OOOO ):#line:3519
        try :#line:3530
            with open ("your.name",'rb')as OO0OO0000OO000000 :#line:3531
                O00O00O00O0000000 =pickle .load (OO0OO0000OO000000 )#line:3532
                OO0O0OO0O0O0OOOOO =O00O00O00O0000000 [0 ]#line:3533
                O00O00000OO0OOOOO =O00O00O00O0000000 [1 ]#line:3534
        except :#line:3535
            OO0O0OO0O0O0OOOOO ='123456'#line:3536
            O00O00000OO0OOOOO =0 #line:3537
        OO00O00OOO0OO00O0 =LoginFrame ('沪牌第一枪',OO0O0OO0O0O0OOOOO ,O00O00000OO0OOOOO )#line:3538
        OO00O00OOO0OO00O0 .Show (True )#line:3539
        return True #line:3540
if __name__ =='__main__':#line:3543
    app =SketchApp ()#line:3544
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
