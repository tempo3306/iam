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
zxco0o0o0o0list =[80000 +OOOOO0OO0O0OOO0O0 *100 for OOOOO0OO0O0OOO0O0 in range (200 )]#line:67
IDnumber =0 #line:68
account =0 #line:69
passwd =0 #line:70
import pyautogui as pg #line:74
def Create_hash ():#line:76
    with open ('dick.dl','rb')as OO0O0O0OO0O0000OO :#line:77
        global dick_hash #line:78
        dick_hash =pickle .load (OO0O0O0OO0O0000OO )#line:79
    with open ('cf.btn','rb')as OOO0OO00O0O0OOO00 :#line:80
        global cf_hash #line:81
        cf_hash =pickle .load (OOO0OO00O0O0OOO00 )#line:82
    with open ("target.tkl",'rb')as O0O0OOO0O0O00OOOO :#line:84
        global dick_target #line:85
        dick_target =pickle .load (O0O0OOO0O0O00OOOO )#line:86
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
Oo0o0Oo0o0o0 =[[0 ,0 ]for OOO0OOOO0O000O00O in range (len (P_relative ))]#line:138
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
def Click (O00O00O0O000OOO00 ,O0O00OOOO00OOO0O0 ):#line:370
    O0OO00O000O0000OO =win32gui .GetCursorPos ()#line:371
    O00O00O0O000OOO00 =int (O00O00O0O000OOO00 )#line:372
    O0O00OOOO00OOO0O0 =int (O0O00OOOO00OOO0O0 )#line:373
    win32api .SetCursorPos ((O00O00O0O000OOO00 ,O0O00OOOO00OOO0O0 ))#line:374
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,O00O00O0O000OOO00 ,O0O00OOOO00OOO0O0 ,0 ,0 )#line:375
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,O00O00O0O000OOO00 ,O0O00OOOO00OOO0O0 ,0 ,0 )#line:376
    win32api .SetCursorPos (O0OO00O000O0000OO )#line:377
import win32clipboard #line:380
def Paste ():#line:381
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:383
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:384
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:385
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:386
def setText (OO0O00OOOOO00OO00 ):#line:388
    OO0O00OOOOO00OO00 =OO0O00OOOOO00OO00 .encode ('utf-8')#line:389
    win32clipboard .OpenClipboard ()#line:390
    win32clipboard .EmptyClipboard ()#line:391
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,OO0O00OOOOO00OO00 )#line:392
    win32clipboard .CloseClipboard ()#line:393
