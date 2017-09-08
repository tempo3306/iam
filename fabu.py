""#line:5
version ='1.71'#line:10
num =0 #line:11
avt =0 #line:12
host_ali ="121.196.220.94"#line:14
url1 ="http://moni.51hupai.org/"#line:17
url2 ="www.baidu.com"#line:18
mainicon ='ico.ico'#line:20
view =False #line:23
do =False #line:24
ad_view =False #line:25
zxco0o0o0o0_view =False #line:27
zxco0o0o0o0_on =False #line:28
zxco0o0o0o0_count =0 #line:29
web_on =False #line:30
view_time =False #line:32
operation_show =False #line:33
time_on =False #line:34
import time #line:35
a_time =time .time ()#line:36
b_time =0 #line:37
o0sdofsfo0sodf0so0_minute =29 #line:39
o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:40
oo0o0O0O0O0_time =0 #line:42
Username =0 #line:44
Password =0 #line:45
o0sdofsfo0sodf0so0_on =False #line:48
ooweo0o0werwr_on =False #line:49
ghjo0o0o0o01 =53 #line:52
ghjo0o0o0o02 =0.0 #line:53
ghjo0o0o0o0_on =True #line:59
ghjo0o0o0o0_repeat =False #line:60
delay =False #line:63
delay_time =0.5 #line:64
login_result =False #line:66
findpos_on =True #line:69
zxco0o0o0o0list =[80000 +O00OO0000O0OOOOOO *100 for O00OO0000O0OOOOOO in range (200 )]#line:71
IDnumber =0 #line:72
account =0 #line:73
passwd =0 #line:74
import pyautogui as pg #line:78
def Create_hash ():#line:80
    with open ('dick.dl','rb')as OOOOOOOOO0OO0OOOO :#line:81
        global dick_hash #line:82
        dick_hash =pickle .load (OOOOOOOOO0OO0OOOO )#line:83
    with open ('cf.btn','rb')as O0O0OOO00OO0OO0OO :#line:84
        global cf_hash #line:85
        cf_hash =pickle .load (O0O0OOO00OO0OO0OO )#line:86
    with open ("target.tkl",'rb')as OOOO0O0OO00OOOOO0 :#line:88
        global dick_target #line:89
        dick_target =pickle .load (OOOO0O0OO00OOOOO0 )#line:90
OO00000o01 =48 #line:95
OO00000o02 =55 #line:96
one_oO0O0O0O0O0O0O0O01 =1000000000000 #line:97
one_oO0O0O0O0O0O0O0O02 =1000000000000 #line:98
one_diff =700 #line:99
one_delay =0.5 #line:100
one_advance =100 #line:101
ooo0O0o0oO0O_time1 =48 #line:104
ooo0O0o0oO0O_time2 =55 #line:105
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =1000000000000 #line:106
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =1000000000000 #line:107
ooo0O0o0oO0O_diff =600 #line:108
ooo0O0o0oO0O_delay =0.5 #line:109
ooo0O0o0oO0O_advance =100 #line:110
osl =[0 ]*15 #line:112
oo0o0O0O0O0_on =True #line:114
oOO0O0O0O0O0O0_on =False #line:115
O0O0O0O0O0O0O_zxco0o0o0o0 =86000 #line:118
own_zxco0o0o0o01 =0 #line:119
own_zxco0o0o0o02 =0 #line:120
own_zxco0o0o0o0 =0 #line:121
oOO0O0O0O0O0O0_OK =False #line:123
e_on =True #line:124
enter_on =False #line:125
twice =False #line:127
oOO0O0O0O0O0O0_num =1 #line:128
oOO0O0O0O0O0O0_one =False #line:129
websize =[902 ,700 ]#line:132
Pxy =pg .size ()#line:133
Px1 =Pxy [0 ]/2 #line:134
Py2 =Pxy [1 ]/2 #line:135
Px =(Pxy [0 ]-websize [0 ])/2 -80 #line:136
Py =(Pxy [1 ]-websize [1 ])/2 #line:137
P_relative =[[343 ,-66 ],[346 ,40 ],[96 ,121 ],[92 ,43 ],[201 ,100 ],[281 ,40 ],[261 ,37 ],[282 ,118 ]]#line:140
P_relative2 =[[647 ,-98 ],[650 ,8 ],[400 ,89 ],[396 ,11 ],[505 ,68 ],[585 ,8 ],[565 ,5 ],[586 ,86 ]]#line:141
Oo0o0Oo0o0o0 =[[0 ,0 ]for O000O0OO00O00O00O in range (len (P_relative ))]#line:142
for i in range (len (Oo0o0Oo0o0o0 )):#line:143
    Oo0o0Oo0o0o0 [i ][0 ]=Px1 +P_relative [i ][0 ]#line:144
    Oo0o0Oo0o0o0 [i ][1 ]=Py2 +P_relative [i ][1 ]#line:145
px_ajust ,py_ajust =0 ,0 #line:148
for i in range (len (P_relative )):#line:149
    P_relative [i ][0 ]+=websize [0 ]/2 +px_ajust #line:150
    P_relative [i ][1 ]+=websize [1 ]/2 +py_ajust #line:151
px_zxco0o0o0o0 =770 -171 #line:153
py_zxco0o0o0o0 =260 #line:154
px_zxco0o0o0o0frame =220 -191 #line:156
py_zxco0o0o0o0frame =480 #line:157
px_timeframe =245 #line:159
py_timeframe =350 #line:160
px_O0O0O0O0O0O0Ozxco0o0o0o0frame =245 #line:162
py_O0O0O0O0O0O0Ozxco0o0o0o0frame =290 #line:163
O0O0O0O0O0O0Ozxco0o0o0o0frame_pos =[px_O0O0O0O0O0O0Ozxco0o0o0o0frame ,py_O0O0O0O0O0O0Ozxco0o0o0o0frame ]#line:164
px_sdfsnisdfafzxcvframe =400 -215 #line:167
py_sdfsnisdfafzxcvframe =460 #line:168
px_mini =200 #line:172
py_mini =40 #line:173
Pricesize =[400 ,80 ]#line:175
Timesize =[200 ,50 ]#line:177
O0O0O0O0O0O0Ozxco0o0o0o0_area =[179 -80 +Px ,424 -50 +Py ,179 +80 +Px ,424 +50 +Py ]#line:180
uioo0o000oo_area =[396 -150 ,11 -100 ,396 +150 ,11 +100 ]#line:181
sdfsf24324297_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:182
Px_zxco0o0o0o0 =Px +px_zxco0o0o0o0 #line:201
Py_zxco0o0o0o0 =Py +py_zxco0o0o0o0 #line:202
Pos_zxco0o0o0o0 =[Px_zxco0o0o0o0 ,Py_zxco0o0o0o0 ,Px_zxco0o0o0o0 +px_mini ,Py_zxco0o0o0o0 +py_mini ]#line:203
Px_zxco0o0o0o0frame =Px +px_zxco0o0o0o0frame #line:206
Py_zxco0o0o0o0frame =Py +py_zxco0o0o0o0frame #line:207
Pos_zxco0o0o0o0frame =[Px_zxco0o0o0o0frame ,Py_zxco0o0o0o0frame ]#line:208
Px_timeframe =px_timeframe #line:211
Py_timeframe =py_timeframe #line:212
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:213
Px_sdfsnisdfafzxcvframe =Px +px_sdfsnisdfafzxcvframe #line:216
Py_sdfsnisdfafzxcvframe =Py +py_sdfsnisdfafzxcvframe #line:217
Pos_sdfsnisdfafzxcvframe =[Px_sdfsnisdfafzxcvframe ,Py_sdfsnisdfafzxcvframe ]#line:218
px_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:226
py_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:227
Px_O0O0O0O0O0O0Ozxco0o0o0o0 =Px +px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:230
Py_O0O0O0O0O0O0Ozxco0o0o0o0 =Py +py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:231
O0O0O0O0O0O0Ozxco0o0o0o0_sizex =41 #line:232
O0O0O0O0O0O0Ozxco0o0o0o0_sizey =16 #line:233
px_relative =49 #line:235
py_relative =0 #line:236
px_sdfsf24324297 =656 #line:238
py_sdfsf24324297 =475 #line:239
Px_sdfsf24324297 =Px +px_sdfsf24324297 #line:240
Py_sdfsf24324297 =Py +py_sdfsf24324297 #line:241
sdfsf24324297_sizex =113 #line:242
sdfsf24324297_sizey =28 #line:243
sdfsf24324297_on =False #line:244
sdfsf24324297_need =False #line:245
sdfsf24324297_one =False #line:246
px_uioo0o000oo =550 #line:248
py_uioo0o000oo =413 #line:249
Px_uioo0o000oo =Px +px_uioo0o000oo #line:250
Py_uioo0o000oo =Py +py_uioo0o000oo #line:251
uioo0o000oo_sizex =108 #line:252
uioo0o000oo_sizey =21 #line:253
uioo0o000oo_on =False #line:254
uioo0o000oo_need =False #line:255
uioo0o000oo_one =False #line:256
oo0o0O0O0O0_interval =False #line:258
oOO0O0O0O0O0O0_interval =False #line:259
query_interval =False #line:260
query_on =False #line:261
import sys #line:264
if sys .platform !='win32':#line:265
    exit ()#line:266
import pyautogui as pg #line:267
import ctypes #line:268
from ctypes import wintypes #line:269
import win32con #line:270
import wx .html2 #line:271
import wx #line:272
import pickle #line:273
import wx .adv #line:274
from PIL import Image #line:275
import imagehash #line:276
import logging #line:354
timenow =time .time ()#line:355
time_local =time .localtime (timenow )#line:357
myapplog =time .strftime ("%Y%m%d%H%M%S",time_local )#line:359
print (myapplog )#line:360
logging .basicConfig (level =logging .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:365
logging .debug ('This is debug message')#line:367
logging .info ('This is info message')#line:368
logging .warning ('This is warning message')#line:369
logging .error ('This is error message')#line:370
import win32gui ,win32api #line:373
import cv2 #line:374
from PIL import ImageGrab #line:375
def Click (OO0O0OO000O00OO0O ,OO0OO0O0000OO0OOO ):#line:377
    O00O0000OO000O0O0 =win32gui .GetCursorPos ()#line:378
    OO0O0OO000O00OO0O =int (OO0O0OO000O00OO0O )#line:379
    OO0OO0O0000OO0OOO =int (OO0OO0O0000OO0OOO )#line:380
    win32api .SetCursorPos ((OO0O0OO000O00OO0O ,OO0OO0O0000OO0OOO ))#line:381
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OO0O0OO000O00OO0O ,OO0OO0O0000OO0OOO ,0 ,0 )#line:382
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OO0O0OO000O00OO0O ,OO0OO0O0000OO0OOO ,0 ,0 )#line:383
def Click2 (OOOO000OO00O0000O ,OOOOO0OOOO0O0O0O0 ):#line:385
    O0O0O00O0O000O0OO =win32gui .GetCursorPos ()#line:386
    OOOO000OO00O0000O =int (OOOO000OO00O0000O )#line:387
    OOOOO0OOOO0O0O0O0 =int (OOOOO0OOOO0O0O0O0 )#line:388
    win32api .SetCursorPos ((OOOO000OO00O0000O ,OOOOO0OOOO0O0O0O0 ))#line:389
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OOOO000OO00O0000O ,OOOOO0OOOO0O0O0O0 ,0 ,0 )#line:390
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OOOO000OO00O0000O ,OOOOO0OOOO0O0O0O0 ,0 ,0 )#line:391
    win32api .SetCursorPos (O0O0O00O0O000O0OO )#line:392
import win32clipboard #line:396
def Paste ():#line:397
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:398
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:399
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:400
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:401
def setText (OO00000OOO0O00000 ):#line:403
    OO00000OOO0O00000 =OO00000OOO0O00000 .encode ('utf-8')#line:404
    win32clipboard .OpenClipboard ()#line:405
    win32clipboard .EmptyClipboard ()#line:406
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,OO00000OOO0O00000 )#line:407
    win32clipboard .CloseClipboard ()#line:408
