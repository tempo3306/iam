""#line:5
version ='1.9'#line:10
num =0 #line:11
avt =0 #line:12
test =True #line:15
host_ali ="121.196.220.94"#line:18
url1 ="http://moni.51hupai.org/"#line:21
url2 ="www.baidu.com"#line:24
url3 ="www.baidu.com"#line:25
url4 ="http://127.0.0.1:5000/Moni"#line:26
mainicon ='ico.ico'#line:30
view =False #line:33
do =False #line:34
ad_view =False #line:35
zxco0o0o0o0_view =False #line:37
zxco0o0o0o0_on =False #line:38
zxco0o0o0o0_count =0 #line:39
web_on =False #line:40
view_time =False #line:42
operation_show =False #line:43
time_on =False #line:44
import time #line:45
a_time =time .time ()#line:46
b_time =0 #line:47
o0sdofsfo0sodf0so0_minute =29 #line:49
o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:50
oo0o0O0O0O0_time =0 #line:52
Username =0 #line:54
Password =0 #line:55
o0sdofsfo0sodf0so0_on =False #line:58
ooweo0o0werwr_on =False #line:59
ghjo0o0o0o01 =53 #line:62
ghjo0o0o0o02 =0.0 #line:63
ghjo0o0o0o0_on =True #line:69
ghjo0o0o0o0_repeat =False #line:70
delay =False #line:73
delay_time =0.5 #line:74
login_result =False #line:76
findpos_on =True #line:79
zxco0o0o0o0list =[80000 +OO0OOO0O000OO0O00 *100 for OO0OOO0O000OO0O00 in range (200 )]#line:81
IDnumber =0 #line:82
account =0 #line:83
passwd =0 #line:84
changetime =0 #line:87
import pyautogui as pg #line:92
def Create_hash ():#line:94
    with open ('dick.dl','rb')as OOO0OOO0OO00OO00O :#line:95
        global dick_hash #line:96
        dick_hash =pickle .load (OOO0OOO0OO00OO00O )#line:97
    with open ('cf.btn','rb')as OOOOOOOOOO0O0000O :#line:98
        global cf_hash #line:99
        cf_hash =pickle .load (OOOOOOOOOO0O0000O )#line:100
    with open ("target.tkl",'rb')as O0OO0OOOOO00OOOOO :#line:102
        global dick_target #line:103
        dick_target =pickle .load (O0OO0OOOOO00OOOOO )#line:104
OO00000o01 =48 #line:109
OO00000o02 =55 #line:110
one_oO0O0O0O0O0O0O0O01 =1000000000000 #line:111
one_oO0O0O0O0O0O0O0O02 =1000000000000 #line:112
one_diff =700 #line:113
one_delay =0.5 #line:114
one_advance =100 #line:115
ooo0O0o0oO0O_time1 =48 #line:118
ooo0O0o0oO0O_time2 =55 #line:119
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =1000000000000 #line:120
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =1000000000000 #line:121
ooo0O0o0oO0O_diff =600 #line:122
ooo0O0o0oO0O_delay =0.5 #line:123
ooo0O0o0oO0O_advance =100 #line:124
osl =[0 ]*15 #line:126
oo0o0O0O0O0_on =True #line:128
oOO0O0O0O0O0O0_on =False #line:129
O0O0O0O0O0O0O_zxco0o0o0o0 =86000 #line:132
own_zxco0o0o0o01 =0 #line:133
own_zxco0o0o0o02 =0 #line:134
own_zxco0o0o0o0 =0 #line:135
oOO0O0O0O0O0O0_OK =False #line:137
e_on =True #line:138
enter_on =False #line:139
twice =False #line:141
oOO0O0O0O0O0O0_num =1 #line:142
oOO0O0O0O0O0O0_one =False #line:143
websize =[902 ,700 ]#line:146
Pxy =pg .size ()#line:147
Px1 =Pxy [0 ]/2 #line:148
Py2 =Pxy [1 ]/2 #line:149
Px =(Pxy [0 ]-websize [0 ])/2 -80 #line:150
Py =(Pxy [1 ]-websize [1 ])/2 #line:151
P_relative =[[343 ,-66 ],[346 ,40 ],[96 ,121 ],[92 ,43 ],[201 ,100 ],[281 ,40 ],[261 ,37 ],[282 ,118 ]]#line:154
P_relative2 =[[647 ,-98 ],[650 ,8 ],[400 ,89 ],[396 ,11 ],[505 ,68 ],[585 ,8 ],[565 ,5 ],[586 ,86 ]]#line:155
Oo0o0Oo0o0o0 =[[0 ,0 ]for O0OO000OOOO0OO00O in range (len (P_relative ))]#line:156
for i in range (len (Oo0o0Oo0o0o0 )):#line:157
    Oo0o0Oo0o0o0 [i ][0 ]=Px1 +P_relative [i ][0 ]#line:158
    Oo0o0Oo0o0o0 [i ][1 ]=Py2 +P_relative [i ][1 ]#line:159
px_ajust ,py_ajust =0 ,0 #line:162
for i in range (len (P_relative )):#line:163
    P_relative [i ][0 ]+=websize [0 ]/2 +px_ajust #line:164
    P_relative [i ][1 ]+=websize [1 ]/2 +py_ajust #line:165
px_zxco0o0o0o0 =770 -171 #line:167
py_zxco0o0o0o0 =260 #line:168
px_zxco0o0o0o0frame =220 -191 #line:170
py_zxco0o0o0o0frame =480 #line:171
px_timeframe =22 #line:173
py_timeframe =350 #line:174
px_O0O0O0O0O0O0Ozxco0o0o0o0frame =245 #line:176
py_O0O0O0O0O0O0Ozxco0o0o0o0frame =290 #line:177
O0O0O0O0O0O0Ozxco0o0o0o0frame_pos =[px_O0O0O0O0O0O0Ozxco0o0o0o0frame ,py_O0O0O0O0O0O0Ozxco0o0o0o0frame ]#line:178
px_sdfsnisdfafzxcvframe =400 -215 #line:181
py_sdfsnisdfafzxcvframe =460 #line:182
px_mini =200 #line:186
py_mini =40 #line:187
Pricesize =[400 ,80 ]#line:189
Timesize =[200 ,50 ]#line:191
O0O0O0O0O0O0Ozxco0o0o0o0_area =[179 -80 +Px ,424 -50 +Py ,179 +80 +Px ,424 +50 +Py ]#line:194
uioo0o000oo_area =[396 -150 ,11 -100 ,396 +150 ,11 +100 ]#line:195
sdfsf24324297_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:196
Px_zxco0o0o0o0 =Px +px_zxco0o0o0o0 #line:215
Py_zxco0o0o0o0 =Py +py_zxco0o0o0o0 #line:216
Pos_zxco0o0o0o0 =[Px_zxco0o0o0o0 ,Py_zxco0o0o0o0 ,Px_zxco0o0o0o0 +px_mini ,Py_zxco0o0o0o0 +py_mini ]#line:217
Px_zxco0o0o0o0frame =Px +px_zxco0o0o0o0frame #line:220
Py_zxco0o0o0o0frame =Py +py_zxco0o0o0o0frame #line:221
Pos_zxco0o0o0o0frame =[Px_zxco0o0o0o0frame ,Py_zxco0o0o0o0frame ]#line:222
Px_timeframe =px_timeframe +Px #line:225
Py_timeframe =py_timeframe +Py #line:226
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:227
print (Pos_timeframe )#line:228
Pos_controlframe =[Px +40 ,Py +480 ]#line:230
Px_sdfsnisdfafzxcvframe =Px +px_sdfsnisdfafzxcvframe #line:233
Py_sdfsnisdfafzxcvframe =Py +py_sdfsnisdfafzxcvframe #line:234
Pos_sdfsnisdfafzxcvframe =[Px_sdfsnisdfafzxcvframe ,Py_sdfsnisdfafzxcvframe ]#line:235
px_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:243
py_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:244
Px_O0O0O0O0O0O0Ozxco0o0o0o0 =Px +px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:247
Py_O0O0O0O0O0O0Ozxco0o0o0o0 =Py +py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:248
O0O0O0O0O0O0Ozxco0o0o0o0_sizex =82 #line:249
O0O0O0O0O0O0Ozxco0o0o0o0_sizey =16 #line:251
px_relative =49 #line:253
py_relative =0 #line:254
px_sdfsf24324297 =656 #line:256
py_sdfsf24324297 =475 #line:257
Px_sdfsf24324297 =Px +px_sdfsf24324297 #line:258
Py_sdfsf24324297 =Py +py_sdfsf24324297 #line:259
sdfsf24324297_sizex =113 #line:260
sdfsf24324297_sizey =28 #line:261
sdfsf24324297_on =False #line:262
sdfsf24324297_need =False #line:263
sdfsf24324297_one =False #line:264
px_uioo0o000oo =550 #line:266
py_uioo0o000oo =413 #line:267
Px_uioo0o000oo =Px +px_uioo0o000oo #line:268
Py_uioo0o000oo =Py +py_uioo0o000oo #line:269
uioo0o000oo_sizex =108 #line:270
uioo0o000oo_sizey =21 #line:271
uioo0o000oo_on =False #line:272
uioo0o000oo_need =False #line:273
uioo0o000oo_one =False #line:274
oo0o0O0O0O0_interval =False #line:276
oOO0O0O0O0O0O0_interval =False #line:277
query_interval =False #line:278
query_on =False #line:279
import sys #line:282
if sys .platform !='win32':#line:283
    exit ()#line:284
import pyautogui as pg #line:285
import ctypes #line:286
from ctypes import wintypes #line:287
import win32con #line:288
import wx .html2 #line:289
import wx #line:290
import pickle #line:291
import wx .adv #line:292
from PIL import Image #line:293
import imagehash #line:294
import logging #line:372
timenow =time .time ()#line:373
time_local =time .localtime (timenow )#line:375
myapplog =time .strftime ("%Y%m%d%H%M%S",time_local )#line:377
print (myapplog )#line:378
logging .basicConfig (level =logging .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:383
logging .debug ('This is debug message')#line:385
logging .info ('This is info message')#line:386
logging .warning ('This is warning message')#line:387
logging .error ('This is error message')#line:388
import win32gui ,win32api #line:391
import cv2 #line:392
from PIL import ImageGrab #line:393
def Click (OO0OOO000O0O000O0 ,OOOOO000OO0OO0000 ):#line:395
    OOOO0O0OOO0O0O000 =win32gui .GetCursorPos ()#line:396
    OO0OOO000O0O000O0 =int (OO0OOO000O0O000O0 )#line:397
    OOOOO000OO0OO0000 =int (OOOOO000OO0OO0000 )#line:398
    win32api .SetCursorPos ((OO0OOO000O0O000O0 ,OOOOO000OO0OO0000 ))#line:399
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OO0OOO000O0O000O0 ,OOOOO000OO0OO0000 ,0 ,0 )#line:400
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OO0OOO000O0O000O0 ,OOOOO000OO0OO0000 ,0 ,0 )#line:401
def Click2 (OOOO00O00OOO00OOO ,OOOO00O0O00O00O00 ):#line:403
    OOO0OOO000O000O00 =win32gui .GetCursorPos ()#line:404
    OOOO00O00OOO00OOO =int (OOOO00O00OOO00OOO )#line:405
    OOOO00O0O00O00O00 =int (OOOO00O0O00O00O00 )#line:406
    win32api .SetCursorPos ((OOOO00O00OOO00OOO ,OOOO00O0O00O00O00 ))#line:407
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OOOO00O00OOO00OOO ,OOOO00O0O00O00O00 ,0 ,0 )#line:408
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OOOO00O00OOO00OOO ,OOOO00O0O00O00O00 ,0 ,0 )#line:409
    win32api .SetCursorPos (OOO0OOO000O000O00 )#line:410
import win32clipboard #line:414
def Paste ():#line:415
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:416
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:417
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:418
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:419
def Paste_o0sdofsfo0sodf0so0 (OOOOOO0OO0000OOO0 ,O0OO0OO0OOO00O0O0 ):#line:421
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:422
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:423
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:424
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:425
def setText (O0O0O0000000OOOOO ):#line:435
    O0O0O0000000OOOOO =O0O0O0000000OOOOO .encode ('utf-8')#line:436
    win32clipboard .OpenClipboard ()#line:437
    win32clipboard .EmptyClipboard ()#line:438
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,O0O0O0000000OOOOO )#line:439
    win32clipboard .CloseClipboard ()#line:440