def findpos ():#line:396
    O0O0O000O00000OO0 =ImageGrab .grab ().convert ('L')#line:398
    OO00000OO0OOO00O0 =np .asarray (O0O0O000O00000OO0 )#line:399
    global dick_target #line:400
    OO00OOOOO000O0000 =dick_target [2 ]#line:401
    OO00000O0000O0000 ,O0O00O000O0000O00 =OO00OOOOO000O0000 .shape [::-1 ]#line:402
    OO0000O0O0OOOOOO0 =cv2 .matchTemplate (OO00000OO0OOO00O0 ,OO00OOOOO000O0000 ,cv2 .TM_CCOEFF_NORMED )#line:404
    OO00OOOO0OO0O0000 ,OOOO0O000O0OO0OO0 ,O0OO00O0O0OOOO0O0 ,O0OOO000O0OOO0000 =cv2 .minMaxLoc (OO0000O0O0OOOOOO0 )#line:405
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:410
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =O0OOO000O0OOO0000 [0 ]+px_relative #line:411
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =O0OOO000O0OOO0000 [1 ]+py_relative #line:412
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:413
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:414
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:416
    for O00O00O0O0000000O in range (len (Oo0o0Oo0o0o0 )):#line:417
        Oo0o0Oo0o0o0 [O00O00O0O0000000O ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O00O00O0O0000000O ][0 ]#line:418
        Oo0o0Oo0o0o0 [O00O00O0O0000000O ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O00O00O0O0000000O ][1 ]#line:419
    uioo0o000oo_area =[396 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:420
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:421
    global findpos_on #line:423
    findpos_on =False #line:424
def finduioo0o000oo ():#line:426
    global dick_target ,uioo0o000oo_on ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:427
    O0OOOO0OO000000O0 =dick_target [0 ]#line:428
    OOOO00O00O00O000O =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:429
    OOO0O00O00OO0OO0O =np .asarray (OOOO00O00O00O000O )#line:430
    O0O00O0O0O0O000O0 ,O00000O00O00OO0O0 =O0OOOO0OO000000O0 .shape [::-1 ]#line:431
    OO0OOOOO00000O000 =cv2 .matchTemplate (OOO0O00O00OO0OO0O ,O0OOOO0OO000000O0 ,cv2 .TM_CCOEFF_NORMED )#line:432
    OOOOOO00O0OOO0OO0 ,OOO00O00O00000OO0 ,OOO0OOO000O0O00OO ,OOOO0O000O0OOO000 =cv2 .minMaxLoc (OO0OOOOO00000O000 )#line:433
    if OOO00O00O00000OO0 >=0.9 :#line:435
        uioo0o000oo_on =True #line:436
def findsdfsf24324297 ():#line:439
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:440
    O0O00O0O0OOO00O0O =dick_target [1 ]#line:441
    O00OOO00O000O0000 =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:442
    O000000O0O0000000 =np .asarray (O00OOO00O000O0000 )#line:443
    O000OOOO0OOO0O00O ,OO00000O00OOO0OO0 =O0O00O0O0OOO00O0O .shape [::-1 ]#line:444
    O0OOOO00OOO000O0O =cv2 .matchTemplate (O000000O0O0000000 ,O0O00O0O0OOO00O0O ,cv2 .TM_CCOEFF_NORMED )#line:445
    OOO00O0000O000OOO ,OO0000OOO0OO00OO0 ,O00OO0O0OO00O00OO ,OOOOO00O0OO0O00OO =cv2 .minMaxLoc (O0OOOO00OOO000O0O )#line:446
    print (OO0000OOO0OO00OO0 )#line:447
    if OO0000OOO0OO00OO0 >=0.9 :#line:448
        sdfsf24324297_on =True #line:449
SZ =20 #line:453
bin_n =16 #line:454
import numpy as np #line:455
def hog (O0000OOO00OO0OOO0 ):#line:458
    O00O0O0000O00OOO0 =cv2 .Sobel (O0000OOO00OO0OOO0 ,cv2 .CV_32F ,1 ,0 )#line:459
    OO0000000000O0000 =cv2 .Sobel (O0000OOO00OO0OOO0 ,cv2 .CV_32F ,0 ,1 )#line:460
    OO00OOO0O0O00O000 ,O0O0OOO0O000O0O0O =cv2 .cartToPolar (O00O0O0000O00OOO0 ,OO0000000000O0000 )#line:461
    O0000O0O0O00O0O0O =np .int32 (bin_n *O0O0OOO0O000O0O0O /(2 *np .pi ))#line:462
    O000OOOOOO0000OOO =O0000O0O0O00O0O0O [:10 ,:10 ],O0000O0O0O00O0O0O [10 :,:10 ],O0000O0O0O00O0O0O [:10 ,10 :],O0000O0O0O00O0O0O [10 :,10 :]#line:463
    OOOOOOO000OOOO0O0 =OO00OOO0O0O00O000 [:10 ,:10 ],OO00OOO0O0O00O000 [10 :,:10 ],OO00OOO0O0O00O000 [:10 ,10 :],OO00OOO0O0O00O000 [10 :,10 :]#line:464
    O0OO0OOO000000O00 =[np .bincount (O000OO000O0O00OO0 .ravel (),O000OO0O0OO0OO00O .ravel (),bin_n )for O000OO000O0O00OO0 ,O000OO0O0OO0OO00O in zip (O000OOOOOO0000OOO ,OOOOOOO000OOOO0O0 )]#line:465
    O00O000O0OOOO0OO0 =np .hstack (O0OO0OOO000000O00 )#line:466
    return O00O000O0OOOO0OO0 #line:467
def cut (OO0OOOO000000OO0O ):#line:471
    OO00OOO0O0O000OOO ,O00000OO0O0OOOOOO =cv2 .threshold (OO0OOOO000000OO0O ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:472
    O0O0OO0O0O0O0O0OO ,O0O0O00OO00O0O000 ,O0O00OOOOOO000O0O =cv2 .findContours (O00000OO0O0OOOOOO ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:474
    O0000O00O0OO00OOO =[]#line:475
    OO000OOOOO00OOOOO =[]#line:476
    for OO0000O0O0O00OOOO in range (len (O0O0O00OO00O0O000 )):#line:477
        OOO0O0OOOOO0O0O0O =O0O0O00OO00O0O000 [OO0000O0O0O00OOOO ]#line:478
        OO0000OOO000OO0OO ,O000000000O0OOO00 ,OO00000OOO00OOOO0 ,O0OOOOOOO00OO00O0 =cv2 .boundingRect (OOO0O0OOOOO0O0O0O )#line:479
        OO000OOOOO00OOOOO .append ([OO0000OOO000OO0OO ,O000000000O0OOO00 ,OO00000OOO00OOOO0 ,O0OOOOOOO00OO00O0 ])#line:481
    OO000OOOOO00OOOOO =sorted (OO000OOOOO00OOOOO )#line:483
    for OO0000O0O0O00OOOO in range (len (O0O0O00OO00O0O000 )):#line:484
        OO0000OOO000OO0OO ,O000000000O0OOO00 ,OO00000OOO00OOOO0 ,O0OOOOOOO00OO00O0 =OO000OOOOO00OOOOO [OO0000O0O0O00OOOO ]#line:485
        O0000O00O0OO00OOO .append (O0O0OO0O0O0O0O0OO [O000000000O0OOO00 :O000000000O0OOO00 +O0OOOOOOO00OO00O0 ,OO0000OOO000OO0OO :OO0000OOO000OO0OO +OO00000OOO00OOOO0 ])#line:486
    return O0000O00O0OO00OOO #line:487
def readpic (OO00O0OO00000O00O ):#line:489
    try :#line:490
        O00OO0O0OO00O0OO0 =cv2 .ml .SVM_load ('maindata.xml')#line:491
        O0OOO0O0OO00OO000 =cut (OO00O0OO00000O00O )#line:492
        O0OOO0O0OO00OO000 =list (map (hog ,O0OOO0O0OO00OO000 ))#line:493
        O0OOO0O0OO00OO000 =np .float32 (O0OOO0O0OO00OO000 ).reshape (-1 ,64 )#line:494
        O0OO0OOOO00000000 =O00OO0O0OO00O0OO0 .predict (O0OOO0O0OO00OO000 )#line:495
        O0OO0OOOO00000000 =O0OO0OOOO00000000 [1 ].reshape (-1 ).astype (int ).astype (str )#line:496
        O00O00OO00OO00OO0 ="".join (list (O0OO0OOOO00000000 ))#line:497
        return O00O00OO00OO00OO0 #line:498
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
    OOO0O00OO0OOO0OO0 =host_ali #line:540
    OOO00O000OO000000 =8080 #line:543
    O00O0OOO0O0OOO000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:545
    try :#line:547
        O00O0OOO0O0OOO000 .connect ((OOO0O00OO0OOO0OO0 ,OOO00O000OO000000 ))#line:548
    except socket .gaierror as OOOO0OOOOO0O0000O :#line:549
        logging .error ('连接失败 %s'%OOOO0OOOOO0O0000O )#line:550
        logging .error ("Address-related error connecting to server: %s"%OOOO0OOOOO0O0000O )#line:551
        return 'net error'#line:552
    except socket .error as OOOO0OOOOO0O0000O :#line:554
        logging .error ('连接失败 %s'%OOOO0OOOOO0O0000O )#line:555
        logging .error ("Connection error: %s"%OOOO0OOOOO0O0000O )#line:556
        return 'net error'#line:557
    OO00O000OO00OO000 =['login',Username ,Password ]#line:561
    OO00O000OO00OO000 =json .dumps (OO00O000OO00OO000 )#line:562
    OO00O000OO00OO000 =bytes (OO00O000OO00OO000 ,encoding ="utf-8")#line:563
    logging .info ('发送信息 %s'%str (OO00O000OO00OO000 ,encoding ="utf-8"))#line:564
    O00O0OOO0O0OOO000 .send (OO00O000OO00OO000 )#line:565
    O00O0OOO0O0OOO000 .shutdown (1 )#line:567
    logging .info ("Submit Complete")#line:568
    print ("Submit Complete")#line:569
    try :#line:570
        OO0OO00000OO000O0 =O00O0OOO0O0OOO000 .recv (1024 )#line:572
        print (OO0OO00000OO000O0 )#line:573
        OO0OO00000OO000O0 =str (OO0OO00000OO000O0 ,encoding ="utf-8")#line:574
        OO0OO00000OO000O0 =json .loads (OO0OO00000OO000O0 )#line:575
        print (OO0OO00000OO000O0 )#line:576
        O0OOO0O0000OOO0O0 =OO0OO00000OO000O0 [0 ]#line:577
        if O0OOO0O0000OOO0O0 =='success':#line:578
            logging .info ('登录成功 %s'%O0OOO0O0000OOO0O0 )#line:579
            global url2 #line:580
            url2 =OO0OO00000OO000O0 [1 ]#line:581
            return 'login success'#line:582
        elif O0OOO0O0000OOO0O0 =='wrong password':#line:583
            logging .warning ('密码错误 %s'%O0OOO0O0000OOO0O0 )#line:584
            return 'wrong password'#line:585
        elif O0OOO0O0000OOO0O0 =="wrong account":#line:586
            logging .warning ('账号错误 %s'%O0OOO0O0000OOO0O0 )#line:587
            return 'wrong account'#line:588
        elif O0OOO0O0000OOO0O0 =='repeat':#line:589
            logging .warning ('账号错误 %s'%O0OOO0O0000OOO0O0 )#line:590
            return 'repeat'#line:591
    except :#line:592
        print ("连接失败")#line:593
        logging .warning ('连接失败 ')#line:594
        return False #line:595
def Logout ():#line:598
    O0000O0OO00O0O0OO =host_ali #line:599
    OO0O000O0OO0OO0O0 =8080 #line:602
    global Username #line:603
    O000O0O00000O00O0 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:604
    try :#line:605
        O000O0O00000O00O0 .connect ((O0000O0OO00O0O0OO ,OO0O000O0OO0OO0O0 ))#line:606
    except socket .gaierror as O0O0000O000O00O0O :#line:607
        print ("Address-related error connecting to server: %s"%O0O0000O000O00O0O )#line:608
        logging .info ("Address-related error connecting to server: %s"%O0O0000O000O00O0O )#line:609
    except socket .error as O0O0000O000O00O0O :#line:611
        print ("Connection error: %s"%O0O0000O000O00O0O )#line:612
        logging .info ("Connection error: %s"%O0O0000O000O00O0O )#line:613
    OOO0OOO0000O00OOO =['logout',Username ,Password ]#line:617
    OOO0OOO0000O00OOO =json .dumps (OOO0OOO0000O00OOO )#line:618
    OOO0OOO0000O00OOO =bytes (OOO0OOO0000O00OOO ,encoding ="utf-8")#line:619
    logging .info ('发送信息 %s'%str (OOO0OOO0000O00OOO ,encoding ="utf-8"))#line:620
    O000O0O00000O00O0 .send (OOO0OOO0000O00OOO )#line:621
    O000O0O00000O00O0 .shutdown (1 )#line:622
    print ("Submit Log Out Complete")#line:623
    logging .info ("Submit Log Out Complete")#line:624
def Keeplogin ():#line:627
    OOO0O0O000O00000O =host_ali #line:628
    O00OO0OOO0OO0OO00 =8080 #line:631
    global Username #line:632
    OOOOO0000OO00OO0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:633
    try :#line:634
        OOOOO0000OO00OO0O .connect ((OOO0O0O000O00000O ,O00OO0OOO0OO0OO00 ))#line:635
    except socket .gaierror as O0OO00000O000OO00 :#line:636
        print ("Address-related error connecting to server: %s"%O0OO00000O000OO00 )#line:637
        logging .info ("Address-related error connecting to server: %s"%O0OO00000O000OO00 )#line:638
    except socket .error as O0OO00000O000OO00 :#line:640
        print ("Connection error: %s"%O0OO00000O000OO00 )#line:641
        logging .info ("Connection error: %s"%O0OO00000O000OO00 )#line:642
    OOOOOO00O0000O0O0 =['keep',Username ,Password ]#line:646
    OOOOOO00O0000O0O0 =json .dumps (OOOOOO00O0000O0O0 )#line:647
    OOOOOO00O0000O0O0 =bytes (OOOOOO00O0000O0O0 ,encoding ="utf-8")#line:648
    logging .info ('发送信息 %s'%str (OOOOOO00O0000O0O0 ,encoding ="utf-8"))#line:649
    OOOOO0000OO00OO0O .send (OOOOOO00O0000O0O0 )#line:650
    OOOOO0000OO00OO0O .shutdown (1 )#line:652
    print ("Submit keep Complete")#line:653
    logging .info ("Submit keep Complete")#line:654
def send_mail (OO0O0O00O000000OO ,OO0OOOO00OO0000OO ,OOO0000OO0O0000OO ):#line:657
    O0OO0000OOO00OOOO =open (OOO0000OO0O0000OO ,'rb')#line:658
    OOOOOO0OO0O0O0OO0 ,O0OO0O000OOO00000 =mimetypes .guess_type (OOO0000OO0O0000OO )#line:659
    if OOOOOO0OO0O0O0OO0 is None and O0OO0O000OOO00000 is None :#line:660
        OOOOOO0OO0O0O0OO0 ='application/octet-stream'#line:661
    O0O00O0000OO0O0OO ,O0OOOO00OOO00OO0O =OOOOOO0OO0O0O0OO0 .split ('/',1 )#line:662
    OO00O0OO0O0O00OOO =email .mime .base .MIMEBase (O0O00O0000OO0O0OO ,O0OOOO00OOO00OO0O )#line:663
    OO00O0OO0O0O00OOO .set_payload (O0OO0000OOO00OOOO .read ())#line:664
    O0OO0000OOO00OOOO .close ()#line:665
    email .encoders .encode_base64 (OO00O0OO0O0O00OOO )#line:666
    O000O0O000OOOO0OO =os .path .basename (OOO0000OO0O0000OO )#line:667
    OO00O0OO0O0O00OOO .add_header ('Content-Disposition','attachment',filename =O000O0O000OOOO0OO )#line:668
    OO0OOOO00OO0000OO =OO0OOOO00OO0000OO #line:669
    OO0OO0OO000O0O000 ='smtp.qq.com'#line:670
    OO000000OOOO0O0O0 =os .environ .get ('MAIL_USERNAME')#line:671
    OO0O000000OOO000O =os .environ .get ('MAIL_PASSWORD')#line:672
    OOOOOOOO0OO00000O =OO000000OOOO0O0O0 #line:673
    OO00OO0OO0OOOOOOO =MIMEMultipart ()#line:674
    OO00OO0OO0OOOOOOO .attach (OO00O0OO0O0O00OOO )#line:675
    OO00OO0OO0OOOOOOO ['Subject']=OO0O0O00O000000OO #line:676
    OO00OO0OO0OOOOOOO ['From']=OOOOOOOO0OO00000O #line:677
    OO00OO0OO0OOOOOOO ['To']=";".join (OO0OOOO00OO0000OO )#line:678
    O00O00OO00OOO00O0 =smtplib .SMTP_SSL (OO0OO0OO000O0O000 ,465 )#line:679
    O00O00OO00OOO00O0 .login (OO000000OOOO0O0O0 ,OO0O000000OOO000O )#line:680
    print ('login in  successfully')#line:681
    O00O00OO00OOO00O0 .sendmail (OOOOOOOO0OO00000O ,OO0OOOO00OO0000OO ,OO00OO0OO0OOOOOOO .as_string ())#line:682
    O00O00OO00OOO00O0 .quit ()#line:683
    print ('send email  successfully')#line:684
def Upload ():#line:686
    pass #line:687
def Com_read ():#line:690
    pass #line:691
def Com_decision ():#line:695
    pass #line:696
class TopFrame (wx .Frame ):#line:729
    def __init__ (OOOO0OOO0O0O00OO0 ,O00O0O0000OOOO00O ,OOOOO0OO0OO0O0O0O ):#line:730
        wx .Frame .__init__ (OOOO0OOO0O0O00OO0 ,None ,-1 ,O00O0O0000OOOO00O ,size =(520 ,320 ))#line:732
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_CLOSE ,OOOO0OOO0O0O00OO0 .OnClose )#line:733
        OOO00O0000OO00OO0 =time .time ()#line:737
        OOOO0OOO0O0O00OO0 .statusbar =OOOO0OOO0O0O00OO0 .CreateStatusBar ()#line:741
        OOOO0OOO0O0O00OO0 .statusbar .SetFieldsCount (3 )#line:743
        OOOO0OOO0O0O00OO0 .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:744
        OOOO0OOO0O0O00OO0 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:746
        OOOO0OOO0O0O00OO0 .SetIcon (OOOO0OOO0O0O00OO0 .icon )#line:747
        OOOO0OOO0O0O00OO0 .statusbar .SetStatusText (u"版本号",0 )#line:749
        OOOO0OOO0O0O00OO0 .statusbar .SetStatusText (u"%s"%OOOOO0OO0OO0O0O0O ,1 )#line:752
        OOOO0OOO0O0O00OO0 .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:755
        OOOO0OOO0O0O00OO0 .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:756
        OO000O0OO00O00000 =wx .Panel (OOOO0OOO0O0O00OO0 ,-1 )#line:758
        OO000O0OO00O00000 .SetBackgroundColour ((240 ,255 ,255 ))#line:760
        OOOO0OOO0O0O00OO0 .SetBackgroundColour ((240 ,255 ,255 ))#line:761
        OOOO0OOO0O0O00OO0 .thread =TimeThread ()#line:789
        OOOO0OOO0O0O00OO0 .keepthread =KeepThread ()#line:790
        OOOO0OOO0O0O00OO0 .button5 =wx .Button (OO000O0OO00O00000 ,label ='打开模拟',pos =(190 ,190 ))#line:818
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_BUTTON ,OOOO0OOO0O0O00OO0 .Openo0sdofsfo0sodf0so0 ,OOOO0OOO0O0O00OO0 .button5 )#line:819
        OOOO0OOO0O0O00OO0 .button6 =wx .Button (OO000O0OO00O00000 ,label ='打开国拍',pos =(280 ,190 ))#line:821
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_BUTTON ,OOOO0OOO0O0O00OO0 .OpenGuopai ,OOOO0OOO0O0O00OO0 .button6 )#line:822
        OOOO0OOO0O0O00OO0 .button16 =wx .Button (OO000O0OO00O00000 ,label ='修改国拍网址',pos =(370 ,190 ))#line:824
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_BUTTON ,OOOO0OOO0O0O00OO0 .UrlGuopai ,OOOO0OOO0O0O00OO0 .button16 )#line:825
        OOOO0OOO0O0O00OO0 .urlText =wx .TextCtrl (OO000O0OO00O00000 ,-1 ,pos =(370 ,230 ),size =(120 ,25 ))#line:826
        OOOO0OOO0O0O00OO0 .button7 =wx .Button (OO000O0OO00O00000 ,label ='显示帮助',pos =(10 ,190 ))#line:828
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_BUTTON ,OOOO0OOO0O0O00OO0 .Help ,OOOO0OOO0O0O00OO0 .button7 )#line:829
        OOOO0OOO0O0O00OO0 .button8 =wx .Button (OO000O0OO00O00000 ,label ='验证码练习',pos =(100 ,190 ))#line:831
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_BUTTON ,OOOO0OOO0O0O00OO0 .Yan_practice ,OOOO0OOO0O0O00OO0 .button8 )#line:832
        OOOO0OOO0O0O00OO0 .timer2 =wx .Timer (OOOO0OOO0O0O00OO0 )#line:872
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_TIMER ,OOOO0OOO0O0O00OO0 .MainControl ,OOOO0OOO0O0O00OO0 .timer2 )#line:873
        OOOO0OOO0O0O00OO0 .timer2 .Start (100 )#line:874
        OOOO0OOO0O0O00OO0 .timer3 =wx .Timer (OOOO0OOO0O0O00OO0 )#line:882
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_TIMER ,OOOO0OOO0O0O00OO0 .Lowest_zxco0o0o0o0 ,OOOO0OOO0O0O00OO0 .timer3 )#line:883
        OOOO0OOO0O0O00OO0 .timer3 .Start (100 )#line:884
        OOOO0OOO0O0O00OO0 .timer4 =wx .Timer (OOOO0OOO0O0O00OO0 )#line:886
        OOOO0OOO0O0O00OO0 .Bind (wx .EVT_TIMER ,OOOO0OOO0O0O00OO0 .Find_pos ,OOOO0OOO0O0O00OO0 .timer4 )#line:887
        OOOO0OOO0O0O00OO0 .timer4 .Start (150 )#line:888
        OOOO0OOO0O0O00OO0 .operationframe =OperationFrame ()#line:897
        OOOO0OOO0O0O00OO0 .operationframe .Show (False )#line:898
    def Lowest_zxco0o0o0o0 (O0OOOOOO0OOOOOOO0 ,O0O0OOOO0OOOOOO0O ):#line:908
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on #line:909
        if not findpos_on :#line:910
            O00O0OOOO0O000OO0 =int (TopFrame .Price_read ())#line:911
            if O00O0OOOO0O000OO0 in zxco0o0o0o0list :#line:913
                O0O0O0O0O0O0O_zxco0o0o0o0 =O00O0OOOO0O000OO0 #line:914
            else :#line:915
                findpos_on =True #line:916
    def Find_pos (OO0OO0OOOOOO0OOOO ,OOO0O00O0OO0O0OOO ):#line:933
        global findpos_on #line:934
        if findpos_on :#line:935
            findpos ()#line:936
    @staticmethod #line:942
    def Confirm ():#line:943
        global cf_hash ,sdfsf24324297_on #line:944
        O0OO0O0O0O000000O =TopFrame .Confirm_hash ()#line:945
        if O0OO0O0O0O000000O ==cf_hash [0 ]:#line:946
            sdfsf24324297_on =True #line:947
    @staticmethod #line:948
    def Refresh ():#line:949
        OOOOO0O000OO00OOO =TopFrame .Refresh_hash ()#line:950
        global cf_hash ,uioo0o000oo_on #line:951
        if OOOOO0O000OO00OOO ==cf_hash [1 ]:#line:952
            uioo0o000oo_on =True #line:953
    @staticmethod #line:962
    def Price_read ():#line:963
        O00OO0OO0O0OOOO0O =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:965
        O00OO0OO0O0OOOO0O =np .asarray (O00OO0OO0O0OOOO0O )#line:971
        OOO0OO0OO00000OOO =readpic (O00OO0OO0O0OOOO0O )#line:972
        return OOO0OO0OO00000OOO #line:974
    @staticmethod #line:977
    def Price_hash ():#line:978
        O0O00O00OOOO000OO =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:980
        global num #line:981
        num +=1 #line:982
        OOOOO00OOOOO0O000 =imagehash .dhash (O0O00O00OOOO000OO )#line:984
        return OOOOO00OOOOO0O000 #line:987
    @staticmethod #line:989
    def Confirm_hash ():#line:990
        OOO0O0O00OO0OO0OO =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:992
        OOOOOOO00O000OO00 =imagehash .dhash (OOO0O0O00OO0OO0OO )#line:995
        return OOOOOOO00O000OO00 #line:996
    @staticmethod #line:998
    def Refresh_hash ():#line:999
        OOOOOO00000O00OOO =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:1001
        O00OO000O000000OO =imagehash .dhash (OOOOOO00000O00OOO )#line:1003
        return O00OO000O000000OO #line:1004
    def OnEraseBackground (O0OO0O0O0O0000O00 ,O00O0OO000O0OO0O0 ):#line:1008
        ""#line:1011
        OO0OO00OOO000OO0O =O00O0OO000O0OO0O0 .GetDC ()#line:1012
        if not OO0OO00OOO000OO0O :#line:1013
            OO0OO00OOO000OO0O =wx .ClientDC (O0OO0O0O0O0000O00 )#line:1014
            O00O0O0O0OO0O00OO =O0OO0O0O0O0000O00 .GetUpdateRegion ().GetBox ()#line:1015
            OO0OO00OOO000OO0O .SetClippingRect (O00O0O0O0OO0O00OO )#line:1016
        OO0OO00OOO000OO0O .Clear ()#line:1017
        OO00O0O000OOOO0OO =wx .Bitmap ("blue.jpg")#line:1018
        OO0OO00OOO000OO0O .DrawBitmap (OO00O0O000OOOO0OO ,0 ,0 )#line:1019
    def OnClose (OO000000OO0O0O0O0 ,OOOOOO00OOO00000O ):#line:1023
        O0000O00OOO00O0O0 =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1024
        if O0000O00OOO00O0O0 ==wx .OK :#line:1025
            import sys as O0OO0OO00000O0OOO #line:1027
            OO000000OO0O0O0O0 .Show (False )#line:1032
            try :#line:1034
                OO000000OO0O0O0O0 .Close_time1 (OOOOOO00OOO00000O )#line:1035
                OO000000OO0O0O0O0 .Close_time2 (OOOOOO00OOO00000O )#line:1036
            except :#line:1037
                pass #line:1038
            Logout ()#line:1040
            wx .GetApp ().ExitMainLoop ()#line:1041
            OOOOOO00OOO00000O .Skip ()#line:1042
            O0OO0OO00000O0OOO .exit (None )#line:1043
    def OnOpenAssist (O00O0O0O00OOO000O ):#line:1047
        O00O0O0O00OOO000O .Open ()#line:1048
        global do #line:1049
        if do :#line:1050
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1051
        else :#line:1052
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1053
        O00O0O0O00OOO000O .Listen ()#line:1054
    @classmethod #line:1056
    def OnCloseAssist (OOO00O0000O0OOOOO ):#line:1057
        OOO00O0000O0OOOOO .Close ()#line:1058
    def OnViewPos (O00O0000O000OOOOO ,O0000OOO0O0000O00 ):#line:1065
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1066
        O00O0000O000OOOOO .MovePos (O0000OOO0O0000O00 )#line:1067
        global view #line:1068
        if not view :#line:1069
            view =True #line:1070
            for O000O000O00OOO0OO in range (len (Oo0o0Oo0o0o0 )):#line:1071
                O00O0000O000OOOOO .posframe [O000O000O00OOO0OO ].Show (view )#line:1072
        else :#line:1073
            view =False #line:1074
            for O000O000O00OOO0OO in range (len (Oo0o0Oo0o0o0 )):#line:1075
                O00O0000O000OOOOO .posframe [O000O000O00OOO0OO ].Hide ()#line:1076
    def OnSavePos (OO00OOO0000O0O0O0 ,O0O0O0O0OOOO0OO0O ):#line:1079
        OO00OOO0000O0O0O0 .MovePos (O0O0O0O0OOOO0OO0O )#line:1080
        OO00OOO0000O0O0O0 .Save_log ()#line:1081
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1082
    def MovePos (O00OOOOO0000OOO00 ,O0OO00O0000000OO0 ):#line:1088
        global Positon #line:1089
        for OOO0O0OOO0OO0O00O in range (5 ):#line:1090
            OO0O0O0OO0O0OOO00 ,OO000O0000O0O0OOO =Oo0o0Oo0o0o0 [OOO0O0OOO0OO0O00O ]#line:1091
            O00OOOOO0000OOO00 .posframe [OOO0O0OOO0OO0O00O ].Move (OO0O0O0OO0O0OOO00 -10 ,OO000O0000O0O0OOO -5 )#line:1092
    def Openo0sdofsfo0sodf0so0 (O00O00OOOO0000O0O ,OOO0OO0OO0OO00OO0 ):#line:1094
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1096
        ghjo0o0o0o0_on =True #line:1097
        O000OOOOO00O000OO =True #line:1098
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
            O00O00OOOO0000O0O .Open ()#line:1113
            if do :#line:1114
                o0sdofsfo0sodf0so0_on =True #line:1115
                ad_view =True #line:1116
                web_on =True #line:1117
                O00O00OOOO0000O0O .fr =WebFrame (Px ,Py ,False ,'沪牌模拟')#line:1118
                O00O00OOOO0000O0O .operationframe .Show (True )#line:1119
                if time_on :#line:1121
                    O00O00OOOO0000O0O .operationframe .Opentime ()#line:1122
                if not ghjo0o0o0o0_repeat :#line:1123
                    O00O00OOOO0000O0O .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1124
                    O00O00OOOO0000O0O .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1125
                    ghjo0o0o0o0_repeat =True #line:1126
                OO0OO0O000OO0OO0O =wx .html2 .WebView .New (O00O00OOOO0000O0O .fr ,size =(websize [0 ],websize [1 ]),pos =(0 ,0 ))#line:1129
                OO0OO0O000OO0OO0O .LoadURL (url1 )#line:1130
                OO0OO0O000OO0OO0O .CanSetZoomType (False )#line:1131
                O00O00OOOO0000O0O .fr .Show ()#line:1132
            else :#line:1136
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1137
                O00O00OOOO0000O0O .Close ()#line:1138
            O00O00OOOO0000O0O .Listen ()#line:1139
    def OpenGuopai (O0OOO0OOO00OO00OO ,OOO0OO0000OO000OO ):#line:1189
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1191
        ghjo0o0o0o0_on =True #line:1192
        OOO0000O00000OOO0 =True #line:1193
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
            O0OOO0OOO00OO00OO .Open ()#line:1205
            if do :#line:1209
                ad_view =True #line:1210
                ooweo0o0werwr_on =True #line:1211
                O0OOO0OOO00OO00OO .fr =WebFrame (Px ,Py ,False ,'国拍网')#line:1212
                O0OOO0OOO00OO00OO .operationframe .Show (True )#line:1213
                if time_on :#line:1215
                    O0OOO0OOO00OO00OO .operationframe .Opentime ()#line:1216
                if not ghjo0o0o0o0_repeat :#line:1217
                    O0OOO0OOO00OO00OO .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1218
                    O0OOO0OOO00OO00OO .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1219
                    ghjo0o0o0o0_repeat =True #line:1220
                OOOO0OOO0000O0000 =wx .html2 .WebView .New (O0OOO0OOO00OO00OO .fr ,size =(websize [0 ],websize [1 ]))#line:1222
                OOOO0OOO0000O0000 .LoadURL (url2 )#line:1223
                OOOO0OOO0000O0000 .CanSetZoomType (False )#line:1224
                O0OOO0OOO00OO00OO .fr .Show ()#line:1225
            else :#line:1229
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1230
                O0OOO0OOO00OO00OO .Close ()#line:1231
            O0OOO0OOO00OO00OO .Listen ()#line:1232
    def UrlGuopai (OO0O0O000O000O0OO ,OO0OOOOOOO00OOOOO ):#line:1234
        global url2 #line:1235
        try :#line:1236
            url2 =OO0O0O000O000O0OO .urlText .GetValue ()#line:1237
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1238
        except :#line:1239
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1240
    def Help (OO0OO00OOO000OO00 ,OOOOO0000O00OO0O0 ):#line:1243
        OO000OO0OO000O0O0 ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1249
        O00OO0O0OOOOO0O00 =wx .adv .AboutDialogInfo ()#line:1252
        O00OO0O0OOOOO0O00 .SetName ("沪牌第一枪")#line:1253
        O00OO0O0OOOOO0O00 .SetVersion (OO000OO0OO000O0O0 )#line:1254
        O00OO0O0OOOOO0O00 .AddDeveloper ("ZS")#line:1258
        wx .adv .AboutBox (O00OO0O0OOOOO0O00 )#line:1259
    def Yan_practice (OO0O0O00O000O0000 ,OOO0000000O00000O ):#line:1261
        pass #line:1262
    def Time_adjust (OOO0OOOO00OO0OO00 ,O00O00OOO0O00O00O ):#line:1264
        pass #line:1265
    @staticmethod #line:1275
    def OnJiajia ():#line:1276
        OOOO0OO00OOOOO00O =pg .position ()#line:1277
        Oo0o0Oo0o0o0 [0 ][0 ]=OOOO0OO00OOOOO00O [0 ]#line:1278
        Oo0o0Oo0o0o0 [0 ][1 ]=OOOO0OO00OOOOO00O [1 ]#line:1279
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1280
        findpos ()#line:1281
    @staticmethod #line:1284
    def OnChujia ():#line:1285
        OOOO0OOO0O00O0OO0 =pg .position ()#line:1286
        Oo0o0Oo0o0o0 [1 ][0 ]=OOOO0OOO0O00O0OO0 [0 ]#line:1287
        Oo0o0Oo0o0o0 [1 ][1 ]=OOOO0OOO0O00O0OO0 [1 ]#line:1288
    @staticmethod #line:1289
    def OnTijiao ():#line:1290
        OOO00OOOO0OOO000O =pg .position ()#line:1291
        Oo0o0Oo0o0o0 [2 ][0 ]=OOO00OOOO0OOO000O [0 ]#line:1292
        Oo0o0Oo0o0o0 [2 ][1 ]=OOO00OOOO0OOO000O [1 ]#line:1293
    @staticmethod #line:1294
    def OnShuaxin ():#line:1295
        O0OO00O0OO0000OOO =pg .position ()#line:1296
        Oo0o0Oo0o0o0 [3 ][0 ]=O0OO00O0OO0000OOO [0 ]#line:1297
        Oo0o0Oo0o0o0 [3 ][1 ]=O0OO00O0OO0000OOO [1 ]#line:1298
    @staticmethod #line:1299
    def OnConfirm ():#line:1300
        O00O0O0O000OO00O0 =pg .position ()#line:1301
        Oo0o0Oo0o0o0 [4 ][0 ]=O00O0O0O000OO00O0 [0 ]#line:1302
        Oo0o0Oo0o0o0 [4 ][1 ]=O00O0O0O000OO00O0 [1 ]#line:1303
    @staticmethod #line:1304
    def OnYanzhengma ():#line:1305
        OO0O0O00O00O0O000 =pg .position ()#line:1306
        Oo0o0Oo0o0o0 [5 ][0 ]=OO0O0O00O00O0O000 [0 ]#line:1307
        Oo0o0Oo0o0o0 [5 ][1 ]=OO0O0O00O00O0O000 [1 ]#line:1308
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
    def OnClick_Tijiao (OO0000O000OOO00O0 ):#line:1336
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1337
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1338
        sdfsf24324297_need =True #line:1339
        if oOO0O0O0O0O0O0_num ==1 :#line:1341
            OOOOO000OOOO0OO00 =threading .Timer (one_delay ,OO0000O000OOO00O0 .Tijiao )#line:1342
            OOOOO000OOOO0OO00 .start ()#line:1343
            oOO0O0O0O0O0O0_on =False #line:1344
            if twice :#line:1345
                print ("修改为2")#line:1346
                oOO0O0O0O0O0O0_num =2 #line:1347
            print ("成功提交")#line:1349
        elif oOO0O0O0O0O0O0_num ==2 :#line:1350
            oOO0O0O0O0O0O0_num =0 #line:1351
            OOOOO000OOOO0OO00 =threading .Timer (ooo0O0o0oO0O_delay ,OO0000O000OOO00O0 .Tijiao )#line:1352
            OOOOO000OOOO0OO00 .start ()#line:1353
            oOO0O0O0O0O0O0_on =False #line:1354
        else :#line:1356
            OO0000O000OOO00O0 .Tijiao ()#line:1357
    @staticmethod #line:1359
    def Tijiao ():#line:1360
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1361
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1362
        oOO0O0O0O0O0O0_OK =False #line:1363
        global sdfsf24324297_one #line:1364
        if not sdfsf24324297_one :#line:1365
            O000O0000O0000OOO =sdfsf24324297Thread ()#line:1366
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
                    OO00O0OOO0OO0OOOO =uioo0o000ooThread ()#line:1410
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
                    OO00O0OOO0OO0OOOO =uioo0o000ooThread ()#line:1424
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
    def MainControl (O00O00O0OOO0000OO ,O0O00OO0OOOOOOOOO ):#line:1504
        if not web_on and time_on :#line:1506
            O00O00O0OOO0000OO .operationframe .Closetime ()#line:1507
        if web_on :#line:1508
            try :#line:1509
                O00O00O0OOO0000OO .operationframe .Show (True )#line:1510
            except :#line:1511
                pass #line:1512
        else :#line:1513
            try :#line:1514
                O00O00O0OOO0000OO .operationframe .Show (False )#line:1515
            except :#line:1516
                pass #line:1517
        if web_on :#line:1520
            O00O00O0OOO0000OO .Show (False )#line:1521
        else :#line:1522
            O00O00O0OOO0000OO .Show (True )#line:1523
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
    def query (OOO0O0O0OOOO0000O ):#line:1542
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
            OOO0O000OOOOO00O0 =threading .Timer (3 ,OOO0O0O0OOOO0000O .query_sleep3 )#line:1553
            OOO0O000OOOOO00O0 .start ()#line:1554
            O0O00O0O0O000OO0O =threading .Timer (5 ,OOO0O0O0OOOO0000O .query_sleep5 )#line:1555
            O0O00O0O0O000OO0O .start ()#line:1556
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
            O000O0O0OO0OOOO0O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1602
            OO000OO00OO0O0O0O =ctypes .windll .user32 #line:1603
            OO0O0OO00000O0O0O ={1 :(O000O0O0OO0OOOO0O ['2'],win32con .MOD_ALT ),2 :(O000O0O0OO0OOOO0O ['3'],win32con .MOD_ALT ),3 :(O000O0O0OO0OOOO0O ['4'],win32con .MOD_ALT ),4 :(O000O0O0OO0OOOO0O ['5'],win32con .MOD_ALT ),5 :(O000O0O0OO0OOOO0O ['6'],win32con .MOD_ALT ),6 :(O000O0O0OO0OOOO0O ['7'],win32con .MOD_ALT ),}#line:1607
            O000000O000O0OOOO ={7 :(O000O0O0OO0OOOO0O ['s'],0x4000 ),8 :(O000O0O0OO0OOOO0O ['f'],0x4000 ),9 :(O000O0O0OO0OOOO0O ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O000O0O0OO0OOOO0O ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O000O0O0OO0OOOO0O ['q'],0x4000 )}#line:1610
            for O0OOO0O0O0000OOO0 ,(OOO00OO00O0O00OO0 ,O0OOO0OO00OO0O00O )in OO0O0OO00000O0O0O .items ():#line:1612
                if not OO000OO00OO0O0O0O .RegisterHotKey (None ,O0OOO0O0O0000OOO0 ,O0OOO0OO00OO0O00O ,OOO00OO00O0O00OO0 ):#line:1613
                    print ("Unable to register id",O0OOO0O0O0000OOO0 )#line:1614
                    logging .info ("Unable to register id",O0OOO0O0O0000OOO0 )#line:1615
                    do =False #line:1616
            for O0OOO0O0O0000OOO0 ,(OOO00OO00O0O00OO0 ,O0OOO0OO00OO0O00O )in O000000O000O0OOOO .items ():#line:1617
                if not OO000OO00OO0O0O0O .RegisterHotKey (None ,O0OOO0O0O0000OOO0 ,O0OOO0OO00OO0O00O ,OOO00OO00O0O00OO0 ):#line:1618
                    print ("Unable to register id",O0OOO0O0O0000OOO0 )#line:1619
                    logging .info ("Unable to register id",O0OOO0O0O0000OOO0 )#line:1620
                    do =False #line:1621
                web_on =True #line:1622
    @staticmethod #line:1625
    def Listen ():#line:1626
        try :#line:1627
            O0O0O00OOO0OO0O0O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1632
            OOOO00OO000OO0O0O ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .selfTijiao ,9 :TopFrame .selfChujia ,10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .query }#line:1638
            O00O0OOOO0OO0OOOO =ctypes .windll .user32 #line:1639
            O0OOOO0OO000O0OOO =wintypes .MSG ()#line:1640
            O0OO0O0OO00OO0OOO =ctypes .byref #line:1641
            while O00O0OOOO0OO0OOOO .GetMessageA (O0OO0O0OO00OO0OOO (O0OOOO0OO000O0OOO ),None ,0 ,0 )!=0 :#line:1642
                if O0OOOO0OO000O0OOO .message ==win32con .WM_HOTKEY :#line:1643
                    OOOOOO00O0OO0OOOO =OOOO00OO000OO0O0O .get (O0OOOO0OO000O0OOO .wParam )#line:1644
                    if OOOOOO00O0OO0OOOO :#line:1645
                        OOOOOO00O0OO0OOOO ()#line:1646
                O00O0OOOO0OO0OOOO .TranslateMessage (O0OO0O0OO00OO0OOO (O0OOOO0OO000O0OOO ))#line:1647
                O00O0OOOO0OO0OOOO .DispatchMessageA (O0OO0O0OO00OO0OOO (O0OOOO0OO000O0OOO ))#line:1648
        finally :#line:1649
            pass #line:1650
    @staticmethod #line:1657
    def Close ():#line:1658
        global do #line:1659
        if do :#line:1660
            do =False #line:1661
            OO0O00OOO0O00OO0O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1665
            OO0000O0OOO0O00O0 ={1 :(OO0O00OOO0O00OO0O ['2'],win32con .MOD_ALT ),2 :(OO0O00OOO0O00OO0O ['3'],win32con .MOD_ALT ),3 :(OO0O00OOO0O00OO0O ['4'],win32con .MOD_ALT ),4 :(OO0O00OOO0O00OO0O ['5'],win32con .MOD_ALT ),5 :(OO0O00OOO0O00OO0O ['6'],win32con .MOD_ALT ),6 :(OO0O00OOO0O00OO0O ['7'],win32con .MOD_ALT ),}#line:1669
            O000O0OOOO0OOO0O0 =ctypes .windll .user32 #line:1670
            OO00O0O00O00O0O00 ={7 :(OO0O00OOO0O00OO0O ['s'],0x4000 ),8 :(OO0O00OOO0O00OO0O ['f'],0x4000 ),9 :(OO0O00OOO0O00OO0O ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OO0O00OOO0O00OO0O ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OO0O00OOO0O00OO0O ['q'],0x4000 )}#line:1673
            for O0OOO00O0O0000OO0 in OO0000O0OOO0O00O0 .keys ():#line:1674
                O000O0OOOO0OOO0O0 .UnregisterHotKey (None ,O0OOO00O0O0000OO0 )#line:1675
            for O0OOO00O0O0000OO0 in OO00O0O00O00O0O00 .keys ():#line:1676
                O000O0OOOO0OOO0O0 .UnregisterHotKey (None ,O0OOO00O0O0000OO0 )#line:1677
            logging .info ("close assistant success")#line:1678
        else :#line:1679
            pass #line:1680
    def Save_log (OO000O0O0O000O00O ):#line:1682
        OO0OOOOO00OOOO0O0 =open ('pos.log','wb')#line:1683
        pickle .dump (Oo0o0Oo0o0o0 ,OO0OOOOO00OOOO0O0 )#line:1684
        OO0OOOOO00OOOO0O0 .close ()#line:1685
    def Confirmlogin (O0O0000000O00O0O0 ,O0OOOO0O0O00O0000 ):#line:1765
        Keeplogin ()#line:1766
    def Choose_time1 (O000O0OOO0O0O0000 ,O00OO0O0O00O0OO00 ):#line:1771
        O000O0OOO0O0O0000 .timelabel .SetLabel ("已设定截止时间"+O000O0OOO0O0O0000 .time_choice1 .GetString (O000O0OOO0O0O0000 .time_choice1 .GetSelection ())+'.'+str (O000O0OOO0O0O0000 .time_choice2 .GetSelection ())+" 秒")#line:1774
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1775
        ghjo0o0o0o01 =O000O0OOO0O0O0000 .time_choice1 .GetString (O000O0OOO0O0O0000 .time_choice1 .GetSelection ())#line:1776
        ghjo0o0o0o02 =O000O0OOO0O0O0000 .time_choice2 .GetString (O000O0OOO0O0O0000 .time_choice2 .GetSelection ())#line:1777
    def Choose_time2 (O00000OO00OO0OO00 ,O0OO000OO0000O000 ):#line:1780
        O00000OO00OO0OO00 .timelabel .SetLabel ("已设定截止时间"+O00000OO00OO0OO00 .time_choice1 .GetString (O00000OO00OO0OO00 .time_choice1 .GetSelection ())+'.'+str (O00000OO00OO0OO00 .time_choice2 .GetSelection ())+" 秒")#line:1783
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1784
        ghjo0o0o0o01 =O00000OO00OO0OO00 .time_choice1 .GetString (O00000OO00OO0OO00 .time_choice1 .GetSelection ())#line:1785
        ghjo0o0o0o02 =O00000OO00OO0OO00 .time_choice2 .GetString (O00000OO00OO0OO00 .time_choice2 .GetSelection ())#line:1786