def Delete ():#line:410
    win32api .keybd_event (0x08 ,0 ,0 ,0 )#line:411
    win32api .keybd_event (0x08 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:412
def findpos ():#line:416
    O000O000OOO00O00O =ImageGrab .grab ().convert ('L')#line:418
    O00OO0000OO00O0O0 =np .asarray (O000O000OOO00O00O )#line:419
    global dick_target #line:420
    OOOO0000OO0O00O00 =dick_target [2 ]#line:421
    O000OO0O0O00000OO ,OO00OOOO0000O0O0O =OOOO0000OO0O00O00 .shape [::-1 ]#line:422
    OO0O00OOOOO000OOO =cv2 .matchTemplate (O00OO0000OO00O0O0 ,OOOO0000OO0O00O00 ,cv2 .TM_CCOEFF_NORMED )#line:424
    O000OO000OO0O0000 ,O0OO00OOO00OOO00O ,OO000OO0OOO000000 ,O0O0O00OOOOO0OOO0 =cv2 .minMaxLoc (OO0O00OOOOO000OOO )#line:425
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:430
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O0O00OOOOO0OOO0 [0 ]+px_relative #line:431
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O0O00OOOOO0OOO0 [1 ]+py_relative #line:432
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:433
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:434
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:436
    for OO000OOO000O00OO0 in range (len (Oo0o0Oo0o0o0 )):#line:437
        Oo0o0Oo0o0o0 [OO000OOO000O00OO0 ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [OO000OOO000O00OO0 ][0 ]#line:438
        Oo0o0Oo0o0o0 [OO000OOO000O00OO0 ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [OO000OOO000O00OO0 ][1 ]#line:439
    uioo0o000oo_area =[396 -150 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -100 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +150 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +100 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:440
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:441
    global findpos_on #line:443
    findpos_on =False #line:444
def finduioo0o000oo ():#line:446
    global dick_target ,uioo0o000oo_on ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:447
    OO000OOO0OO0O0O0O =dick_target [0 ]#line:448
    O000OO000O0OOOO00 =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:449
    O000O0O00O0O00OOO =np .asarray (O000OO000O0OOOO00 )#line:451
    O0OOOO00O0OOO00OO ,OOO0O0OO000O00OO0 =OO000OOO0OO0O0O0O .shape [::-1 ]#line:452
    O0O000O000OO00OOO =cv2 .matchTemplate (O000O0O00O0O00OOO ,OO000OOO0OO0O0O0O ,cv2 .TM_CCOEFF_NORMED )#line:453
    OO0000O00OO000000 ,OOO0O0O0OOO00000O ,O000OOOO00O00OOOO ,OOOO0OOO0OO00O00O =cv2 .minMaxLoc (O0O000O000OO00OOO )#line:454
    print (OOO0O0O0OOO00000O )#line:455
    if OOO0O0O0OOO00000O >=0.6 :#line:456
        uioo0o000oo_on =True #line:457
def findsdfsf24324297 ():#line:460
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:461
    O0OOOO00O000O0000 =dick_target [1 ]#line:462
    OO0OO00O00000OO0O =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:463
    O0OO0O00O0O0OO0O0 =np .asarray (OO0OO00O00000OO0O )#line:464
    OO0OOOOOOO000O0OO ,O0OOO0000OOOOOOOO =O0OOOO00O000O0000 .shape [::-1 ]#line:465
    OOO0O00O000O000O0 =cv2 .matchTemplate (O0OO0O00O0O0OO0O0 ,O0OOOO00O000O0000 ,cv2 .TM_CCOEFF_NORMED )#line:466
    O00O0O0OO00000OOO ,OO0OO000OO0O0OOO0 ,O0OO0O000O0OO0000 ,O0OO0O0O0O0OOOO00 =cv2 .minMaxLoc (OOO0O00O000O000O0 )#line:467
    print (OO0OO000OO0O0OOO0 )#line:468
    if OO0OO000OO0O0OOO0 >=0.9 :#line:469
        sdfsf24324297_on =True #line:470
SZ =20 #line:474
bin_n =16 #line:475
import numpy as np #line:476
def hog (OO0OO000O0OO0000O ):#line:479
    O000OOO0O0000O000 =cv2 .Sobel (OO0OO000O0OO0000O ,cv2 .CV_32F ,1 ,0 )#line:480
    OO00O0OOOOO0OOOOO =cv2 .Sobel (OO0OO000O0OO0000O ,cv2 .CV_32F ,0 ,1 )#line:481
    O000OOO0O0000O0OO ,OO00OO00OOO00000O =cv2 .cartToPolar (O000OOO0O0000O000 ,OO00O0OOOOO0OOOOO )#line:482
    OOOO0O0OOO00OOOOO =np .int32 (bin_n *OO00OO00OOO00000O /(2 *np .pi ))#line:483
    O0OOO00O0OOOO00OO =OOOO0O0OOO00OOOOO [:10 ,:10 ],OOOO0O0OOO00OOOOO [10 :,:10 ],OOOO0O0OOO00OOOOO [:10 ,10 :],OOOO0O0OOO00OOOOO [10 :,10 :]#line:484
    O0OO0O0OOOOOO00OO =O000OOO0O0000O0OO [:10 ,:10 ],O000OOO0O0000O0OO [10 :,:10 ],O000OOO0O0000O0OO [:10 ,10 :],O000OOO0O0000O0OO [10 :,10 :]#line:485
    O0OOO000O00OOO00O =[np .bincount (O00OOOO00O00OO0O0 .ravel (),O0O0000O0OO00O0O0 .ravel (),bin_n )for O00OOOO00O00OO0O0 ,O0O0000O0OO00O0O0 in zip (O0OOO00O0OOOO00OO ,O0OO0O0OOOOOO00OO )]#line:486
    O0OO0OOOO0O00O0OO =np .hstack (O0OOO000O00OOO00O )#line:487
    return O0OO0OOOO0O00O0OO #line:488
def cut (O0O00OOO000O00O00 ):#line:492
    OOO0O0OOO000O0OO0 ,O00OOOOOO000O000O =cv2 .threshold (O0O00OOO000O00O00 ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:493
    OO0OOO0000OO00OO0 ,OOO0000O0O0OOOOO0 ,OO00O00O0O000O000 =cv2 .findContours (O00OOOOOO000O000O ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:495
    OOO00000O00000O00 =[]#line:496
    OOOOOO0OO0O00O0OO =[]#line:497
    for O00OO00000OOOOOO0 in range (len (OOO0000O0O0OOOOO0 )):#line:498
        OOO00OO0000OO0O00 =OOO0000O0O0OOOOO0 [O00OO00000OOOOOO0 ]#line:499
        OO00OO00O00O0000O ,O0O0O0O0OO0O0O0O0 ,O000000OOO0O000O0 ,OO00OO0OOO0OO000O =cv2 .boundingRect (OOO00OO0000OO0O00 )#line:500
        OOOOOO0OO0O00O0OO .append ([OO00OO00O00O0000O ,O0O0O0O0OO0O0O0O0 ,O000000OOO0O000O0 ,OO00OO0OOO0OO000O ])#line:502
    OOOOOO0OO0O00O0OO =sorted (OOOOOO0OO0O00O0OO )#line:504
    for O00OO00000OOOOOO0 in range (len (OOO0000O0O0OOOOO0 )):#line:505
        OO00OO00O00O0000O ,O0O0O0O0OO0O0O0O0 ,O000000OOO0O000O0 ,OO00OO0OOO0OO000O =OOOOOO0OO0O00O0OO [O00OO00000OOOOOO0 ]#line:506
        OOO00000O00000O00 .append (OO0OOO0000OO00OO0 [O0O0O0O0OO0O0O0O0 :O0O0O0O0OO0O0O0O0 +OO00OO0OOO0OO000O ,OO00OO00O00O0000O :OO00OO00O00O0000O +O000000OOO0O000O0 ])#line:507
    return OOO00000O00000O00 #line:508
def readpic (O0O0O0OOOOOO00OO0 ):#line:510
    try :#line:511
        O00O00OOOOOOOO000 =cv2 .ml .SVM_load ('maindata.xml')#line:512
        OOOO0OOO0OO00O0O0 =cut (O0O0O0OOOOOO00OO0 )#line:513
        OOOO0OOO0OO00O0O0 =list (map (hog ,OOOO0OOO0OO00O0O0 ))#line:514
        OOOO0OOO0OO00O0O0 =np .float32 (OOOO0OOO0OO00O0O0 ).reshape (-1 ,64 )#line:515
        OOOO00O0OOOO0O000 =O00O00OOOOOOOO000 .predict (OOOO0OOO0OO00O0O0 )#line:516
        OOOO00O0OOOO0O000 =OOOO00O0OOOO0O000 [1 ].reshape (-1 ).astype (int ).astype (str )#line:517
        OO00OO0OOOOOOO00O ="".join (list (OOOO00O0OOOO0O000 ))#line:518
        return OO00OO0OOOOOOO00O #line:519
    except :#line:520
        return False #line:521
import os #line:527
import socket #line:528
import struct #line:529
import select #line:530
import time #line:531
ICMP_ECHO_REQUEST =8 #line:533
DEFAULT_TIMEOUT =2 #line:534
DEFAULT_COUNT =1 #line:535
class Pinger (object ):#line:538
    ""#line:539
    def __init__ (OOOOO00O0O00O0O00 ,OOO00O0O0OO0OOO0O ,O00O0000O00O00OOO =DEFAULT_COUNT ,O0OO000O0O0O00O00 =DEFAULT_TIMEOUT ):#line:541
        OOOOO00O0O00O0O00 .target_host =OOO00O0O0OO0OOO0O #line:542
        OOOOO00O0O00O0O00 .count =O00O0000O00O00OOO #line:543
        OOOOO00O0O00O0O00 .timeout =O0OO000O0O0O00O00 #line:544
    def do_checksum (O00O0O0OOO00000O0 ,O0O00O0O0O0OOO0O0 ):#line:547
        ""#line:548
        OO0O0OO000OO0000O =0 #line:549
        OOO00O0O00O0OO0O0 =(len (O0O00O0O0O0OOO0O0 )/2 )*2 #line:550
        O0OO0O00O00O0O000 =0 #line:551
        while O0OO0O00O00O0O000 <OOO00O0O00O0OO0O0 :#line:552
            O0OOO000000OO0O0O =O0O00O0O0O0OOO0O0 [O0OO0O00O00O0O000 +1 ]*256 +O0O00O0O0O0OOO0O0 [O0OO0O00O00O0O000 ]#line:553
            OO0O0OO000OO0000O =OO0O0OO000OO0000O +O0OOO000000OO0O0O #line:554
            OO0O0OO000OO0000O =OO0O0OO000OO0000O &0xffffffff #line:555
            O0OO0O00O00O0O000 =O0OO0O00O00O0O000 +2 #line:556
        if OOO00O0O00O0OO0O0 <len (O0O00O0O0O0OOO0O0 ):#line:558
            OO0O0OO000OO0000O =OO0O0OO000OO0000O +O0O00O0O0O0OOO0O0 [len (O0O00O0O0O0OOO0O0 )-1 ]#line:559
            OO0O0OO000OO0000O =OO0O0OO000OO0000O &0xffffffff #line:560
        OO0O0OO000OO0000O =(OO0O0OO000OO0000O >>16 )+(OO0O0OO000OO0000O &0xffff )#line:561
        OO0O0OO000OO0000O =OO0O0OO000OO0000O +(OO0O0OO000OO0000O >>16 )#line:562
        OO00OOO000O00O000 =~OO0O0OO000OO0000O #line:563
        OO00OOO000O00O000 =OO00OOO000O00O000 &0xffff #line:564
        OO00OOO000O00O000 =OO00OOO000O00O000 >>8 |(OO00OOO000O00O000 <<8 &0xff00 )#line:565
        return OO00OOO000O00O000 #line:566
    def receive_ping (OO0000O0OO0000O0O ,O000OOOO0OO000000 ,OOO0OOOOOO00O000O ,O00OOO0O0OOO0O0OO ):#line:568
        OO0OO00O0OOOO0O00 =O00OOO0O0OOO0O0OO #line:569
        while True :#line:570
            O00OO0000O0O00OO0 =time .time ()#line:571
            OO0O0O0O0OO00OOO0 =select .select ([O000OOOO0OO000000 ],[],[],OO0OO00O0OOOO0O00 )#line:572
            OOO0O00O0OOO000O0 =(time .time ()-O00OO0000O0O00OO0 )#line:573
            if OO0O0O0O0OO00OOO0 [0 ]==[]:#line:574
                return #line:575
            O0O00OOOO000OOO00 =time .time ()#line:577
            OO0O0O0000O0O0000 ,OO0O0000O00O0O0O0 =O000OOOO0OO000000 .recvfrom (1024 )#line:578
            O0000000O000O000O =OO0O0O0000O0O0000 [20 :28 ]#line:579
            OOOOOO00O0000O0OO ,O00OOOOOO0OO0OOO0 ,O0OOOO00O0O000000 ,OOOOOOO0O00OO0OO0 ,O00OO0000OO0000O0 =struct .unpack ("bbHHh",O0000000O000O000O )#line:582
            if OOOOOOO0O00OO0OO0 ==OOO0OOOOOO00O000O :#line:583
                OOOO0000O0000OOO0 =struct .calcsize ("d")#line:584
                O00000O0OOO0OO000 =struct .unpack ("d",OO0O0O0000O0O0000 [28 :28 +OOOO0000O0000OOO0 ])[0 ]#line:585
                return O0O00OOOO000OOO00 -O00000O0OOO0OO000 #line:586
            OO0OO00O0OOOO0O00 =OO0OO00O0OOOO0O00 -OOO0O00O0OOO000O0 #line:588
            if OO0OO00O0OOOO0O00 <=0 :#line:589
                return #line:590
    def send_ping (O00000O0OO000O000 ,OOOO0O000O00000O0 ,O000OOOO0OOO00000 ):#line:592
        ""#line:595
        OO000O00OOOO0O0O0 =socket .gethostbyname (O00000O0OO000O000 .target_host )#line:596
        OOO0O00OO0O000OOO =0 #line:598
        OO0O0O00O00OOO000 =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,OOO0O00OO0O000OOO ,O000OOOO0OOO00000 ,1 )#line:601
        O0O0OOOOO0O0O0O00 =struct .calcsize ("d")#line:602
        OO0OOO0000O0O0OO0 =(192 -O0O0OOOOO0O0O0O00 )*"Q"#line:603
        OO0OOO0000O0O0OO0 =struct .pack ("d",time .time ())+bytes (OO0OOO0000O0O0OO0 ,encoding ="utf-8")#line:604
        OOO0O00OO0O000OOO =O00000O0OO000O000 .do_checksum (OO0O0O00O00OOO000 +OO0OOO0000O0O0OO0 )#line:607
        OO0O0O00O00OOO000 =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,socket .htons (OOO0O00OO0O000OOO ),O000OOOO0OOO00000 ,1 )#line:610
        O0O000OOO00OOO0OO =OO0O0O00O00OOO000 +OO0OOO0000O0O0OO0 #line:611
        OOOO0O000O00000O0 .sendto (O0O000OOO00OOO0OO ,(OO000O00OOOO0O0O0 ,1 ))#line:612
    def ping_once (O0OO000O0O0O00OOO ):#line:614
        ""#line:617
        O0OOOO0000O000O00 =socket .getprotobyname ("icmp")#line:618
        try :#line:619
            O000000OOOO00O000 =socket .socket (socket .AF_INET ,socket .SOCK_RAW ,O0OOOO0000O000O00 )#line:620
        except socket .error as OO0000OO000O00O00 :#line:621
            if OO0000OO000O00O00 [0 ]==1 :#line:622
                OO0000OO000O00O00 [1 ]+="ICMP messages can only be sent from root user processes"#line:624
                raise socket .error (OO0000OO000O00O00 [1 ])#line:625
        except Exception as OO0OO000O0O0O0OO0 :#line:626
            print ("Exception: %s"%(OO0OO000O0O0O0OO0 ))#line:627
        O0O0OO000O0OOO0O0 =os .getpid ()&0xFFFF #line:630
        O0OO000O0O0O00OOO .send_ping (O000000OOOO00O000 ,O0O0OO000O0OOO0O0 )#line:632
        O000OO0O0OOOOOO0O =O0OO000O0O0O00OOO .receive_ping (O000000OOOO00O000 ,O0O0OO000O0OOO0O0 ,O0OO000O0O0O00OOO .timeout )#line:633
        O000000OOOO00O000 .close ()#line:634
        return O000OO0O0OOOOOO0O #line:635
    def ping (O0OOOOO000O0OOO0O ):#line:637
        ""#line:640
        for OOOOOO0OOO000O0OO in range (O0OOOOO000O0OOO0O .count ):#line:641
            try :#line:643
                O0OO0O0O0000OOO00 =O0OOOOO000O0OOO0O .ping_once ()#line:644
            except socket .gaierror as O0O0OOOOO00O0O000 :#line:645
                return "timeout"#line:647
            if O0OO0O0O0000OOO00 ==None :#line:649
                return "timeout"#line:651
            else :#line:653
                O0OO0O0O0000OOO00 =O0OO0O0O0000OOO00 *1000 #line:654
                return int (O0OO0O0O0000OOO00 )#line:656
pinger =Pinger (url2 )#line:658
import winreg ,re ,subprocess #line:662
needpath =r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'#line:663
path1 ='C:\Program Files (x86)'#line:664
path2 ='C:\Program Files'#line:665
def getwebpath ():#line:666
    global needpath #line:667
    try :#line:669
        O0O0O00OO0OO0O000 =winreg .OpenKey (winreg .HKEY_CLASSES_ROOT ,r"http\shell\open\command")#line:670
        OOOO00O0O0OOOO000 ,O00000OO00O000OO0 ,OO0000O0OO0OOO0OO =winreg .EnumValue (O0O0O00OO0OO0O000 ,0 )#line:671
        O0OO0OOOOOOO0O00O =re .compile ("\"*(.+\.exe)")#line:672
        O0O0OOOO0000OO0O0 =re .findall (O0OO0OOOOOOO0O00O ,O00000OO00O000OO0 )#line:673
        if O0O0OOOO0000OO0O0 :#line:674
            needpath =O0O0OOOO0000OO0O0 [0 ]#line:675
    except :#line:677
        pass #line:678
    if not os .path .exists (needpath ):#line:679
        if os .path .exists ('C:\Program Files (x86)'):#line:680
            pass #line:681
def openweb (O00O000O0OO0O000O ):#line:683
    global needpath #line:684
    subprocess .Popen ([needpath ,O00O000O0OO0O000O ])#line:687
import smtplib #line:690
from email .mime .text import MIMEText #line:693
import os #line:694
import mimetypes #line:695
import email #line:696
from email .mime .multipart import MIMEMultipart #line:697
from threading import Thread #line:700
import threading #line:701
from wx .lib .pubsub import pub #line:702
import socket ,sys ,json #line:707
timeout =10 #line:708
socket .setdefaulttimeout (timeout )#line:709
def ConfirmUser ():#line:711
    O00OO00O0000O00OO =host_ali #line:712
    O0O0000O0OOOO0OOO =8080 #line:715
    OOO0O0O00O0O0OOOO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:717
    try :#line:719
        OOO0O0O00O0O0OOOO .connect ((O00OO00O0000O00OO ,O0O0000O0OOOO0OOO ))#line:720
    except socket .gaierror as O00O0000OO00O00O0 :#line:721
        logging .error ('连接失败 %s'%O00O0000OO00O00O0 )#line:722
        logging .error ("Address-related error connecting to server: %s"%O00O0000OO00O00O0 )#line:723
        return 'net error'#line:724
    except socket .error as O00O0000OO00O00O0 :#line:726
        logging .error ('连接失败 %s'%O00O0000OO00O00O0 )#line:727
        logging .error ("Connection error: %s"%O00O0000OO00O00O0 )#line:728
        return 'net error'#line:729
    O00OO0000O000OOOO =['login',Username ,Password ]#line:733
    O00OO0000O000OOOO =json .dumps (O00OO0000O000OOOO )#line:734
    O00OO0000O000OOOO =bytes (O00OO0000O000OOOO ,encoding ="utf-8")#line:735
    logging .info ('发送信息 %s'%str (O00OO0000O000OOOO ,encoding ="utf-8"))#line:736
    OOO0O0O00O0O0OOOO .send (O00OO0000O000OOOO )#line:737
    OOO0O0O00O0O0OOOO .shutdown (1 )#line:739
    logging .info ("Submit Complete")#line:740
    print ("Submit Complete")#line:741
    try :#line:742
        O000OOOOOO000OO0O =OOO0O0O00O0O0OOOO .recv (1024 )#line:744
        print (O000OOOOOO000OO0O )#line:745
        O000OOOOOO000OO0O =str (O000OOOOOO000OO0O ,encoding ="utf-8")#line:746
        O000OOOOOO000OO0O =json .loads (O000OOOOOO000OO0O )#line:747
        print ("login_reply%s"%O000OOOOOO000OO0O )#line:748
        O000O0OOOOOO0OOOO =O000OOOOOO000OO0O [0 ]#line:749
        if O000O0OOOOOO0OOOO =='success':#line:750
            logging .info ('登录成功 %s'%O000O0OOOOOO0OOOO )#line:751
            global url2 #line:752
            url2 =O000OOOOOO000OO0O [1 ]#line:753
            return 'login success'#line:754
        elif O000O0OOOOOO0OOOO =='wrong password':#line:755
            logging .warning ('密码错误 %s'%O000O0OOOOOO0OOOO )#line:756
            return 'wrong password'#line:757
        elif O000O0OOOOOO0OOOO =="wrong account":#line:758
            logging .warning ('账号错误 %s'%O000O0OOOOOO0OOOO )#line:759
            return 'wrong account'#line:760
        elif O000O0OOOOOO0OOOO =='repeat':#line:761
            logging .warning ('账号错误 %s'%O000O0OOOOOO0OOOO )#line:762
            return 'repeat'#line:763
    except :#line:764
        print ("连接失败")#line:765
        logging .warning ('连接失败 ')#line:766
        return False #line:767
def Logout ():#line:770
    O0000OOOOO000OO0O =host_ali #line:771
    O000OO0O0O0000O0O =8080 #line:774
    global Username #line:775
    O0O000O0O0O0O0O0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:776
    try :#line:777
        O0O000O0O0O0O0O0O .connect ((O0000OOOOO000OO0O ,O000OO0O0O0000O0O ))#line:778
    except socket .gaierror as OO00OOOO0OOOO0000 :#line:779
        print ("Address-related error connecting to server: %s"%OO00OOOO0OOOO0000 )#line:780
        logging .info ("Address-related error connecting to server: %s"%OO00OOOO0OOOO0000 )#line:781
    except socket .error as OO00OOOO0OOOO0000 :#line:783
        print ("Connection error: %s"%OO00OOOO0OOOO0000 )#line:784
        logging .info ("Connection error: %s"%OO00OOOO0OOOO0000 )#line:785
    OOOO0OO0OOO0O0OO0 =['logout',Username ,Password ]#line:789
    OOOO0OO0OOO0O0OO0 =json .dumps (OOOO0OO0OOO0O0OO0 )#line:790
    OOOO0OO0OOO0O0OO0 =bytes (OOOO0OO0OOO0O0OO0 ,encoding ="utf-8")#line:791
    logging .info ('发送信息 %s'%str (OOOO0OO0OOO0O0OO0 ,encoding ="utf-8"))#line:792
    O0O000O0O0O0O0O0O .send (OOOO0OO0OOO0O0OO0 )#line:793
    O0O000O0O0O0O0O0O .shutdown (1 )#line:794
    print ("Submit Log Out Complete")#line:795
    logging .info ("Submit Log Out Complete")#line:796
def Keeplogin ():#line:799
    O0O0O00OOO00O0000 =host_ali #line:800
    OOOO00OOOO00O00O0 =8080 #line:803
    global Username #line:804
    O0O0O0OO0OO0OOO0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:805
    try :#line:806
        O0O0O0OO0OO0OOO0O .connect ((O0O0O00OOO00O0000 ,OOOO00OOOO00O00O0 ))#line:807
    except socket .gaierror as O0O0000O00OO00O00 :#line:808
        print ("Address-related error connecting to server: %s"%O0O0000O00OO00O00 )#line:809
        logging .info ("Address-related error connecting to server: %s"%O0O0000O00OO00O00 )#line:810
    except socket .error as O0O0000O00OO00O00 :#line:812
        print ("Connection error: %s"%O0O0000O00OO00O00 )#line:813
        logging .info ("Connection error: %s"%O0O0000O00OO00O00 )#line:814
    OO00O000O000O0O0O =['keep',Username ,Password ]#line:818
    OO00O000O000O0O0O =json .dumps (OO00O000O000O0O0O )#line:819
    OO00O000O000O0O0O =bytes (OO00O000O000O0O0O ,encoding ="utf-8")#line:820
    logging .info ('发送信息 %s'%str (OO00O000O000O0O0O ,encoding ="utf-8"))#line:821
    O0O0O0OO0OO0OOO0O .send (OO00O000O000O0O0O )#line:822
    O0O0O0OO0OO0OOO0O .shutdown (1 )#line:824
    print ("Submit keep Complete")#line:825
    logging .info ("Submit keep Complete")#line:826
def send_mail (O00000O000000000O ,OO0O00000000000O0 ,OOO0OOOOOOOO0OO0O ):#line:829
    O000000OOO0O0O00O =open (OOO0OOOOOOOO0OO0O ,'rb')#line:830
    O00OOOO0O00O0OOO0 ,O0O00OOOOO0O00OOO =mimetypes .guess_type (OOO0OOOOOOOO0OO0O )#line:831
    if O00OOOO0O00O0OOO0 is None and O0O00OOOOO0O00OOO is None :#line:832
        O00OOOO0O00O0OOO0 ='application/octet-stream'#line:833
    OO00OO0O0OO00000O ,OO0OO0OO00OO00O00 =O00OOOO0O00O0OOO0 .split ('/',1 )#line:834
    O0OOOO000OO00OO00 =email .mime .base .MIMEBase (OO00OO0O0OO00000O ,OO0OO0OO00OO00O00 )#line:835
    O0OOOO000OO00OO00 .set_payload (O000000OOO0O0O00O .read ())#line:836
    O000000OOO0O0O00O .close ()#line:837
    email .encoders .encode_base64 (O0OOOO000OO00OO00 )#line:838
    O0O000000OOOO00OO =os .path .basename (OOO0OOOOOOOO0OO0O )#line:839
    O0OOOO000OO00OO00 .add_header ('Content-Disposition','attachment',filename =O0O000000OOOO00OO )#line:840
    OO0O00000000000O0 =OO0O00000000000O0 #line:841
    OO0000OO000OOO000 ='smtp.qq.com'#line:842
    O0OO000O0OO0O0OO0 =os .environ .get ('MAIL_USERNAME')#line:843
    OOO0O0000OO0O000O =os .environ .get ('MAIL_PASSWORD')#line:844
    O00OO0O00O0OO0O0O =O0OO000O0OO0O0OO0 #line:845
    OOOOO00O00O00O0O0 =MIMEMultipart ()#line:846
    OOOOO00O00O00O0O0 .attach (O0OOOO000OO00OO00 )#line:847
    OOOOO00O00O00O0O0 ['Subject']=O00000O000000000O #line:848
    OOOOO00O00O00O0O0 ['From']=O00OO0O00O0OO0O0O #line:849
    OOOOO00O00O00O0O0 ['To']=";".join (OO0O00000000000O0 )#line:850
    O0O00OOOO0OO00000 =smtplib .SMTP_SSL (OO0000OO000OOO000 ,465 )#line:851
    O0O00OOOO0OO00000 .login (O0OO000O0OO0O0OO0 ,OOO0O0000OO0O000O )#line:852
    print ('login in  successfully')#line:853
    O0O00OOOO0OO00000 .sendmail (O00OO0O00O0OO0O0O ,OO0O00000000000O0 ,OOOOO00O00O00O0O0 .as_string ())#line:854
    O0O00OOOO0OO00000 .quit ()#line:855
    print ('send email  successfully')#line:856
def Upload ():#line:858
    pass #line:859
def Com_read ():#line:862
    pass #line:863
def Com_decision ():#line:867
    pass #line:868
class TopFrame (wx .Frame ):#line:901
    def __init__ (O00000000O00O0OOO ,OOO0OOO0O0OO0000O ,O00OO00O0O0O0OOO0 ):#line:902
        wx .Frame .__init__ (O00000000O00O0OOO ,None ,1 ,OOO0OOO0O0OO0000O ,size =(320 ,320 ))#line:904
        O00000000O00O0OOO .Bind (wx .EVT_CLOSE ,O00000000O00O0OOO .OnClose )#line:905
        O00000000O00O0OOO .statusbar =O00000000O00O0OOO .CreateStatusBar ()#line:907
        O00000000O00O0OOO .statusbar .SetFieldsCount (3 )#line:909
        O00000000O00O0OOO .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:910
        O00000000O00O0OOO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:912
        O00000000O00O0OOO .SetIcon (O00000000O00O0OOO .icon )#line:913
        O00000000O00O0OOO .statusbar .SetStatusText (u"版本号",0 )#line:915
        O00000000O00O0OOO .statusbar .SetStatusText (u"%s"%O00OO00O0O0O0OOO0 ,1 )#line:918
        O00000000O00O0OOO .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:921
        O00000000O00O0OOO .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:922
        OOO000O000000OOOO =wx .Panel (O00000000O00O0OOO ,-1 )#line:924
        OOO000O000000OOOO .SetBackgroundColour ((240 ,255 ,255 ))#line:926
        O00000000O00O0OOO .SetBackgroundColour ((240 ,255 ,255 ))#line:927
        O00000000O00O0OOO .operationarea =wx .StaticBox (OOO000O000000OOOO ,label ="基本功能")#line:930
        O00000000O00O0OOO .operationareasizer =wx .StaticBoxSizer (O00000000O00O0OOO .operationarea ,wx .VERTICAL )#line:931
        O00000000O00O0OOO .hbox1 =wx .BoxSizer (wx .HORIZONTAL )#line:934
        O00000000O00O0OOO .o0sdofsfo0sodf0so0button =wx .Button (OOO000O000000OOOO ,label ='打开模拟')#line:935
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .Openo0sdofsfo0sodf0so0 ,O00000000O00O0OOO .o0sdofsfo0sodf0so0button )#line:936
        O00000000O00O0OOO .ooweo0o0werwrbutton =wx .Button (OOO000O000000OOOO ,label ='打开国拍')#line:938
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .OpenGuopai ,O00000000O00O0OOO .ooweo0o0werwrbutton )#line:939
        O00000000O00O0OOO .hbox1 .Add (O00000000O00O0OOO .o0sdofsfo0sodf0so0button ,0 ,wx .ALL |wx .CENTER ,5 )#line:940
        O00000000O00O0OOO .hbox1 .Add (O00000000O00O0OOO .ooweo0o0werwrbutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:941
        O00000000O00O0OOO .operationareasizer .Add (O00000000O00O0OOO .hbox1 )#line:942
        O00000000O00O0OOO .helpbutton =wx .Button (OOO000O000000OOOO ,label ='查看帮助')#line:944
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .help ,O00000000O00O0OOO .helpbutton )#line:945
        O00000000O00O0OOO .rulebutton =wx .Button (OOO000O000000OOOO ,label ='查看规定')#line:946
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .rule ,O00000000O00O0OOO .rulebutton )#line:947
        O00000000O00O0OOO .hbox2 =wx .BoxSizer (wx .HORIZONTAL )#line:952
        O00000000O00O0OOO .hbox2 .Add (O00000000O00O0OOO .helpbutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:953
        O00000000O00O0OOO .hbox2 .Add (O00000000O00O0OOO .rulebutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:954
        O00000000O00O0OOO .operationareasizer .Add (O00000000O00O0OOO .hbox2 )#line:955
        O00000000O00O0OOO .set =wx .StaticBox (OOO000O000000OOOO ,label ="常规设置")#line:958
        O00000000O00O0OOO .setsizer =wx .StaticBoxSizer (O00000000O00O0OOO .set )#line:959
        O00000000O00O0OOO .hbox3 =wx .BoxSizer (wx .HORIZONTAL )#line:961
        O00000000O00O0OOO .advanceset =wx .Button (OOO000O000000OOOO ,label ='策略设置')#line:962
        O00000000O00O0OOO .timeautoset =wx .Button (OOO000O000000OOOO ,label ='即将到来')#line:963
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .Advanceset ,O00000000O00O0OOO .advanceset )#line:964
        O00000000O00O0OOO .Bind (wx .EVT_BUTTON ,O00000000O00O0OOO .Timeautoset ,O00000000O00O0OOO .timeautoset )#line:965
        O00000000O00O0OOO .hbox3 .Add (O00000000O00O0OOO .advanceset ,0 ,wx .ALL |wx .CENTER ,5 )#line:966
        O00000000O00O0OOO .hbox3 .Add (O00000000O00O0OOO .timeautoset ,0 ,wx .ALL |wx .CENTER ,5 )#line:967
        O00000000O00O0OOO .setsizer .Add (O00000000O00O0OOO .hbox3 ,0 ,wx .ALL |wx .CENTER ,5 )#line:968
        O00000000O00O0OOO .vbox =wx .BoxSizer (wx .VERTICAL )#line:970
        O00000000O00O0OOO .vbox .Add (O00000000O00O0OOO .operationareasizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:971
        O00000000O00O0OOO .vbox .Add (O00000000O00O0OOO .setsizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:972
        OOO000O000000OOOO .SetSizer (O00000000O00O0OOO .vbox )#line:973
        O00000000O00O0OOO .thread =TimeThread ()#line:985
        O00000000O00O0OOO .keepthread =KeepThread ()#line:986
        O00000000O00O0OOO .operationframe =OperationFrame ()#line:988
        O00000000O00O0OOO .operationframe .Show (False )#line:989
        O00000000O00O0OOO .timer2 =wx .Timer (O00000000O00O0OOO )#line:992
        O00000000O00O0OOO .Bind (wx .EVT_TIMER ,O00000000O00O0OOO .MainControl ,O00000000O00O0OOO .timer2 )#line:993
        O00000000O00O0OOO .timer2 .Start (100 )#line:994
        O00000000O00O0OOO .timer3 =wx .Timer (O00000000O00O0OOO )#line:997
        O00000000O00O0OOO .Bind (wx .EVT_TIMER ,O00000000O00O0OOO .Lowest_zxco0o0o0o0 ,O00000000O00O0OOO .timer3 )#line:998
        O00000000O00O0OOO .timer3 .Start (100 )#line:999
        O00000000O00O0OOO .timer4 =wx .Timer (O00000000O00O0OOO )#line:1001
        O00000000O00O0OOO .Bind (wx .EVT_TIMER ,O00000000O00O0OOO .Find_pos ,O00000000O00O0OOO .timer4 )#line:1002
        O00000000O00O0OOO .timer4 .Start (150 )#line:1003
    def Openo0sdofsfo0sodf0so0 (OO0O00OOOO0OOOO00 ,O0O0OOOO0OOOOO000 ):#line:1015
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1017
        ghjo0o0o0o0_on =True #line:1018
        OOOOOO0O000O000O0 =True #line:1019
        oo0o0O0O0O0_on =True #line:1020
        oOO0O0O0O0O0O0_on =False #line:1021
        oOO0O0O0O0O0O0_num =1 #line:1022
        oOO0O0O0O0O0O0_OK =False #line:1023
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,ooweo0o0werwr_on ,o0sdofsfo0sodf0so0_on ,ghjo0o0o0o0_repeat #line:1024
        if ooweo0o0werwr_on :#line:1025
            wx .MessageBox ('请关闭国拍页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1026
        elif o0sdofsfo0sodf0so0_on :#line:1027
            wx .MessageBox ('请关闭模拟页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1028
        else :#line:1029
            OO0O00OOOO0OOOO00 .Open ()#line:1034
            if do :#line:1035
                o0sdofsfo0sodf0so0_on =True #line:1036
                ad_view =True #line:1037
                web_on =True #line:1038
                OO0O00OOOO0OOOO00 .fr =WebFrame (Px ,Py ,False ,'小鲜肉模拟')#line:1039
                OO0O00OOOO0OOOO00 .operationframe .Show (True )#line:1040
                if time_on :#line:1042
                    OO0O00OOOO0OOOO00 .operationframe .Opentime ()#line:1043
                if not ghjo0o0o0o0_repeat :#line:1044
                    OO0O00OOOO0OOOO00 .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1045
                    OO0O00OOOO0OOOO00 .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1046
                    ghjo0o0o0o0_repeat =True #line:1047
                OOOO0OOO0OOO00000 =wx .html2 .WebView .New (OO0O00OOOO0OOOO00 .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ),style =wx .BORDER_NONE )#line:1050
                OOOO0OOO0OOO00000 .LoadURL (url1 )#line:1051
                OOOO0OOO0OOO00000 .CanSetZoomType (False )#line:1052
                OO0O00OOOO0OOOO00 .fr .Show ()#line:1053
            else :#line:1057
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1058
                OO0O00OOOO0OOOO00 .Close ()#line:1059
            OO0O00OOOO0OOOO00 .Listen ()#line:1060
    def OpenGuopai (O0OOO0OO00O000O0O ,O0O0000000O0O0OO0 ):#line:1062
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1064
        ghjo0o0o0o0_on =True #line:1065
        OOO0OO00OOOOOOO00 =True #line:1066
        oo0o0O0O0O0_on =True #line:1067
        oOO0O0O0O0O0O0_on =False #line:1068
        oOO0O0O0O0O0O0_num =1 #line:1069
        oOO0O0O0O0O0O0_OK =False #line:1070
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1071
        if o0sdofsfo0sodf0so0_on :#line:1072
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1073
        elif ooweo0o0werwr_on :#line:1074
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1075
        else :#line:1076
            O0OOO0OO00O000O0O .Open ()#line:1078
            if do :#line:1082
                ad_view =True #line:1083
                ooweo0o0werwr_on =True #line:1084
                O0OOO0OO00O000O0O .fr =WebFrame (Px ,Py ,False ,'小鲜肉代拍 国拍')#line:1085
                O0OOO0OO00O000O0O .operationframe .Show (True )#line:1086
                if time_on :#line:1088
                    O0OOO0OO00O000O0O .operationframe .Opentime ()#line:1089
                if not ghjo0o0o0o0_repeat :#line:1090
                    O0OOO0OO00O000O0O .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1091
                    O0OOO0OO00O000O0O .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1092
                    ghjo0o0o0o0_repeat =True #line:1093
                OO0O000000O00OOOO =wx .html2 .WebView .New (O0OOO0OO00O000O0O .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ))#line:1095
                OO0O000000O00OOOO .LoadURL (url2 )#line:1096
                OO0O000000O00OOOO .CanSetZoomType (False )#line:1097
                O0OOO0OO00O000O0O .fr .Show ()#line:1098
            else :#line:1102
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1103
                O0OOO0OO00O000O0O .Close ()#line:1104
            O0OOO0OO00O000O0O .Listen ()#line:1105
    def UrlGuopai (O00O0OO00O0OOO000 ,O0OOOOO000O0OO00O ):#line:1107
        global url2 #line:1108
        try :#line:1109
            url2 =O00O0OO00O0OOO000 .urlText .GetValue ()#line:1110
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1111
        except :#line:1112
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1113
    def Help (OOOO000O0000OO000 ,OO00O0OOOOO0O0OO0 ):#line:1115
        O000OO00O000000OO ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1121
        O000O00O0O000OOOO =wx .adv .AboutDialogInfo ()#line:1123
        O000O00O0O000OOOO .SetName ("小鲜肉拍牌")#line:1124
        O000O00O0O000OOOO .SetVersion (O000OO00O000000OO )#line:1125
        O000O00O0O000OOOO .AddDeveloper ("ZS")#line:1129
        wx .adv .AboutBox (O000O00O0O000OOOO )#line:1130
    def rule (OO00OOO0O0O0O0OO0 ,OOO0O00OOO0OOO0OO ):#line:1132
        O0O000OO00OO00O0O ="http://121.196.220.94/coursestudy"#line:1133
        OpenwebThread (O0O000OO00OO00O0O )#line:1134
    def help (OOOO000O0000O0O0O ,O0OO000OO00O00000 ):#line:1135
        O0OOO000O00O0O000 ="http://121.196.220.94/rules"#line:1136
        OpenwebThread (O0OOO000O00O0O000 )#line:1137
    def Yan_practice (O0O00OOOOO0000OOO ,OO0O0O00OO0O000OO ):#line:1139
        pass #line:1140
    def Yan_test (OOO0O0OOOO00000O0 ,OOOO00OOO00O0000O ):#line:1142
        pass #line:1143
    def Time_adjust (OO0OO0000000O0OOO ,O000000OOOO0O000O ):#line:1146
        pass #line:1147
    def Advanceset (O00OO00O0OOO0OO00 ,O0OOOOO000OO0OO0O ):#line:1151
        OOOOOO00OO00O000O =O00OO00O0OOO0OO00 .FindWindowById (2 )#line:1152
        OOOOOO00OO00O000O .Show (True )#line:1153
    def Timeautoset (OO00000O0OO0OO00O ,O0OOOO0O0OOOOO0OO ):#line:1156
        pass #line:1157
    def Lowest_zxco0o0o0o0 (O0O00000000O000O0 ,O00000000OO00OOO0 ):#line:1165
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on #line:1166
        if not findpos_on :#line:1167
            O0OOO00OOO00OO000 =int (TopFrame .Price_read ())#line:1168
            if O0OOO00OOO00OO000 in zxco0o0o0o0list :#line:1170
                O0O0O0O0O0O0O_zxco0o0o0o0 =O0OOO00OOO00OO000 #line:1171
            else :#line:1172
                findpos_on =True #line:1173
    def Find_pos (OO0O0O00OOO00O000 ,O00000O0O00O0OO0O ):#line:1190
        global findpos_on #line:1191
        if findpos_on :#line:1192
            findpos ()#line:1193
    @staticmethod #line:1199
    def Confirm ():#line:1200
        global cf_hash ,sdfsf24324297_on #line:1201
        O00OO00OOO00000O0 =TopFrame .Confirm_hash ()#line:1202
        if O00OO00OOO00000O0 ==cf_hash [0 ]:#line:1203
            sdfsf24324297_on =True #line:1204
    @staticmethod #line:1205
    def Refresh ():#line:1206
        O00OO0000OOOO0OO0 =TopFrame .Refresh_hash ()#line:1207
        global cf_hash ,uioo0o000oo_on #line:1208
        if O00OO0000OOOO0OO0 ==cf_hash [1 ]:#line:1209
            uioo0o000oo_on =True #line:1210
    @staticmethod #line:1213
    def Price_read ():#line:1214
        O00O0000OOOOO0OOO =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:1216
        O00O0000OOOOO0OOO =np .asarray (O00O0000OOOOO0OOO )#line:1222
        OOOOOOOO0000OOOOO =readpic (O00O0000OOOOO0OOO )#line:1223
        return OOOOOOOO0000OOOOO #line:1225
    @staticmethod #line:1228
    def Price_hash ():#line:1229
        OO0O000000O000OO0 =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:1231
        global num #line:1232
        num +=1 #line:1233
        O0000000OO0OO0OOO =imagehash .dhash (OO0O000000O000OO0 )#line:1235
        return O0000000OO0OO0OOO #line:1238
    @staticmethod #line:1240
    def Confirm_hash ():#line:1241
        OO0O00OO000OOOO0O =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:1243
        OO0000000OOO0OO00 =imagehash .dhash (OO0O00OO000OOOO0O )#line:1246
        return OO0000000OOO0OO00 #line:1247
    @staticmethod #line:1249
    def Refresh_hash ():#line:1250
        OO00OOO00000OOOO0 =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:1252
        O000000O0O00OOOOO =imagehash .dhash (OO00OOO00000OOOO0 )#line:1254
        return O000000O0O00OOOOO #line:1255
    @staticmethod #line:1258
    def OnJiajia ():#line:1259
        O0OO0OOO0O000O0OO =pg .position ()#line:1260
        Oo0o0Oo0o0o0 [0 ][0 ]=O0OO0OOO0O000O0OO [0 ]#line:1261
        Oo0o0Oo0o0o0 [0 ][1 ]=O0OO0OOO0O000O0OO [1 ]#line:1262
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1263
        findpos ()#line:1264
    @staticmethod #line:1266
    def OnChujia ():#line:1267
        OOOOO0O0OO0O00O00 =pg .position ()#line:1268
        Oo0o0Oo0o0o0 [1 ][0 ]=OOOOO0O0OO0O00O00 [0 ]#line:1269
        Oo0o0Oo0o0o0 [1 ][1 ]=OOOOO0O0OO0O00O00 [1 ]#line:1270
    @staticmethod #line:1272
    def OnTijiao ():#line:1273
        O0OO00O0O00OO0O0O =pg .position ()#line:1274
        Oo0o0Oo0o0o0 [2 ][0 ]=O0OO00O0O00OO0O0O [0 ]#line:1275
        Oo0o0Oo0o0o0 [2 ][1 ]=O0OO00O0O00OO0O0O [1 ]#line:1276
    @staticmethod #line:1278
    def OnShuaxin ():#line:1279
        O000OO000OO00O000 =pg .position ()#line:1280
        Oo0o0Oo0o0o0 [3 ][0 ]=O000OO000OO00O000 [0 ]#line:1281
        Oo0o0Oo0o0o0 [3 ][1 ]=O000OO000OO00O000 [1 ]#line:1282
    @staticmethod #line:1284
    def OnConfirm ():#line:1285
        O0OO00000O00O00O0 =pg .position ()#line:1286
        Oo0o0Oo0o0o0 [4 ][0 ]=O0OO00000O00O00O0 [0 ]#line:1287
        Oo0o0Oo0o0o0 [4 ][1 ]=O0OO00000O00O00O0 [1 ]#line:1288
    @staticmethod #line:1290
    def OnYanzhengma ():#line:1291
        O000OO000O0O0OOO0 =pg .position ()#line:1292
        Oo0o0Oo0o0o0 [5 ][0 ]=O000OO000O0O0OOO0 [0 ]#line:1293
        Oo0o0Oo0o0o0 [5 ][1 ]=O000OO000O0O0OOO0 [1 ]#line:1294
    @staticmethod #line:1297
    def handle_Jiajia ():#line:1298
        TopFrame .OnJiajia ()#line:1299
    @staticmethod #line:1301
    def handle_Chujia ():#line:1302
        TopFrame .OnChujia ()#line:1303
    @staticmethod #line:1305
    def handle_Tijiao ():#line:1306
        TopFrame .OnTijiao ()#line:1307
    @staticmethod #line:1309
    def handle_Shuaxin ():#line:1310
        TopFrame .OnShuaxin ()#line:1311
    @staticmethod #line:1313
    def handle_Confirm ():#line:1314
        TopFrame .OnConfirm ()#line:1315
    @staticmethod #line:1317
    def handle_Yanzhengma ():#line:1318
        TopFrame .OnYanzhengma ()#line:1319
    @classmethod #line:1327
    def OnClick_Tijiao (O00OOO0000OOOO00O ):#line:1328
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1329
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1330
        sdfsf24324297_need =True #line:1331
        if oOO0O0O0O0O0O0_num ==1 :#line:1333
            OOO00O00OO0OO0O0O =threading .Timer (one_delay ,O00OOO0000OOOO00O .Tijiao )#line:1334
            OOO00O00OO0OO0O0O .start ()#line:1335
            oOO0O0O0O0O0O0_on =False #line:1336
            if twice :#line:1337
                print ("修改为2")#line:1338
                oOO0O0O0O0O0O0_num =2 #line:1339
            print ("成功提交")#line:1341
        elif oOO0O0O0O0O0O0_num ==2 :#line:1342
            oOO0O0O0O0O0O0_num =0 #line:1343
            OOO00O00OO0OO0O0O =threading .Timer (ooo0O0o0oO0O_delay ,O00OOO0000OOOO00O .Tijiao )#line:1344
            OOO00O00OO0OO0O0O .start ()#line:1345
            oOO0O0O0O0O0O0_on =False #line:1346
        else :#line:1348
            O00OOO0000OOOO00O .Tijiao ()#line:1349
    @staticmethod #line:1351
    def Tijiao ():#line:1352
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1353
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1354
        oOO0O0O0O0O0O0_OK =False #line:1355
        global sdfsf24324297_one #line:1356
        if not sdfsf24324297_one :#line:1357
            OO0O0OOOO0OO00OOO =sdfsf24324297Thread ()#line:1358
            sdfsf24324297_one =False #line:1359
    @staticmethod #line:1367
    def OnClick_Shuaxin ():#line:1368
        global web_on #line:1369
        Click (Oo0o0Oo0o0o0 [3 ][0 ],Oo0o0Oo0o0o0 [3 ][1 ])#line:1370
        Click (Oo0o0Oo0o0o0 [5 ][0 ],Oo0o0Oo0o0o0 [5 ][1 ])#line:1371
    @staticmethod #line:1373
    def OnClick_sdfsf24324297 ():#line:1374
        print (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1375
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1376
    @staticmethod #line:1378
    def OnClick_oo0o0O0O0O0 ():#line:1379
        global web_on ,O0O0O0O0O0O0O_zxco0o0o0o0 #line:1380
        global oOO0O0O0O0O0O0_num ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:1381
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on #line:1382
        global uioo0o000oo_need ,uioo0o000oo_one ,oo0o0O0O0O0_interval #line:1383
        print (oo0o0O0O0O0_interval )#line:1384
        if not oo0o0O0O0O0_interval :#line:1385
            print (oOO0O0O0O0O0O0_num ,twice )#line:1386
            oo0o0O0O0O0_interval =True #line:1387
            oOO0O0O0O0O0O0_on =True #line:1388
            uioo0o000oo_need =True #line:1389
            if oOO0O0O0O0O0O0_num ==1 :#line:1390
                own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:1391
                setText (str (own_zxco0o0o0o01 ))#line:1392
                TopFrame .selfdelete ()#line:1393
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1394
                oOO0O0O0O0O0O0_on =True #line:1395
                oo0o0O0O0O0_on =False #line:1396
                oo0o0O0O0O0_interval =False #line:1397
                print (oo0o0O0O0O0_interval )#line:1398
                if not uioo0o000oo_one :#line:1400
                    OO0O00O000OO00OO0 =uioo0o000ooThread ()#line:1401
                    uioo0o000oo_one =True #line:1402
            elif oOO0O0O0O0O0O0_num ==2 and twice :#line:1403
                own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:1405
                setText (str (own_zxco0o0o0o02 ))#line:1406
                TopFrame .selfdelete ()#line:1407
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1408
                oOO0O0O0O0O0O0_on =True #line:1409
                oo0o0O0O0O0_on =False #line:1410
                oo0o0O0O0O0_interval =False #line:1411
                if not uioo0o000oo_one :#line:1412
                    OO0O00O000OO00OO0 =uioo0o000ooThread ()#line:1413
                    uioo0o000oo_one =True #line:1414
    @staticmethod #line:1416
    def selfdelete ():#line:1417
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1418
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1419
        Delete ()#line:1420
        Paste ()#line:1421
    @staticmethod #line:1423
    def selfChujia ():#line:1424
        global zxco0o0o0o0_view ,zxco0o0o0o0_count #line:1430
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1431
        Click (Oo0o0Oo0o0o0 [0 ][0 ],Oo0o0Oo0o0o0 [0 ][1 ])#line:1432
        Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1433
        zxco0o0o0o0_view =True #line:1434
        zxco0o0o0o0_count =0 #line:1435
    @staticmethod #line:1437
    def selfTijiao ():#line:1438
        OperationFrame .Del_shot ()#line:1439
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1440
    @staticmethod #line:1442
    def OnClick_Backspace ():#line:1443
        pg .press ('backspace')#line:1444
    def MainControl (OOOOOO0OOO0000O0O ,OOO0O000OOO0O0O0O ):#line:1446
        if not web_on and time_on :#line:1448
            OOOOOO0OOO0000O0O .operationframe .Closetime ()#line:1449
    @staticmethod #line:1470
    def oOO0O0O0O0O0O0_ok ():#line:1471
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need ,oOO0O0O0O0O0O0_on #line:1472
        if e_on and oOO0O0O0O0O0O0_on :#line:1473
            oOO0O0O0O0O0O0_OK =True #line:1474
            uioo0o000oo_need =False #line:1475
    @staticmethod #line:1477
    def oOO0O0O0O0O0O0_ok2 ():#line:1478
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need #line:1479
        if enter_on and oOO0O0O0O0O0O0_on :#line:1480
            oOO0O0O0O0O0O0_OK =True #line:1481
            uioo0o000oo_need =False #line:1482
    @classmethod #line:1484
    def query (OOO0OOOO0O00O000O ):#line:1485
        global query_interval ,query_on #line:1486
        if not query_interval and not query_on :#line:1487
            query_on =True #line:1489
            query_interval =True #line:1490
            setText (str (1000000 ))#line:1491
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1492
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1493
            Paste ()#line:1494
            Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1495
            OO0O0000O0OO00OOO =threading .Timer (3 ,OOO0OOOO0O00O000O .query_sleep3 )#line:1496
            OO0O0000O0OO00OOO .start ()#line:1497
            OOOO0O000OOO0O000 =threading .Timer (5 ,OOO0OOOO0O00O000O .query_sleep5 )#line:1498
            OOOO0O000OOO0O000 .start ()#line:1499
        elif query_interval and query_on :#line:1500
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1502
            query_on =False #line:1503
    @staticmethod #line:1505
    def query_sleep3 ():#line:1506
        global query_interval ,query_on #line:1508
        if query_on :#line:1509
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1511
            query_on =False #line:1512
    @staticmethod #line:1514
    def query_sleep5 ():#line:1515
        global query_interval #line:1517
        query_interval =False #line:1518
    @staticmethod #line:1522
    def Open ():#line:1523
        global do ,web_on #line:1524
        if not do :#line:1525
            do =True #line:1526
            OO00OO00000OO0O00 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1532
            O0OOO0O0000OOOOO0 =ctypes .windll .user32 #line:1533
            OO0OO0OOOOO00OO0O ={1 :(OO00OO00000OO0O00 ['2'],win32con .MOD_ALT ),2 :(OO00OO00000OO0O00 ['3'],win32con .MOD_ALT ),3 :(OO00OO00000OO0O00 ['4'],win32con .MOD_ALT ),4 :(OO00OO00000OO0O00 ['5'],win32con .MOD_ALT ),5 :(OO00OO00000OO0O00 ['6'],win32con .MOD_ALT ),6 :(OO00OO00000OO0O00 ['7'],win32con .MOD_ALT ),}#line:1537
            OOOOO00000OO000OO ={7 :(OO00OO00000OO0O00 ['s'],0x4000 ),8 :(OO00OO00000OO0O00 ['f'],0x4000 ),9 :(OO00OO00000OO0O00 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OO00OO00000OO0O00 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OO00OO00000OO0O00 ['q'],0x4000 )}#line:1540
            for OO000OO0000O0O0O0 ,(O000OO000OO0O00OO ,OOOOOO0O00OO0O0O0 )in OO0OO0OOOOO00OO0O .items ():#line:1542
                if not O0OOO0O0000OOOOO0 .RegisterHotKey (None ,OO000OO0000O0O0O0 ,OOOOOO0O00OO0O0O0 ,O000OO000OO0O00OO ):#line:1543
                    print ("Unable to register id",OO000OO0000O0O0O0 )#line:1544
                    logging .info ("Unable to register id",OO000OO0000O0O0O0 )#line:1545
                    do =False #line:1546
            for OO000OO0000O0O0O0 ,(O000OO000OO0O00OO ,OOOOOO0O00OO0O0O0 )in OOOOO00000OO000OO .items ():#line:1547
                if not O0OOO0O0000OOOOO0 .RegisterHotKey (None ,OO000OO0000O0O0O0 ,OOOOOO0O00OO0O0O0 ,O000OO000OO0O00OO ):#line:1548
                    print ("Unable to register id",OO000OO0000O0O0O0 )#line:1549
                    logging .info ("Unable to register id",OO000OO0000O0O0O0 )#line:1550
                    do =False #line:1551
                web_on =True #line:1552
    @staticmethod #line:1555
    def Listen ():#line:1556
        try :#line:1557
            OOO0O00OO00O0O0OO ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1562
            O00O0O0OO00O0OO00 ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .selfTijiao ,9 :(lambda :TopFrame .selfChujia ()),10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .query }#line:1568
            OOO00OOOOOOO000O0 =ctypes .windll .user32 #line:1569
            O00OOO00O0O0O00OO =wintypes .MSG ()#line:1570
            OOOOOO0OO0O0OO0O0 =ctypes .byref #line:1571
            while OOO00OOOOOOO000O0 .GetMessageA (OOOOOO0OO0O0OO0O0 (O00OOO00O0O0O00OO ),None ,0 ,0 )!=0 :#line:1572
                if O00OOO00O0O0O00OO .message ==win32con .WM_HOTKEY :#line:1573
                    O0OO0OO000OO0000O =O00O0O0OO00O0OO00 .get (O00OOO00O0O0O00OO .wParam )#line:1574
                    if O0OO0OO000OO0000O :#line:1575
                        O0OO0OO000OO0000O ()#line:1576
                OOO00OOOOOOO000O0 .TranslateMessage (OOOOOO0OO0O0OO0O0 (O00OOO00O0O0O00OO ))#line:1577
                OOO00OOOOOOO000O0 .DispatchMessageA (OOOOOO0OO0O0OO0O0 (O00OOO00O0O0O00OO ))#line:1578
        finally :#line:1579
            pass #line:1580
    @staticmethod #line:1588
    def Close ():#line:1589
        global do #line:1590
        if do :#line:1591
            do =False #line:1592
            O0O00000O00O0000O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1596
            O0OOO000O00000O0O ={1 :(O0O00000O00O0000O ['2'],win32con .MOD_ALT ),2 :(O0O00000O00O0000O ['3'],win32con .MOD_ALT ),3 :(O0O00000O00O0000O ['4'],win32con .MOD_ALT ),4 :(O0O00000O00O0000O ['5'],win32con .MOD_ALT ),5 :(O0O00000O00O0000O ['6'],win32con .MOD_ALT ),6 :(O0O00000O00O0000O ['7'],win32con .MOD_ALT ),}#line:1600
            OO0O00O0O0OOOOOOO =ctypes .windll .user32 #line:1601
            OOO0OOOOO0O0OO00O ={7 :(O0O00000O00O0000O ['s'],0x4000 ),8 :(O0O00000O00O0000O ['f'],0x4000 ),9 :(O0O00000O00O0000O ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O0O00000O00O0000O ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O0O00000O00O0000O ['q'],0x4000 )}#line:1604
            for O000O0000O0OOOOOO in O0OOO000O00000O0O .keys ():#line:1605
                OO0O00O0O0OOOOOOO .UnregisterHotKey (None ,O000O0000O0OOOOOO )#line:1606
            for O000O0000O0OOOOOO in OOO0OOOOO0O0OO00O .keys ():#line:1607
                OO0O00O0O0OOOOOOO .UnregisterHotKey (None ,O000O0000O0OOOOOO )#line:1608
            logging .info ("close assistant success")#line:1609
        else :#line:1610
            pass #line:1611
    def OnEraseBackground (OO0O0OOO0O0000OO0 ,O0O00OO0000OO0OO0 ):#line:1617
        ""#line:1620
        O0O00OO0OOOOO0000 =O0O00OO0000OO0OO0 .GetDC ()#line:1621
        if not O0O00OO0OOOOO0000 :#line:1622
            O0O00OO0OOOOO0000 =wx .ClientDC (OO0O0OOO0O0000OO0 )#line:1623
            OOO000O0O00O0OO0O =OO0O0OOO0O0000OO0 .GetUpdateRegion ().GetBox ()#line:1624
            O0O00OO0OOOOO0000 .SetClippingRect (OOO000O0O00O0OO0O )#line:1625
        O0O00OO0OOOOO0000 .Clear ()#line:1626
        O00OO0O0OO000O00O =wx .Bitmap ("blue.jpg")#line:1627
        O0O00OO0OOOOO0000 .DrawBitmap (O00OO0O0OO000O00O ,0 ,0 )#line:1628
    def OnClose (O0O00O000O0O0O00O ,OO0O00OOO0OO0OO00 ):#line:1641
        O00OOO0OO0000O0O0 =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1642
        if O00OOO0OO0000O0O0 ==wx .OK :#line:1643
            import sys as O0O0OOO0O000OOO0O #line:1645
            O0O00O000O0O0O00O .Show (False )#line:1650
            try :#line:1652
                O0O00O000O0O0O00O .Close_time1 (OO0O00OOO0OO0OO00 )#line:1653
                O0O00O000O0O0O00O .Close_time2 (OO0O00OOO0OO0OO00 )#line:1654
            except :#line:1655
                pass #line:1656
            Logout ()#line:1658
            wx .GetApp ().ExitMainLoop ()#line:1659
            OO0O00OOO0OO0OO00 .Skip ()#line:1660
            O0O0OOO0O000OOO0O .exit (None )#line:1661
    def OnOpenAssist (O0OOOO0000O0O000O ):#line:1669
        O0OOOO0000O0O000O .Open ()#line:1670
        global do #line:1671
        if do :#line:1672
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1673
        else :#line:1674
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1675
        O0OOOO0000O0O000O .Listen ()#line:1676
    @classmethod #line:1678
    def OnCloseAssist (OOO0OO0OO0OOO0OO0 ):#line:1679
        OOO0OO0OO0OOO0OO0 .Close ()#line:1680
    def OnViewPos (O0O0O00O0O000000O ,O00OOOOO0O000O0O0 ):#line:1690
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1691
        O0O0O00O0O000000O .MovePos (O00OOOOO0O000O0O0 )#line:1692
        global view #line:1693
        if not view :#line:1694
            view =True #line:1695
            for O00O0OO00O0000OO0 in range (len (Oo0o0Oo0o0o0 )):#line:1696
                O0O0O00O0O000000O .posframe [O00O0OO00O0000OO0 ].Show (view )#line:1697
        else :#line:1698
            view =False #line:1699
            for O00O0OO00O0000OO0 in range (len (Oo0o0Oo0o0o0 )):#line:1700
                O0O0O00O0O000000O .posframe [O00O0OO00O0000OO0 ].Hide ()#line:1701
    def OnSavePos (OOO0O00O0OO0OOOO0 ,O0OOOO000OO0O0OO0 ):#line:1704
        OOO0O00O0OO0OOOO0 .MovePos (O0OOOO000OO0O0OO0 )#line:1705
        OOO0O00O0OO0OOOO0 .Save_log ()#line:1706
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1707
    def MovePos (O0O0O0OOO00000OO0 ,O0O0O0OO0O000OO0O ):#line:1713
        global Positon #line:1714
        for OO0OO0O0O0OOOO00O in range (5 ):#line:1715
            OOO0000OOOOOOOO00 ,O0O00000OOOOOOOO0 =Oo0o0Oo0o0o0 [OO0OO0O0O0OOOO00O ]#line:1716
            O0O0O0OOO00000OO0 .posframe [OO0OO0O0O0OOOO00O ].Move (OOO0000OOOOOOOO00 -10 ,O0O00000OOOOOOOO0 -5 )#line:1717
    def Save_log (O0O0O00O00O0OO0O0 ):#line:1797
        OO0000OO0O0O00OOO =open ('pos.log','wb')#line:1798
        pickle .dump (Oo0o0Oo0o0o0 ,OO0000OO0O0O00OOO )#line:1799
        OO0000OO0O0O00OOO .close ()#line:1800
    def Confirmlogin (OO000OO000OO00O0O ,OOOO0O0OOO000OOOO ):#line:1880
        Keeplogin ()#line:1881
    def Choose_time1 (O0O0O0O0OO00OO0O0 ,OO00OO0OOO0OOO000 ):#line:1886
        O0O0O0O0OO00OO0O0 .timelabel .SetLabel ("已设定截止时间"+O0O0O0O0OO00OO0O0 .time_choice1 .GetString (O0O0O0O0OO00OO0O0 .time_choice1 .GetSelection ())+'.'+str (O0O0O0O0OO00OO0O0 .time_choice2 .GetSelection ())+" 秒")#line:1889
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1890
        ghjo0o0o0o01 =O0O0O0O0OO00OO0O0 .time_choice1 .GetString (O0O0O0O0OO00OO0O0 .time_choice1 .GetSelection ())#line:1891
        ghjo0o0o0o02 =O0O0O0O0OO00OO0O0 .time_choice2 .GetString (O0O0O0O0OO00OO0O0 .time_choice2 .GetSelection ())#line:1892
    def Choose_time2 (O0OOO0OO0OO00OOOO ,OO0O00OOO00O0O000 ):#line:1895
        O0OOO0OO0OO00OOOO .timelabel .SetLabel ("已设定截止时间"+O0OOO0OO0OO00OOOO .time_choice1 .GetString (O0OOO0OO0OO00OOOO .time_choice1 .GetSelection ())+'.'+str (O0OOO0OO0OO00OOOO .time_choice2 .GetSelection ())+" 秒")#line:1898
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1899
        ghjo0o0o0o01 =O0OOO0OO0OO00OOOO .time_choice1 .GetString (O0OOO0OO0OO00OOOO .time_choice1 .GetSelection ())#line:1900
        ghjo0o0o0o02 =O0OOO0OO0OO00OOOO .time_choice2 .GetString (O0OOO0OO0OO00OOOO .time_choice2 .GetSelection ())#line:1901
class ClockWindow (wx .Panel ):#line:1954
    def __init__ (O0OOOOO00OOO0OOOO ,OOOOO0OOO0OOOOO00 ):#line:1955
        wx .Window .__init__ (O0OOOOO00OOO0OOOO ,OOOOO0OOO0OOOOO00 ,size =Timesize )#line:1956
        O0OOOOO00OOO0OOOO .Bind (wx .EVT_PAINT ,O0OOOOO00OOO0OOOO .OnPaint )#line:1957
        O0OOOOO00OOO0OOOO .timer =wx .Timer (O0OOOOO00OOO0OOOO )#line:1958
        O0OOOOO00OOO0OOOO .Bind (wx .EVT_TIMER ,O0OOOOO00OOO0OOOO .OnTimer ,O0OOOOO00OOO0OOOO .timer )#line:1959
        O0OOOOO00OOO0OOOO .timer .Start (100 )#line:1960
    def Draw (O0000O0000O00OO00 ,OOO0O000O0000O0OO ):#line:1962
        global a_time #line:1963
        OOOOOO0OOO0OOO00O =time .localtime (a_time )#line:1964
        OO00OO000OOOO0O0O =time .strftime ("%H:%M:%S",OOOOOO0OOO0OOO00O )#line:1965
        OO0O0OO0O00OO0O00 ,O000OOOO0O0O0O0O0 =O0000O0000O00OO00 .GetClientSize ()#line:1966
        OOO0O000O0000O0OO .SetBackground (wx .Brush (O0000O0000O00OO00 .GetBackgroundColour ()))#line:1967
        OOO0O000O0000O0OO .Clear ()#line:1968
        OOO0O000O0000O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1969
        OOOO000OOO0O0O000 ,OOO0OOO0O0O000OOO =OOO0O000O0000O0OO .GetTextExtent (OO00OO000OOOO0O0O )#line:1970
        OOO0O000O0000O0OO .DrawText (OO00OO000OOOO0O0O ,(OO0O0OO0O00OO0O00 -OOOO000OOO0O0O000 )/2 ,(O000OOOO0O0O0O0O0 )/2 -OOO0OOO0O0O000OOO /2 )#line:1971
    def Modify (O00OO0OOO000000O0 ,OOO000O0O00O0O0OO ):#line:1973
        global a_time ,b_time #line:1974
        if b_time <9 :#line:1976
            b_time =b_time +1 #line:1977
        else :#line:1978
            b_time =0 #line:1979
        O0OO000O00O0O000O =time .localtime (a_time )#line:1980
        OOOO0O0O0O0OO0O00 =time .strftime ("%H:%M:%S",O0OO000O00O0O000O )#line:1981
        OO0O0OO0O00OOOO0O ,OOO00OO000OO00O0O =O00OO0OOO000000O0 .GetClientSize ()#line:1983
        OOO000O0O00O0O0OO .SetBackground (wx .Brush (O00OO0OOO000000O0 .GetBackgroundColour ()))#line:1984
        OOO000O0O00O0O0OO .Clear ()#line:1985
        OOO000O0O00O0O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:1986
        O000OO00000000OOO ,O0OOO00000O00O0OO =OOO000O0O00O0O0OO .GetTextExtent (OOOO0O0O0O0OO0O00 )#line:1987
        OOO000O0O00O0O0OO .DrawText (OOOO0O0O0O0OO0O00 ,(OO0O0OO0O00OOOO0O -O000OO00000000OOO )/2 ,(OOO00OO000OO00O0O )/2 -O0OOO00000O00O0OO /2 )#line:1988
    def OnTimer (OO0OOO0OOO0OOO00O ,O0O0000000OOOO000 ):#line:1990
        O0OOO0O0O0O0O00OO =wx .BufferedDC (wx .ClientDC (OO0OOO0OOO0OOO00O ))#line:1991
        OO0OOO0OOO0OOO00O .Modify (O0OOO0O0O0O0O00OO )#line:1992
    def OnPaint (OOO0000O0OO0OO000 ,OOOOOOO0O00OOOOOO ):#line:1994
        OOO00OO0O00O000O0 =wx .BufferedPaintDC (OOO0000O0OO0OO000 )#line:1995
        OOO0000O0OO0OO000 .Draw (OOO00OO0O00O000O0 )#line:1996
class TimeFrame (wx .Frame ):#line:2000
    def __init__ (O000000O00O000000 ):#line:2001
        wx .Frame .__init__ (O000000O00O000000 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2003
        ClockWindow (O000000O00O000000 )#line:2006
class MoniClockWindow (wx .Panel ):#line:2011
    def __init__ (O00000O0OO0O0O00O ,OOOO0OOO0000000OO ):#line:2012
        wx .Window .__init__ (O00000O0OO0O0O00O ,OOOO0OOO0000000OO ,size =Timesize )#line:2013
        O00000O0OO0O0O00O .Bind (wx .EVT_PAINT ,O00000O0OO0O0O00O .OnPaint )#line:2014
        O00000O0OO0O0O00O .timer =wx .Timer (O00000O0OO0O0O00O )#line:2015
        O00000O0OO0O0O00O .Bind (wx .EVT_TIMER ,O00000O0OO0O0O00O .OnTimer ,O00000O0OO0O0O00O .timer )#line:2016
        O00000O0OO0O0O00O .timer .Start (100 )#line:2017
    def Draw (O000OO000OOOOO0OO ,OOO0OO000OO0O0O0O ):#line:2019
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2020
        O000O0000O0O00OO0 ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2021
        OO0OO0O0OO0OOOOO0 ,OOO0000O000OOOOOO =O000OO000OOOOO0OO .GetClientSize ()#line:2022
        OOO0OO000OO0O0O0O .SetBackground (wx .Brush (O000OO000OOOOO0OO .GetBackgroundColour ()))#line:2023
        OOO0OO000OO0O0O0O .Clear ()#line:2024
        OOO0OO000OO0O0O0O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2025
        O00OOO00O0OO00O00 ,OOOOOOOOOOOOOOO0O =OOO0OO000OO0O0O0O .GetTextExtent (O000O0000O0O00OO0 )#line:2026
        OOO0OO000OO0O0O0O .DrawText (O000O0000O0O00OO0 ,(OO0OO0O0OO0OOOOO0 -O00OOO00O0OO00O00 )/2 ,(OOO0000O000OOOOOO )/2 -OOOOOOOOOOOOOOO0O /2 )#line:2027
    def Modify (OO00O00O00O0O00OO ,OOOOOO000O0O0OOOO ):#line:2029
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2030
        O00OOOOOOOO0OO0OO =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2032
        O0O0OO0OO00000000 ="%s:%s:%s"%(11 ,29 ,O00OOOOOOOO0OO0OO )#line:2033
        OOOO00O00OO0OO0O0 ,OOOO00OO0O0OOOOO0 =OO00O00O00O0O00OO .GetClientSize ()#line:2034
        OOOOOO000O0O0OOOO .SetBackground (wx .Brush (OO00O00O00O0O00OO .GetBackgroundColour ()))#line:2035
        OOOOOO000O0O0OOOO .Clear ()#line:2036
        OOOOOO000O0O0OOOO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2037
        O000OO000000000OO ,O0O0OOOO0OOO00OOO =OOOOOO000O0O0OOOO .GetTextExtent (O0O0OO0OO00000000 )#line:2038
        OOOOOO000O0O0OOOO .DrawText (O0O0OO0OO00000000 ,(OOOO00O00OO0OO0O0 -O000OO000000000OO )/2 ,(OOOO00OO0O0OOOOO0 )/2 -O0O0OOOO0OOO00OOO /2 )#line:2039
    def OnTimer (O0O00OO0O0OOO000O ,O000O0OO0OO0OOO0O ):#line:2041
        O00OO00O0OO00O0OO =wx .BufferedDC (wx .ClientDC (O0O00OO0O0OOO000O ))#line:2042
        O0O00OO0O0OOO000O .Modify (O00OO00O0OO00O0OO )#line:2043
    def OnPaint (OO0O0OOO00O000OOO ,OO0OOO000OO0OOO0O ):#line:2045
        OO0O0O0OO0O0OO00O =wx .BufferedPaintDC (OO0O0OOO00O000OOO )#line:2046
        OO0O0OOO00O000OOO .Draw (OO0O0O0OO0O0OO00O )#line:2047
class MoniTimeFrame (wx .Frame ):#line:2051
    def __init__ (O0OO00O000OO0OOOO ):#line:2052
        wx .Frame .__init__ (O0OO00O000OO0OOOO ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2054
        MoniClockWindow (O0OO00O000OO0OOOO )#line:2057
class PosFrame (wx .Frame ):#line:2062
    def __init__ (OOO0000000OO0O000 ,O000O0OOO00O00O0O ,OOOO00O0O00OO0000 ):#line:2063
        OO0OO0OO0O00000O0 ,O0O000000000O0OOO =O000O0OOO00O00O0O #line:2064
        wx .Frame .__init__ (OOO0000000OO0O000 ,None ,-1 ,'POS',pos =(OO0OO0OO0O00000O0 -20 ,O0O000000000O0OOO -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:2066
        OO00000OOOOO0OOO0 =wx .Panel (OOO0000000OO0O000 ,-1 ,size =(30 ,20 ))#line:2067
        O00000O00OOOO0O00 =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2069
        O00OO0O0OO00O000O =[]#line:2070
        O00OO0O0OO00O000O .append (wx .StaticText (OO00000OOOOO0OOO0 ,-1 ,OOOO00O0O00OO0000 ,(0 ,0 )))#line:2072
        for O00O0O00O000000OO in range (len (O00OO0O0OO00O000O )):#line:2073
            O00OO0O0OO00O000O [O00O0O00O000000OO ].SetFont (O00000O00OOOO0O00 )#line:2074
class PriceFrame (wx .Frame ):#line:2076
    def __init__ (O0000OO0O0O0OO0OO ,OO00O00O000000O0O ):#line:2077
        wx .Frame .__init__ (O0000OO0O0O0OO0OO ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2080
        O0000OO0O0O0OO0OO .panel =wx .Panel (O0000OO0O0O0OO0OO ,size =Pricesize )#line:2081
        wx .StaticBitmap (O0000OO0O0O0OO0OO .panel ,-1 ,wx .BitmapFromImage (OO00O00O000000O0O ))#line:2083
class YanzhengmaFrame (wx .Frame ):#line:2085
    def __init__ (O0OOO0O00OO00O000 ,OO0000O0O00OO00O0 ):#line:2086
        wx .Frame .__init__ (O0OOO0O00OO00O000 ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2089
        O0OOO0O00OO00O000 .panel =wx .Panel (O0OOO0O00OO00O000 ,size =(400 ,80 ))#line:2090
        wx .StaticBitmap (O0OOO0O00OO00O000 .panel ,-1 ,wx .BitmapFromImage (OO0000O0O00OO00O0 ))#line:2092
class AdFrame (wx .Frame ):#line:2096
    def __init__ (OOOO0O0OOO0OO0OO0 ):#line:2097
        wx .Frame .__init__ (OOOO0O0OOO0OO0OO0 ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2099
        O0OOOO0OOOOOOO0O0 =wx .Panel (OOOO0O0OOO0OO0OO0 ,-1 ,size =(250 ,200 ))#line:2100
        O0OO0OO00O0OOO000 =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2102
        O000OO0O00OO00000 =[]#line:2103
        O000OO0O00OO00000 .append (wx .StaticText (O0OOOO0OOOOOOO0O0 ,-1 ," 专业代拍软件",(15 ,10 )))#line:2105
        O000OO0O00OO00000 .append (wx .StaticText (O0OOOO0OOOOOOO0O0 ,-1 ," 专业代拍团队",(15 ,60 )))#line:2107
        O000OO0O00OO00000 .append (wx .StaticText (O0OOOO0OOOOOOO0O0 ,-1 ,"关注微信公众号",(15 ,110 )))#line:2109
        O000OO0O00OO00000 .append (wx .StaticText (O0OOOO0OOOOOOO0O0 ,-1 ," 小鲜肉拍牌",(15 ,160 )))#line:2111
        for OO0OO000OOO000O0O in range (len (O000OO0O00OO00000 )):#line:2112
            O000OO0O00OO00000 [OO0OO000OOO000O0O ].SetFont (O0OO0OO00O0OOO000 )#line:2113
class WebFrame (wx .Frame ):#line:2115
    def __init__ (O0O0O0000O00OO000 ,O000O000000OO000O ,OO000O0O00OOO000O ,O0O0O0OO000O0OOO0 ,OOO000OOOOO0OO000 ):#line:2116
        wx .Frame .__init__ (O0O0O0000O00OO000 ,None ,-1 ,OOO000OOOOO0OO000 ,size =(websize [0 ],websize [1 ]),pos =(O000O000000OO000O ,OO000O0O00OOO000O ),style =wx .SIMPLE_BORDER )#line:2117
        if O0O0O0OO000O0OOO0 :#line:2122
            O0O0O0000O00OO000 .adframe =AdFrame ()#line:2123
            O0O0O0000O00OO000 .adframe .Show (True )#line:2124
        O0O0O0000O00OO000 .Bind (wx .EVT_CLOSE ,O0O0O0000O00OO000 .OnClose )#line:2125
        O0O0O0000O00OO000 .ad2 =O0O0O0OO000O0OOO0 #line:2126
        O0O0O0000O00OO000 .control =ControlFrame ()#line:2127
        O0O0O0000O00OO000 .control .Show (True )#line:2128
        pub .subscribe (O0O0O0000O00OO000 .OnClose2 ,"close web")#line:2153
    def OnClose (OO00OOOO0O0O0O0OO ,OOO0OOOO00O0000O0 ):#line:2154
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2155
        web_on =False #line:2156
        view_time =False #line:2157
        o0sdofsfo0sodf0so0_on =False #line:2158
        ooweo0o0werwr_on =False #line:2159
        TopFrame .Close ()#line:2160
        O0OOOO00OOOOOOO0O ="sc_new.png"#line:2161
        if os .path .exists (O0OOOO00OOOOOOO0O ):#line:2162
            os .remove (O0OOOO00OOOOOOO0O )#line:2163
        OO00OOOO0O0O0O0OO .Destroy ()#line:2164
        if OO00OOOO0O0O0O0OO .ad2 :#line:2165
            OO00OOOO0O0O0O0OO .adframe .Destroy ()#line:2166
        OOO0OOOO00O0000O0 .Skip ()#line:2167
    def OnClose2 (O0O0OO0OO000OO0O0 ):#line:2169
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2170
        web_on =False #line:2171
        view_time =False #line:2172
        o0sdofsfo0sodf0so0_on =False #line:2173
        ooweo0o0werwr_on =False #line:2174
        TopFrame .Close ()#line:2175
        O0OOOOOOOOOOO000O ="sc_new.png"#line:2176
        if os .path .exists (O0OOOOOOOOOOO000O ):#line:2177
            os .remove (O0OOOOOOOOOOO000O )#line:2178
        O0O0OO0OO000OO0O0 .Destroy ()#line:2179
        if O0O0OO0OO000OO0O0 .ad2 :#line:2180
            O0O0OO0OO000OO0O0 .adframe .Destroy ()#line:2181
class ControlFrame (wx .Frame ):#line:2184
    def __init__ (OO00OOO00O0OO0O00 ):#line:2185
        wx .Frame .__init__ (OO00OOO00O0OO0O00 ,None ,-1 ,size =(330 ,270 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +40 ,Py +480 ))#line:2187
        OO00OOO00O0OO0O00 .panel =wx .Panel (OO00OOO00O0OO0O00 ,-1 ,size =(330 ,270 ))#line:2188
        OO0O000OOOOOO0O0O =wx .Font (25 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2191
        O0000OOO0000O000O =wx .Font (15 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2192
        OO00OOO00O0OO0O00 .adtext =wx .StaticText (OO00OOO00O0OO0O00 .panel ,label =u"小鲜肉代拍",pos =(90 ,20 ))#line:2193
        OO00OOO00O0OO0O00 .adtext .SetFont (OO0O000OOOOOO0O0O )#line:2194
        OO00OOO00O0OO0O00 .zxco0o0o0o0text =wx .StaticText (OO00OOO00O0OO0O00 .panel ,label =u"最低成交价:",pos =(50 ,90 ))#line:2195
        OO00OOO00O0OO0O00 .zxco0o0o0o0text .SetFont (O0000OOO0000O000O )#line:2196
        OO00OOO00O0OO0O00 .zxco0o0o0o0 =wx .StaticText (OO00OOO00O0OO0O00 .panel ,pos =(190 ,90 ))#line:2197
        OO00OOO00O0OO0O00 .zxco0o0o0o0 .SetFont (O0000OOO0000O000O )#line:2198
        OO00OOO00O0OO0O00 .timetext =wx .StaticText (OO00OOO00O0OO0O00 .panel ,label =u"当前时间:",pos =(50 ,130 ))#line:2199
        OO00OOO00O0OO0O00 .timetext .SetFont (O0000OOO0000O000O )#line:2200
        OO00OOO00O0OO0O00 .time =wx .StaticText (OO00OOO00O0OO0O00 .panel ,pos =(190 ,130 ))#line:2201
        OO00OOO00O0OO0O00 .time .SetFont (O0000OOO0000O000O )#line:2202
        OO00OOO00O0OO0O00 .netstattext =wx .StaticText (OO00OOO00O0OO0O00 .panel ,pos =(80 ,170 ),label =u"网速")#line:2204
        OO00OOO00O0OO0O00 .netstattext .SetFont (O0000OOO0000O000O )#line:2205
        OO00OOO00O0OO0O00 .netstat =wx .StaticText (OO00OOO00O0OO0O00 .panel ,pos =(190 ,170 ))#line:2206
        OO00OOO00O0OO0O00 .timetimer1 =wx .Timer (OO00OOO00O0OO0O00 )#line:2210
        OO00OOO00O0OO0O00 .Bind (wx .EVT_TIMER ,OO00OOO00O0OO0O00 .Timego ,OO00OOO00O0OO0O00 .timetimer1 )#line:2211
        OO00OOO00O0OO0O00 .timetimer1 .Start (100 )#line:2212
    def o_closeweb (O0O0OOO0000OO0000 ,OOO0OOO00OOOOOO0O ):#line:2213
        wx .CallAfter (pub .sendMessage ,"close web")#line:2214
        O0O0OOO0000OO0000 .Destroy ()#line:2215
        OOO0OOO00OOOOOO0O .Skip ()#line:2216
    def Timego (OOO0OO00000OOOOO0 ,OO00OOO00OO0O0O00 ):#line:2218
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,a_time #line:2219
        OOO0OO00000OOOOO0 .zxco0o0o0o0 .SetLabel ("%s"%O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2220
        if o0sdofsfo0sodf0so0_on :#line:2221
            OOO0OO00000OOOOO0 .time .SetLabel ("11:29:%s"%int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:2222
        else :#line:2223
            O00OO0000OO0O0O00 =time .localtime (a_time )#line:2224
            OOO0OOOOOOO0OOOO0 =time .strftime ("%H:%M:%S",O00OO0000OO0O0O00 )#line:2225
            OOO0OO00000OOOOO0 .time .SetLabel (OOO0OOOOOOO0OOOO0 )#line:2226
        global pinger #line:2227
        O0O0OOO0O000000O0 =pinger .ping ()#line:2228
        if O0O0OOO0O000000O0 =="timeout":#line:2229
            OOO0OO00000OOOOO0 .netstat .SetLabel ("%s"%O0O0OOO0O000000O0 )#line:2230
        else :#line:2231
            OOO0OO00000OOOOO0 .netstat .SetLabel ("%sms"%O0O0OOO0O000000O0 )#line:2232
class OperationFrame (wx .Frame ):#line:2235
    def __init__ (O00O0O0000OOO0O00 ):#line:2236
        wx .Frame .__init__ (O00O0O0000OOO0O00 ,None ,2 ,title ="小鲜肉代拍",pos =(1070 ,100 ),size =(300 ,425 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION |wx .CLOSE_BOX )#line:2238
        O00O0O0000OOO0O00 .Bind (wx .EVT_CLOSE ,O00O0O0000OOO0O00 .OnClose )#line:2240
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2242
        one_oO0O0O0O0O0O0O0O01 =O00O0O0000OOO0O00 .gettime (OO00000o01 )#line:2243
        one_oO0O0O0O0O0O0O0O02 =O00O0O0000OOO0O00 .gettime (OO00000o02 )#line:2244
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00O0O0000OOO0O00 .gettime (ooo0O0o0oO0O_time1 )#line:2245
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00O0O0000OOO0O00 .gettime (ooo0O0o0oO0O_time2 )#line:2246
        O00O0O0000OOO0O00 .timer1 =wx .Timer (O00O0O0000OOO0O00 )#line:2248
        O00O0O0000OOO0O00 .Bind (wx .EVT_TIMER ,O00O0O0000OOO0O00 .Price_view ,O00O0O0000OOO0O00 .timer1 )#line:2249
        O00O0O0000OOO0O00 .timer1 .Start (500 )#line:2250
        O00O0O0000OOO0O00 .timer2 =wx .Timer (O00O0O0000OOO0O00 )#line:2252
        O00O0O0000OOO0O00 .Bind (wx .EVT_TIMER ,O00O0O0000OOO0O00 .Price_count ,O00O0O0000OOO0O00 .timer2 )#line:2253
        O00O0O0000OOO0O00 .timer2 .Start (100 )#line:2254
        O00O0O0000OOO0O00 .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:2256
        O00O0O0000OOO0O00 .O0O0O0O0O0O0Oframe .Show (False )#line:2257
        OO000OOOOO00OOOOO =wx .Panel (O00O0O0000OOO0O00 ,-1 ,size =(300 ,380 ))#line:2261
        OO0OO000OOO0O0OOO =wx .StaticBox (OO000OOOOO00OOOOO ,-1 ,u'选择策略:')#line:2262
        O00O0O0000OOO0O00 .stractagySizer =wx .StaticBoxSizer (OO0OO000OOO0O0OOO ,wx .VERTICAL )#line:2263
        OO00O0OO0O0OOO0OO =wx .StaticText (OO000OOOOO00OOOOO ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2264
        OOO0O0O00O0OO0O0O =wx .BoxSizer (wx .HORIZONTAL )#line:2265
        OOO0O0O00O0OO0O0O .Add (OO00O0OO0O0OOO0OO )#line:2266
        OOO00OOOO0O000OOO =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2271
        O00O0O0000OOO0O00 .select_stractagy =wx .Choice (OO000OOOOO00OOOOO ,-1 ,choices =OOO00OOOO0O000OOO ,size =(100 ,50 ))#line:2272
        OOO0O0O00O0OO0O0O .Add (O00O0O0000OOO0O00 .select_stractagy )#line:2273
        O00O0O0000OOO0O00 .select_stractagy .SetSelection (0 )#line:2274
        O00O0O0000OOO0O00 .timeview =wx .CheckBox (OO000OOOOO00OOOOO ,-1 ,label =u'显示时间')#line:2276
        O0OOOOO0OOOOOOO00 =wx .BoxSizer (wx .HORIZONTAL )#line:2277
        O0OOOOO0OOOOOOO00 .Add (O00O0O0000OOO0O00 .timeview )#line:2278
        O00O0O0000OOO0O00 .button1 =wx .Button (OO000OOOOO00OOOOO ,label ='+1s',size =(35 ,25 ))#line:2281
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Add_ooo0O0o0oO0O ,O00O0O0000OOO0O00 .button1 )#line:2282
        O00O0O0000OOO0O00 .button2 =wx .Button (OO000OOOOO00OOOOO ,label ='-1s',size =(35 ,25 ))#line:2283
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Minus_ooo0O0o0oO0O ,O00O0O0000OOO0O00 .button2 )#line:2284
        O00O0O0000OOO0O00 .button3 =wx .Button (OO000OOOOO00OOOOO ,label ='+0.1s',size =(35 ,25 ))#line:2285
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Add_time ,O00O0O0000OOO0O00 .button3 )#line:2286
        O00O0O0000OOO0O00 .button4 =wx .Button (OO000OOOOO00OOOOO ,label ='-0.1s',size =(35 ,25 ))#line:2287
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Minus_time ,O00O0O0000OOO0O00 .button4 )#line:2288
        O0OOOOO0OOOOOOO00 .Add (O00O0O0000OOO0O00 .button1 )#line:2290
        O0OOOOO0OOOOOOO00 .Add (O00O0O0000OOO0O00 .button2 )#line:2291
        O0OOOOO0OOOOOOO00 .Add (O00O0O0000OOO0O00 .button3 )#line:2292
        O0OOOOO0OOOOOOO00 .Add (O00O0O0000OOO0O00 .button4 )#line:2293
        O000O0000O0O0O00O =wx .BoxSizer (wx .VERTICAL )#line:2295
        O000O0000O0O0O00O .Add (OOO0O0O00O0OO0O0O )#line:2296
        O000O0000O0O0O00O .Add (O0OOOOO0OOOOOOO00 )#line:2297
        OO0OOOOO0O00OOO0O =["E键","回车"]#line:2300
        O00O0O0000OOO0O00 .sdfsf24324297_choice =wx .Choice (OO000OOOOO00OOOOO ,-1 ,choices =OO0OOOOO0O00OOO0O )#line:2301
        O00O0O0000OOO0O00 .sdfsf24324297_choice .SetSelection (0 )#line:2302
        O00O0O0000OOO0O00 .sdfsf24324297_label =wx .StaticText (OO000OOOOO00OOOOO ,label =u"确认提交方式     ")#line:2303
        O00O0O0O0OO00O00O =wx .BoxSizer (wx .HORIZONTAL )#line:2304
        O00O0O0O0OO00O00O .Add (O00O0O0000OOO0O00 .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2305
        O00O0O0O0OO00O00O .Add (O00O0O0000OOO0O00 .sdfsf24324297_choice )#line:2306
        O000O0000O0O0O00O .Add (O00O0O0O0OO00O00O )#line:2307
        O00O0O0000OOO0O00 .ghjo0o0o0o0_save =wx .Button (OO000OOOOO00OOOOO ,label ="保存策略",size =(60 ,35 ))#line:2310
        O00O0O0000OOO0O00 .ghjo0o0o0o0_load =wx .Button (OO000OOOOO00OOOOO ,label ="载入策略",size =(60 ,35 ))#line:2311
        O00O0O0000OOO0O00 .save_info =wx .Button (OO000OOOOO00OOOOO ,label ="用户信息",size =(60 ,35 ))#line:2312
        OOOO0OOO0OOOOOO00 =wx .BoxSizer (wx .HORIZONTAL )#line:2313
        OOOO0OOO0OOOOOO00 .Add (O00O0O0000OOO0O00 .ghjo0o0o0o0_save )#line:2314
        OOOO0OOO0OOOOOO00 .Add (O00O0O0000OOO0O00 .ghjo0o0o0o0_load )#line:2315
        OOOO0OOO0OOOOOO00 .Add (O00O0O0000OOO0O00 .save_info )#line:2316
        O000O0000O0O0O00O .Add (OOOO0OOO0OOOOOO00 )#line:2317
        OO000000O0OOO000O =wx .StaticBox (OO000OOOOO00OOOOO ,-1 ,u'单枪策略:')#line:2321
        O00O0O0000OOO0O00 .oneshotSizer =wx .StaticBoxSizer (OO000000O0OOO000O ,wx .VERTICAL )#line:2322
        O0O0O00O0OO0OO00O =wx .GridBagSizer (4 ,4 )#line:2323
        O00O0O0000OOO0O00 .jiajia_time =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2324
        O00O0O0000OOO0O00 .jiajia_time .SetRange (40 ,55 )#line:2325
        O00O0O0000OOO0O00 .jiajia_time .SetValue (48 )#line:2326
        O00O0O0000OOO0O00 .jiajia_time .SetIncrement (0.1 )#line:2327
        O0O0O00O0OO0OO00O .Add (O00O0O0000OOO0O00 .jiajia_time ,pos =(0 ,0 ))#line:2329
        OO0OOOOO00000000O =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2330
        O0O0O00O0OO0OO00O .Add (OO0OOOOO00000000O ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2331
        OOOO000O0000O0OO0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2332
        O0O0O00O0OO0OO00O .Add (OOOO000O0000O0OO0 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2333
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2334
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2335
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2336
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2337
        O0O0O00O0OO0OO00O .Add (O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2338
        O0O0000OO0O0OOOO0 =[u"提前100",u"提前200",u"踩点"]#line:2341
        O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O0 =wx .Choice (OO000OOOOO00OOOOO ,-1 ,choices =O0O0000OO0O0OOOO0 ,size =(68 ,25 ))#line:2342
        O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2343
        O0O0O00O0OO0OO00O .Add (O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2344
        OO0OOOO000O0OOOOO =wx .StaticText (OO000OOOOO00OOOOO ,label =u"出价提交延迟")#line:2345
        O0O0O00O0OO0OO00O .Add (OO0OOOO000O0OOOOO ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2346
        O00O0O0000OOO0O00 .yanchi_time =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2347
        O00O0O0000OOO0O00 .yanchi_time .SetRange (0.0 ,1.0 )#line:2348
        O00O0O0000OOO0O00 .yanchi_time .SetValue (0.5 )#line:2349
        O00O0O0000OOO0O00 .yanchi_time .SetIncrement (0.1 )#line:2350
        O0O0O00O0OO0OO00O .Add (O00O0O0000OOO0O00 .yanchi_time ,pos =(1 ,3 ))#line:2351
        O0O000O000O0OOOO0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2352
        O0O0O00O0OO0OO00O .Add (O0O000O000O0OOOO0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2353
        O0O0O0O0OOO00O0O0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"强制提交时间")#line:2356
        O0O0O00O0OO0OO00O .Add (O0O0O0O0OOO00O0O0 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2357
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2358
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2359
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2360
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2361
        O0O0O00O0OO0OO00O .Add (O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2362
        O00OO0O0OOOO00OO0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2363
        O0O0O00O0OO0OO00O .Add (O00OO0O0OOOO00OO0 ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2364
        O00O0O0000OOO0O00 .oneshotSizer .Add (O0O0O00O0OO0OO00O ,0 ,flag =wx .ALL ,border =5 )#line:2366
        O0O000OOO0OOO000O =wx .StaticBox (OO000OOOOO00OOOOO ,-1 ,u'双枪策略:')#line:2370
        O00O0O0000OOO0O00 .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (O0O000OOO0OOO000O ,wx .VERTICAL )#line:2371
        O00OOO0OOO00000O0 =wx .GridBagSizer (4 ,4 )#line:2372
        O00O0O0000OOO0O00 .jiajia_time2 =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2373
        O00O0O0000OOO0O00 .jiajia_time2 .SetRange (40 ,55 )#line:2374
        O00O0O0000OOO0O00 .jiajia_time2 .SetValue (48 )#line:2375
        O00O0O0000OOO0O00 .jiajia_time2 .SetIncrement (0.1 )#line:2376
        O00OOO0OOO00000O0 .Add (O00O0O0000OOO0O00 .jiajia_time2 ,pos =(0 ,0 ))#line:2377
        O00OOOOOOOOOOOOOO =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2378
        O00OOO0OOO00000O0 .Add (O00OOOOOOOOOOOOOO ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2379
        OOOOOO00O0000000O =wx .StaticText (OO000OOOOO00OOOOO ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2380
        O00OOO0OOO00000O0 .Add (OOOOOO00O0000000O ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2381
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2382
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2383
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2384
        O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2385
        O00OOO0OOO00000O0 .Add (O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2386
        O0OOO00O00OO00O0O =[u"提前100",u"提前200",u"踩点"]#line:2388
        O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O02 =wx .Choice (OO000OOOOO00OOOOO ,-1 ,choices =O0OOO00O00OO00O0O ,size =(68 ,25 ))#line:2389
        O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2390
        O00OOO0OOO00000O0 .Add (O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2391
        O00OO00O00OOO00O0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"出价提交延迟")#line:2392
        O00OOO0OOO00000O0 .Add (O00OO00O00OOO00O0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2393
        O00O0O0000OOO0O00 .yanchi_time2 =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2394
        O00O0O0000OOO0O00 .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2395
        O00O0O0000OOO0O00 .yanchi_time2 .SetValue (0.5 )#line:2396
        O00O0O0000OOO0O00 .yanchi_time2 .SetIncrement (0.1 )#line:2397
        O00OOO0OOO00000O0 .Add (O00O0O0000OOO0O00 .yanchi_time2 ,pos =(1 ,3 ))#line:2398
        O00O00OO0O00O0OO0 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2399
        O00OOO0OOO00000O0 .Add (O00O00OO0O00O0OO0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2400
        OO00O0OO0OO0OO000 =wx .StaticText (OO000OOOOO00OOOOO ,label =u"强制提交时间")#line:2403
        O00OOO0OOO00000O0 .Add (OO00O0OO0OO0OO000 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2404
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (OO000OOOOO00OOOOO ,-1 ,"",size =(68 ,25 ))#line:2405
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2406
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2407
        O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2408
        O00OOO0OOO00000O0 .Add (O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2409
        O00O0O000OO00O0OO =wx .StaticText (OO000OOOOO00OOOOO ,label =u"秒")#line:2410
        O00OOO0OOO00000O0 .Add (O00O0O000OO00O0OO ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2411
        O00O0O0000OOO0O00 .ooo0O0o0oO0OshotSizer .Add (O00OOO0OOO00000O0 ,0 ,flag =wx .ALL ,border =5 )#line:2413
        O00O0O0000OOO0O00 .stractagySizer .Add (O000O0000O0O0O00O ,0 ,wx .ALL |wx .CENTER ,5 )#line:2414
        O00O0O0000OOO0O00 .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2415
        O00O000000OOOO00O =wx .StaticText (OO000OOOOO00OOOOO ,-1 ,label =u"拍牌功能设置")#line:2418
        OO000O0000OOOOO0O =wx .StaticText (OO000OOOOO00OOOOO ,-1 ,label =u"10点半需要进行第一次出价")#line:2419
        OO000O0000OOOOO0O .SetForegroundColour ('red')#line:2420
        OOO000OO00O00O000 =wx .StaticLine (OO000OOOOO00OOOOO ,-1 )#line:2421
        O00O0O0000OOO0O00 .vbox1 .Add (O00O000000OOOO00O ,0 ,wx .ALL |wx .LEFT ,10 )#line:2422
        O00O0O0000OOO0O00 .vbox1 .Add (OO000O0000OOOOO0O ,0 ,wx .LEFT ,10 )#line:2423
        O00O0O0000OOO0O00 .vbox1 .Add (OOO000OO00O00O000 ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2424
        O00O0O0000OOO0O00 .vbox1 .Add (O00O0O0000OOO0O00 .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2425
        O00O0O0000OOO0O00 .vbox1 .Add (O00O0O0000OOO0O00 .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2426
        O00O0O0000OOO0O00 .vbox1 .Add (O00O0O0000OOO0O00 .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2427
        OO000OOOOO00OOOOO .SetSizer (O00O0O0000OOO0O00 .vbox1 )#line:2428
        O00O0O0000OOO0O00 .ooo0O0o0oO0Osizer_Shown =False #line:2431
        O00O0O0000OOO0O00 .oneshotsizer_Shown =True #line:2432
        O00O0O0000OOO0O00 .vbox1 .Hide (O00O0O0000OOO0O00 .ooo0O0o0oO0OshotSizer )#line:2433
        O00O0O0000OOO0O00 .Bind (wx .EVT_CHECKBOX ,O00O0O0000OOO0O00 .Timeview ,O00O0O0000OOO0O00 .timeview )#line:2442
        O00O0O0000OOO0O00 .Bind (wx .EVT_CHOICE ,O00O0O0000OOO0O00 .Confirmchoice ,O00O0O0000OOO0O00 .sdfsf24324297_choice )#line:2443
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Strategy_save ,O00O0O0000OOO0O00 .ghjo0o0o0o0_save )#line:2444
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Strategy_load ,O00O0O0000OOO0O00 .ghjo0o0o0o0_load )#line:2445
        O00O0O0000OOO0O00 .Bind (wx .EVT_BUTTON ,O00O0O0000OOO0O00 .Save_info ,O00O0O0000OOO0O00 .save_info )#line:2446
        O00O0O0000OOO0O00 .Bind (wx .EVT_CHOICE ,O00O0O0000OOO0O00 .Refresh_panel ,O00O0O0000OOO0O00 .select_stractagy )#line:2448
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Jiajia_time ,O00O0O0000OOO0O00 .jiajia_time )#line:2450
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Jiajia_zxco0o0o0o0 ,O00O0O0000OOO0O00 .jiajia_zxco0o0o0o0 )#line:2452
        O00O0O0000OOO0O00 .Bind (wx .EVT_CHOICE ,O00O0O0000OOO0O00 .Select_oOO0O0O0O0O0O0 ,O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O0 )#line:2453
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Yanchi_time ,O00O0O0000OOO0O00 .yanchi_time )#line:2455
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Tijiao_time ,O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time )#line:2457
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Jiajia_time2 ,O00O0O0000OOO0O00 .jiajia_time2 )#line:2460
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Jiajia_zxco0o0o0o02 ,O00O0O0000OOO0O00 .jiajia_zxco0o0o0o02 )#line:2462
        O00O0O0000OOO0O00 .Bind (wx .EVT_CHOICE ,O00O0O0000OOO0O00 .Select_oOO0O0O0O0O0O02 ,O00O0O0000OOO0O00 .select_oOO0O0O0O0O0O02 )#line:2463
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Yanchi_time2 ,O00O0O0000OOO0O00 .yanchi_time2 )#line:2465
        O00O0O0000OOO0O00 .Bind (wx .EVT_TEXT ,O00O0O0000OOO0O00 .Tijiao_time2 ,O00O0O0000OOO0O00 .oOO0O0O0O0O0O0_time2 )#line:2467
        O00O0O0000OOO0O00 .timeframe1 =TimeFrame ()#line:2469
        O00O0O0000OOO0O00 .timeframe1 .Show (False )#line:2470
        O00O0O0000OOO0O00 .timeframe2 =MoniTimeFrame ()#line:2472
        O00O0O0000OOO0O00 .timeframe2 .Show (False )#line:2473
        O00O0O0000OOO0O00 .operationtimer =wx .Timer (O00O0O0000OOO0O00 )#line:2476
        O00O0O0000OOO0O00 .Bind (wx .EVT_TIMER ,O00O0O0000OOO0O00 .opt ,O00O0O0000OOO0O00 .operationtimer )#line:2477
        O00O0O0000OOO0O00 .operationtimer .Start (3000 )#line:2478
    def OnClose (OOOO0O00OOOO000OO ,O0O0OOOOOOO00OO00 ):#line:2480
        OOOO0O00OOOO000OO .Show (False )#line:2481
    def Price_view (OO0OOO000O0O0OOO0 ,O0O0O0OOO0O0OO0OO ):#line:2483
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:2484
        if zxco0o0o0o0_view and zxco0o0o0o0_count >=4 :#line:2486
            try :#line:2487
                OO0OOO000O0O0OOO0 .Price_close ()#line:2488
            except :#line:2489
                pass #line:2490
            OO0OOO000O0O0OOO0 .Screen_shot ()#line:2491
            OOO0OOO00OOO0OOO0 ="sc_new.png"#line:2492
            OO0OOO000O0O0OOO0 .zxco0o0o0o0frame =PriceFrame (OOO0OOO00OOO0OOO0 )#line:2493
            OO0OOO000O0O0OOO0 .zxco0o0o0o0frame .Show (True )#line:2494
            zxco0o0o0o0_view =False #line:2495
            zxco0o0o0o0_on =True #line:2496
    def Price_count (OO00000O00OOOOO0O ,O00OOOO0O0O0O0OO0 ):#line:2499
        global zxco0o0o0o0_count #line:2501
        zxco0o0o0o0_count +=1 #line:2502
        OO0OOO000OO0O0OOO ='sc_new.png'#line:2503
        if web_on and ghjo0o0o0o0_on :#line:2504
            OO00000O00OOOOO0O .O0O0O0O0O0O0Oframe .Show (True )#line:2505
        if not os .path .exists (OO0OOO000OO0O0OOO ):#line:2506
            try :#line:2507
                OO00000O00OOOOO0O .Price_close ()#line:2508
            except :#line:2509
                pass #line:2510
        if not ghjo0o0o0o0_on or not web_on :#line:2512
            OO00000O00OOOOO0O .O0O0O0O0O0O0Oframe .Show (False )#line:2513
    def Screen_shot (OOO0OO0O0O0OO00OO ):#line:2518
        global Pricesize #line:2519
        O0OOO0OOO00000OOO =Pos_zxco0o0o0o0 #line:2520
        O0OOOOOO0OOO00OO0 =ImageGrab .grab (O0OOO0OOO00000OOO )#line:2521
        O0OOOOOO0OOO00OO0 .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:2522
    @staticmethod #line:2525
    def Del_shot ():#line:2526
        try :#line:2527
            os .remove ("sc_new.png")#line:2528
        except :#line:2529
            pass #line:2530
    def Price_close (O0000OOO0OOOO0OOO ):#line:2533
        try :#line:2534
            O0000OOO0OOOO0OOO .zxco0o0o0o0frame .Destroy ()#line:2535
        except :#line:2536
            pass #line:2537
    def opt (OO0OOO00O00OO00OO ,O000000OO0O0O0O0O ):#line:2541
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2542
        global ghjo0o0o0o0_on #line:2543
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2544
        if OO0OOO00O00OO00OO .select_stractagy .GetSelection ==0 :#line:2545
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2546
                twice =False #line:2548
                ghjo0o0o0o0_on =True #line:2549
                oo0o0O0O0O0_on =True #line:2550
                oOO0O0O0O0O0O0_on =False #line:2551
                oOO0O0O0O0O0O0_num =1 #line:2552
                oOO0O0O0O0O0O0_OK =False #line:2553
                oOO0O0O0O0O0O0_one =False #line:2554
        elif OO0OOO00O00OO00OO .select_stractagy .GetSelection ==1 :#line:2555
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2556
                ghjo0o0o0o0_on =True #line:2558
                twice =True #line:2559
                oo0o0O0O0O0_on =True #line:2560
                oOO0O0O0O0O0O0_on =False #line:2561
                oOO0O0O0O0O0O0_num =1 #line:2562
                oOO0O0O0O0O0O0_OK =False #line:2563
                oOO0O0O0O0O0O0_one =False #line:2564
    def Add_time (O00O000O0OO000OO0 ,OO0000OO0O00OO00O ):#line:2568
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2569
        if o0sdofsfo0sodf0so0_on :#line:2570
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2571
        else :#line:2572
            a_time +=0.1 #line:2573
    def Minus_time (OOO0OOOOOO00OO0OO ,O0OOO0OO0OOOO0O00 ):#line:2575
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2576
        if o0sdofsfo0sodf0so0_on :#line:2577
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2578
        else :#line:2579
            a_time -=0.1 #line:2580
    def Add_ooo0O0o0oO0O (O0O0OOOOOOOOOOOOO ,OO0OOOOOOOO000O00 ):#line:2582
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2583
        if o0sdofsfo0sodf0so0_on :#line:2584
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2585
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2586
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2587
        else :#line:2588
            a_time +=1 #line:2589
    def Minus_ooo0O0o0oO0O (OOO0O000O0000OO0O ,OO00O00OOOO0OOOOO ):#line:2591
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2592
        if o0sdofsfo0sodf0so0_on :#line:2593
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2594
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2595
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2596
        else :#line:2597
            a_time -=1 #line:2598
    def Timeview (OOO0O00OO00OO0OOO ,O0000O0OOOOOOO00O ):#line:2600
        OOOOO000OOOOO00O0 =O0000O0OOOOOOO00O .GetEventObject ()#line:2601
        global view_time ,time_on #line:2602
        if OOOOO000OOOOO00O0 .IsChecked ():#line:2603
            view_time =True #line:2604
            time_on =True #line:2605
            if ooweo0o0werwr_on :#line:2606
                OOO0O00OO00OO0OOO .timeframe1 .Show (True )#line:2607
            elif o0sdofsfo0sodf0so0_on :#line:2608
                OOO0O00OO00OO0OOO .timeframe2 .Show (True )#line:2609
        else :#line:2610
            view_time =False #line:2611
            time_on =False #line:2612
            if ooweo0o0werwr_on :#line:2613
                OOO0O00OO00OO0OOO .timeframe1 .Show (False )#line:2614
            elif o0sdofsfo0sodf0so0_on :#line:2615
                OOO0O00OO00OO0OOO .timeframe2 .Show (False )#line:2616
    def Opentime (O00O0OO0OO0OOOOOO ):#line:2618
        if o0sdofsfo0sodf0so0_on :#line:2619
            try :#line:2620
                O00O0OO0OO0OOOOOO .timeframe2 .Show (True )#line:2621
            except :#line:2622
                pass #line:2623
        elif ooweo0o0werwr_on :#line:2624
            try :#line:2625
                O00O0OO0OO0OOOOOO .timeframe1 .Show (True )#line:2626
            except :#line:2627
                pass #line:2628
    def Closetime (OO0O00OOO0OO0OOO0 ):#line:2631
        try :#line:2632
            OO0O00OOO0OO0OOO0 .timeframe1 .Show (False )#line:2633
        except :#line:2634
            pass #line:2635
        try :#line:2636
            OO0O00OOO0OO0OOO0 .timeframe2 .Show (False )#line:2637
        except :#line:2638
            pass #line:2639
    def Confirmchoice (OOOOO0OO0O0OO0000 ,OO0O0O0000O00OO00 ):#line:2641
        global e_on ,enter_on #line:2642
        O000O0OOOOO00O00O =OOOOO0OO0O0OO0000 .sdfsf24324297_choice .GetSelection ()#line:2643
        if O000O0OOOOO00O00O ==0 :#line:2644
            e_on =True #line:2645
            enter_on =False #line:2646
        elif O000O0OOOOO00O00O ==1 :#line:2647
            e_on =False #line:2648
            enter_on =True #line:2649
    def Jiajia_time (O0O0000OOO00OO0OO ,OOOO00000O0OO00O0 ):#line:2653
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2654
        O00OOOO0OO00O0OOO =O0O0000OOO00OO0OO .jiajia_time .GetValue ()#line:2655
        OOO0O00OO0OO00OOO =[40 +OOO0OO0O0OOO000O0 *0.1 for OOO0OO0O0OOO000O0 in range (151 )]#line:2656
        if O00OOOO0OO00O0OOO in OOO0O00OO0OO00OOO :#line:2657
            OO00000o01 =O00OOOO0OO00O0OOO #line:2658
            OO00000o01 =float (OO00000o01 )#line:2659
            one_oO0O0O0O0O0O0O0O01 =O0O0000OOO00OO0OO .gettime (OO00000o01 )#line:2660
        else :#line:2661
            O0O0000OOO00OO0OO .jiajia_time .SetValue (OO00000o01 )#line:2662
    def Jiajia_zxco0o0o0o0 (OO00000OOOO0000O0 ,O0O0OOO00000O0000 ):#line:2665
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2666
        OOO0O000000O000OO =[300 +OO0O00OO0O0OO0O0O *100 for OO0O00OO0O0OO0O0O in range (13 )]#line:2667
        O0O0OO00O000OOOOO =OO00000OOOO0000O0 .jiajia_zxco0o0o0o0 .GetValue ()#line:2668
        if O0O0OO00O000OOOOO in OOO0O000000O000OO :#line:2669
            one_diff =int (O0O0OO00O000OOOOO )#line:2670
        else :#line:2671
            OO00000OOOO0000O0 .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2672
    def Select_oOO0O0O0O0O0O0 (O0OOOOO0O00OO000O ,O0O00OO0O00000O00 ):#line:2675
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2676
        O00O000O00OO0000O =O0OOOOO0O00OO000O .select_oOO0O0O0O0O0O0 .GetString (O0OOOOO0O00OO000O .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2677
        if O00O000O00OO0000O ==u"提前100":#line:2678
            one_advance =100 #line:2679
        elif O00O000O00OO0000O ==u"提前200":#line:2680
            one_advance =200 #line:2681
        else :#line:2682
            one_advance =0 #line:2683
    def Yanchi_time (O00OO0O0OOO0OO0OO ,O0000OOOO000OO0OO ):#line:2685
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2686
        O0OO00000O0OOOO0O =['0.%d'%O0O0OO0O0O0OO0O0O for O0O0OO0O0O0OO0O0O in range (11 )]#line:2687
        O0OO00000O0OOOO0O .append ('1.0')#line:2688
        OO0O0OO0OOOO000OO =str (O00OO0O0OOO0OO0OO .yanchi_time .GetValue ())#line:2689
        if OO0O0OO0OOOO000OO in O0OO00000O0OOOO0O :#line:2690
            one_delay =float (OO0O0OO0OOOO000OO )#line:2691
        else :#line:2692
            O00OO0O0OOO0OO0OO .yanchi_time .SetValue (one_delay )#line:2693
    def Tijiao_time (O0O0OOO000OO00O0O ,OOOOOOOO0O0OOO00O ):#line:2695
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2696
        O000O000000OO0O00 =O0O0OOO000OO00O0O .oOO0O0O0O0O0O0_time .GetValue ()#line:2697
        O00OO000OOOOO0O00 =[40 +O0OO0OO0O0OO0OO00 *0.1 for O0OO0OO0O0OO0OO00 in range (171 )]#line:2698
        if O000O000000OO0O00 in O00OO000OOOOO0O00 :#line:2699
            OO00000o02 =float (O000O000000OO0O00 )#line:2700
            one_oO0O0O0O0O0O0O0O02 =O0O0OOO000OO00O0O .gettime (OO00000o02 )#line:2701
        else :#line:2702
            O0O0OOO000OO00O0O .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2703
    def Jiajia_time2 (O00OO00OO0O0OOOO0 ,O0OO0O0OO0O000O0O ):#line:2705
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2706
        O0OO0OO00OO0OO0OO =O00OO00OO0O0OOOO0 .jiajia_time2 .GetValue ()#line:2707
        OOO00OOO0O000OO00 =[40 +O000OO0000O00OOOO *0.1 for O000OO0000O00OOOO in range (151 )]#line:2708
        if O0OO0OO00OO0OO0OO in OOO00OOO0O000OO00 :#line:2709
            ooo0O0o0oO0O_time1 =float (O0OO0OO00OO0OO0OO )#line:2710
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00OO00OO0O0OOOO0 .gettime (ooo0O0o0oO0O_time1 )#line:2711
        else :#line:2712
            O00OO00OO0O0OOOO0 .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2713
    def Jiajia_zxco0o0o0o02 (OO0O00O0O00O0O000 ,OO000OOOO0OOOOOO0 ):#line:2715
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2716
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2717
        O00O0OOOOO0000O0O =[300 +O0O000OOO00O0O0OO *100 for O0O000OOO00O0O0OO in range (13 )]#line:2718
        O000OO00O0OO0OOOO =OO0O00O0O00O0O000 .jiajia_zxco0o0o0o02 .GetValue ()#line:2719
        if O000OO00O0OO0OOOO in O00O0OOOOO0000O0O :#line:2720
            ooo0O0o0oO0O_diff =int (O000OO00O0OO0OOOO )#line:2721
        else :#line:2722
            OO0O00O0O00O0O000 .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2723
    def Select_oOO0O0O0O0O0O02 (O00000OOO00OO000O ,OO00O0OO000OO00OO ):#line:2725
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2726
        O000OOOOO0O0O000O =O00000OOO00OO000O .select_oOO0O0O0O0O0O02 .GetString (O00000OOO00OO000O .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2727
        if O000OOOOO0O0O000O ==u"提前100":#line:2728
            ooo0O0o0oO0O_advance =100 #line:2729
        elif O000OOOOO0O0O000O ==u"提前200":#line:2730
            ooo0O0o0oO0O_advance =200 #line:2731
        else :#line:2732
            ooo0O0o0oO0O_advance =0 #line:2733
    def Yanchi_time2 (OO00000000OOOOO00 ,O0O0O00O00OO000OO ):#line:2736
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2737
        O0OOO00OO00O00000 =['0.%d'%O0O0O0000OOOOO0OO for O0O0O0000OOOOO0OO in range (11 )]#line:2738
        O0OOO00OO00O00000 .append ('1.0')#line:2739
        O0O00O000O0OOOOOO =str (OO00000000OOOOO00 .yanchi_time2 .GetValue ())#line:2740
        if O0O00O000O0OOOOOO in O0OOO00OO00O00000 :#line:2741
            ooo0O0o0oO0O_delay =float (O0O00O000O0OOOOOO )#line:2742
        else :#line:2743
            OO00000000OOOOO00 .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2744
    def Tijiao_time2 (OO0OOOO0000O000O0 ,O0OOOOOOO00000O00 ):#line:2747
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2748
        OOO00O0000O00OO00 =OO0OOOO0000O000O0 .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2749
        O0000O00000OOOOO0 =[53 +OOO0O0OO0OOO000OO *0.1 for OOO0O0OO0OOO000OO in range (41 )]#line:2750
        if OOO00O0000O00OO00 in O0000O00000OOOOO0 :#line:2751
            ooo0O0o0oO0O_time2 =float (OOO00O0000O00OO00 )#line:2752
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0OOOO0000O000O0 .gettime (ooo0O0o0oO0O_time2 )#line:2753
        else :#line:2754
            OO0OOOO0000O000O0 .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2755
    def Refresh_panel (O00OOO0OO0OOOOOOO ,O0O0OOO0OOO00OOO0 ):#line:2759
        global ghjo0o0o0o0_on #line:2761
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2762
        OOO00000OO0OOO0OO =O00OOO0OO0OOOOOOO .select_stractagy .GetString (O00OOO0OO0OOOOOOO .select_stractagy .GetSelection ())#line:2763
        if OOO00000OO0OOO0OO ==u"单枪策略":#line:2764
            O00OOO0OO0OOOOOOO .ss_Hide ()#line:2765
            twice =False #line:2766
            ghjo0o0o0o0_on =True #line:2767
            oo0o0O0O0O0_on =True #line:2768
            oOO0O0O0O0O0O0_on =False #line:2769
            oOO0O0O0O0O0O0_num =1 #line:2770
            oOO0O0O0O0O0O0_OK =False #line:2771
            oOO0O0O0O0O0O0_one =False #line:2772
        elif OOO00000OO0OOO0OO ==u"双枪策略":#line:2774
            O00OOO0OO0OOOOOOO .ss_Shown ()#line:2775
            ghjo0o0o0o0_on =True #line:2776
            twice =True #line:2777
            oo0o0O0O0O0_on =True #line:2778
            oOO0O0O0O0O0O0_on =False #line:2779
            oOO0O0O0O0O0O0_num =1 #line:2780
            oOO0O0O0O0O0O0_OK =False #line:2781
            oOO0O0O0O0O0O0_one =False #line:2782
        else :#line:2783
            O00OOO0OO0OOOOOOO .none_show ()#line:2784
            ghjo0o0o0o0_on =False #line:2785
            twice =False #line:2786
    def ss_Shown (O0O00000OOOOO0O00 ):#line:2789
        if not O0O00000OOOOO0O00 .ooo0O0o0oO0Osizer_Shown :#line:2790
            O0O00000OOOOO0O00 .vbox1 .Show (O0O00000OOOOO0O00 .ooo0O0o0oO0OshotSizer )#line:2791
            O0O00000OOOOO0O00 .ooo0O0o0oO0Osizer_Shown =True #line:2792
        if not O0O00000OOOOO0O00 .oneshotsizer_Shown :#line:2793
            O0O00000OOOOO0O00 .vbox1 .Show (O0O00000OOOOO0O00 .oneshotSizer )#line:2794
            O0O00000OOOOO0O00 .oneshotsizer_Shown =True #line:2795
        O0O00000OOOOO0O00 .ooo0O0o0oO0Osizer_Shown =True #line:2796
        O0O00000OOOOO0O00 .oneshotSizer_Shown =True #line:2797
        O0O00000OOOOO0O00 .SetClientSize ((280 ,575 ))#line:2798
        O0O00000OOOOO0O00 .Secondshot_reset ()#line:2799
        O0O00000OOOOO0O00 .Layout ()#line:2800
    def ss_Hide (OOO00000O0O0000O0 ):#line:2802
        if OOO00000O0O0000O0 .ooo0O0o0oO0Osizer_Shown :#line:2803
            OOO00000O0O0000O0 .vbox1 .Hide (OOO00000O0O0000O0 .ooo0O0o0oO0OshotSizer )#line:2804
        if not OOO00000O0O0000O0 .oneshotsizer_Shown :#line:2807
            OOO00000O0O0000O0 .vbox1 .Show (OOO00000O0O0000O0 .oneshotSizer )#line:2808
        OOO00000O0O0000O0 .ooo0O0o0oO0Osizer_Shown =False #line:2809
        OOO00000O0O0000O0 .oneshotSizer_Shown =True #line:2810
        OOO00000O0O0000O0 .SetClientSize ((280 ,375 ))#line:2811
        OOO00000O0O0000O0 .Oneshot_reset ()#line:2812
        OOO00000O0O0000O0 .Layout ()#line:2813
    def none_show (OOO000O0OOO00O0O0 ):#line:2815
        if OOO000O0OOO00O0O0 .oneshotsizer_Shown :#line:2816
            OOO000O0OOO00O0O0 .vbox1 .Hide (OOO000O0OOO00O0O0 .ooo0O0o0oO0OshotSizer )#line:2817
        if OOO000O0OOO00O0O0 .ooo0O0o0oO0Osizer_Shown :#line:2818
            OOO000O0OOO00O0O0 .vbox1 .Hide (OOO000O0OOO00O0O0 .oneshotSizer )#line:2819
        OOO000O0OOO00O0O0 .oneshotsizer_Shown =False #line:2821
        OOO000O0OOO00O0O0 .ooo0O0o0oO0Osizer_Shown =False #line:2822
        OOO000O0OOO00O0O0 .SetClientSize ((280 ,255 ))#line:2823
        OOO000O0OOO00O0O0 .Layout ()#line:2824
    def Oneshot_reset (OO00OOO0OO00OO000 ):#line:2826
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2827
        OO00OOO0OO00OO000 .jiajia_time .SetValue (48.0 )#line:2828
        OO00OOO0OO00OO000 .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2829
        OO00OOO0OO00OO000 .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2830
        OO00OOO0OO00OO000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2831
        OO00OOO0OO00OO000 .yanchi_time .SetValue (0.5 )#line:2832
        OO00000o01 =48 #line:2834
        OO00000o02 =55 #line:2835
        one_diff =700 #line:2836
        one_delay =0.5 #line:2837
        one_advance =100 #line:2838
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2840
        one_oO0O0O0O0O0O0O0O01 =OO00OOO0OO00OO000 .gettime (OO00000o01 )#line:2841
        one_oO0O0O0O0O0O0O0O02 =OO00OOO0OO00OO000 .gettime (OO00000o02 )#line:2842
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO00OOO0OO00OO000 .gettime (ooo0O0o0oO0O_time1 )#line:2843
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO00OOO0OO00OO000 .gettime (ooo0O0o0oO0O_time2 )#line:2844
    def Secondshot_reset (OO0000000OO0OOOO0 ):#line:2847
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2848
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2849
        OO0000000OO0OOOO0 .jiajia_time .SetValue (40.0 )#line:2850
        OO0000000OO0OOOO0 .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:2851
        OO0000000OO0OOOO0 .jiajia_zxco0o0o0o0 .SetValue (500 )#line:2852
        OO0000000OO0OOOO0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2853
        OO0000000OO0OOOO0 .yanchi_time .SetValue (0.0 )#line:2854
        OO0000000OO0OOOO0 .jiajia_time2 .SetValue (50.0 )#line:2856
        OO0000000OO0OOOO0 .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:2857
        OO0000000OO0OOOO0 .jiajia_zxco0o0o0o02 .SetValue (700 )#line:2858
        OO0000000OO0OOOO0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2859
        OO0000000OO0OOOO0 .yanchi_time2 .SetValue (0.5 )#line:2860
        OO00000o01 =40 #line:2862
        OO00000o02 =48 #line:2863
        one_diff =500 #line:2864
        one_delay =0.5 #line:2865
        one_advance =100 #line:2866
        ooo0O0o0oO0O_time1 =50 #line:2868
        ooo0O0o0oO0O_time2 =55.5 #line:2869
        ooo0O0o0oO0O_diff =700 #line:2870
        ooo0O0o0oO0O_delay =0.5 #line:2871
        ooo0O0o0oO0O_advance =100 #line:2872
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2874
        one_oO0O0O0O0O0O0O0O01 =OO0000000OO0OOOO0 .gettime (OO00000o01 )#line:2875
        one_oO0O0O0O0O0O0O0O02 =OO0000000OO0OOOO0 .gettime (OO00000o02 )#line:2876
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0000000OO0OOOO0 .gettime (ooo0O0o0oO0O_time1 )#line:2877
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0000000OO0OOOO0 .gettime (ooo0O0o0oO0O_time2 )#line:2878
    def Strategy_save (O0O000000O00O0OO0 ,O00O00OO00000O0O0 ):#line:2881
        O000OO0O00O0O0O00 =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:2883
        if O000OO0O00O0O0O00 .ShowModal ()==wx .ID_OK :#line:2884
            O00OO0O0O00O000O0 =O000OO0O00O0O0O00 .GetValue ()#line:2885
            if O00OO0O0O00O000O0 :#line:2886
                OOOO00O0O0000000O =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:2887
                if OOOO00O0O0000000O ==wx .ID_OK :#line:2888
                    OOOO00O0O0000000O .Destroy ()#line:2889
                    O000OO0O00O0O0O00 .Destroy ()#line:2890
                O0O000000O00O0OO0 .save (O00OO0O0O00O000O0 )#line:2891
            else :#line:2892
                OOOO00O0O0000000O =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:2893
                if OOOO00O0O0000000O ==wx .ID_OK :#line:2894
                    OOOO00O0O0000000O .Destroy ()#line:2895
                    O000OO0O00O0O0O00 .Destroy ()#line:2896
    def save (O000OO0O00000OO00 ,OOO00OOOOOOOOOOOO ):#line:2898
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2899
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2900
        global osl ,e_on ,enter_on #line:2901
        if O000OO0O00000OO00 .select_stractagy .GetSelection ()==2 :#line:2903
            O0000OO0OO0O00OO0 =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:2904
            if O0000OO0OO0O00OO0 ==wx .ID_OK :#line:2905
                O0000OO0OO0O00OO0 .Destroy ()#line:2906
        elif O000OO0O00000OO00 .select_stractagy .GetSelection ()==0 :#line:2907
            osl [0 ]=0 #line:2908
            osl [1 ]=OO00000o01 #line:2909
            osl [2 ]=OO00000o02 #line:2910
            osl [3 ]=one_diff #line:2911
            osl [4 ]=one_delay #line:2912
            osl [5 ]=one_advance #line:2913
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2914
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2915
            osl [8 ]=ooo0O0o0oO0O_diff #line:2916
            osl [9 ]=ooo0O0o0oO0O_delay #line:2917
            osl [10 ]=ooo0O0o0oO0O_advance #line:2918
            osl [11 ]=e_on #line:2919
            osl [12 ]=enter_on #line:2920
        elif O000OO0O00000OO00 .select_stractagy .GetSelection ()==1 :#line:2921
            osl [0 ]=1 #line:2922
            osl [0 ]=1 #line:2923
            osl [1 ]=OO00000o01 #line:2924
            osl [2 ]=OO00000o02 #line:2925
            osl [3 ]=one_diff #line:2926
            osl [4 ]=one_delay #line:2927
            osl [5 ]=one_advance #line:2928
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2929
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2930
            osl [8 ]=ooo0O0o0oO0O_diff #line:2931
            osl [9 ]=ooo0O0o0oO0O_delay #line:2932
            osl [10 ]=ooo0O0o0oO0O_advance #line:2933
            osl [11 ]=e_on #line:2934
            osl [12 ]=enter_on #line:2935
        with open ('%s.ghjo0o0o0o0'%OOO00OOOOOOOOOOOO ,'wb')as OO00OO0O0OO00O0OO :#line:2936
            pickle .dump (osl ,OO00OO0O0OO00O0OO )#line:2937
    def Strategy_load (OOOOOO000000OO00O ,O00OOO00000O0O00O ):#line:2952
        import os as OOOO000O00000O00O #line:2953
        OO0O00OO00OOOO0OO =OOOO000O00000O00O .getcwd ()#line:2954
        OO0OOOOO00OOOO0OO =OOOOOO000000OO00O .findfiles (OO0O00OO00OOOO0OO )#line:2955
        if OO0OOOOO00OOOO0OO :#line:2956
            OO0OOOO0OOOO0OOO0 =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =OO0OOOOO00OOOO0OO )#line:2958
            if OO0OOOO0OOOO0OOO0 .ShowModal ()==wx .ID_OK :#line:2959
                OO0O00OO00OOOO0OO =OO0OOOO0OOOO0OOO0 .GetStringSelection ()#line:2960
                O0OO0O00000000OO0 =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:2961
                if O0OO0O00000000OO0 .ShowModal ()==wx .ID_OK :#line:2962
                    O0OO0O00000000OO0 .Destroy ()#line:2963
                OOOOOO000000OO00O .load (OO0O00OO00OOOO0OO )#line:2964
            OO0OOOO0OOOO0OOO0 .Destroy ()#line:2966
        else :#line:2967
            O0OO0O00000000OO0 =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:2968
            if O0OO0O00000000OO0 ==wx .ID_OK :#line:2969
                O0OO0O00000000OO0 .Destroy ()#line:2970
                OO0OOOO0OOOO0OOO0 .Destroy ()#line:2971
    def load (OOO00O0OO000O00O0 ,OO000O00OOO000O00 ):#line:2973
        global osl ,e_on ,enter_on #line:2974
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2975
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2976
        global ghjo0o0o0o0_on #line:2978
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2979
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2980
        try :#line:2981
            with open (OO000O00OOO000O00 ,'rb')as OO0OO0OOOOO0O0O0O :#line:2982
                osl =pickle .load (OO0OO0OOOOO0O0O0O )#line:2983
        except :#line:2984
            pass #line:2985
        if osl [0 ]==0 :#line:2986
            OOO00O0OO000O00O0 .ss_Hide ()#line:2987
            twice =False #line:2990
            ghjo0o0o0o0_on =True #line:2991
            oo0o0O0O0O0_on =True #line:2992
            oOO0O0O0O0O0O0_on =False #line:2993
            oOO0O0O0O0O0O0_num =1 #line:2994
            oOO0O0O0O0O0O0_OK =False #line:2995
            oOO0O0O0O0O0O0_one =False #line:2996
            OOO00O0OO000O00O0 .select_stractagy .SetSelection (0 )#line:2998
            OOO00O0OO000O00O0 .jiajia_time .SetValue (osl [1 ])#line:2999
            OOO00O0OO000O00O0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3000
            OOO00O0OO000O00O0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3001
            OOO00O0OO000O00O0 .yanchi_time .SetValue (osl [4 ])#line:3002
            if osl [5 ]==100 :#line:3003
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3004
            elif osl [5 ]==200 :#line:3005
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3006
            else :#line:3007
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3008
            OO00000o01 =osl [1 ]#line:3010
            OO00000o02 =osl [2 ]#line:3011
            one_diff =osl [3 ]#line:3012
            one_delay =osl [4 ]#line:3013
            one_advance =osl [5 ]#line:3014
            e_on =osl [11 ]#line:3016
            enter_on =osl [12 ]#line:3017
            if e_on :#line:3018
                OOO00O0OO000O00O0 .sdfsf24324297_choice .SetSelection (0 )#line:3019
            elif enter_on :#line:3020
                OOO00O0OO000O00O0 .sdfsf24324297_choice .SetSelection (1 )#line:3021
            one_oO0O0O0O0O0O0O0O01 =OOO00O0OO000O00O0 .gettime (OO00000o01 )#line:3023
            one_oO0O0O0O0O0O0O0O02 =OOO00O0OO000O00O0 .gettime (OO00000o02 )#line:3024
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOO00O0OO000O00O0 .gettime (ooo0O0o0oO0O_time1 )#line:3025
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOO00O0OO000O00O0 .gettime (ooo0O0o0oO0O_time2 )#line:3026
        elif osl [0 ]==1 :#line:3028
            ghjo0o0o0o0_on =True #line:3029
            twice =True #line:3030
            oo0o0O0O0O0_on =True #line:3031
            oOO0O0O0O0O0O0_on =False #line:3032
            oOO0O0O0O0O0O0_num =1 #line:3033
            oOO0O0O0O0O0O0_OK =False #line:3034
            oOO0O0O0O0O0O0_one =False #line:3035
            OOO00O0OO000O00O0 .ss_Shown ()#line:3036
            OOO00O0OO000O00O0 .select_stractagy .SetSelection (1 )#line:3037
            OOO00O0OO000O00O0 .jiajia_time .SetValue (osl [1 ])#line:3038
            OOO00O0OO000O00O0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3039
            OOO00O0OO000O00O0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3040
            OOO00O0OO000O00O0 .yanchi_time .SetValue (osl [4 ])#line:3041
            if osl [5 ]==100 :#line:3042
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3043
            elif osl [5 ]==200 :#line:3044
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3045
            else :#line:3046
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3047
            OOO00O0OO000O00O0 .jiajia_time2 .SetValue (osl [6 ])#line:3048
            OOO00O0OO000O00O0 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:3049
            OOO00O0OO000O00O0 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:3050
            OOO00O0OO000O00O0 .yanchi_time2 .SetValue (osl [9 ])#line:3051
            if osl [10 ]==100 :#line:3052
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:3053
            elif osl [10 ]==200 :#line:3054
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:3055
            else :#line:3056
                OOO00O0OO000O00O0 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:3057
            OO00000o01 =osl [1 ]#line:3060
            OO00000o02 =osl [2 ]#line:3061
            one_diff =osl [3 ]#line:3062
            one_delay =osl [4 ]#line:3063
            one_advance =osl [5 ]#line:3064
            ooo0O0o0oO0O_time1 =osl [6 ]#line:3066
            ooo0O0o0oO0O_time2 =osl [7 ]#line:3067
            ooo0O0o0oO0O_diff =osl [8 ]#line:3068
            ooo0O0o0oO0O_delay =osl [9 ]#line:3069
            ooo0O0o0oO0O_advance =osl [10 ]#line:3070
            e_on =osl [11 ]#line:3072
            enter_on =osl [12 ]#line:3073
            if e_on :#line:3074
                OOO00O0OO000O00O0 .sdfsf24324297_choice .SetSelection (0 )#line:3075
            elif enter_on :#line:3076
                OOO00O0OO000O00O0 .sdfsf24324297_choice .SetSelection (1 )#line:3077
            one_oO0O0O0O0O0O0O0O01 =OOO00O0OO000O00O0 .gettime (OO00000o01 )#line:3079
            one_oO0O0O0O0O0O0O0O02 =OOO00O0OO000O00O0 .gettime (OO00000o02 )#line:3080
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOO00O0OO000O00O0 .gettime (ooo0O0o0oO0O_time1 )#line:3081
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOO00O0OO000O00O0 .gettime (ooo0O0o0oO0O_time2 )#line:3082
    def findfiles (O0OO00O000O0OOO0O ,OO0O0O000OO0000OO ):#line:3084
        OOOOOO000OOO0O00O =[]#line:3085
        for OO0OO0OO00OO00OO0 ,OO000OOO000OOOOOO ,OOO00OOO00OOOO0O0 in os .walk (OO0O0O000OO0000OO ):#line:3086
            for OO00000O0OOOO0000 in OOO00OOO00OOOO0O0 :#line:3087
                if os .path .splitext (OO00000O0OOOO0000 )[1 ]=='.ghjo0o0o0o0':#line:3088
                    OOOOOO000OOO0O00O .append (os .path .join (OO0OO0OO00OO00OO0 ,OO00000O0OOOO0000 ))#line:3089
        return OOOOOO000OOO0O00O #line:3090
    def Save_info (O000OO000O0O0O0O0 ,O0O0O00000000OOO0 ):#line:3092
        pass #line:3093
    def changetime (O000OO0OO00O0OOOO ,OO0OOO0OOO000OOOO ):#line:3098
        O00O00O0OOO00O000 =time .mktime (time .strptime (OO0OOO0OOO000OOOO ,'%Y-%m-%d %H:%M:%S'))#line:3099
        return O00O00O0OOO00O000 #line:3100
    def get_nowtime (OO0OOOOO00O00O000 ):#line:3103
        O0O0OOOO0O0O00OO0 =time .time ()#line:3104
        OOO000O0O00OO0O0O =time .strftime ('%Y-%m-%d',time .localtime (O0O0OOOO0O0O00OO0 ))#line:3105
        return OOO000O0O00OO0O0O #line:3106
    def gettime (OO0OO000OO0O0O0OO ,O0OO0O00000O0OOO0 ):#line:3109
        OOO0000OO0000O000 =OO0OO000OO0O0O0OO .get_nowtime ()#line:3110
        O000O00OO0O0000OO =OOO0000OO0000O000 +' 11:29:'+str (int (O0OO0O00000O0OOO0 ))#line:3111
        OOOOOO00OOO0O0OOO =OO0OO000OO0O0O0OO .changetime (O000O00OO0O0000OO )+float (O0OO0O00000O0OOO0 )-int (O0OO0O00000O0OOO0 )#line:3112
        return OOOOOO00OOO0O0OOO #line:3113
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:3116
    def __init__ (OOO00O0OO0OO0O0OO ,OO00000000OOOOO0O ):#line:3117
        wx .Window .__init__ (OOO00O0OO0OO0O0OO ,OO00000000OOOOO0O ,size =Timesize )#line:3118
        OOO00O0OO0OO0O0OO .Bind (wx .EVT_PAINT ,OOO00O0OO0OO0O0OO .OnPaint )#line:3119
        OOO00O0OO0OO0O0OO .timer =wx .Timer (OOO00O0OO0OO0O0OO )#line:3120
        OOO00O0OO0OO0O0OO .Bind (wx .EVT_TIMER ,OOO00O0OO0OO0O0OO .OnTimer ,OOO00O0OO0OO0O0OO .timer )#line:3121
        OOO00O0OO0OO0O0OO .timer .Start (100 )#line:3122
    def Draw (O0O00OOOOOOO0O0O0 ,O0OOOOOOO000OOOOO ):#line:3124
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3125
        OOO00OOOOO0O00000 =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3126
        O000OOO0OO00OO00O ,O00O0OO0000O00000 =O0O00OOOOOOO0O0O0 .GetClientSize ()#line:3127
        O0OOOOOOO000OOOOO .SetBackground (wx .Brush (O0O00OOOOOOO0O0O0 .GetBackgroundColour ()))#line:3128
        O0OOOOOOO000OOOOO .Clear ()#line:3129
        O0OOOOOOO000OOOOO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3130
        OOO00OOO00O000O00 ,OOOOOO00OO0O0O0OO =O0OOOOOOO000OOOOO .GetTextExtent (OOO00OOOOO0O00000 )#line:3131
        O0OOOOOOO000OOOOO .DrawText (OOO00OOOOO0O00000 ,(O000OOO0OO00OO00O -OOO00OOO00O000O00 )/2 ,(O00O0OO0000O00000 )/2 -OOOOOO00OO0O0O0OO /2 )#line:3132
    def Modify (OOOO0OO0O00OO0OO0 ,O000000OO0O00O0OO ):#line:3134
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3135
        O0O00OOOOOO00O000 =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3136
        OO0O0OOO00OO0000O ,O0OO000O0OO0O0OOO =OOOO0OO0O00OO0OO0 .GetClientSize ()#line:3137
        O000000OO0O00O0OO .SetBackground (wx .Brush (OOOO0OO0O00OO0OO0 .GetBackgroundColour ()))#line:3138
        O000000OO0O00O0OO .Clear ()#line:3139
        O000000OO0O00O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3140
        O0O00000OOO0O0OO0 ,OO00OO00OOO00OO00 =O000000OO0O00O0OO .GetTextExtent (O0O00OOOOOO00O000 )#line:3141
        O000000OO0O00O0OO .DrawText (O0O00OOOOOO00O000 ,(OO0O0OOO00OO0000O -O0O00000OOO0O0OO0 )/2 ,(O0OO000O0OO0O0OOO )/2 -OO00OO00OOO00OO00 /2 )#line:3142
    def OnTimer (O00OOOO0OOO00OO00 ,OOO00OO0OOOOOOOOO ):#line:3144
        OOOOO000OO0O000O0 =wx .BufferedDC (wx .ClientDC (O00OOOO0OOO00OO00 ))#line:3145
        O00OOOO0OOO00OO00 .Modify (OOOOO000OO0O000O0 )#line:3146
    def OnPaint (OOO0OOOO000O0OOO0 ,O00OOOO00O00000O0 ):#line:3148
        O0OO00OO000OO00OO =wx .BufferedPaintDC (OOO0OOOO000O0OOO0 )#line:3149
        OOO0OOOO000O0OOO0 .Draw (O0OO00OO000OO00OO )#line:3150
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:3152
    def __init__ (OOO00O00OOO0OO000 ):#line:3153
         wx .Frame .__init__ (OOO00O00OOO0OO000 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =O0O0O0O0O0O0Ozxco0o0o0o0frame_pos ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:3155
         Lowestzxco0o0o0o0Window (OOO00O00OOO0OO000 )#line:3158
import string #line:3176
import wx .lib .agw .hyperlink as hyperlink #line:3177
class LoginFrame (wx .Frame ):#line:3178
    def __init__ (O0O000O0O000OO0O0 ,O0O00OO0OOO0000O0 ,OOOOOOO00OOOOOOO0 ,O0OOO00O0O0O00OO0 ):#line:3179
        wx .Frame .__init__ (O0O000O0O000OO0O0 ,None ,-1 ,O0O00OO0OOO0000O0 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3180
        O0O000O0O000OO0O0 .Bind (wx .EVT_CLOSE ,O0O000O0O000OO0O0 .OnClose )#line:3181
        O0O000O0O000OO0O0 .panel =wx .Panel (O0O000O0O000OO0O0 ,size =(300 ,220 ))#line:3182
        O0O000O0O000OO0O0 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3183
        O0O000O0O000OO0O0 .SetIcon (O0O000O0O000OO0O0 .icon )#line:3184
        O0O000O0O000OO0O0 .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3197
        O0O000O0O000OO0O0 .welcomelabel =wx .StaticText (O0O000O0O000OO0O0 .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3198
        O0O000O0O000OO0O0 .sizer_v1 .Add (O0O000O0O000OO0O0 .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3199
        O0O000O0O000OO0O0 .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3202
        O0O000O0O000OO0O0 .userlabel =wx .StaticText (O0O000O0O000OO0O0 .panel ,-1 ,label ="账号")#line:3203
        O0O000O0O000OO0O0 .userText =wx .TextCtrl (O0O000O0O000OO0O0 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3205
        O0O000O0O000OO0O0 .userbox .Add (O0O000O0O000OO0O0 .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3206
        O0O000O0O000OO0O0 .userbox .Add (O0O000O0O000OO0O0 .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3207
        O0O000O0O000OO0O0 .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3209
        O0O000O0O000OO0O0 .passlabel =wx .StaticText (O0O000O0O000OO0O0 .panel ,-1 ,label ="密码")#line:3210
        O0O000O0O000OO0O0 .passText =wx .TextCtrl (O0O000O0O000OO0O0 .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3212
        O0O000O0O000OO0O0 .passbox .Add (O0O000O0O000OO0O0 .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3213
        O0O000O0O000OO0O0 .passbox .Add (O0O000O0O000OO0O0 .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3214
        if OOOOOOO00OOOOOOO0 :#line:3215
            O0O000O0O000OO0O0 .userText .SetValue (OOOOOOO00OOOOOOO0 )#line:3216
        if O0OOO00O0O0O00OO0 :#line:3217
            O0O000O0O000OO0O0 .passText .SetValue (O0OOO00O0O0O00OO0 )#line:3218
        O0O000O0O000OO0O0 .sizer_v1 .Add (O0O000O0O000OO0O0 .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3219
        O0O000O0O000OO0O0 .sizer_v1 .Add (O0O000O0O000OO0O0 .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3220
        O0O000O0O000OO0O0 .Bind (wx .EVT_TEXT_ENTER ,O0O000O0O000OO0O0 .OnLogin ,O0O000O0O000OO0O0 .userText )#line:3222
        O0O000O0O000OO0O0 .Bind (wx .EVT_TEXT_ENTER ,O0O000O0O000OO0O0 .OnLogin ,O0O000O0O000OO0O0 .passText )#line:3223
        O0O000O0O000OO0O0 .o0sdofsfo0sodf0so0btn =wx .Button (O0O000O0O000OO0O0 .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3225
        O0O000O0O000OO0O0 .loginbtn =wx .Button (O0O000O0O000OO0O0 .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3226
        O0O000O0O000OO0O0 .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3227
        O0O000O0O000OO0O0 .btnSizer .Add (O0O000O0O000OO0O0 .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3228
        O0O000O0O000OO0O0 .btnSizer .Add (O0O000O0O000OO0O0 .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3229
        O0O000O0O000OO0O0 .sizer_v1 .Add (O0O000O0O000OO0O0 .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3230
        O0O000O0O000OO0O0 .loginbtn .Bind (wx .EVT_BUTTON ,O0O000O0O000OO0O0 .OnLogin ,O0O000O0O000OO0O0 .loginbtn )#line:3231
        O0O000O0O000OO0O0 .purchaselink =hyperlink .HyperLinkCtrl (O0O000O0O000OO0O0 .panel ,-1 ,u"购买账号")#line:3233
        O0O000O0O000OO0O0 .purchaselink .UnsetToolTip ()#line:3234
        O0O000O0O000OO0O0 .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O0O000O0O000OO0O0 .Purchase )#line:3235
        O0O000O0O000OO0O0 .purchaselink .AutoBrowse (False )#line:3236
        O0O000O0O000OO0O0 .purchaselink .EnableRollover (True )#line:3237
        O0O000O0O000OO0O0 .purchaselink .SetUnderlines (False ,False ,True )#line:3238
        O0O000O0O000OO0O0 .purchaselink .OpenInSameWindow (True )#line:3239
        O0O000O0O000OO0O0 .purchaselink .UpdateLink ()#line:3240
        O0O000O0O000OO0O0 .helplink =hyperlink .HyperLinkCtrl (O0O000O0O000OO0O0 .panel ,-1 ,u"查看帮助")#line:3242
        O0O000O0O000OO0O0 .helplink .UnsetToolTip ()#line:3243
        O0O000O0O000OO0O0 .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,O0O000O0O000OO0O0 .Purchase )#line:3244
        O0O000O0O000OO0O0 .helplink .AutoBrowse (False )#line:3245
        O0O000O0O000OO0O0 .helplink .EnableRollover (True )#line:3246
        O0O000O0O000OO0O0 .helplink .SetUnderlines (False ,False ,True )#line:3247
        O0O000O0O000OO0O0 .helplink .OpenInSameWindow (True )#line:3248
        O0O000O0O000OO0O0 .helplink .UpdateLink ()#line:3249
        O0O000O0O000OO0O0 .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3251
        O0O000O0O000OO0O0 .linkbox .Add (O0O000O0O000OO0O0 .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3252
        O0O000O0O000OO0O0 .linkbox .Add (O0O000O0O000OO0O0 .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3253
        O0O000O0O000OO0O0 .sizer_v1 .Add (O0O000O0O000OO0O0 .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3254
        O0O000O0O000OO0O0 .SetSizer (O0O000O0O000OO0O0 .sizer_v1 )#line:3256
        O0O000O0O000OO0O0 .Center ()#line:3257
        pub .subscribe (O0O000O0O000OO0O0 .connect_success ,"connect")#line:3259
        O0O000O0O000OO0O0 .hashthread =HashThread ()#line:3262
    def connect_success (O000OOOOOOOO000O0 ):#line:3264
        O000OOOOOOOO000O0 .loginbtn .Enable ()#line:3265
        global login_result #line:3266
        if login_result =='login success':#line:3267
            O000OOOOOOOO000O0 .Destroy ()#line:3268
            O000OOOOOOOO000O0 .topframe =TopFrame ('小鲜肉拍牌',version )#line:3269
            O000OOOOOOOO000O0 .topframe .Show (True )#line:3270
        elif login_result =='net error':#line:3272
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3273
        elif login_result =='repeat':#line:3274
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3275
        elif login_result =='wrong account':#line:3276
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3277
        elif login_result =='wrong password':#line:3278
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3279
        else :#line:3280
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3281
    def OnEraseBack (OO0OO0O0OO0O0OOOO ,O0O0OO00OO00OOO0O ):#line:3284
        O00OO000O00OOOOOO =O0O0OO00OO00OOO0O .GetDC ()#line:3285
        if not O00OO000O00OOOOOO :#line:3286
            O00OO000O00OOOOOO =wx .ClientDC (OO0OO0O0OO0O0OOOO )#line:3287
            O00OOO00O000OOOOO =OO0OO0O0OO0O0OOOO .GetUpdateRegion ().GetBox ()#line:3288
            O00OO000O00OOOOOO .SetClippingRect (O00OOO00O000OOOOO )#line:3289
        O00OO000O00OOOOOO .Clear ()#line:3290
        OOOO0OOO0OOO0O000 =wx .Bitmap ("blue.jpg")#line:3291
        O00OO000O00OOOOOO .DrawBitmap (OOOO0OOO0OOO0O000 ,0 ,0 )#line:3292
    def OnClose (O00O000OO00OO000O ,O0OOO000OO0OOOO00 ):#line:3294
        O0OOO000OO0OOOO00 .Skip ()#line:3295
        sys .exit (None )#line:3296
    def OnLogin (OOO00O0OOOO0OO000 ,O00O0OOO00O0O0O0O ):#line:3304
        global Username ,Password #line:3305
        O00OO0000O00O00OO =OOO00O0OOOO0OO000 .userText .GetValue ()#line:3306
        OOO000000OO000OO0 =OOO00O0OOOO0OO000 .passText .GetValue ()#line:3307
        if O00OO0000O00O00OO =="":#line:3308
            wx .MessageBox ('请输入用户名！')#line:3309
            OOO00O0OOOO0OO000 .userText .SetFocus ()#line:3310
        elif OOO000000OO000OO0 =="":#line:3311
            wx .MessageBox ('请输入密码！')#line:3312
            OOO00O0OOOO0OO000 .passText .SetFocus ()#line:3313
        else :#line:3315
            Username =O00OO0000O00O00OO #line:3316
            Password =OOO000000OO000OO0 #line:3317
            OOO00O0OOOO0OO000 .loginthread =LoginThread ()#line:3318
            O0OOO00O0OO0O0000 =[O00OO0000O00O00OO ,OOO000000OO000OO0 ]#line:3319
            with open ('your.name','wb')as OO0OO0O0000O000O0 :#line:3320
                pickle .dump (O0OOO00O0OO0O0000 ,OO0OO0O0000O000O0 )#line:3321
            O00O0OOO00O0O0O0O .GetEventObject ().Disable ()#line:3323
    def Purchase (O0OO0OO0OOOOOO0O0 ,OOOO00O000O0O000O ):#line:3325
        print ("购买")#line:3326
class UserValidator (wx .Validator ):#line:3330
    ""#line:3331
    def __init__ (O00OO0OOO000OO0OO ,O0OOOO00OO0O000O0 ):#line:3333
        wx .Validator .__init__ (O00OO0OOO000OO0OO )#line:3334
        O00OO0OOO000OO0OO .flag =O0OOOO00OO0O000O0 #line:3335
        O00OO0OOO000OO0OO .Bind (wx .EVT_CHAR ,O00OO0OOO000OO0OO .OnChar )#line:3336
    def Clone (OO0O0O000O00O0O00 ):#line:3339
        ""#line:3340
        return UserValidator (OO0O0O000O00O0O00 .flag )#line:3341
    def Validate (OO00O00O0OOOO0O0O ,O0O0O00O0O0000O0O ):#line:3344
        return True #line:3345
    def TransferToWindow (O0OO0O0O0O00O000O ):#line:3348
        return True #line:3349
    def TransferFromWindow (O00000O0OOO00OO00 ):#line:3352
        return True #line:3353
    def OnChar (OO000O0OOOOOO000O ,O00O0000000000OO0 ):#line:3356
        pass #line:3357
class PassValidator (wx .Validator ):#line:3371
    ""#line:3372
    def __init__ (O000O0OO0OO00OO0O ):#line:3375
        wx .Validator .__init__ (O000O0OO0OO00OO0O )#line:3376
        O000O0OO0OO00OO0O .Bind (wx .EVT_CHAR ,O000O0OO0OO00OO0O .OnChar )#line:3377
    def Clone (OOO0OOO0OO0OO0O00 ):#line:3380
        ""#line:3381
        return PassValidator ()#line:3382
    def Validate (OOOOOOOOOOO00000O ,O0O00O00O0OOO00O0 ):#line:3385
        return True #line:3386
    def TransferToWindow (O0O0OO00O000000OO ):#line:3389
        return True #line:3390
    def TransferFromWindow (OO000O0OO00OO0O0O ):#line:3393
        return True #line:3394
    def OnChar (OO0O0O0OO0000O0OO ,OO0O0OOOO0O0OOOOO ):#line:3397
        pass #line:3398
class ConfirmLogin (wx .Frame ):#line:3412
    pass #line:3413
class TimeThread (Thread ):#line:3416
    def __init__ (OOOO0000000OOOO0O ):#line:3417
        ""#line:3418
        Thread .__init__ (OOOO0000000OOOO0O )#line:3419
        OOOO0000000OOOO0O .setDaemon (True )#line:3420
        OOOO0000000OOOO0O .start ()#line:3421
    def run (O00OO0OO00OOOO00O ):#line:3423
        ""#line:3424
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:3426
        for O0O00O000O0OOOOO0 in range (1000000 ):#line:3427
            O00OO00O0O000000O =time .clock ()#line:3428
            time .sleep (0.1 )#line:3429
            OO0O00OO0OO00OO00 =time .clock ()#line:3430
            a_time +=OO0O00OO0OO00OO00 -O00OO00O0O000000O #line:3431
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=OO0O00OO0OO00OO00 -O00OO00O0O000000O #line:3432
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:3433
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:3434
class OpenwebThread (Thread ):#line:3465
    def __init__ (O00OOOO0OO000OOOO ,OOO0O0OOO0OOO000O ):#line:3466
        ""#line:3467
        Thread .__init__ (O00OOOO0OO000OOOO )#line:3468
        O00OOOO0OO000OOOO .url =OOO0O0OOO0OOO000O #line:3469
        O00OOOO0OO000OOOO .setDaemon (True )#line:3470
        O00OOOO0OO000OOOO .start ()#line:3471
    def run (OO0000O0O0OOOOOOO ):#line:3473
        ""#line:3474
        openweb (OO0000O0O0OOOOOOO .url )#line:3476
class HashThread (Thread ):#line:3478
    def __init__ (O0O0O000O00O00O0O ):#line:3479
        ""#line:3480
        Thread .__init__ (O0O0O000O00O00O0O )#line:3481
        O0O0O000O00O00O0O .setDaemon (True )#line:3482
        O0O0O000O00O00O0O .start ()#line:3483
    def run (OOO0000O0O00OOOO0 ):#line:3485
        ""#line:3486
        Create_hash ()#line:3488
        getwebpath ()#line:3489
class findposThread (Thread ):#line:3495
    def __init__ (OO00000O0OO00O0OO ):#line:3496
        Thread .__init__ (OO00000O0OO00O0OO )#line:3497
        OO00000O0OO00O0OO .setDaemon (True )#line:3498
        OO00000O0OO00O0OO .start ()#line:3499
    def run (OOOOO0000OO0O00O0 ):#line:3501
        findpos ()#line:3502
class sdfsf24324297Thread (Thread ):#line:3505
    def __init__ (O0OOO000000O0O000 ):#line:3506
        Thread .__init__ (O0OOO000000O0O000 )#line:3507
        O0OOO000000O0O000 .setDaemon (True )#line:3508
        O0OOO000000O0O000 .start ()#line:3509
    def run (OOO00OO00O0O00OO0 ):#line:3511
        global sdfsf24324297_need ,sdfsf24324297_on #line:3512
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3513
        for O00OO000OO0000OO0 in range (100 ):#line:3514
            wx .Sleep (0.1 )#line:3515
            if sdfsf24324297_need :#line:3517
                findsdfsf24324297 ()#line:3519
                if sdfsf24324297_on :#line:3520
                    TopFrame .OnClick_sdfsf24324297 ()#line:3521
                    sdfsf24324297_need =False #line:3522
                    sdfsf24324297_on =False #line:3523
                    sdfsf24324297_one =False #line:3524
                    oo0o0O0O0O0_on =True #line:3525
        sdfsf24324297_one =False #line:3526
class uioo0o000ooThread (Thread ):#line:3528
    def __init__ (O000OO0OO0000OO00 ):#line:3529
        Thread .__init__ (O000OO0OO0000OO00 )#line:3530
        O000OO0OO0000OO00 .setDaemon (True )#line:3531
        O000OO0OO0000OO00 .start ()#line:3532
    def run (O0O0OO0OO0000O00O ):#line:3534
        global sdfsf24324297_need ,sdfsf24324297_on #line:3535
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3536
        for OOO000OO0000OO0OO in range (60 ):#line:3537
            if uioo0o000oo_need :#line:3538
                finduioo0o000oo ()#line:3539
                if uioo0o000oo_on :#line:3540
                    TopFrame .OnClick_Shuaxin ()#line:3541
                    uioo0o000oo_on =False #line:3542
                    uioo0o000oo_need =False #line:3543
                    uioo0o000oo_one =False #line:3544
        uioo0o000oo_one =False #line:3545
class LoginThread (Thread ):#line:3550
    def __init__ (O000OO00O0OOOOOO0 ):#line:3551
        ""#line:3552
        Thread .__init__ (O000OO00O0OOOOOO0 )#line:3553
        O000OO00O0OOOOOO0 .setDaemon (True )#line:3554
        O000OO00O0OOOOOO0 .start ()#line:3555
    def run (O0OO0OO0O00OOOOO0 ):#line:3557
        global Username ,login_result #line:3559
        login_result =ConfirmUser ()#line:3560
        print (login_result )#line:3561
        logging .info ("%s"%login_result )#line:3562
        wx .CallAfter (pub .sendMessage ,"connect")#line:3563
class controlThread (Thread ):#line:3566
    def __init__ (O00O0O000O0000O00 ):#line:3567
        ""#line:3568
        Thread .__init__ (O00O0O000O0000O00 )#line:3569
        O00O0O000O0000O00 .setDaemon (True )#line:3570
        O00O0O000O0000O00 .start ()#line:3571
    def run (O0O00O00O00000OO0 ):#line:3574
        wx .Sleep (10 )#line:3575
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3576
class KeepThread (Thread ):#line:3581
    def __init__ (OOOOO00O0OO0OOOOO ):#line:3582
        ""#line:3583
        Thread .__init__ (OOOOO00O0OO0OOOOO )#line:3584
        OOOOO00O0OO0OOOOO .setDaemon (True )#line:3585
        OOOOO00O0OO0OOOOO .start ()#line:3586
    def run (O0O000000OOO00000 ):#line:3589
        for OO0O0OOOOOOOO0OO0 in range (1000000 ):#line:3590
            time .sleep (90 )#line:3591
            Keeplogin ()#line:3592
class TijiaoThread (Thread ):#line:3598
    def __init__ (OO0O000O00OO0O0OO ):#line:3599
        ""#line:3600
        Thread .__init__ (OO0O000O00OO0O0OO )#line:3601
        OO0O000O00OO0O0OO .setDaemon (True )#line:3602
        OO0O000O00OO0O0OO .start ()#line:3603
    def run (O000OO00OOOO00O00 ):#line:3606
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3607
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3608
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3609
        for O0O0O0OOO0O0000O0 in range (10000000 ):#line:3610
            time .sleep (0.1 )#line:3611
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3615
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3617
                    oOO0O0O0O0O0O0_on =False #line:3618
                    TopFrame .OnClick_Tijiao ()#line:3619
                    oOO0O0O0O0O0O0_on =False #line:3620
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3621
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3622
                    oOO0O0O0O0O0O0_one =True #line:3623
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3624
                    oOO0O0O0O0O0O0_on =False #line:3625
                    TopFrame .OnClick_Tijiao ()#line:3626
                    oOO0O0O0O0O0O0_on =False #line:3627
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3628
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3629
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3630
                    oOO0O0O0O0O0O0_on =False #line:3631
                    oOO0O0O0O0O0O0_on =False #line:3632
                    TopFrame .OnClick_Tijiao ()#line:3633
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3634
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3635
                    oOO0O0O0O0O0O0_one =True #line:3636
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance :#line:3637
                    oOO0O0O0O0O0O0_on =False #line:3638
                    oOO0O0O0O0O0O0_on =False #line:3639
                    TopFrame .OnClick_Tijiao ()#line:3640
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3641
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3642
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3644
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time <=one_oO0O0O0O0O0O0O0O01 +0.2 :#line:3646
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3647
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3648
                    oOO0O0O0O0O0O0_on =True #line:3649
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3650
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3651
                if oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3652
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3653
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3654
                    oOO0O0O0O0O0O0_on =True #line:3655
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3656
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3657
class MoniTijiaoThread (Thread ):#line:3661
    def __init__ (OOO0OOOO0O0OOO0O0 ):#line:3662
        ""#line:3663
        Thread .__init__ (OOO0OOOO0O0OOO0O0 )#line:3664
        OOO0OOOO0O0OOO0O0 .setDaemon (True )#line:3665
        OOO0OOOO0O0OOO0O0 .start ()#line:3666
    def run (O0O0OO0OOOO00000O ):#line:3669
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3670
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3671
        for OOO00000O0OO0O00O in range (10000000 ):#line:3672
            time .sleep (0.1 )#line:3673
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3675
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3679
                    TopFrame .OnClick_Tijiao ()#line:3680
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3681
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3682
                    oOO0O0O0O0O0O0_on =False #line:3683
                    oOO0O0O0O0O0O0_one =True #line:3684
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3685
                    TopFrame .OnClick_Tijiao ()#line:3686
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3687
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3688
                    oOO0O0O0O0O0O0_on =False #line:3689
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3690
                    oOO0O0O0O0O0O0_on =False #line:3691
                    TopFrame .OnClick_Tijiao ()#line:3692
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3693
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3694
                    oOO0O0O0O0O0O0_one =True #line:3695
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3696
                    oOO0O0O0O0O0O0_on =False #line:3697
                    TopFrame .OnClick_Tijiao ()#line:3698
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3699
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3700
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3705
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=OO00000o01 +0.2 :#line:3706
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3707
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3709
                    oOO0O0O0O0O0O0_on =True #line:3710
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3711
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3712
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3713
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3714
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3716
                    oOO0O0O0O0O0O0_on =True #line:3717
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3718
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3719
class Infoframe (wx .Frame ):#line:3722
    def __init__ (OOOO00OO0O0000OOO ,O00OOO00O0OOO0O00 ,OO0O00O0000OOOO00 ,O000O0000OOOO00OO ):#line:3723
        wx .Frame .__init__ (OOOO00OO0O0000OOO ,None ,-1 ,O00OOO00O0OOO0O00 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3724
        OOOO00OO0O0000OOO .Bind (wx .EVT_CLOSE ,OOOO00OO0O0000OOO .OnClose )#line:3725
        OOOO00OO0O0000OOO .panel =wx .Panel (OOOO00OO0O0000OOO ,size =(300 ,220 ))#line:3726
        OOOO00OO0O0000OOO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3727
        OOOO00OO0O0000OOO .SetIcon (OOOO00OO0O0000OOO .icon )#line:3728
class SketchApp (wx .App ):#line:3731
    def OnInit (OOOO00OO000O00OOO ):#line:3732
        try :#line:3743
            with open ("your.name",'rb')as OOOOOOOO0000O0OOO :#line:3744
                O00O0O0O00O0O000O =pickle .load (OOOOOOOO0000O0OOO )#line:3745
                O00O0OO000O00OOOO =O00O0O0O00O0O000O [0 ]#line:3746
                O0O0000O00000OOO0 =O00O0O0O00O0O000O [1 ]#line:3747
        except :#line:3748
            O00O0OO000O00OOOO ='123456'#line:3749
            O0O0000O00000OOO0 =0 #line:3750
        OO0O000OOO00000O0 =LoginFrame ('小鲜肉拍牌',O00O0OO000O00OOOO ,O0O0000O00000OOO0 )#line:3751
        OO0O000OOO00000O0 .Show (True )#line:3752
        return True #line:3753
if __name__ =='__main__':#line:3756
    app =SketchApp ()#line:3757
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