def Delete ():#line:442
    win32api .keybd_event (0x08 ,0 ,0 ,0 )#line:443
    win32api .keybd_event (0x08 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:444
def findpos ():#line:448
    OO00O000OOOOO000O =ImageGrab .grab ().convert ('L')#line:450
    OOOO000O0O000O0O0 =np .asarray (OO00O000OOOOO000O )#line:451
    global dick_target #line:452
    O000OO0000OO00OO0 =dick_target [2 ]#line:453
    O00O0OOO000OO0OOO ,O0OOOOOO0OOOOOO0O =O000OO0000OO00OO0 .shape [::-1 ]#line:454
    OO00O0OOOOOO0000O =cv2 .matchTemplate (OOOO000O0O000O0O0 ,O000OO0000OO00OO0 ,cv2 .TM_CCOEFF_NORMED )#line:456
    OOO0O00OO0000OOO0 ,OOOOOO000O000O000 ,O0000OOO0O000OO00 ,O0O000O00OO00OOO0 =cv2 .minMaxLoc (OO00O0OOOOOO0000O )#line:457
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:462
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O000O00OO00OOO0 [0 ]+px_relative #line:463
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O000O00OO00OOO0 [1 ]+py_relative #line:464
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:465
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:466
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area ,Pos_timeframe ,Pos_controlframe #line:469
    for O0000000O00O00O0O in range (len (Oo0o0Oo0o0o0 )):#line:470
        Oo0o0Oo0o0o0 [O0000000O00O00O0O ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0000000O00O00O0O ][0 ]#line:471
        Oo0o0Oo0o0o0 [O0000000O00O00O0O ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O0000000O00O00O0O ][1 ]#line:472
    uioo0o000oo_area =[396 -150 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -100 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +150 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +100 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:473
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:474
    Pos_controlframe =[192 -344 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,514 -183 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:475
    global findpos_on #line:478
    findpos_on =False #line:479
def finduioo0o000oo ():#line:481
    global dick_target ,uioo0o000oo_on ,uioo0o000oo_need ,uioo0o000oo_one ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:482
    O0000O00OOO00O0O0 =dick_target [0 ]#line:483
    OOOO000OOO00OO000 =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:484
    OOO0O0OO000OOOO00 =np .asarray (OOOO000OOO00OO000 )#line:486
    OO00OOOO0O000O0OO ,O0O0O0OOO000O0OOO =O0000O00OOO00O0O0 .shape [::-1 ]#line:487
    O0OO0OO0O0000OO0O =cv2 .matchTemplate (OOO0O0OO000OOOO00 ,O0000O00OOO00O0O0 ,cv2 .TM_CCOEFF_NORMED )#line:488
    OO0O000O0000O00OO ,OO00OO0O00OO00OOO ,OO0O000000O00O0O0 ,O0OO0OOOOO0O00OOO =cv2 .minMaxLoc (O0OO0OO0O0000OO0O )#line:489
    print (OO00OO0O00OO00OOO )#line:490
    if OO00OO0O00OO00OOO >=0.7 :#line:491
        uioo0o000oo_on =True #line:492
    else :#line:493
        uioo0o000oo_on =False #line:494
        uioo0o000oo_need =False #line:495
        uioo0o000oo_one =False #line:496
def findsdfsf24324297 ():#line:499
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:500
    OOO00OOOOOOO0O00O =dick_target [1 ]#line:501
    OO000O000OO000O0O =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:502
    OOOOOOOOOO00OO0O0 =np .asarray (OO000O000OO000O0O )#line:503
    OOO000OO0O00O0OO0 ,OO000O0O0OOO00000 =OOO00OOOOOOO0O00O .shape [::-1 ]#line:504
    OO00O000O0OO0000O =cv2 .matchTemplate (OOOOOOOOOO00OO0O0 ,OOO00OOOOOOO0O00O ,cv2 .TM_CCOEFF_NORMED )#line:505
    O0OOO00000O000O00 ,OOOO0O0OOO0OOO0O0 ,OOO0O0O0OOOO0000O ,O0OOO000O0OO0O00O =cv2 .minMaxLoc (OO00O000O0OO0000O )#line:506
    print (OOOO0O0OOO0OOO0O0 )#line:507
    if OOOO0O0OOO0OOO0O0 >=0.9 :#line:508
        sdfsf24324297_on =True #line:509
SZ =20 #line:513
bin_n =16 #line:514
import numpy as np #line:515
def hog (OOO00OOO00O0OOO00 ):#line:518
    O00OOOO0OO0OO00O0 =cv2 .Sobel (OOO00OOO00O0OOO00 ,cv2 .CV_32F ,1 ,0 )#line:519
    OO000OO0000O00O0O =cv2 .Sobel (OOO00OOO00O0OOO00 ,cv2 .CV_32F ,0 ,1 )#line:520
    O0O000O000OOOO0O0 ,O0O0O0O000OOOOOO0 =cv2 .cartToPolar (O00OOOO0OO0OO00O0 ,OO000OO0000O00O0O )#line:521
    O0OOO000O00O0OOO0 =np .int32 (bin_n *O0O0O0O000OOOOOO0 /(2 *np .pi ))#line:522
    O0O0O00O000O00O00 =O0OOO000O00O0OOO0 [:10 ,:10 ],O0OOO000O00O0OOO0 [10 :,:10 ],O0OOO000O00O0OOO0 [:10 ,10 :],O0OOO000O00O0OOO0 [10 :,10 :]#line:523
    O00O000OO0OO0O0O0 =O0O000O000OOOO0O0 [:10 ,:10 ],O0O000O000OOOO0O0 [10 :,:10 ],O0O000O000OOOO0O0 [:10 ,10 :],O0O000O000OOOO0O0 [10 :,10 :]#line:524
    O0OOOO000OOO0OOOO =[np .bincount (O00OO000O0O0O0O0O .ravel (),O000OOOO00O0OO00O .ravel (),bin_n )for O00OO000O0O0O0O0O ,O000OOOO00O0OO00O in zip (O0O0O00O000O00O00 ,O00O000OO0OO0O0O0 )]#line:525
    OO00OOO00O0OO00O0 =np .hstack (O0OOOO000OOO0OOOO )#line:526
    return OO00OOO00O0OO00O0 #line:527
def cut (OO00O00O000OO0O00 ):#line:531
    O0O000OOO0O0OO000 ,OOO00O00OO00OOO0O =cv2 .threshold (OO00O00O000OO0O00 ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:532
    O0OOOOOO0OO0O0O00 ,OO0OOO0OOOOO0O00O ,O0O0O000O00O00O0O =cv2 .findContours (OOO00O00OO00OOO0O ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:534
    OO0OOOO0O0OOO00OO =[]#line:535
    O00OO00O0OO0O0OOO =[]#line:536
    for O0OO0OOOOOOO0OOOO in range (len (OO0OOO0OOOOO0O00O )):#line:537
        OO00OOO0O0O00000O =OO0OOO0OOOOO0O00O [O0OO0OOOOOOO0OOOO ]#line:538
        OOOO0O0OOOO0O0O00 ,OO0O00O0O00O0O000 ,OOOOOOOOOOOOO0OOO ,OOO0OOOOO00000000 =cv2 .boundingRect (OO00OOO0O0O00000O )#line:539
        O00OO00O0OO0O0OOO .append ([OOOO0O0OOOO0O0O00 ,OO0O00O0O00O0O000 ,OOOOOOOOOOOOO0OOO ,OOO0OOOOO00000000 ])#line:541
    O00OO00O0OO0O0OOO =sorted (O00OO00O0OO0O0OOO )#line:543
    for O0OO0OOOOOOO0OOOO in range (len (OO0OOO0OOOOO0O00O )):#line:544
        OOOO0O0OOOO0O0O00 ,OO0O00O0O00O0O000 ,OOOOOOOOOOOOO0OOO ,OOO0OOOOO00000000 =O00OO00O0OO0O0OOO [O0OO0OOOOOOO0OOOO ]#line:545
        OO0OOOO0O0OOO00OO .append (O0OOOOOO0OO0O0O00 [OO0O00O0O00O0O000 :OO0O00O0O00O0O000 +OOO0OOOOO00000000 ,OOOO0O0OOOO0O0O00 :OOOO0O0OOOO0O0O00 +OOOOOOOOOOOOO0OOO ])#line:546
    return OO0OOOO0O0OOO00OO #line:547
def readpic (O0O0O00O0000000O0 ):#line:549
    try :#line:550
        OO00OO000OO0000OO =cv2 .ml .SVM_load ('maindata.xml')#line:551
        O0OO0OO000OO00000 =cut (O0O0O00O0000000O0 )#line:552
        O0OO0OO000OO00000 =list (map (hog ,O0OO0OO000OO00000 ))#line:553
        O0OO0OO000OO00000 =np .float32 (O0OO0OO000OO00000 ).reshape (-1 ,64 )#line:554
        O00O00OOOO0O0O00O =OO00OO000OO0000OO .predict (O0OO0OO000OO00000 )#line:555
        O00O00OOOO0O0O00O =O00O00OOOO0O0O00O [1 ].reshape (-1 ).astype (int ).astype (str )#line:556
        OO000O0OO00OOOOOO ="".join (list (O00O00OOOO0O0O00O ))#line:557
        return OO000O0OO00OOOOOO #line:558
    except :#line:559
        return False #line:560
import os #line:566
import socket #line:567
import struct #line:568
import select #line:569
import time #line:570
ICMP_ECHO_REQUEST =8 #line:572
DEFAULT_TIMEOUT =2 #line:573
DEFAULT_COUNT =1 #line:574
class Pinger (object ):#line:577
    ""#line:578
    def __init__ (O000O0OOO0OO0O0OO ,O0O0O0O0O0OOOOO0O ,OO00OO0OO000O0O0O =DEFAULT_COUNT ,O0O000000O0O000O0 =DEFAULT_TIMEOUT ):#line:580
        O000O0OOO0OO0O0OO .target_host =O0O0O0O0O0OOOOO0O #line:581
        O000O0OOO0OO0O0OO .count =OO00OO0OO000O0O0O #line:582
        O000O0OOO0OO0O0OO .timeout =O0O000000O0O000O0 #line:583
    def do_checksum (OOOO0000000O00O00 ,OO000OOOO0000OO0O ):#line:586
        ""#line:587
        O0O0OOO0OO0O00O0O =0 #line:588
        OOOOOOO000O00OOOO =(len (OO000OOOO0000OO0O )/2 )*2 #line:589
        OOO0OOO0O0OOOOOOO =0 #line:590
        while OOO0OOO0O0OOOOOOO <OOOOOOO000O00OOOO :#line:591
            OOOOOOOO00000OO00 =OO000OOOO0000OO0O [OOO0OOO0O0OOOOOOO +1 ]*256 +OO000OOOO0000OO0O [OOO0OOO0O0OOOOOOO ]#line:592
            O0O0OOO0OO0O00O0O =O0O0OOO0OO0O00O0O +OOOOOOOO00000OO00 #line:593
            O0O0OOO0OO0O00O0O =O0O0OOO0OO0O00O0O &0xffffffff #line:594
            OOO0OOO0O0OOOOOOO =OOO0OOO0O0OOOOOOO +2 #line:595
        if OOOOOOO000O00OOOO <len (OO000OOOO0000OO0O ):#line:597
            O0O0OOO0OO0O00O0O =O0O0OOO0OO0O00O0O +OO000OOOO0000OO0O [len (OO000OOOO0000OO0O )-1 ]#line:598
            O0O0OOO0OO0O00O0O =O0O0OOO0OO0O00O0O &0xffffffff #line:599
        O0O0OOO0OO0O00O0O =(O0O0OOO0OO0O00O0O >>16 )+(O0O0OOO0OO0O00O0O &0xffff )#line:600
        O0O0OOO0OO0O00O0O =O0O0OOO0OO0O00O0O +(O0O0OOO0OO0O00O0O >>16 )#line:601
        OOO0OOOO00O000OO0 =~O0O0OOO0OO0O00O0O #line:602
        OOO0OOOO00O000OO0 =OOO0OOOO00O000OO0 &0xffff #line:603
        OOO0OOOO00O000OO0 =OOO0OOOO00O000OO0 >>8 |(OOO0OOOO00O000OO0 <<8 &0xff00 )#line:604
        return OOO0OOOO00O000OO0 #line:605
    def receive_ping (OOO0O0OOO00OOO00O ,O0OO0OOO00O00000O ,OO0OO00OOOOOOO000 ,OOO0OO00OO00OOO0O ):#line:607
        OOO000OO0O0O00O00 =OOO0OO00OO00OOO0O #line:608
        while True :#line:609
            OOOO00000000O00O0 =time .time ()#line:610
            OO00O000O0O00O00O =select .select ([O0OO0OOO00O00000O ],[],[],OOO000OO0O0O00O00 )#line:611
            O0OO0O0OO00OOO000 =(time .time ()-OOOO00000000O00O0 )#line:612
            if OO00O000O0O00O00O [0 ]==[]:#line:613
                return #line:614
            OO0O000O000O0O0OO =time .time ()#line:616
            O0OO0OO0O00OO0OO0 ,O0O0OO0OO000O0OO0 =O0OO0OOO00O00000O .recvfrom (1024 )#line:617
            OOOOOO0O0000OO00O =O0OO0OO0O00OO0OO0 [20 :28 ]#line:618
            O0OO0O00000OO00O0 ,O0O000O00OOOOOO0O ,OO00000OO0OOOOO0O ,O0O0O00O0O00O00O0 ,O0OO0OOOOO00000O0 =struct .unpack ("bbHHh",OOOOOO0O0000OO00O )#line:621
            if O0O0O00O0O00O00O0 ==OO0OO00OOOOOOO000 :#line:622
                OOOO0O00O0OO0O00O =struct .calcsize ("d")#line:623
                OOOO0OO0OO00OO0OO =struct .unpack ("d",O0OO0OO0O00OO0OO0 [28 :28 +OOOO0O00O0OO0O00O ])[0 ]#line:624
                return OO0O000O000O0O0OO -OOOO0OO0OO00OO0OO #line:625
            OOO000OO0O0O00O00 =OOO000OO0O0O00O00 -O0OO0O0OO00OOO000 #line:627
            if OOO000OO0O0O00O00 <=0 :#line:628
                return #line:629
    def send_ping (O0O00OO000O00O0O0 ,OO0OOOO00O0O0O00O ,OO00OO0OO000OO00O ):#line:631
        ""#line:634
        OO0000000000O0OOO =socket .gethostbyname (O0O00OO000O00O0O0 .target_host )#line:635
        OOOOO00O0O00OO00O =0 #line:637
        O00O000O0000OO0OO =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,OOOOO00O0O00OO00O ,OO00OO0OO000OO00O ,1 )#line:640
        O0O0OOO00O0OO0OO0 =struct .calcsize ("d")#line:641
        OO00OO00000000OO0 =(192 -O0O0OOO00O0OO0OO0 )*"Q"#line:642
        OO00OO00000000OO0 =struct .pack ("d",time .time ())+bytes (OO00OO00000000OO0 ,encoding ="utf-8")#line:643
        OOOOO00O0O00OO00O =O0O00OO000O00O0O0 .do_checksum (O00O000O0000OO0OO +OO00OO00000000OO0 )#line:646
        O00O000O0000OO0OO =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,socket .htons (OOOOO00O0O00OO00O ),OO00OO0OO000OO00O ,1 )#line:649
        OO0OOOOOOOO0O0O00 =O00O000O0000OO0OO +OO00OO00000000OO0 #line:650
        OO0OOOO00O0O0O00O .sendto (OO0OOOOOOOO0O0O00 ,(OO0000000000O0OOO ,1 ))#line:651
    def ping_once (OOO0OO00O0O00O0O0 ):#line:653
        ""#line:656
        OOO0O000O0O00OOO0 =socket .getprotobyname ("icmp")#line:657
        try :#line:658
            OOOO0OO0OO00O0OOO =socket .socket (socket .AF_INET ,socket .SOCK_RAW ,OOO0O000O0O00OOO0 )#line:659
        except socket .error as OOOO000OO0000O0OO :#line:660
            if OOOO000OO0000O0OO [0 ]==1 :#line:661
                OOOO000OO0000O0OO [1 ]+="ICMP messages can only be sent from root user processes"#line:663
                raise socket .error (OOOO000OO0000O0OO [1 ])#line:664
        except Exception as O00O0O0OOO00OOO0O :#line:665
            print ("Exception: %s"%(O00O0O0OOO00OOO0O ))#line:666
        O00OOO0O0O0O0000O =os .getpid ()&0xFFFF #line:669
        OOO0OO00O0O00O0O0 .send_ping (OOOO0OO0OO00O0OOO ,O00OOO0O0O0O0000O )#line:671
        O00OOOOOO0000OO0O =OOO0OO00O0O00O0O0 .receive_ping (OOOO0OO0OO00O0OOO ,O00OOO0O0O0O0000O ,OOO0OO00O0O00O0O0 .timeout )#line:672
        OOOO0OO0OO00O0OOO .close ()#line:673
        return O00OOOOOO0000OO0O #line:674
    def ping (O00OOO000O00OO00O ):#line:676
        ""#line:679
        for O0OO00000O0O00000 in range (O00OOO000O00OO00O .count ):#line:680
            try :#line:682
                O000000000000O00O =O00OOO000O00OO00O .ping_once ()#line:683
            except socket .gaierror as O00OO00OOO0O000O0 :#line:684
                return "timeout"#line:686
            if O000000000000O00O ==None :#line:688
                return "timeout"#line:690
            else :#line:692
                O000000000000O00O =O000000000000O00O *1000 #line:693
                return int (O000000000000O00O )#line:695
pinger =Pinger (url2 )#line:697
import winreg ,re ,subprocess #line:701
needpath =r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'#line:702
path1 ='C:\Program Files (x86)'#line:703
path2 ='C:\Program Files'#line:704
def getwebpath ():#line:705
    global needpath #line:706
    try :#line:708
        OOOOOO00O00O000OO =winreg .OpenKey (winreg .HKEY_CLASSES_ROOT ,r"http\shell\open\command")#line:709
        O00OO0000O0O0OOOO ,OOOO000OOO0O0O0OO ,O000OO00OO0OOO00O =winreg .EnumValue (OOOOOO00O00O000OO ,0 )#line:710
        OOOO0OOOO000O0000 =re .compile ("\"*(.+\.exe)")#line:711
        O00OOOO0OO0OOO00O =re .findall (OOOO0OOOO000O0000 ,OOOO000OOO0O0O0OO )#line:712
        if O00OOOO0OO0OOO00O :#line:713
            needpath =O00OOOO0OO0OOO00O [0 ]#line:714
    except :#line:716
        pass #line:717
    if not os .path .exists (needpath ):#line:718
        if os .path .exists ('C:\Program Files (x86)'):#line:719
            pass #line:720
def openweb (O0O00O0O000000O0O ):#line:722
    global needpath #line:723
    subprocess .Popen ([needpath ,O0O00O0O000000O0O ])#line:726
import smtplib #line:729
from email .mime .text import MIMEText #line:732
import os #line:733
import mimetypes #line:734
import email #line:735
from email .mime .multipart import MIMEMultipart #line:736
from threading import Thread #line:739
import threading #line:740
from wx .lib .pubsub import pub #line:741
import socket ,sys ,json #line:746
timeout =10 #line:747
socket .setdefaulttimeout (timeout )#line:748
def ConfirmUser ():#line:750
    O00O0O000O00OO0OO =host_ali #line:751
    OO0OOO0OOOOOO0OOO =8080 #line:754
    OO0O0O0O0OO00O0OO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:756
    try :#line:758
        OO0O0O0O0OO00O0OO .connect ((O00O0O000O00OO0OO ,OO0OOO0OOOOOO0OOO ))#line:759
    except socket .gaierror as OO00000000O00O0OO :#line:760
        logging .error ('连接失败 %s'%OO00000000O00O0OO )#line:761
        logging .error ("Address-related error connecting to server: %s"%OO00000000O00O0OO )#line:762
        return 'net error'#line:763
    except socket .error as OO00000000O00O0OO :#line:765
        logging .error ('连接失败 %s'%OO00000000O00O0OO )#line:766
        logging .error ("Connection error: %s"%OO00000000O00O0OO )#line:767
        return 'net error'#line:768
    OO00OOO00OOOO00O0 =['login',Username ,Password ]#line:772
    OO00OOO00OOOO00O0 =json .dumps (OO00OOO00OOOO00O0 )#line:773
    OO00OOO00OOOO00O0 =bytes (OO00OOO00OOOO00O0 ,encoding ="utf-8")#line:774
    logging .info ('发送信息 %s'%str (OO00OOO00OOOO00O0 ,encoding ="utf-8"))#line:775
    OO0O0O0O0OO00O0OO .send (OO00OOO00OOOO00O0 )#line:776
    OO0O0O0O0OO00O0OO .shutdown (1 )#line:778
    logging .info ("Submit Complete")#line:779
    print ("Submit Complete")#line:780
    try :#line:781
        OOOO0O00O000O0O0O =OO0O0O0O0OO00O0OO .recv (1024 )#line:782
        print (OOOO0O00O000O0O0O )#line:783
        OOOO0O00O000O0O0O =str (OOOO0O00O000O0O0O ,encoding ="utf-8")#line:784
        OOOO0O00O000O0O0O =json .loads (OOOO0O00O000O0O0O )#line:785
        print ("login_reply%s"%OOOO0O00O000O0O0O )#line:786
        O00O000OOO00O00OO =OOOO0O00O000O0O0O [0 ]#line:787
        if O00O000OOO00O00OO =='success':#line:788
            logging .info ('登录成功 %s'%O00O000OOO00O00OO )#line:789
            global url2 ,url3 #line:790
            url2 =OOOO0O00O000O0O0O [1 ]#line:791
            url3 =OOOO0O00O000O0O0O [2 ]#line:792
            return 'login success'#line:793
        elif O00O000OOO00O00OO =='wrong password':#line:794
            logging .warning ('密码错误 %s'%O00O000OOO00O00OO )#line:795
            return 'wrong password'#line:796
        elif O00O000OOO00O00OO =="wrong account":#line:797
            logging .warning ('账号错误 %s'%O00O000OOO00O00OO )#line:798
            return 'wrong account'#line:799
        elif O00O000OOO00O00OO =='repeat':#line:800
            logging .warning ('账号错误 %s'%O00O000OOO00O00OO )#line:801
            return 'repeat'#line:802
    except :#line:803
        print ("连接失败")#line:804
        logging .warning ('连接失败 ')#line:805
        return False #line:806
def Logout ():#line:809
    O0OO0OO000O0000OO =host_ali #line:810
    O0O000O000OOOO0OO =8080 #line:813
    global Username #line:814
    O00OOO00000OOOO0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:815
    try :#line:816
        O00OOO00000OOOO0O .connect ((O0OO0OO000O0000OO ,O0O000O000OOOO0OO ))#line:817
    except socket .gaierror as O00O0OO000OO0OOO0 :#line:818
        print ("Address-related error connecting to server: %s"%O00O0OO000OO0OOO0 )#line:819
        logging .info ("Address-related error connecting to server: %s"%O00O0OO000OO0OOO0 )#line:820
    except socket .error as O00O0OO000OO0OOO0 :#line:822
        print ("Connection error: %s"%O00O0OO000OO0OOO0 )#line:823
        logging .info ("Connection error: %s"%O00O0OO000OO0OOO0 )#line:824
    O000000O0OOO0O000 =['logout',Username ,Password ]#line:828
    O000000O0OOO0O000 =json .dumps (O000000O0OOO0O000 )#line:829
    O000000O0OOO0O000 =bytes (O000000O0OOO0O000 ,encoding ="utf-8")#line:830
    logging .info ('发送信息 %s'%str (O000000O0OOO0O000 ,encoding ="utf-8"))#line:831
    O00OOO00000OOOO0O .send (O000000O0OOO0O000 )#line:832
    O00OOO00000OOOO0O .shutdown (1 )#line:833
    print ("Submit Log Out Complete")#line:834
    logging .info ("Submit Log Out Complete")#line:835
def Keeplogin ():#line:838
    OOO0OOOO00O0O00OO =host_ali #line:839
    O000000000OOO0OOO =8080 #line:842
    global Username #line:843
    OOO00OO0O000000OO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:844
    try :#line:845
        OOO00OO0O000000OO .connect ((OOO0OOOO00O0O00OO ,O000000000OOO0OOO ))#line:846
    except socket .gaierror as O00OO0OO0OOO000O0 :#line:847
        print ("Address-related error connecting to server: %s"%O00OO0OO0OOO000O0 )#line:848
        logging .info ("Address-related error connecting to server: %s"%O00OO0OO0OOO000O0 )#line:849
    except socket .error as O00OO0OO0OOO000O0 :#line:851
        print ("Connection error: %s"%O00OO0OO0OOO000O0 )#line:852
        logging .info ("Connection error: %s"%O00OO0OO0OOO000O0 )#line:853
    O0OOO00000OOO0OO0 =['keep',Username ,Password ]#line:857
    O0OOO00000OOO0OO0 =json .dumps (O0OOO00000OOO0OO0 )#line:858
    O0OOO00000OOO0OO0 =bytes (O0OOO00000OOO0OO0 ,encoding ="utf-8")#line:859
    logging .info ('发送信息 %s'%str (O0OOO00000OOO0OO0 ,encoding ="utf-8"))#line:860
    OOO00OO0O000000OO .send (O0OOO00000OOO0OO0 )#line:861
    OOO00OO0O000000OO .shutdown (1 )#line:863
    print ("Submit keep Complete")#line:864
    logging .info ("Submit keep Complete")#line:865
def send_mail (OO0OO0000OO0OOOOO ,OOO00OOOOO00000OO ,OO0000O0OOOOOO0OO ):#line:868
    O0O00OO0O0O00O0O0 =open (OO0000O0OOOOOO0OO ,'rb')#line:869
    OO0OO0O00OOO0OOO0 ,OO0O0OO00O0O0OO00 =mimetypes .guess_type (OO0000O0OOOOOO0OO )#line:870
    if OO0OO0O00OOO0OOO0 is None and OO0O0OO00O0O0OO00 is None :#line:871
        OO0OO0O00OOO0OOO0 ='application/octet-stream'#line:872
    OO0O0OO000OOOO0O0 ,OOOOO0OOOOOOO0O00 =OO0OO0O00OOO0OOO0 .split ('/',1 )#line:873
    OO00OOO0O0O0O0OO0 =email .mime .base .MIMEBase (OO0O0OO000OOOO0O0 ,OOOOO0OOOOOOO0O00 )#line:874
    OO00OOO0O0O0O0OO0 .set_payload (O0O00OO0O0O00O0O0 .read ())#line:875
    O0O00OO0O0O00O0O0 .close ()#line:876
    email .encoders .encode_base64 (OO00OOO0O0O0O0OO0 )#line:877
    OOO00O0OOO0O00000 =os .path .basename (OO0000O0OOOOOO0OO )#line:878
    OO00OOO0O0O0O0OO0 .add_header ('Content-Disposition','attachment',filename =OOO00O0OOO0O00000 )#line:879
    OOO00OOOOO00000OO =OOO00OOOOO00000OO #line:880
    O00OO000OOO00OO0O ='smtp.qq.com'#line:881
    O00OOOO00O0OO0OO0 =os .environ .get ('MAIL_USERNAME')#line:882
    OOO0O0O0O000000O0 =os .environ .get ('MAIL_PASSWORD')#line:883
    O0000OOO0O00O00O0 =O00OOOO00O0OO0OO0 #line:884
    O00000O0OO000OOOO =MIMEMultipart ()#line:885
    O00000O0OO000OOOO .attach (OO00OOO0O0O0O0OO0 )#line:886
    O00000O0OO000OOOO ['Subject']=OO0OO0000OO0OOOOO #line:887
    O00000O0OO000OOOO ['From']=O0000OOO0O00O00O0 #line:888
    O00000O0OO000OOOO ['To']=";".join (OOO00OOOOO00000OO )#line:889
    OOO0OO0000000O000 =smtplib .SMTP_SSL (O00OO000OOO00OO0O ,465 )#line:890
    OOO0OO0000000O000 .login (O00OOOO00O0OO0OO0 ,OOO0O0O0O000000O0 )#line:891
    print ('login in  successfully')#line:892
    OOO0OO0000000O000 .sendmail (O0000OOO0O00O00O0 ,OOO00OOOOO00000OO ,O00000O0OO000OOOO .as_string ())#line:893
    OOO0OO0000000O000 .quit ()#line:894
    print ('send email  successfully')#line:895
def Upload ():#line:897
    pass #line:898
def Com_read ():#line:901
    pass #line:902
def Com_decision ():#line:906
    pass #line:907
class TopFrame (wx .Frame ):#line:940
    def __init__ (OO00O0OO000000O00 ,OO00O00OO0OO0OOO0 ,OOO00O000O00OOOOO ):#line:941
        wx .Frame .__init__ (OO00O0OO000000O00 ,None ,1 ,OO00O00OO0OO0OOO0 ,size =(320 ,320 ))#line:943
        OO00O0OO000000O00 .Bind (wx .EVT_CLOSE ,OO00O0OO000000O00 .OnClose )#line:944
        OO00O0OO000000O00 .statusbar =OO00O0OO000000O00 .CreateStatusBar ()#line:946
        OO00O0OO000000O00 .statusbar .SetFieldsCount (3 )#line:948
        OO00O0OO000000O00 .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:949
        OO00O0OO000000O00 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:951
        OO00O0OO000000O00 .SetIcon (OO00O0OO000000O00 .icon )#line:952
        OO00O0OO000000O00 .statusbar .SetStatusText (u"版本号",0 )#line:954
        OO00O0OO000000O00 .statusbar .SetStatusText (u"%s"%OOO00O000O00OOOOO ,1 )#line:957
        OO00O0OO000000O00 .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:960
        OO00O0OO000000O00 .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:961
        O0O0OO0OOOO0O00OO =wx .Panel (OO00O0OO000000O00 ,-1 )#line:963
        O0O0OO0OOOO0O00OO .SetBackgroundColour ((240 ,255 ,255 ))#line:965
        OO00O0OO000000O00 .SetBackgroundColour ((240 ,255 ,255 ))#line:966
        OO00O0OO000000O00 .operationarea =wx .StaticBox (O0O0OO0OOOO0O00OO ,label ="基本功能")#line:969
        OO00O0OO000000O00 .operationareasizer =wx .StaticBoxSizer (OO00O0OO000000O00 .operationarea ,wx .VERTICAL )#line:970
        OO00O0OO000000O00 .hbox1 =wx .BoxSizer (wx .HORIZONTAL )#line:973
        OO00O0OO000000O00 .o0sdofsfo0sodf0so0button =wx .Button (O0O0OO0OOOO0O00OO ,label ='打开模拟')#line:974
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .Openo0sdofsfo0sodf0so0 ,OO00O0OO000000O00 .o0sdofsfo0sodf0so0button )#line:975
        OO00O0OO000000O00 .ooweo0o0werwrbutton =wx .Button (O0O0OO0OOOO0O00OO ,label ='打开国拍')#line:977
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .Openurlchoice ,OO00O0OO000000O00 .ooweo0o0werwrbutton )#line:978
        OO00O0OO000000O00 .hbox1 .Add (OO00O0OO000000O00 .o0sdofsfo0sodf0so0button ,0 ,wx .ALL |wx .CENTER ,5 )#line:979
        OO00O0OO000000O00 .hbox1 .Add (OO00O0OO000000O00 .ooweo0o0werwrbutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:980
        OO00O0OO000000O00 .operationareasizer .Add (OO00O0OO000000O00 .hbox1 )#line:981
        OO00O0OO000000O00 .helpbutton =wx .Button (O0O0OO0OOOO0O00OO ,label ='查看帮助')#line:983
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .help ,OO00O0OO000000O00 .helpbutton )#line:984
        OO00O0OO000000O00 .rulebutton =wx .Button (O0O0OO0OOOO0O00OO ,label ='查看规定')#line:985
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .rule ,OO00O0OO000000O00 .rulebutton )#line:986
        OO00O0OO000000O00 .hbox2 =wx .BoxSizer (wx .HORIZONTAL )#line:991
        OO00O0OO000000O00 .hbox2 .Add (OO00O0OO000000O00 .helpbutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:992
        OO00O0OO000000O00 .hbox2 .Add (OO00O0OO000000O00 .rulebutton ,0 ,wx .ALL |wx .CENTER ,5 )#line:993
        OO00O0OO000000O00 .operationareasizer .Add (OO00O0OO000000O00 .hbox2 )#line:994
        OO00O0OO000000O00 .set =wx .StaticBox (O0O0OO0OOOO0O00OO ,label ="常规设置")#line:997
        OO00O0OO000000O00 .setsizer =wx .StaticBoxSizer (OO00O0OO000000O00 .set )#line:998
        OO00O0OO000000O00 .hbox3 =wx .BoxSizer (wx .HORIZONTAL )#line:1000
        OO00O0OO000000O00 .advanceset =wx .Button (O0O0OO0OOOO0O00OO ,label ='策略设置')#line:1001
        OO00O0OO000000O00 .posautoset =wx .Button (O0O0OO0OOOO0O00OO ,label ='刷新定位')#line:1002
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .Advanceset ,OO00O0OO000000O00 .advanceset )#line:1003
        OO00O0OO000000O00 .Bind (wx .EVT_BUTTON ,OO00O0OO000000O00 .Posautoset ,OO00O0OO000000O00 .posautoset )#line:1004
        OO00O0OO000000O00 .hbox3 .Add (OO00O0OO000000O00 .advanceset ,0 ,wx .ALL |wx .CENTER ,5 )#line:1005
        OO00O0OO000000O00 .hbox3 .Add (OO00O0OO000000O00 .posautoset ,0 ,wx .ALL |wx .CENTER ,5 )#line:1006
        OO00O0OO000000O00 .hbox4 =wx .BoxSizer (wx .HORIZONTAL )#line:1008
        OO00O0OO000000O00 .highadvanceset =wx .Button (O0O0OO0OOOO0O00OO ,label ='动态策略')#line:1009
        OO00O0OO000000O00 .timeautoreset =wx .Button (O0O0OO0OOOO0O00OO ,label ='时间同步')#line:1010
        OO00O0OO000000O00 .hbox4 .Add (OO00O0OO000000O00 .highadvanceset ,0 ,wx .ALL |wx .CENTER ,5 )#line:1011
        OO00O0OO000000O00 .hbox4 .Add (OO00O0OO000000O00 .timeautoreset ,0 ,wx .ALL |wx .CENTER ,5 )#line:1012
        OO00O0OO000000O00 .vbox_setting =wx .BoxSizer (wx .VERTICAL )#line:1014
        OO00O0OO000000O00 .vbox_setting .Add (OO00O0OO000000O00 .hbox3 )#line:1017
        OO00O0OO000000O00 .vbox_setting .Add (OO00O0OO000000O00 .hbox4 )#line:1018
        OO00O0OO000000O00 .setsizer .Add (OO00O0OO000000O00 .vbox_setting )#line:1019
        OO00O0OO000000O00 .vbox =wx .BoxSizer (wx .VERTICAL )#line:1021
        OO00O0OO000000O00 .vbox .Add (OO00O0OO000000O00 .operationareasizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:1022
        OO00O0OO000000O00 .vbox .Add (OO00O0OO000000O00 .setsizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:1023
        O0O0OO0OOOO0O00OO .SetSizer (OO00O0OO000000O00 .vbox )#line:1024
        OO00O0OO000000O00 .thread =TimeThread ()#line:1036
        OO00O0OO000000O00 .keepthread =KeepThread ()#line:1037
        OO00O0OO000000O00 .operationframe =OperationFrame ()#line:1039
        OO00O0OO000000O00 .operationframe .Show (False )#line:1040
        OO00O0OO000000O00 .timer2 =wx .Timer (OO00O0OO000000O00 )#line:1043
        OO00O0OO000000O00 .Bind (wx .EVT_TIMER ,OO00O0OO000000O00 .MainControl ,OO00O0OO000000O00 .timer2 )#line:1044
        OO00O0OO000000O00 .timer2 .Start (100 )#line:1045
        OO00O0OO000000O00 .timer3 =wx .Timer (OO00O0OO000000O00 )#line:1048
        OO00O0OO000000O00 .Bind (wx .EVT_TIMER ,OO00O0OO000000O00 .Lowest_zxco0o0o0o0 ,OO00O0OO000000O00 .timer3 )#line:1049
        OO00O0OO000000O00 .timer3 .Start (100 )#line:1050
        OO00O0OO000000O00 .timer4 =wx .Timer (OO00O0OO000000O00 )#line:1052
        OO00O0OO000000O00 .Bind (wx .EVT_TIMER ,OO00O0OO000000O00 .Find_pos ,OO00O0OO000000O00 .timer4 )#line:1053
        OO00O0OO000000O00 .timer4 .Start (150 )#line:1054
        pub .subscribe (OO00O0OO000000O00 .OpenGuopai_dianxin ,"open dianxin")#line:1065
        pub .subscribe (OO00O0OO000000O00 .OpenGuopai_nodianxin ,"open nodianxin")#line:1066
    def Openo0sdofsfo0sodf0so0 (OOOOOO0000OO00OO0 ,OOOOOO0OO0OOOO000 ):#line:1071
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1073
        ghjo0o0o0o0_on =True #line:1074
        O0OOOOO00000000OO =True #line:1075
        oo0o0O0O0O0_on =True #line:1076
        oOO0O0O0O0O0O0_on =False #line:1077
        oOO0O0O0O0O0O0_num =1 #line:1078
        oOO0O0O0O0O0O0_OK =False #line:1079
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,ooweo0o0werwr_on ,o0sdofsfo0sodf0so0_on ,ghjo0o0o0o0_repeat #line:1080
        if ooweo0o0werwr_on :#line:1081
            wx .MessageBox ('请关闭国拍页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1082
        elif o0sdofsfo0sodf0so0_on :#line:1083
            wx .MessageBox ('请关闭模拟页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1084
        else :#line:1085
            OOOOOO0000OO00OO0 .Open ()#line:1090
            if do :#line:1091
                o0sdofsfo0sodf0so0_on =True #line:1092
                ad_view =True #line:1093
                web_on =True #line:1094
                OOOOOO0000OO00OO0 .fr =WebFrame (Px ,Py ,False ,'小鲜肉模拟')#line:1095
                if time_on :#line:1098
                    OOOOOO0000OO00OO0 .operationframe .Opentime ()#line:1099
                if not ghjo0o0o0o0_repeat :#line:1100
                    OOOOOO0000OO00OO0 .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1101
                    OOOOOO0000OO00OO0 .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1102
                    ghjo0o0o0o0_repeat =True #line:1103
                OOOOO00O0O00O0000 =wx .html2 .WebView .New (OOOOOO0000OO00OO0 .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ),style =wx .BORDER_NONE )#line:1106
                OOOOO00O0O00O0000 .LoadURL (url1 )#line:1107
                OOOOO00O0O00O0000 .CanSetZoomType (False )#line:1108
                OOOOOO0000OO00OO0 .fr .Show ()#line:1109
            else :#line:1113
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1114
                OOOOOO0000OO00OO0 .Close ()#line:1115
            OOOOOO0000OO00OO0 .Listen ()#line:1116
    def Openurlchoice (O00O00O0000OOO00O ,O0OO000O0OOO000O0 ):#line:1118
        OO00O00OOO00OOOO0 =Guopaiframe ("国拍")#line:1119
    def OpenGuopai_dianxin (OOO000OOOOOOOOO0O ):#line:1123
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1125
        ghjo0o0o0o0_on =True #line:1126
        O000OO00OOO0OO0OO =True #line:1127
        oo0o0O0O0O0_on =True #line:1128
        oOO0O0O0O0O0O0_on =False #line:1129
        oOO0O0O0O0O0O0_num =1 #line:1130
        oOO0O0O0O0O0O0_OK =False #line:1131
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1132
        if o0sdofsfo0sodf0so0_on :#line:1133
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1134
        elif ooweo0o0werwr_on :#line:1135
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1136
        else :#line:1137
            OOO000OOOOOOOOO0O .Open ()#line:1139
            if do :#line:1143
                ad_view =True #line:1144
                ooweo0o0werwr_on =True #line:1145
                OOO000OOOOOOOOO0O .fr =WebFrame (Px ,Py ,False ,'小鲜肉代拍 国拍')#line:1146
                if time_on :#line:1149
                    OOO000OOOOOOOOO0O .operationframe .Opentime ()#line:1150
                if not ghjo0o0o0o0_repeat :#line:1151
                    OOO000OOOOOOOOO0O .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1152
                    OOO000OOOOOOOOO0O .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1153
                    ghjo0o0o0o0_repeat =True #line:1154
                O0O00OO00OOOO0O00 =wx .html2 .WebView .New (OOO000OOOOOOOOO0O .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ))#line:1156
                O0O00OO00OOOO0O00 .LoadURL (url2 )#line:1157
                O0O00OO00OOOO0O00 .CanSetZoomType (False )#line:1158
                OOO000OOOOOOOOO0O .fr .Show ()#line:1159
            else :#line:1163
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1164
                OOO000OOOOOOOOO0O .Close ()#line:1165
            OOO000OOOOOOOOO0O .Listen ()#line:1166
    def OpenGuopai_nodianxin (O0OOO0OOO0OOOOO0O ):#line:1168
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1170
        ghjo0o0o0o0_on =True #line:1171
        O00000000O0OO0O00 =True #line:1172
        oo0o0O0O0O0_on =True #line:1173
        oOO0O0O0O0O0O0_on =False #line:1174
        oOO0O0O0O0O0O0_num =1 #line:1175
        oOO0O0O0O0O0O0_OK =False #line:1176
        global Px ,Py ,url3 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1177
        if o0sdofsfo0sodf0so0_on :#line:1178
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1179
        elif ooweo0o0werwr_on :#line:1180
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1181
        else :#line:1182
            O0OOO0OOO0OOOOO0O .Open ()#line:1184
            if do :#line:1188
                ad_view =True #line:1189
                ooweo0o0werwr_on =True #line:1190
                O0OOO0OOO0OOOOO0O .fr =WebFrame (Px ,Py ,False ,'小鲜肉代拍 国拍')#line:1191
                if time_on :#line:1194
                    O0OOO0OOO0OOOOO0O .operationframe .Opentime ()#line:1195
                if not ghjo0o0o0o0_repeat :#line:1196
                    O0OOO0OOO0OOOOO0O .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1197
                    O0OOO0OOO0OOOOO0O .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1198
                    ghjo0o0o0o0_repeat =True #line:1199
                OOOOO00O0000O0OOO =wx .html2 .WebView .New (O0OOO0OOO0OOOOO0O .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ))#line:1201
                OOOOO00O0000O0OOO .LoadURL (url3 )#line:1202
                OOOOO00O0000O0OOO .CanSetZoomType (False )#line:1203
                O0OOO0OOO0OOOOO0O .fr .Show ()#line:1204
            else :#line:1208
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1209
                O0OOO0OOO0OOOOO0O .Close ()#line:1210
            O0OOO0OOO0OOOOO0O .Listen ()#line:1211
    def UrlGuopai (OOO0OO0O0000O0O00 ,OO00O0O0O000O000O ):#line:1216
        global url2 #line:1217
        try :#line:1218
            url2 =OOO0OO0O0000O0O00 .urlText .GetValue ()#line:1219
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1220
        except :#line:1221
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1222
    def Help (OOOOO0O00O0OOOOO0 ,OO000OOO0OOOO0O00 ):#line:1224
        O0O000OOO0OOOO0OO ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1230
        OOO000O0OOOOOOO0O =wx .adv .AboutDialogInfo ()#line:1232
        OOO000O0OOOOOOO0O .SetName ("小鲜肉拍牌")#line:1233
        OOO000O0OOOOOOO0O .SetVersion (O0O000OOO0OOOO0OO )#line:1234
        OOO000O0OOOOOOO0O .AddDeveloper ("ZS")#line:1238
        wx .adv .AboutBox (OOO000O0OOOOOOO0O )#line:1239
    def rule (O00O00OOO0OO00OOO ,OOO000OOOO0000OOO ):#line:1241
        O000OO000O0O000OO ="http://hupai.pro/rules"#line:1242
        OpenwebThread (O000OO000O0O000OO )#line:1243
    def help (O0O0OO000OOO00O00 ,OO0O000OOOOOO000O ):#line:1244
        O0O0000OOOO000O0O ="http://hupai.pro/coursestudy"#line:1245
        OpenwebThread (O0O0000OOOO000O0O )#line:1246
    def Yan_practice (O0OO0O0000O0000O0 ,OOOO0OO0O0O0OOOOO ):#line:1248
        pass #line:1249
    def Yan_test (O0OO00O000O0O00OO ,O00O000000OO00O0O ):#line:1251
        pass #line:1252
    def Time_adjust (O00O0OOO00OO00O00 ,O00OO0000000000O0 ):#line:1255
        pass #line:1256
    def Advanceset (O00O0OO0O00OOOOO0 ,O00OOOO0OOOOOOO0O ):#line:1260
        O0OO0OOO000OO0O00 =O00O0OO0O00OOOOO0 .FindWindowById (2 )#line:1261
        O0OO0OOO000OO0O00 .Show (True )#line:1262
    def Posautoset (OOO0O0000OOO0OO00 ,OO000O0000O0O0000 ):#line:1264
        findpos ()#line:1265
    def Timeautoset (OO000OOOOOO00OOO0 ,OO00O00O0O0OOOOOO ):#line:1267
        pass #line:1268
    def Lowest_zxco0o0o0o0 (OO0000000O0O00OO0 ,OO00OO000OO0O0O0O ):#line:1276
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on ,changetime #line:1277
        if not findpos_on :#line:1278
            OOOOOOO0O0000OO00 =int (TopFrame .Price_read ())#line:1279
            if OOOOOOO0O0000OO00 in zxco0o0o0o0list :#line:1281
                if O0O0O0O0O0O0O_zxco0o0o0o0 ==OOOOOOO0O0000OO00 :#line:1282
                    pass #line:1283
                else :#line:1284
                    O0O0O0O0O0O0O_zxco0o0o0o0 =OOOOOOO0O0000OO00 #line:1285
                    if o0sdofsfo0sodf0so0_on :#line:1286
                        changetime =o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:1287
                    else :#line:1288
                        changetime =a_time #line:1289
            else :#line:1290
                findpos_on =True #line:1291
    def Find_pos (O0O000000OOO00O00 ,OO00O0OO000O00OO0 ):#line:1308
        global findpos_on #line:1309
        if findpos_on :#line:1310
            findpos ()#line:1311
    @staticmethod #line:1317
    def Confirm ():#line:1318
        global cf_hash ,sdfsf24324297_on #line:1319
        OOOO0OO00O000OOO0 =TopFrame .Confirm_hash ()#line:1320
        if OOOO0OO00O000OOO0 ==cf_hash [0 ]:#line:1321
            sdfsf24324297_on =True #line:1322
    @staticmethod #line:1323
    def Refresh ():#line:1324
        O0O000OO00000OO0O =TopFrame .Refresh_hash ()#line:1325
        global cf_hash ,uioo0o000oo_on #line:1326
        if O0O000OO00000OO0O ==cf_hash [1 ]:#line:1327
            uioo0o000oo_on =True #line:1328
    @staticmethod #line:1331
    def Price_read ():#line:1332
        OO0O00000OOO00OOO =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:1334
        OO0O00000OOO00OOO =np .asarray (OO0O00000OOO00OOO )#line:1340
        O0O0000OO00OOOO0O =readpic (OO0O00000OOO00OOO )#line:1341
        return O0O0000OO00OOOO0O #line:1343
    @staticmethod #line:1346
    def Price_hash ():#line:1347
        O0O0O000000O00OOO =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:1349
        global num #line:1350
        num +=1 #line:1351
        O00000OOO000OOO0O =imagehash .dhash (O0O0O000000O00OOO )#line:1353
        return O00000OOO000OOO0O #line:1356
    @staticmethod #line:1358
    def Confirm_hash ():#line:1359
        O0OO0O0OOOOO00O0O =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:1361
        OO0OO00O0OOOO00O0 =imagehash .dhash (O0OO0O0OOOOO00O0O )#line:1364
        return OO0OO00O0OOOO00O0 #line:1365
    @staticmethod #line:1367
    def Refresh_hash ():#line:1368
        O00000O0OOOOO000O =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:1370
        OO0O000O00O000OO0 =imagehash .dhash (O00000O0OOOOO000O )#line:1372
        return OO0O000O00O000OO0 #line:1373
    @staticmethod #line:1376
    def OnJiajia ():#line:1377
        OOO0OO00O000OOOO0 =pg .position ()#line:1378
        Oo0o0Oo0o0o0 [0 ][0 ]=OOO0OO00O000OOOO0 [0 ]#line:1379
        Oo0o0Oo0o0o0 [0 ][1 ]=OOO0OO00O000OOOO0 [1 ]#line:1380
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1381
        findpos ()#line:1382
    @staticmethod #line:1384
    def OnChujia ():#line:1385
        OO0OOO000O000O0O0 =pg .position ()#line:1386
        Oo0o0Oo0o0o0 [1 ][0 ]=OO0OOO000O000O0O0 [0 ]#line:1387
        Oo0o0Oo0o0o0 [1 ][1 ]=OO0OOO000O000O0O0 [1 ]#line:1388
    @staticmethod #line:1390
    def OnTijiao ():#line:1391
        OO000000O00O00OO0 =pg .position ()#line:1392
        Oo0o0Oo0o0o0 [2 ][0 ]=OO000000O00O00OO0 [0 ]#line:1393
        Oo0o0Oo0o0o0 [2 ][1 ]=OO000000O00O00OO0 [1 ]#line:1394
    @staticmethod #line:1396
    def OnShuaxin ():#line:1397
        O00O0O0OOOO00O0O0 =pg .position ()#line:1398
        Oo0o0Oo0o0o0 [3 ][0 ]=O00O0O0OOOO00O0O0 [0 ]#line:1399
        Oo0o0Oo0o0o0 [3 ][1 ]=O00O0O0OOOO00O0O0 [1 ]#line:1400
    @staticmethod #line:1402
    def OnConfirm ():#line:1403
        OO0OOO0000O00OOOO =pg .position ()#line:1404
        Oo0o0Oo0o0o0 [4 ][0 ]=OO0OOO0000O00OOOO [0 ]#line:1405
        Oo0o0Oo0o0o0 [4 ][1 ]=OO0OOO0000O00OOOO [1 ]#line:1406
    @staticmethod #line:1408
    def OnYanzhengma ():#line:1409
        O0OO0OO00OO0OOOOO =pg .position ()#line:1410
        Oo0o0Oo0o0o0 [5 ][0 ]=O0OO0OO00OO0OOOOO [0 ]#line:1411
        Oo0o0Oo0o0o0 [5 ][1 ]=O0OO0OO00OO0OOOOO [1 ]#line:1412
    @staticmethod #line:1415
    def handle_Jiajia ():#line:1416
        TopFrame .OnJiajia ()#line:1417
    @staticmethod #line:1419
    def handle_Chujia ():#line:1420
        TopFrame .OnChujia ()#line:1421
    @staticmethod #line:1423
    def handle_Tijiao ():#line:1424
        TopFrame .OnTijiao ()#line:1425
    @staticmethod #line:1427
    def handle_Shuaxin ():#line:1428
        TopFrame .OnShuaxin ()#line:1429
    @staticmethod #line:1431
    def handle_Confirm ():#line:1432
        TopFrame .OnConfirm ()#line:1433
    @staticmethod #line:1435
    def handle_Yanzhengma ():#line:1436
        TopFrame .OnYanzhengma ()#line:1437
    @classmethod #line:1445
    def OnClick_Tijiao (O0OOO00OOO00O0OO0 ):#line:1446
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1447
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1448
        sdfsf24324297_need =True #line:1449
        if oOO0O0O0O0O0O0_num ==1 :#line:1451
            O000O0OOO000000O0 =threading .Timer (one_delay ,O0OOO00OOO00O0OO0 .Tijiao )#line:1452
            O000O0OOO000000O0 .start ()#line:1453
            oOO0O0O0O0O0O0_on =False #line:1454
            if twice :#line:1455
                oOO0O0O0O0O0O0_num =2 #line:1456
        elif oOO0O0O0O0O0O0_num ==2 :#line:1458
            oOO0O0O0O0O0O0_num =0 #line:1459
            O000O0OOO000000O0 =threading .Timer (ooo0O0o0oO0O_delay ,O0OOO00OOO00O0OO0 .Tijiao )#line:1460
            O000O0OOO000000O0 .start ()#line:1461
            oOO0O0O0O0O0O0_on =False #line:1462
        else :#line:1464
            O0OOO00OOO00O0OO0 .Tijiao ()#line:1465
    @staticmethod #line:1467
    def Tijiao ():#line:1468
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1469
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1470
        oOO0O0O0O0O0O0_OK =False #line:1471
        global sdfsf24324297_one #line:1472
        if not sdfsf24324297_one :#line:1473
            O00OOOOO0000OO0OO =sdfsf24324297Thread ()#line:1474
            sdfsf24324297_one =True #line:1475
    @classmethod #line:1478
    def SmartTijiao (O00O0O000OOO0O0O0 ):#line:1479
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1480
        if o0sdofsfo0sodf0so0_on :#line:1481
            OOO0O0OO0000O0O00 =o0sdofsfo0sodf0so0_ooo0O0o0oO0O -changetime #line:1482
        else :#line:1483
            OOO0O0OO0000O0O00 =a_time -changetime #line:1484
        if O0O0O0O0O0O0O_zxco0o0o0o0 >own_zxco0o0o0o01 :#line:1486
            if O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -600 :#line:1487
                oOO0O0O0O0O0O0_num =0 #line:1488
                OOOOOO0O00O00000O =threading .Timer (0.5 ,O00O0O000OOO0O0O0 .Tijiao )#line:1489
                OOOOOO0O00O00000O .start ()#line:1490
                oOO0O0O0O0O0O0_on =False #line:1491
            elif O0O0O0O0O0O0O_zxco0o0o0o0 ==own_zxco0o0o0o02 -500 and OOO0O0OO0000O0O00 <1 :#line:1492
                oOO0O0O0O0O0O0_num =0 #line:1493
                OO0000OOOO00O0O00 =(1 -OOO0O0OO0000O0O00 )/3 +0.25 #line:1494
                OOOOOO0O00O00000O =threading .Timer (OO0000OOOO00O0O00 ,O00O0O000OOO0O0O0 .Tijiao )#line:1495
                OOOOOO0O00O00000O .start ()#line:1496
                oOO0O0O0O0O0O0_on =False #line:1497
            else :#line:1498
                oOO0O0O0O0O0O0_num =0 #line:1499
                O00O0O000OOO0O0O0 .Tijiao ()#line:1500
                oOO0O0O0O0O0O0_on =False #line:1501
        else :#line:1502
            if O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -600 :#line:1503
                OOOOOO0O00O00000O =threading .Timer (0.5 ,O00O0O000OOO0O0O0 .Tijiao )#line:1504
                OOOOOO0O00O00000O .start ()#line:1505
                oOO0O0O0O0O0O0_on =False #line:1506
                if twice :#line:1507
                    oOO0O0O0O0O0O0_num =2 #line:1508
            elif O0O0O0O0O0O0O_zxco0o0o0o0 ==own_zxco0o0o0o01 -500 and OOO0O0OO0000O0O00 <1 :#line:1509
                OO0000OOOO00O0O00 =(1 -OOO0O0OO0000O0O00 )/3 +0.25 #line:1510
                OOOOOO0O00O00000O =threading .Timer (OO0000OOOO00O0O00 ,O00O0O000OOO0O0O0 .Tijiao )#line:1511
                OOOOOO0O00O00000O .start ()#line:1512
                oOO0O0O0O0O0O0_on =False #line:1513
                if twice :#line:1514
                    oOO0O0O0O0O0O0_num =2 #line:1515
            else :#line:1516
                O00O0O000OOO0O0O0 .Tijiao ()#line:1517
                oOO0O0O0O0O0O0_on =False #line:1518
                if twice :#line:1519
                    oOO0O0O0O0O0O0_num =2 #line:1520
    @staticmethod #line:1529
    def OnClick_Shuaxin ():#line:1530
        global web_on #line:1531
        Click (Oo0o0Oo0o0o0 [3 ][0 ],Oo0o0Oo0o0o0 [3 ][1 ])#line:1532
        Click (Oo0o0Oo0o0o0 [5 ][0 ],Oo0o0Oo0o0o0 [5 ][1 ])#line:1533
    @staticmethod #line:1535
    def OnClick_sdfsf24324297 ():#line:1536
        print (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1537
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1538
    @staticmethod #line:1540
    def OnClick_oo0o0O0O0O0 ():#line:1541
        global web_on ,O0O0O0O0O0O0O_zxco0o0o0o0 #line:1542
        global oOO0O0O0O0O0O0_num ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:1543
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on #line:1544
        global uioo0o000oo_need ,uioo0o000oo_one ,oo0o0O0O0O0_interval #line:1545
        print (oo0o0O0O0O0_interval )#line:1546
        if not oo0o0O0O0O0_interval :#line:1547
            print (oOO0O0O0O0O0O0_num ,twice )#line:1548
            oo0o0O0O0O0_interval =True #line:1549
            oOO0O0O0O0O0O0_on =True #line:1550
            uioo0o000oo_need =True #line:1551
            if oOO0O0O0O0O0O0_num ==1 :#line:1552
                own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:1553
                setText (str (own_zxco0o0o0o01 ))#line:1554
                TopFrame .selfdelete ()#line:1555
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1556
                oOO0O0O0O0O0O0_on =True #line:1557
                oo0o0O0O0O0_on =False #line:1558
                oo0o0O0O0O0_interval =False #line:1559
                print (oo0o0O0O0O0_interval )#line:1560
                if not uioo0o000oo_one :#line:1562
                    O0O0OOO00OOOOOOO0 =uioo0o000ooThread ()#line:1563
                    uioo0o000oo_one =True #line:1564
            elif oOO0O0O0O0O0O0_num ==2 and twice :#line:1565
                own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:1567
                setText (str (own_zxco0o0o0o02 ))#line:1568
                TopFrame .selfdelete ()#line:1569
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1570
                oOO0O0O0O0O0O0_on =True #line:1571
                oo0o0O0O0O0_on =False #line:1572
                oo0o0O0O0O0_interval =False #line:1573
                if not uioo0o000oo_one :#line:1574
                    O0O0OOO00OOOOOOO0 =uioo0o000ooThread ()#line:1575
                    uioo0o000oo_one =True #line:1576
    @staticmethod #line:1578
    def selfdelete ():#line:1579
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1580
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1581
        Delete ()#line:1582
        if o0sdofsfo0sodf0so0_on :#line:1583
            Paste_o0sdofsfo0sodf0so0 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1584
        else :#line:1585
            Paste ()#line:1586
    @staticmethod #line:1588
    def selfChujia ():#line:1589
        global zxco0o0o0o0_view ,zxco0o0o0o0_count #line:1595
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1596
        Click (Oo0o0Oo0o0o0 [0 ][0 ],Oo0o0Oo0o0o0 [0 ][1 ])#line:1597
        Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1598
        zxco0o0o0o0_view =True #line:1599
        zxco0o0o0o0_count =0 #line:1600
    @staticmethod #line:1602
    def selfTijiao ():#line:1603
        OperationFrame .Del_shot ()#line:1604
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1605
    @staticmethod #line:1607
    def OnClick_Backspace ():#line:1608
        pg .press ('backspace')#line:1609
    def MainControl (OO00O0000O0000O0O ,O0OOO0O0O00000O00 ):#line:1611
        if not web_on and time_on :#line:1613
            OO00O0000O0000O0O .operationframe .Closetime ()#line:1614
    @staticmethod #line:1638
    def oOO0O0O0O0O0O0_ok ():#line:1639
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need ,oOO0O0O0O0O0O0_on #line:1640
        if e_on and oOO0O0O0O0O0O0_on :#line:1641
            oOO0O0O0O0O0O0_OK =True #line:1642
            uioo0o000oo_need =False #line:1643
    @staticmethod #line:1645
    def oOO0O0O0O0O0O0_ok2 ():#line:1646
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need #line:1647
        if enter_on and oOO0O0O0O0O0O0_on :#line:1648
            oOO0O0O0O0O0O0_OK =True #line:1649
            uioo0o000oo_need =False #line:1650
    @classmethod #line:1652
    def query (OO0000O000O000OOO ):#line:1653
        global query_interval ,query_on #line:1654
        if not query_interval and not query_on :#line:1655
            query_on =True #line:1657
            query_interval =True #line:1658
            setText (str (1000000 ))#line:1659
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1660
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1661
            if o0sdofsfo0sodf0so0_on :#line:1662
                print ("o0sdofsfo0sodf0so0")#line:1663
                Paste_o0sdofsfo0sodf0so0 ()#line:1664
            else :#line:1665
                Paste ()#line:1666
            Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1667
            OO0000OO00O0OOOO0 =threading .Timer (3 ,OO0000O000O000OOO .query_sleep3 )#line:1668
            OO0000OO00O0OOOO0 .start ()#line:1669
            O00O0OOOO000O0O0O =threading .Timer (5 ,OO0000O000O000OOO .query_sleep5 )#line:1670
            O00O0OOOO000O0O0O .start ()#line:1671
        elif query_interval and query_on :#line:1672
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1674
            query_on =False #line:1675
    @staticmethod #line:1677
    def query_sleep3 ():#line:1678
        global query_interval ,query_on #line:1680
        if query_on :#line:1681
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1683
            query_on =False #line:1684
    @staticmethod #line:1686
    def query_sleep5 ():#line:1687
        global query_interval #line:1689
        query_interval =False #line:1690
    @staticmethod #line:1694
    def Open ():#line:1695
        global do ,web_on #line:1696
        if not do :#line:1697
            do =True #line:1698
            O0000O000OO000O00 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1704
            O0OO00OOO0OOO0OOO =ctypes .windll .user32 #line:1705
            OOOO000OO0OO0O0OO ={1 :(O0000O000OO000O00 ['2'],win32con .MOD_ALT ),2 :(O0000O000OO000O00 ['3'],win32con .MOD_ALT ),3 :(O0000O000OO000O00 ['4'],win32con .MOD_ALT ),4 :(O0000O000OO000O00 ['5'],win32con .MOD_ALT ),5 :(O0000O000OO000O00 ['6'],win32con .MOD_ALT ),6 :(O0000O000OO000O00 ['7'],win32con .MOD_ALT ),}#line:1709
            O00O00000OOOOOO00 ={7 :(O0000O000OO000O00 ['s'],0x4000 ),8 :(O0000O000OO000O00 ['f'],0x4000 ),9 :(O0000O000OO000O00 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O0000O000OO000O00 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O0000O000OO000O00 ['q'],0x4000 )}#line:1712
            for O0OOOO0OO000000OO ,(O0OOO0OOO0O00OO00 ,OO00O0O0O000O00O0 )in OOOO000OO0OO0O0OO .items ():#line:1714
                if not O0OO00OOO0OOO0OOO .RegisterHotKey (None ,O0OOOO0OO000000OO ,OO00O0O0O000O00O0 ,O0OOO0OOO0O00OO00 ):#line:1715
                    print ("Unable to register id",O0OOOO0OO000000OO )#line:1716
                    logging .info ("Unable to register id",O0OOOO0OO000000OO )#line:1717
                    do =False #line:1718
            for O0OOOO0OO000000OO ,(O0OOO0OOO0O00OO00 ,OO00O0O0O000O00O0 )in O00O00000OOOOOO00 .items ():#line:1719
                if not O0OO00OOO0OOO0OOO .RegisterHotKey (None ,O0OOOO0OO000000OO ,OO00O0O0O000O00O0 ,O0OOO0OOO0O00OO00 ):#line:1720
                    print ("Unable to register id",O0OOOO0OO000000OO )#line:1721
                    logging .info ("Unable to register id",O0OOOO0OO000000OO )#line:1722
                    do =False #line:1723
                web_on =True #line:1724
    @staticmethod #line:1727
    def Listen ():#line:1728
        try :#line:1729
            OO00O00O00O0O000O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1734
            OOOOO0O0OO0O0O000 ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .selfTijiao ,9 :(lambda :TopFrame .selfChujia ()),10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .OnClick_oo0o0O0O0O0 }#line:1740
            O00O000OO0O00OO0O =ctypes .windll .user32 #line:1741
            OOO00O00OOOO000OO =wintypes .MSG ()#line:1742
            OO0O0O0O00O00OOOO =ctypes .byref #line:1743
            while O00O000OO0O00OO0O .GetMessageA (OO0O0O0O00O00OOOO (OOO00O00OOOO000OO ),None ,0 ,0 )!=0 :#line:1744
                if OOO00O00OOOO000OO .message ==win32con .WM_HOTKEY :#line:1745
                    OOO0OOOO0O0OO0O00 =OOOOO0O0OO0O0O000 .get (OOO00O00OOOO000OO .wParam )#line:1746
                    if OOO0OOOO0O0OO0O00 :#line:1747
                        OOO0OOOO0O0OO0O00 ()#line:1748
                O00O000OO0O00OO0O .TranslateMessage (OO0O0O0O00O00OOOO (OOO00O00OOOO000OO ))#line:1749
                O00O000OO0O00OO0O .DispatchMessageA (OO0O0O0O00O00OOOO (OOO00O00OOOO000OO ))#line:1750
        finally :#line:1751
            pass #line:1752
    @staticmethod #line:1760
    def Close ():#line:1761
        global do #line:1762
        if do :#line:1763
            do =False #line:1764
            OOOOOOO00OOO0OOO0 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1768
            O0OOO0OOOOOO00O00 ={1 :(OOOOOOO00OOO0OOO0 ['2'],win32con .MOD_ALT ),2 :(OOOOOOO00OOO0OOO0 ['3'],win32con .MOD_ALT ),3 :(OOOOOOO00OOO0OOO0 ['4'],win32con .MOD_ALT ),4 :(OOOOOOO00OOO0OOO0 ['5'],win32con .MOD_ALT ),5 :(OOOOOOO00OOO0OOO0 ['6'],win32con .MOD_ALT ),6 :(OOOOOOO00OOO0OOO0 ['7'],win32con .MOD_ALT ),}#line:1772
            O000OO0O00OO000OO =ctypes .windll .user32 #line:1773
            O00O0OOOO0O0OOO0O ={7 :(OOOOOOO00OOO0OOO0 ['s'],0x4000 ),8 :(OOOOOOO00OOO0OOO0 ['f'],0x4000 ),9 :(OOOOOOO00OOO0OOO0 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(OOOOOOO00OOO0OOO0 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(OOOOOOO00OOO0OOO0 ['q'],0x4000 )}#line:1776
            for OO0O0O00O0OO0O0O0 in O0OOO0OOOOOO00O00 .keys ():#line:1777
                O000OO0O00OO000OO .UnregisterHotKey (None ,OO0O0O00O0OO0O0O0 )#line:1778
            for OO0O0O00O0OO0O0O0 in O00O0OOOO0O0OOO0O .keys ():#line:1779
                O000OO0O00OO000OO .UnregisterHotKey (None ,OO0O0O00O0OO0O0O0 )#line:1780
            logging .info ("close assistant success")#line:1781
        else :#line:1782
            pass #line:1783
    def OnEraseBackground (O00O0O00000OO0OOO ,OOO0OO0O000O00000 ):#line:1789
        ""#line:1792
        O0000OO0O0O00000O =OOO0OO0O000O00000 .GetDC ()#line:1793
        if not O0000OO0O0O00000O :#line:1794
            O0000OO0O0O00000O =wx .ClientDC (O00O0O00000OO0OOO )#line:1795
            OOOO00000O000OOO0 =O00O0O00000OO0OOO .GetUpdateRegion ().GetBox ()#line:1796
            O0000OO0O0O00000O .SetClippingRect (OOOO00000O000OOO0 )#line:1797
        O0000OO0O0O00000O .Clear ()#line:1798
        O000OOO0O0OO0OOOO =wx .Bitmap ("blue.jpg")#line:1799
        O0000OO0O0O00000O .DrawBitmap (O000OOO0O0OO0OOOO ,0 ,0 )#line:1800
    def OnClose (O0000OOO0OOOO00O0 ,OOO000O0OOOO000O0 ):#line:1813
        OOO0O00O0O00O0OO0 =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1814
        if OOO0O00O0O00O0OO0 ==wx .OK :#line:1815
            import sys as OOOOO00OO0OOOOOOO #line:1817
            O0000OOO0OOOO00O0 .Show (False )#line:1822
            try :#line:1824
                O0000OOO0OOOO00O0 .Close_time1 (OOO000O0OOOO000O0 )#line:1825
                O0000OOO0OOOO00O0 .Close_time2 (OOO000O0OOOO000O0 )#line:1826
            except :#line:1827
                pass #line:1828
            Logout ()#line:1830
            wx .GetApp ().ExitMainLoop ()#line:1831
            OOO000O0OOOO000O0 .Skip ()#line:1832
            OOOOO00OO0OOOOOOO .exit (None )#line:1833
    def OnOpenAssist (OO0O000OOOO0O00O0 ):#line:1841
        OO0O000OOOO0O00O0 .Open ()#line:1842
        global do #line:1843
        if do :#line:1844
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1845
        else :#line:1846
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1847
        OO0O000OOOO0O00O0 .Listen ()#line:1848
    @classmethod #line:1850
    def OnCloseAssist (OO00OO00OO000OO0O ):#line:1851
        OO00OO00OO000OO0O .Close ()#line:1852
    def OnViewPos (OO0O0OO0O000O0O00 ,OOO000O00O00OOO00 ):#line:1862
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1863
        OO0O0OO0O000O0O00 .MovePos (OOO000O00O00OOO00 )#line:1864
        global view #line:1865
        if not view :#line:1866
            view =True #line:1867
            for OO00OOO00000OOOOO in range (len (Oo0o0Oo0o0o0 )):#line:1868
                OO0O0OO0O000O0O00 .posframe [OO00OOO00000OOOOO ].Show (view )#line:1869
        else :#line:1870
            view =False #line:1871
            for OO00OOO00000OOOOO in range (len (Oo0o0Oo0o0o0 )):#line:1872
                OO0O0OO0O000O0O00 .posframe [OO00OOO00000OOOOO ].Hide ()#line:1873
    def OnSavePos (OO00000OO00OOOO00 ,OOO00O000OOOO0OO0 ):#line:1876
        OO00000OO00OOOO00 .MovePos (OOO00O000OOOO0OO0 )#line:1877
        OO00000OO00OOOO00 .Save_log ()#line:1878
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1879
    def MovePos (OOO000O00O0000000 ,O0000OO0OO0OOOO00 ):#line:1885
        global Positon #line:1886
        for O00O0O00O00O0000O in range (5 ):#line:1887
            OOOOOOO0OOO0OOOO0 ,OOO00O00O000OOO00 =Oo0o0Oo0o0o0 [O00O0O00O00O0000O ]#line:1888
            OOO000O00O0000000 .posframe [O00O0O00O00O0000O ].Move (OOOOOOO0OOO0OOOO0 -10 ,OOO00O00O000OOO00 -5 )#line:1889
    def Save_log (OOOOO00000O0O0O00 ):#line:1969
        O00000O000OO00O00 =open ('pos.log','wb')#line:1970
        pickle .dump (Oo0o0Oo0o0o0 ,O00000O000OO00O00 )#line:1971
        O00000O000OO00O00 .close ()#line:1972
    def Confirmlogin (OOOOOO0OO0OO0OO0O ,OO000OO0000OO0O00 ):#line:2052
        Keeplogin ()#line:2053
    def Choose_time1 (OO0000OOOOOOOO0OO ,OOOOOO00000OOOOOO ):#line:2058
        OO0000OOOOOOOO0OO .timelabel .SetLabel ("已设定截止时间"+OO0000OOOOOOOO0OO .time_choice1 .GetString (OO0000OOOOOOOO0OO .time_choice1 .GetSelection ())+'.'+str (OO0000OOOOOOOO0OO .time_choice2 .GetSelection ())+" 秒")#line:2061
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:2062
        ghjo0o0o0o01 =OO0000OOOOOOOO0OO .time_choice1 .GetString (OO0000OOOOOOOO0OO .time_choice1 .GetSelection ())#line:2063
        ghjo0o0o0o02 =OO0000OOOOOOOO0OO .time_choice2 .GetString (OO0000OOOOOOOO0OO .time_choice2 .GetSelection ())#line:2064
    def Choose_time2 (O0000OOO0O0O0OO0O ,OOOOO0OOO000000OO ):#line:2067
        O0000OOO0O0O0OO0O .timelabel .SetLabel ("已设定截止时间"+O0000OOO0O0O0OO0O .time_choice1 .GetString (O0000OOO0O0O0OO0O .time_choice1 .GetSelection ())+'.'+str (O0000OOO0O0O0OO0O .time_choice2 .GetSelection ())+" 秒")#line:2070
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:2071
        ghjo0o0o0o01 =O0000OOO0O0O0OO0O .time_choice1 .GetString (O0000OOO0O0O0OO0O .time_choice1 .GetSelection ())#line:2072
        ghjo0o0o0o02 =O0000OOO0O0O0OO0O .time_choice2 .GetString (O0000OOO0O0O0OO0O .time_choice2 .GetSelection ())#line:2073
class ClockWindow (wx .Panel ):#line:2126
    def __init__ (O0O0O000O0OO0OO0O ,O000OO000O0O0O0O0 ):#line:2127
        wx .Window .__init__ (O0O0O000O0OO0OO0O ,O000OO000O0O0O0O0 ,size =Timesize )#line:2128
        O0O0O000O0OO0OO0O .Bind (wx .EVT_PAINT ,O0O0O000O0OO0OO0O .OnPaint )#line:2129
        O0O0O000O0OO0OO0O .timer =wx .Timer (O0O0O000O0OO0OO0O )#line:2130
        O0O0O000O0OO0OO0O .Bind (wx .EVT_TIMER ,O0O0O000O0OO0OO0O .OnTimer ,O0O0O000O0OO0OO0O .timer )#line:2131
        O0O0O000O0OO0OO0O .timer .Start (100 )#line:2132
    def Draw (O0OO0O0OO0O00OO0O ,OO0OOO00000O0O00O ):#line:2134
        global a_time #line:2135
        OO00O00O000000OO0 =time .localtime (a_time )#line:2136
        O0OOOO0OO0O0O0000 =time .strftime ("%H:%M:%S",OO00O00O000000OO0 )#line:2137
        OOOOO0O00OOOO0O0O ,OO00000OO0OOOO0O0 =O0OO0O0OO0O00OO0O .GetClientSize ()#line:2138
        OO0OOO00000O0O00O .SetBackground (wx .Brush (O0OO0O0OO0O00OO0O .GetBackgroundColour ()))#line:2139
        OO0OOO00000O0O00O .Clear ()#line:2140
        OO0OOO00000O0O00O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2141
        OOO0000OOO0O0O0O0 ,O00O0O000O0O000OO =OO0OOO00000O0O00O .GetTextExtent (O0OOOO0OO0O0O0000 )#line:2142
        OO0OOO00000O0O00O .DrawText (O0OOOO0OO0O0O0000 ,(OOOOO0O00OOOO0O0O -OOO0000OOO0O0O0O0 )/2 ,(OO00000OO0OOOO0O0 )/2 -O00O0O000O0O000OO /2 )#line:2143
    def Modify (OO00OOOOOO0OOO00O ,OOOO0OOOO00O00000 ):#line:2145
        global a_time ,b_time #line:2146
        if b_time <9 :#line:2148
            b_time =b_time +1 #line:2149
        else :#line:2150
            b_time =0 #line:2151
        OO0O00OO0O00O00O0 =time .localtime (a_time )#line:2152
        OOOOO000OOO000OOO =time .strftime ("%H:%M:%S",OO0O00OO0O00O00O0 )#line:2153
        O000OO00OO000O00O ,O0000OOOO0OOO0O00 =OO00OOOOOO0OOO00O .GetClientSize ()#line:2155
        OOOO0OOOO00O00000 .SetBackground (wx .Brush (OO00OOOOOO0OOO00O .GetBackgroundColour ()))#line:2156
        OOOO0OOOO00O00000 .Clear ()#line:2157
        OOOO0OOOO00O00000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2158
        O00OOO0OO0OOOOO00 ,O0OO0OO000000OOOO =OOOO0OOOO00O00000 .GetTextExtent (OOOOO000OOO000OOO )#line:2159
        OOOO0OOOO00O00000 .DrawText (OOOOO000OOO000OOO ,(O000OO00OO000O00O -O00OOO0OO0OOOOO00 )/2 ,(O0000OOOO0OOO0O00 )/2 -O0OO0OO000000OOOO /2 )#line:2160
    def OnTimer (O0O0000O0OO000000 ,O0O0OO000O00O0OO0 ):#line:2162
        O0O00OO00OOOO00OO =wx .BufferedDC (wx .ClientDC (O0O0000O0OO000000 ))#line:2163
        O0O0000O0OO000000 .Modify (O0O00OO00OOOO00OO )#line:2164
    def OnPaint (O0O000OO0000OO0OO ,OOO000OO0OOOOOOO0 ):#line:2166
        O0OO00OO0O00OO0O0 =wx .BufferedPaintDC (O0O000OO0000OO0OO )#line:2167
        O0O000OO0000OO0OO .Draw (O0OO00OO0O00OO0O0 )#line:2168
class TimeFrame (wx .Frame ):#line:2172
    def __init__ (O0OO00O0OO00OOO00 ):#line:2173
        wx .Frame .__init__ (O0OO00O0OO00OOO00 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2175
        ClockWindow (O0OO00O0OO00OOO00 )#line:2178
class MoniClockWindow (wx .Panel ):#line:2183
    def __init__ (OO0OO000O0OO0O0OO ,O0OO00O000OO000OO ):#line:2184
        wx .Window .__init__ (OO0OO000O0OO0O0OO ,O0OO00O000OO000OO ,size =Timesize )#line:2185
        OO0OO000O0OO0O0OO .Bind (wx .EVT_PAINT ,OO0OO000O0OO0O0OO .OnPaint )#line:2186
        OO0OO000O0OO0O0OO .timer =wx .Timer (OO0OO000O0OO0O0OO )#line:2187
        OO0OO000O0OO0O0OO .Bind (wx .EVT_TIMER ,OO0OO000O0OO0O0OO .OnTimer ,OO0OO000O0OO0O0OO .timer )#line:2188
        OO0OO000O0OO0O0OO .timer .Start (100 )#line:2189
    def Draw (O0000OO0OO000O0O0 ,OO00OOO00OOO0O0OO ):#line:2191
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2192
        OOO0OO0O0OOOOOO00 ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2193
        OO000OO0O000O0OOO ,OO00OO0O0O0OO0O0O =O0000OO0OO000O0O0 .GetClientSize ()#line:2194
        OO00OOO00OOO0O0OO .SetBackground (wx .Brush (O0000OO0OO000O0O0 .GetBackgroundColour ()))#line:2195
        OO00OOO00OOO0O0OO .Clear ()#line:2196
        OO00OOO00OOO0O0OO .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2197
        O0OOO00OOOOOOO000 ,O000000OO0000O0O0 =OO00OOO00OOO0O0OO .GetTextExtent (OOO0OO0O0OOOOOO00 )#line:2198
        OO00OOO00OOO0O0OO .DrawText (OOO0OO0O0OOOOOO00 ,(OO000OO0O000O0OOO -O0OOO00OOOOOOO000 )/2 ,(OO00OO0O0O0OO0O0O )/2 -O000000OO0000O0O0 /2 )#line:2199
    def Modify (O00OOOOO00OO000OO ,OOOO00OO00OOO000O ):#line:2201
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2202
        OO0OOOOO000OO00O0 =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2204
        OOOO000O00O0O000O ="%s:%s:%s"%(11 ,29 ,OO0OOOOO000OO00O0 )#line:2205
        OO0O0OOO000O000OO ,OO0000O0000OO00O0 =O00OOOOO00OO000OO .GetClientSize ()#line:2206
        OOOO00OO00OOO000O .SetBackground (wx .Brush (O00OOOOO00OO000OO .GetBackgroundColour ()))#line:2207
        OOOO00OO00OOO000O .Clear ()#line:2208
        OOOO00OO00OOO000O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2209
        O000OOO000O0O0OOO ,OO0OO0O0O000OO000 =OOOO00OO00OOO000O .GetTextExtent (OOOO000O00O0O000O )#line:2210
        OOOO00OO00OOO000O .DrawText (OOOO000O00O0O000O ,(OO0O0OOO000O000OO -O000OOO000O0O0OOO )/2 ,(OO0000O0000OO00O0 )/2 -OO0OO0O0O000OO000 /2 )#line:2211
    def OnTimer (O0OOOOOOO0O00OO00 ,OOO0O0OO00000O000 ):#line:2213
        O00OOOOOOOOOO0OO0 =wx .BufferedDC (wx .ClientDC (O0OOOOOOO0O00OO00 ))#line:2214
        O0OOOOOOO0O00OO00 .Modify (O00OOOOOOOOOO0OO0 )#line:2215
    def OnPaint (O0OO0000OOO00OOOO ,O00OO0OOOO0OOO000 ):#line:2217
        O0OOOOOOOOOOO0O0O =wx .BufferedPaintDC (O0OO0000OOO00OOOO )#line:2218
        O0OO0000OOO00OOOO .Draw (O0OOOOOOOOOOO0O0O )#line:2219
class MoniTimeFrame (wx .Frame ):#line:2223
    def __init__ (O0OO00O000O0OOOO0 ):#line:2224
        wx .Frame .__init__ (O0OO00O000O0OOOO0 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2226
        MoniClockWindow (O0OO00O000O0OOOO0 )#line:2229
class PosFrame (wx .Frame ):#line:2234
    def __init__ (OOO00000O0O0000OO ,OO000000O0OO0OO0O ,OO0OO000000O0O0OO ):#line:2235
        O0000OOOOO0O0OO0O ,O0O0000O0OOOOOOOO =OO000000O0OO0OO0O #line:2236
        wx .Frame .__init__ (OOO00000O0O0000OO ,None ,-1 ,'POS',pos =(O0000OOOOO0O0OO0O -20 ,O0O0000O0OOOOOOOO -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:2238
        OOO0O000O00O000OO =wx .Panel (OOO00000O0O0000OO ,-1 ,size =(30 ,20 ))#line:2239
        O00000OOO0000O000 =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2241
        OO0O0000OO00O00OO =[]#line:2242
        OO0O0000OO00O00OO .append (wx .StaticText (OOO0O000O00O000OO ,-1 ,OO0OO000000O0O0OO ,(0 ,0 )))#line:2244
        for O0O0O00O0OOOO0OOO in range (len (OO0O0000OO00O00OO )):#line:2245
            OO0O0000OO00O00OO [O0O0O00O0OOOO0OOO ].SetFont (O00000OOO0000O000 )#line:2246
class PriceFrame (wx .Frame ):#line:2248
    def __init__ (OOOOOOOO0000000OO ,OO0O00OOO00000O00 ):#line:2249
        wx .Frame .__init__ (OOOOOOOO0000000OO ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2252
        OOOOOOOO0000000OO .panel =wx .Panel (OOOOOOOO0000000OO ,size =Pricesize )#line:2253
        wx .StaticBitmap (OOOOOOOO0000000OO .panel ,-1 ,wx .BitmapFromImage (OO0O00OOO00000O00 ))#line:2255
class YanzhengmaFrame (wx .Frame ):#line:2257
    def __init__ (OO0OOOOOOOO0OOO00 ,O0O00O0O0O00O0OOO ):#line:2258
        wx .Frame .__init__ (OO0OOOOOOOO0OOO00 ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2261
        OO0OOOOOOOO0OOO00 .panel =wx .Panel (OO0OOOOOOOO0OOO00 ,size =(400 ,80 ))#line:2262
        wx .StaticBitmap (OO0OOOOOOOO0OOO00 .panel ,-1 ,wx .BitmapFromImage (O0O00O0O0O00O0OOO ))#line:2264
class AdFrame (wx .Frame ):#line:2268
    def __init__ (OOO00OO000O0O0OOO ):#line:2269
        wx .Frame .__init__ (OOO00OO000O0O0OOO ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2271
        OO0OOO0O0OO0OOOOO =wx .Panel (OOO00OO000O0O0OOO ,-1 ,size =(250 ,200 ))#line:2272
        O00O00O000O00O000 =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2274
        OOO00O0O0000O000O =[]#line:2275
        OOO00O0O0000O000O .append (wx .StaticText (OO0OOO0O0OO0OOOOO ,-1 ," 专业代拍软件",(15 ,10 )))#line:2277
        OOO00O0O0000O000O .append (wx .StaticText (OO0OOO0O0OO0OOOOO ,-1 ," 专业代拍团队",(15 ,60 )))#line:2279
        OOO00O0O0000O000O .append (wx .StaticText (OO0OOO0O0OO0OOOOO ,-1 ,"关注微信公众号",(15 ,110 )))#line:2281
        OOO00O0O0000O000O .append (wx .StaticText (OO0OOO0O0OO0OOOOO ,-1 ," 小鲜肉拍牌",(15 ,160 )))#line:2283
        for O0OO00O00000OO00O in range (len (OOO00O0O0000O000O )):#line:2284
            OOO00O0O0000O000O [O0OO00O00000OO00O ].SetFont (O00O00O000O00O000 )#line:2285
class WebFrame (wx .Frame ):#line:2287
    def __init__ (O00OOOOO0O00O0O00 ,O0000OO00000OOO0O ,O0O0O00OOOOOO0000 ,OO00OOO0O0OO00O0O ,OO0O00000O000O00O ):#line:2288
        wx .Frame .__init__ (O00OOOOO0O00O0O00 ,None ,3 ,OO0O00000O000O00O ,size =(websize [0 ],websize [1 ]),pos =(O0000OO00000OOO0O ,O0O0O00OOOOOO0000 ),style =wx .SIMPLE_BORDER )#line:2289
        if OO00OOO0O0OO00O0O :#line:2294
            O00OOOOO0O00O0O00 .adframe =AdFrame ()#line:2295
            O00OOOOO0O00O0O00 .adframe .Show (True )#line:2296
        O00OOOOO0O00O0O00 .Bind (wx .EVT_CLOSE ,O00OOOOO0O00O0O00 .OnClose )#line:2297
        O00OOOOO0O00O0O00 .ad2 =OO00OOO0O0OO00O0O #line:2298
        O00OOOOO0O00O0O00 .control =ControlFrame ()#line:2299
        global test #line:2301
        if not test :#line:2303
            O00OOOOO0O00O0O00 .control .Show (True )#line:2304
        pub .subscribe (O00OOOOO0O00O0O00 .OnClose2 ,"close web")#line:2330
    def OnClose (OO0OOO000O000000O ,O0O000O00OOO000O0 ):#line:2331
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2332
        web_on =False #line:2333
        view_time =False #line:2334
        o0sdofsfo0sodf0so0_on =False #line:2336
        ooweo0o0werwr_on =False #line:2337
        TopFrame .Close ()#line:2338
        OOO0OOO0O0O0000O0 ="sc_new.png"#line:2339
        OO0OOO000O000000O .control .Destroy ()#line:2342
        if os .path .exists (OOO0OOO0O0O0000O0 ):#line:2343
            os .remove (OOO0OOO0O0O0000O0 )#line:2344
        OO0OOO000O000000O .Destroy ()#line:2345
        if OO0OOO000O000000O .ad2 :#line:2346
            OO0OOO000O000000O .adframe .Destroy ()#line:2347
        O0O000O00OOO000O0 .Skip ()#line:2348
    def OnClose2 (OOOO0O0OO0OO0O000 ):#line:2350
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2351
        web_on =False #line:2352
        view_time =False #line:2353
        o0sdofsfo0sodf0so0_on =False #line:2354
        ooweo0o0werwr_on =False #line:2355
        TopFrame .Close ()#line:2356
        OO0OO0OO00OOO0000 ="sc_new.png"#line:2357
        if os .path .exists (OO0OO0OO00OOO0000 ):#line:2358
            os .remove (OO0OO0OO00OOO0000 )#line:2359
        OOOO0O0OO0OO0O000 .Destroy ()#line:2360
        if OOOO0O0OO0OO0O000 .ad2 :#line:2361
            OOOO0O0OO0OO0O000 .adframe .Destroy ()#line:2362
class ControlFrame (wx .Frame ):#line:2365
    def __init__ (OO0OOO0OOO0O000OO ):#line:2366
        wx .Frame .__init__ (OO0OOO0OOO0O000OO ,None ,4 ,size =(330 ,200 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +40 ,Py +480 ),name ="control")#line:2368
        OO0OOO0OOO0O000OO .panel =wx .Panel (OO0OOO0OOO0O000OO ,-1 ,size =(330 ,270 ))#line:2369
        O0OO0OO0O0OO0O00O =wx .Font (25 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2372
        O00OO0OO0O00000OO =wx .Font (15 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2373
        OO0OOO0OOO0O000OO .adtext =wx .StaticText (OO0OOO0OOO0O000OO .panel ,label =u"小鲜肉代拍",pos =(90 ,20 ))#line:2374
        OO0OOO0OOO0O000OO .adtext .SetFont (O0OO0OO0O0OO0O00O )#line:2375
        OO0OOO0OOO0O000OO .zxco0o0o0o0text =wx .StaticText (OO0OOO0OOO0O000OO .panel ,label =u"最低成交价:",pos =(50 ,90 ))#line:2376
        OO0OOO0OOO0O000OO .zxco0o0o0o0text .SetFont (O00OO0OO0O00000OO )#line:2377
        OO0OOO0OOO0O000OO .zxco0o0o0o0 =wx .StaticText (OO0OOO0OOO0O000OO .panel ,pos =(190 ,90 ))#line:2378
        OO0OOO0OOO0O000OO .zxco0o0o0o0 .SetFont (O00OO0OO0O00000OO )#line:2379
        OO0OOO0OOO0O000OO .timetext =wx .StaticText (OO0OOO0OOO0O000OO .panel ,label =u"当前时间:",pos =(50 ,130 ))#line:2380
        OO0OOO0OOO0O000OO .timetext .SetFont (O00OO0OO0O00000OO )#line:2381
        OO0OOO0OOO0O000OO .time =wx .StaticText (OO0OOO0OOO0O000OO .panel ,pos =(190 ,130 ))#line:2382
        OO0OOO0OOO0O000OO .time .SetFont (O00OO0OO0O00000OO )#line:2383
        OO0OOO0OOO0O000OO .netstattext =wx .StaticText (OO0OOO0OOO0O000OO .panel ,pos =(80 ,170 ),label =u"网速")#line:2385
        OO0OOO0OOO0O000OO .netstattext .SetFont (O00OO0OO0O00000OO )#line:2386
        OO0OOO0OOO0O000OO .netstat =wx .StaticText (OO0OOO0OOO0O000OO .panel ,pos =(190 ,170 ))#line:2387
        OO0OOO0OOO0O000OO .timetimer1 =wx .Timer (OO0OOO0OOO0O000OO )#line:2391
        OO0OOO0OOO0O000OO .Bind (wx .EVT_TIMER ,OO0OOO0OOO0O000OO .Timego ,OO0OOO0OOO0O000OO .timetimer1 )#line:2392
        OO0OOO0OOO0O000OO .timetimer1 .Start (100 )#line:2393
    def o_closeweb (OO000O0O0OOO0OO00 ,OO0OO00O0000OOOO0 ):#line:2394
        wx .CallAfter (pub .sendMessage ,"close web")#line:2395
        OO000O0O0OOO0OO00 .Destroy ()#line:2396
        OO0OO00O0000OOOO0 .Skip ()#line:2397
    def Timego (O000OO0O0OO00000O ,OO0OOOOOO000O0O00 ):#line:2399
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,a_time #line:2400
        O000OO0O0OO00000O .zxco0o0o0o0 .SetLabel ("%s"%O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2401
        if o0sdofsfo0sodf0so0_on :#line:2402
            O000OO0O0OO00000O .time .SetLabel ("11:29:%s"%int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:2403
        else :#line:2404
            O00O00OO0OOO00OO0 =time .localtime (a_time )#line:2405
            OOO0OO00000O0OOO0 =time .strftime ("%H:%M:%S",O00O00OO0OOO00OO0 )#line:2406
            O000OO0O0OO00000O .time .SetLabel (OOO0OO00000O0OOO0 )#line:2407
        global pinger #line:2408
        O0O0OO0O0O00OO00O =pinger .ping ()#line:2409
        if O0O0OO0O0O00OO00O =="timeout":#line:2410
            O000OO0O0OO00000O .netstat .SetLabel ("%s"%O0O0OO0O0O00OO00O )#line:2411
        else :#line:2412
            O000OO0O0OO00000O .netstat .SetLabel ("%sms"%O0O0OO0O0O00OO00O )#line:2413
class OperationFrame (wx .Frame ):#line:2416
    def __init__ (OO0O0OO0O00000OO0 ):#line:2417
        wx .Frame .__init__ (OO0O0OO0O00000OO0 ,None ,2 ,title ="小鲜肉代拍",pos =(1070 ,100 ),size =(300 ,425 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION |wx .CLOSE_BOX )#line:2419
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CLOSE ,OO0O0OO0O00000OO0 .OnClose )#line:2421
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2423
        one_oO0O0O0O0O0O0O0O01 =OO0O0OO0O00000OO0 .gettime (OO00000o01 )#line:2424
        one_oO0O0O0O0O0O0O0O02 =OO0O0OO0O00000OO0 .gettime (OO00000o02 )#line:2425
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0O0OO0O00000OO0 .gettime (ooo0O0o0oO0O_time1 )#line:2426
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0O0OO0O00000OO0 .gettime (ooo0O0o0oO0O_time2 )#line:2427
        OO0O0OO0O00000OO0 .timer1 =wx .Timer (OO0O0OO0O00000OO0 )#line:2429
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TIMER ,OO0O0OO0O00000OO0 .Price_view ,OO0O0OO0O00000OO0 .timer1 )#line:2430
        OO0O0OO0O00000OO0 .timer1 .Start (500 )#line:2431
        OO0O0OO0O00000OO0 .timer2 =wx .Timer (OO0O0OO0O00000OO0 )#line:2433
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TIMER ,OO0O0OO0O00000OO0 .Price_count ,OO0O0OO0O00000OO0 .timer2 )#line:2434
        OO0O0OO0O00000OO0 .timer2 .Start (100 )#line:2435
        OO0O0OO0O00000OO0 .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:2437
        OO0O0OO0O00000OO0 .O0O0O0O0O0O0Oframe .Show (False )#line:2438
        OOO0O0O0OOOOO0O00 =wx .Panel (OO0O0OO0O00000OO0 ,-1 ,size =(300 ,380 ))#line:2442
        OO0O0OOOO00O00OO0 =wx .StaticBox (OOO0O0O0OOOOO0O00 ,-1 ,u'选择策略:')#line:2443
        OO0O0OO0O00000OO0 .stractagySizer =wx .StaticBoxSizer (OO0O0OOOO00O00OO0 ,wx .VERTICAL )#line:2444
        OO0OOOO0OOO0000OO =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2445
        O0OO0OO0000O000OO =wx .BoxSizer (wx .HORIZONTAL )#line:2446
        O0OO0OO0000O000OO .Add (OO0OOOO0OOO0000OO )#line:2447
        OO00O00O00OO00OO0 =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2452
        OO0O0OO0O00000OO0 .select_stractagy =wx .Choice (OOO0O0O0OOOOO0O00 ,-1 ,choices =OO00O00O00OO00OO0 ,size =(100 ,50 ))#line:2453
        O0OO0OO0000O000OO .Add (OO0O0OO0O00000OO0 .select_stractagy )#line:2454
        OO0O0OO0O00000OO0 .select_stractagy .SetSelection (0 )#line:2455
        OO0O0OO0O00000OO0 .timeview =wx .CheckBox (OOO0O0O0OOOOO0O00 ,-1 ,label =u'显示时间')#line:2457
        O000OOO00OO000OO0 =wx .BoxSizer (wx .HORIZONTAL )#line:2458
        O000OOO00OO000OO0 .Add (OO0O0OO0O00000OO0 .timeview )#line:2459
        OO0O0OO0O00000OO0 .button1 =wx .Button (OOO0O0O0OOOOO0O00 ,label ='+1s',size =(35 ,25 ))#line:2462
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Add_ooo0O0o0oO0O ,OO0O0OO0O00000OO0 .button1 )#line:2463
        OO0O0OO0O00000OO0 .button2 =wx .Button (OOO0O0O0OOOOO0O00 ,label ='-1s',size =(35 ,25 ))#line:2464
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Minus_ooo0O0o0oO0O ,OO0O0OO0O00000OO0 .button2 )#line:2465
        OO0O0OO0O00000OO0 .button3 =wx .Button (OOO0O0O0OOOOO0O00 ,label ='+0.1s',size =(35 ,25 ))#line:2466
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Add_time ,OO0O0OO0O00000OO0 .button3 )#line:2467
        OO0O0OO0O00000OO0 .button4 =wx .Button (OOO0O0O0OOOOO0O00 ,label ='-0.1s',size =(35 ,25 ))#line:2468
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Minus_time ,OO0O0OO0O00000OO0 .button4 )#line:2469
        O000OOO00OO000OO0 .Add (OO0O0OO0O00000OO0 .button1 )#line:2471
        O000OOO00OO000OO0 .Add (OO0O0OO0O00000OO0 .button2 )#line:2472
        O000OOO00OO000OO0 .Add (OO0O0OO0O00000OO0 .button3 )#line:2473
        O000OOO00OO000OO0 .Add (OO0O0OO0O00000OO0 .button4 )#line:2474
        O00O000OOO00OOOOO =wx .BoxSizer (wx .VERTICAL )#line:2476
        O00O000OOO00OOOOO .Add (O0OO0OO0000O000OO )#line:2477
        O00O000OOO00OOOOO .Add (O000OOO00OO000OO0 )#line:2478
        O00O000OO0OOO0OOO =["E键","回车"]#line:2481
        OO0O0OO0O00000OO0 .sdfsf24324297_choice =wx .Choice (OOO0O0O0OOOOO0O00 ,-1 ,choices =O00O000OO0OOO0OOO )#line:2482
        OO0O0OO0O00000OO0 .sdfsf24324297_choice .SetSelection (0 )#line:2483
        OO0O0OO0O00000OO0 .sdfsf24324297_label =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"确认提交方式     ")#line:2484
        OO00O0O0000OO0O0O =wx .BoxSizer (wx .HORIZONTAL )#line:2485
        OO00O0O0000OO0O0O .Add (OO0O0OO0O00000OO0 .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2486
        OO00O0O0000OO0O0O .Add (OO0O0OO0O00000OO0 .sdfsf24324297_choice )#line:2487
        O00O000OOO00OOOOO .Add (OO00O0O0000OO0O0O )#line:2488
        OO0O0OO0O00000OO0 .ghjo0o0o0o0_save =wx .Button (OOO0O0O0OOOOO0O00 ,label ="保存策略",size =(60 ,35 ))#line:2491
        OO0O0OO0O00000OO0 .ghjo0o0o0o0_load =wx .Button (OOO0O0O0OOOOO0O00 ,label ="载入策略",size =(60 ,35 ))#line:2492
        OO0O0OO0O00000OO0 .save_info =wx .Button (OOO0O0O0OOOOO0O00 ,label ="用户信息",size =(60 ,35 ))#line:2493
        OOO00O000OO00OO00 =wx .BoxSizer (wx .HORIZONTAL )#line:2494
        OOO00O000OO00OO00 .Add (OO0O0OO0O00000OO0 .ghjo0o0o0o0_save )#line:2495
        OOO00O000OO00OO00 .Add (OO0O0OO0O00000OO0 .ghjo0o0o0o0_load )#line:2496
        OOO00O000OO00OO00 .Add (OO0O0OO0O00000OO0 .save_info )#line:2497
        O00O000OOO00OOOOO .Add (OOO00O000OO00OO00 )#line:2498
        OOOOOO0OOO00OOO00 =wx .StaticBox (OOO0O0O0OOOOO0O00 ,-1 ,u'单枪策略:')#line:2502
        OO0O0OO0O00000OO0 .oneshotSizer =wx .StaticBoxSizer (OOOOOO0OOO00OOO00 ,wx .VERTICAL )#line:2503
        O000O0000O00OO00O =wx .GridBagSizer (4 ,4 )#line:2504
        OO0O0OO0O00000OO0 .jiajia_time =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2505
        OO0O0OO0O00000OO0 .jiajia_time .SetRange (40 ,55 )#line:2506
        OO0O0OO0O00000OO0 .jiajia_time .SetValue (48 )#line:2507
        OO0O0OO0O00000OO0 .jiajia_time .SetIncrement (0.1 )#line:2508
        O000O0000O00OO00O .Add (OO0O0OO0O00000OO0 .jiajia_time ,pos =(0 ,0 ))#line:2510
        OOOO0O00OOO0OO0OO =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2511
        O000O0000O00OO00O .Add (OOOO0O00OOO0OO0OO ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2512
        O0OOO000OOOOO0000 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2513
        O000O0000O00OO00O .Add (O0OOO000OOOOO0000 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2514
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2515
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2516
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2517
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2518
        O000O0000O00OO00O .Add (OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2519
        OO00OO00OOOO0O0OO =[u"提前100",u"提前200",u"踩点"]#line:2522
        OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O0 =wx .Choice (OOO0O0O0OOOOO0O00 ,-1 ,choices =OO00OO00OOOO0O0OO ,size =(68 ,25 ))#line:2523
        OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2524
        O000O0000O00OO00O .Add (OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2525
        O00OOOOOOOO000O00 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"出价提交延迟")#line:2526
        O000O0000O00OO00O .Add (O00OOOOOOOO000O00 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2527
        OO0O0OO0O00000OO0 .yanchi_time =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2528
        OO0O0OO0O00000OO0 .yanchi_time .SetRange (0.0 ,1.0 )#line:2529
        OO0O0OO0O00000OO0 .yanchi_time .SetValue (0.5 )#line:2530
        OO0O0OO0O00000OO0 .yanchi_time .SetIncrement (0.1 )#line:2531
        O000O0000O00OO00O .Add (OO0O0OO0O00000OO0 .yanchi_time ,pos =(1 ,3 ))#line:2532
        OO0OO00OOOOO00OOO =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2533
        O000O0000O00OO00O .Add (OO0OO00OOOOO00OOO ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2534
        O0OO000OOOO00OOOO =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"强制提交时间")#line:2537
        O000O0000O00OO00O .Add (O0OO000OOOO00OOOO ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2538
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2539
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2540
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2541
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2542
        O000O0000O00OO00O .Add (OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2543
        OOO0O0O0OOOO00OO0 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2544
        O000O0000O00OO00O .Add (OOO0O0O0OOOO00OO0 ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2545
        OO0O0OO0O00000OO0 .oneshotSizer .Add (O000O0000O00OO00O ,0 ,flag =wx .ALL ,border =5 )#line:2547
        O00OO00O00O0O00O0 =wx .StaticBox (OOO0O0O0OOOOO0O00 ,-1 ,u'双枪策略:')#line:2551
        OO0O0OO0O00000OO0 .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (O00OO00O00O0O00O0 ,wx .VERTICAL )#line:2552
        O0O0000OOOO0000OO =wx .GridBagSizer (4 ,4 )#line:2553
        OO0O0OO0O00000OO0 .jiajia_time2 =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2554
        OO0O0OO0O00000OO0 .jiajia_time2 .SetRange (40 ,55 )#line:2555
        OO0O0OO0O00000OO0 .jiajia_time2 .SetValue (48 )#line:2556
        OO0O0OO0O00000OO0 .jiajia_time2 .SetIncrement (0.1 )#line:2557
        O0O0000OOOO0000OO .Add (OO0O0OO0O00000OO0 .jiajia_time2 ,pos =(0 ,0 ))#line:2558
        OOOOO00OO00O00OO0 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2559
        O0O0000OOOO0000OO .Add (OOOOO00OO00O00OO0 ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2560
        OOOOOO00OOO0OOOO0 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2561
        O0O0000OOOO0000OO .Add (OOOOOO00OOO0OOOO0 ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2562
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2563
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2564
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2565
        OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2566
        O0O0000OOOO0000OO .Add (OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2567
        OO0OO0O0OO00O0O00 =[u"提前100",u"提前200",u"踩点"]#line:2569
        OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O02 =wx .Choice (OOO0O0O0OOOOO0O00 ,-1 ,choices =OO0OO0O0OO00O0O00 ,size =(68 ,25 ))#line:2570
        OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2571
        O0O0000OOOO0000OO .Add (OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2572
        O0O0O0O00O00O0OO0 =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"出价提交延迟")#line:2573
        O0O0000OOOO0000OO .Add (O0O0O0O00O00O0OO0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2574
        OO0O0OO0O00000OO0 .yanchi_time2 =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2575
        OO0O0OO0O00000OO0 .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2576
        OO0O0OO0O00000OO0 .yanchi_time2 .SetValue (0.5 )#line:2577
        OO0O0OO0O00000OO0 .yanchi_time2 .SetIncrement (0.1 )#line:2578
        O0O0000OOOO0000OO .Add (OO0O0OO0O00000OO0 .yanchi_time2 ,pos =(1 ,3 ))#line:2579
        OOO0OO0000O000O0O =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2580
        O0O0000OOOO0000OO .Add (OOO0OO0000O000O0O ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2581
        OO00000000OOOO00O =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"强制提交时间")#line:2584
        O0O0000OOOO0000OO .Add (OO00000000OOOO00O ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2585
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (OOO0O0O0OOOOO0O00 ,-1 ,"",size =(68 ,25 ))#line:2586
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2587
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2588
        OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2589
        O0O0000OOOO0000OO .Add (OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2590
        O0O00O0OOOOOO0O0O =wx .StaticText (OOO0O0O0OOOOO0O00 ,label =u"秒")#line:2591
        O0O0000OOOO0000OO .Add (O0O00O0OOOOOO0O0O ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2592
        OO0O0OO0O00000OO0 .ooo0O0o0oO0OshotSizer .Add (O0O0000OOOO0000OO ,0 ,flag =wx .ALL ,border =5 )#line:2594
        OO0O0OO0O00000OO0 .stractagySizer .Add (O00O000OOO00OOOOO ,0 ,wx .ALL |wx .CENTER ,5 )#line:2595
        OO0O0OO0O00000OO0 .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2596
        O00000000O0OOOOOO =wx .StaticText (OOO0O0O0OOOOO0O00 ,-1 ,label =u"拍牌功能设置")#line:2599
        OOO0OOO0OO0OO0OO0 =wx .StaticText (OOO0O0O0OOOOO0O00 ,-1 ,label =u"10点半需要进行第一次出价")#line:2600
        OOO0OOO0OO0OO0OO0 .SetForegroundColour ('red')#line:2601
        OO000000OOO0O0O0O =wx .StaticLine (OOO0O0O0OOOOO0O00 ,-1 )#line:2602
        OO0O0OO0O00000OO0 .vbox1 .Add (O00000000O0OOOOOO ,0 ,wx .ALL |wx .LEFT ,10 )#line:2603
        OO0O0OO0O00000OO0 .vbox1 .Add (OOO0OOO0OO0OO0OO0 ,0 ,wx .LEFT ,10 )#line:2604
        OO0O0OO0O00000OO0 .vbox1 .Add (OO000000OOO0O0O0O ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2605
        OO0O0OO0O00000OO0 .vbox1 .Add (OO0O0OO0O00000OO0 .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2606
        OO0O0OO0O00000OO0 .vbox1 .Add (OO0O0OO0O00000OO0 .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2607
        OO0O0OO0O00000OO0 .vbox1 .Add (OO0O0OO0O00000OO0 .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2608
        OOO0O0O0OOOOO0O00 .SetSizer (OO0O0OO0O00000OO0 .vbox1 )#line:2609
        OO0O0OO0O00000OO0 .ooo0O0o0oO0Osizer_Shown =False #line:2612
        OO0O0OO0O00000OO0 .oneshotsizer_Shown =True #line:2613
        OO0O0OO0O00000OO0 .vbox1 .Hide (OO0O0OO0O00000OO0 .ooo0O0o0oO0OshotSizer )#line:2614
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CHECKBOX ,OO0O0OO0O00000OO0 .Timeview ,OO0O0OO0O00000OO0 .timeview )#line:2623
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CHOICE ,OO0O0OO0O00000OO0 .Confirmchoice ,OO0O0OO0O00000OO0 .sdfsf24324297_choice )#line:2624
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Strategy_save ,OO0O0OO0O00000OO0 .ghjo0o0o0o0_save )#line:2625
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Strategy_load ,OO0O0OO0O00000OO0 .ghjo0o0o0o0_load )#line:2626
        OO0O0OO0O00000OO0 .Bind (wx .EVT_BUTTON ,OO0O0OO0O00000OO0 .Save_info ,OO0O0OO0O00000OO0 .save_info )#line:2627
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CHOICE ,OO0O0OO0O00000OO0 .Refresh_panel ,OO0O0OO0O00000OO0 .select_stractagy )#line:2629
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Jiajia_time ,OO0O0OO0O00000OO0 .jiajia_time )#line:2631
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Jiajia_zxco0o0o0o0 ,OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o0 )#line:2633
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CHOICE ,OO0O0OO0O00000OO0 .Select_oOO0O0O0O0O0O0 ,OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O0 )#line:2634
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Yanchi_time ,OO0O0OO0O00000OO0 .yanchi_time )#line:2636
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Tijiao_time ,OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time )#line:2638
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Jiajia_time2 ,OO0O0OO0O00000OO0 .jiajia_time2 )#line:2641
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Jiajia_zxco0o0o0o02 ,OO0O0OO0O00000OO0 .jiajia_zxco0o0o0o02 )#line:2643
        OO0O0OO0O00000OO0 .Bind (wx .EVT_CHOICE ,OO0O0OO0O00000OO0 .Select_oOO0O0O0O0O0O02 ,OO0O0OO0O00000OO0 .select_oOO0O0O0O0O0O02 )#line:2644
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Yanchi_time2 ,OO0O0OO0O00000OO0 .yanchi_time2 )#line:2646
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TEXT ,OO0O0OO0O00000OO0 .Tijiao_time2 ,OO0O0OO0O00000OO0 .oOO0O0O0O0O0O0_time2 )#line:2648
        OO0O0OO0O00000OO0 .timeframe1 =TimeFrame ()#line:2650
        OO0O0OO0O00000OO0 .timeframe1 .Show (False )#line:2651
        OO0O0OO0O00000OO0 .timeframe2 =MoniTimeFrame ()#line:2653
        OO0O0OO0O00000OO0 .timeframe2 .Show (False )#line:2654
        OO0O0OO0O00000OO0 .operationtimer =wx .Timer (OO0O0OO0O00000OO0 )#line:2657
        OO0O0OO0O00000OO0 .Bind (wx .EVT_TIMER ,OO0O0OO0O00000OO0 .opt ,OO0O0OO0O00000OO0 .operationtimer )#line:2658
        OO0O0OO0O00000OO0 .operationtimer .Start (1000 )#line:2659
    def OnClose (O0O00OO0O0OO00000 ,OOO0000OOO0O0O0OO ):#line:2661
        O0O00OO0O0OO00000 .Show (False )#line:2662
    def Price_view (OO0OOO00OO000O000 ,OOO00OOOOO0O000OO ):#line:2664
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:2665
        if zxco0o0o0o0_view and zxco0o0o0o0_count >=4 :#line:2667
            try :#line:2668
                OO0OOO00OO000O000 .Price_close ()#line:2669
            except :#line:2670
                pass #line:2671
            OO0OOO00OO000O000 .Screen_shot ()#line:2672
            O000OO0OO000O0OOO ="sc_new.png"#line:2673
            OO0OOO00OO000O000 .zxco0o0o0o0frame =PriceFrame (O000OO0OO000O0OOO )#line:2674
            OO0OOO00OO000O000 .zxco0o0o0o0frame .Show (True )#line:2675
            zxco0o0o0o0_view =False #line:2676
            zxco0o0o0o0_on =True #line:2677
    def Price_count (O0O0000OOOOO0O000 ,OOOOOO0OO0O000O00 ):#line:2680
        global zxco0o0o0o0_count #line:2682
        zxco0o0o0o0_count +=1 #line:2683
        O0OOOO0O00OOOO00O ='sc_new.png'#line:2684
        if web_on and ghjo0o0o0o0_on :#line:2685
            O0O0000OOOOO0O000 .O0O0O0O0O0O0Oframe .Show (False )#line:2686
        if not os .path .exists (O0OOOO0O00OOOO00O ):#line:2687
            try :#line:2688
                O0O0000OOOOO0O000 .Price_close ()#line:2689
            except :#line:2690
                pass #line:2691
        if not ghjo0o0o0o0_on or not web_on :#line:2693
            O0O0000OOOOO0O000 .O0O0O0O0O0O0Oframe .Show (False )#line:2694
    def Screen_shot (O000OO00000OO00OO ):#line:2699
        global Pricesize #line:2700
        OOO00OOO000000000 =Pos_zxco0o0o0o0 #line:2701
        O0OO000000OO0OOO0 =ImageGrab .grab (OOO00OOO000000000 )#line:2702
        O0OO000000OO0OOO0 .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:2703
    @staticmethod #line:2706
    def Del_shot ():#line:2707
        try :#line:2708
            os .remove ("sc_new.png")#line:2709
        except :#line:2710
            pass #line:2711
    def Price_close (OOOO0O00OO0O000O0 ):#line:2714
        try :#line:2715
            OOOO0O00OO0O000O0 .zxco0o0o0o0frame .Destroy ()#line:2716
        except :#line:2717
            pass #line:2718
    def opt (OOOO0OOO0000OO000 ,OOO00O00OO0OO0O00 ):#line:2722
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2723
        global ghjo0o0o0o0_on #line:2724
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2725
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on and not twice :#line:2726
            print ("触发还原")#line:2727
            ghjo0o0o0o0_on =True #line:2728
            twice =True #line:2729
            oo0o0O0O0O0_on =True #line:2730
            oOO0O0O0O0O0O0_on =False #line:2731
            oOO0O0O0O0O0O0_num =1 #line:2732
            oOO0O0O0O0O0O0_OK =False #line:2733
            oOO0O0O0O0O0O0_one =False #line:2734
        elif o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on and twice :#line:2735
            ghjo0o0o0o0_on =True #line:2736
            twice =True #line:2737
            oo0o0O0O0O0_on =True #line:2738
            oOO0O0O0O0O0O0_on =False #line:2739
            oOO0O0O0O0O0O0_num =1 #line:2740
            oOO0O0O0O0O0O0_OK =False #line:2741
            oOO0O0O0O0O0O0_one =False #line:2742
    def Add_time (OOOO0000O000OO00O ,O00O0OO000OO0O000 ):#line:2745
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2746
        if o0sdofsfo0sodf0so0_on :#line:2747
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2748
        else :#line:2749
            a_time +=0.1 #line:2750
    def Minus_time (O00O0O000OOO0O000 ,OOO00OOOOOO00O0OO ):#line:2752
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2753
        if o0sdofsfo0sodf0so0_on :#line:2754
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2755
        else :#line:2756
            a_time -=0.1 #line:2757
    def Add_ooo0O0o0oO0O (O0O0O0O00OOOOOOO0 ,OOOOO0O00O0O0O00O ):#line:2759
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2760
        if o0sdofsfo0sodf0so0_on :#line:2761
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2762
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2763
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2764
        else :#line:2765
            a_time +=1 #line:2766
    def Minus_ooo0O0o0oO0O (O0OO0O00OO00OO0O0 ,OO0O0000O0000OO00 ):#line:2768
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2769
        if o0sdofsfo0sodf0so0_on :#line:2770
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2771
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2772
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2773
        else :#line:2774
            a_time -=1 #line:2775
    def Timeview (OOOO0O00OOO0O00O0 ,O0OOO00OO0OOO00OO ):#line:2777
        O00O0OO0O00OOO00O =O0OOO00OO0OOO00OO .GetEventObject ()#line:2778
        global view_time ,time_on #line:2779
        if O00O0OO0O00OOO00O .IsChecked ():#line:2780
            view_time =True #line:2781
            time_on =True #line:2782
            if ooweo0o0werwr_on :#line:2783
                OOOO0O00OOO0O00O0 .timeframe1 .Show (True )#line:2784
            elif o0sdofsfo0sodf0so0_on :#line:2785
                OOOO0O00OOO0O00O0 .timeframe2 .Show (True )#line:2786
        else :#line:2787
            view_time =False #line:2788
            time_on =False #line:2789
            if ooweo0o0werwr_on :#line:2790
                OOOO0O00OOO0O00O0 .timeframe1 .Show (False )#line:2791
            elif o0sdofsfo0sodf0so0_on :#line:2792
                OOOO0O00OOO0O00O0 .timeframe2 .Show (False )#line:2793
    def Opentime (O0OOOOO00OOO0O0OO ):#line:2795
        if o0sdofsfo0sodf0so0_on :#line:2796
            try :#line:2797
                O0OOOOO00OOO0O0OO .timeframe2 .Show (True )#line:2798
            except :#line:2799
                pass #line:2800
        elif ooweo0o0werwr_on :#line:2801
            try :#line:2802
                O0OOOOO00OOO0O0OO .timeframe1 .Show (True )#line:2803
            except :#line:2804
                pass #line:2805
    def Closetime (O0OOO0O00O000OOO0 ):#line:2808
        try :#line:2809
            O0OOO0O00O000OOO0 .timeframe1 .Show (False )#line:2810
        except :#line:2811
            pass #line:2812
        try :#line:2813
            O0OOO0O00O000OOO0 .timeframe2 .Show (False )#line:2814
        except :#line:2815
            pass #line:2816
    def Confirmchoice (O00OOO0OOOOOOO0OO ,OO0OOO0OO0OOO00OO ):#line:2818
        global e_on ,enter_on #line:2819
        O0000000O000O0O0O =O00OOO0OOOOOOO0OO .sdfsf24324297_choice .GetSelection ()#line:2820
        if O0000000O000O0O0O ==0 :#line:2821
            e_on =True #line:2822
            enter_on =False #line:2823
        elif O0000000O000O0O0O ==1 :#line:2824
            e_on =False #line:2825
            enter_on =True #line:2826
    def Jiajia_time (O0000OOOO0O0OOOOO ,O00OOO0000OO0OO0O ):#line:2830
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2831
        OOOO00O0O00OO00OO =O0000OOOO0O0OOOOO .jiajia_time .GetValue ()#line:2832
        OOO00O0OO0000O0OO =[40 +OO0OOOO0OO0OO00O0 *0.1 for OO0OOOO0OO0OO00O0 in range (151 )]#line:2833
        if OOOO00O0O00OO00OO in OOO00O0OO0000O0OO :#line:2834
            OO00000o01 =OOOO00O0O00OO00OO #line:2835
            OO00000o01 =float (OO00000o01 )#line:2836
            one_oO0O0O0O0O0O0O0O01 =O0000OOOO0O0OOOOO .gettime (OO00000o01 )#line:2837
        else :#line:2838
            O0000OOOO0O0OOOOO .jiajia_time .SetValue (OO00000o01 )#line:2839
    def Jiajia_zxco0o0o0o0 (O0OO000O00O00O0O0 ,OOOOOO0O00OO0O0O0 ):#line:2842
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2843
        OOOO000OO0O0O00OO =[300 +OO000O0O00O0O0O0O *100 for OO000O0O00O0O0O0O in range (13 )]#line:2844
        OOO0O00O0O0OO0OO0 =O0OO000O00O00O0O0 .jiajia_zxco0o0o0o0 .GetValue ()#line:2845
        if OOO0O00O0O0OO0OO0 in OOOO000OO0O0O00OO :#line:2846
            one_diff =int (OOO0O00O0O0OO0OO0 )#line:2847
        else :#line:2848
            O0OO000O00O00O0O0 .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2849
    def Select_oOO0O0O0O0O0O0 (O00000O00OO00O00O ,OO0OOO00OOO000000 ):#line:2852
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2853
        OO00OO00O000O0O00 =O00000O00OO00O00O .select_oOO0O0O0O0O0O0 .GetString (O00000O00OO00O00O .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2854
        if OO00OO00O000O0O00 ==u"提前100":#line:2855
            one_advance =100 #line:2856
        elif OO00OO00O000O0O00 ==u"提前200":#line:2857
            one_advance =200 #line:2858
        else :#line:2859
            one_advance =0 #line:2860
    def Yanchi_time (OOOOO00O000OO00O0 ,OO00O00O0O0000OOO ):#line:2862
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2863
        OOOOO0O00O00OO000 =['0.%d'%O0O000000OOO00O0O for O0O000000OOO00O0O in range (11 )]#line:2864
        OOOOO0O00O00OO000 .append ('1.0')#line:2865
        OOOO0O00O0000O00O =str (OOOOO00O000OO00O0 .yanchi_time .GetValue ())#line:2866
        if OOOO0O00O0000O00O in OOOOO0O00O00OO000 :#line:2867
            one_delay =float (OOOO0O00O0000O00O )#line:2868
        else :#line:2869
            OOOOO00O000OO00O0 .yanchi_time .SetValue (one_delay )#line:2870
    def Tijiao_time (O00OO000000000000 ,O0OO0OO0O000O000O ):#line:2872
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2873
        O00O00OO00OO0OO0O =O00OO000000000000 .oOO0O0O0O0O0O0_time .GetValue ()#line:2874
        O0O0O00000O0OO000 =[40 +OOOO00000O0000OOO *0.1 for OOOO00000O0000OOO in range (171 )]#line:2875
        if O00O00OO00OO0OO0O in O0O0O00000O0OO000 :#line:2876
            OO00000o02 =float (O00O00OO00OO0OO0O )#line:2877
            one_oO0O0O0O0O0O0O0O02 =O00OO000000000000 .gettime (OO00000o02 )#line:2878
        else :#line:2879
            O00OO000000000000 .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2880
    def Jiajia_time2 (OOO0O0OOOOO00O000 ,O00OOO0O00OOOO0OO ):#line:2882
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2883
        OOOO000O000OOOOOO =OOO0O0OOOOO00O000 .jiajia_time2 .GetValue ()#line:2884
        O0OOO00OO00000000 =[40 +OOO0O0O00O000OO00 *0.1 for OOO0O0O00O000OO00 in range (151 )]#line:2885
        if OOOO000O000OOOOOO in O0OOO00OO00000000 :#line:2886
            ooo0O0o0oO0O_time1 =float (OOOO000O000OOOOOO )#line:2887
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOO0O0OOOOO00O000 .gettime (ooo0O0o0oO0O_time1 )#line:2888
        else :#line:2889
            OOO0O0OOOOO00O000 .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2890
    def Jiajia_zxco0o0o0o02 (OO000O0O0OOOOOOO0 ,OO0OOOO0O0OOOOO00 ):#line:2892
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2893
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2894
        OOOOO00OOOO0000O0 =[300 +OOOO00OO000OO0OOO *100 for OOOO00OO000OO0OOO in range (13 )]#line:2895
        OO0O0OO0O0O0O00OO =OO000O0O0OOOOOOO0 .jiajia_zxco0o0o0o02 .GetValue ()#line:2896
        if OO0O0OO0O0O0O00OO in OOOOO00OOOO0000O0 :#line:2897
            ooo0O0o0oO0O_diff =int (OO0O0OO0O0O0O00OO )#line:2898
        else :#line:2899
            OO000O0O0OOOOOOO0 .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2900
    def Select_oOO0O0O0O0O0O02 (OOOO0OOOOO00OOOO0 ,OOOOO0O00OO000O0O ):#line:2902
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2903
        OO0O0000O0O000000 =OOOO0OOOOO00OOOO0 .select_oOO0O0O0O0O0O02 .GetString (OOOO0OOOOO00OOOO0 .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2904
        if OO0O0000O0O000000 ==u"提前100":#line:2905
            ooo0O0o0oO0O_advance =100 #line:2906
        elif OO0O0000O0O000000 ==u"提前200":#line:2907
            ooo0O0o0oO0O_advance =200 #line:2908
        else :#line:2909
            ooo0O0o0oO0O_advance =0 #line:2910
    def Yanchi_time2 (OO0O000O0OOOO0O0O ,O00O0000OO00OOO00 ):#line:2913
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2914
        O00OOOO0000OO0O00 =['0.%d'%O0O0O00OOOO00OO0O for O0O0O00OOOO00OO0O in range (11 )]#line:2915
        O00OOOO0000OO0O00 .append ('1.0')#line:2916
        OO0O00O0OOOOO000O =str (OO0O000O0OOOO0O0O .yanchi_time2 .GetValue ())#line:2917
        if OO0O00O0OOOOO000O in O00OOOO0000OO0O00 :#line:2918
            ooo0O0o0oO0O_delay =float (OO0O00O0OOOOO000O )#line:2919
        else :#line:2920
            OO0O000O0OOOO0O0O .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2921
    def Tijiao_time2 (O0O000O00OOOOO0OO ,OO0O0O0000O0OOO00 ):#line:2924
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2925
        OOOO0O0000OO0O00O =O0O000O00OOOOO0OO .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2926
        OO000OOO0O00000OO =[53 +O0O0OO000000O0O0O *0.1 for O0O0OO000000O0O0O in range (41 )]#line:2927
        if OOOO0O0000OO0O00O in OO000OOO0O00000OO :#line:2928
            ooo0O0o0oO0O_time2 =float (OOOO0O0000OO0O00O )#line:2929
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0O000O00OOOOO0OO .gettime (ooo0O0o0oO0O_time2 )#line:2930
        else :#line:2931
            O0O000O00OOOOO0OO .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2932
    def Refresh_panel (OO0O0O0O0O0OO0OOO ,O0000O0O000OO0OO0 ):#line:2936
        global ghjo0o0o0o0_on #line:2938
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2939
        OOOOO000O000O0OOO =OO0O0O0O0O0OO0OOO .select_stractagy .GetString (OO0O0O0O0O0OO0OOO .select_stractagy .GetSelection ())#line:2940
        if OOOOO000O000O0OOO ==u"单枪策略":#line:2941
            OO0O0O0O0O0OO0OOO .ss_Hide ()#line:2942
            twice =False #line:2943
            ghjo0o0o0o0_on =True #line:2944
            oo0o0O0O0O0_on =True #line:2945
            oOO0O0O0O0O0O0_on =False #line:2946
            oOO0O0O0O0O0O0_num =1 #line:2947
            oOO0O0O0O0O0O0_OK =False #line:2948
            oOO0O0O0O0O0O0_one =False #line:2949
        elif OOOOO000O000O0OOO ==u"双枪策略":#line:2951
            OO0O0O0O0O0OO0OOO .ss_Shown ()#line:2952
            ghjo0o0o0o0_on =True #line:2953
            twice =True #line:2954
            oo0o0O0O0O0_on =True #line:2955
            oOO0O0O0O0O0O0_on =False #line:2956
            oOO0O0O0O0O0O0_num =1 #line:2957
            oOO0O0O0O0O0O0_OK =False #line:2958
            oOO0O0O0O0O0O0_one =False #line:2959
        else :#line:2960
            OO0O0O0O0O0OO0OOO .none_show ()#line:2961
            ghjo0o0o0o0_on =False #line:2962
            twice =False #line:2963
    def ss_Shown (OOOOOO0000OO000O0 ):#line:2966
        if not OOOOOO0000OO000O0 .ooo0O0o0oO0Osizer_Shown :#line:2967
            OOOOOO0000OO000O0 .vbox1 .Show (OOOOOO0000OO000O0 .ooo0O0o0oO0OshotSizer )#line:2968
            OOOOOO0000OO000O0 .ooo0O0o0oO0Osizer_Shown =True #line:2969
        if not OOOOOO0000OO000O0 .oneshotsizer_Shown :#line:2970
            OOOOOO0000OO000O0 .vbox1 .Show (OOOOOO0000OO000O0 .oneshotSizer )#line:2971
            OOOOOO0000OO000O0 .oneshotsizer_Shown =True #line:2972
        OOOOOO0000OO000O0 .ooo0O0o0oO0Osizer_Shown =True #line:2973
        OOOOOO0000OO000O0 .oneshotSizer_Shown =True #line:2974
        OOOOOO0000OO000O0 .SetClientSize ((280 ,575 ))#line:2975
        OOOOOO0000OO000O0 .Secondshot_reset ()#line:2976
        OOOOOO0000OO000O0 .Layout ()#line:2977
    def ss_Hide (O00O0OO0O0OOO000O ):#line:2979
        if O00O0OO0O0OOO000O .ooo0O0o0oO0Osizer_Shown :#line:2980
            O00O0OO0O0OOO000O .vbox1 .Hide (O00O0OO0O0OOO000O .ooo0O0o0oO0OshotSizer )#line:2981
        if not O00O0OO0O0OOO000O .oneshotsizer_Shown :#line:2984
            O00O0OO0O0OOO000O .vbox1 .Show (O00O0OO0O0OOO000O .oneshotSizer )#line:2985
        O00O0OO0O0OOO000O .ooo0O0o0oO0Osizer_Shown =False #line:2986
        O00O0OO0O0OOO000O .oneshotSizer_Shown =True #line:2987
        O00O0OO0O0OOO000O .SetClientSize ((280 ,375 ))#line:2988
        O00O0OO0O0OOO000O .Oneshot_reset ()#line:2989
        O00O0OO0O0OOO000O .Layout ()#line:2990
    def none_show (OO0O0OO0O0O00OOO0 ):#line:2992
        if OO0O0OO0O0O00OOO0 .oneshotsizer_Shown :#line:2993
            OO0O0OO0O0O00OOO0 .vbox1 .Hide (OO0O0OO0O0O00OOO0 .ooo0O0o0oO0OshotSizer )#line:2994
        if OO0O0OO0O0O00OOO0 .ooo0O0o0oO0Osizer_Shown :#line:2995
            OO0O0OO0O0O00OOO0 .vbox1 .Hide (OO0O0OO0O0O00OOO0 .oneshotSizer )#line:2996
        OO0O0OO0O0O00OOO0 .oneshotsizer_Shown =False #line:2998
        OO0O0OO0O0O00OOO0 .ooo0O0o0oO0Osizer_Shown =False #line:2999
        OO0O0OO0O0O00OOO0 .SetClientSize ((280 ,255 ))#line:3000
        OO0O0OO0O0O00OOO0 .Layout ()#line:3001
    def Oneshot_reset (OOO00OOO000OO0000 ):#line:3003
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:3004
        OOO00OOO000OO0000 .jiajia_time .SetValue (48.0 )#line:3005
        OOO00OOO000OO0000 .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:3006
        OOO00OOO000OO0000 .jiajia_zxco0o0o0o0 .SetValue (700 )#line:3007
        OOO00OOO000OO0000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3008
        OOO00OOO000OO0000 .yanchi_time .SetValue (0.5 )#line:3009
        OO00000o01 =48 #line:3011
        OO00000o02 =55 #line:3012
        one_diff =700 #line:3013
        one_delay =0.5 #line:3014
        one_advance =100 #line:3015
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3017
        one_oO0O0O0O0O0O0O0O01 =OOO00OOO000OO0000 .gettime (OO00000o01 )#line:3018
        one_oO0O0O0O0O0O0O0O02 =OOO00OOO000OO0000 .gettime (OO00000o02 )#line:3019
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OOO00OOO000OO0000 .gettime (ooo0O0o0oO0O_time1 )#line:3020
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOO00OOO000OO0000 .gettime (ooo0O0o0oO0O_time2 )#line:3021
    def Secondshot_reset (O000O0000O0O0O000 ):#line:3024
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:3025
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:3026
        O000O0000O0O0O000 .jiajia_time .SetValue (40.0 )#line:3027
        O000O0000O0O0O000 .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:3028
        O000O0000O0O0O000 .jiajia_zxco0o0o0o0 .SetValue (500 )#line:3029
        O000O0000O0O0O000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3030
        O000O0000O0O0O000 .yanchi_time .SetValue (0.0 )#line:3031
        O000O0000O0O0O000 .jiajia_time2 .SetValue (50.0 )#line:3033
        O000O0000O0O0O000 .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:3034
        O000O0000O0O0O000 .jiajia_zxco0o0o0o02 .SetValue (700 )#line:3035
        O000O0000O0O0O000 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:3036
        O000O0000O0O0O000 .yanchi_time2 .SetValue (0.5 )#line:3037
        OO00000o01 =40 #line:3039
        OO00000o02 =48 #line:3040
        one_diff =500 #line:3041
        one_delay =0.5 #line:3042
        one_advance =100 #line:3043
        ooo0O0o0oO0O_time1 =50 #line:3045
        ooo0O0o0oO0O_time2 =55.5 #line:3046
        ooo0O0o0oO0O_diff =700 #line:3047
        ooo0O0o0oO0O_delay =0.5 #line:3048
        ooo0O0o0oO0O_advance =100 #line:3049
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3051
        one_oO0O0O0O0O0O0O0O01 =O000O0000O0O0O000 .gettime (OO00000o01 )#line:3052
        one_oO0O0O0O0O0O0O0O02 =O000O0000O0O0O000 .gettime (OO00000o02 )#line:3053
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O000O0000O0O0O000 .gettime (ooo0O0o0oO0O_time1 )#line:3054
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O000O0000O0O0O000 .gettime (ooo0O0o0oO0O_time2 )#line:3055
    def Strategy_save (O0O0000OOO00OOO00 ,OO00000O00OO000OO ):#line:3058
        OO0O0OOO0OOO0OOO0 =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:3060
        if OO0O0OOO0OOO0OOO0 .ShowModal ()==wx .ID_OK :#line:3061
            O00O0O0OO0OO00O0O =OO0O0OOO0OOO0OOO0 .GetValue ()#line:3062
            if O00O0O0OO0OO00O0O :#line:3063
                OO0000O0OO0000O0O =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:3064
                if OO0000O0OO0000O0O ==wx .ID_OK :#line:3065
                    OO0000O0OO0000O0O .Destroy ()#line:3066
                    OO0O0OOO0OOO0OOO0 .Destroy ()#line:3067
                O0O0000OOO00OOO00 .save (O00O0O0OO0OO00O0O )#line:3068
            else :#line:3069
                OO0000O0OO0000O0O =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:3070
                if OO0000O0OO0000O0O ==wx .ID_OK :#line:3071
                    OO0000O0OO0000O0O .Destroy ()#line:3072
                    OO0O0OOO0OOO0OOO0 .Destroy ()#line:3073
    def save (O000O00OO00OO0OO0 ,OOO0O00O0OO0O0O00 ):#line:3075
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:3076
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:3077
        global osl ,e_on ,enter_on #line:3078
        if O000O00OO00OO0OO0 .select_stractagy .GetSelection ()==2 :#line:3080
            OOO00OO000000O0O0 =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:3081
            if OOO00OO000000O0O0 ==wx .ID_OK :#line:3082
                OOO00OO000000O0O0 .Destroy ()#line:3083
        elif O000O00OO00OO0OO0 .select_stractagy .GetSelection ()==0 :#line:3084
            osl [0 ]=0 #line:3085
            osl [1 ]=OO00000o01 #line:3086
            osl [2 ]=OO00000o02 #line:3087
            osl [3 ]=one_diff #line:3088
            osl [4 ]=one_delay #line:3089
            osl [5 ]=one_advance #line:3090
            osl [6 ]=ooo0O0o0oO0O_time1 #line:3091
            osl [7 ]=ooo0O0o0oO0O_time2 #line:3092
            osl [8 ]=ooo0O0o0oO0O_diff #line:3093
            osl [9 ]=ooo0O0o0oO0O_delay #line:3094
            osl [10 ]=ooo0O0o0oO0O_advance #line:3095
            osl [11 ]=e_on #line:3096
            osl [12 ]=enter_on #line:3097
        elif O000O00OO00OO0OO0 .select_stractagy .GetSelection ()==1 :#line:3098
            osl [0 ]=1 #line:3099
            osl [0 ]=1 #line:3100
            osl [1 ]=OO00000o01 #line:3101
            osl [2 ]=OO00000o02 #line:3102
            osl [3 ]=one_diff #line:3103
            osl [4 ]=one_delay #line:3104
            osl [5 ]=one_advance #line:3105
            osl [6 ]=ooo0O0o0oO0O_time1 #line:3106
            osl [7 ]=ooo0O0o0oO0O_time2 #line:3107
            osl [8 ]=ooo0O0o0oO0O_diff #line:3108
            osl [9 ]=ooo0O0o0oO0O_delay #line:3109
            osl [10 ]=ooo0O0o0oO0O_advance #line:3110
            osl [11 ]=e_on #line:3111
            osl [12 ]=enter_on #line:3112
        with open ('%s.ghjo0o0o0o0'%OOO0O00O0OO0O0O00 ,'wb')as O0O0OOO00OO0OOO00 :#line:3113
            pickle .dump (osl ,O0O0OOO00OO0OOO00 )#line:3114
    def Strategy_load (OOOO00O000OOO0OO0 ,O0O00OOOO00000OOO ):#line:3129
        import os as O00O0O0O0O0OOO00O #line:3130
        OOOO0O0OOOO0O00O0 =O00O0O0O0O0OOO00O .getcwd ()#line:3131
        O00000O00OO00OO00 =OOOO00O000OOO0OO0 .findfiles (OOOO0O0OOOO0O00O0 )#line:3132
        if O00000O00OO00OO00 :#line:3133
            OOO0O0O0O0O0OOOOO =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =O00000O00OO00OO00 )#line:3135
            if OOO0O0O0O0O0OOOOO .ShowModal ()==wx .ID_OK :#line:3136
                OOOO0O0OOOO0O00O0 =OOO0O0O0O0O0OOOOO .GetStringSelection ()#line:3137
                O00O0OOOO00OO0O0O =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:3138
                if O00O0OOOO00OO0O0O .ShowModal ()==wx .ID_OK :#line:3139
                    O00O0OOOO00OO0O0O .Destroy ()#line:3140
                OOOO00O000OOO0OO0 .load (OOOO0O0OOOO0O00O0 )#line:3141
            OOO0O0O0O0O0OOOOO .Destroy ()#line:3143
        else :#line:3144
            O00O0OOOO00OO0O0O =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:3145
            if O00O0OOOO00OO0O0O ==wx .ID_OK :#line:3146
                O00O0OOOO00OO0O0O .Destroy ()#line:3147
    def load (O0OOOOOO000000OO0 ,O0000000OO0O0OOOO ):#line:3149
        global osl ,e_on ,enter_on #line:3150
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:3151
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:3152
        global ghjo0o0o0o0_on #line:3154
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:3155
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3156
        try :#line:3157
            with open (O0000000OO0O0OOOO ,'rb')as O00OO00OOO00O0O0O :#line:3158
                osl =pickle .load (O00OO00OOO00O0O0O )#line:3159
        except :#line:3160
            pass #line:3161
        if osl [0 ]==0 :#line:3162
            O0OOOOOO000000OO0 .ss_Hide ()#line:3163
            twice =False #line:3166
            ghjo0o0o0o0_on =True #line:3167
            oo0o0O0O0O0_on =True #line:3168
            oOO0O0O0O0O0O0_on =False #line:3169
            oOO0O0O0O0O0O0_num =1 #line:3170
            oOO0O0O0O0O0O0_OK =False #line:3171
            oOO0O0O0O0O0O0_one =False #line:3172
            O0OOOOOO000000OO0 .select_stractagy .SetSelection (0 )#line:3174
            O0OOOOOO000000OO0 .jiajia_time .SetValue (osl [1 ])#line:3175
            O0OOOOOO000000OO0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3176
            O0OOOOOO000000OO0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3177
            O0OOOOOO000000OO0 .yanchi_time .SetValue (osl [4 ])#line:3178
            if osl [5 ]==100 :#line:3179
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3180
            elif osl [5 ]==200 :#line:3181
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3182
            else :#line:3183
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3184
            OO00000o01 =osl [1 ]#line:3186
            OO00000o02 =osl [2 ]#line:3187
            one_diff =osl [3 ]#line:3188
            one_delay =osl [4 ]#line:3189
            one_advance =osl [5 ]#line:3190
            e_on =osl [11 ]#line:3192
            enter_on =osl [12 ]#line:3193
            if e_on :#line:3194
                O0OOOOOO000000OO0 .sdfsf24324297_choice .SetSelection (0 )#line:3195
            elif enter_on :#line:3196
                O0OOOOOO000000OO0 .sdfsf24324297_choice .SetSelection (1 )#line:3197
            one_oO0O0O0O0O0O0O0O01 =O0OOOOOO000000OO0 .gettime (OO00000o01 )#line:3199
            one_oO0O0O0O0O0O0O0O02 =O0OOOOOO000000OO0 .gettime (OO00000o02 )#line:3200
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0OOOOOO000000OO0 .gettime (ooo0O0o0oO0O_time1 )#line:3201
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0OOOOOO000000OO0 .gettime (ooo0O0o0oO0O_time2 )#line:3202
        elif osl [0 ]==1 :#line:3204
            ghjo0o0o0o0_on =True #line:3205
            twice =True #line:3206
            oo0o0O0O0O0_on =True #line:3207
            oOO0O0O0O0O0O0_on =False #line:3208
            oOO0O0O0O0O0O0_num =1 #line:3209
            oOO0O0O0O0O0O0_OK =False #line:3210
            oOO0O0O0O0O0O0_one =False #line:3211
            O0OOOOOO000000OO0 .ss_Shown ()#line:3212
            O0OOOOOO000000OO0 .select_stractagy .SetSelection (1 )#line:3213
            O0OOOOOO000000OO0 .jiajia_time .SetValue (osl [1 ])#line:3214
            O0OOOOOO000000OO0 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3215
            O0OOOOOO000000OO0 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3216
            O0OOOOOO000000OO0 .yanchi_time .SetValue (osl [4 ])#line:3217
            if osl [5 ]==100 :#line:3218
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3219
            elif osl [5 ]==200 :#line:3220
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3221
            else :#line:3222
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3223
            O0OOOOOO000000OO0 .jiajia_time2 .SetValue (osl [6 ])#line:3224
            O0OOOOOO000000OO0 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:3225
            O0OOOOOO000000OO0 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:3226
            O0OOOOOO000000OO0 .yanchi_time2 .SetValue (osl [9 ])#line:3227
            if osl [10 ]==100 :#line:3228
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:3229
            elif osl [10 ]==200 :#line:3230
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:3231
            else :#line:3232
                O0OOOOOO000000OO0 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:3233
            OO00000o01 =osl [1 ]#line:3236
            OO00000o02 =osl [2 ]#line:3237
            one_diff =osl [3 ]#line:3238
            one_delay =osl [4 ]#line:3239
            one_advance =osl [5 ]#line:3240
            ooo0O0o0oO0O_time1 =osl [6 ]#line:3242
            ooo0O0o0oO0O_time2 =osl [7 ]#line:3243
            ooo0O0o0oO0O_diff =osl [8 ]#line:3244
            ooo0O0o0oO0O_delay =osl [9 ]#line:3245
            ooo0O0o0oO0O_advance =osl [10 ]#line:3246
            e_on =osl [11 ]#line:3248
            enter_on =osl [12 ]#line:3249
            if e_on :#line:3250
                O0OOOOOO000000OO0 .sdfsf24324297_choice .SetSelection (0 )#line:3251
            elif enter_on :#line:3252
                O0OOOOOO000000OO0 .sdfsf24324297_choice .SetSelection (1 )#line:3253
            one_oO0O0O0O0O0O0O0O01 =O0OOOOOO000000OO0 .gettime (OO00000o01 )#line:3255
            one_oO0O0O0O0O0O0O0O02 =O0OOOOOO000000OO0 .gettime (OO00000o02 )#line:3256
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O0OOOOOO000000OO0 .gettime (ooo0O0o0oO0O_time1 )#line:3257
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O0OOOOOO000000OO0 .gettime (ooo0O0o0oO0O_time2 )#line:3258
    def findfiles (O000OOO0O00O0O0O0 ,O0000O0O0O0OOO0O0 ):#line:3260
        O0O00OOOO0OOO0O00 =[]#line:3261
        for O00OO00OOO0O0O000 ,O000O0O0OO00O00OO ,OO00O0OO00000OOO0 in os .walk (O0000O0O0O0OOO0O0 ):#line:3262
            for OOOO00O0O0OOOO00O in OO00O0OO00000OOO0 :#line:3263
                if os .path .splitext (OOOO00O0O0OOOO00O )[1 ]=='.ghjo0o0o0o0':#line:3264
                    O0O00OOOO0OOO0O00 .append (os .path .join (O00OO00OOO0O0O000 ,OOOO00O0O0OOOO00O ))#line:3265
        return O0O00OOOO0OOO0O00 #line:3266
    def Save_info (OO00OO0O00OOOOOO0 ,O00OO000000000OO0 ):#line:3268
        pass #line:3269
    def changetime (O00000OO00000O0O0 ,OO000000000OO0OO0 ):#line:3274
        OO0OO000OO0000O0O =time .mktime (time .strptime (OO000000000OO0OO0 ,'%Y-%m-%d %H:%M:%S'))#line:3275
        return OO0OO000OO0000O0O #line:3276
    def get_nowtime (OOO00O00O0O00O0OO ):#line:3279
        O0000000OOOO0000O =time .time ()#line:3280
        O0O0OOO00O0OO0O0O =time .strftime ('%Y-%m-%d',time .localtime (O0000000OOOO0000O ))#line:3281
        return O0O0OOO00O0OO0O0O #line:3282
    def gettime (OO0OO00OOOOO0OO00 ,OOOOOO000OOO0O000 ):#line:3285
        OOOO00O0OOO00O0O0 =OO0OO00OOOOO0OO00 .get_nowtime ()#line:3286
        O0OO0O00O00O00O0O =OOOO00O0OOO00O0O0 +' 11:29:'+str (int (OOOOOO000OOO0O000 ))#line:3287
        OO000OOOOO0OOO000 =OO0OO00OOOOO0OO00 .changetime (O0OO0O00O00O00O0O )+float (OOOOOO000OOO0O000 )-int (OOOOOO000OOO0O000 )#line:3288
        return OO000OOOOO0OOO000 #line:3289
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:3292
    def __init__ (O000OOO0OOO0O0OOO ,OOOOO000O0O0O0000 ):#line:3293
        wx .Window .__init__ (O000OOO0OOO0O0OOO ,OOOOO000O0O0O0000 ,size =Timesize )#line:3294
        O000OOO0OOO0O0OOO .Bind (wx .EVT_PAINT ,O000OOO0OOO0O0OOO .OnPaint )#line:3295
        O000OOO0OOO0O0OOO .timer =wx .Timer (O000OOO0OOO0O0OOO )#line:3296
        O000OOO0OOO0O0OOO .Bind (wx .EVT_TIMER ,O000OOO0OOO0O0OOO .OnTimer ,O000OOO0OOO0O0OOO .timer )#line:3297
        O000OOO0OOO0O0OOO .timer .Start (100 )#line:3298
    def Draw (OOOO0000000000O00 ,OOOOOOO0OOOO0000O ):#line:3300
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3301
        O0000OOOO000O000O =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3302
        OO00O00OOOO000O00 ,OOO00O0OOO000O000 =OOOO0000000000O00 .GetClientSize ()#line:3303
        OOOOOOO0OOOO0000O .SetBackground (wx .Brush (OOOO0000000000O00 .GetBackgroundColour ()))#line:3304
        OOOOOOO0OOOO0000O .Clear ()#line:3305
        OOOOOOO0OOOO0000O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3306
        OOO0O00O00000OO00 ,OO0OO00O00000O000 =OOOOOOO0OOOO0000O .GetTextExtent (O0000OOOO000O000O )#line:3307
        OOOOOOO0OOOO0000O .DrawText (O0000OOOO000O000O ,(OO00O00OOOO000O00 -OOO0O00O00000OO00 )/2 ,(OOO00O0OOO000O000 )/2 -OO0OO00O00000O000 /2 )#line:3308
    def Modify (OO0O0O0O0O0O0O00O ,OO000O0000OOOO0O0 ):#line:3310
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3311
        O0O0O0O00O0O00OO0 =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3312
        O0000O0OO0OOO0OOO ,O0O0OOO0O0OO0OOOO =OO0O0O0O0O0O0O00O .GetClientSize ()#line:3313
        OO000O0000OOOO0O0 .SetBackground (wx .Brush (OO0O0O0O0O0O0O00O .GetBackgroundColour ()))#line:3314
        OO000O0000OOOO0O0 .Clear ()#line:3315
        OO000O0000OOOO0O0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3316
        OOO000OOOOOOO000O ,O00OO0OO00OO00000 =OO000O0000OOOO0O0 .GetTextExtent (O0O0O0O00O0O00OO0 )#line:3317
        OO000O0000OOOO0O0 .DrawText (O0O0O0O00O0O00OO0 ,(O0000O0OO0OOO0OOO -OOO000OOOOOOO000O )/2 ,(O0O0OOO0O0OO0OOOO )/2 -O00OO0OO00OO00000 /2 )#line:3318
    def OnTimer (OOOO0000000O0OOO0 ,OO00O0OO000O00O0O ):#line:3320
        OOO0O00OO00O00OO0 =wx .BufferedDC (wx .ClientDC (OOOO0000000O0OOO0 ))#line:3321
        OOOO0000000O0OOO0 .Modify (OOO0O00OO00O00OO0 )#line:3322
    def OnPaint (O00OOOOO0O0O0O00O ,OO000O0O0O0O000OO ):#line:3324
        OOO0OOOO00O0OO000 =wx .BufferedPaintDC (O00OOOOO0O0O0O00O )#line:3325
        O00OOOOO0O0O0O00O .Draw (OOO0OOOO00O0OO000 )#line:3326
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:3328
    def __init__ (OO0OOOO0OO000O000 ):#line:3329
         wx .Frame .__init__ (OO0OOOO0OO000O000 ,None ,title ="wx.Timer",size =(200 ,50 ),pos =O0O0O0O0O0O0Ozxco0o0o0o0frame_pos ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:3331
         Lowestzxco0o0o0o0Window (OO0OOOO0OO000O000 )#line:3334
import string #line:3352
import wx .lib .agw .hyperlink as hyperlink #line:3353
class LoginFrame (wx .Frame ):#line:3354
    def __init__ (OO00OOOOO0000O0OO ,OO0O00OOOOO00O000 ,OOO0OO0OO0O00O000 ,O000OOO0OOOO0O000 ):#line:3355
        wx .Frame .__init__ (OO00OOOOO0000O0OO ,None ,-1 ,OO0O00OOOOO00O000 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3356
        OO00OOOOO0000O0OO .Bind (wx .EVT_CLOSE ,OO00OOOOO0000O0OO .OnClose )#line:3357
        OO00OOOOO0000O0OO .panel =wx .Panel (OO00OOOOO0000O0OO ,size =(300 ,220 ))#line:3358
        OO00OOOOO0000O0OO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3359
        OO00OOOOO0000O0OO .SetIcon (OO00OOOOO0000O0OO .icon )#line:3360
        OO00OOOOO0000O0OO .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3373
        OO00OOOOO0000O0OO .welcomelabel =wx .StaticText (OO00OOOOO0000O0OO .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3374
        OO00OOOOO0000O0OO .sizer_v1 .Add (OO00OOOOO0000O0OO .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3375
        OO00OOOOO0000O0OO .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3378
        OO00OOOOO0000O0OO .userlabel =wx .StaticText (OO00OOOOO0000O0OO .panel ,-1 ,label ="账号")#line:3379
        OO00OOOOO0000O0OO .userText =wx .TextCtrl (OO00OOOOO0000O0OO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3381
        OO00OOOOO0000O0OO .userbox .Add (OO00OOOOO0000O0OO .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3382
        OO00OOOOO0000O0OO .userbox .Add (OO00OOOOO0000O0OO .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3383
        OO00OOOOO0000O0OO .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3385
        OO00OOOOO0000O0OO .passlabel =wx .StaticText (OO00OOOOO0000O0OO .panel ,-1 ,label ="密码")#line:3386
        OO00OOOOO0000O0OO .passText =wx .TextCtrl (OO00OOOOO0000O0OO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3388
        OO00OOOOO0000O0OO .passbox .Add (OO00OOOOO0000O0OO .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3389
        OO00OOOOO0000O0OO .passbox .Add (OO00OOOOO0000O0OO .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3390
        if OOO0OO0OO0O00O000 :#line:3391
            OO00OOOOO0000O0OO .userText .SetValue (OOO0OO0OO0O00O000 )#line:3392
        if O000OOO0OOOO0O000 :#line:3393
            OO00OOOOO0000O0OO .passText .SetValue (O000OOO0OOOO0O000 )#line:3394
        OO00OOOOO0000O0OO .sizer_v1 .Add (OO00OOOOO0000O0OO .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3395
        OO00OOOOO0000O0OO .sizer_v1 .Add (OO00OOOOO0000O0OO .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3396
        OO00OOOOO0000O0OO .Bind (wx .EVT_TEXT_ENTER ,OO00OOOOO0000O0OO .OnLogin ,OO00OOOOO0000O0OO .userText )#line:3398
        OO00OOOOO0000O0OO .Bind (wx .EVT_TEXT_ENTER ,OO00OOOOO0000O0OO .OnLogin ,OO00OOOOO0000O0OO .passText )#line:3399
        OO00OOOOO0000O0OO .o0sdofsfo0sodf0so0btn =wx .Button (OO00OOOOO0000O0OO .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3401
        OO00OOOOO0000O0OO .loginbtn =wx .Button (OO00OOOOO0000O0OO .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3402
        OO00OOOOO0000O0OO .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3403
        OO00OOOOO0000O0OO .btnSizer .Add (OO00OOOOO0000O0OO .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3404
        OO00OOOOO0000O0OO .btnSizer .Add (OO00OOOOO0000O0OO .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3405
        OO00OOOOO0000O0OO .sizer_v1 .Add (OO00OOOOO0000O0OO .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3406
        OO00OOOOO0000O0OO .loginbtn .Bind (wx .EVT_BUTTON ,OO00OOOOO0000O0OO .OnLogin ,OO00OOOOO0000O0OO .loginbtn )#line:3407
        OO00OOOOO0000O0OO .purchaselink =hyperlink .HyperLinkCtrl (OO00OOOOO0000O0OO .panel ,-1 ,u"购买账号")#line:3409
        OO00OOOOO0000O0OO .purchaselink .UnsetToolTip ()#line:3410
        OO00OOOOO0000O0OO .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OO00OOOOO0000O0OO .Purchase )#line:3411
        OO00OOOOO0000O0OO .purchaselink .AutoBrowse (False )#line:3412
        OO00OOOOO0000O0OO .purchaselink .EnableRollover (True )#line:3413
        OO00OOOOO0000O0OO .purchaselink .SetUnderlines (False ,False ,True )#line:3414
        OO00OOOOO0000O0OO .purchaselink .OpenInSameWindow (True )#line:3415
        OO00OOOOO0000O0OO .purchaselink .UpdateLink ()#line:3416
        OO00OOOOO0000O0OO .helplink =hyperlink .HyperLinkCtrl (OO00OOOOO0000O0OO .panel ,-1 ,u"查看帮助")#line:3418
        OO00OOOOO0000O0OO .helplink .UnsetToolTip ()#line:3419
        OO00OOOOO0000O0OO .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OO00OOOOO0000O0OO .Purchase )#line:3420
        OO00OOOOO0000O0OO .helplink .AutoBrowse (False )#line:3421
        OO00OOOOO0000O0OO .helplink .EnableRollover (True )#line:3422
        OO00OOOOO0000O0OO .helplink .SetUnderlines (False ,False ,True )#line:3423
        OO00OOOOO0000O0OO .helplink .OpenInSameWindow (True )#line:3424
        OO00OOOOO0000O0OO .helplink .UpdateLink ()#line:3425
        OO00OOOOO0000O0OO .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3427
        OO00OOOOO0000O0OO .linkbox .Add (OO00OOOOO0000O0OO .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3428
        OO00OOOOO0000O0OO .linkbox .Add (OO00OOOOO0000O0OO .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3429
        OO00OOOOO0000O0OO .sizer_v1 .Add (OO00OOOOO0000O0OO .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3430
        OO00OOOOO0000O0OO .SetSizer (OO00OOOOO0000O0OO .sizer_v1 )#line:3432
        OO00OOOOO0000O0OO .Center ()#line:3433
        pub .subscribe (OO00OOOOO0000O0OO .connect_success ,"connect")#line:3435
        OO00OOOOO0000O0OO .hashthread =HashThread ()#line:3438
    def connect_success (OOO00O00OOOOO0O00 ):#line:3440
        OOO00O00OOOOO0O00 .loginbtn .Enable ()#line:3441
        global login_result #line:3442
        if login_result =='login success':#line:3443
            OOO00O00OOOOO0O00 .Destroy ()#line:3444
            OOO00O00OOOOO0O00 .topframe =TopFrame ('小鲜肉拍牌',version )#line:3445
            OOO00O00OOOOO0O00 .topframe .Show (True )#line:3446
        elif login_result =='net error':#line:3448
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3449
        elif login_result =='repeat':#line:3450
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3451
        elif login_result =='wrong account':#line:3452
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3453
        elif login_result =='wrong password':#line:3454
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3455
        else :#line:3456
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3457
    def OnEraseBack (OOOOOOO00O0OOOOO0 ,O0OOOO0OOO0O00OOO ):#line:3460
        OOO00O0OOOOOOO000 =O0OOOO0OOO0O00OOO .GetDC ()#line:3461
        if not OOO00O0OOOOOOO000 :#line:3462
            OOO00O0OOOOOOO000 =wx .ClientDC (OOOOOOO00O0OOOOO0 )#line:3463
            O0000OO0OO000O00O =OOOOOOO00O0OOOOO0 .GetUpdateRegion ().GetBox ()#line:3464
            OOO00O0OOOOOOO000 .SetClippingRect (O0000OO0OO000O00O )#line:3465
        OOO00O0OOOOOOO000 .Clear ()#line:3466
        OO0OOOO0OOO0O0O00 =wx .Bitmap ("blue.jpg")#line:3467
        OOO00O0OOOOOOO000 .DrawBitmap (OO0OOOO0OOO0O0O00 ,0 ,0 )#line:3468
    def OnClose (OO0O0OOOOO000O000 ,O0OOO000O0O0O00OO ):#line:3470
        O0OOO000O0O0O00OO .Skip ()#line:3471
        sys .exit (None )#line:3472
    def OnLogin (OOO00O000OOOOOOOO ,O0OO0000O0OOOOO00 ):#line:3480
        global Username ,Password #line:3481
        O0O00OO0OO0O0OOOO =OOO00O000OOOOOOOO .userText .GetValue ()#line:3482
        O00OOO0O0O0OO0000 =OOO00O000OOOOOOOO .passText .GetValue ()#line:3483
        if O0O00OO0OO0O0OOOO =="":#line:3484
            wx .MessageBox ('请输入用户名！')#line:3485
            OOO00O000OOOOOOOO .userText .SetFocus ()#line:3486
        elif O00OOO0O0O0OO0000 =="":#line:3487
            wx .MessageBox ('请输入密码！')#line:3488
            OOO00O000OOOOOOOO .passText .SetFocus ()#line:3489
        else :#line:3491
            Username =O0O00OO0OO0O0OOOO #line:3492
            Password =O00OOO0O0O0OO0000 #line:3493
            OOO00O000OOOOOOOO .loginthread =LoginThread ()#line:3494
            OO0000O0OOO0O00OO =[O0O00OO0OO0O0OOOO ,O00OOO0O0O0OO0000 ]#line:3495
            with open ('your.name','wb')as O0O0OO00O0OOO00O0 :#line:3496
                pickle .dump (OO0000O0OOO0O00OO ,O0O0OO00O0OOO00O0 )#line:3497
            O0OO0000O0OOOOO00 .GetEventObject ().Disable ()#line:3499
    def Purchase (OOOOOOO000000OO0O ,O000OOO0O0O0O0O00 ):#line:3501
        print ("购买")#line:3502
class UserValidator (wx .Validator ):#line:3506
    ""#line:3507
    def __init__ (OO00000O0O00OOOO0 ,OOOO0O0OOO0OO0O00 ):#line:3509
        wx .Validator .__init__ (OO00000O0O00OOOO0 )#line:3510
        OO00000O0O00OOOO0 .flag =OOOO0O0OOO0OO0O00 #line:3511
        OO00000O0O00OOOO0 .Bind (wx .EVT_CHAR ,OO00000O0O00OOOO0 .OnChar )#line:3512
    def Clone (O0O0O0OO0O0O000O0 ):#line:3515
        ""#line:3516
        return UserValidator (O0O0O0OO0O0O000O0 .flag )#line:3517
    def Validate (OOO00O0OO0OO0OO0O ,OO00OOOO0O0O0O0OO ):#line:3520
        return True #line:3521
    def TransferToWindow (O0O00O0OO0OOOO0O0 ):#line:3524
        return True #line:3525
    def TransferFromWindow (O0OOO0OOO00OO0OO0 ):#line:3528
        return True #line:3529
    def OnChar (O00O0OOOOO00O0OO0 ,OO0OOO00OO0OOOO00 ):#line:3532
        pass #line:3533
class PassValidator (wx .Validator ):#line:3547
    ""#line:3548
    def __init__ (OOOO0OO00OO00OOOO ):#line:3551
        wx .Validator .__init__ (OOOO0OO00OO00OOOO )#line:3552
        OOOO0OO00OO00OOOO .Bind (wx .EVT_CHAR ,OOOO0OO00OO00OOOO .OnChar )#line:3553
    def Clone (O0OO0000O0000OOOO ):#line:3556
        ""#line:3557
        return PassValidator ()#line:3558
    def Validate (OO00OO00OOO0OOOOO ,O0000OOO00OOOOO0O ):#line:3561
        return True #line:3562
    def TransferToWindow (OO0OOO0O0OO00OOO0 ):#line:3565
        return True #line:3566
    def TransferFromWindow (O000OOO00OOO00O00 ):#line:3569
        return True #line:3570
    def OnChar (OOOO000OOO0OO0000 ,O0000000O0O0OOOO0 ):#line:3573
        pass #line:3574
class ConfirmLogin (wx .Frame ):#line:3588
    pass #line:3589
class TimeThread (Thread ):#line:3592
    def __init__ (O0O0O000O00O00OOO ):#line:3593
        ""#line:3594
        Thread .__init__ (O0O0O000O00O00OOO )#line:3595
        O0O0O000O00O00OOO .setDaemon (True )#line:3596
        O0O0O000O00O00OOO .start ()#line:3597
    def run (OO000O000O000O0OO ):#line:3599
        ""#line:3600
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:3602
        for O000O00OOO0OO00OO in range (1000000 ):#line:3603
            OO00OOOO00O0O00O0 =time .clock ()#line:3604
            time .sleep (0.1 )#line:3605
            OO00OOO0OO0O0OO00 =time .clock ()#line:3606
            a_time +=OO00OOO0OO0O0OO00 -OO00OOOO00O0O00O0 #line:3607
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=OO00OOO0OO0O0OO00 -OO00OOOO00O0O00O0 #line:3608
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:3609
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:3610
class OpenwebThread (Thread ):#line:3641
    def __init__ (O000OO0O000O0O00O ,OOO00O0OO0000OOOO ):#line:3642
        ""#line:3643
        Thread .__init__ (O000OO0O000O0O00O )#line:3644
        O000OO0O000O0O00O .url =OOO00O0OO0000OOOO #line:3645
        O000OO0O000O0O00O .setDaemon (True )#line:3646
        O000OO0O000O0O00O .start ()#line:3647
    def run (OO0OOO0O0O000OO0O ):#line:3649
        ""#line:3650
        openweb (OO0OOO0O0O000OO0O .url )#line:3652
class HashThread (Thread ):#line:3654
    def __init__ (O00O00OOO00000OOO ):#line:3655
        ""#line:3656
        Thread .__init__ (O00O00OOO00000OOO )#line:3657
        O00O00OOO00000OOO .setDaemon (True )#line:3658
        O00O00OOO00000OOO .start ()#line:3659
    def run (OO0OOO0OO00OOOO0O ):#line:3661
        ""#line:3662
        Create_hash ()#line:3664
        getwebpath ()#line:3665
        import winreg as O0000000O0OOO0000 ,sys as O0O00OO000OO00O00 #line:3668
        OOO0O00O00O0OOOOO =O0000000O0OOO0000 .OpenKey (O0000000O0OOO0000 .HKEY_CURRENT_USER ,r"SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION",0 ,O0000000O0OOO0000 .KEY_ALL_ACCESS )#line:3672
        try :#line:3683
            O00O0O00OO0O0O0OO =os .path .realpath (O0O00OO000OO00O00 .argv [0 ])#line:3685
            O00O0O00OO0O0O0OO =O00O0O00OO0O0O0OO .split ('\\')[-1 ]#line:3686
            O0000000O0OOO0000 .SetValueEx (OOO0O00O00O0OOOOO ,'%s'%O00O0O00OO0O0O0OO ,0 ,O0000000O0OOO0000 .REG_DWORD ,0x00002710 )#line:3687
        except :#line:3689
            print ('error in set value!')#line:3691
class findposThread (Thread ):#line:3700
    def __init__ (O0O000000O00O00O0 ):#line:3701
        Thread .__init__ (O0O000000O00O00O0 )#line:3702
        O0O000000O00O00O0 .setDaemon (True )#line:3703
        O0O000000O00O00O0 .start ()#line:3704
    def run (O000OO0OO000O0O0O ):#line:3706
        findpos ()#line:3707
class sdfsf24324297Thread (Thread ):#line:3710
    def __init__ (O0OO00OO0O0OOO000 ):#line:3711
        Thread .__init__ (O0OO00OO0O0OOO000 )#line:3712
        O0OO00OO0O0OOO000 .setDaemon (True )#line:3713
        O0OO00OO0O0OOO000 .start ()#line:3714
    def run (O000OOO00OO0O0OO0 ):#line:3716
        global sdfsf24324297_need ,sdfsf24324297_on #line:3717
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3718
        for O0O000O000OO0O0O0 in range (100 ):#line:3719
            wx .Sleep (0.1 )#line:3720
            if sdfsf24324297_need :#line:3722
                findsdfsf24324297 ()#line:3724
                if sdfsf24324297_on :#line:3725
                    TopFrame .OnClick_sdfsf24324297 ()#line:3726
                    sdfsf24324297_need =False #line:3727
                    sdfsf24324297_on =False #line:3728
                    sdfsf24324297_one =False #line:3729
                    oo0o0O0O0O0_on =True #line:3730
        sdfsf24324297_one =False #line:3731
class uioo0o000ooThread (Thread ):#line:3733
    def __init__ (OOOO00O00O00OOOO0 ):#line:3734
        Thread .__init__ (OOOO00O00O00OOOO0 )#line:3735
        OOOO00O00O00OOOO0 .setDaemon (True )#line:3736
        OOOO00O00O00OOOO0 .start ()#line:3737
    def run (OO0O00O0000O00OOO ):#line:3739
        global sdfsf24324297_need ,sdfsf24324297_on #line:3740
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3741
        for O0OO0OOO00OO0O0OO in range (60 ):#line:3742
            if uioo0o000oo_need :#line:3743
                finduioo0o000oo ()#line:3744
                if uioo0o000oo_on :#line:3745
                    TopFrame .OnClick_Shuaxin ()#line:3746
        uioo0o000oo_one =False #line:3748
class LoginThread (Thread ):#line:3753
    def __init__ (O0000OO0O00O000OO ):#line:3754
        ""#line:3755
        Thread .__init__ (O0000OO0O00O000OO )#line:3756
        O0000OO0O00O000OO .setDaemon (True )#line:3757
        O0000OO0O00O000OO .start ()#line:3758
    def run (O00O00O00O0O00O00 ):#line:3760
        global Username ,login_result #line:3762
        login_result =ConfirmUser ()#line:3763
        print (login_result )#line:3764
        logging .info ("%s"%login_result )#line:3765
        wx .CallAfter (pub .sendMessage ,"connect")#line:3766
class controlThread (Thread ):#line:3769
    def __init__ (O0O000OO000OO0OOO ):#line:3770
        ""#line:3771
        Thread .__init__ (O0O000OO000OO0OOO )#line:3772
        O0O000OO000OO0OOO .setDaemon (True )#line:3773
        O0O000OO000OO0OOO .start ()#line:3774
    def run (OO0OO00000OOO000O ):#line:3777
        wx .Sleep (10 )#line:3778
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3779
class KeepThread (Thread ):#line:3784
    def __init__ (O0O0O0OO00OO0000O ):#line:3785
        ""#line:3786
        Thread .__init__ (O0O0O0OO00OO0000O )#line:3787
        O0O0O0OO00OO0000O .setDaemon (True )#line:3788
        O0O0O0OO00OO0000O .start ()#line:3789
    def run (O0O00O0O0OO0O0O00 ):#line:3792
        for O00O0OOOO0O0OO00O in range (1000000 ):#line:3793
            time .sleep (90 )#line:3794
            Keeplogin ()#line:3795
class TijiaoThread (Thread ):#line:3801
    def __init__ (OO0000OO00O00OOO0 ):#line:3802
        ""#line:3803
        Thread .__init__ (OO0000OO00O00OOO0 )#line:3804
        OO0000OO00O00OOO0 .setDaemon (True )#line:3805
        OO0000OO00O00OOO0 .start ()#line:3806
    def run (O0OOOOOOO000O0OOO ):#line:3809
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3810
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3811
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3812
        for OO0OOO000O000OOOO in range (10000000 ):#line:3813
            time .sleep (0.1 )#line:3814
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3818
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3820
                    oOO0O0O0O0O0O0_on =False #line:3821
                    TopFrame .SmartTijiao ()#line:3822
                    oOO0O0O0O0O0O0_on =False #line:3823
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3824
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3825
                    oOO0O0O0O0O0O0_one =True #line:3826
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3827
                    oOO0O0O0O0O0O0_on =False #line:3828
                    TopFrame .SmartTijiao ()#line:3829
                    oOO0O0O0O0O0O0_on =False #line:3830
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3831
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3832
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and a_time <=one_oO0O0O0O0O0O0O0O02 -one_delay and not oOO0O0O0O0O0O0_one :#line:3833
                    oOO0O0O0O0O0O0_on =False #line:3834
                    oOO0O0O0O0O0O0_on =False #line:3835
                    TopFrame .OnClick_Tijiao ()#line:3836
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3837
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3838
                    oOO0O0O0O0O0O0_one =True #line:3839
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and a_time <=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 -ooo0O0o0oO0O_delay :#line:3840
                    oOO0O0O0O0O0O0_on =False #line:3841
                    oOO0O0O0O0O0O0_on =False #line:3842
                    TopFrame .OnClick_Tijiao ()#line:3843
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3844
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3845
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3847
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time :#line:3849
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3850
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3851
                    oOO0O0O0O0O0O0_on =True #line:3852
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3853
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3854
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3855
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3856
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3857
                    oOO0O0O0O0O0O0_on =True #line:3858
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3859
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3860
class MoniTijiaoThread (Thread ):#line:3864
    def __init__ (OOO0OO0OO00O0OO0O ):#line:3865
        ""#line:3866
        Thread .__init__ (OOO0OO0OO00O0OO0O )#line:3867
        OOO0OO0OO00O0OO0O .setDaemon (True )#line:3868
        OOO0OO0OO00O0OO0O .start ()#line:3869
    def run (O0O0OOOOOO0O0O0O0 ):#line:3872
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3873
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3874
        for O0OOO0OOOO0O0OOO0 in range (10000000 ):#line:3875
            time .sleep (0.1 )#line:3876
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3878
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3882
                    TopFrame .SmartTijiao ()#line:3883
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3884
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3885
                    oOO0O0O0O0O0O0_on =False #line:3886
                    oOO0O0O0O0O0O0_one =True #line:3887
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3888
                    TopFrame .SmartTijiao ()#line:3889
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3890
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3891
                    oOO0O0O0O0O0O0_on =False #line:3892
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3893
                    oOO0O0O0O0O0O0_on =False #line:3894
                    TopFrame .OnClick_Tijiao ()#line:3895
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3896
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3897
                    oOO0O0O0O0O0O0_one =True #line:3898
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3899
                    oOO0O0O0O0O0O0_on =False #line:3900
                    TopFrame .OnClick_Tijiao ()#line:3901
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3902
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3903
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3908
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3909
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3910
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3912
                    oOO0O0O0O0O0O0_on =True #line:3913
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3914
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3915
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3916
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3917
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3919
                    oOO0O0O0O0O0O0_on =True #line:3920
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3921
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3922
class Infoframe (wx .Frame ):#line:3925
    def __init__ (OO0O000OO0O00O000 ,O0OO0OOOOOOOOOO00 ,OO0O0OO0OO000OOOO ,O0O00OOO0O000OO0O ):#line:3926
        wx .Frame .__init__ (OO0O000OO0O00O000 ,None ,-1 ,O0OO0OOOOOOOOOO00 ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3927
        OO0O000OO0O00O000 .Bind (wx .EVT_CLOSE ,OO0O000OO0O00O000 .OnClose )#line:3928
        OO0O000OO0O00O000 .panel =wx .Panel (OO0O000OO0O00O000 ,size =(300 ,220 ))#line:3929
        OO0O000OO0O00O000 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3930
        OO0O000OO0O00O000 .SetIcon (OO0O000OO0O00O000 .icon )#line:3931
class Guopaiframe (wx .Dialog ):#line:3934
    def __init__ (OO0OO00OO00O0O0O0 ,OOO0OOO00000OOOOO ):#line:3935
        wx .Frame .__init__ (OO0OO00OO00O0O0O0 ,None ,-1 ,OOO0OOO00000OOOOO ,size =(195 ,195 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3936
        OO0OO00OO00O0O0O0 .Bind (wx .EVT_CLOSE ,OO0OO00OO00O0O0O0 .OnClose )#line:3937
        OO0OO00OO00O0O0O0 .panel =wx .Panel (OO0OO00OO00O0O0O0 ,size =(195 ,200 ))#line:3938
        OO0OO00OO00O0O0O0 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3939
        OO0OO00OO00O0O0O0 .SetIcon (OO0OO00OO00O0O0O0 .icon )#line:3940
        OO0OO00OO00O0O0O0 .dianxin =wx .Button (OO0OO00OO00O0O0O0 .panel ,label ="上海电信",pos =(20 ,10 ),size =(140 ,60 ))#line:3944
        OO0OO00OO00O0O0O0 .nodianxin =wx .Button (OO0OO00OO00O0O0O0 .panel ,label ="非电信",pos =(20 ,80 ),size =(140 ,60 ))#line:3945
        OO0OO00OO00O0O0O0 .dianxin .SetFont (wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3946
        OO0OO00OO00O0O0O0 .nodianxin .SetFont (wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3947
        OO0OO00OO00O0O0O0 .Bind (wx .EVT_BUTTON ,OO0OO00OO00O0O0O0 .Dianxin ,OO0OO00OO00O0O0O0 .dianxin )#line:3948
        OO0OO00OO00O0O0O0 .Bind (wx .EVT_BUTTON ,OO0OO00OO00O0O0O0 .NoDianxin ,OO0OO00OO00O0O0O0 .nodianxin )#line:3949
        OO0OO00OO00O0O0O0 .Center ()#line:3950
        OO0OO00OO00O0O0O0 .ShowModal ()#line:3951
    def Dianxin (OO0000OO00O000OO0 ,OO0000O0OOO000OO0 ):#line:3952
        wx .CallAfter (pub .sendMessage ,"open dianxin")#line:3953
        OO0000OO00O000OO0 .Destroy ()#line:3954
        OO0000O0OOO000OO0 .Skip ()#line:3955
    def NoDianxin (O00OO0OOOO00OOO0O ,OOOO0000000O0000O ):#line:3956
        wx .CallAfter (pub .sendMessage ,"open nodianxin")#line:3957
        O00OO0OOOO00OOO0O .Destroy ()#line:3958
        OOOO0000000O0000O .Skip ()#line:3959
    def OnClose (OOOO00OOOO00O00OO ,O0O0OOO0OO00000OO ):#line:3960
        OOOO00OOOO00O00OO .Destroy ()#line:3961
        O0O0OOO0OO00000OO .Skip ()#line:3962
class SketchApp (wx .App ):#line:3964
    def OnInit (OOOO0000000OO00OO ):#line:3965
        try :#line:3976
            with open ("your.name",'rb')as O0OO0OO0OO0OO000O :#line:3977
                OO00OO0O0O000O0O0 =pickle .load (O0OO0OO0OO0OO000O )#line:3978
                O0OO0OO0OO0O0000O =OO00OO0O0O000O0O0 [0 ]#line:3979
                OOOO0O00O00000O0O =OO00OO0O0O000O0O0 [1 ]#line:3980
        except :#line:3981
            O0OO0OO0OO0O0000O ='123456'#line:3982
            OOOO0O00O00000O0O =0 #line:3983
        OO0O0O0O0O00O000O =LoginFrame ('小鲜肉拍牌',O0OO0OO0OO0O0000O ,OOOO0O00O00000O0O )#line:3984
        OO0O0O0O0O00O000O .Show (True )#line:3985
        return True #line:3986
if __name__ =='__main__':#line:3989
    app =SketchApp ()#line:3990
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