class ClockWindow (wx .Panel ):#line:1839
    def __init__ (O0O0000O00O000O00 ,OO00OOO0O00O0O00O ):#line:1840
        wx .Window .__init__ (O0O0000O00O000O00 ,OO00OOO0O00O0O00O ,size =Timesize )#line:1841
        O0O0000O00O000O00 .Bind (wx .EVT_PAINT ,O0O0000O00O000O00 .OnPaint )#line:1842
        O0O0000O00O000O00 .timer =wx .Timer (O0O0000O00O000O00 )#line:1843
        O0O0000O00O000O00 .Bind (wx .EVT_TIMER ,O0O0000O00O000O00 .OnTimer ,O0O0000O00O000O00 .timer )#line:1844
        O0O0000O00O000O00 .timer .Start (100 )#line:1845
    def Draw (O0O000O0OO00O00O0 ,OOOO0O0OOOOO0O0OO ):#line:1847
        global a_time #line:1848
        OO00000OOO0OO0O00 =time .localtime (a_time )#line:1849
        O0OOO0O0OO0000O00 =time .strftime ("%H:%M:%S",OO00000OOO0OO0O00 )#line:1850
        OOO00OOO0O0OOO00O ,O0O00O00OO0O0OOO0 =O0O000O0OO00O00O0 .GetClientSize ()#line:1851
        OOOO0O0OOOOO0O0OO .SetBackground (wx .Brush (O0O000O0OO00O00O0 .GetBackgroundColour ()))#line:1852
        OOOO0O0OOOOO0O0OO .Clear ()#line:1853
        OOOO0O0OOOOO0O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1854
        OO00OO000000O0O0O ,OOOOOOO0O00OOOO00 =OOOO0O0OOOOO0O0OO .GetTextExtent (O0OOO0O0OO0000O00 )#line:1855
        OOOO0O0OOOOO0O0OO .DrawText (O0OOO0O0OO0000O00 ,(OOO00OOO0O0OOO00O -OO00OO000000O0O0O )/2 ,(O0O00O00OO0O0OOO0 )/2 -OOOOOOO0O00OOOO00 /2 )#line:1856
    def Modify (O0O0OOO000O0O0000 ,O0OO00O0OOO00O0OO ):#line:1858
        global a_time ,b_time #line:1859
        if b_time <9 :#line:1861
            b_time =b_time +1 #line:1862
        else :#line:1863
            b_time =0 #line:1864
        O00O000OOO00000OO =time .localtime (a_time )#line:1865
        OO000000000OO0000 =time .strftime ("%H:%M:%S",O00O000OOO00000OO )#line:1866
        OO0O0000O0OOO0OO0 ,O000O0OOO00OO00OO =O0O0OOO000O0O0000 .GetClientSize ()#line:1868
        O0OO00O0OOO00O0OO .SetBackground (wx .Brush (O0O0OOO000O0O0000 .GetBackgroundColour ()))#line:1869
        O0OO00O0OOO00O0OO .Clear ()#line:1870
        O0OO00O0OOO00O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1871
        O00O000OO0OO0000O ,O00O0O0000O00O0OO =O0OO00O0OOO00O0OO .GetTextExtent (OO000000000OO0000 )#line:1872
        O0OO00O0OOO00O0OO .DrawText (OO000000000OO0000 ,(OO0O0000O0OOO0OO0 -O00O000OO0OO0000O )/2 ,(O000O0OOO00OO00OO )/2 -O00O0O0000O00O0OO /2 )#line:1873
    def OnTimer (OOO0O0000O0O00000 ,O000000O00OO00O0O ):#line:1875
        O0OOOO000O0O0O000 =wx .BufferedDC (wx .ClientDC (OOO0O0000O0O00000 ))#line:1876
        OOO0O0000O0O00000 .Modify (O0OOOO000O0O0O000 )#line:1877
    def OnPaint (O0OOOOO0OOOOO00O0 ,OOO000OO0OO0OO0OO ):#line:1879
        OO00000O0O000000O =wx .BufferedPaintDC (O0OOOOO0OOOOO00O0 )#line:1880
        O0OOOOO0OOOOO00O0 .Draw (OO00000O0O000000O )#line:1881
class TimeFrame (wx .Frame ):#line:1885
    def __init__ (OO00OOO00O0OOOO0O ):#line:1886
        wx .Frame .__init__ (OO00OOO00O0OOOO0O ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1888
        ClockWindow (OO00OOO00O0OOOO0O )#line:1891
class MoniClockWindow (wx .Panel ):#line:1896
    def __init__ (O000O0O000O0O0O0O ,OOOOOO0OO00000O00 ):#line:1897
        wx .Window .__init__ (O000O0O000O0O0O0O ,OOOOOO0OO00000O00 ,size =Timesize )#line:1898
        O000O0O000O0O0O0O .Bind (wx .EVT_PAINT ,O000O0O000O0O0O0O .OnPaint )#line:1899
        O000O0O000O0O0O0O .timer =wx .Timer (O000O0O000O0O0O0O )#line:1900
        O000O0O000O0O0O0O .Bind (wx .EVT_TIMER ,O000O0O000O0O0O0O .OnTimer ,O000O0O000O0O0O0O .timer )#line:1901
        O000O0O000O0O0O0O .timer .Start (100 )#line:1902
    def Draw (OO00O0000OO0O0O00 ,OO00OOOO000OOOOO0 ):#line:1904
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1905
        O0O000O00OO00O00O ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1906
        OOO00000O000OO0OO ,OO000O0OOO0OO0OOO =OO00O0000OO0O0O00 .GetClientSize ()#line:1907
        OO00OOOO000OOOOO0 .SetBackground (wx .Brush (OO00O0000OO0O0O00 .GetBackgroundColour ()))#line:1908
        OO00OOOO000OOOOO0 .Clear ()#line:1909
        OO00OOOO000OOOOO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1910
        O0000OOO0O0000000 ,OOO000OOO00000OOO =OO00OOOO000OOOOO0 .GetTextExtent (O0O000O00OO00O00O )#line:1911
        OO00OOOO000OOOOO0 .DrawText (O0O000O00OO00O00O ,(OOO00000O000OO0OO -O0000OOO0O0000000 )/2 ,(OO000O0OOO0OO0OOO )/2 -OOO000OOO00000OOO /2 )#line:1912
    def Modify (O0O0OOO0O0OO0000O ,OOOOOO0OOOO0000O0 ):#line:1914
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1915
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:1916
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:1917
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:1918
        OOO0O0OOO0O0O0000 =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:1919
        O0OO0O00OO0OOO0OO ="%s:%s:%s"%(11 ,29 ,OOO0O0OOO0O0O0000 )#line:1920
        OO00OO00OOOOO00OO ,O00OO00000O00O00O =O0O0OOO0O0OO0000O .GetClientSize ()#line:1921
        OOOOOO0OOOO0000O0 .SetBackground (wx .Brush (O0O0OOO0O0OO0000O .GetBackgroundColour ()))#line:1922
        OOOOOO0OOOO0000O0 .Clear ()#line:1923
        OOOOOO0OOOO0000O0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1924
        OO00OOOOOO00OOO00 ,OOOO00O0OO00O00OO =OOOOOO0OOOO0000O0 .GetTextExtent (O0OO0O00OO0OOO0OO )#line:1925
        OOOOOO0OOOO0000O0 .DrawText (O0OO0O00OO0OOO0OO ,(OO00OO00OOOOO00OO -OO00OOOOOO00OOO00 )/2 ,(O00OO00000O00O00O )/2 -OOOO00O0OO00O00OO /2 )#line:1926
    def OnTimer (O0OOOO0OO0OO00O00 ,O00O0000OO0O0OO0O ):#line:1928
        OOOOOOO000000O00O =wx .BufferedDC (wx .ClientDC (O0OOOO0OO0OO00O00 ))#line:1929
        O0OOOO0OO0OO00O00 .Modify (OOOOOOO000000O00O )#line:1930
    def OnPaint (O00OOO00OOO00OOOO ,OO000O0OOOOOO00O0 ):#line:1932
        O0OOOO0O0O0O0OOOO =wx .BufferedPaintDC (O00OOO00OOO00OOOO )#line:1933
        O00OOO00OOO00OOOO .Draw (O0OOOO0O0O0O0OOOO )#line:1934
class MoniTimeFrame (wx .Frame ):#line:1938
    def __init__ (OOOOO0000OOOOOO0O ):#line:1939
        wx .Frame .__init__ (OOOOO0000OOOOOO0O ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1941
        MoniClockWindow (OOOOO0000OOOOOO0O )#line:1944
class PosFrame (wx .Frame ):#line:1949
    def __init__ (OOO0O0O0OO0O0OO00 ,O000O0OO0OO0O0OO0 ,OO0OOO0OOO0O00O0O ):#line:1950
        OO0O00O000O000000 ,OO0O00OO0000OOOO0 =O000O0OO0OO0O0OO0 #line:1951
        wx .Frame .__init__ (OOO0O0O0OO0O0OO00 ,None ,-1 ,'POS',pos =(OO0O00O000O000000 -20 ,OO0O00OO0000OOOO0 -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:1953
        O0OO00000O0000O0O =wx .Panel (OOO0O0O0OO0O0OO00 ,-1 ,size =(30 ,20 ))#line:1954
        O0O0000O0O00O000O =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:1956
        OOOO00OOOO0O0OOOO =[]#line:1957
        OOOO00OOOO0O0OOOO .append (wx .StaticText (O0OO00000O0000O0O ,-1 ,OO0OOO0OOO0O00O0O ,(0 ,0 )))#line:1959
        for OOO0OO00OOOO0000O in range (len (OOOO00OOOO0O0OOOO )):#line:1960
            OOOO00OOOO0O0OOOO [OOO0OO00OOOO0000O ].SetFont (O0O0000O0O00O000O )#line:1961
class PriceFrame (wx .Frame ):#line:1963
    def __init__ (O0O00OOO0OO0O0O00 ,OOOOOOOOO00OO0O0O ):#line:1964
        wx .Frame .__init__ (O0O00OOO0OO0O0O00 ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1967
        O0O00OOO0OO0O0O00 .panel =wx .Panel (O0O00OOO0OO0O0O00 ,size =Pricesize )#line:1968
        wx .StaticBitmap (O0O00OOO0OO0O0O00 .panel ,-1 ,wx .BitmapFromImage (OOOOOOOOO00OO0O0O ))#line:1970
class YanzhengmaFrame (wx .Frame ):#line:1972
    def __init__ (O0O00OOO0O0OO0000 ,OO00OOOOOO0O0000O ):#line:1973
        wx .Frame .__init__ (O0O00OOO0O0OO0000 ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1976
        O0O00OOO0O0OO0000 .panel =wx .Panel (O0O00OOO0O0OO0000 ,size =(400 ,80 ))#line:1977
        wx .StaticBitmap (O0O00OOO0O0OO0000 .panel ,-1 ,wx .BitmapFromImage (OO00OOOOOO0O0000O ))#line:1979
class AdFrame (wx .Frame ):#line:1983
    def __init__ (O00OOO0OOOOO0000O ):#line:1984
        wx .Frame .__init__ (O00OOO0OOOOO0000O ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:1986
        O0O00OO0OO0000000 =wx .Panel (O00OOO0OOOOO0000O ,-1 ,size =(250 ,200 ))#line:1987
        O00O00OO0O000O0OO =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:1989
        O0O0O00000OOOOO00 =[]#line:1990
        O0O0O00000OOOOO00 .append (wx .StaticText (O0O00OO0OO0000000 ,-1 ," 专业代拍软件",(15 ,10 )))#line:1992
        O0O0O00000OOOOO00 .append (wx .StaticText (O0O00OO0OO0000000 ,-1 ," 专业代拍团队",(15 ,60 )))#line:1994
        O0O0O00000OOOOO00 .append (wx .StaticText (O0O00OO0OO0000000 ,-1 ,"关注微信公众号",(15 ,110 )))#line:1996
        O0O0O00000OOOOO00 .append (wx .StaticText (O0O00OO0OO0000000 ,-1 ," 沪牌第一枪",(15 ,160 )))#line:1998
        for OO0OO0000OO0O0OO0 in range (len (O0O0O00000OOOOO00 )):#line:1999
            O0O0O00000OOOOO00 [OO0OO0000OO0O0OO0 ].SetFont (O00O00OO0O000O0OO )#line:2000
class WebFrame (wx .Frame ):#line:2002
    def __init__ (O0OO000OO00O0OO0O ,OO0OO000O0O000OO0 ,OOOO0O00OO0OOOOOO ,OOOOOO00OO0O0O0OO ,OO00OO00OOOOOO00O ):#line:2003
        wx .Frame .__init__ (O0OO000OO00O0OO0O ,None ,-1 ,OO00OO00OOOOOO00O ,size =(websize [0 ],websize [1 ]),pos =(OO0OO000O0O000OO0 ,OOOO0O00OO0OOOOOO ),style =wx .SIMPLE_BORDER )#line:2004
        if OOOOOO00OO0O0O0OO :#line:2009
            O0OO000OO00O0OO0O .adframe =AdFrame ()#line:2010
            O0OO000OO00O0OO0O .adframe .Show (True )#line:2011
        O0OO000OO00O0OO0O .Bind (wx .EVT_CLOSE ,O0OO000OO00O0OO0O .OnClose )#line:2012
        O0OO000OO00O0OO0O .ad2 =OOOOOO00OO0O0O0OO #line:2013
        O0OO000OO00O0OO0O .control =ControlFrame (OO00OO00OOOOOO00O )#line:2014
        O0OO000OO00O0OO0O .control .Show (True )#line:2015
        pub .subscribe (O0OO000OO00O0OO0O .OnClose2 ,"close web")#line:2040
    def OnClose (O0O00000O0OO0OO00 ,OO0O0000OOOO0OOOO ):#line:2041
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2042
        web_on =False #line:2043
        view_time =False #line:2044
        o0sdofsfo0sodf0so0_on =False #line:2045
        ooweo0o0werwr_on =False #line:2046
        TopFrame .Close ()#line:2047
        O0O0O000OO0OOO00O ="sc_new.png"#line:2048
        if os .path .exists (O0O0O000OO0OOO00O ):#line:2049
            os .remove (O0O0O000OO0OOO00O )#line:2050
        O0O00000O0OO0OO00 .Destroy ()#line:2051
        if O0O00000O0OO0OO00 .ad2 :#line:2052
            O0O00000O0OO0OO00 .adframe .Destroy ()#line:2053
        OO0O0000OOOO0OOOO .Skip ()#line:2054
    def OnClose2 (O0O0OOO0O00OOOO00 ):#line:2056
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2057
        web_on =False #line:2058
        view_time =False #line:2059
        o0sdofsfo0sodf0so0_on =False #line:2060
        ooweo0o0werwr_on =False #line:2061
        TopFrame .Close ()#line:2062
        O000O00OOO0OOOOO0 ="sc_new.png"#line:2063
        if os .path .exists (O000O00OOO0OOOOO0 ):#line:2064
            os .remove (O000O00OOO0OOOOO0 )#line:2065
        O0O0OOO0O00OOOO00 .Destroy ()#line:2066
        if O0O0OOO0O00OOOO00 .ad2 :#line:2067
            O0O0OOO0O00OOOO00 .adframe .Destroy ()#line:2068
class ControlFrame (wx .Frame ):#line:2071
    def __init__ (OO0O000O0000000O0 ,OO0O00O00O000O000 ):#line:2072
        wx .Frame .__init__ (OO0O000O0000000O0 ,None ,-1 ,size =(50 ,35 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +websize [0 ]-50 ,0 ))#line:2074
        OO0O000O0000000O0 .panel =wx .Panel (OO0O000O0000000O0 ,-1 ,size =(50 ,35 ))#line:2075
        OO0O000O0000000O0 .button1 =wx .Button (OO0O000O0000000O0 .panel ,pos =(0 ,0 ),size =(50 ,25 ),label ="关闭")#line:2076
        OO0O000O0000000O0 .Bind (wx .EVT_BUTTON ,OO0O000O0000000O0 .o_closeweb ,OO0O000O0000000O0 .button1 )#line:2077
    def o_closeweb (O000OO0000O00OOOO ,O0O0OOOO0OOO000O0 ):#line:2078
        wx .CallAfter (pub .sendMessage ,"close web")#line:2079
        O000OO0000O00OOOO .Destroy ()#line:2080
        O0O0OOOO0OOO000O0 .Skip ()#line:2081
class OperationFrame (wx .Frame ):#line:2084
    def __init__ (O0000000000O0OO0O ):#line:2085
        wx .Frame .__init__ (O0000000000O0OO0O ,None ,-1 ,pos =(1070 ,100 ),size =(300 ,410 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION )#line:2087
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2089
        one_oO0O0O0O0O0O0O0O01 =O0000000000O0OO0O .gettime (OO00000o01 )#line:2090
        one_oO0O0O0O0O0O0O0O02 =O0000000000O0OO0O .gettime (OO00000o02 )#line:2091
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0000000000O0OO0O .gettime (ooo0O0o0oO0O_time1 )#line:2092
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0000000000O0OO0O .gettime (ooo0O0o0oO0O_time2 )#line:2093
        O0000000000O0OO0O .timer1 =wx .Timer (O0000000000O0OO0O )#line:2095
        O0000000000O0OO0O .Bind (wx .EVT_TIMER ,O0000000000O0OO0O .Price_view ,O0000000000O0OO0O .timer1 )#line:2096
        O0000000000O0OO0O .timer1 .Start (500 )#line:2097
        O0000000000O0OO0O .timer2 =wx .Timer (O0000000000O0OO0O )#line:2099
        O0000000000O0OO0O .Bind (wx .EVT_TIMER ,O0000000000O0OO0O .Price_count ,O0000000000O0OO0O .timer2 )#line:2100
        O0000000000O0OO0O .timer2 .Start (100 )#line:2101
        O0000000000O0OO0O .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:2103
        O0000000000O0OO0O .O0O0O0O0O0O0Oframe .Show (False )#line:2104
        O0OO00OOO0O000O00 =wx .Panel (O0000000000O0OO0O ,-1 ,size =(300 ,380 ))#line:2108
        OOOOO0O0O0000O000 =wx .StaticBox (O0OO00OOO0O000O00 ,-1 ,u'选择策略:')#line:2110
        O0000000000O0OO0O .stractagySizer =wx .StaticBoxSizer (OOOOO0O0O0000O000 ,wx .VERTICAL )#line:2111
        O0OOO0O0OOOOOOOO0 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2112
        O0O00O0000O0O000O =wx .BoxSizer (wx .HORIZONTAL )#line:2113
        O0O00O0000O0O000O .Add (O0OOO0O0OOOOOOOO0 )#line:2114
        OO0O0O00OOOOO00O0 =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2118
        O0000000000O0OO0O .select_stractagy =wx .Choice (O0OO00OOO0O000O00 ,-1 ,choices =OO0O0O00OOOOO00O0 ,size =(100 ,50 ))#line:2119
        O0O00O0000O0O000O .Add (O0000000000O0OO0O .select_stractagy )#line:2120
        O0000000000O0OO0O .select_stractagy .SetSelection (0 )#line:2121
        O0000000000O0OO0O .timeview =wx .CheckBox (O0OO00OOO0O000O00 ,-1 ,label =u'显示时间')#line:2123
        O000000O000OO0O0O =wx .BoxSizer (wx .HORIZONTAL )#line:2124
        O000000O000OO0O0O .Add (O0000000000O0OO0O .timeview )#line:2125
        O0000000000O0OO0O .button1 =wx .Button (O0OO00OOO0O000O00 ,label ='+1s',size =(35 ,25 ))#line:2128
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Add_ooo0O0o0oO0O ,O0000000000O0OO0O .button1 )#line:2129
        O0000000000O0OO0O .button2 =wx .Button (O0OO00OOO0O000O00 ,label ='-1s',size =(35 ,25 ))#line:2130
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Minus_ooo0O0o0oO0O ,O0000000000O0OO0O .button2 )#line:2131
        O0000000000O0OO0O .button3 =wx .Button (O0OO00OOO0O000O00 ,label ='+0.1s',size =(35 ,25 ))#line:2132
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Add_time ,O0000000000O0OO0O .button3 )#line:2133
        O0000000000O0OO0O .button4 =wx .Button (O0OO00OOO0O000O00 ,label ='-0.1s',size =(35 ,25 ))#line:2134
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Minus_time ,O0000000000O0OO0O .button4 )#line:2135
        O000000O000OO0O0O .Add (O0000000000O0OO0O .button1 )#line:2137
        O000000O000OO0O0O .Add (O0000000000O0OO0O .button2 )#line:2138
        O000000O000OO0O0O .Add (O0000000000O0OO0O .button3 )#line:2139
        O000000O000OO0O0O .Add (O0000000000O0OO0O .button4 )#line:2140
        OOO0OO0OO0000OOO0 =wx .BoxSizer (wx .VERTICAL )#line:2142
        OOO0OO0OO0000OOO0 .Add (O0O00O0000O0O000O )#line:2143
        OOO0OO0OO0000OOO0 .Add (O000000O000OO0O0O )#line:2144
        O00O00O0O000O0OO0 =["E键","回车"]#line:2147
        O0000000000O0OO0O .sdfsf24324297_choice =wx .Choice (O0OO00OOO0O000O00 ,-1 ,choices =O00O00O0O000O0OO0 )#line:2148
        O0000000000O0OO0O .sdfsf24324297_choice .SetSelection (0 )#line:2149
        O0000000000O0OO0O .sdfsf24324297_label =wx .StaticText (O0OO00OOO0O000O00 ,label =u"确认提交方式     ")#line:2150
        O00O00000O0O0O0O0 =wx .BoxSizer (wx .HORIZONTAL )#line:2151
        O00O00000O0O0O0O0 .Add (O0000000000O0OO0O .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2152
        O00O00000O0O0O0O0 .Add (O0000000000O0OO0O .sdfsf24324297_choice )#line:2153
        OOO0OO0OO0000OOO0 .Add (O00O00000O0O0O0O0 )#line:2154
        O0000000000O0OO0O .ghjo0o0o0o0_save =wx .Button (O0OO00OOO0O000O00 ,label ="保存策略",size =(60 ,35 ))#line:2157
        O0000000000O0OO0O .ghjo0o0o0o0_load =wx .Button (O0OO00OOO0O000O00 ,label ="载入策略",size =(60 ,35 ))#line:2158
        O0000000000O0OO0O .save_info =wx .Button (O0OO00OOO0O000O00 ,label ="用户信息",size =(60 ,35 ))#line:2159
        O0000OOOOOO00OOOO =wx .BoxSizer (wx .HORIZONTAL )#line:2160
        O0000OOOOOO00OOOO .Add (O0000000000O0OO0O .ghjo0o0o0o0_save )#line:2161
        O0000OOOOOO00OOOO .Add (O0000000000O0OO0O .ghjo0o0o0o0_load )#line:2162
        O0000OOOOOO00OOOO .Add (O0000000000O0OO0O .save_info )#line:2163
        OOO0OO0OO0000OOO0 .Add (O0000OOOOOO00OOOO )#line:2164
        O00O00OO000O00000 =wx .StaticBox (O0OO00OOO0O000O00 ,-1 ,u'单枪策略:')#line:2168
        O0000000000O0OO0O .oneshotSizer =wx .StaticBoxSizer (O00O00OO000O00000 ,wx .VERTICAL )#line:2169
        O0O000OO0O0O00OOO =wx .GridBagSizer (4 ,4 )#line:2170
        O0000000000O0OO0O .jiajia_time =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2171
        O0000000000O0OO0O .jiajia_time .SetRange (40 ,55 )#line:2172
        O0000000000O0OO0O .jiajia_time .SetValue (48 )#line:2173
        O0000000000O0OO0O .jiajia_time .SetIncrement (0.1 )#line:2174
        O0O000OO0O0O00OOO .Add (O0000000000O0OO0O .jiajia_time ,pos =(0 ,0 ))#line:2176
        OOOOOOOO0O0OOO0O0 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2177
        O0O000OO0O0O00OOO .Add (OOOOOOOO0O0OOO0O0 ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2178
        OOOOO0O0O00O00OOO =wx .StaticText (O0OO00OOO0O000O00 ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2179
        O0O000OO0O0O00OOO .Add (OOOOO0O0O00O00OOO ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2180
        O0000000000O0OO0O .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2181
        O0000000000O0OO0O .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2182
        O0000000000O0OO0O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2183
        O0000000000O0OO0O .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2184
        O0O000OO0O0O00OOO .Add (O0000000000O0OO0O .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2185
        O00OO0O0O0O00OO0O =[u"提前100",u"提前200",u"踩点"]#line:2188
        O0000000000O0OO0O .select_oOO0O0O0O0O0O0 =wx .Choice (O0OO00OOO0O000O00 ,-1 ,choices =O00OO0O0O0O00OO0O ,size =(68 ,25 ))#line:2189
        O0000000000O0OO0O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2190
        O0O000OO0O0O00OOO .Add (O0000000000O0OO0O .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2191
        OO000000OO00O0O00 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"出价提交延迟")#line:2192
        O0O000OO0O0O00OOO .Add (OO000000OO00O0O00 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2193
        O0000000000O0OO0O .yanchi_time =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2194
        O0000000000O0OO0O .yanchi_time .SetRange (0.0 ,1.0 )#line:2195
        O0000000000O0OO0O .yanchi_time .SetValue (0.5 )#line:2196
        O0000000000O0OO0O .yanchi_time .SetIncrement (0.1 )#line:2197
        O0O000OO0O0O00OOO .Add (O0000000000O0OO0O .yanchi_time ,pos =(1 ,3 ))#line:2198
        O000O0O0O00OO0OO0 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2199
        O0O000OO0O0O00OOO .Add (O000O0O0O00OO0OO0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2200
        O00OO0O0OO00O0O00 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"强制提交时间")#line:2203
        O0O000OO0O0O00OOO .Add (O00OO0O0OO00O0O00 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2204
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2205
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2206
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2207
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2208
        O0O000OO0O0O00OOO .Add (O0000000000O0OO0O .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2209
        OO00O0OO0O0O0O0OO =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2210
        O0O000OO0O0O00OOO .Add (OO00O0OO0O0O0O0OO ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2211
        O0000000000O0OO0O .oneshotSizer .Add (O0O000OO0O0O00OOO ,0 ,flag =wx .ALL ,border =5 )#line:2213
        OO0O00OOO0OOOO000 =wx .StaticBox (O0OO00OOO0O000O00 ,-1 ,u'双枪策略:')#line:2217
        O0000000000O0OO0O .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (OO0O00OOO0OOOO000 ,wx .VERTICAL )#line:2218
        O0OO00O0O0OO0O00O =wx .GridBagSizer (4 ,4 )#line:2219
        O0000000000O0OO0O .jiajia_time2 =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2220
        O0000000000O0OO0O .jiajia_time2 .SetRange (40 ,55 )#line:2221
        O0000000000O0OO0O .jiajia_time2 .SetValue (48 )#line:2222
        O0000000000O0OO0O .jiajia_time2 .SetIncrement (0.1 )#line:2223
        O0OO00O0O0OO0O00O .Add (O0000000000O0OO0O .jiajia_time2 ,pos =(0 ,0 ))#line:2224
        O0000OO000OOO0000 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2225
        O0OO00O0O0OO0O00O .Add (O0000OO000OOO0000 ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2226
        O0OO0O0OO0OO00O0O =wx .StaticText (O0OO00OOO0O000O00 ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2227
        O0OO00O0O0OO0O00O .Add (O0OO0O0OO0OO00O0O ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2228
        O0000000000O0OO0O .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2229
        O0000000000O0OO0O .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2230
        O0000000000O0OO0O .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2231
        O0000000000O0OO0O .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2232
        O0OO00O0O0OO0O00O .Add (O0000000000O0OO0O .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2233
        OO0000OOO0O0O0OOO =[u"提前100",u"提前200",u"踩点"]#line:2235
        O0000000000O0OO0O .select_oOO0O0O0O0O0O02 =wx .Choice (O0OO00OOO0O000O00 ,-1 ,choices =OO0000OOO0O0O0OOO ,size =(68 ,25 ))#line:2236
        O0000000000O0OO0O .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2237
        O0OO00O0O0OO0O00O .Add (O0000000000O0OO0O .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2238
        OOO0O000000O0OO0O =wx .StaticText (O0OO00OOO0O000O00 ,label =u"出价提交延迟")#line:2239
        O0OO00O0O0OO0O00O .Add (OOO0O000000O0OO0O ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2240
        O0000000000O0OO0O .yanchi_time2 =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2241
        O0000000000O0OO0O .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2242
        O0000000000O0OO0O .yanchi_time2 .SetValue (0.5 )#line:2243
        O0000000000O0OO0O .yanchi_time2 .SetIncrement (0.1 )#line:2244
        O0OO00O0O0OO0O00O .Add (O0000000000O0OO0O .yanchi_time2 ,pos =(1 ,3 ))#line:2245
        O0OOOO0O0000OO000 =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2246
        O0OO00O0O0OO0O00O .Add (O0OOOO0O0000OO000 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2247
        O00OO0O0O0000O00O =wx .StaticText (O0OO00OOO0O000O00 ,label =u"强制提交时间")#line:2250
        O0OO00O0O0OO0O00O .Add (O00OO0O0O0000O00O ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2251
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (O0OO00OOO0O000O00 ,-1 ,"",size =(68 ,25 ))#line:2252
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2253
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2254
        O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2255
        O0OO00O0O0OO0O00O .Add (O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2256
        O000O0O000OO0000O =wx .StaticText (O0OO00OOO0O000O00 ,label =u"秒")#line:2257
        O0OO00O0O0OO0O00O .Add (O000O0O000OO0000O ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2258
        O0000000000O0OO0O .ooo0O0o0oO0OshotSizer .Add (O0OO00O0O0OO0O00O ,0 ,flag =wx .ALL ,border =5 )#line:2260
        O0000000000O0OO0O .stractagySizer .Add (OOO0OO0OO0000OOO0 ,0 ,wx .ALL |wx .CENTER ,5 )#line:2262
        O0000000000O0OO0O .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2263
        O0OOOOO0O00000OOO =wx .StaticText (O0OO00OOO0O000O00 ,-1 ,label =u"拍牌功能设置")#line:2266
        OO0000O0000O00OO0 =wx .StaticLine (O0OO00OOO0O000O00 ,-1 )#line:2267
        O0000000000O0OO0O .vbox1 .Add (O0OOOOO0O00000OOO ,0 ,wx .ALL |wx .LEFT ,10 )#line:2268
        O0000000000O0OO0O .vbox1 .Add (OO0000O0000O00OO0 ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2269
        O0000000000O0OO0O .vbox1 .Add (O0000000000O0OO0O .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2270
        O0000000000O0OO0O .vbox1 .Add (O0000000000O0OO0O .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2271
        O0000000000O0OO0O .vbox1 .Add (O0000000000O0OO0O .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2272
        O0OO00OOO0O000O00 .SetSizer (O0000000000O0OO0O .vbox1 )#line:2273
        O0000000000O0OO0O .ooo0O0o0oO0Osizer_Shown =False #line:2276
        O0000000000O0OO0O .oneshotsizer_Shown =True #line:2277
        O0000000000O0OO0O .vbox1 .Hide (O0000000000O0OO0O .ooo0O0o0oO0OshotSizer )#line:2278
        O0000000000O0OO0O .Bind (wx .EVT_CHECKBOX ,O0000000000O0OO0O .Timeview ,O0000000000O0OO0O .timeview )#line:2287
        O0000000000O0OO0O .Bind (wx .EVT_CHOICE ,O0000000000O0OO0O .Confirmchoice ,O0000000000O0OO0O .sdfsf24324297_choice )#line:2288
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Strategy_save ,O0000000000O0OO0O .ghjo0o0o0o0_save )#line:2289
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Strategy_load ,O0000000000O0OO0O .ghjo0o0o0o0_load )#line:2290
        O0000000000O0OO0O .Bind (wx .EVT_BUTTON ,O0000000000O0OO0O .Save_info ,O0000000000O0OO0O .save_info )#line:2291
        O0000000000O0OO0O .Bind (wx .EVT_CHOICE ,O0000000000O0OO0O .Refresh_panel ,O0000000000O0OO0O .select_stractagy )#line:2293
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Jiajia_time ,O0000000000O0OO0O .jiajia_time )#line:2295
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Jiajia_zxco0o0o0o0 ,O0000000000O0OO0O .jiajia_zxco0o0o0o0 )#line:2297
        O0000000000O0OO0O .Bind (wx .EVT_CHOICE ,O0000000000O0OO0O .Select_oOO0O0O0O0O0O0 ,O0000000000O0OO0O .select_oOO0O0O0O0O0O0 )#line:2298
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Yanchi_time ,O0000000000O0OO0O .yanchi_time )#line:2300
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Tijiao_time ,O0000000000O0OO0O .oOO0O0O0O0O0O0_time )#line:2302
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Jiajia_time2 ,O0000000000O0OO0O .jiajia_time2 )#line:2305
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Jiajia_zxco0o0o0o02 ,O0000000000O0OO0O .jiajia_zxco0o0o0o02 )#line:2307
        O0000000000O0OO0O .Bind (wx .EVT_CHOICE ,O0000000000O0OO0O .Select_oOO0O0O0O0O0O02 ,O0000000000O0OO0O .select_oOO0O0O0O0O0O02 )#line:2308
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Yanchi_time2 ,O0000000000O0OO0O .yanchi_time2 )#line:2310
        O0000000000O0OO0O .Bind (wx .EVT_TEXT ,O0000000000O0OO0O .Tijiao_time2 ,O0000000000O0OO0O .oOO0O0O0O0O0O0_time2 )#line:2312
        O0000000000O0OO0O .timeframe1 =TimeFrame ()#line:2314
        O0000000000O0OO0O .timeframe1 .Show (False )#line:2315
        O0000000000O0OO0O .timeframe2 =MoniTimeFrame ()#line:2317
        O0000000000O0OO0O .timeframe2 .Show (False )#line:2318
        O0000000000O0OO0O .operationtimer =wx .Timer (O0000000000O0OO0O )#line:2321
        O0000000000O0OO0O .Bind (wx .EVT_TIMER ,O0000000000O0OO0O .opt ,O0000000000O0OO0O .operationtimer )#line:2322
        O0000000000O0OO0O .operationtimer .Start (3000 )#line:2323
    def Price_view (O0OOO0O0O0OO0OOOO ,OOO0OOO0O0OO00OOO ):#line:2326
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:2327
        print (zxco0o0o0o0_view ,zxco0o0o0o0_count )#line:2328
        if zxco0o0o0o0_view and zxco0o0o0o0_count >=4 :#line:2329
            try :#line:2330
                O0OOO0O0O0OO0OOOO .Price_close ()#line:2331
            except :#line:2332
                pass #line:2333
            O0OOO0O0O0OO0OOOO .Screen_shot ()#line:2334
            OO00OO0O0OOO00OO0 ="sc_new.png"#line:2335
            O0OOO0O0O0OO0OOOO .zxco0o0o0o0frame =PriceFrame (OO00OO0O0OOO00OO0 )#line:2336
            O0OOO0O0O0OO0OOOO .zxco0o0o0o0frame .Show (True )#line:2337
            zxco0o0o0o0_view =False #line:2338
            zxco0o0o0o0_on =True #line:2339
            print ("到这5")#line:2340
    def Price_count (OOO00OO0OOOO0000O ,OO0O00000OO0000OO ):#line:2342
        global zxco0o0o0o0_count #line:2344
        zxco0o0o0o0_count +=1 #line:2345
        O000O00O0O00O00OO ='sc_new.png'#line:2346
        if web_on and ghjo0o0o0o0_on :#line:2347
            OOO00OO0OOOO0000O .O0O0O0O0O0O0Oframe .Show (True )#line:2348
        if not os .path .exists (O000O00O0O00O00OO ):#line:2349
            try :#line:2350
                OOO00OO0OOOO0000O .Price_close ()#line:2351
            except :#line:2352
                pass #line:2353
        if not ghjo0o0o0o0_on or not web_on :#line:2355
            OOO00OO0OOOO0000O .O0O0O0O0O0O0Oframe .Show (False )#line:2356
    def Screen_shot (O00OO0O00O0O00O0O ):#line:2361
        global Pricesize #line:2362
        OO0OOOOOO0O0O0000 =Pos_zxco0o0o0o0 #line:2363
        O0OO00OO0O0OO0O00 =ImageGrab .grab (OO0OOOOOO0O0O0000 )#line:2364
        O0OO00OO0O0OO0O00 .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:2365
    @staticmethod #line:2368
    def Del_shot ():#line:2369
        try :#line:2370
            os .remove ("sc_new.png")#line:2371
        except :#line:2372
            pass #line:2373
    def Price_close (OOOOO00O0O00000OO ):#line:2376
        try :#line:2377
            OOOOO00O0O00000OO .zxco0o0o0o0frame .Destroy ()#line:2378
        except :#line:2379
            pass #line:2380
    def opt (O000OO0OO0OO000O0 ,O00OOO00OO00O000O ):#line:2384
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2385
        global ghjo0o0o0o0_on #line:2386
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2387
        if O000OO0OO0OO000O0 .select_stractagy .GetSelection ==0 :#line:2388
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2389
                print ("触发1")#line:2390
                twice =False #line:2391
                ghjo0o0o0o0_on =True #line:2392
                oo0o0O0O0O0_on =True #line:2393
                oOO0O0O0O0O0O0_on =False #line:2394
                oOO0O0O0O0O0O0_num =1 #line:2395
                oOO0O0O0O0O0O0_OK =False #line:2396
                oOO0O0O0O0O0O0_one =False #line:2397
        elif O000OO0OO0OO000O0 .select_stractagy .GetSelection ==1 :#line:2398
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2399
                print ("触发2")#line:2400
                ghjo0o0o0o0_on =True #line:2401
                twice =True #line:2402
                oo0o0O0O0O0_on =True #line:2403
                oOO0O0O0O0O0O0_on =False #line:2404
                oOO0O0O0O0O0O0_num =1 #line:2405
                oOO0O0O0O0O0O0_OK =False #line:2406
                oOO0O0O0O0O0O0_one =False #line:2407
    def Add_time (OOO0O0OOOO0O00O00 ,O0OO00OO0O00O0O00 ):#line:2411
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2412
        if o0sdofsfo0sodf0so0_on :#line:2413
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2414
        else :#line:2415
            a_time +=0.1 #line:2416
    def Minus_time (O000000OO00OOO00O ,O0O0O0O00OOO0O000 ):#line:2418
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2419
        if o0sdofsfo0sodf0so0_on :#line:2420
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2421
        else :#line:2422
            a_time -=0.1 #line:2423
    def Add_ooo0O0o0oO0O (O0O00O0OOO0O0000O ,OO00O0OO000OOO000 ):#line:2425
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2426
        if o0sdofsfo0sodf0so0_on :#line:2427
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2428
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2429
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2430
        else :#line:2431
            a_time +=1 #line:2432
    def Minus_ooo0O0o0oO0O (OO00O0O00000OOOO0 ,OOO0000000O0O0OOO ):#line:2434
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2435
        if o0sdofsfo0sodf0so0_on :#line:2436
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2437
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2438
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2439
        else :#line:2440
            a_time -=1 #line:2441
    def Timeview (O0O00OO0000O00O00 ,OOO000OOO0OOO0000 ):#line:2443
        OOO000OOO0OOOO0O0 =OOO000OOO0OOO0000 .GetEventObject ()#line:2444
        global view_time ,time_on #line:2445
        if OOO000OOO0OOOO0O0 .IsChecked ():#line:2446
            view_time =True #line:2447
            time_on =True #line:2448
            if ooweo0o0werwr_on :#line:2449
                O0O00OO0000O00O00 .timeframe1 .Show (True )#line:2450
            elif o0sdofsfo0sodf0so0_on :#line:2451
                O0O00OO0000O00O00 .timeframe2 .Show (True )#line:2452
        else :#line:2453
            view_time =False #line:2454
            time_on =False #line:2455
            if ooweo0o0werwr_on :#line:2456
                O0O00OO0000O00O00 .timeframe1 .Show (False )#line:2457
            elif o0sdofsfo0sodf0so0_on :#line:2458
                O0O00OO0000O00O00 .timeframe2 .Show (False )#line:2459
    def Opentime (O0O000OOO00O00OO0 ):#line:2461
        if o0sdofsfo0sodf0so0_on :#line:2462
            try :#line:2463
                O0O000OOO00O00OO0 .timeframe2 .Show (True )#line:2464
            except :#line:2465
                pass #line:2466
        elif ooweo0o0werwr_on :#line:2467
            try :#line:2468
                O0O000OOO00O00OO0 .timeframe1 .Show (True )#line:2469
            except :#line:2470
                pass #line:2471
    def Closetime (O0OOOO0O00O00OOO0 ):#line:2474
        try :#line:2475
            O0OOOO0O00O00OOO0 .timeframe1 .Show (False )#line:2476
        except :#line:2477
            pass #line:2478
        try :#line:2479
            O0OOOO0O00O00OOO0 .timeframe2 .Show (False )#line:2480
        except :#line:2481
            pass #line:2482
    def Confirmchoice (O000O00000000OOOO ,OO0O0000O000OO0OO ):#line:2484
        global e_on ,enter_on #line:2485
        OOO0O0OO0000000OO =O000O00000000OOOO .sdfsf24324297_choice .GetSelection ()#line:2486
        if OOO0O0OO0000000OO ==0 :#line:2487
            e_on =True #line:2488
            enter_on =False #line:2489
        elif OOO0O0OO0000000OO ==1 :#line:2490
            e_on =False #line:2491
            enter_on =True #line:2492
    def Jiajia_time (O0OO000OOOOOO0O00 ,OOOO00O0000OO0OOO ):#line:2496
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2497
        OOOOOO0OO00OO00OO =O0OO000OOOOOO0O00 .jiajia_time .GetValue ()#line:2498
        OOO00OOO0OO0OO00O =[40 +OOOOOO00O0OO00OOO *0.1 for OOOOOO00O0OO00OOO in range (151 )]#line:2499
        if OOOOOO0OO00OO00OO in OOO00OOO0OO0OO00O :#line:2500
            OO00000o01 =OOOOOO0OO00OO00OO #line:2501
            OO00000o01 =float (OO00000o01 )#line:2502
            one_oO0O0O0O0O0O0O0O01 =O0OO000OOOOOO0O00 .gettime (OO00000o01 )#line:2503
        else :#line:2504
            O0OO000OOOOOO0O00 .jiajia_time .SetValue (OO00000o01 )#line:2505
    def Jiajia_zxco0o0o0o0 (OOO000OOOO00OO0O0 ,OO0O000O0OO0000OO ):#line:2508
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2509
        OO00000O0O0OOO0O0 =[300 +OO000OOO00O00O0O0 *100 for OO000OOO00O00O0O0 in range (13 )]#line:2510
        O00O0OOO000O0OOOO =OOO000OOOO00OO0O0 .jiajia_zxco0o0o0o0 .GetValue ()#line:2511
        if O00O0OOO000O0OOOO in OO00000O0O0OOO0O0 :#line:2512
            one_diff =int (O00O0OOO000O0OOOO )#line:2513
        else :#line:2514
            OOO000OOOO00OO0O0 .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2515
    def Select_oOO0O0O0O0O0O0 (O0O00OOO0O00OO0O0 ,OOOOO000O0000OOO0 ):#line:2518
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2519
        OO0OOO0OO00OO000O =O0O00OOO0O00OO0O0 .select_oOO0O0O0O0O0O0 .GetString (O0O00OOO0O00OO0O0 .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2520
        if OO0OOO0OO00OO000O ==u"提前100":#line:2521
            one_advance =100 #line:2522
        elif OO0OOO0OO00OO000O ==u"提前200":#line:2523
            one_advance =200 #line:2524
        else :#line:2525
            one_advance =0 #line:2526
    def Yanchi_time (O00O0OO00OOOOO0O0 ,OOO0OO0O0OO00OO00 ):#line:2528
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2529
        O00O0OOOO00O00OO0 =['0.%d'%OOOO00O0O0OOOO00O for OOOO00O0O0OOOO00O in range (11 )]#line:2530
        O00O0OOOO00O00OO0 .append ('1.0')#line:2531
        OO0O0O0OO0O0OOO0O =str (O00O0OO00OOOOO0O0 .yanchi_time .GetValue ())#line:2532
        if OO0O0O0OO0O0OOO0O in O00O0OOOO00O00OO0 :#line:2533
            one_delay =float (OO0O0O0OO0O0OOO0O )#line:2534
        else :#line:2535
            O00O0OO00OOOOO0O0 .yanchi_time .SetValue (one_delay )#line:2536
    def Tijiao_time (OO0O000OO00OOO000 ,O0O000O0OO00O0O0O ):#line:2538
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2539
        OO0OOOO0000OO0O00 =OO0O000OO00OOO000 .oOO0O0O0O0O0O0_time .GetValue ()#line:2540
        OOOO0O0O000OOOOOO =[40 +O0O00OO00OO00OO0O *0.1 for O0O00OO00OO00OO0O in range (171 )]#line:2541
        if OO0OOOO0000OO0O00 in OOOO0O0O000OOOOOO :#line:2542
            OO00000o02 =float (OO0OOOO0000OO0O00 )#line:2543
            one_oO0O0O0O0O0O0O0O02 =OO0O000OO00OOO000 .gettime (OO00000o02 )#line:2544
        else :#line:2545
            OO0O000OO00OOO000 .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2546
    def Jiajia_time2 (O00O000O00OO0O00O ,OO0OOOO00O000000O ):#line:2548
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2549
        O000000OOO0O000OO =O00O000O00OO0O00O .jiajia_time2 .GetValue ()#line:2550
        O0O0O0O0O00O0OO0O =[40 +O00OO0O00O00OO0OO *0.1 for O00OO0O00O00OO0OO in range (151 )]#line:2551
        if O000000OOO0O000OO in O0O0O0O0O00O0OO0O :#line:2552
            ooo0O0o0oO0O_time1 =float (O000000OOO0O000OO )#line:2553
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00O000O00OO0O00O .gettime (ooo0O0o0oO0O_time1 )#line:2554
        else :#line:2555
            O00O000O00OO0O00O .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2556
    def Jiajia_zxco0o0o0o02 (O00OO0000OO00OO0O ,OO0OOO0OO0O000O00 ):#line:2558
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2559
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2560
        OOOO0OOOOO00OO00O =[300 +O000000O00O0O0OOO *100 for O000000O00O0O0OOO in range (13 )]#line:2561
        OO0OO00O0OO0O000O =O00OO0000OO00OO0O .jiajia_zxco0o0o0o02 .GetValue ()#line:2562
        if OO0OO00O0OO0O000O in OOOO0OOOOO00OO00O :#line:2563
            ooo0O0o0oO0O_diff =int (OO0OO00O0OO0O000O )#line:2564
        else :#line:2565
            O00OO0000OO00OO0O .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2566
    def Select_oOO0O0O0O0O0O02 (OO0O000O0OO00O0OO ,O000000OOOOO00000 ):#line:2568
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2569
        OOOO000O000OOO0O0 =OO0O000O0OO00O0OO .select_oOO0O0O0O0O0O02 .GetString (OO0O000O0OO00O0OO .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2570
        if OOOO000O000OOO0O0 ==u"提前100":#line:2571
            ooo0O0o0oO0O_advance =100 #line:2572
        elif OOOO000O000OOO0O0 ==u"提前200":#line:2573
            ooo0O0o0oO0O_advance =200 #line:2574
        else :#line:2575
            ooo0O0o0oO0O_advance =0 #line:2576
    def Yanchi_time2 (O0OO0OOO00O00O00O ,O000O00OOOO0000OO ):#line:2579
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2580
        O0OO0000O0O0O000O =['0.%d'%OOOOOO0O0OOOO0O0O for OOOOOO0O0OOOO0O0O in range (11 )]#line:2581
        O0OO0000O0O0O000O .append ('1.0')#line:2582
        OOO0O00O00O00O0OO =str (O0OO0OOO00O00O00O .yanchi_time2 .GetValue ())#line:2583
        if OOO0O00O00O00O0OO in O0OO0000O0O0O000O :#line:2584
            ooo0O0o0oO0O_delay =float (OOO0O00O00O00O0OO )#line:2585
        else :#line:2586
            O0OO0OOO00O00O00O .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2587
    def Tijiao_time2 (O000O0O0OOO0OO000 ,OOO00O0O000O0OO00 ):#line:2590
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2591
        OO000000OOO0O00O0 =O000O0O0OOO0OO000 .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2592
        OO0OO00000OOOOOOO =[53 +OOOOOO0OO000O0O00 *0.1 for OOOOOO0OO000O0O00 in range (41 )]#line:2593
        if OO000000OOO0O00O0 in OO0OO00000OOOOOOO :#line:2594
            ooo0O0o0oO0O_time2 =float (OO000000OOO0O00O0 )#line:2595
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O000O0O0OOO0OO000 .gettime (ooo0O0o0oO0O_time2 )#line:2596
        else :#line:2597
            O000O0O0OOO0OO000 .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2598
    def Refresh_panel (OOO0O000O0O000OOO ,O0OOO0OO0OOO0000O ):#line:2602
        global ghjo0o0o0o0_on #line:2604
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2605
        OO0O000OO00OOO0O0 =OOO0O000O0O000OOO .select_stractagy .GetString (OOO0O000O0O000OOO .select_stractagy .GetSelection ())#line:2606
        if OO0O000OO00OOO0O0 ==u"单枪策略":#line:2607
            OOO0O000O0O000OOO .ss_Hide ()#line:2608
            twice =False #line:2609
            ghjo0o0o0o0_on =True #line:2610
            oo0o0O0O0O0_on =True #line:2611
            oOO0O0O0O0O0O0_on =False #line:2612
            oOO0O0O0O0O0O0_num =1 #line:2613
            oOO0O0O0O0O0O0_OK =False #line:2614
            oOO0O0O0O0O0O0_one =False #line:2615
        elif OO0O000OO00OOO0O0 ==u"双枪策略":#line:2617
            OOO0O000O0O000OOO .ss_Shown ()#line:2618
            ghjo0o0o0o0_on =True #line:2619
            twice =True #line:2620
            oo0o0O0O0O0_on =True #line:2621
            oOO0O0O0O0O0O0_on =False #line:2622
            oOO0O0O0O0O0O0_num =1 #line:2623
            oOO0O0O0O0O0O0_OK =False #line:2624
            oOO0O0O0O0O0O0_one =False #line:2625
        else :#line:2626
            OOO0O000O0O000OOO .none_show ()#line:2627
            ghjo0o0o0o0_on =False #line:2628
            twice =False #line:2629
    def ss_Shown (OOOOOOOOO00O00OOO ):#line:2632
        if not OOOOOOOOO00O00OOO .ooo0O0o0oO0Osizer_Shown :#line:2633
            OOOOOOOOO00O00OOO .vbox1 .Show (OOOOOOOOO00O00OOO .ooo0O0o0oO0OshotSizer )#line:2634
            OOOOOOOOO00O00OOO .ooo0O0o0oO0Osizer_Shown =True #line:2635
        if not OOOOOOOOO00O00OOO .oneshotsizer_Shown :#line:2636
            OOOOOOOOO00O00OOO .vbox1 .Show (OOOOOOOOO00O00OOO .oneshotSizer )#line:2637
            OOOOOOOOO00O00OOO .oneshotsizer_Shown =True #line:2638
        OOOOOOOOO00O00OOO .ooo0O0o0oO0Osizer_Shown =True #line:2639
        OOOOOOOOO00O00OOO .oneshotSizer_Shown =True #line:2640
        OOOOOOOOO00O00OOO .SetClientSize ((280 ,560 ))#line:2641
        OOOOOOOOO00O00OOO .Secondshot_reset ()#line:2642
        OOOOOOOOO00O00OOO .Layout ()#line:2643
    def ss_Hide (O00OO0OO0OO0OO0OO ):#line:2645
        if O00OO0OO0OO0OO0OO .ooo0O0o0oO0Osizer_Shown :#line:2646
            O00OO0OO0OO0OO0OO .vbox1 .Hide (O00OO0OO0OO0OO0OO .ooo0O0o0oO0OshotSizer )#line:2647
        if not O00OO0OO0OO0OO0OO .oneshotsizer_Shown :#line:2650
            O00OO0OO0OO0OO0OO .vbox1 .Show (O00OO0OO0OO0OO0OO .oneshotSizer )#line:2651
        O00OO0OO0OO0OO0OO .ooo0O0o0oO0Osizer_Shown =False #line:2652
        O00OO0OO0OO0OO0OO .oneshotSizer_Shown =True #line:2653
        O00OO0OO0OO0OO0OO .SetClientSize ((280 ,360 ))#line:2654
        O00OO0OO0OO0OO0OO .Oneshot_reset ()#line:2655
        O00OO0OO0OO0OO0OO .Layout ()#line:2656
    def none_show (O00000OOOOO00OO0O ):#line:2658
        if O00000OOOOO00OO0O .oneshotsizer_Shown :#line:2659
            O00000OOOOO00OO0O .vbox1 .Hide (O00000OOOOO00OO0O .ooo0O0o0oO0OshotSizer )#line:2660
        if O00000OOOOO00OO0O .ooo0O0o0oO0Osizer_Shown :#line:2661
            O00000OOOOO00OO0O .vbox1 .Hide (O00000OOOOO00OO0O .oneshotSizer )#line:2662
        O00000OOOOO00OO0O .oneshotsizer_Shown =False #line:2664
        O00000OOOOO00OO0O .ooo0O0o0oO0Osizer_Shown =False #line:2665
        O00000OOOOO00OO0O .SetClientSize ((280 ,240 ))#line:2666
        O00000OOOOO00OO0O .Layout ()#line:2667
    def Oneshot_reset (OO0OOO0O0OOOO000O ):#line:2669
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2670
        OO0OOO0O0OOOO000O .jiajia_time .SetValue (48.0 )#line:2671
        OO0OOO0O0OOOO000O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2672
        OO0OOO0O0OOOO000O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2673
        OO0OOO0O0OOOO000O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2674
        OO0OOO0O0OOOO000O .yanchi_time .SetValue (0.5 )#line:2675
        OO00000o01 =48 #line:2677
        OO00000o02 =55 #line:2678
        one_diff =700 #line:2679
        one_delay =0.5 #line:2680
        one_advance =100 #line:2681
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2683
        one_oO0O0O0O0O0O0O0O01 =OO0OOO0O0OOOO000O .gettime (OO00000o01 )#line:2684
        one_oO0O0O0O0O0O0O0O02 =OO0OOO0O0OOOO000O .gettime (OO00000o02 )#line:2685
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0OOO0O0OOOO000O .gettime (ooo0O0o0oO0O_time1 )#line:2686
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0OOO0O0OOOO000O .gettime (ooo0O0o0oO0O_time2 )#line:2687
    def Secondshot_reset (OO000O0O0OO00O000 ):#line:2690
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2691
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2692
        OO000O0O0OO00O000 .jiajia_time .SetValue (40.0 )#line:2693
        OO000O0O0OO00O000 .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:2694
        OO000O0O0OO00O000 .jiajia_zxco0o0o0o0 .SetValue (500 )#line:2695
        OO000O0O0OO00O000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2696
        OO000O0O0OO00O000 .yanchi_time .SetValue (0.0 )#line:2697
        OO000O0O0OO00O000 .jiajia_time2 .SetValue (50.0 )#line:2699
        OO000O0O0OO00O000 .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:2700
        OO000O0O0OO00O000 .jiajia_zxco0o0o0o02 .SetValue (700 )#line:2701
        OO000O0O0OO00O000 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2702
        OO000O0O0OO00O000 .yanchi_time2 .SetValue (0.5 )#line:2703
        OO00000o01 =40 #line:2705
        OO00000o02 =48 #line:2706
        one_diff =500 #line:2707
        one_delay =0.5 #line:2708
        one_advance =100 #line:2709
        ooo0O0o0oO0O_time1 =50 #line:2711
        ooo0O0o0oO0O_time2 =55.5 #line:2712
        ooo0O0o0oO0O_diff =700 #line:2713
        ooo0O0o0oO0O_delay =0.5 #line:2714
        ooo0O0o0oO0O_advance =100 #line:2715
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2717
        one_oO0O0O0O0O0O0O0O01 =OO000O0O0OO00O000 .gettime (OO00000o01 )#line:2718
        one_oO0O0O0O0O0O0O0O02 =OO000O0O0OO00O000 .gettime (OO00000o02 )#line:2719
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO000O0O0OO00O000 .gettime (ooo0O0o0oO0O_time1 )#line:2720
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO000O0O0OO00O000 .gettime (ooo0O0o0oO0O_time2 )#line:2721
    def Strategy_save (O0O00000OO0OO0000 ,O00O0OOOOO0OO00OO ):#line:2724
        O00000O0OOOO0000O =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:2726
        if O00000O0OOOO0000O .ShowModal ()==wx .ID_OK :#line:2727
            O000000OOOOO0OOOO =O00000O0OOOO0000O .GetValue ()#line:2728
            if O000000OOOOO0OOOO :#line:2729
                OOO00OO0OOO0O000O =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:2730
                if OOO00OO0OOO0O000O ==wx .ID_OK :#line:2731
                    OOO00OO0OOO0O000O .Destroy ()#line:2732
                    O00000O0OOOO0000O .Destroy ()#line:2733
                O0O00000OO0OO0000 .save (O000000OOOOO0OOOO )#line:2734
            else :#line:2735
                OOO00OO0OOO0O000O =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:2736
                if OOO00OO0OOO0O000O ==wx .ID_OK :#line:2737
                    OOO00OO0OOO0O000O .Destroy ()#line:2738
                    O00000O0OOOO0000O .Destroy ()#line:2739
    def save (O0OOO0OO0OOO0O00O ,O00000OO00000OO00 ):#line:2741
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2742
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2743
        global osl ,e_on ,enter_on #line:2744
        if O0OOO0OO0OOO0O00O .select_stractagy .GetSelection ()==2 :#line:2746
            O0OO00O00OO0OO00O =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:2747
            if O0OO00O00OO0OO00O ==wx .ID_OK :#line:2748
                O0OO00O00OO0OO00O .Destroy ()#line:2749
        elif O0OOO0OO0OOO0O00O .select_stractagy .GetSelection ()==0 :#line:2750
            osl [0 ]=0 #line:2751
            osl [1 ]=OO00000o01 #line:2752
            osl [2 ]=OO00000o02 #line:2753
            osl [3 ]=one_diff #line:2754
            osl [4 ]=one_delay #line:2755
            osl [5 ]=one_advance #line:2756
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2757
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2758
            osl [8 ]=ooo0O0o0oO0O_diff #line:2759
            osl [9 ]=ooo0O0o0oO0O_delay #line:2760
            osl [10 ]=ooo0O0o0oO0O_advance #line:2761
            osl [11 ]=e_on #line:2762
            osl [12 ]=enter_on #line:2763
        elif O0OOO0OO0OOO0O00O .select_stractagy .GetSelection ()==1 :#line:2764
            osl [0 ]=1 #line:2765
            osl [0 ]=1 #line:2766
            osl [1 ]=OO00000o01 #line:2767
            osl [2 ]=OO00000o02 #line:2768
            osl [3 ]=one_diff #line:2769
            osl [4 ]=one_delay #line:2770
            osl [5 ]=one_advance #line:2771
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2772
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2773
            osl [8 ]=ooo0O0o0oO0O_diff #line:2774
            osl [9 ]=ooo0O0o0oO0O_delay #line:2775
            osl [10 ]=ooo0O0o0oO0O_advance #line:2776
            osl [11 ]=e_on #line:2777
            osl [12 ]=enter_on #line:2778
        with open ('%s.ghjo0o0o0o0'%O00000OO00000OO00 ,'wb')as O000000OO0O00O0O0 :#line:2779
            pickle .dump (osl ,O000000OO0O00O0O0 )#line:2780
    def Strategy_load (O0O0O0O00O00OO0O0 ,OO0OOOOO00O000O0O ):#line:2795
        import os as OOOOO000OOOOOOOO0 #line:2796
        O00000O0O0O000000 =OOOOO000OOOOOOOO0 .getcwd ()#line:2797
        O0000OO00OOO0O0OO =O0O0O0O00O00OO0O0 .findfiles (O00000O0O0O000000 )#line:2798
        if O0000OO00OOO0O0OO :#line:2799
            O00OO00OO0000OO0O =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =O0000OO00OOO0O0OO )#line:2801
            if O00OO00OO0000OO0O .ShowModal ()==wx .ID_OK :#line:2802
                O00000O0O0O000000 =O00OO00OO0000OO0O .GetStringSelection ()#line:2803
                O0OOOO0000OOO0OO0 =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:2804
                if O0OOOO0000OOO0OO0 .ShowModal ()==wx .ID_OK :#line:2805
                    O0OOOO0000OOO0OO0 .Destroy ()#line:2806
                O0O0O0O00O00OO0O0 .load (O00000O0O0O000000 )#line:2807
            print ("载入")#line:2808
            O00OO00OO0000OO0O .Destroy ()#line:2809
        else :#line:2810
            O0OOOO0000OOO0OO0 =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:2811
            if O0OOOO0000OOO0OO0 ==wx .ID_OK :#line:2812
                O0OOOO0000OOO0OO0 .Destroy ()#line:2813
                O00OO00OO0000OO0O .Destroy ()#line:2814
    def load (O00000000OOO00OO0 ,OOOO00000O000000O ):#line:2816
        global osl ,e_on ,enter_on #line:2817
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2818
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2819
        global ghjo0o0o0o0_on #line:2821
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2822
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2823
        try :#line:2824
            with open (OOOO00000O000000O ,'rb')as O0OO0OO0O00000OOO :#line:2825
                osl =pickle .load (O0OO0OO0O00000OOO )#line:2826
        except :#line:2827
            pass #line:2828
        if osl [0 ]==0 :#line:2829
            O00000000OOO00OO0 .ss_Hide ()#line:2830
            twice =False #line:2833
            ghjo0o0o0o0_on =True #line:2834
            oo0o0O0O0O0_on =True #line:2835
            oOO0O0O0O0O0O0_on =False #line:2836
            oOO0O0O0O0O0O0_num =1 #line:2837
            oOO0O0O0O0O0O0_OK =False #line:2838
            oOO0O0O0O0O0O0_one =False #line:2839
            O00000000OOO00OO0 .select_stractagy .SetSelection (0 )#line:2841
            O00000000OOO00OO0 .jiajia_time .SetValue (osl [1 ])#line:2842
            O00000000OOO00OO0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2843
            O00000000OOO00OO0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2844
            O00000000OOO00OO0 .yanchi_time .SetValue (osl [4 ])#line:2845
            if osl [5 ]==100 :#line:2846
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2847
            elif osl [5 ]==200 :#line:2848
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2849
            else :#line:2850
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2851
            OO00000o01 =osl [1 ]#line:2853
            OO00000o02 =osl [2 ]#line:2854
            one_diff =osl [3 ]#line:2855
            one_delay =osl [4 ]#line:2856
            one_advance =osl [5 ]#line:2857
            e_on =osl [11 ]#line:2859
            enter_on =osl [12 ]#line:2860
            if e_on :#line:2861
                O00000000OOO00OO0 .sdfsf24324297_choice .SetSelection (0 )#line:2862
            elif enter_on :#line:2863
                O00000000OOO00OO0 .sdfsf24324297_choice .SetSelection (1 )#line:2864
            one_oO0O0O0O0O0O0O0O01 =O00000000OOO00OO0 .gettime (OO00000o01 )#line:2866
            one_oO0O0O0O0O0O0O0O02 =O00000000OOO00OO0 .gettime (OO00000o02 )#line:2867
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00000000OOO00OO0 .gettime (ooo0O0o0oO0O_time1 )#line:2868
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00000000OOO00OO0 .gettime (ooo0O0o0oO0O_time2 )#line:2869
        elif osl [0 ]==1 :#line:2871
            ghjo0o0o0o0_on =True #line:2872
            twice =True #line:2873
            oo0o0O0O0O0_on =True #line:2874
            oOO0O0O0O0O0O0_on =False #line:2875
            oOO0O0O0O0O0O0_num =1 #line:2876
            oOO0O0O0O0O0O0_OK =False #line:2877
            oOO0O0O0O0O0O0_one =False #line:2878
            O00000000OOO00OO0 .ss_Shown ()#line:2879
            O00000000OOO00OO0 .select_stractagy .SetSelection (1 )#line:2880
            O00000000OOO00OO0 .jiajia_time .SetValue (osl [1 ])#line:2881
            O00000000OOO00OO0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:2882
            O00000000OOO00OO0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:2883
            O00000000OOO00OO0 .yanchi_time .SetValue (osl [4 ])#line:2884
            if osl [5 ]==100 :#line:2885
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2886
            elif osl [5 ]==200 :#line:2887
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:2888
            else :#line:2889
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2890
            O00000000OOO00OO0 .jiajia_time2 .SetValue (osl [6 ])#line:2891
            O00000000OOO00OO0 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:2892
            O00000000OOO00OO0 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:2893
            O00000000OOO00OO0 .yanchi_time2 .SetValue (osl [9 ])#line:2894
            if osl [10 ]==100 :#line:2895
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2896
            elif osl [10 ]==200 :#line:2897
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:2898
            else :#line:2899
                O00000000OOO00OO0 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:2900
            OO00000o01 =osl [1 ]#line:2903
            OO00000o02 =osl [2 ]#line:2904
            one_diff =osl [3 ]#line:2905
            one_delay =osl [4 ]#line:2906
            one_advance =osl [5 ]#line:2907
            ooo0O0o0oO0O_time1 =osl [6 ]#line:2909
            ooo0O0o0oO0O_time2 =osl [7 ]#line:2910
            ooo0O0o0oO0O_diff =osl [8 ]#line:2911
            ooo0O0o0oO0O_delay =osl [9 ]#line:2912
            ooo0O0o0oO0O_advance =osl [10 ]#line:2913
            e_on =osl [11 ]#line:2915
            enter_on =osl [12 ]#line:2916
            if e_on :#line:2917
                O00000000OOO00OO0 .sdfsf24324297_choice .SetSelection (0 )#line:2918
            elif enter_on :#line:2919
                O00000000OOO00OO0 .sdfsf24324297_choice .SetSelection (1 )#line:2920
            one_oO0O0O0O0O0O0O0O01 =O00000000OOO00OO0 .gettime (OO00000o01 )#line:2922
            one_oO0O0O0O0O0O0O0O02 =O00000000OOO00OO0 .gettime (OO00000o02 )#line:2923
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00000000OOO00OO0 .gettime (ooo0O0o0oO0O_time1 )#line:2924
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00000000OOO00OO0 .gettime (ooo0O0o0oO0O_time2 )#line:2925
    def findfiles (O000O0OOOOOOOO0OO ,OOO00OO0OO0000O00 ):#line:2927
        OOO0O0O0O0O0OOOO0 =[]#line:2928
        for O000O0OO0OOOOO0O0 ,O0OO0O0O0O0O00000 ,O0OOO0O0000O0OO00 in os .walk (OOO00OO0OO0000O00 ):#line:2929
            for OOO0O0OOOO0OO00O0 in O0OOO0O0000O0OO00 :#line:2930
                if os .path .splitext (OOO0O0OOOO0OO00O0 )[1 ]=='.ghjo0o0o0o0':#line:2931
                    OOO0O0O0O0O0OOOO0 .append (os .path .join (O000O0OO0OOOOO0O0 ,OOO0O0OOOO0OO00O0 ))#line:2932
        return OOO0O0O0O0O0OOOO0 #line:2933
    def Save_info (O0000OOO00O0O00O0 ,OOO0OO0O00OOO0000 ):#line:2935
        pass #line:2936
    def changetime (O000OOOOO0000O00O ,O0O00OOOOOO00OOOO ):#line:2941
        OOO0OO00OO00O000O =time .mktime (time .strptime (O0O00OOOOOO00OOOO ,'%Y-%m-%d %H:%M:%S'))#line:2942
        return OOO0OO00OO00O000O #line:2943
    def get_nowtime (OOO0000OOOOO0O00O ):#line:2946
        OOOOO0000OOOO000O =time .time ()#line:2947
        O0000O000OO0O00O0 =time .strftime ('%Y-%m-%d',time .localtime (OOOOO0000OOOO000O ))#line:2948
        return O0000O000OO0O00O0 #line:2949
    def gettime (OOOO00000000OOOO0 ,OOO00O00OO0O0OOOO ):#line:2952
        O0O000O00O0OOOOO0 =OOOO00000000OOOO0 .get_nowtime ()#line:2953
        OOOOO0OO000OOO00O =O0O000O00O0OOOOO0 +' 11:29:'+str (int (OOO00O00OO0O0OOOO ))#line:2954
        OOO000O00OO0O00OO =OOOO00000000OOOO0 .changetime (OOOOO0OO000OOO00O )+float (OOO00O00OO0O0OOOO )-int (OOO00O00OO0O0OOOO )#line:2955
        return OOO000O00OO0O00OO #line:2956
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:2959
    def __init__ (O000O000OOO0O00OO ,O0OO00OO000O0O0O0 ):#line:2960
        wx .Window .__init__ (O000O000OOO0O00OO ,O0OO00OO000O0O0O0 ,size =Timesize )#line:2961
        O000O000OOO0O00OO .Bind (wx .EVT_PAINT ,O000O000OOO0O00OO .OnPaint )#line:2962
        O000O000OOO0O00OO .timer =wx .Timer (O000O000OOO0O00OO )#line:2963
        O000O000OOO0O00OO .Bind (wx .EVT_TIMER ,O000O000OOO0O00OO .OnTimer ,O000O000OOO0O00OO .timer )#line:2964
        O000O000OOO0O00OO .timer .Start (100 )#line:2965
    def Draw (OOOOO00OO0O0O0OO0 ,O0OOO000O00000O0O ):#line:2967
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2968
        OO000000OO0OO0OOO =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2969
        O0O0OOOO0O0OO000O ,OO0OO0O0O0O0OOO0O =OOOOO00OO0O0O0OO0 .GetClientSize ()#line:2970
        O0OOO000O00000O0O .SetBackground (wx .Brush (OOOOO00OO0O0O0OO0 .GetBackgroundColour ()))#line:2971
        O0OOO000O00000O0O .Clear ()#line:2972
        O0OOO000O00000O0O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2973
        OOO0O0OOO0OOO000O ,O00O0OOO0000OOOO0 =O0OOO000O00000O0O .GetTextExtent (OO000000OO0OO0OOO )#line:2974
        O0OOO000O00000O0O .DrawText (OO000000OO0OO0OOO ,(O0O0OOOO0O0OO000O -OOO0O0OOO0OOO000O )/2 ,(OO0OO0O0O0O0OOO0O )/2 -O00O0OOO0000OOOO0 /2 )#line:2975
    def Modify (O0O000OO0OO00O00O ,O0O0O00O0O0O0O0OO ):#line:2977
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:2978
        OOO00O0OOO00O00OO =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2979
        O00OO00O00OO0000O ,OO00OOOO000OO000O =O0O000OO0OO00O00O .GetClientSize ()#line:2980
        O0O0O00O0O0O0O0OO .SetBackground (wx .Brush (O0O000OO0OO00O00O .GetBackgroundColour ()))#line:2981
        O0O0O00O0O0O0O0OO .Clear ()#line:2982
        O0O0O00O0O0O0O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2983
        O00OO00000000OO0O ,O00OOO0O0O00O00O0 =O0O0O00O0O0O0O0OO .GetTextExtent (OOO00O0OOO00O00OO )#line:2984
        O0O0O00O0O0O0O0OO .DrawText (OOO00O0OOO00O00OO ,(O00OO00O00OO0000O -O00OO00000000OO0O )/2 ,(OO00OOOO000OO000O )/2 -O00OOO0O0O00O00O0 /2 )#line:2985
    def OnTimer (O0000OOOOOO000OO0 ,O0OO0OOOOO0O0OO00 ):#line:2987
        OOOOOOOOO0OOOOOOO =wx .BufferedDC (wx .ClientDC (O0000OOOOOO000OO0 ))#line:2988
        O0000OOOOOO000OO0 .Modify (OOOOOOOOO0OOOOOOO )#line:2989
    def OnPaint (O0OO000OOO0O000O0 ,OOOOOOOO0O00OOO00 ):#line:2991
        O00OOO000000OO0OO =wx .BufferedPaintDC (O0OO000OOO0O000O0 )#line:2992
        O0OO000OOO0O000O0 .Draw (O00OOO000000OO0OO )#line:2993
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:2995
    def __init__ (O0OOOOO0O0O0000OO ):#line:2996
         wx .Frame .__init__ (O0OOOOO0O0O0000OO ,None ,title ="wx.Timer",size =(200 ,50 ),pos =O0O0O0O0O0O0Ozxco0o0o0o0frame_pos ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2998
         Lowestzxco0o0o0o0Window (O0OOOOO0O0O0000OO )#line:3001
import string #line:3019
import wx .lib .agw .hyperlink as hyperlink #line:3020
class LoginFrame (wx .Frame ):#line:3021
    def __init__ (O00OOO0O0000O00OO ,OOO0OO0OOO0000000 ,O0OO00O00OOO0OOO0 ,OOOOO00O0O000OO00 ):#line:3022
        wx .Frame .__init__ (O00OOO0O0000O00OO ,None ,-1 ,OOO0OO0OOO0000000 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3023
        O00OOO0O0000O00OO .Bind (wx .EVT_CLOSE ,O00OOO0O0000O00OO .OnClose )#line:3024
        O00OOO0O0000O00OO .panel =wx .Panel (O00OOO0O0000O00OO ,size =(300 ,220 ))#line:3025
        O00OOO0O0000O00OO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3026
        O00OOO0O0000O00OO .SetIcon (O00OOO0O0000O00OO .icon )#line:3027
        O00OOO0O0000O00OO .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3040
        O00OOO0O0000O00OO .welcomelabel =wx .StaticText (O00OOO0O0000O00OO .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3041
        O00OOO0O0000O00OO .sizer_v1 .Add (O00OOO0O0000O00OO .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3042
        O00OOO0O0000O00OO .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3045
        O00OOO0O0000O00OO .userlabel =wx .StaticText (O00OOO0O0000O00OO .panel ,-1 ,label ="账号")#line:3046
        O00OOO0O0000O00OO .userText =wx .TextCtrl (O00OOO0O0000O00OO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3048
        O00OOO0O0000O00OO .userbox .Add (O00OOO0O0000O00OO .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3049
        O00OOO0O0000O00OO .userbox .Add (O00OOO0O0000O00OO .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3050
        O00OOO0O0000O00OO .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3052
        O00OOO0O0000O00OO .passlabel =wx .StaticText (O00OOO0O0000O00OO .panel ,-1 ,label ="密码")#line:3053
        O00OOO0O0000O00OO .passText =wx .TextCtrl (O00OOO0O0000O00OO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3055
        O00OOO0O0000O00OO .passbox .Add (O00OOO0O0000O00OO .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3056
        O00OOO0O0000O00OO .passbox .Add (O00OOO0O0000O00OO .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3057
        if O0OO00O00OOO0OOO0 :#line:3058
            O00OOO0O0000O00OO .userText .SetValue (O0OO00O00OOO0OOO0 )#line:3059
        if OOOOO00O0O000OO00 :#line:3060
            O00OOO0O0000O00OO .passText .SetValue (OOOOO00O0O000OO00 )#line:3061
        O00OOO0O0000O00OO .sizer_v1 .Add (O00OOO0O0000O00OO .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3062
        O00OOO0O0000O00OO .sizer_v1 .Add (O00OOO0O0000O00OO .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3063
        O00OOO0O0000O00OO .Bind (wx .EVT_TEXT_ENTER ,O00OOO0O0000O00OO .OnLogin ,O00OOO0O0000O00OO .userText )#line:3065
        O00OOO0O0000O00OO .Bind (wx .EVT_TEXT_ENTER ,O00OOO0O0000O00OO .OnLogin ,O00OOO0O0000O00OO .passText )#line:3066
        O00OOO0O0000O00OO .o0sdofsfo0sodf0so0btn =wx .Button (O00OOO0O0000O00OO .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3068
        O00OOO0O0000O00OO .loginbtn =wx .Button (O00OOO0O0000O00OO .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3069
        O00OOO0O0000O00OO .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3070
        O00OOO0O0000O00OO .btnSizer .Add (O00OOO0O0000O00OO .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3071
        O00OOO0O0000O00OO .btnSizer .Add (O00OOO0O0000O00OO .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3072
        O00OOO0O0000O00OO .sizer_v1 .Add (O00OOO0O0000O00OO .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3073
        O00OOO0O0000O00OO .loginbtn .Bind (wx .EVT_BUTTON ,O00OOO0O0000O00OO .OnLogin ,O00OOO0O0000O00OO .loginbtn )#line:3074
        O00OOO0O0000O00OO .purchaselink =hyperlink .HyperLinkCtrl (O00OOO0O0000O00OO .panel ,-1 ,u"购买账号")#line:3076
        O00OOO0O0000O00OO .purchaselink .UnsetToolTip ()#line:3077
        O00OOO0O0000O00OO .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O00OOO0O0000O00OO .Purchase )#line:3078
        O00OOO0O0000O00OO .purchaselink .AutoBrowse (False )#line:3079
        O00OOO0O0000O00OO .purchaselink .EnableRollover (True )#line:3080
        O00OOO0O0000O00OO .purchaselink .SetUnderlines (False ,False ,True )#line:3081
        O00OOO0O0000O00OO .purchaselink .OpenInSameWindow (True )#line:3082
        O00OOO0O0000O00OO .purchaselink .UpdateLink ()#line:3083
        O00OOO0O0000O00OO .helplink =hyperlink .HyperLinkCtrl (O00OOO0O0000O00OO .panel ,-1 ,u"查看帮助")#line:3085
        O00OOO0O0000O00OO .helplink .UnsetToolTip ()#line:3086
        O00OOO0O0000O00OO .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O00OOO0O0000O00OO .Purchase )#line:3087
        O00OOO0O0000O00OO .helplink .AutoBrowse (False )#line:3088
        O00OOO0O0000O00OO .helplink .EnableRollover (True )#line:3089
        O00OOO0O0000O00OO .helplink .SetUnderlines (False ,False ,True )#line:3090
        O00OOO0O0000O00OO .helplink .OpenInSameWindow (True )#line:3091
        O00OOO0O0000O00OO .helplink .UpdateLink ()#line:3092
        O00OOO0O0000O00OO .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3094
        O00OOO0O0000O00OO .linkbox .Add (O00OOO0O0000O00OO .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3095
        O00OOO0O0000O00OO .linkbox .Add (O00OOO0O0000O00OO .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3096
        O00OOO0O0000O00OO .sizer_v1 .Add (O00OOO0O0000O00OO .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3097
        O00OOO0O0000O00OO .SetSizer (O00OOO0O0000O00OO .sizer_v1 )#line:3099
        O00OOO0O0000O00OO .Center ()#line:3100
        pub .subscribe (O00OOO0O0000O00OO .connect_success ,"connect")#line:3102
        O00OOO0O0000O00OO .hashthread =HashThread ()#line:3105
    def connect_success (OOOO0OO0O0OOO0OOO ):#line:3107
        OOOO0OO0O0OOO0OOO .loginbtn .Enable ()#line:3108
        global login_result #line:3109
        if login_result =='login success':#line:3110
            OOOO0OO0O0OOO0OOO .Destroy ()#line:3111
            OOOO0OO0O0OOO0OOO .topframe =TopFrame ('沪牌第一枪',version )#line:3112
            OOOO0OO0O0OOO0OOO .topframe .Show (True )#line:3113
        elif login_result =='net error':#line:3115
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3116
        elif login_result =='repeat':#line:3117
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3118
        elif login_result =='wrong account':#line:3119
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3120
        elif login_result =='wrong password':#line:3121
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3122
        else :#line:3123
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3124
    def OnEraseBack (O0O00OO000O000OOO ,OOO00O0O0OO000OO0 ):#line:3127
        OOO0O000O0O00O000 =OOO00O0O0OO000OO0 .GetDC ()#line:3128
        if not OOO0O000O0O00O000 :#line:3129
            OOO0O000O0O00O000 =wx .ClientDC (O0O00OO000O000OOO )#line:3130
            OOO0OOO00O0OO000O =O0O00OO000O000OOO .GetUpdateRegion ().GetBox ()#line:3131
            OOO0O000O0O00O000 .SetClippingRect (OOO0OOO00O0OO000O )#line:3132
        OOO0O000O0O00O000 .Clear ()#line:3133
        O000OO00O000OO0O0 =wx .Bitmap ("blue.jpg")#line:3134
        OOO0O000O0O00O000 .DrawBitmap (O000OO00O000OO0O0 ,0 ,0 )#line:3135
    def OnClose (OOOOO000000OOO0O0 ,O0O0OOO00OOOO0OOO ):#line:3137
        O0O0OOO00OOOO0OOO .Skip ()#line:3138
        sys .exit (None )#line:3139
    def OnLogin (OOO0OO0O000O0OOOO ,OOOO0OO000OOOO00O ):#line:3147
        global Username ,Password #line:3148
        OOO0OO0OOOOO0O000 =OOO0OO0O000O0OOOO .userText .GetValue ()#line:3149
        O00O00OO0OOO000O0 =OOO0OO0O000O0OOOO .passText .GetValue ()#line:3150
        if OOO0OO0OOOOO0O000 =="":#line:3151
            wx .MessageBox ('请输入用户名！')#line:3152
            OOO0OO0O000O0OOOO .userText .SetFocus ()#line:3153
        elif O00O00OO0OOO000O0 =="":#line:3154
            wx .MessageBox ('请输入密码！')#line:3155
            OOO0OO0O000O0OOOO .passText .SetFocus ()#line:3156
        else :#line:3158
            Username =OOO0OO0OOOOO0O000 #line:3159
            Password =O00O00OO0OOO000O0 #line:3160
            OOO0OO0O000O0OOOO .loginthread =LoginThread ()#line:3161
            OO0O0O000OOO0O00O =[OOO0OO0OOOOO0O000 ,O00O00OO0OOO000O0 ]#line:3162
            with open ('your.name','wb')as OOO000OOO000O0000 :#line:3163
                pickle .dump (OO0O0O000OOO0O00O ,OOO000OOO000O0000 )#line:3164
            OOOO0OO000OOOO00O .GetEventObject ().Disable ()#line:3166
    def Purchase (O0O0O00OOOOO0OO00 ,OO00O00OOOOO00000 ):#line:3168
        print ("购买")#line:3169
class UserValidator (wx .Validator ):#line:3173
    ""#line:3174
    def __init__ (O0OOO00O00O00OOOO ,O0O00O0O0000000OO ):#line:3176
        wx .Validator .__init__ (O0OOO00O00O00OOOO )#line:3177
        O0OOO00O00O00OOOO .flag =O0O00O0O0000000OO #line:3178
        O0OOO00O00O00OOOO .Bind (wx .EVT_CHAR ,O0OOO00O00O00OOOO .OnChar )#line:3179
    def Clone (OO0OOO0OO00O0000O ):#line:3182
        ""#line:3183
        return UserValidator (OO0OOO0OO00O0000O .flag )#line:3184
    def Validate (OOO000OOOOOO0OO00 ,O0OOO0OOOOOO0O0OO ):#line:3187
        return True #line:3188
    def TransferToWindow (OOO00O00O000O000O ):#line:3191
        return True #line:3192
    def TransferFromWindow (O0OO0O00OOO00O0OO ):#line:3195
        return True #line:3196
    def OnChar (O0000OO0OO00O00OO ,OOOO0O0O000O000O0 ):#line:3199
        pass #line:3200
class PassValidator (wx .Validator ):#line:3214
    ""#line:3215
    def __init__ (O0O00OO00OO0OOO00 ):#line:3218
        wx .Validator .__init__ (O0O00OO00OO0OOO00 )#line:3219
        O0O00OO00OO0OOO00 .Bind (wx .EVT_CHAR ,O0O00OO00OO0OOO00 .OnChar )#line:3220
    def Clone (OO00OO0OO0OO0OOO0 ):#line:3223
        ""#line:3224
        return PassValidator ()#line:3225
    def Validate (O0O0OOOOOOO0OO000 ,O0O00O0000000O0OO ):#line:3228
        return True #line:3229
    def TransferToWindow (OO0OO0O00000OOO00 ):#line:3232
        return True #line:3233
    def TransferFromWindow (O00O0OO0OO00O0O00 ):#line:3236
        return True #line:3237
    def OnChar (O0O0000O00O0OO000 ,O0000O0OOO000OO0O ):#line:3240
        pass #line:3241
class ConfirmLogin (wx .Frame ):#line:3255
    pass #line:3256
class TimeThread (Thread ):#line:3259
    def __init__ (OO000O0O0OO0O0OOO ):#line:3260
        ""#line:3261
        Thread .__init__ (OO000O0O0OO0O0OOO )#line:3262
        OO000O0O0OO0O0OOO .setDaemon (True )#line:3263
        OO000O0O0OO0O0OOO .start ()#line:3264
    def run (O00000000000OO0OO ):#line:3266
        ""#line:3267
        global a_time #line:3269
        for OOOOOO0O00OOOOO00 in range (1000000 ):#line:3270
            O00O0OOO000OO0O00 =time .clock ()#line:3271
            time .sleep (0.1 )#line:3272
            OOO0OOO000O00OO0O =time .clock ()#line:3273
            a_time +=OOO0OOO000O00OO0O -O00O0OOO000OO0O00 #line:3274
class HashThread (Thread ):#line:3305
    def __init__ (O0O00OO0O000O0O00 ):#line:3306
        ""#line:3307
        Thread .__init__ (O0O00OO0O000O0O00 )#line:3308
        O0O00OO0O000O0O00 .setDaemon (True )#line:3309
        O0O00OO0O000O0O00 .start ()#line:3310
    def run (OO0OO0O0000000OO0 ):#line:3312
        ""#line:3313
        Create_hash ()#line:3315
class findposThread (Thread ):#line:3321
    def __init__ (OO0OOO0O000O0OOOO ):#line:3322
        Thread .__init__ (OO0OOO0O000O0OOOO )#line:3323
        OO0OOO0O000O0OOOO .setDaemon (True )#line:3324
        OO0OOO0O000O0OOOO .start ()#line:3325
    def run (O000O000O00O000O0 ):#line:3327
        findpos ()#line:3328
class sdfsf24324297Thread (Thread ):#line:3331
    def __init__ (O0O00OOO00O000O0O ):#line:3332
        Thread .__init__ (O0O00OOO00O000O0O )#line:3333
        O0O00OOO00O000O0O .setDaemon (True )#line:3334
        O0O00OOO00O000O0O .start ()#line:3335
    def run (OO00OOO0O00000O00 ):#line:3337
        global sdfsf24324297_need ,sdfsf24324297_on #line:3338
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3339
        for OO0OO00O00OO00O00 in range (100 ):#line:3340
            wx .Sleep (0.1 )#line:3341
            if sdfsf24324297_need :#line:3343
                print ("开启查找")#line:3344
                findsdfsf24324297 ()#line:3345
                if sdfsf24324297_on :#line:3346
                    TopFrame .OnClick_sdfsf24324297 ()#line:3347
                    sdfsf24324297_need =False #line:3348
                    sdfsf24324297_on =False #line:3349
                    sdfsf24324297_one =False #line:3350
                    oo0o0O0O0O0_on =True #line:3351
        sdfsf24324297_one =False #line:3352
class uioo0o000ooThread (Thread ):#line:3354
    def __init__ (OO00OO0O000O00O0O ):#line:3355
        Thread .__init__ (OO00OO0O000O00O0O )#line:3356
        OO00OO0O000O00O0O .setDaemon (True )#line:3357
        OO00OO0O000O00O0O .start ()#line:3358
    def run (O00O00OOOO0O0OO00 ):#line:3360
        global sdfsf24324297_need ,sdfsf24324297_on #line:3361
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3362
        for OOO00O000O0000O0O in range (50 ):#line:3363
            if uioo0o000oo_need :#line:3364
                finduioo0o000oo ()#line:3365
                if uioo0o000oo_on :#line:3366
                    TopFrame .OnClick_Shuaxin ()#line:3367
                    uioo0o000oo_on =False #line:3368
                    uioo0o000oo_need =False #line:3369
                    uioo0o000oo_one =False #line:3370
        uioo0o000oo_one =False #line:3371
class LoginThread (Thread ):#line:3376
    def __init__ (O00OO00O000OO0000 ):#line:3377
        ""#line:3378
        Thread .__init__ (O00OO00O000OO0000 )#line:3379
        O00OO00O000OO0000 .setDaemon (True )#line:3380
        O00OO00O000OO0000 .start ()#line:3381
    def run (OO000O000O0OOO000 ):#line:3383
        global Username ,login_result #line:3385
        login_result =ConfirmUser ()#line:3386
        print (login_result )#line:3387
        logging .info ("%s"%login_result )#line:3388
        wx .CallAfter (pub .sendMessage ,"connect")#line:3389
class controlThread (Thread ):#line:3392
    def __init__ (O0O00O00OO0OOOOO0 ):#line:3393
        ""#line:3394
        Thread .__init__ (O0O00O00OO0OOOOO0 )#line:3395
        O0O00O00OO0OOOOO0 .setDaemon (True )#line:3396
        O0O00O00OO0OOOOO0 .start ()#line:3397
    def run (OO0O00OOOO000000O ):#line:3400
        wx .Sleep (10 )#line:3401
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3402
class KeepThread (Thread ):#line:3407
    def __init__ (OOOOO0OOO00OOOOO0 ):#line:3408
        ""#line:3409
        Thread .__init__ (OOOOO0OOO00OOOOO0 )#line:3410
        OOOOO0OOO00OOOOO0 .setDaemon (True )#line:3411
        OOOOO0OOO00OOOOO0 .start ()#line:3412
    def run (O00OO0000OO0OO0O0 ):#line:3415
        for O0OOO00O000OOO0O0 in range (1000000 ):#line:3416
            time .sleep (90 )#line:3417
            Keeplogin ()#line:3418
class TijiaoThread (Thread ):#line:3424
    def __init__ (OO00OO0OO00OO00O0 ):#line:3425
        ""#line:3426
        Thread .__init__ (OO00OO0OO00OO00O0 )#line:3427
        OO00OO0OO00OO00O0 .setDaemon (True )#line:3428
        OO00OO0OO00OO00O0 .start ()#line:3429
    def run (O0O00000OO0OO0OO0 ):#line:3432
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3433
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3434
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3435
        for O0OOOO00O0OOOO0O0 in range (10000000 ):#line:3436
            time .sleep (0.1 )#line:3437
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3441
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3443
                    oOO0O0O0O0O0O0_on =False #line:3444
                    TopFrame .OnClick_Tijiao ()#line:3445
                    oOO0O0O0O0O0O0_on =False #line:3446
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3447
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3448
                    oOO0O0O0O0O0O0_one =True #line:3449
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3450
                    oOO0O0O0O0O0O0_on =False #line:3451
                    TopFrame .OnClick_Tijiao ()#line:3452
                    oOO0O0O0O0O0O0_on =False #line:3453
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3454
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3455
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3456
                    oOO0O0O0O0O0O0_on =False #line:3457
                    oOO0O0O0O0O0O0_on =False #line:3458
                    TopFrame .OnClick_Tijiao ()#line:3459
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3460
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3461
                    oOO0O0O0O0O0O0_one =True #line:3462
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance :#line:3463
                    oOO0O0O0O0O0O0_on =False #line:3464
                    oOO0O0O0O0O0O0_on =False #line:3465
                    TopFrame .OnClick_Tijiao ()#line:3466
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3467
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3468
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3470
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time <=one_oO0O0O0O0O0O0O0O01 +0.2 :#line:3472
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3473
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3474
                    oOO0O0O0O0O0O0_on =True #line:3475
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3476
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3477
                if oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3478
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3479
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3480
                    oOO0O0O0O0O0O0_on =True #line:3481
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3482
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3483
class MoniTijiaoThread (Thread ):#line:3487
    def __init__ (OO0O000OO00OOOOOO ):#line:3488
        ""#line:3489
        Thread .__init__ (OO0O000OO00OOOOOO )#line:3490
        OO0O000OO00OOOOOO .setDaemon (True )#line:3491
        OO0O000OO00OOOOOO .start ()#line:3492
    def run (OO0O0OO0O0O000OOO ):#line:3495
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3496
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3497
        for OOO0OO0O0O000OO0O in range (10000000 ):#line:3498
            time .sleep (0.1 )#line:3499
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3501
                print (oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK )#line:3502
                print (oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ,oOO0O0O0O0O0O0_one )#line:3503
                print (O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 )#line:3504
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3505
                    TopFrame .OnClick_Tijiao ()#line:3506
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3507
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3508
                    oOO0O0O0O0O0O0_on =False #line:3509
                    oOO0O0O0O0O0O0_one =True #line:3510
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3511
                    TopFrame .OnClick_Tijiao ()#line:3512
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3513
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3514
                    oOO0O0O0O0O0O0_on =False #line:3515
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3516
                    oOO0O0O0O0O0O0_on =False #line:3517
                    TopFrame .OnClick_Tijiao ()#line:3518
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3519
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3520
                    oOO0O0O0O0O0O0_one =True #line:3521
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3522
                    oOO0O0O0O0O0O0_on =False #line:3523
                    TopFrame .OnClick_Tijiao ()#line:3524
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3525
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3526
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3531
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=OO00000o01 +0.2 :#line:3532
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3533
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3535
                    oOO0O0O0O0O0O0_on =True #line:3536
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3537
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3538
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3539
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3540
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3542
                    oOO0O0O0O0O0O0_on =True #line:3543
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3544
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3545
class Infoframe (wx .Frame ):#line:3548
    def __init__ (O0O000OOOO000O0OO ,OO0OO0O000O0OOO00 ,O0OO000OO00O000OO ,OO0O00OO00OOOO00O ):#line:3549
        wx .Frame .__init__ (O0O000OOOO000O0OO ,None ,-1 ,OO0OO0O000O0OOO00 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3550
        O0O000OOOO000O0OO .Bind (wx .EVT_CLOSE ,O0O000OOOO000O0OO .OnClose )#line:3551
        O0O000OOOO000O0OO .panel =wx .Panel (O0O000OOOO000O0OO ,size =(300 ,220 ))#line:3552
        O0O000OOOO000O0OO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3553
        O0O000OOOO000O0OO .SetIcon (O0O000OOOO000O0OO .icon )#line:3554
class SketchApp (wx .App ):#line:3557
    def OnInit (O000O0OO0O0O0O0OO ):#line:3558
        try :#line:3569
            with open ("your.name",'rb')as OO0OOO00O000O00OO :#line:3570
                OOOOOOO00O0OOO0O0 =pickle .load (OO0OOO00O000O00OO )#line:3571
                O0O0O00OOOO0O0OO0 =OOOOOOO00O0OOO0O0 [0 ]#line:3572
                O0O0O00O0O0O00O0O =OOOOOOO00O0OOO0O0 [1 ]#line:3573
        except :#line:3574
            O0O0O00OOOO0O0OO0 ='123456'#line:3575
            O0O0O00O0O0O00O0O =0 #line:3576
        OOOOOO0O000O000OO =LoginFrame ('沪牌第一枪',O0O0O00OOOO0O0OO0 ,O0O0O00O0O0O00O0O )#line:3577
        OOOOOO0O000O000OO .Show (True )#line:3578
        return True #line:3579
if __name__ =='__main__':#line:3582
    app =SketchApp ()#line:3583
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
