""#line:5
version ='1.5s'#line:8
num =0 #line:9
avt =0 #line:10
host_ali ="121.196.220.94"#line:12
url1 ="http://moni.51hupai.org/"#line:15
url2 ="www.baidu.com"#line:16
mainicon ='ico.ico'#line:18
view =False #line:21
do =False #line:22
ad_view =False #line:23
zxco0o0o0o0_view =False #line:25
zxco0o0o0o0_on =False #line:26
zxco0o0o0o0_count =0 #line:27
web_on =False #line:28
view_time =False #line:30
time_on =False #line:31
import time #line:32
a_time =time .time ()#line:33
b_time =0 #line:34
o0sdofsfo0sodf0so0_minute =29 #line:36
o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:37
oo0o0O0O0O0_time =0 #line:39
Username =0 #line:41
Password =0 #line:42
o0sdofsfo0sodf0so0_on =False #line:45
ooweo0o0werwr_on =False #line:46
ghjo0o0o0o01 =53 #line:49
ghjo0o0o0o02 =0.0 #line:50
ghjo0o0o0o0_on =True #line:56
ghjo0o0o0o0_repeat =False #line:57
delay =False #line:60
delay_time =0.5 #line:61
login_result =False #line:63
findpos_on =True #line:66
zxco0o0o0o0list =[80000 +OO0OO00OOOOOOO0O0 *100 for OO0OO00OOOOOOO0O0 in range (200 )]#line:68
IDnumber =0 #line:69
account =0 #line:70
passwd =0 #line:71
import pyautogui as pg #line:75
def Create_hash ():#line:77
    with open ('dick.dl','rb')as O00OOOOOOO0OO0OO0 :#line:78
        global dick_hash #line:79
        dick_hash =pickle .load (O00OOOOOOO0OO0OO0 )#line:80
    with open ('cf.btn','rb')as OO0000O00O00O0O00 :#line:81
        global cf_hash #line:82
        cf_hash =pickle .load (OO0000O00O00O0O00 )#line:83
    with open ("target.tkl",'rb')as O0O00O00O00O000O0 :#line:85
        global dick_target #line:86
        dick_target =pickle .load (O0O00O00O00O000O0 )#line:87
OO00000o01 =48 #line:92
OO00000o02 =55 #line:93
one_oO0O0O0O0O0O0O0O01 =1000000000000 #line:94
one_oO0O0O0O0O0O0O0O02 =1000000000000 #line:95
one_diff =700 #line:96
one_delay =0.5 #line:97
one_advance =100 #line:98
ooo0O0o0oO0O_time1 =48 #line:101
ooo0O0o0oO0O_time2 =55 #line:102
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =1000000000000 #line:103
ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =1000000000000 #line:104
ooo0O0o0oO0O_diff =600 #line:105
ooo0O0o0oO0O_delay =0.5 #line:106
ooo0O0o0oO0O_advance =100 #line:107
osl =[0 ]*15 #line:109
oo0o0O0O0O0_on =True #line:111
oOO0O0O0O0O0O0_on =False #line:112
O0O0O0O0O0O0O_zxco0o0o0o0 =86000 #line:115
own_zxco0o0o0o01 =0 #line:116
own_zxco0o0o0o02 =0 #line:117
own_zxco0o0o0o0 =0 #line:118
oOO0O0O0O0O0O0_OK =False #line:120
e_on =True #line:121
enter_on =False #line:122
twice =False #line:124
oOO0O0O0O0O0O0_num =1 #line:125
oOO0O0O0O0O0O0_one =False #line:126
websize =[902 ,700 ]#line:129
Pxy =pg .size ()#line:130
Px1 =Pxy [0 ]/2 #line:131
Py2 =Pxy [1 ]/2 #line:132
Px =(Pxy [0 ]-websize [0 ])/2 -80 #line:133
Py =(Pxy [1 ]-websize [1 ])/2 #line:134
P_relative =[[343 ,-66 ],[346 ,40 ],[96 ,121 ],[92 ,43 ],[201 ,100 ],[281 ,40 ],[261 ,37 ],[282 ,118 ]]#line:137
P_relative2 =[[647 ,-98 ],[650 ,8 ],[400 ,89 ],[396 ,11 ],[505 ,68 ],[585 ,8 ],[565 ,5 ],[586 ,86 ]]#line:138
Oo0o0Oo0o0o0 =[[0 ,0 ]for O000O00O00O0OO0O0 in range (len (P_relative ))]#line:139
for i in range (len (Oo0o0Oo0o0o0 )):#line:140
    Oo0o0Oo0o0o0 [i ][0 ]=Px1 +P_relative [i ][0 ]#line:141
    Oo0o0Oo0o0o0 [i ][1 ]=Py2 +P_relative [i ][1 ]#line:142
px_ajust ,py_ajust =0 ,0 #line:145
for i in range (len (P_relative )):#line:146
    P_relative [i ][0 ]+=websize [0 ]/2 +px_ajust #line:147
    P_relative [i ][1 ]+=websize [1 ]/2 +py_ajust #line:148
px_zxco0o0o0o0 =770 -171 #line:150
py_zxco0o0o0o0 =260 #line:151
px_zxco0o0o0o0frame =220 -191 #line:153
py_zxco0o0o0o0frame =480 #line:154
px_timeframe =245 #line:156
py_timeframe =350 #line:157
px_O0O0O0O0O0O0Ozxco0o0o0o0frame =245 #line:159
py_O0O0O0O0O0O0Ozxco0o0o0o0frame =290 #line:160
O0O0O0O0O0O0Ozxco0o0o0o0frame_pos =[px_O0O0O0O0O0O0Ozxco0o0o0o0frame ,py_O0O0O0O0O0O0Ozxco0o0o0o0frame ]#line:161
px_sdfsnisdfafzxcvframe =400 -215 #line:164
py_sdfsnisdfafzxcvframe =460 #line:165
px_mini =200 #line:169
py_mini =40 #line:170
Pricesize =[400 ,80 ]#line:172
Timesize =[200 ,50 ]#line:174
O0O0O0O0O0O0Ozxco0o0o0o0_area =[179 -80 +Px ,424 -50 +Py ,179 +80 +Px ,424 +50 +Py ]#line:177
uioo0o000oo_area =[396 -80 ,11 -50 ,396 +80 ,11 +50 ]#line:178
sdfsf24324297_area =[505 -80 ,68 -50 ,505 +80 ,68 +50 ]#line:179
Px_zxco0o0o0o0 =Px +px_zxco0o0o0o0 #line:198
Py_zxco0o0o0o0 =Py +py_zxco0o0o0o0 #line:199
Pos_zxco0o0o0o0 =[Px_zxco0o0o0o0 ,Py_zxco0o0o0o0 ,Px_zxco0o0o0o0 +px_mini ,Py_zxco0o0o0o0 +py_mini ]#line:200
Px_zxco0o0o0o0frame =Px +px_zxco0o0o0o0frame #line:203
Py_zxco0o0o0o0frame =Py +py_zxco0o0o0o0frame #line:204
Pos_zxco0o0o0o0frame =[Px_zxco0o0o0o0frame ,Py_zxco0o0o0o0frame ]#line:205
Px_timeframe =px_timeframe #line:208
Py_timeframe =py_timeframe #line:209
Pos_timeframe =[Px_timeframe ,Py_timeframe ]#line:210
Px_sdfsnisdfafzxcvframe =Px +px_sdfsnisdfafzxcvframe #line:213
Py_sdfsnisdfafzxcvframe =Py +py_sdfsnisdfafzxcvframe #line:214
Pos_sdfsnisdfafzxcvframe =[Px_sdfsnisdfafzxcvframe ,Py_sdfsnisdfafzxcvframe ]#line:215
px_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:223
py_O0O0O0O0O0O0Ozxco0o0o0o0 =0 #line:224
Px_O0O0O0O0O0O0Ozxco0o0o0o0 =Px +px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:227
Py_O0O0O0O0O0O0Ozxco0o0o0o0 =Py +py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:228
O0O0O0O0O0O0Ozxco0o0o0o0_sizex =41 #line:229
O0O0O0O0O0O0Ozxco0o0o0o0_sizey =16 #line:230
px_relative =49 #line:232
py_relative =0 #line:233
px_sdfsf24324297 =656 #line:235
py_sdfsf24324297 =475 #line:236
Px_sdfsf24324297 =Px +px_sdfsf24324297 #line:237
Py_sdfsf24324297 =Py +py_sdfsf24324297 #line:238
sdfsf24324297_sizex =113 #line:239
sdfsf24324297_sizey =28 #line:240
sdfsf24324297_on =False #line:241
sdfsf24324297_need =False #line:242
sdfsf24324297_one =False #line:243
px_uioo0o000oo =550 #line:245
py_uioo0o000oo =413 #line:246
Px_uioo0o000oo =Px +px_uioo0o000oo #line:247
Py_uioo0o000oo =Py +py_uioo0o000oo #line:248
uioo0o000oo_sizex =108 #line:249
uioo0o000oo_sizey =21 #line:250
uioo0o000oo_on =False #line:251
uioo0o000oo_need =False #line:252
uioo0o000oo_one =False #line:253
oo0o0O0O0O0_interval =False #line:255
oOO0O0O0O0O0O0_interval =False #line:256
query_interval =False #line:257
query_on =False #line:258
import sys #line:261
if sys .platform !='win32':#line:262
    exit ()#line:263
import pyautogui as pg #line:264
import ctypes #line:265
from ctypes import wintypes #line:266
import win32con #line:267
import wx .html2 #line:268
import wx #line:269
import pickle #line:270
import wx .adv #line:271
from PIL import Image #line:272
import imagehash #line:273
import logging #line:350
timenow =time .time ()#line:351
time_local =time .localtime (timenow )#line:353
myapplog =time .strftime ("%Y%m%d%H%M%S",time_local )#line:355
print (myapplog )#line:356
logging .basicConfig (level =logging .DEBUG ,format ='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt ='%a, %d %b %Y %H:%M:%S',filename ='%s.log'%myapplog ,filemode ='w')#line:361
logging .debug ('This is debug message')#line:363
logging .info ('This is info message')#line:364
logging .warning ('This is warning message')#line:365
logging .error ('This is error message')#line:366
import win32gui ,win32api #line:369
import cv2 #line:370
from PIL import ImageGrab #line:371
def Click (OO0OO0000O0OO0O0O ,OO0000OO0O00OOOO0 ):#line:373
    OO00O00O0OO0000O0 =win32gui .GetCursorPos ()#line:374
    OO0OO0000O0OO0O0O =int (OO0OO0000O0OO0O0O )#line:375
    OO0000OO0O00OOOO0 =int (OO0000OO0O00OOOO0 )#line:376
    win32api .SetCursorPos ((OO0OO0000O0OO0O0O ,OO0000OO0O00OOOO0 ))#line:377
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OO0OO0000O0OO0O0O ,OO0000OO0O00OOOO0 ,0 ,0 )#line:378
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OO0OO0000O0OO0O0O ,OO0000OO0O00OOOO0 ,0 ,0 )#line:379
def Click2 (OO0OO0O0O00O0OO0O ,OO0O0000O00O00OOO ):#line:381
    OOOO0OOOOOO00O0O0 =win32gui .GetCursorPos ()#line:382
    OO0OO0O0O00O0OO0O =int (OO0OO0O0O00O0OO0O )#line:383
    OO0O0000O00O00OOO =int (OO0O0000O00O00OOO )#line:384
    win32api .SetCursorPos ((OO0OO0O0O00O0OO0O ,OO0O0000O00O00OOO ))#line:385
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,OO0OO0O0O00O0OO0O ,OO0O0000O00O00OOO ,0 ,0 )#line:386
    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,OO0OO0O0O00O0OO0O ,OO0O0000O00O00OOO ,0 ,0 )#line:387
    win32api .SetCursorPos (OOOO0OOOOOO00O0O0 )#line:388
import win32clipboard #line:392
def Paste ():#line:393
    win32api .keybd_event (17 ,0 ,0 ,0 )#line:394
    win32api .keybd_event (86 ,0 ,0 ,0 )#line:395
    win32api .keybd_event (86 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:396
    win32api .keybd_event (17 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:397
def setText (O00OO00O0O0O00OO0 ):#line:399
    O00OO00O0O0O00OO0 =O00OO00O0O0O00OO0 .encode ('utf-8')#line:400
    win32clipboard .OpenClipboard ()#line:401
    win32clipboard .EmptyClipboard ()#line:402
    win32clipboard .SetClipboardData (win32con .CF_TEXT ,O00OO00O0O0O00OO0 )#line:403
    win32clipboard .CloseClipboard ()#line:404
def Delete ():#line:406
    win32api .keybd_event (0x08 ,0 ,0 ,0 )#line:407
    win32api .keybd_event (0x08 ,0 ,win32con .KEYEVENTF_KEYUP ,0 )#line:408
def findpos ():#line:412
    O0O0O000O0OO0OOOO =ImageGrab .grab ().convert ('L')#line:414
    OOO0O000OOO0000OO =np .asarray (O0O0O000O0OO0OOOO )#line:415
    global dick_target #line:416
    OO0OOOOOOOO000000 =dick_target [2 ]#line:417
    OOOOO000OO000OOO0 ,O00OO0O0O0O0OOOO0 =OO0OOOOOOOO000000 .shape [::-1 ]#line:418
    OO00OOOOO000OOO0O =cv2 .matchTemplate (OOO0O000OOO0000OO ,OO0OOOOOOOO000000 ,cv2 .TM_CCOEFF_NORMED )#line:420
    O0OO0OO0O0OOO000O ,O000O0OOOOO0O0000 ,OOO00O0OOOOO00O0O ,O0O0OO00O00000O0O =cv2 .minMaxLoc (OO00OOOOO000OOO0O )#line:421
    global px_O0O0O0O0O0O0Ozxco0o0o0o0 ,py_O0O0O0O0O0O0Ozxco0o0o0o0 ,px_relative ,py_relative ,Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,Px ,Py #line:426
    px_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O0OO00O00000O0O [0 ]+px_relative #line:427
    py_O0O0O0O0O0O0Ozxco0o0o0o0 =O0O0OO00O00000O0O [1 ]+py_relative #line:428
    Px_O0O0O0O0O0O0Ozxco0o0o0o0 =px_O0O0O0O0O0O0Ozxco0o0o0o0 #line:429
    Py_O0O0O0O0O0O0Ozxco0o0o0o0 =py_O0O0O0O0O0O0Ozxco0o0o0o0 #line:430
    global Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:432
    for O000O0O000O00OOO0 in range (len (Oo0o0Oo0o0o0 )):#line:433
        Oo0o0Oo0o0o0 [O000O0O000O00OOO0 ][0 ]=Px_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O000O0O000O00OOO0 ][0 ]#line:434
        Oo0o0Oo0o0o0 [O000O0O000O00OOO0 ][1 ]=Py_O0O0O0O0O0O0Ozxco0o0o0o0 +P_relative2 [O000O0O000O00OOO0 ][1 ]#line:435
    uioo0o000oo_area =[396 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,396 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,11 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:436
    sdfsf24324297_area =[505 -80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 -50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,505 +80 +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,68 +50 +Py_O0O0O0O0O0O0Ozxco0o0o0o0 ]#line:437
    global findpos_on #line:439
    findpos_on =False #line:440
def finduioo0o000oo ():#line:442
    global dick_target ,uioo0o000oo_on ,Oo0o0Oo0o0o0 ,uioo0o000oo_area ,sdfsf24324297_area #line:443
    O0OO000O0OO00O000 =dick_target [0 ]#line:444
    OOOOOO0OOOO0OOOO0 =ImageGrab .grab (uioo0o000oo_area ).convert ('L')#line:445
    OOOOOO0OOOO0OOOO0 =ImageGrab .grab ().convert ('L')#line:446
    OO00O000000O000OO =np .asarray (OOOOOO0OOOO0OOOO0 )#line:447
    OO0OOOO000OO0OOOO ,O000O0OOO0O0OOOO0 =O0OO000O0OO00O000 .shape [::-1 ]#line:448
    O00000000O000O0O0 =cv2 .matchTemplate (OO00O000000O000OO ,O0OO000O0OO00O000 ,cv2 .TM_CCOEFF_NORMED )#line:449
    O0000O000O000OO00 ,O0OO00OOO000OOO00 ,OO00OOO0O00OOOOO0 ,OO00OO0OOO0OOO0OO =cv2 .minMaxLoc (O00000000O000O0O0 )#line:450
    print (O0OO00OOO000OOO00 )#line:451
    if O0OO00OOO000OOO00 >=0.6 :#line:452
        uioo0o000oo_on =True #line:453
def findsdfsf24324297 ():#line:456
    global dick_target ,sdfsf24324297_on ,Oo0o0Oo0o0o0 #line:457
    O00O0000OO0OO0000 =dick_target [1 ]#line:458
    OOO0O0OOO0O000000 =ImageGrab .grab (sdfsf24324297_area ).convert ('L')#line:459
    O0OO000O0O0O0O0O0 =np .asarray (OOO0O0OOO0O000000 )#line:460
    O000000000OO0O0O0 ,O00OOOO0000OO00O0 =O00O0000OO0OO0000 .shape [::-1 ]#line:461
    OO00O000O00O00OO0 =cv2 .matchTemplate (O0OO000O0O0O0O0O0 ,O00O0000OO0OO0000 ,cv2 .TM_CCOEFF_NORMED )#line:462
    O0O00O0OOOO000OOO ,OO0OOO00OO00OOOO0 ,O0O000000O00O0OO0 ,O000OOO00OOO00OO0 =cv2 .minMaxLoc (OO00O000O00O00OO0 )#line:463
    print (OO0OOO00OO00OOOO0 )#line:464
    if OO0OOO00OO00OOOO0 >=0.9 :#line:465
        sdfsf24324297_on =True #line:466
SZ =20 #line:470
bin_n =16 #line:471
import numpy as np #line:472
def hog (O0OO000000OOOO0O0 ):#line:475
    O00OO0OOO00O0O000 =cv2 .Sobel (O0OO000000OOOO0O0 ,cv2 .CV_32F ,1 ,0 )#line:476
    OO0OO0O0OO000OOOO =cv2 .Sobel (O0OO000000OOOO0O0 ,cv2 .CV_32F ,0 ,1 )#line:477
    O00OO0OO00O0O00OO ,O0O000O0OO0000O00 =cv2 .cartToPolar (O00OO0OOO00O0O000 ,OO0OO0O0OO000OOOO )#line:478
    OO0O0OO0OO0O000OO =np .int32 (bin_n *O0O000O0OO0000O00 /(2 *np .pi ))#line:479
    OO00O0O0OOOOO00OO =OO0O0OO0OO0O000OO [:10 ,:10 ],OO0O0OO0OO0O000OO [10 :,:10 ],OO0O0OO0OO0O000OO [:10 ,10 :],OO0O0OO0OO0O000OO [10 :,10 :]#line:480
    O0OOOOOO0000OO00O =O00OO0OO00O0O00OO [:10 ,:10 ],O00OO0OO00O0O00OO [10 :,:10 ],O00OO0OO00O0O00OO [:10 ,10 :],O00OO0OO00O0O00OO [10 :,10 :]#line:481
    OOO00000O0OO0O0OO =[np .bincount (O0O0OO0OO00000000 .ravel (),OO000OOOOO00O0O00 .ravel (),bin_n )for O0O0OO0OO00000000 ,OO000OOOOO00O0O00 in zip (OO00O0O0OOOOO00OO ,O0OOOOOO0000OO00O )]#line:482
    OO000O0OOOO000000 =np .hstack (OOO00000O0OO0O0OO )#line:483
    return OO000O0OOOO000000 #line:484
def cut (OOOOO0O0O00O0OOO0 ):#line:488
    OO0OO0O0O00OOOO00 ,OOO0O0OOOO0O000OO =cv2 .threshold (OOOOO0O0O00O0OOO0 ,127 ,255 ,cv2 .THRESH_BINARY_INV )#line:489
    OO0OOOOOO0OOOO0O0 ,O0O000OO0OO0O0000 ,OOOO0O00OOO0OO0O0 =cv2 .findContours (OOO0O0OOOO0O000OO ,cv2 .RETR_EXTERNAL ,cv2 .CHAIN_APPROX_NONE )#line:491
    OO0O0O0OOO0OOO000 =[]#line:492
    OOO0O00O0OOOO00OO =[]#line:493
    for O0OOO0O0000OO00OO in range (len (O0O000OO0OO0O0000 )):#line:494
        OO0O0000OOOO00O00 =O0O000OO0OO0O0000 [O0OOO0O0000OO00OO ]#line:495
        OO0OOOOO00OOO00O0 ,OO00000O0OOO0O0OO ,OOO00O00OOO0O0O0O ,OOO0OO00OO0O000O0 =cv2 .boundingRect (OO0O0000OOOO00O00 )#line:496
        OOO0O00O0OOOO00OO .append ([OO0OOOOO00OOO00O0 ,OO00000O0OOO0O0OO ,OOO00O00OOO0O0O0O ,OOO0OO00OO0O000O0 ])#line:498
    OOO0O00O0OOOO00OO =sorted (OOO0O00O0OOOO00OO )#line:500
    for O0OOO0O0000OO00OO in range (len (O0O000OO0OO0O0000 )):#line:501
        OO0OOOOO00OOO00O0 ,OO00000O0OOO0O0OO ,OOO00O00OOO0O0O0O ,OOO0OO00OO0O000O0 =OOO0O00O0OOOO00OO [O0OOO0O0000OO00OO ]#line:502
        OO0O0O0OOO0OOO000 .append (OO0OOOOOO0OOOO0O0 [OO00000O0OOO0O0OO :OO00000O0OOO0O0OO +OOO0OO00OO0O000O0 ,OO0OOOOO00OOO00O0 :OO0OOOOO00OOO00O0 +OOO00O00OOO0O0O0O ])#line:503
    return OO0O0O0OOO0OOO000 #line:504
def readpic (O0O0O00000OOOO00O ):#line:506
    try :#line:507
        OO0O0O000O0OOO0OO =cv2 .ml .SVM_load ('maindata.xml')#line:508
        O00OO000O0O0OO0O0 =cut (O0O0O00000OOOO00O )#line:509
        O00OO000O0O0OO0O0 =list (map (hog ,O00OO000O0O0OO0O0 ))#line:510
        O00OO000O0O0OO0O0 =np .float32 (O00OO000O0O0OO0O0 ).reshape (-1 ,64 )#line:511
        O00OOOOOOO0OO0O00 =OO0O0O000O0OOO0OO .predict (O00OO000O0O0OO0O0 )#line:512
        O00OOOOOOO0OO0O00 =O00OOOOOOO0OO0O00 [1 ].reshape (-1 ).astype (int ).astype (str )#line:513
        O000O00OO00OOO000 ="".join (list (O00OOOOOOO0OO0O00 ))#line:514
        return O000O00OO00OOO000 #line:515
    except :#line:516
        return False #line:517
import os #line:523
import socket #line:524
import struct #line:525
import select #line:526
import time #line:527
ICMP_ECHO_REQUEST =8 #line:529
DEFAULT_TIMEOUT =2 #line:530
DEFAULT_COUNT =1 #line:531
class Pinger (object ):#line:534
    ""#line:535
    def __init__ (OOO00O0OOO00000O0 ,OO00OO0OOO0O0OOO0 ,O0OOO0OOO000OOOOO =DEFAULT_COUNT ,OO0O0OOOO000O00O0 =DEFAULT_TIMEOUT ):#line:537
        OOO00O0OOO00000O0 .target_host =OO00OO0OOO0O0OOO0 #line:538
        OOO00O0OOO00000O0 .count =O0OOO0OOO000OOOOO #line:539
        OOO00O0OOO00000O0 .timeout =OO0O0OOOO000O00O0 #line:540
    def do_checksum (OOOOO0000OOOO0O0O ,O0O0O0OOO0OO00O00 ):#line:543
        ""#line:544
        OO0O0O0OOO000O00O =0 #line:545
        O0O000OOOO00OO0OO =(len (O0O0O0OOO0OO00O00 )/2 )*2 #line:546
        OO0000OOOOOO00OO0 =0 #line:547
        while OO0000OOOOOO00OO0 <O0O000OOOO00OO0OO :#line:548
            OO00O0OO00O000O0O =O0O0O0OOO0OO00O00 [OO0000OOOOOO00OO0 +1 ]*256 +O0O0O0OOO0OO00O00 [OO0000OOOOOO00OO0 ]#line:549
            OO0O0O0OOO000O00O =OO0O0O0OOO000O00O +OO00O0OO00O000O0O #line:550
            OO0O0O0OOO000O00O =OO0O0O0OOO000O00O &0xffffffff #line:551
            OO0000OOOOOO00OO0 =OO0000OOOOOO00OO0 +2 #line:552
        if O0O000OOOO00OO0OO <len (O0O0O0OOO0OO00O00 ):#line:554
            OO0O0O0OOO000O00O =OO0O0O0OOO000O00O +O0O0O0OOO0OO00O00 [len (O0O0O0OOO0OO00O00 )-1 ]#line:555
            OO0O0O0OOO000O00O =OO0O0O0OOO000O00O &0xffffffff #line:556
        OO0O0O0OOO000O00O =(OO0O0O0OOO000O00O >>16 )+(OO0O0O0OOO000O00O &0xffff )#line:557
        OO0O0O0OOO000O00O =OO0O0O0OOO000O00O +(OO0O0O0OOO000O00O >>16 )#line:558
        OOO0OOO00O0000O00 =~OO0O0O0OOO000O00O #line:559
        OOO0OOO00O0000O00 =OOO0OOO00O0000O00 &0xffff #line:560
        OOO0OOO00O0000O00 =OOO0OOO00O0000O00 >>8 |(OOO0OOO00O0000O00 <<8 &0xff00 )#line:561
        return OOO0OOO00O0000O00 #line:562
    def receive_ping (OOOO0000O0OO0O00O ,OO00OO0OO00OOOOOO ,O0O0OOO0OOOO0O0O0 ,OOOO0OOOO0O0000O0 ):#line:564
        OOO00000OO00O00OO =OOOO0OOOO0O0000O0 #line:565
        while True :#line:566
            OOOOOO0OO0O0O0OO0 =time .time ()#line:567
            O0OO0O00OOOOOO00O =select .select ([OO00OO0OO00OOOOOO ],[],[],OOO00000OO00O00OO )#line:568
            O0000OO0OO0OOO0O0 =(time .time ()-OOOOOO0OO0O0O0OO0 )#line:569
            if O0OO0O00OOOOOO00O [0 ]==[]:#line:570
                return #line:571
            OOO0OO00OOOOO0000 =time .time ()#line:573
            O00OOO0OOOO0OOO00 ,OO0OO0000O000O0OO =OO00OO0OO00OOOOOO .recvfrom (1024 )#line:574
            OO0OO0OO00O0000OO =O00OOO0OOOO0OOO00 [20 :28 ]#line:575
            O0O0O00OOO0O000OO ,OO0O0OO0O00OOOOO0 ,O000OO0O00000OO0O ,O0O00OOO0O0O000O0 ,O0O0O0OO0O0OOOOO0 =struct .unpack ("bbHHh",OO0OO0OO00O0000OO )#line:578
            if O0O00OOO0O0O000O0 ==O0O0OOO0OOOO0O0O0 :#line:579
                O00O00OO0OOOOO0O0 =struct .calcsize ("d")#line:580
                OOO0OO0O0O0OOO000 =struct .unpack ("d",O00OOO0OOOO0OOO00 [28 :28 +O00O00OO0OOOOO0O0 ])[0 ]#line:581
                return OOO0OO00OOOOO0000 -OOO0OO0O0O0OOO000 #line:582
            OOO00000OO00O00OO =OOO00000OO00O00OO -O0000OO0OO0OOO0O0 #line:584
            if OOO00000OO00O00OO <=0 :#line:585
                return #line:586
    def send_ping (O00O00OO0O000OO00 ,OO000OO000O000O0O ,O0O00OO0OOOO000OO ):#line:588
        ""#line:591
        O00OO0O00OOO00O0O =socket .gethostbyname (O00O00OO0O000OO00 .target_host )#line:592
        OOOO000O00000O0OO =0 #line:594
        OOOOOOOOOOOO0O0O0 =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,OOOO000O00000O0OO ,O0O00OO0OOOO000OO ,1 )#line:597
        OO000O000OOO000O0 =struct .calcsize ("d")#line:598
        OO00O00O00OOO0OO0 =(192 -OO000O000OOO000O0 )*"Q"#line:599
        OO00O00O00OOO0OO0 =struct .pack ("d",time .time ())+bytes (OO00O00O00OOO0OO0 ,encoding ="utf-8")#line:600
        OOOO000O00000O0OO =O00O00OO0O000OO00 .do_checksum (OOOOOOOOOOOO0O0O0 +OO00O00O00OOO0OO0 )#line:603
        OOOOOOOOOOOO0O0O0 =struct .pack ("bbHHh",ICMP_ECHO_REQUEST ,0 ,socket .htons (OOOO000O00000O0OO ),O0O00OO0OOOO000OO ,1 )#line:606
        O00000OOO0000O0O0 =OOOOOOOOOOOO0O0O0 +OO00O00O00OOO0OO0 #line:607
        OO000OO000O000O0O .sendto (O00000OOO0000O0O0 ,(O00OO0O00OOO00O0O ,1 ))#line:608
    def ping_once (OOOO000OO0O0OO0OO ):#line:610
        ""#line:613
        OO00OO0000O0O0O00 =socket .getprotobyname ("icmp")#line:614
        try :#line:615
            O00O00O0O0O0O0O00 =socket .socket (socket .AF_INET ,socket .SOCK_RAW ,OO00OO0000O0O0O00 )#line:616
        except socket .error as O0OOOO00000O0000O :#line:617
            if O0OOOO00000O0000O [0 ]==1 :#line:618
                O0OOOO00000O0000O [1 ]+="ICMP messages can only be sent from root user processes"#line:620
                raise socket .error (O0OOOO00000O0000O [1 ])#line:621
        except Exception as O000OOOO0O0OOO0O0 :#line:622
            print ("Exception: %s"%(O000OOOO0O0OOO0O0 ))#line:623
        OOOOOO0O000OOO0OO =os .getpid ()&0xFFFF #line:626
        OOOO000OO0O0OO0OO .send_ping (O00O00O0O0O0O0O00 ,OOOOOO0O000OOO0OO )#line:628
        OO000000OOO000000 =OOOO000OO0O0OO0OO .receive_ping (O00O00O0O0O0O0O00 ,OOOOOO0O000OOO0OO ,OOOO000OO0O0OO0OO .timeout )#line:629
        O00O00O0O0O0O0O00 .close ()#line:630
        return OO000000OOO000000 #line:631
    def ping (OO0OOOOOOO000O0OO ):#line:633
        ""#line:636
        for O00OO0000OO00O0OO in range (OO0OOOOOOO000O0OO .count ):#line:637
            print ("Ping to %s..."%OO0OOOOOOO000O0OO .target_host )#line:638
            try :#line:639
                O0000O0OO000000OO =OO0OOOOOOO000O0OO .ping_once ()#line:640
            except socket .gaierror as O00O000000O000O0O :#line:641
                print ("Ping failed. (socket error: '%s')"%O00O000000O000O0O )#line:642
                return "timeout"#line:643
            if O0000O0OO000000OO ==None :#line:645
                print ("Ping failed. (timeout within %ssec.)"%OO0OOOOOOO000O0OO .timeout )#line:646
                return "timeout"#line:647
            else :#line:649
                O0000O0OO000000OO =O0000O0OO000000OO *1000 #line:650
                print ("Get ping in %0.4fms"%O0000O0OO000000OO )#line:651
                return int (O0000O0OO000000OO )#line:652
pinger =Pinger (url2 )#line:654
pingnow =pinger .ping ()#line:655
import smtplib #line:659
from email .mime .text import MIMEText #line:662
import os #line:663
import mimetypes #line:664
import email #line:665
from email .mime .multipart import MIMEMultipart #line:666
from threading import Thread #line:669
import threading #line:670
from wx .lib .pubsub import pub #line:671
import socket ,sys ,json #line:676
timeout =10 #line:677
socket .setdefaulttimeout (timeout )#line:678
def ConfirmUser ():#line:680
    OO000O000O00O0000 =host_ali #line:681
    OOO0OOOOO0OO0000O =8080 #line:684
    OOOOO0000OOOO0OOO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:686
    try :#line:688
        OOOOO0000OOOO0OOO .connect ((OO000O000O00O0000 ,OOO0OOOOO0OO0000O ))#line:689
    except socket .gaierror as O0OOOOOOOOOOO0000 :#line:690
        logging .error ('连接失败 %s'%O0OOOOOOOOOOO0000 )#line:691
        logging .error ("Address-related error connecting to server: %s"%O0OOOOOOOOOOO0000 )#line:692
        return 'net error'#line:693
    except socket .error as O0OOOOOOOOOOO0000 :#line:695
        logging .error ('连接失败 %s'%O0OOOOOOOOOOO0000 )#line:696
        logging .error ("Connection error: %s"%O0OOOOOOOOOOO0000 )#line:697
        return 'net error'#line:698
    OOOO00OO0OO0O00O0 =['login',Username ,Password ]#line:702
    OOOO00OO0OO0O00O0 =json .dumps (OOOO00OO0OO0O00O0 )#line:703
    OOOO00OO0OO0O00O0 =bytes (OOOO00OO0OO0O00O0 ,encoding ="utf-8")#line:704
    logging .info ('发送信息 %s'%str (OOOO00OO0OO0O00O0 ,encoding ="utf-8"))#line:705
    OOOOO0000OOOO0OOO .send (OOOO00OO0OO0O00O0 )#line:706
    OOOOO0000OOOO0OOO .shutdown (1 )#line:708
    logging .info ("Submit Complete")#line:709
    print ("Submit Complete")#line:710
    try :#line:711
        O00OO0O000OO00OO0 =OOOOO0000OOOO0OOO .recv (1024 )#line:713
        print (O00OO0O000OO00OO0 )#line:714
        O00OO0O000OO00OO0 =str (O00OO0O000OO00OO0 ,encoding ="utf-8")#line:715
        O00OO0O000OO00OO0 =json .loads (O00OO0O000OO00OO0 )#line:716
        print (O00OO0O000OO00OO0 )#line:717
        OOOOOO0OO0O0O0O0O =O00OO0O000OO00OO0 [0 ]#line:718
        if OOOOOO0OO0O0O0O0O =='success':#line:719
            logging .info ('登录成功 %s'%OOOOOO0OO0O0O0O0O )#line:720
            global url2 #line:721
            url2 =O00OO0O000OO00OO0 [1 ]#line:722
            return 'login success'#line:723
        elif OOOOOO0OO0O0O0O0O =='wrong password':#line:724
            logging .warning ('密码错误 %s'%OOOOOO0OO0O0O0O0O )#line:725
            return 'wrong password'#line:726
        elif OOOOOO0OO0O0O0O0O =="wrong account":#line:727
            logging .warning ('账号错误 %s'%OOOOOO0OO0O0O0O0O )#line:728
            return 'wrong account'#line:729
        elif OOOOOO0OO0O0O0O0O =='repeat':#line:730
            logging .warning ('账号错误 %s'%OOOOOO0OO0O0O0O0O )#line:731
            return 'repeat'#line:732
    except :#line:733
        print ("连接失败")#line:734
        logging .warning ('连接失败 ')#line:735
        return False #line:736
def Logout ():#line:739
    OO00OO0000000OOO0 =host_ali #line:740
    OO0OOO0OOO00OO00O =8080 #line:743
    global Username #line:744
    O000OO0000O00O0O0 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:745
    try :#line:746
        O000OO0000O00O0O0 .connect ((OO00OO0000000OOO0 ,OO0OOO0OOO00OO00O ))#line:747
    except socket .gaierror as OO00OO0OOOO000O0O :#line:748
        print ("Address-related error connecting to server: %s"%OO00OO0OOOO000O0O )#line:749
        logging .info ("Address-related error connecting to server: %s"%OO00OO0OOOO000O0O )#line:750
    except socket .error as OO00OO0OOOO000O0O :#line:752
        print ("Connection error: %s"%OO00OO0OOOO000O0O )#line:753
        logging .info ("Connection error: %s"%OO00OO0OOOO000O0O )#line:754
    O0OO0OOOO0O0OO000 =['logout',Username ,Password ]#line:758
    O0OO0OOOO0O0OO000 =json .dumps (O0OO0OOOO0O0OO000 )#line:759
    O0OO0OOOO0O0OO000 =bytes (O0OO0OOOO0O0OO000 ,encoding ="utf-8")#line:760
    logging .info ('发送信息 %s'%str (O0OO0OOOO0O0OO000 ,encoding ="utf-8"))#line:761
    O000OO0000O00O0O0 .send (O0OO0OOOO0O0OO000 )#line:762
    O000OO0000O00O0O0 .shutdown (1 )#line:763
    print ("Submit Log Out Complete")#line:764
    logging .info ("Submit Log Out Complete")#line:765
def Keeplogin ():#line:768
    OO0OO0000O0O000O0 =host_ali #line:769
    OO0OOO00O000O0O00 =8080 #line:772
    global Username #line:773
    OO0O000O00OO00000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:774
    try :#line:775
        OO0O000O00OO00000 .connect ((OO0OO0000O0O000O0 ,OO0OOO00O000O0O00 ))#line:776
    except socket .gaierror as OOOOO0OO0OO00O000 :#line:777
        print ("Address-related error connecting to server: %s"%OOOOO0OO0OO00O000 )#line:778
        logging .info ("Address-related error connecting to server: %s"%OOOOO0OO0OO00O000 )#line:779
    except socket .error as OOOOO0OO0OO00O000 :#line:781
        print ("Connection error: %s"%OOOOO0OO0OO00O000 )#line:782
        logging .info ("Connection error: %s"%OOOOO0OO0OO00O000 )#line:783
    OO00O0O0OO00O000O =['keep',Username ,Password ]#line:787
    OO00O0O0OO00O000O =json .dumps (OO00O0O0OO00O000O )#line:788
    OO00O0O0OO00O000O =bytes (OO00O0O0OO00O000O ,encoding ="utf-8")#line:789
    logging .info ('发送信息 %s'%str (OO00O0O0OO00O000O ,encoding ="utf-8"))#line:790
    OO0O000O00OO00000 .send (OO00O0O0OO00O000O )#line:791
    OO0O000O00OO00000 .shutdown (1 )#line:793
    print ("Submit keep Complete")#line:794
    logging .info ("Submit keep Complete")#line:795
def send_mail (O0OO00O0O0O0O0O00 ,O000O0O00O0O000O0 ,OO0O00OOO0O00O0O0 ):#line:798
    O00OO0OOO0O0O0000 =open (OO0O00OOO0O00O0O0 ,'rb')#line:799
    OO0000O0O000O000O ,O0O0OOOOOO0OO00O0 =mimetypes .guess_type (OO0O00OOO0O00O0O0 )#line:800
    if OO0000O0O000O000O is None and O0O0OOOOOO0OO00O0 is None :#line:801
        OO0000O0O000O000O ='application/octet-stream'#line:802
    O0O0OO000O0OOO0O0 ,OOO00OOOO00O0O00O =OO0000O0O000O000O .split ('/',1 )#line:803
    O0O0O0OOO00O0O000 =email .mime .base .MIMEBase (O0O0OO000O0OOO0O0 ,OOO00OOOO00O0O00O )#line:804
    O0O0O0OOO00O0O000 .set_payload (O00OO0OOO0O0O0000 .read ())#line:805
    O00OO0OOO0O0O0000 .close ()#line:806
    email .encoders .encode_base64 (O0O0O0OOO00O0O000 )#line:807
    O00O000OOO0O0OO00 =os .path .basename (OO0O00OOO0O00O0O0 )#line:808
    O0O0O0OOO00O0O000 .add_header ('Content-Disposition','attachment',filename =O00O000OOO0O0OO00 )#line:809
    O000O0O00O0O000O0 =O000O0O00O0O000O0 #line:810
    OO00000OOO0OOO000 ='smtp.qq.com'#line:811
    OO00OOO0O0O0OO000 =os .environ .get ('MAIL_USERNAME')#line:812
    O000O00OOO0OO00O0 =os .environ .get ('MAIL_PASSWORD')#line:813
    O0OOO0OOO00O000OO =OO00OOO0O0O0OO000 #line:814
    O00OOO0O0O0OOO0O0 =MIMEMultipart ()#line:815
    O00OOO0O0O0OOO0O0 .attach (O0O0O0OOO00O0O000 )#line:816
    O00OOO0O0O0OOO0O0 ['Subject']=O0OO00O0O0O0O0O00 #line:817
    O00OOO0O0O0OOO0O0 ['From']=O0OOO0OOO00O000OO #line:818
    O00OOO0O0O0OOO0O0 ['To']=";".join (O000O0O00O0O000O0 )#line:819
    O0OO0OOOO0OO00000 =smtplib .SMTP_SSL (OO00000OOO0OOO000 ,465 )#line:820
    O0OO0OOOO0OO00000 .login (OO00OOO0O0O0OO000 ,O000O00OOO0OO00O0 )#line:821
    print ('login in  successfully')#line:822
    O0OO0OOOO0OO00000 .sendmail (O0OOO0OOO00O000OO ,O000O0O00O0O000O0 ,O00OOO0O0O0OOO0O0 .as_string ())#line:823
    O0OO0OOOO0OO00000 .quit ()#line:824
    print ('send email  successfully')#line:825
def Upload ():#line:827
    pass #line:828
def Com_read ():#line:831
    pass #line:832
def Com_decision ():#line:836
    pass #line:837
class TopFrame (wx .Frame ):#line:870
    def __init__ (O00OOO0OOOOOO00O0 ,OO0O00OOOOO0O0OO0 ,O0OOOO0OOO0OO00O0 ):#line:871
        wx .Frame .__init__ (O00OOO0OOOOOO00O0 ,None ,1 ,OO0O00OOOOO0O0OO0 ,size =(520 ,320 ))#line:873
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_CLOSE ,O00OOO0OOOOOO00O0 .OnClose )#line:874
        OO00OOO0O0OOO0O00 =time .time ()#line:878
        O00OOO0OOOOOO00O0 .statusbar =O00OOO0OOOOOO00O0 .CreateStatusBar ()#line:882
        O00OOO0OOOOOO00O0 .statusbar .SetFieldsCount (3 )#line:884
        O00OOO0OOOOOO00O0 .statusbar .SetStatusWidths ([-1 ,-2 ,-3 ])#line:885
        O00OOO0OOOOOO00O0 .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:887
        O00OOO0OOOOOO00O0 .SetIcon (O00OOO0OOOOOO00O0 .icon )#line:888
        O00OOO0OOOOOO00O0 .statusbar .SetStatusText (u"版本号",0 )#line:890
        O00OOO0OOOOOO00O0 .statusbar .SetStatusText (u"%s"%O0OOOO0OOO0OO00O0 ,1 )#line:893
        O00OOO0OOOOOO00O0 .statusbar .SetStatusText (u"软件作者：ZS ",2 )#line:896
        O00OOO0OOOOOO00O0 .statusbar .SetBackgroundColour ((240 ,255 ,255 ))#line:897
        OOO000OO00000O0O0 =wx .Panel (O00OOO0OOOOOO00O0 ,-1 )#line:899
        OOO000OO00000O0O0 .SetBackgroundColour ((240 ,255 ,255 ))#line:901
        O00OOO0OOOOOO00O0 .SetBackgroundColour ((240 ,255 ,255 ))#line:902
        O00OOO0OOOOOO00O0 .thread =TimeThread ()#line:930
        O00OOO0OOOOOO00O0 .keepthread =KeepThread ()#line:931
        O00OOO0OOOOOO00O0 .button5 =wx .Button (OOO000OO00000O0O0 ,label ='打开模拟',pos =(190 ,190 ))#line:959
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_BUTTON ,O00OOO0OOOOOO00O0 .Openo0sdofsfo0sodf0so0 ,O00OOO0OOOOOO00O0 .button5 )#line:960
        O00OOO0OOOOOO00O0 .button6 =wx .Button (OOO000OO00000O0O0 ,label ='打开国拍',pos =(280 ,190 ))#line:962
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_BUTTON ,O00OOO0OOOOOO00O0 .OpenGuopai ,O00OOO0OOOOOO00O0 .button6 )#line:963
        O00OOO0OOOOOO00O0 .button16 =wx .Button (OOO000OO00000O0O0 ,label ='修改国拍网址',pos =(370 ,190 ))#line:965
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_BUTTON ,O00OOO0OOOOOO00O0 .UrlGuopai ,O00OOO0OOOOOO00O0 .button16 )#line:966
        O00OOO0OOOOOO00O0 .urlText =wx .TextCtrl (OOO000OO00000O0O0 ,-1 ,pos =(370 ,230 ),size =(120 ,25 ))#line:967
        O00OOO0OOOOOO00O0 .button7 =wx .Button (OOO000OO00000O0O0 ,label ='显示帮助',pos =(10 ,190 ))#line:969
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_BUTTON ,O00OOO0OOOOOO00O0 .Help ,O00OOO0OOOOOO00O0 .button7 )#line:970
        O00OOO0OOOOOO00O0 .button8 =wx .Button (OOO000OO00000O0O0 ,label ='验证码练习',pos =(100 ,190 ))#line:972
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_BUTTON ,O00OOO0OOOOOO00O0 .Yan_practice ,O00OOO0OOOOOO00O0 .button8 )#line:973
        O00OOO0OOOOOO00O0 .timer2 =wx .Timer (O00OOO0OOOOOO00O0 )#line:1013
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_TIMER ,O00OOO0OOOOOO00O0 .MainControl ,O00OOO0OOOOOO00O0 .timer2 )#line:1014
        O00OOO0OOOOOO00O0 .timer2 .Start (100 )#line:1015
        O00OOO0OOOOOO00O0 .timer3 =wx .Timer (O00OOO0OOOOOO00O0 )#line:1023
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_TIMER ,O00OOO0OOOOOO00O0 .Lowest_zxco0o0o0o0 ,O00OOO0OOOOOO00O0 .timer3 )#line:1024
        O00OOO0OOOOOO00O0 .timer3 .Start (100 )#line:1025
        O00OOO0OOOOOO00O0 .timer4 =wx .Timer (O00OOO0OOOOOO00O0 )#line:1027
        O00OOO0OOOOOO00O0 .Bind (wx .EVT_TIMER ,O00OOO0OOOOOO00O0 .Find_pos ,O00OOO0OOOOOO00O0 .timer4 )#line:1028
        O00OOO0OOOOOO00O0 .timer4 .Start (150 )#line:1029
        O00OOO0OOOOOO00O0 .operationframe =OperationFrame ()#line:1038
        O00OOO0OOOOOO00O0 .operationframe .Show (False )#line:1039
    def Lowest_zxco0o0o0o0 (OO0000000O000O00O ,O0OOOOO0O000OOOOO ):#line:1049
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,findpos_on #line:1050
        if not findpos_on :#line:1051
            OOO00O0OO00OO0O0O =int (TopFrame .Price_read ())#line:1052
            if OOO00O0OO00OO0O0O in zxco0o0o0o0list :#line:1054
                O0O0O0O0O0O0O_zxco0o0o0o0 =OOO00O0OO00OO0O0O #line:1055
            else :#line:1056
                findpos_on =True #line:1057
    def Find_pos (O0OO00O00O0O0O00O ,O0OO0OOOO00OO0000 ):#line:1074
        global findpos_on #line:1075
        if findpos_on :#line:1076
            findpos ()#line:1077
    @staticmethod #line:1083
    def Confirm ():#line:1084
        global cf_hash ,sdfsf24324297_on #line:1085
        OOOOO000000OOO0OO =TopFrame .Confirm_hash ()#line:1086
        if OOOOO000000OOO0OO ==cf_hash [0 ]:#line:1087
            sdfsf24324297_on =True #line:1088
    @staticmethod #line:1089
    def Refresh ():#line:1090
        OOOO0O0OOOO00OOOO =TopFrame .Refresh_hash ()#line:1091
        global cf_hash ,uioo0o000oo_on #line:1092
        if OOOO0O0OOOO00OOOO ==cf_hash [1 ]:#line:1093
            uioo0o000oo_on =True #line:1094
    @staticmethod #line:1103
    def Price_read ():#line:1104
        OO00O00O0OO0OO00O =ImageGrab .grab ((Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex +Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey +Py_O0O0O0O0O0O0Ozxco0o0o0o0 )).convert ('L')#line:1106
        OO00O00O0OO0OO00O =np .asarray (OO00O00O0OO0OO00O )#line:1112
        OO0000OOOOOOO0O00 =readpic (OO00O00O0OO0OO00O )#line:1113
        return OO0000OOOOOOO0O00 #line:1115
    @staticmethod #line:1118
    def Price_hash ():#line:1119
        O00O00O00O000O0O0 =pg .screenshot (region =(Px_O0O0O0O0O0O0Ozxco0o0o0o0 ,Py_O0O0O0O0O0O0Ozxco0o0o0o0 ,O0O0O0O0O0O0Ozxco0o0o0o0_sizex ,O0O0O0O0O0O0Ozxco0o0o0o0_sizey ))#line:1121
        global num #line:1122
        num +=1 #line:1123
        OOOOO0O000OOO000O =imagehash .dhash (O00O00O00O000O0O0 )#line:1125
        return OOOOO0O000OOO000O #line:1128
    @staticmethod #line:1130
    def Confirm_hash ():#line:1131
        OO00000000OOO00O0 =pg .screenshot (region =(Px_sdfsf24324297 ,Py_sdfsf24324297 ,sdfsf24324297_sizex ,sdfsf24324297_sizey ))#line:1133
        OO00OOOOO00OOO0O0 =imagehash .dhash (OO00000000OOO00O0 )#line:1136
        return OO00OOOOO00OOO0O0 #line:1137
    @staticmethod #line:1139
    def Refresh_hash ():#line:1140
        OO00O0000O0OO000O =pg .screenshot (region =(Px_uioo0o000oo ,Py_uioo0o000oo ,uioo0o000oo_sizex ,uioo0o000oo_sizey ))#line:1142
        OOOOO00O00OO00000 =imagehash .dhash (OO00O0000O0OO000O )#line:1144
        return OOOOO00O00OO00000 #line:1145
    def OnEraseBackground (O0OO0OOO0O0O0OO00 ,O00O0OO0O00O00O00 ):#line:1149
        ""#line:1152
        O000O00000OOO00O0 =O00O0OO0O00O00O00 .GetDC ()#line:1153
        if not O000O00000OOO00O0 :#line:1154
            O000O00000OOO00O0 =wx .ClientDC (O0OO0OOO0O0O0OO00 )#line:1155
            O00O0OO0O00OOO0OO =O0OO0OOO0O0O0OO00 .GetUpdateRegion ().GetBox ()#line:1156
            O000O00000OOO00O0 .SetClippingRect (O00O0OO0O00OOO0OO )#line:1157
        O000O00000OOO00O0 .Clear ()#line:1158
        OO00OOOO0OOOO00O0 =wx .Bitmap ("blue.jpg")#line:1159
        O000O00000OOO00O0 .DrawBitmap (OO00OOOO0OOOO00O0 ,0 ,0 )#line:1160
    def OnClose (OO0O000O000O00O00 ,OOO00O0OO0O0OO0O0 ):#line:1164
        O0O0000OOO0OO0O0O =wx .MessageBox ('真的要退出第一枪吗?','确认',wx .OK |wx .CANCEL )#line:1165
        if O0O0000OOO0OO0O0O ==wx .OK :#line:1166
            import sys as OO0OO00OOO000OOO0 #line:1168
            OO0O000O000O00O00 .Show (False )#line:1173
            try :#line:1175
                OO0O000O000O00O00 .Close_time1 (OOO00O0OO0O0OO0O0 )#line:1176
                OO0O000O000O00O00 .Close_time2 (OOO00O0OO0O0OO0O0 )#line:1177
            except :#line:1178
                pass #line:1179
            Logout ()#line:1181
            wx .GetApp ().ExitMainLoop ()#line:1182
            OOO00O0OO0O0OO0O0 .Skip ()#line:1183
            OO0OO00OOO000OOO0 .exit (None )#line:1184
    def OnOpenAssist (O00O000OO0OOOO0OO ):#line:1188
        O00O000OO0OOOO0OO .Open ()#line:1189
        global do #line:1190
        if do :#line:1191
            wx .MessageBox ('启用成功','开启辅助',wx .OK |wx .ICON_INFORMATION )#line:1192
        else :#line:1193
            wx .MessageBox ('启用失败','开启辅助',wx .OK |wx .ICON_ERROR )#line:1194
        O00O000OO0OOOO0OO .Listen ()#line:1195
    @classmethod #line:1197
    def OnCloseAssist (O0OO00O0OOO000O0O ):#line:1198
        O0OO00O0OOO000O0O .Close ()#line:1199
    def OnViewPos (OOO0O0O00OOO0O000 ,O0OO0O0O0OO0OO00O ):#line:1206
        wx .CallAfter (pub .sendMessage ,"uioo0o000oo")#line:1207
        OOO0O0O00OOO0O000 .MovePos (O0OO0O0O0OO0OO00O )#line:1208
        global view #line:1209
        if not view :#line:1210
            view =True #line:1211
            for OOOO0O0OO0OOOO0O0 in range (len (Oo0o0Oo0o0o0 )):#line:1212
                OOO0O0O00OOO0O000 .posframe [OOOO0O0OO0OOOO0O0 ].Show (view )#line:1213
        else :#line:1214
            view =False #line:1215
            for OOOO0O0OO0OOOO0O0 in range (len (Oo0o0Oo0o0o0 )):#line:1216
                OOO0O0O00OOO0O000 .posframe [OOOO0O0OO0OOOO0O0 ].Hide ()#line:1217
    def OnSavePos (O00OO00OO00O0O00O ,O0O00OO0O0O0OO00O ):#line:1220
        O00OO00OO00O0O00O .MovePos (O0O00OO0O0O0OO00O )#line:1221
        O00OO00OO00O0O00O .Save_log ()#line:1222
        wx .MessageBox ('保存成功','定位保存',wx .OK |wx .ICON_INFORMATION )#line:1223
    def MovePos (O00000OO0OO0O000O ,OO00000OOO00OO0O0 ):#line:1229
        global Positon #line:1230
        for O0O0OO00000OOO00O in range (5 ):#line:1231
            O00O00O00000OO000 ,O0O000O00O0OOOO00 =Oo0o0Oo0o0o0 [O0O0OO00000OOO00O ]#line:1232
            O00000OO0OO0O000O .posframe [O0O0OO00000OOO00O ].Move (O00O00O00000OO000 -10 ,O0O000O00O0OOOO00 -5 )#line:1233
    def Openo0sdofsfo0sodf0so0 (O0000OOOO0O0O0OOO ,O0OO0O000OOO000O0 ):#line:1235
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1237
        ghjo0o0o0o0_on =True #line:1238
        OOOOOOO0OO0O0O00O =True #line:1239
        oo0o0O0O0O0_on =True #line:1240
        oOO0O0O0O0O0O0_on =False #line:1241
        oOO0O0O0O0O0O0_num =1 #line:1242
        oOO0O0O0O0O0O0_OK =False #line:1243
        global Px ,Py ,url1 ,ad_view ,web_on ,do ,ooweo0o0werwr_on ,o0sdofsfo0sodf0so0_on ,ghjo0o0o0o0_repeat #line:1244
        if ooweo0o0werwr_on :#line:1245
            wx .MessageBox ('请关闭国拍页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1246
        elif o0sdofsfo0sodf0so0_on :#line:1247
            wx .MessageBox ('请关闭模拟页面','开启模拟失败',wx .OK |wx .ICON_ERROR )#line:1248
        else :#line:1249
            O0000OOOO0O0O0OOO .Open ()#line:1254
            if do :#line:1255
                o0sdofsfo0sodf0so0_on =True #line:1256
                ad_view =True #line:1257
                web_on =True #line:1258
                O0000OOOO0O0O0OOO .fr =WebFrame (Px ,Py ,False ,'小鲜肉模拟')#line:1259
                O0000OOOO0O0O0OOO .operationframe .Show (True )#line:1260
                if time_on :#line:1262
                    O0000OOOO0O0O0OOO .operationframe .Opentime ()#line:1263
                if not ghjo0o0o0o0_repeat :#line:1264
                    O0000OOOO0O0O0OOO .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1265
                    O0000OOOO0O0O0OOO .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1266
                    ghjo0o0o0o0_repeat =True #line:1267
                OO00O000O00OO000O =wx .html2 .WebView .New (O0000OOOO0O0O0OOO .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ),style =wx .BORDER_NONE )#line:1270
                OO00O000O00OO000O .LoadURL (url1 )#line:1271
                OO00O000O00OO000O .CanSetZoomType (False )#line:1272
                O0000OOOO0O0O0OOO .fr .Show ()#line:1273
            else :#line:1277
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1278
                O0000OOOO0O0O0OOO .Close ()#line:1279
            O0000OOOO0O0O0OOO .Listen ()#line:1280
    def OpenGuopai (O00O00O00O000OOOO ,OOO0OO00O00O00OO0 ):#line:1330
        global oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,oOO0O0O0O0O0O0_OK #line:1332
        ghjo0o0o0o0_on =True #line:1333
        O000OOOO00O00000O =True #line:1334
        oo0o0O0O0O0_on =True #line:1335
        oOO0O0O0O0O0O0_on =False #line:1336
        oOO0O0O0O0O0O0_num =1 #line:1337
        oOO0O0O0O0O0O0_OK =False #line:1338
        global Px ,Py ,url2 ,ad_view ,web_on ,do ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:1339
        if o0sdofsfo0sodf0so0_on :#line:1340
            wx .MessageBox ('请关闭模拟页面','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1341
        elif ooweo0o0werwr_on :#line:1342
            wx .MessageBox ('国拍已经打开','开启国拍失败',wx .OK |wx .ICON_ERROR )#line:1343
        else :#line:1344
            O00O00O00O000OOOO .Open ()#line:1346
            if do :#line:1350
                ad_view =True #line:1351
                ooweo0o0werwr_on =True #line:1352
                O00O00O00O000OOOO .fr =WebFrame (Px ,Py ,False ,'小鲜肉代拍 国拍')#line:1353
                O00O00O00O000OOOO .operationframe .Show (True )#line:1354
                if time_on :#line:1356
                    O00O00O00O000OOOO .operationframe .Opentime ()#line:1357
                if not ghjo0o0o0o0_repeat :#line:1358
                    O00O00O00O000OOOO .o0sdofsfo0sodf0so0oOO0O0O0O0O0O0thread =MoniTijiaoThread ()#line:1359
                    O00O00O00O000OOOO .oOO0O0O0O0O0O0thread =TijiaoThread ()#line:1360
                    ghjo0o0o0o0_repeat =True #line:1361
                OOO00000O0O00O000 =wx .html2 .WebView .New (O00O00O00O000OOOO .fr ,size =(websize [0 ]+48 ,websize [1 ]+40 ),pos =(-17 ,0 ))#line:1363
                OOO00000O0O00O000 .LoadURL (url2 )#line:1364
                OOO00000O0O00O000 .CanSetZoomType (False )#line:1365
                O00O00O00O000OOOO .fr .Show ()#line:1366
            else :#line:1370
                wx .MessageBox ('请检查其它软件热键占用','辅助启用失败',wx .OK |wx .ICON_ERROR )#line:1371
                O00O00O00O000OOOO .Close ()#line:1372
            O00O00O00O000OOOO .Listen ()#line:1373
    def UrlGuopai (OO0OOO0O00O0O00O0 ,O0OOO000OOOOO00OO ):#line:1375
        global url2 #line:1376
        try :#line:1377
            url2 =OO0OOO0O00O0O00O0 .urlText .GetValue ()#line:1378
            wx .MessageBox ('修改网址成功','修改国拍网址',wx .OK )#line:1379
        except :#line:1380
            wx .MessageBox ('请输入正确网址','修改国址网址',wx .OK |wx .ICON_ERROR )#line:1381
    def Help (OOOOO00O0O0O000O0 ,O000O00OOO0000O00 ):#line:1384
        O0O000O0O000O00OO ="""%s

 谁帮我写个帮助啊
 啊
 啊
 啊"""%version #line:1390
        O0O0O000OO00O0000 =wx .adv .AboutDialogInfo ()#line:1393
        O0O0O000OO00O0000 .SetName ("小鲜肉拍牌")#line:1394
        O0O0O000OO00O0000 .SetVersion (O0O000O0O000O00OO )#line:1395
        O0O0O000OO00O0000 .AddDeveloper ("ZS")#line:1399
        wx .adv .AboutBox (O0O0O000OO00O0000 )#line:1400
    def Yan_practice (OOO00O00OO00O00OO ,OO0000O0000O0O0O0 ):#line:1402
        pass #line:1403
    def Time_adjust (OO0OOO000OOOO0OO0 ,OO00O00OOOO000000 ):#line:1405
        pass #line:1406
    @staticmethod #line:1416
    def OnJiajia ():#line:1417
        O0OOO0O0O0O0OO000 =pg .position ()#line:1418
        Oo0o0Oo0o0o0 [0 ][0 ]=O0OOO0O0O0O0OO000 [0 ]#line:1419
        Oo0o0Oo0o0o0 [0 ][1 ]=O0OOO0O0O0O0OO000 [1 ]#line:1420
        print (Oo0o0Oo0o0o0 [0 ][0 ],"  ",Oo0o0Oo0o0o0 [0 ][1 ])#line:1421
        findpos ()#line:1422
    @staticmethod #line:1425
    def OnChujia ():#line:1426
        O0O0OO000OO00OO00 =pg .position ()#line:1427
        Oo0o0Oo0o0o0 [1 ][0 ]=O0O0OO000OO00OO00 [0 ]#line:1428
        Oo0o0Oo0o0o0 [1 ][1 ]=O0O0OO000OO00OO00 [1 ]#line:1429
    @staticmethod #line:1430
    def OnTijiao ():#line:1431
        OOO0OOO00OO0OO000 =pg .position ()#line:1432
        Oo0o0Oo0o0o0 [2 ][0 ]=OOO0OOO00OO0OO000 [0 ]#line:1433
        Oo0o0Oo0o0o0 [2 ][1 ]=OOO0OOO00OO0OO000 [1 ]#line:1434
    @staticmethod #line:1435
    def OnShuaxin ():#line:1436
        OO0O0O0000O000OOO =pg .position ()#line:1437
        Oo0o0Oo0o0o0 [3 ][0 ]=OO0O0O0000O000OOO [0 ]#line:1438
        Oo0o0Oo0o0o0 [3 ][1 ]=OO0O0O0000O000OOO [1 ]#line:1439
    @staticmethod #line:1440
    def OnConfirm ():#line:1441
        O0O0O0000OOO00OO0 =pg .position ()#line:1442
        Oo0o0Oo0o0o0 [4 ][0 ]=O0O0O0000OOO00OO0 [0 ]#line:1443
        Oo0o0Oo0o0o0 [4 ][1 ]=O0O0O0000OOO00OO0 [1 ]#line:1444
    @staticmethod #line:1445
    def OnYanzhengma ():#line:1446
        O00OO0000OO0O0000 =pg .position ()#line:1447
        Oo0o0Oo0o0o0 [5 ][0 ]=O00OO0000OO0O0000 [0 ]#line:1448
        Oo0o0Oo0o0o0 [5 ][1 ]=O00OO0000OO0O0000 [1 ]#line:1449
    @staticmethod #line:1452
    def handle_Jiajia ():#line:1453
        TopFrame .OnJiajia ()#line:1454
    @staticmethod #line:1455
    def handle_Chujia ():#line:1456
        TopFrame .OnChujia ()#line:1457
    @staticmethod #line:1458
    def handle_Tijiao ():#line:1459
        TopFrame .OnTijiao ()#line:1460
    @staticmethod #line:1461
    def handle_Shuaxin ():#line:1462
        TopFrame .OnShuaxin ()#line:1463
    @staticmethod #line:1464
    def handle_Confirm ():#line:1465
        TopFrame .OnConfirm ()#line:1466
    @staticmethod #line:1467
    def handle_Yanzhengma ():#line:1468
        TopFrame .OnYanzhengma ()#line:1469
    @classmethod #line:1476
    def OnClick_Tijiao (O0OOOOO0O0OO0O0OO ):#line:1477
        global web_on ,oOO0O0O0O0O0O0_on ,one_delay ,ooo0O0o0oO0O_delay ,oOO0O0O0O0O0O0_num #line:1478
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on ,sdfsf24324297_one ,sdfsf24324297_need #line:1479
        sdfsf24324297_need =True #line:1480
        if oOO0O0O0O0O0O0_num ==1 :#line:1482
            O0OO000O0OOOO0000 =threading .Timer (one_delay ,O0OOOOO0O0OO0O0OO .Tijiao )#line:1483
            O0OO000O0OOOO0000 .start ()#line:1484
            oOO0O0O0O0O0O0_on =False #line:1485
            if twice :#line:1486
                print ("修改为2")#line:1487
                oOO0O0O0O0O0O0_num =2 #line:1488
            print ("成功提交")#line:1490
        elif oOO0O0O0O0O0O0_num ==2 :#line:1491
            oOO0O0O0O0O0O0_num =0 #line:1492
            O0OO000O0OOOO0000 =threading .Timer (ooo0O0o0oO0O_delay ,O0OOOOO0O0OO0O0OO .Tijiao )#line:1493
            O0OO000O0OOOO0000 .start ()#line:1494
            oOO0O0O0O0O0O0_on =False #line:1495
        else :#line:1497
            O0OOOOO0O0OO0O0OO .Tijiao ()#line:1498
    @staticmethod #line:1500
    def Tijiao ():#line:1501
        global oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_num #line:1502
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1503
        oOO0O0O0O0O0O0_OK =False #line:1504
        global sdfsf24324297_one #line:1505
        if not sdfsf24324297_one :#line:1506
            OOO000O0O0O0OOOO0 =sdfsf24324297Thread ()#line:1507
            sdfsf24324297_one =False #line:1508
    @staticmethod #line:1515
    def OnClick_Shuaxin ():#line:1516
        global web_on #line:1517
        Click (Oo0o0Oo0o0o0 [3 ][0 ],Oo0o0Oo0o0o0 [3 ][1 ])#line:1518
        Click (Oo0o0Oo0o0o0 [5 ][0 ],Oo0o0Oo0o0o0 [5 ][1 ])#line:1519
    @staticmethod #line:1521
    def OnClick_sdfsf24324297 ():#line:1522
        print (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1523
        Click (Oo0o0Oo0o0o0 [4 ][0 ],Oo0o0Oo0o0o0 [4 ][1 ])#line:1524
    @staticmethod #line:1526
    def OnClick_oo0o0O0O0O0 ():#line:1527
        global web_on ,O0O0O0O0O0O0O_zxco0o0o0o0 #line:1528
        global oOO0O0O0O0O0O0_num ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:1529
        global oOO0O0O0O0O0O0_on ,oo0o0O0O0O0_on #line:1530
        global uioo0o000oo_need ,uioo0o000oo_one ,oo0o0O0O0O0_interval #line:1531
        print (oo0o0O0O0O0_interval )#line:1532
        if not oo0o0O0O0O0_interval :#line:1533
            print (oOO0O0O0O0O0O0_num ,twice )#line:1534
            oo0o0O0O0O0_interval =True #line:1535
            oOO0O0O0O0O0O0_on =True #line:1536
            uioo0o000oo_need =True #line:1537
            if oOO0O0O0O0O0O0_num ==1 :#line:1538
                own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:1539
                setText (str (own_zxco0o0o0o01 ))#line:1540
                TopFrame .selfdelete ()#line:1541
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1542
                oOO0O0O0O0O0O0_on =True #line:1543
                oo0o0O0O0O0_on =False #line:1544
                oo0o0O0O0O0_interval =False #line:1545
                print (oo0o0O0O0O0_interval )#line:1546
                if not uioo0o000oo_one :#line:1548
                    O0O00O0O0O0OOO0OO =uioo0o000ooThread ()#line:1549
                    uioo0o000oo_one =True #line:1550
            elif oOO0O0O0O0O0O0_num ==2 and twice :#line:1551
                own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:1553
                setText (str (own_zxco0o0o0o02 ))#line:1554
                TopFrame .selfdelete ()#line:1555
                Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1556
                oOO0O0O0O0O0O0_on =True #line:1557
                oo0o0O0O0O0_on =False #line:1558
                oo0o0O0O0O0_interval =False #line:1559
                if not uioo0o000oo_one :#line:1560
                    O0O00O0O0O0OOO0OO =uioo0o000ooThread ()#line:1561
                    uioo0o000oo_one =True #line:1562
    @staticmethod #line:1563
    def selfdelete ():#line:1564
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1565
        Click2 (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1566
        Delete ()#line:1567
        Paste ()#line:1568
    @staticmethod #line:1573
    def selfChujia ():#line:1574
        OOO00OOOOO0000O0O =wx .FindWindowById (1 )#line:1579
        OOO00OOOOO0000O0O .Show (True )#line:1580
    @staticmethod #line:1591
    def selfTijiao ():#line:1592
        OperationFrame .Del_shot ()#line:1593
        Click (Oo0o0Oo0o0o0 [2 ][0 ],Oo0o0Oo0o0o0 [2 ][1 ])#line:1594
    @staticmethod #line:1654
    def OnClick_Backspace ():#line:1655
        pg .press ('backspace')#line:1656
    def MainControl (OOOOOOO0O0O00OOOO ,O0OOOO000OOOO00OO ):#line:1660
        if not web_on and time_on :#line:1662
            OOOOOOO0O0O00OOOO .operationframe .Closetime ()#line:1663
        if web_on :#line:1664
            try :#line:1665
                OOOOOOO0O0O00OOOO .operationframe .Show (True )#line:1666
            except :#line:1667
                pass #line:1668
        else :#line:1669
            try :#line:1670
                OOOOOOO0O0O00OOOO .operationframe .Show (False )#line:1671
            except :#line:1672
                pass #line:1673
        if web_on :#line:1676
            OOOOOOO0O0O00OOOO .Show (False )#line:1677
        else :#line:1678
            OOOOOOO0O0O00OOOO .Show (True )#line:1679
    @staticmethod #line:1683
    def oOO0O0O0O0O0O0_ok ():#line:1684
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need ,oOO0O0O0O0O0O0_on #line:1685
        if e_on and oOO0O0O0O0O0O0_on :#line:1686
            oOO0O0O0O0O0O0_OK =True #line:1687
            uioo0o000oo_need =False #line:1688
    @staticmethod #line:1690
    def oOO0O0O0O0O0O0_ok2 ():#line:1691
        global oOO0O0O0O0O0O0_OK ,uioo0o000oo_need #line:1692
        if enter_on and oOO0O0O0O0O0O0_on :#line:1693
            oOO0O0O0O0O0O0_OK =True #line:1694
            uioo0o000oo_need =False #line:1695
    @classmethod #line:1697
    def query (OO00O0000OO0000OO ):#line:1698
        global query_interval ,query_on #line:1699
        if not query_interval and not query_on :#line:1700
            query_on =True #line:1702
            query_interval =True #line:1703
            setText (str (1000000 ))#line:1704
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1705
            Click (Oo0o0Oo0o0o0 [6 ][0 ],Oo0o0Oo0o0o0 [6 ][1 ])#line:1706
            Paste ()#line:1707
            Click (Oo0o0Oo0o0o0 [1 ][0 ],Oo0o0Oo0o0o0 [1 ][1 ])#line:1708
            O00O000000OO000OO =threading .Timer (3 ,OO00O0000OO0000OO .query_sleep3 )#line:1709
            O00O000000OO000OO .start ()#line:1710
            O00OOO0O000O00OOO =threading .Timer (5 ,OO00O0000OO0000OO .query_sleep5 )#line:1711
            O00OOO0O000O00OOO .start ()#line:1712
        elif query_interval and query_on :#line:1713
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1715
            query_on =False #line:1716
    @staticmethod #line:1719
    def query_sleep3 ():#line:1720
        global query_interval ,query_on #line:1722
        if query_on :#line:1723
            Click (Oo0o0Oo0o0o0 [7 ][0 ],Oo0o0Oo0o0o0 [7 ][1 ])#line:1725
            query_on =False #line:1726
    @staticmethod #line:1728
    def query_sleep5 ():#line:1729
        global query_interval #line:1731
        query_interval =False #line:1732
    @staticmethod #line:1748
    def Open ():#line:1749
        global do ,web_on #line:1750
        if not do :#line:1751
            do =True #line:1752
            O0OOO0O000OOO0000 ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1758
            OO0OOOO0O0O00OO00 =ctypes .windll .user32 #line:1759
            OOO0O0O000OO000O0 ={1 :(O0OOO0O000OOO0000 ['2'],win32con .MOD_ALT ),2 :(O0OOO0O000OOO0000 ['3'],win32con .MOD_ALT ),3 :(O0OOO0O000OOO0000 ['4'],win32con .MOD_ALT ),4 :(O0OOO0O000OOO0000 ['5'],win32con .MOD_ALT ),5 :(O0OOO0O000OOO0000 ['6'],win32con .MOD_ALT ),6 :(O0OOO0O000OOO0000 ['7'],win32con .MOD_ALT ),}#line:1763
            O0O000OOO000OO000 ={7 :(O0OOO0O000OOO0000 ['s'],0x4000 ),8 :(O0OOO0O000OOO0000 ['f'],0x4000 ),9 :(O0OOO0O000OOO0000 ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O0OOO0O000OOO0000 ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O0OOO0O000OOO0000 ['q'],0x4000 )}#line:1766
            for OOO0OO00O0OO00O0O ,(O00OO0OOO0OO000OO ,O0OOO0000OOOO00OO )in OOO0O0O000OO000O0 .items ():#line:1768
                if not OO0OOOO0O0O00OO00 .RegisterHotKey (None ,OOO0OO00O0OO00O0O ,O0OOO0000OOOO00OO ,O00OO0OOO0OO000OO ):#line:1769
                    print ("Unable to register id",OOO0OO00O0OO00O0O )#line:1770
                    logging .info ("Unable to register id",OOO0OO00O0OO00O0O )#line:1771
                    do =False #line:1772
            for OOO0OO00O0OO00O0O ,(O00OO0OOO0OO000OO ,O0OOO0000OOOO00OO )in O0O000OOO000OO000 .items ():#line:1773
                if not OO0OOOO0O0O00OO00 .RegisterHotKey (None ,OOO0OO00O0OO00O0O ,O0OOO0000OOOO00OO ,O00OO0OOO0OO000OO ):#line:1774
                    print ("Unable to register id",OOO0OO00O0OO00O0O )#line:1775
                    logging .info ("Unable to register id",OOO0OO00O0OO00O0O )#line:1776
                    do =False #line:1777
                web_on =True #line:1778
    @staticmethod #line:1781
    def Listen ():#line:1782
        try :#line:1783
            O0OOOO0OO0O0OO00O ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1788
            O0O0O000OOO000O00 ={1 :TopFrame .handle_Jiajia ,2 :TopFrame .handle_Chujia ,3 :TopFrame .handle_Tijiao ,4 :TopFrame .handle_Shuaxin ,5 :TopFrame .handle_Confirm ,6 :TopFrame .handle_Yanzhengma ,7 :TopFrame .OnClick_Shuaxin ,8 :TopFrame .selfTijiao ,9 :TopFrame .selfChujia ,10 :TopFrame .OnClick_Backspace ,11 :TopFrame .oOO0O0O0O0O0O0_ok ,12 :TopFrame .oOO0O0O0O0O0O0_ok2 ,13 :TopFrame .query }#line:1794
            OO0OO0OO0O0OOOOOO =ctypes .windll .user32 #line:1795
            O00O000O0000O0O0O =wintypes .MSG ()#line:1796
            OOO0OOO0OOOOOOO00 =ctypes .byref #line:1797
            while OO0OO0OO0O0OOOOOO .GetMessageA (OOO0OOO0OOOOOOO00 (O00O000O0000O0O0O ),None ,0 ,0 )!=0 :#line:1798
                if O00O000O0000O0O0O .message ==win32con .WM_HOTKEY :#line:1799
                    OO0OO0O000O0OOO00 =O0O0O000OOO000O00 .get (O00O000O0000O0O0O .wParam )#line:1800
                    if OO0OO0O000O0OOO00 :#line:1801
                        OO0OO0O000O0OOO00 ()#line:1802
                OO0OO0OO0O0OOOOOO .TranslateMessage (OOO0OOO0OOOOOOO00 (O00O000O0000O0O0O ))#line:1803
                OO0OO0OO0O0OOOOOO .DispatchMessageA (OOO0OOO0OOOOOOO00 (O00O000O0000O0O0O ))#line:1804
        finally :#line:1805
            pass #line:1806
    @staticmethod #line:1813
    def Close ():#line:1814
        global do #line:1815
        if do :#line:1816
            do =False #line:1817
            O0O0OO00OOOO0OOOO ={'0':0x30 ,'1':0x31 ,'2':0x32 ,'3':0x33 ,'4':0x34 ,'5':0x35 ,'6':0x36 ,'7':0x37 ,'8':0x38 ,'9':0x39 ,'a':0x41 ,'b':0x42 ,'c':0x43 ,'d':0x44 ,'e':0x45 ,'f':0x46 ,'s':0x53 ,'q':0x51 }#line:1821
            O0OOOOO0000O0O000 ={1 :(O0O0OO00OOOO0OOOO ['2'],win32con .MOD_ALT ),2 :(O0O0OO00OOOO0OOOO ['3'],win32con .MOD_ALT ),3 :(O0O0OO00OOOO0OOOO ['4'],win32con .MOD_ALT ),4 :(O0O0OO00OOOO0OOOO ['5'],win32con .MOD_ALT ),5 :(O0O0OO00OOOO0OOOO ['6'],win32con .MOD_ALT ),6 :(O0O0OO00OOOO0OOOO ['7'],win32con .MOD_ALT ),}#line:1825
            OO00OO0O000OO00O0 =ctypes .windll .user32 #line:1826
            OOO00000OO0O000O0 ={7 :(O0O0OO00OOOO0OOOO ['s'],0x4000 ),8 :(O0O0OO00OOOO0OOOO ['f'],0x4000 ),9 :(O0O0OO00OOOO0OOOO ['d'],0x4000 ),10 :(win32con .VK_SPACE ,0x4000 ),11 :(O0O0OO00OOOO0OOOO ['e'],0x4000 ),12 :(win32con .VK_RETURN ,0x4000 ),13 :(O0O0OO00OOOO0OOOO ['q'],0x4000 )}#line:1829
            for O0OOO0O0OOOOO0OO0 in O0OOOOO0000O0O000 .keys ():#line:1830
                OO00OO0O000OO00O0 .UnregisterHotKey (None ,O0OOO0O0OOOOO0OO0 )#line:1831
            for O0OOO0O0OOOOO0OO0 in OOO00000OO0O000O0 .keys ():#line:1832
                OO00OO0O000OO00O0 .UnregisterHotKey (None ,O0OOO0O0OOOOO0OO0 )#line:1833
            logging .info ("close assistant success")#line:1834
        else :#line:1835
            pass #line:1836
    def Save_log (O00000OOOOO000000 ):#line:1838
        OO0OO0OOO0O00OO00 =open ('pos.log','wb')#line:1839
        pickle .dump (Oo0o0Oo0o0o0 ,OO0OO0OOO0O00OO00 )#line:1840
        OO0OO0OOO0O00OO00 .close ()#line:1841
    def Confirmlogin (O00OO0O0OOO000OO0 ,OO0O0OO0OOOOO0OO0 ):#line:1921
        Keeplogin ()#line:1922
    def Choose_time1 (O0OOO00OO0O0OOO0O ,OO0OO0O00OO0O0O0O ):#line:1927
        O0OOO00OO0O0OOO0O .timelabel .SetLabel ("已设定截止时间"+O0OOO00OO0O0OOO0O .time_choice1 .GetString (O0OOO00OO0O0OOO0O .time_choice1 .GetSelection ())+'.'+str (O0OOO00OO0O0OOO0O .time_choice2 .GetSelection ())+" 秒")#line:1930
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1931
        ghjo0o0o0o01 =O0OOO00OO0O0OOO0O .time_choice1 .GetString (O0OOO00OO0O0OOO0O .time_choice1 .GetSelection ())#line:1932
        ghjo0o0o0o02 =O0OOO00OO0O0OOO0O .time_choice2 .GetString (O0OOO00OO0O0OOO0O .time_choice2 .GetSelection ())#line:1933
    def Choose_time2 (OO0OO00OOO00000O0 ,O00000O000OOO0OO0 ):#line:1936
        OO0OO00OOO00000O0 .timelabel .SetLabel ("已设定截止时间"+OO0OO00OOO00000O0 .time_choice1 .GetString (OO0OO00OOO00000O0 .time_choice1 .GetSelection ())+'.'+str (OO0OO00OOO00000O0 .time_choice2 .GetSelection ())+" 秒")#line:1939
        global ghjo0o0o0o01 ,ghjo0o0o0o02 #line:1940
        ghjo0o0o0o01 =OO0OO00OOO00000O0 .time_choice1 .GetString (OO0OO00OOO00000O0 .time_choice1 .GetSelection ())#line:1941
        ghjo0o0o0o02 =OO0OO00OOO00000O0 .time_choice2 .GetString (OO0OO00OOO00000O0 .time_choice2 .GetSelection ())#line:1942
class ClockWindow (wx .Panel ):#line:1995
    def __init__ (O00O0OO000O00OO0O ,OO0OOO00O00O0O000 ):#line:1996
        wx .Window .__init__ (O00O0OO000O00OO0O ,OO0OOO00O00O0O000 ,size =Timesize )#line:1997
        O00O0OO000O00OO0O .Bind (wx .EVT_PAINT ,O00O0OO000O00OO0O .OnPaint )#line:1998
        O00O0OO000O00OO0O .timer =wx .Timer (O00O0OO000O00OO0O )#line:1999
        O00O0OO000O00OO0O .Bind (wx .EVT_TIMER ,O00O0OO000O00OO0O .OnTimer ,O00O0OO000O00OO0O .timer )#line:2000
        O00O0OO000O00OO0O .timer .Start (100 )#line:2001
    def Draw (OOO00O0OO0O0000OO ,OOO000O0OO0OO0O0O ):#line:2003
        global a_time #line:2004
        OO000OOO0O000O0O0 =time .localtime (a_time )#line:2005
        O0O0O0O00OO0OO0O0 =time .strftime ("%H:%M:%S",OO000OOO0O000O0O0 )#line:2006
        O0OOO00O00OO0O0O0 ,O0OOO000O00OOO0OO =OOO00O0OO0O0000OO .GetClientSize ()#line:2007
        OOO000O0OO0OO0O0O .SetBackground (wx .Brush (OOO00O0OO0O0000OO .GetBackgroundColour ()))#line:2008
        OOO000O0OO0OO0O0O .Clear ()#line:2009
        OOO000O0OO0OO0O0O .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2010
        O0O00000OO00O00OO ,O0O0OOO00O0O0O0OO =OOO000O0OO0OO0O0O .GetTextExtent (O0O0O0O00OO0OO0O0 )#line:2011
        OOO000O0OO0OO0O0O .DrawText (O0O0O0O00OO0OO0O0 ,(O0OOO00O00OO0O0O0 -O0O00000OO00O00OO )/2 ,(O0OOO000O00OOO0OO )/2 -O0O0OOO00O0O0O0OO /2 )#line:2012
    def Modify (O00O0OO0OO0OOOO00 ,OO000OO000O000000 ):#line:2014
        global a_time ,b_time #line:2015
        if b_time <9 :#line:2017
            b_time =b_time +1 #line:2018
        else :#line:2019
            b_time =0 #line:2020
        O000O000O00O000OO =time .localtime (a_time )#line:2021
        OO0OOOOOO0OOOOOO0 =time .strftime ("%H:%M:%S",O000O000O00O000OO )#line:2022
        OO00O0000000OOO00 ,OOOO00O0O0000OO00 =O00O0OO0OO0OOOO00 .GetClientSize ()#line:2024
        OO000OO000O000000 .SetBackground (wx .Brush (O00O0OO0OO0OOOO00 .GetBackgroundColour ()))#line:2025
        OO000OO000O000000 .Clear ()#line:2026
        OO000OO000O000000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2027
        OOO00000000OO0OOO ,OO000O00O0OO0O00O =OO000OO000O000000 .GetTextExtent (OO0OOOOOO0OOOOOO0 )#line:2028
        OO000OO000O000000 .DrawText (OO0OOOOOO0OOOOOO0 ,(OO00O0000000OOO00 -OOO00000000OO0OOO )/2 ,(OOOO00O0O0000OO00 )/2 -OO000O00O0OO0O00O /2 )#line:2029
    def OnTimer (O0OO000O000000O00 ,OOO000O000OOO00O0 ):#line:2031
        OO0OO00OO0000O00O =wx .BufferedDC (wx .ClientDC (O0OO000O000000O00 ))#line:2032
        O0OO000O000000O00 .Modify (OO0OO00OO0000O00O )#line:2033
    def OnPaint (O0000O00O0OOOOO0O ,OOOO00O0O00O00O0O ):#line:2035
        O0O00OO0O0O0OOO0O =wx .BufferedPaintDC (O0000O00O0OOOOO0O )#line:2036
        O0000O00O0OOOOO0O .Draw (O0O00OO0O0O0OOO0O )#line:2037
class TimeFrame (wx .Frame ):#line:2041
    def __init__ (O00OOO0OOOOO00OO0 ):#line:2042
        wx .Frame .__init__ (O00OOO0OOOOO00OO0 ,None ,title ="wx.Timer",size =Timesize ,pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2044
        ClockWindow (O00OOO0OOOOO00OO0 )#line:2047
class MoniClockWindow (wx .Panel ):#line:2052
    def __init__ (OOOO0O0OOO0OO0OOO ,O0OO00O0O0O0O0OO0 ):#line:2053
        wx .Window .__init__ (OOOO0O0OOO0OO0OOO ,O0OO00O0O0O0O0OO0 ,size =Timesize )#line:2054
        OOOO0O0OOO0OO0OOO .Bind (wx .EVT_PAINT ,OOOO0O0OOO0OO0OOO .OnPaint )#line:2055
        OOOO0O0OOO0OO0OOO .timer =wx .Timer (OOOO0O0OOO0OO0OOO )#line:2056
        OOOO0O0OOO0OO0OOO .Bind (wx .EVT_TIMER ,OOOO0O0OOO0OO0OOO .OnTimer ,OOOO0O0OOO0OO0OOO .timer )#line:2057
        OOOO0O0OOO0OO0OOO .timer .Start (100 )#line:2058
    def Draw (OO0O00OOOO0O0O0O0 ,OOOOO00OOOOO0O000 ):#line:2060
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2061
        OO000000OOO00000O ="%s:%s:%s"%(11 ,29 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2062
        O000O00OOO0OOOO00 ,OOO000O00OO000O00 =OO0O00OOOO0O0O0O0 .GetClientSize ()#line:2063
        OOOOO00OOOOO0O000 .SetBackground (wx .Brush (OO0O00OOOO0O0O0O0 .GetBackgroundColour ()))#line:2064
        OOOOO00OOOOO0O000 .Clear ()#line:2065
        OOOOO00OOOOO0O000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2066
        OO0O000O00O00O00O ,OOO0O00O00OOO00OO =OOOOO00OOOOO0O000 .GetTextExtent (OO000000OOO00000O )#line:2067
        OOOOO00OOOOO0O000 .DrawText (OO000000OOO00000O ,(O000O00OOO0OOOO00 -OO0O000O00O00O00O )/2 ,(OOO000O00OO000O00 )/2 -OOO0O00O00OOO00OO /2 )#line:2068
    def Modify (O0OOO0OO0000O00O0 ,OOOOO00OOO00O0OO0 ):#line:2070
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O #line:2071
        o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2072
        if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2073
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2074
        OOO0O0OOOOOOO0O0O =int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O )#line:2075
        OOO000OOOO0OOO0O0 ="%s:%s:%s"%(11 ,29 ,OOO0O0OOOOOOO0O0O )#line:2076
        O00O0OOOO0000OO00 ,O000OOOO000000000 =O0OOO0OO0000O00O0 .GetClientSize ()#line:2077
        OOOOO00OOO00O0OO0 .SetBackground (wx .Brush (O0OOO0OO0000O00O0 .GetBackgroundColour ()))#line:2078
        OOOOO00OOO00O0OO0 .Clear ()#line:2079
        OOOOO00OOO00O0OO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:2080
        O00O0OO00O0000OO0 ,OOOO0OOO0O0O00OO0 =OOOOO00OOO00O0OO0 .GetTextExtent (OOO000OOOO0OOO0O0 )#line:2081
        OOOOO00OOO00O0OO0 .DrawText (OOO000OOOO0OOO0O0 ,(O00O0OOOO0000OO00 -O00O0OO00O0000OO0 )/2 ,(O000OOOO000000000 )/2 -OOOO0OOO0O0O00OO0 /2 )#line:2082
    def OnTimer (OO0OO0OO0OO0O0O00 ,OO0O00OO00OOOO000 ):#line:2084
        O0000000O0000O0OO =wx .BufferedDC (wx .ClientDC (OO0OO0OO0OO0O0O00 ))#line:2085
        OO0OO0OO0OO0O0O00 .Modify (O0000000O0000O0OO )#line:2086
    def OnPaint (OO00OOOOOOO000OOO ,OO0O00O0OO0O000OO ):#line:2088
        O000OOOO0OO0OOOO0 =wx .BufferedPaintDC (OO00OOOOOOO000OOO )#line:2089
        OO00OOOOOOO000OOO .Draw (O000OOOO0OO0OOOO0 )#line:2090
class MoniTimeFrame (wx .Frame ):#line:2094
    def __init__ (OO0OO000O00OO0O0O ):#line:2095
        wx .Frame .__init__ (OO0OO000O00OO0O0O ,None ,title ="wx.Timer",size =(200 ,50 ),pos =Pos_timeframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2097
        MoniClockWindow (OO0OO000O00OO0O0O )#line:2100
class PosFrame (wx .Frame ):#line:2105
    def __init__ (O00OOO00000OOOOOO ,O000OO00000OOOOOO ,O0OOOOOO00000OOOO ):#line:2106
        OO0O0000OOO00O000 ,OO000OO00OOO0OO0O =O000OO00000OOOOOO #line:2107
        wx .Frame .__init__ (O00OOO00000OOOOOO ,None ,-1 ,'POS',pos =(OO0O0000OOO00O000 -20 ,OO000OO00OOO0OO0O -10 ),size =(30 ,20 ),style =wx .FRAME_TOOL_WINDOW )#line:2109
        OOOOOOO00000000OO =wx .Panel (O00OOO00000OOOOOO ,-1 ,size =(30 ,20 ))#line:2110
        O0OO00OOO0000O0OO =wx .Font (10 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2112
        OO00O0OO0OOOO0O00 =[]#line:2113
        OO00O0OO0OOOO0O00 .append (wx .StaticText (OOOOOOO00000000OO ,-1 ,O0OOOOOO00000OOOO ,(0 ,0 )))#line:2115
        for O00O0O00000OOOOO0 in range (len (OO00O0OO0OOOO0O00 )):#line:2116
            OO00O0OO0OOOO0O00 [O00O0O00000OOOOO0 ].SetFont (O0OO00OOO0000O0OO )#line:2117
class PriceFrame (wx .Frame ):#line:2119
    def __init__ (O00O0OO00O0O00OOO ,O0O000OOO0O0O0OO0 ):#line:2120
        wx .Frame .__init__ (O00O0OO00O0O00OOO ,None ,-1 ,'Price',size =Pricesize ,pos =Pos_zxco0o0o0o0frame ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2123
        O00O0OO00O0O00OOO .panel =wx .Panel (O00O0OO00O0O00OOO ,size =Pricesize )#line:2124
        wx .StaticBitmap (O00O0OO00O0O00OOO .panel ,-1 ,wx .BitmapFromImage (O0O000OOO0O0O0OO0 ))#line:2126
class YanzhengmaFrame (wx .Frame ):#line:2128
    def __init__ (O0OO0O000OO0000OO ,O0O0OOOO000O0OO00 ):#line:2129
        wx .Frame .__init__ (O0OO0O000OO0000OO ,None ,-1 ,'Price',size =(400 ,80 ),pos =Pos_sdfsnisdfafzxcvframe ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2132
        O0OO0O000OO0000OO .panel =wx .Panel (O0OO0O000OO0000OO ,size =(400 ,80 ))#line:2133
        wx .StaticBitmap (O0OO0O000OO0000OO .panel ,-1 ,wx .BitmapFromImage (O0O0OOOO000O0OO00 ))#line:2135
class AdFrame (wx .Frame ):#line:2139
    def __init__ (OO0O0000O0O000O00 ):#line:2140
        wx .Frame .__init__ (OO0O0000O0O000O00 ,None ,-1 ,"广告",pos =(0 ,250 ),size =(250 ,200 ),style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:2142
        O0000OOO0OO00O000 =wx .Panel (OO0O0000O0O000O00 ,-1 ,size =(250 ,200 ))#line:2143
        O0O0O0O0OOOOOOO0O =wx .Font (20 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2145
        O0OO00OO00OOOO000 =[]#line:2146
        O0OO00OO00OOOO000 .append (wx .StaticText (O0000OOO0OO00O000 ,-1 ," 专业代拍软件",(15 ,10 )))#line:2148
        O0OO00OO00OOOO000 .append (wx .StaticText (O0000OOO0OO00O000 ,-1 ," 专业代拍团队",(15 ,60 )))#line:2150
        O0OO00OO00OOOO000 .append (wx .StaticText (O0000OOO0OO00O000 ,-1 ,"关注微信公众号",(15 ,110 )))#line:2152
        O0OO00OO00OOOO000 .append (wx .StaticText (O0000OOO0OO00O000 ,-1 ," 小鲜肉拍牌",(15 ,160 )))#line:2154
        for OOOO00OOOOO0000OO in range (len (O0OO00OO00OOOO000 )):#line:2155
            O0OO00OO00OOOO000 [OOOO00OOOOO0000OO ].SetFont (O0O0O0O0OOOOOOO0O )#line:2156
class WebFrame (wx .Frame ):#line:2158
    def __init__ (OOOOO0OO00OO0O0OO ,O00O0000OOOOO0O00 ,OO0OOOOOOO0OOOO0O ,O0OOOO0O00O0OOO0O ,O0O00OO00O0000O0O ):#line:2159
        wx .Frame .__init__ (OOOOO0OO00OO0O0OO ,None ,-1 ,O0O00OO00O0000O0O ,size =(websize [0 ],websize [1 ]),pos =(O00O0000OOOOO0O00 ,OO0OOOOOOO0OOOO0O ),style =wx .SIMPLE_BORDER )#line:2160
        if O0OOOO0O00O0OOO0O :#line:2165
            OOOOO0OO00OO0O0OO .adframe =AdFrame ()#line:2166
            OOOOO0OO00OO0O0OO .adframe .Show (True )#line:2167
        OOOOO0OO00OO0O0OO .Bind (wx .EVT_CLOSE ,OOOOO0OO00OO0O0OO .OnClose )#line:2168
        OOOOO0OO00OO0O0OO .ad2 =O0OOOO0O00O0OOO0O #line:2169
        OOOOO0OO00OO0O0OO .control =ControlFrame ()#line:2170
        OOOOO0OO00OO0O0OO .control .Show (True )#line:2171
        pub .subscribe (OOOOO0OO00OO0O0OO .OnClose2 ,"close web")#line:2196
    def OnClose (O000OOOOO0O0OO00O ,O0OOOO0000OOO0OOO ):#line:2197
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2198
        web_on =False #line:2199
        view_time =False #line:2200
        o0sdofsfo0sodf0so0_on =False #line:2201
        ooweo0o0werwr_on =False #line:2202
        TopFrame .Close ()#line:2203
        OOO0OOOOO0O00O000 ="sc_new.png"#line:2204
        if os .path .exists (OOO0OOOOO0O00O000 ):#line:2205
            os .remove (OOO0OOOOO0O00O000 )#line:2206
        O000OOOOO0O0OO00O .Destroy ()#line:2207
        if O000OOOOO0O0OO00O .ad2 :#line:2208
            O000OOOOO0O0OO00O .adframe .Destroy ()#line:2209
        O0OOOO0000OOO0OOO .Skip ()#line:2210
    def OnClose2 (O0O0000OOO0OOOO0O ):#line:2212
        global web_on ,view_time ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on ,ghjo0o0o0o0_repeat #line:2213
        web_on =False #line:2214
        view_time =False #line:2215
        o0sdofsfo0sodf0so0_on =False #line:2216
        ooweo0o0werwr_on =False #line:2217
        TopFrame .Close ()#line:2218
        OOOOO00000O0O0000 ="sc_new.png"#line:2219
        if os .path .exists (OOOOO00000O0O0000 ):#line:2220
            os .remove (OOOOO00000O0O0000 )#line:2221
        O0O0000OOO0OOOO0O .Destroy ()#line:2222
        if O0O0000OOO0OOOO0O .ad2 :#line:2223
            O0O0000OOO0OOOO0O .adframe .Destroy ()#line:2224
class ControlFrame (wx .Frame ):#line:2227
    def __init__ (O00000O00O0OOOOO0 ):#line:2228
        wx .Frame .__init__ (O00000O00O0OOOOO0 ,None ,-1 ,size =(330 ,270 ),style =wx .NO_BORDER |wx .STAY_ON_TOP |wx .FRAME_NO_TASKBAR ,pos =(Px +40 ,Py +480 ))#line:2230
        O00000O00O0OOOOO0 .panel =wx .Panel (O00000O00O0OOOOO0 ,-1 ,size =(330 ,270 ))#line:2231
        O0OO0O0O0O00000O0 =wx .Font (25 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2234
        OO0O00OOOOO00O0O0 =wx .Font (15 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL )#line:2235
        O00000O00O0OOOOO0 .adtext =wx .StaticText (O00000O00O0OOOOO0 .panel ,label =u"小鲜肉代拍",pos =(90 ,20 ))#line:2236
        O00000O00O0OOOOO0 .adtext .SetFont (O0OO0O0O0O00000O0 )#line:2237
        O00000O00O0OOOOO0 .zxco0o0o0o0text =wx .StaticText (O00000O00O0OOOOO0 .panel ,label =u"最低成交价:",pos =(50 ,90 ))#line:2238
        O00000O00O0OOOOO0 .zxco0o0o0o0text .SetFont (OO0O00OOOOO00O0O0 )#line:2239
        O00000O00O0OOOOO0 .zxco0o0o0o0 =wx .StaticText (O00000O00O0OOOOO0 .panel ,pos =(190 ,90 ))#line:2240
        O00000O00O0OOOOO0 .zxco0o0o0o0 .SetFont (OO0O00OOOOO00O0O0 )#line:2241
        O00000O00O0OOOOO0 .timetext =wx .StaticText (O00000O00O0OOOOO0 .panel ,label =u"当前时间:",pos =(50 ,130 ))#line:2242
        O00000O00O0OOOOO0 .timetext .SetFont (OO0O00OOOOO00O0O0 )#line:2243
        O00000O00O0OOOOO0 .time =wx .StaticText (O00000O00O0OOOOO0 .panel ,pos =(190 ,130 ))#line:2244
        O00000O00O0OOOOO0 .time .SetFont (OO0O00OOOOO00O0O0 )#line:2245
        O00000O00O0OOOOO0 .netstattext =wx .StaticText (O00000O00O0OOOOO0 .panel ,pos =(80 ,170 ),label =u"网速")#line:2247
        O00000O00O0OOOOO0 .netstattext .SetFont (OO0O00OOOOO00O0O0 )#line:2248
        O00000O00O0OOOOO0 .netstat =wx .StaticText (O00000O00O0OOOOO0 .panel ,pos =(190 ,170 ))#line:2249
        O00000O00O0OOOOO0 .timetimer1 =wx .Timer (O00000O00O0OOOOO0 )#line:2253
        O00000O00O0OOOOO0 .Bind (wx .EVT_TIMER ,O00000O00O0OOOOO0 .Timego ,O00000O00O0OOOOO0 .timetimer1 )#line:2254
        O00000O00O0OOOOO0 .timetimer1 .Start (100 )#line:2255
    def o_closeweb (O00O0OOO000OOOO00 ,O0OO0O0O00O0O0O0O ):#line:2256
        wx .CallAfter (pub .sendMessage ,"close web")#line:2257
        O00O0OOO000OOOO00 .Destroy ()#line:2258
        O0OO0O0O00O0O0O0O .Skip ()#line:2259
    def Timego (O000OOOO000OOOO00 ,OOOO0OOOO00000000 ):#line:2261
        global O0O0O0O0O0O0O_zxco0o0o0o0 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,a_time #line:2262
        O000OOOO000OOOO00 .zxco0o0o0o0 .SetLabel ("%s"%O0O0O0O0O0O0O_zxco0o0o0o0 )#line:2263
        if o0sdofsfo0sodf0so0_on :#line:2264
            O000OOOO000OOOO00 .time .SetLabel ("11:29:%s"%int (o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:2265
        else :#line:2266
            O0OOOOOOOOO00O00O =time .localtime (a_time )#line:2267
            OOOOOO00O0O0OO00O =time .strftime ("%H:%M:%S",O0OOOOOOOOO00O00O )#line:2268
            O000OOOO000OOOO00 .time .SetLabel (OOOOOO00O0O0OO00O )#line:2269
        global pinger #line:2270
        OO00OO0O0OOO00OOO =pinger .ping ()#line:2271
        if OO00OO0O0OOO00OOO =="timeout":#line:2272
            O000OOOO000OOOO00 .netstat .SetLabel ("%s"%OO00OO0O0OOO00OOO )#line:2273
        else :#line:2274
            O000OOOO000OOOO00 .netstat .SetLabel ("%sms"%OO00OO0O0OOO00OOO )#line:2275
class OperationFrame (wx .Frame ):#line:2278
    def __init__ (OO0O0OOOO0O0OO00O ):#line:2279
        wx .Frame .__init__ (OO0O0OOOO0O0OO00O ,None ,-1 ,title ="小鲜肉代拍",pos =(1070 ,100 ),size =(300 ,425 ),style =wx .FRAME_NO_TASKBAR |wx .CAPTION )#line:2281
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2283
        one_oO0O0O0O0O0O0O0O01 =OO0O0OOOO0O0OO00O .gettime (OO00000o01 )#line:2284
        one_oO0O0O0O0O0O0O0O02 =OO0O0OOOO0O0OO00O .gettime (OO00000o02 )#line:2285
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0O0OOOO0O0OO00O .gettime (ooo0O0o0oO0O_time1 )#line:2286
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0O0OOOO0O0OO00O .gettime (ooo0O0o0oO0O_time2 )#line:2287
        OO0O0OOOO0O0OO00O .timer1 =wx .Timer (OO0O0OOOO0O0OO00O )#line:2289
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TIMER ,OO0O0OOOO0O0OO00O .Price_view ,OO0O0OOOO0O0OO00O .timer1 )#line:2290
        OO0O0OOOO0O0OO00O .timer1 .Start (500 )#line:2291
        OO0O0OOOO0O0OO00O .timer2 =wx .Timer (OO0O0OOOO0O0OO00O )#line:2293
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TIMER ,OO0O0OOOO0O0OO00O .Price_count ,OO0O0OOOO0O0OO00O .timer2 )#line:2294
        OO0O0OOOO0O0OO00O .timer2 .Start (100 )#line:2295
        OO0O0OOOO0O0OO00O .O0O0O0O0O0O0Oframe =Lowestzxco0o0o0o0Frame ()#line:2297
        OO0O0OOOO0O0OO00O .O0O0O0O0O0O0Oframe .Show (False )#line:2298
        OOOOOOOOOOOO000OO =wx .Panel (OO0O0OOOO0O0OO00O ,-1 ,size =(300 ,380 ))#line:2302
        O0000OO0000OO0OO0 =wx .StaticBox (OOOOOOOOOOOO000OO ,-1 ,u'选择策略:')#line:2304
        OO0O0OOOO0O0OO00O .stractagySizer =wx .StaticBoxSizer (O0000OO0000OO0OO0 ,wx .VERTICAL )#line:2305
        O0OOOOO00000000O0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"设定拍牌策略",size =(100 ,50 ))#line:2306
        O0OO000O0OO000000 =wx .BoxSizer (wx .HORIZONTAL )#line:2307
        O0OO000O0OO000000 .Add (O0OOOOO00000000O0 )#line:2308
        OO00000OO00OO000O =[u'单枪策略',u'双枪策略',u'手动操作（热键辅助）']#line:2312
        OO0O0OOOO0O0OO00O .select_stractagy =wx .Choice (OOOOOOOOOOOO000OO ,-1 ,choices =OO00000OO00OO000O ,size =(100 ,50 ))#line:2313
        O0OO000O0OO000000 .Add (OO0O0OOOO0O0OO00O .select_stractagy )#line:2314
        OO0O0OOOO0O0OO00O .select_stractagy .SetSelection (0 )#line:2315
        OO0O0OOOO0O0OO00O .timeview =wx .CheckBox (OOOOOOOOOOOO000OO ,-1 ,label =u'显示时间')#line:2317
        OO0OOOOOOO0O0O0O0 =wx .BoxSizer (wx .HORIZONTAL )#line:2318
        OO0OOOOOOO0O0O0O0 .Add (OO0O0OOOO0O0OO00O .timeview )#line:2319
        OO0O0OOOO0O0OO00O .button1 =wx .Button (OOOOOOOOOOOO000OO ,label ='+1s',size =(35 ,25 ))#line:2322
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Add_ooo0O0o0oO0O ,OO0O0OOOO0O0OO00O .button1 )#line:2323
        OO0O0OOOO0O0OO00O .button2 =wx .Button (OOOOOOOOOOOO000OO ,label ='-1s',size =(35 ,25 ))#line:2324
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Minus_ooo0O0o0oO0O ,OO0O0OOOO0O0OO00O .button2 )#line:2325
        OO0O0OOOO0O0OO00O .button3 =wx .Button (OOOOOOOOOOOO000OO ,label ='+0.1s',size =(35 ,25 ))#line:2326
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Add_time ,OO0O0OOOO0O0OO00O .button3 )#line:2327
        OO0O0OOOO0O0OO00O .button4 =wx .Button (OOOOOOOOOOOO000OO ,label ='-0.1s',size =(35 ,25 ))#line:2328
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Minus_time ,OO0O0OOOO0O0OO00O .button4 )#line:2329
        OO0OOOOOOO0O0O0O0 .Add (OO0O0OOOO0O0OO00O .button1 )#line:2331
        OO0OOOOOOO0O0O0O0 .Add (OO0O0OOOO0O0OO00O .button2 )#line:2332
        OO0OOOOOOO0O0O0O0 .Add (OO0O0OOOO0O0OO00O .button3 )#line:2333
        OO0OOOOOOO0O0O0O0 .Add (OO0O0OOOO0O0OO00O .button4 )#line:2334
        O00O0O0OOO00O00O0 =wx .BoxSizer (wx .VERTICAL )#line:2336
        O00O0O0OOO00O00O0 .Add (O0OO000O0OO000000 )#line:2337
        O00O0O0OOO00O00O0 .Add (OO0OOOOOOO0O0O0O0 )#line:2338
        O0OOOO00O0O0O0OOO =["E键","回车"]#line:2341
        OO0O0OOOO0O0OO00O .sdfsf24324297_choice =wx .Choice (OOOOOOOOOOOO000OO ,-1 ,choices =O0OOOO00O0O0O0OOO )#line:2342
        OO0O0OOOO0O0OO00O .sdfsf24324297_choice .SetSelection (0 )#line:2343
        OO0O0OOOO0O0OO00O .sdfsf24324297_label =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"确认提交方式     ")#line:2344
        O0O0000OOOOO0OO00 =wx .BoxSizer (wx .HORIZONTAL )#line:2345
        O0O0000OOOOO0OO00 .Add (OO0O0OOOO0O0OO00O .sdfsf24324297_label ,flag =wx .TOP ,border =4 )#line:2346
        O0O0000OOOOO0OO00 .Add (OO0O0OOOO0O0OO00O .sdfsf24324297_choice )#line:2347
        O00O0O0OOO00O00O0 .Add (O0O0000OOOOO0OO00 )#line:2348
        OO0O0OOOO0O0OO00O .ghjo0o0o0o0_save =wx .Button (OOOOOOOOOOOO000OO ,label ="保存策略",size =(60 ,35 ))#line:2351
        OO0O0OOOO0O0OO00O .ghjo0o0o0o0_load =wx .Button (OOOOOOOOOOOO000OO ,label ="载入策略",size =(60 ,35 ))#line:2352
        OO0O0OOOO0O0OO00O .save_info =wx .Button (OOOOOOOOOOOO000OO ,label ="用户信息",size =(60 ,35 ))#line:2353
        O0O0OOO0000OOOO0O =wx .BoxSizer (wx .HORIZONTAL )#line:2354
        O0O0OOO0000OOOO0O .Add (OO0O0OOOO0O0OO00O .ghjo0o0o0o0_save )#line:2355
        O0O0OOO0000OOOO0O .Add (OO0O0OOOO0O0OO00O .ghjo0o0o0o0_load )#line:2356
        O0O0OOO0000OOOO0O .Add (OO0O0OOOO0O0OO00O .save_info )#line:2357
        O00O0O0OOO00O00O0 .Add (O0O0OOO0000OOOO0O )#line:2358
        O00O0OO0OO0O0OOOO =wx .StaticBox (OOOOOOOOOOOO000OO ,-1 ,u'单枪策略:')#line:2362
        OO0O0OOOO0O0OO00O .oneshotSizer =wx .StaticBoxSizer (O00O0OO0OO0O0OOOO ,wx .VERTICAL )#line:2363
        OOO000OOOO0OO00OO =wx .GridBagSizer (4 ,4 )#line:2364
        OO0O0OOOO0O0OO00O .jiajia_time =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2365
        OO0O0OOOO0O0OO00O .jiajia_time .SetRange (40 ,55 )#line:2366
        OO0O0OOOO0O0OO00O .jiajia_time .SetValue (48 )#line:2367
        OO0O0OOOO0O0OO00O .jiajia_time .SetIncrement (0.1 )#line:2368
        OOO000OOOO0OO00OO .Add (OO0O0OOOO0O0OO00O .jiajia_time ,pos =(0 ,0 ))#line:2370
        OOOOO0OOO00OOOOO0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2371
        OOO000OOOO0OO00OO .Add (OOOOO0OOO00OOOOO0 ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2372
        O0OO0O0O000OO00OO =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"加价",style =wx .ALIGN_CENTER ,size =(25 ,25 ))#line:2373
        OOO000OOOO0OO00OO .Add (O0OO0O0O000OO00OO ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2374
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2375
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 .SetRange (300 ,1500 )#line:2376
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2377
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 .SetIncrement (100 )#line:2378
        OOO000OOOO0OO00OO .Add (OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 ,pos =(0 ,3 ))#line:2379
        O00O0OOO0OOOO0OOO =[u"提前100",u"提前200",u"踩点"]#line:2382
        OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O0 =wx .Choice (OOOOOOOOOOOO000OO ,-1 ,choices =O00O0OOO0OOOO0OOO ,size =(68 ,25 ))#line:2383
        OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2384
        OOO000OOOO0OO00OO .Add (OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O0 ,pos =(1 ,0 ))#line:2385
        OO0O00O0OOO0OO0O0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"出价提交延迟")#line:2386
        OOO000OOOO0OO00OO .Add (OO0O00O0OOO0OO0O0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2387
        OO0O0OOOO0O0OO00O .yanchi_time =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2388
        OO0O0OOOO0O0OO00O .yanchi_time .SetRange (0.0 ,1.0 )#line:2389
        OO0O0OOOO0O0OO00O .yanchi_time .SetValue (0.5 )#line:2390
        OO0O0OOOO0O0OO00O .yanchi_time .SetIncrement (0.1 )#line:2391
        OOO000OOOO0OO00OO .Add (OO0O0OOOO0O0OO00O .yanchi_time ,pos =(1 ,3 ))#line:2392
        OOOOO00OOOO0OOOO0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2393
        OOO000OOOO0OO00OO .Add (OOOOO00OOOO0OOOO0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2394
        O000O0O0O0000O000 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"强制提交时间")#line:2397
        OOO000OOOO0OO00OO .Add (O000O0O0O0000O000 ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2398
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2399
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time .SetRange (40.0 ,57.0 )#line:2400
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2401
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time .SetIncrement (0.1 )#line:2402
        OOO000OOOO0OO00OO .Add (OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time ,pos =(2 ,1 ))#line:2403
        O0O000000O0OOO000 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2404
        OOO000OOOO0OO00OO .Add (O0O000000O0OOO000 ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2405
        OO0O0OOOO0O0OO00O .oneshotSizer .Add (OOO000OOOO0OO00OO ,0 ,flag =wx .ALL ,border =5 )#line:2407
        OO0OOOO00000OOOOO =wx .StaticBox (OOOOOOOOOOOO000OO ,-1 ,u'双枪策略:')#line:2411
        OO0O0OOOO0O0OO00O .ooo0O0o0oO0OshotSizer =wx .StaticBoxSizer (OO0OOOO00000OOOOO ,wx .VERTICAL )#line:2412
        OOOOO00O000OOO0OO =wx .GridBagSizer (4 ,4 )#line:2413
        OO0O0OOOO0O0OO00O .jiajia_time2 =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2414
        OO0O0OOOO0O0OO00O .jiajia_time2 .SetRange (40 ,55 )#line:2415
        OO0O0OOOO0O0OO00O .jiajia_time2 .SetValue (48 )#line:2416
        OO0O0OOOO0O0OO00O .jiajia_time2 .SetIncrement (0.1 )#line:2417
        OOOOO00O000OOO0OO .Add (OO0O0OOOO0O0OO00O .jiajia_time2 ,pos =(0 ,0 ))#line:2418
        OO0OOOOO0OO000OOO =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2419
        OOOOO00O000OOO0OO .Add (OO0OOOOO0OO000OOO ,pos =(0 ,1 ),flag =wx .TOP |wx .ALIGN_LEFT ,border =4 )#line:2420
        O0OOO0O00O00OO00O =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"加价",size =(25 ,25 ),style =wx .ALIGN_CENTER )#line:2421
        OOOOO00O000OOO0OO .Add (O0OOO0O00O00OO00O ,pos =(0 ,2 ),flag =wx .TOP ,border =4 )#line:2422
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2423
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 .SetRange (300 ,1500 )#line:2424
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 .SetValue (600 )#line:2425
        OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 .SetIncrement (100 )#line:2426
        OOOOO00O000OOO0OO .Add (OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 ,pos =(0 ,3 ))#line:2427
        O00O000O0OO000O0O =[u"提前100",u"提前200",u"踩点"]#line:2429
        OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O02 =wx .Choice (OOOOOOOOOOOO000OO ,-1 ,choices =O00O000O0OO000O0O ,size =(68 ,25 ))#line:2430
        OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2431
        OOOOO00O000OOO0OO .Add (OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O02 ,pos =(1 ,0 ))#line:2432
        OO0O0OO0000O0O0O0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"出价提交延迟")#line:2433
        OOOOO00O000OOO0OO .Add (OO0O0OO0000O0O0O0 ,pos =(1 ,1 ),flag =wx .TOP ,border =4 )#line:2434
        OO0O0OOOO0O0OO00O .yanchi_time2 =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2435
        OO0O0OOOO0O0OO00O .yanchi_time2 .SetRange (0.0 ,1.0 )#line:2436
        OO0O0OOOO0O0OO00O .yanchi_time2 .SetValue (0.5 )#line:2437
        OO0O0OOOO0O0OO00O .yanchi_time2 .SetIncrement (0.1 )#line:2438
        OOOOO00O000OOO0OO .Add (OO0O0OOOO0O0OO00O .yanchi_time2 ,pos =(1 ,3 ))#line:2439
        OO00O000O000OO0O0 =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2440
        OOOOO00O000OOO0OO .Add (OO00O000O000OO0O0 ,pos =(1 ,4 ),flag =wx .TOP ,border =4 )#line:2441
        OOO0OOO00OOOOO00O =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"强制提交时间")#line:2444
        OOOOO00O000OOO0OO .Add (OOO0OOO00OOOOO00O ,pos =(2 ,0 ),flag =wx .TOP ,border =4 )#line:2445
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 =wx .SpinCtrlDouble (OOOOOOOOOOOO000OO ,-1 ,"",size =(68 ,25 ))#line:2446
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 .SetRange (53.0 ,57.0 )#line:2447
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 .SetValue (55.0 )#line:2448
        OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 .SetIncrement (0.1 )#line:2449
        OOOOO00O000OOO0OO .Add (OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 ,pos =(2 ,1 ))#line:2450
        OO0O0O000OOOOO0OO =wx .StaticText (OOOOOOOOOOOO000OO ,label =u"秒")#line:2451
        OOOOO00O000OOO0OO .Add (OO0O0O000OOOOO0OO ,pos =(2 ,2 ),flag =wx .TOP ,border =4 )#line:2452
        OO0O0OOOO0O0OO00O .ooo0O0o0oO0OshotSizer .Add (OOOOO00O000OOO0OO ,0 ,flag =wx .ALL ,border =5 )#line:2454
        OO0O0OOOO0O0OO00O .stractagySizer .Add (O00O0O0OOO00O00O0 ,0 ,wx .ALL |wx .CENTER ,5 )#line:2456
        OO0O0OOOO0O0OO00O .vbox1 =wx .BoxSizer (wx .VERTICAL )#line:2457
        OO00O00OOOO00OO0O =wx .StaticText (OOOOOOOOOOOO000OO ,-1 ,label =u"拍牌功能设置")#line:2460
        O0O000OOO00OO0O00 =wx .StaticText (OOOOOOOOOOOO000OO ,-1 ,label =u"10点半需要进行第一次出价")#line:2461
        O0O000OOO00OO0O00 .SetForegroundColour ('red')#line:2462
        O0O0OOOO0OO00OOOO =wx .StaticLine (OOOOOOOOOOOO000OO ,-1 )#line:2463
        OO0O0OOOO0O0OO00O .vbox1 .Add (OO00O00OOOO00OO0O ,0 ,wx .ALL |wx .LEFT ,10 )#line:2464
        OO0O0OOOO0O0OO00O .vbox1 .Add (O0O000OOO00OO0O00 ,0 ,wx .LEFT ,10 )#line:2465
        OO0O0OOOO0O0OO00O .vbox1 .Add (O0O0OOOO0OO00OOOO ,flag =wx .EXPAND |wx .BOTTOM ,border =10 )#line:2466
        OO0O0OOOO0O0OO00O .vbox1 .Add (OO0O0OOOO0O0OO00O .stractagySizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2467
        OO0O0OOOO0O0OO00O .vbox1 .Add (OO0O0OOOO0O0OO00O .oneshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2468
        OO0O0OOOO0O0OO00O .vbox1 .Add (OO0O0OOOO0O0OO00O .ooo0O0o0oO0OshotSizer ,0 ,wx .ALL |wx .CENTER ,5 )#line:2469
        OOOOOOOOOOOO000OO .SetSizer (OO0O0OOOO0O0OO00O .vbox1 )#line:2470
        OO0O0OOOO0O0OO00O .ooo0O0o0oO0Osizer_Shown =False #line:2473
        OO0O0OOOO0O0OO00O .oneshotsizer_Shown =True #line:2474
        OO0O0OOOO0O0OO00O .vbox1 .Hide (OO0O0OOOO0O0OO00O .ooo0O0o0oO0OshotSizer )#line:2475
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_CHECKBOX ,OO0O0OOOO0O0OO00O .Timeview ,OO0O0OOOO0O0OO00O .timeview )#line:2484
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_CHOICE ,OO0O0OOOO0O0OO00O .Confirmchoice ,OO0O0OOOO0O0OO00O .sdfsf24324297_choice )#line:2485
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Strategy_save ,OO0O0OOOO0O0OO00O .ghjo0o0o0o0_save )#line:2486
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Strategy_load ,OO0O0OOOO0O0OO00O .ghjo0o0o0o0_load )#line:2487
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_BUTTON ,OO0O0OOOO0O0OO00O .Save_info ,OO0O0OOOO0O0OO00O .save_info )#line:2488
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_CHOICE ,OO0O0OOOO0O0OO00O .Refresh_panel ,OO0O0OOOO0O0OO00O .select_stractagy )#line:2490
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Jiajia_time ,OO0O0OOOO0O0OO00O .jiajia_time )#line:2492
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Jiajia_zxco0o0o0o0 ,OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o0 )#line:2494
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_CHOICE ,OO0O0OOOO0O0OO00O .Select_oOO0O0O0O0O0O0 ,OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O0 )#line:2495
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Yanchi_time ,OO0O0OOOO0O0OO00O .yanchi_time )#line:2497
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Tijiao_time ,OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time )#line:2499
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Jiajia_time2 ,OO0O0OOOO0O0OO00O .jiajia_time2 )#line:2502
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Jiajia_zxco0o0o0o02 ,OO0O0OOOO0O0OO00O .jiajia_zxco0o0o0o02 )#line:2504
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_CHOICE ,OO0O0OOOO0O0OO00O .Select_oOO0O0O0O0O0O02 ,OO0O0OOOO0O0OO00O .select_oOO0O0O0O0O0O02 )#line:2505
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Yanchi_time2 ,OO0O0OOOO0O0OO00O .yanchi_time2 )#line:2507
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TEXT ,OO0O0OOOO0O0OO00O .Tijiao_time2 ,OO0O0OOOO0O0OO00O .oOO0O0O0O0O0O0_time2 )#line:2509
        OO0O0OOOO0O0OO00O .timeframe1 =TimeFrame ()#line:2511
        OO0O0OOOO0O0OO00O .timeframe1 .Show (False )#line:2512
        OO0O0OOOO0O0OO00O .timeframe2 =MoniTimeFrame ()#line:2514
        OO0O0OOOO0O0OO00O .timeframe2 .Show (False )#line:2515
        OO0O0OOOO0O0OO00O .operationtimer =wx .Timer (OO0O0OOOO0O0OO00O )#line:2518
        OO0O0OOOO0O0OO00O .Bind (wx .EVT_TIMER ,OO0O0OOOO0O0OO00O .opt ,OO0O0OOOO0O0OO00O .operationtimer )#line:2519
        OO0O0OOOO0O0OO00O .operationtimer .Start (3000 )#line:2520
    def Price_view (O00OO0OO000OOO0OO ,O000OOOO00O000OO0 ):#line:2523
        global zxco0o0o0o0_view ,web_on ,zxco0o0o0o0_on ,view_time #line:2524
        if zxco0o0o0o0_view and zxco0o0o0o0_count >=4 :#line:2526
            try :#line:2527
                O00OO0OO000OOO0OO .Price_close ()#line:2528
            except :#line:2529
                pass #line:2530
            O00OO0OO000OOO0OO .Screen_shot ()#line:2531
            O00OO0O00OO00O0O0 ="sc_new.png"#line:2532
            O00OO0OO000OOO0OO .zxco0o0o0o0frame =PriceFrame (O00OO0O00OO00O0O0 )#line:2533
            O00OO0OO000OOO0OO .zxco0o0o0o0frame .Show (True )#line:2534
            zxco0o0o0o0_view =False #line:2535
            zxco0o0o0o0_on =True #line:2536
    def Price_count (OO00000OOO0O0O0OO ,O0OOO000OO0OO0O00 ):#line:2539
        global zxco0o0o0o0_count #line:2541
        zxco0o0o0o0_count +=1 #line:2542
        O0O0O0O000O00O0O0 ='sc_new.png'#line:2543
        if web_on and ghjo0o0o0o0_on :#line:2544
            OO00000OOO0O0O0OO .O0O0O0O0O0O0Oframe .Show (True )#line:2545
        if not os .path .exists (O0O0O0O000O00O0O0 ):#line:2546
            try :#line:2547
                OO00000OOO0O0O0OO .Price_close ()#line:2548
            except :#line:2549
                pass #line:2550
        if not ghjo0o0o0o0_on or not web_on :#line:2552
            OO00000OOO0O0O0OO .O0O0O0O0O0O0Oframe .Show (False )#line:2553
    def Screen_shot (O00000000OO00O000 ):#line:2558
        global Pricesize #line:2559
        OO00OOOO00OOOOO00 =Pos_zxco0o0o0o0 #line:2560
        OOO000O00O0O0O000 =ImageGrab .grab (OO00OOOO00OOOOO00 )#line:2561
        OOO000O00O0O0O000 .resize (Pricesize ,Image .ANTIALIAS ).save ("sc_new.png")#line:2562
    @staticmethod #line:2565
    def Del_shot ():#line:2566
        try :#line:2567
            os .remove ("sc_new.png")#line:2568
        except :#line:2569
            pass #line:2570
    def Price_close (OO0OOOOOO000000O0 ):#line:2573
        try :#line:2574
            OO0OOOOOO000000O0 .zxco0o0o0o0frame .Destroy ()#line:2575
        except :#line:2576
            pass #line:2577
    def opt (OO000OOO00OO00OOO ,OO00000O0OO0O000O ):#line:2581
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_one ,oo0o0O0O0O0_on #line:2582
        global ghjo0o0o0o0_on #line:2583
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2584
        if OO000OOO00OO00OOO .select_stractagy .GetSelection ==0 :#line:2585
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2586
                twice =False #line:2588
                ghjo0o0o0o0_on =True #line:2589
                oo0o0O0O0O0_on =True #line:2590
                oOO0O0O0O0O0O0_on =False #line:2591
                oOO0O0O0O0O0O0_num =1 #line:2592
                oOO0O0O0O0O0O0_OK =False #line:2593
                oOO0O0O0O0O0O0_one =False #line:2594
        elif OO000OOO00OO00OOO .select_stractagy .GetSelection ==1 :#line:2595
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <OO00000o01 and o0sdofsfo0sodf0so0_on :#line:2596
                ghjo0o0o0o0_on =True #line:2598
                twice =True #line:2599
                oo0o0O0O0O0_on =True #line:2600
                oOO0O0O0O0O0O0_on =False #line:2601
                oOO0O0O0O0O0O0_num =1 #line:2602
                oOO0O0O0O0O0O0_OK =False #line:2603
                oOO0O0O0O0O0O0_one =False #line:2604
    def Add_time (OOO0OO00O0000OO00 ,O000OOOO0OO0O000O ):#line:2608
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2609
        if o0sdofsfo0sodf0so0_on :#line:2610
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=0.1 #line:2611
        else :#line:2612
            a_time +=0.1 #line:2613
    def Minus_time (OOO000OO0OOO0O000 ,O0OO0OOOO00O0O000 ):#line:2615
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2616
        if o0sdofsfo0sodf0so0_on :#line:2617
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=0.1 #line:2618
        else :#line:2619
            a_time -=0.1 #line:2620
    def Add_ooo0O0o0oO0O (O0O000000OOOO00O0 ,O00OOOO00O000O000 ):#line:2622
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2623
        if o0sdofsfo0sodf0so0_on :#line:2624
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O +=1 #line:2625
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=60 :#line:2626
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =0 #line:2627
        else :#line:2628
            a_time +=1 #line:2629
    def Minus_ooo0O0o0oO0O (O0O0OO00000O000OO ,O000O0O00O000O0O0 ):#line:2631
        global a_time ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,o0sdofsfo0sodf0so0_on ,ooweo0o0werwr_on #line:2632
        if o0sdofsfo0sodf0so0_on :#line:2633
            o0sdofsfo0sodf0so0_ooo0O0o0oO0O -=1 #line:2634
            if o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=0 :#line:2635
                o0sdofsfo0sodf0so0_ooo0O0o0oO0O =60 #line:2636
        else :#line:2637
            a_time -=1 #line:2638
    def Timeview (O0OO0OO000OO0OO0O ,OOOO000OOO0O0000O ):#line:2640
        O00O0OOO0O0O0OOOO =OOOO000OOO0O0000O .GetEventObject ()#line:2641
        global view_time ,time_on #line:2642
        if O00O0OOO0O0O0OOOO .IsChecked ():#line:2643
            view_time =True #line:2644
            time_on =True #line:2645
            if ooweo0o0werwr_on :#line:2646
                O0OO0OO000OO0OO0O .timeframe1 .Show (True )#line:2647
            elif o0sdofsfo0sodf0so0_on :#line:2648
                O0OO0OO000OO0OO0O .timeframe2 .Show (True )#line:2649
        else :#line:2650
            view_time =False #line:2651
            time_on =False #line:2652
            if ooweo0o0werwr_on :#line:2653
                O0OO0OO000OO0OO0O .timeframe1 .Show (False )#line:2654
            elif o0sdofsfo0sodf0so0_on :#line:2655
                O0OO0OO000OO0OO0O .timeframe2 .Show (False )#line:2656
    def Opentime (OO0O000O0OOOO0000 ):#line:2658
        if o0sdofsfo0sodf0so0_on :#line:2659
            try :#line:2660
                OO0O000O0OOOO0000 .timeframe2 .Show (True )#line:2661
            except :#line:2662
                pass #line:2663
        elif ooweo0o0werwr_on :#line:2664
            try :#line:2665
                OO0O000O0OOOO0000 .timeframe1 .Show (True )#line:2666
            except :#line:2667
                pass #line:2668
    def Closetime (OOOOO000O00O00O0O ):#line:2671
        try :#line:2672
            OOOOO000O00O00O0O .timeframe1 .Show (False )#line:2673
        except :#line:2674
            pass #line:2675
        try :#line:2676
            OOOOO000O00O00O0O .timeframe2 .Show (False )#line:2677
        except :#line:2678
            pass #line:2679
    def Confirmchoice (O00OO0OOOOO0OO000 ,OO0OOO0O0OOO0O0O0 ):#line:2681
        global e_on ,enter_on #line:2682
        OO00OO0O000000000 =O00OO0OOOOO0OO000 .sdfsf24324297_choice .GetSelection ()#line:2683
        if OO00OO0O000000000 ==0 :#line:2684
            e_on =True #line:2685
            enter_on =False #line:2686
        elif OO00OO0O000000000 ==1 :#line:2687
            e_on =False #line:2688
            enter_on =True #line:2689
    def Jiajia_time (OOO000OOO0O0OOO00 ,O0O0O0OO00O0O000O ):#line:2693
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 #line:2694
        O00O0OO0O0000O0O0 =OOO000OOO0O0OOO00 .jiajia_time .GetValue ()#line:2695
        O0OOO0OOOOO00O00O =[40 +O00O0O00000OOO0OO *0.1 for O00O0O00000OOO0OO in range (151 )]#line:2696
        if O00O0OO0O0000O0O0 in O0OOO0OOOOO00O00O :#line:2697
            OO00000o01 =O00O0OO0O0000O0O0 #line:2698
            OO00000o01 =float (OO00000o01 )#line:2699
            one_oO0O0O0O0O0O0O0O01 =OOO000OOO0O0OOO00 .gettime (OO00000o01 )#line:2700
        else :#line:2701
            OOO000OOO0O0OOO00 .jiajia_time .SetValue (OO00000o01 )#line:2702
    def Jiajia_zxco0o0o0o0 (OOO000O0OOOO0000O ,O00O000OOOO0000O0 ):#line:2705
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2706
        OOO0OOOO0OO00OO0O =[300 +O0O00000OO0OOO0O0 *100 for O0O00000OO0OOO0O0 in range (13 )]#line:2707
        OO0OO0OO0O0OOO000 =OOO000O0OOOO0000O .jiajia_zxco0o0o0o0 .GetValue ()#line:2708
        if OO0OO0OO0O0OOO000 in OOO0OOOO0OO00OO0O :#line:2709
            one_diff =int (OO0OO0OO0O0OOO000 )#line:2710
        else :#line:2711
            OOO000O0OOOO0000O .jiajia_zxco0o0o0o0 .SetValue (one_diff )#line:2712
    def Select_oOO0O0O0O0O0O0 (O0O0OOO000OO00OO0 ,OO00000O00OOO0O0O ):#line:2715
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2716
        OO0OO0000000O0OO0 =O0O0OOO000OO00OO0 .select_oOO0O0O0O0O0O0 .GetString (O0O0OOO000OO00OO0 .select_oOO0O0O0O0O0O0 .GetSelection ())#line:2717
        if OO0OO0000000O0OO0 ==u"提前100":#line:2718
            one_advance =100 #line:2719
        elif OO0OO0000000O0OO0 ==u"提前200":#line:2720
            one_advance =200 #line:2721
        else :#line:2722
            one_advance =0 #line:2723
    def Yanchi_time (OOO00O0OO00O0O0OO ,OO0OO0O00OOO0OO00 ):#line:2725
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2726
        OO00O000OOO0O0000 =['0.%d'%OOOO0OOOOO0O000OO for OOOO0OOOOO0O000OO in range (11 )]#line:2727
        OO00O000OOO0O0000 .append ('1.0')#line:2728
        O00OOO0O0O00OO0O0 =str (OOO00O0OO00O0O0OO .yanchi_time .GetValue ())#line:2729
        if O00OOO0O0O00OO0O0 in OO00O000OOO0O0000 :#line:2730
            one_delay =float (O00OOO0O0O00OO0O0 )#line:2731
        else :#line:2732
            OOO00O0OO00O0O0OO .yanchi_time .SetValue (one_delay )#line:2733
    def Tijiao_time (OO0O0000OOOOOO0OO ,O0O00O0OOO0O0000O ):#line:2735
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 ,one_oO0O0O0O0O0O0O0O02 #line:2736
        OO00O0O00O00OOOO0 =OO0O0000OOOOOO0OO .oOO0O0O0O0O0O0_time .GetValue ()#line:2737
        OO0000OOO0OOOO0OO =[40 +O000O0O000OOO0000 *0.1 for O000O0O000OOO0000 in range (171 )]#line:2738
        if OO00O0O00O00OOOO0 in OO0000OOO0OOOO0OO :#line:2739
            OO00000o02 =float (OO00O0O00O00OOOO0 )#line:2740
            one_oO0O0O0O0O0O0O0O02 =OO0O0000OOOOOO0OO .gettime (OO00000o02 )#line:2741
        else :#line:2742
            OO0O0000OOOOOO0OO .oOO0O0O0O0O0O0_time .SetValue (OO00000o02 )#line:2743
    def Jiajia_time2 (OO0OO0O0O0O000O00 ,OOOO0OOO00O00O0OO ):#line:2745
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 #line:2746
        OO00OOOO0O0O00OOO =OO0OO0O0O0O000O00 .jiajia_time2 .GetValue ()#line:2747
        O0000OOO0O00OO00O =[40 +O00O0000000OO00OO *0.1 for O00O0000000OO00OO in range (151 )]#line:2748
        if OO00OOOO0O0O00OOO in O0000OOO0O00OO00O :#line:2749
            ooo0O0o0oO0O_time1 =float (OO00OOOO0O0O00OOO )#line:2750
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0OO0O0O0O000O00 .gettime (ooo0O0o0oO0O_time1 )#line:2751
        else :#line:2752
            OO0OO0O0O0O000O00 .jiajia_time2 .SetValue (ooo0O0o0oO0O_time1 )#line:2753
    def Jiajia_zxco0o0o0o02 (O0O000OO000OOOOO0 ,O0O0000OO0000O0O0 ):#line:2755
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2756
        global one_advance ,one_delay ,one_diff ,OO00000o01 ,OO00000o02 #line:2757
        O00OO00OOOO00O000 =[300 +OOOO0O0O00OO0OOOO *100 for OOOO0O0O00OO0OOOO in range (13 )]#line:2758
        OO0000O0O00O0O000 =O0O000OO000OOOOO0 .jiajia_zxco0o0o0o02 .GetValue ()#line:2759
        if OO0000O0O00O0O000 in O00OO00OOOO00O000 :#line:2760
            ooo0O0o0oO0O_diff =int (OO0000O0O00O0O000 )#line:2761
        else :#line:2762
            O0O000OO000OOOOO0 .jiajia_zxco0o0o0o02 .SetValue (ooo0O0o0oO0O_diff )#line:2763
    def Select_oOO0O0O0O0O0O02 (O0O0O0OOOO00OOOO0 ,O00OO0000000O0OO0 ):#line:2765
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2766
        OOO0OOO00O000000O =O0O0O0OOOO00OOOO0 .select_oOO0O0O0O0O0O02 .GetString (O0O0O0OOOO00OOOO0 .select_oOO0O0O0O0O0O02 .GetSelection ())#line:2767
        if OOO0OOO00O000000O ==u"提前100":#line:2768
            ooo0O0o0oO0O_advance =100 #line:2769
        elif OOO0OOO00O000000O ==u"提前200":#line:2770
            ooo0O0o0oO0O_advance =200 #line:2771
        else :#line:2772
            ooo0O0o0oO0O_advance =0 #line:2773
    def Yanchi_time2 (OOO00O0OOOO0OOOO0 ,O0O0OO000O000O000 ):#line:2776
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 #line:2777
        O0O0O0O000OO000OO =['0.%d'%O0OO000OO0OOOOOO0 for O0OO000OO0OOOOOO0 in range (11 )]#line:2778
        O0O0O0O000OO000OO .append ('1.0')#line:2779
        O0O0O0OO0OO0000O0 =str (OOO00O0OOOO0OOOO0 .yanchi_time2 .GetValue ())#line:2780
        if O0O0O0OO0OO0000O0 in O0O0O0O000OO000OO :#line:2781
            ooo0O0o0oO0O_delay =float (O0O0O0OO0OO0000O0 )#line:2782
        else :#line:2783
            OOO00O0OOOO0OOOO0 .yanchi_time2 .SetValue (ooo0O0o0oO0O_delay )#line:2784
    def Tijiao_time2 (OOO000OOO0OO00O0O ,OOO0OO0O00OOO0O0O ):#line:2787
        global ooo0O0o0oO0O_advance ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2788
        O00OOO00000O0000O =OOO000OOO0OO00O0O .oOO0O0O0O0O0O0_time2 .GetValue ()#line:2789
        OO0O0O0OO00O00OOO =[53 +OOO00O00O0OO00OO0 *0.1 for OOO00O00O0OO00OO0 in range (41 )]#line:2790
        if O00OOO00000O0000O in OO0O0O0OO00O00OOO :#line:2791
            ooo0O0o0oO0O_time2 =float (O00OOO00000O0000O )#line:2792
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OOO000OOO0OO00O0O .gettime (ooo0O0o0oO0O_time2 )#line:2793
        else :#line:2794
            OOO000OOO0OO00O0O .oOO0O0O0O0O0O0_time2 .SetValue (ooo0O0o0oO0O_time2 )#line:2795
    def Refresh_panel (O00O00O000O00000O ,O0O00O000OO0O00O0 ):#line:2799
        global ghjo0o0o0o0_on #line:2801
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:2802
        O00OOOOOO0000000O =O00O00O000O00000O .select_stractagy .GetString (O00O00O000O00000O .select_stractagy .GetSelection ())#line:2803
        if O00OOOOOO0000000O ==u"单枪策略":#line:2804
            O00O00O000O00000O .ss_Hide ()#line:2805
            twice =False #line:2806
            ghjo0o0o0o0_on =True #line:2807
            oo0o0O0O0O0_on =True #line:2808
            oOO0O0O0O0O0O0_on =False #line:2809
            oOO0O0O0O0O0O0_num =1 #line:2810
            oOO0O0O0O0O0O0_OK =False #line:2811
            oOO0O0O0O0O0O0_one =False #line:2812
        elif O00OOOOOO0000000O ==u"双枪策略":#line:2814
            O00O00O000O00000O .ss_Shown ()#line:2815
            ghjo0o0o0o0_on =True #line:2816
            twice =True #line:2817
            oo0o0O0O0O0_on =True #line:2818
            oOO0O0O0O0O0O0_on =False #line:2819
            oOO0O0O0O0O0O0_num =1 #line:2820
            oOO0O0O0O0O0O0_OK =False #line:2821
            oOO0O0O0O0O0O0_one =False #line:2822
        else :#line:2823
            O00O00O000O00000O .none_show ()#line:2824
            ghjo0o0o0o0_on =False #line:2825
            twice =False #line:2826
    def ss_Shown (O00O00O0O000O0OO0 ):#line:2829
        if not O00O00O0O000O0OO0 .ooo0O0o0oO0Osizer_Shown :#line:2830
            O00O00O0O000O0OO0 .vbox1 .Show (O00O00O0O000O0OO0 .ooo0O0o0oO0OshotSizer )#line:2831
            O00O00O0O000O0OO0 .ooo0O0o0oO0Osizer_Shown =True #line:2832
        if not O00O00O0O000O0OO0 .oneshotsizer_Shown :#line:2833
            O00O00O0O000O0OO0 .vbox1 .Show (O00O00O0O000O0OO0 .oneshotSizer )#line:2834
            O00O00O0O000O0OO0 .oneshotsizer_Shown =True #line:2835
        O00O00O0O000O0OO0 .ooo0O0o0oO0Osizer_Shown =True #line:2836
        O00O00O0O000O0OO0 .oneshotSizer_Shown =True #line:2837
        O00O00O0O000O0OO0 .SetClientSize ((280 ,575 ))#line:2838
        O00O00O0O000O0OO0 .Secondshot_reset ()#line:2839
        O00O00O0O000O0OO0 .Layout ()#line:2840
    def ss_Hide (OOO0O0O000O000O0O ):#line:2842
        if OOO0O0O000O000O0O .ooo0O0o0oO0Osizer_Shown :#line:2843
            OOO0O0O000O000O0O .vbox1 .Hide (OOO0O0O000O000O0O .ooo0O0o0oO0OshotSizer )#line:2844
        if not OOO0O0O000O000O0O .oneshotsizer_Shown :#line:2847
            OOO0O0O000O000O0O .vbox1 .Show (OOO0O0O000O000O0O .oneshotSizer )#line:2848
        OOO0O0O000O000O0O .ooo0O0o0oO0Osizer_Shown =False #line:2849
        OOO0O0O000O000O0O .oneshotSizer_Shown =True #line:2850
        OOO0O0O000O000O0O .SetClientSize ((280 ,375 ))#line:2851
        OOO0O0O000O000O0O .Oneshot_reset ()#line:2852
        OOO0O0O000O000O0O .Layout ()#line:2853
    def none_show (O00O0O0O0OOOO0OOO ):#line:2855
        if O00O0O0O0OOOO0OOO .oneshotsizer_Shown :#line:2856
            O00O0O0O0OOOO0OOO .vbox1 .Hide (O00O0O0O0OOOO0OOO .ooo0O0o0oO0OshotSizer )#line:2857
        if O00O0O0O0OOOO0OOO .ooo0O0o0oO0Osizer_Shown :#line:2858
            O00O0O0O0OOOO0OOO .vbox1 .Hide (O00O0O0O0OOOO0OOO .oneshotSizer )#line:2859
        O00O0O0O0OOOO0OOO .oneshotsizer_Shown =False #line:2861
        O00O0O0O0OOOO0OOO .ooo0O0o0oO0Osizer_Shown =False #line:2862
        O00O0O0O0OOOO0OOO .SetClientSize ((280 ,255 ))#line:2863
        O00O0O0O0OOOO0OOO .Layout ()#line:2864
    def Oneshot_reset (OO000OO0O00O0O00O ):#line:2866
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2867
        OO000OO0O00O0O00O .jiajia_time .SetValue (48.0 )#line:2868
        OO000OO0O00O0O00O .oOO0O0O0O0O0O0_time .SetValue (55.0 )#line:2869
        OO000OO0O00O0O00O .jiajia_zxco0o0o0o0 .SetValue (700 )#line:2870
        OO000OO0O00O0O00O .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:2871
        OO000OO0O00O0O00O .yanchi_time .SetValue (0.5 )#line:2872
        OO00000o01 =48 #line:2874
        OO00000o02 =55 #line:2875
        one_diff =700 #line:2876
        one_delay =0.5 #line:2877
        one_advance =100 #line:2878
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2880
        one_oO0O0O0O0O0O0O0O01 =OO000OO0O00O0O00O .gettime (OO00000o01 )#line:2881
        one_oO0O0O0O0O0O0O0O02 =OO000OO0O00O0O00O .gettime (OO00000o02 )#line:2882
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO000OO0O00O0O00O .gettime (ooo0O0o0oO0O_time1 )#line:2883
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO000OO0O00O0O00O .gettime (ooo0O0o0oO0O_time2 )#line:2884
    def Secondshot_reset (OO0000OOOOOO000O0 ):#line:2887
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2888
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2889
        OO0000OOOOOO000O0 .jiajia_time .SetValue (40.0 )#line:2890
        OO0000OOOOOO000O0 .oOO0O0O0O0O0O0_time .SetValue (48.0 )#line:2891
        OO0000OOOOOO000O0 .jiajia_zxco0o0o0o0 .SetValue (500 )#line:2892
        OO0000OOOOOO000O0 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:2893
        OO0000OOOOOO000O0 .yanchi_time .SetValue (0.0 )#line:2894
        OO0000OOOOOO000O0 .jiajia_time2 .SetValue (50.0 )#line:2896
        OO0000OOOOOO000O0 .oOO0O0O0O0O0O0_time2 .SetValue (55.5 )#line:2897
        OO0000OOOOOO000O0 .jiajia_zxco0o0o0o02 .SetValue (700 )#line:2898
        OO0000OOOOOO000O0 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:2899
        OO0000OOOOOO000O0 .yanchi_time2 .SetValue (0.5 )#line:2900
        OO00000o01 =40 #line:2902
        OO00000o02 =48 #line:2903
        one_diff =500 #line:2904
        one_delay =0.5 #line:2905
        one_advance =100 #line:2906
        ooo0O0o0oO0O_time1 =50 #line:2908
        ooo0O0o0oO0O_time2 =55.5 #line:2909
        ooo0O0o0oO0O_diff =700 #line:2910
        ooo0O0o0oO0O_delay =0.5 #line:2911
        ooo0O0o0oO0O_advance =100 #line:2912
        global one_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:2914
        one_oO0O0O0O0O0O0O0O01 =OO0000OOOOOO000O0 .gettime (OO00000o01 )#line:2915
        one_oO0O0O0O0O0O0O0O02 =OO0000OOOOOO000O0 .gettime (OO00000o02 )#line:2916
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =OO0000OOOOOO000O0 .gettime (ooo0O0o0oO0O_time1 )#line:2917
        ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =OO0000OOOOOO000O0 .gettime (ooo0O0o0oO0O_time2 )#line:2918
    def Strategy_save (OOOOO0O0OOO00O00O ,O0O0OOO0000OOOO00 ):#line:2921
        OOO0OOO000OO0OO00 =wx .TextEntryDialog (None ,'设定你的策略名称:',"策略保存","策略1",style =wx .OK )#line:2923
        if OOO0OOO000OO0OO00 .ShowModal ()==wx .ID_OK :#line:2924
            O00O000OO0O000O0O =OOO0OOO000OO0OO00 .GetValue ()#line:2925
            if O00O000OO0O000O0O :#line:2926
                O0OO00O000OOO00OO =wx .MessageBox ('保存成功','策略保存',wx .OK |wx .ICON_INFORMATION )#line:2927
                if O0OO00O000OOO00OO ==wx .ID_OK :#line:2928
                    O0OO00O000OOO00OO .Destroy ()#line:2929
                    OOO0OOO000OO0OO00 .Destroy ()#line:2930
                OOOOO0O0OOO00O00O .save (O00O000OO0O000O0O )#line:2931
            else :#line:2932
                O0OO00O000OOO00OO =wx .MessageBox ('名称不能为空','策略保存',wx .OK |wx .ICON_ERROR )#line:2933
                if O0OO00O000OOO00OO ==wx .ID_OK :#line:2934
                    O0OO00O000OOO00OO .Destroy ()#line:2935
                    OOO0OOO000OO0OO00 .Destroy ()#line:2936
    def save (OO0OOO0O0O00O0O00 ,OOO00OO0OO0O0O0O0 ):#line:2938
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:2939
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:2940
        global osl ,e_on ,enter_on #line:2941
        if OO0OOO0O0O00O0O00 .select_stractagy .GetSelection ()==2 :#line:2943
            OO0OOOO0O0O0OOOOO =wx .MessageBox ('请先制定一个策略','策略保存',wx .OK |wx .ICON_ERROR )#line:2944
            if OO0OOOO0O0O0OOOOO ==wx .ID_OK :#line:2945
                OO0OOOO0O0O0OOOOO .Destroy ()#line:2946
        elif OO0OOO0O0O00O0O00 .select_stractagy .GetSelection ()==0 :#line:2947
            osl [0 ]=0 #line:2948
            osl [1 ]=OO00000o01 #line:2949
            osl [2 ]=OO00000o02 #line:2950
            osl [3 ]=one_diff #line:2951
            osl [4 ]=one_delay #line:2952
            osl [5 ]=one_advance #line:2953
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2954
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2955
            osl [8 ]=ooo0O0o0oO0O_diff #line:2956
            osl [9 ]=ooo0O0o0oO0O_delay #line:2957
            osl [10 ]=ooo0O0o0oO0O_advance #line:2958
            osl [11 ]=e_on #line:2959
            osl [12 ]=enter_on #line:2960
        elif OO0OOO0O0O00O0O00 .select_stractagy .GetSelection ()==1 :#line:2961
            osl [0 ]=1 #line:2962
            osl [0 ]=1 #line:2963
            osl [1 ]=OO00000o01 #line:2964
            osl [2 ]=OO00000o02 #line:2965
            osl [3 ]=one_diff #line:2966
            osl [4 ]=one_delay #line:2967
            osl [5 ]=one_advance #line:2968
            osl [6 ]=ooo0O0o0oO0O_time1 #line:2969
            osl [7 ]=ooo0O0o0oO0O_time2 #line:2970
            osl [8 ]=ooo0O0o0oO0O_diff #line:2971
            osl [9 ]=ooo0O0o0oO0O_delay #line:2972
            osl [10 ]=ooo0O0o0oO0O_advance #line:2973
            osl [11 ]=e_on #line:2974
            osl [12 ]=enter_on #line:2975
        with open ('%s.ghjo0o0o0o0'%OOO00OO0OO0O0O0O0 ,'wb')as O000O00O0OO0OO0OO :#line:2976
            pickle .dump (osl ,O000O00O0OO0OO0OO )#line:2977
    def Strategy_load (OO00000O0O0O0OO0O ,O0O0O00O0O0O00O0O ):#line:2992
        import os as OOO00O00OO0000O00 #line:2993
        O0OO0000OO0OOO00O =OOO00O00OO0000O00 .getcwd ()#line:2994
        O00O00OO0OOO0OO00 =OO00000O0O0O0OO0O .findfiles (O0OO0000OO0OOO00O )#line:2995
        if O00O00OO0OOO0OO00 :#line:2996
            OO0O0O0OO00OOO0O0 =wx .SingleChoiceDialog (None ,u"请选择策略:",u"策略载入",choices =O00O00OO0OOO0OO00 )#line:2998
            if OO0O0O0OO00OOO0O0 .ShowModal ()==wx .ID_OK :#line:2999
                O0OO0000OO0OOO00O =OO0O0O0OO00OOO0O0 .GetStringSelection ()#line:3000
                O00O0000OO0O000O0 =wx .MessageDialog (None ,"载入成功",u"载入策略",wx .OK |wx .ICON_INFORMATION )#line:3001
                if O00O0000OO0O000O0 .ShowModal ()==wx .ID_OK :#line:3002
                    O00O0000OO0O000O0 .Destroy ()#line:3003
                OO00000O0O0O0OO0O .load (O0OO0000OO0OOO00O )#line:3004
            OO0O0O0OO00OOO0O0 .Destroy ()#line:3006
        else :#line:3007
            O00O0000OO0O000O0 =wx .MessageBox ('找不到任何保存的策略','策略载入',wx .OK |wx .ICON_ERROR )#line:3008
            if O00O0000OO0O000O0 ==wx .ID_OK :#line:3009
                O00O0000OO0O000O0 .Destroy ()#line:3010
                OO0O0O0OO00OOO0O0 .Destroy ()#line:3011
    def load (O00OOOO00000O0000 ,OO00000OO00O0OO00 ):#line:3013
        global osl ,e_on ,enter_on #line:3014
        global OO00000o01 ,OO00000o02 ,one_diff ,one_delay ,one_advance #line:3015
        global ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_time2 ,ooo0O0o0oO0O_diff ,ooo0O0o0oO0O_delay ,ooo0O0o0oO0O_advance #line:3016
        global ghjo0o0o0o0_on #line:3018
        global twice ,oOO0O0O0O0O0O0_num ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,oOO0O0O0O0O0O0_one #line:3019
        global one_oO0O0O0O0O0O0O0O01 ,one_oO0O0O0O0O0O0O0O02 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3020
        try :#line:3021
            with open (OO00000OO00O0OO00 ,'rb')as OOO00O0O0OO00OO00 :#line:3022
                osl =pickle .load (OOO00O0O0OO00OO00 )#line:3023
        except :#line:3024
            pass #line:3025
        if osl [0 ]==0 :#line:3026
            O00OOOO00000O0000 .ss_Hide ()#line:3027
            twice =False #line:3030
            ghjo0o0o0o0_on =True #line:3031
            oo0o0O0O0O0_on =True #line:3032
            oOO0O0O0O0O0O0_on =False #line:3033
            oOO0O0O0O0O0O0_num =1 #line:3034
            oOO0O0O0O0O0O0_OK =False #line:3035
            oOO0O0O0O0O0O0_one =False #line:3036
            O00OOOO00000O0000 .select_stractagy .SetSelection (0 )#line:3038
            O00OOOO00000O0000 .jiajia_time .SetValue (osl [1 ])#line:3039
            O00OOOO00000O0000 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3040
            O00OOOO00000O0000 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3041
            O00OOOO00000O0000 .yanchi_time .SetValue (osl [4 ])#line:3042
            if osl [5 ]==100 :#line:3043
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3044
            elif osl [5 ]==200 :#line:3045
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3046
            else :#line:3047
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3048
            OO00000o01 =osl [1 ]#line:3050
            OO00000o02 =osl [2 ]#line:3051
            one_diff =osl [3 ]#line:3052
            one_delay =osl [4 ]#line:3053
            one_advance =osl [5 ]#line:3054
            e_on =osl [11 ]#line:3056
            enter_on =osl [12 ]#line:3057
            if e_on :#line:3058
                O00OOOO00000O0000 .sdfsf24324297_choice .SetSelection (0 )#line:3059
            elif enter_on :#line:3060
                O00OOOO00000O0000 .sdfsf24324297_choice .SetSelection (1 )#line:3061
            one_oO0O0O0O0O0O0O0O01 =O00OOOO00000O0000 .gettime (OO00000o01 )#line:3063
            one_oO0O0O0O0O0O0O0O02 =O00OOOO00000O0000 .gettime (OO00000o02 )#line:3064
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00OOOO00000O0000 .gettime (ooo0O0o0oO0O_time1 )#line:3065
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00OOOO00000O0000 .gettime (ooo0O0o0oO0O_time2 )#line:3066
        elif osl [0 ]==1 :#line:3068
            ghjo0o0o0o0_on =True #line:3069
            twice =True #line:3070
            oo0o0O0O0O0_on =True #line:3071
            oOO0O0O0O0O0O0_on =False #line:3072
            oOO0O0O0O0O0O0_num =1 #line:3073
            oOO0O0O0O0O0O0_OK =False #line:3074
            oOO0O0O0O0O0O0_one =False #line:3075
            O00OOOO00000O0000 .ss_Shown ()#line:3076
            O00OOOO00000O0000 .select_stractagy .SetSelection (1 )#line:3077
            O00OOOO00000O0000 .jiajia_time .SetValue (osl [1 ])#line:3078
            O00OOOO00000O0000 .oOO0O0O0O0O0O0_time .SetValue (osl [2 ])#line:3079
            O00OOOO00000O0000 .jiajia_zxco0o0o0o0 .SetValue (osl [3 ])#line:3080
            O00OOOO00000O0000 .yanchi_time .SetValue (osl [4 ])#line:3081
            if osl [5 ]==100 :#line:3082
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (0 )#line:3083
            elif osl [5 ]==200 :#line:3084
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (1 )#line:3085
            else :#line:3086
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O0 .SetSelection (2 )#line:3087
            O00OOOO00000O0000 .jiajia_time2 .SetValue (osl [6 ])#line:3088
            O00OOOO00000O0000 .oOO0O0O0O0O0O0_time2 .SetValue (osl [7 ])#line:3089
            O00OOOO00000O0000 .jiajia_zxco0o0o0o02 .SetValue (osl [8 ])#line:3090
            O00OOOO00000O0000 .yanchi_time2 .SetValue (osl [9 ])#line:3091
            if osl [10 ]==100 :#line:3092
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O02 .SetSelection (0 )#line:3093
            elif osl [10 ]==200 :#line:3094
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O02 .SetSelection (1 )#line:3095
            else :#line:3096
                O00OOOO00000O0000 .select_oOO0O0O0O0O0O02 .SetSelection (2 )#line:3097
            OO00000o01 =osl [1 ]#line:3100
            OO00000o02 =osl [2 ]#line:3101
            one_diff =osl [3 ]#line:3102
            one_delay =osl [4 ]#line:3103
            one_advance =osl [5 ]#line:3104
            ooo0O0o0oO0O_time1 =osl [6 ]#line:3106
            ooo0O0o0oO0O_time2 =osl [7 ]#line:3107
            ooo0O0o0oO0O_diff =osl [8 ]#line:3108
            ooo0O0o0oO0O_delay =osl [9 ]#line:3109
            ooo0O0o0oO0O_advance =osl [10 ]#line:3110
            e_on =osl [11 ]#line:3112
            enter_on =osl [12 ]#line:3113
            if e_on :#line:3114
                O00OOOO00000O0000 .sdfsf24324297_choice .SetSelection (0 )#line:3115
            elif enter_on :#line:3116
                O00OOOO00000O0000 .sdfsf24324297_choice .SetSelection (1 )#line:3117
            one_oO0O0O0O0O0O0O0O01 =O00OOOO00000O0000 .gettime (OO00000o01 )#line:3119
            one_oO0O0O0O0O0O0O0O02 =O00OOOO00000O0000 .gettime (OO00000o02 )#line:3120
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 =O00OOOO00000O0000 .gettime (ooo0O0o0oO0O_time1 )#line:3121
            ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 =O00OOOO00000O0000 .gettime (ooo0O0o0oO0O_time2 )#line:3122
    def findfiles (O0OO000OOOO000O0O ,OO0OO0O0OOOO00O0O ):#line:3124
        OO00O0O0O0OOOO00O =[]#line:3125
        for O00OO0O0O00OOOO0O ,OOOO00O00OOO0O000 ,O00O00O00OOO00OOO in os .walk (OO0OO0O0OOOO00O0O ):#line:3126
            for O0O0O000O0OOO00O0 in O00O00O00OOO00OOO :#line:3127
                if os .path .splitext (O0O0O000O0OOO00O0 )[1 ]=='.ghjo0o0o0o0':#line:3128
                    OO00O0O0O0OOOO00O .append (os .path .join (O00OO0O0O00OOOO0O ,O0O0O000O0OOO00O0 ))#line:3129
        return OO00O0O0O0OOOO00O #line:3130
    def Save_info (O0OOOOOO0O00OO00O ,O0OO0OO0O00O0OOO0 ):#line:3132
        pass #line:3133
    def changetime (O0O00O00000O0OOOO ,O00000OOOO00O0OOO ):#line:3138
        O0O0OO00O00000OOO =time .mktime (time .strptime (O00000OOOO00O0OOO ,'%Y-%m-%d %H:%M:%S'))#line:3139
        return O0O0OO00O00000OOO #line:3140
    def get_nowtime (O0O00O0O0OO0OO0OO ):#line:3143
        O0O00OOO00OOOOOOO =time .time ()#line:3144
        O0OO0000OOOOO00OO =time .strftime ('%Y-%m-%d',time .localtime (O0O00OOO00OOOOOOO ))#line:3145
        return O0OO0000OOOOO00OO #line:3146
    def gettime (O00O0O000OO00O000 ,O00OO0OO00O0OOOO0 ):#line:3149
        O00O0O0O0OOOOO0OO =O00O0O000OO00O000 .get_nowtime ()#line:3150
        O000OO00O000O00OO =O00O0O0O0OOOOO0OO +' 11:29:'+str (int (O00OO0OO00O0OOOO0 ))#line:3151
        OOO0OOO0O00OOOO0O =O00O0O000OO00O000 .changetime (O000OO00O000O00OO )+float (O00OO0OO00O0OOOO0 )-int (O00OO0OO00O0OOOO0 )#line:3152
        return OOO0OOO0O00OOOO0O #line:3153
class Lowestzxco0o0o0o0Window (wx .Panel ):#line:3156
    def __init__ (O0OOO00OO00O0OO0O ,OO0O0O0O0OO0OO00O ):#line:3157
        wx .Window .__init__ (O0OOO00OO00O0OO0O ,OO0O0O0O0OO0OO00O ,size =Timesize )#line:3158
        O0OOO00OO00O0OO0O .Bind (wx .EVT_PAINT ,O0OOO00OO00O0OO0O .OnPaint )#line:3159
        O0OOO00OO00O0OO0O .timer =wx .Timer (O0OOO00OO00O0OO0O )#line:3160
        O0OOO00OO00O0OO0O .Bind (wx .EVT_TIMER ,O0OOO00OO00O0OO0O .OnTimer ,O0OOO00OO00O0OO0O .timer )#line:3161
        O0OOO00OO00O0OO0O .timer .Start (100 )#line:3162
    def Draw (O00OOOOOO000000O0 ,O0O00OO0O0OOOO000 ):#line:3164
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3165
        OOO0O0000OO0O0OOO =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3166
        O000OO00000000OO0 ,OO000OOO0OOO0OO0O =O00OOOOOO000000O0 .GetClientSize ()#line:3167
        O0O00OO0O0OOOO000 .SetBackground (wx .Brush (O00OOOOOO000000O0 .GetBackgroundColour ()))#line:3168
        O0O00OO0O0OOOO000 .Clear ()#line:3169
        O0O00OO0O0OOOO000 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3170
        O00000000OO0OO0O0 ,OO0OOOO0OOO0O000O =O0O00OO0O0OOOO000 .GetTextExtent (OOO0O0000OO0O0OOO )#line:3171
        O0O00OO0O0OOOO000 .DrawText (OOO0O0000OO0O0OOO ,(O000OO00000000OO0 -O00000000OO0OO0O0 )/2 ,(OO000OOO0OOO0OO0O )/2 -OO0OOOO0OOO0O000O /2 )#line:3172
    def Modify (O000O000OOOO00OO0 ,OOOO0O0O00O0OOOO0 ):#line:3174
        global O0O0O0O0O0O0O_zxco0o0o0o0 #line:3175
        OO000OO0000OOOOO0 =str (O0O0O0O0O0O0O_zxco0o0o0o0 )#line:3176
        O0O0O00OOO00O00O0 ,O0O0OO00OOOO0OO0O =O000O000OOOO00OO0 .GetClientSize ()#line:3177
        OOOO0O0O00O0OOOO0 .SetBackground (wx .Brush (O000O000OOOO00OO0 .GetBackgroundColour ()))#line:3178
        OOOO0O0O00O0OOOO0 .Clear ()#line:3179
        OOOO0O0O00O0OOOO0 .SetFont (wx .Font (30 ,wx .SWISS ,wx .NORMAL ,wx .NORMAL ))#line:3180
        O00OO0O00000O0000 ,O00OO000OOOO000O0 =OOOO0O0O00O0OOOO0 .GetTextExtent (OO000OO0000OOOOO0 )#line:3181
        OOOO0O0O00O0OOOO0 .DrawText (OO000OO0000OOOOO0 ,(O0O0O00OOO00O00O0 -O00OO0O00000O0000 )/2 ,(O0O0OO00OOOO0OO0O )/2 -O00OO000OOOO000O0 /2 )#line:3182
    def OnTimer (O00OOOOO000O000O0 ,OOO00OOOO0O00O000 ):#line:3184
        O00O0O00OOO00O0OO =wx .BufferedDC (wx .ClientDC (O00OOOOO000O000O0 ))#line:3185
        O00OOOOO000O000O0 .Modify (O00O0O00OOO00O0OO )#line:3186
    def OnPaint (O0OOO0OOOO0O0OOOO ,OOO0O0O0000O0O0O0 ):#line:3188
        O0OOOO0000O0000OO =wx .BufferedPaintDC (O0OOO0OOOO0O0OOOO )#line:3189
        O0OOO0OOOO0O0OOOO .Draw (O0OOOO0000O0000OO )#line:3190
class Lowestzxco0o0o0o0Frame (wx .Frame ):#line:3192
    def __init__ (O0OO0OO000O000O0O ):#line:3193
         wx .Frame .__init__ (O0OO0OO000O000O0O ,None ,title ="wx.Timer",size =(200 ,50 ),pos =O0O0O0O0O0O0Ozxco0o0o0o0frame_pos ,style =wx .FRAME_TOOL_WINDOW |wx .STAY_ON_TOP )#line:3195
         Lowestzxco0o0o0o0Window (O0OO0OO000O000O0O )#line:3198
import string #line:3216
import wx .lib .agw .hyperlink as hyperlink #line:3217
class LoginFrame (wx .Frame ):#line:3218
    def __init__ (OOOO0O0O00OO00OOO ,OOO0OOO00000OOOOO ,OOOOO0OOOOO0O0O0O ,O0O0O0000OOO00O00 ):#line:3219
        wx .Frame .__init__ (OOOO0O0O00OO00OOO ,None ,-1 ,OOO0OOO00000OOOOO ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3220
        OOOO0O0O00OO00OOO .Bind (wx .EVT_CLOSE ,OOOO0O0O00OO00OOO .OnClose )#line:3221
        OOOO0O0O00OO00OOO .panel =wx .Panel (OOOO0O0O00OO00OOO ,size =(300 ,220 ))#line:3222
        OOOO0O0O00OO00OOO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3223
        OOOO0O0O00OO00OOO .SetIcon (OOOO0O0O00OO00OOO .icon )#line:3224
        OOOO0O0O00OO00OOO .sizer_v1 =wx .BoxSizer (wx .VERTICAL )#line:3237
        OOOO0O0O00OO00OOO .welcomelabel =wx .StaticText (OOOO0O0O00OO00OOO .panel ,-1 ,label ="请输入用户名和密码",style =wx .ALIGN_CENTER )#line:3238
        OOOO0O0O00OO00OOO .sizer_v1 .Add (OOOO0O0O00OO00OOO .welcomelabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =10 )#line:3239
        OOOO0O0O00OO00OOO .userbox =wx .BoxSizer (wx .HORIZONTAL )#line:3242
        OOOO0O0O00OO00OOO .userlabel =wx .StaticText (OOOO0O0O00OO00OOO .panel ,-1 ,label ="账号")#line:3243
        OOOO0O0O00OO00OOO .userText =wx .TextCtrl (OOOO0O0O00OO00OOO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER )#line:3245
        OOOO0O0O00OO00OOO .userbox .Add (OOOO0O0O00OO00OOO .userlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3246
        OOOO0O0O00OO00OOO .userbox .Add (OOOO0O0O00OO00OOO .userText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3247
        OOOO0O0O00OO00OOO .passbox =wx .BoxSizer (wx .HORIZONTAL )#line:3249
        OOOO0O0O00OO00OOO .passlabel =wx .StaticText (OOOO0O0O00OO00OOO .panel ,-1 ,label ="密码")#line:3250
        OOOO0O0O00OO00OOO .passText =wx .TextCtrl (OOOO0O0O00OO00OOO .panel ,-1 ,size =(150 ,-1 ),style =wx .TE_CENTER |wx .TE_PROCESS_ENTER |wx .TE_PASSWORD )#line:3252
        OOOO0O0O00OO00OOO .passbox .Add (OOOO0O0O00OO00OOO .passlabel ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3253
        OOOO0O0O00OO00OOO .passbox .Add (OOOO0O0O00OO00OOO .passText ,flag =wx .ALIGN_CENTER_HORIZONTAL |wx .ALL ,border =5 )#line:3254
        if OOOOO0OOOOO0O0O0O :#line:3255
            OOOO0O0O00OO00OOO .userText .SetValue (OOOOO0OOOOO0O0O0O )#line:3256
        if O0O0O0000OOO00O00 :#line:3257
            OOOO0O0O00OO00OOO .passText .SetValue (O0O0O0000OOO00O00 )#line:3258
        OOOO0O0O00OO00OOO .sizer_v1 .Add (OOOO0O0O00OO00OOO .userbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3259
        OOOO0O0O00OO00OOO .sizer_v1 .Add (OOOO0O0O00OO00OOO .passbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3260
        OOOO0O0O00OO00OOO .Bind (wx .EVT_TEXT_ENTER ,OOOO0O0O00OO00OOO .OnLogin ,OOOO0O0O00OO00OOO .userText )#line:3262
        OOOO0O0O00OO00OOO .Bind (wx .EVT_TEXT_ENTER ,OOOO0O0O00OO00OOO .OnLogin ,OOOO0O0O00OO00OOO .passText )#line:3263
        OOOO0O0O00OO00OOO .o0sdofsfo0sodf0so0btn =wx .Button (OOOO0O0O00OO00OOO .panel ,-1 ,label ="模拟",size =(90 ,30 ))#line:3265
        OOOO0O0O00OO00OOO .loginbtn =wx .Button (OOOO0O0O00OO00OOO .panel ,-1 ,label ="登录",size =(90 ,30 ))#line:3266
        OOOO0O0O00OO00OOO .btnSizer =wx .BoxSizer (wx .HORIZONTAL )#line:3267
        OOOO0O0O00OO00OOO .btnSizer .Add (OOOO0O0O00OO00OOO .o0sdofsfo0sodf0so0btn ,flag =wx .ALIGN_LEFT |wx .ALL ,border =3 )#line:3268
        OOOO0O0O00OO00OOO .btnSizer .Add (OOOO0O0O00OO00OOO .loginbtn ,flag =wx .ALIGN_RIGHT |wx .ALL ,border =3 )#line:3269
        OOOO0O0O00OO00OOO .sizer_v1 .Add (OOOO0O0O00OO00OOO .btnSizer ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3270
        OOOO0O0O00OO00OOO .loginbtn .Bind (wx .EVT_BUTTON ,OOOO0O0O00OO00OOO .OnLogin ,OOOO0O0O00OO00OOO .loginbtn )#line:3271
        OOOO0O0O00OO00OOO .purchaselink =hyperlink .HyperLinkCtrl (OOOO0O0O00OO00OOO .panel ,-1 ,u"购买账号")#line:3273
        OOOO0O0O00OO00OOO .purchaselink .UnsetToolTip ()#line:3274
        OOOO0O0O00OO00OOO .purchaselink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OOOO0O0O00OO00OOO .Purchase )#line:3275
        OOOO0O0O00OO00OOO .purchaselink .AutoBrowse (False )#line:3276
        OOOO0O0O00OO00OOO .purchaselink .EnableRollover (True )#line:3277
        OOOO0O0O00OO00OOO .purchaselink .SetUnderlines (False ,False ,True )#line:3278
        OOOO0O0O00OO00OOO .purchaselink .OpenInSameWindow (True )#line:3279
        OOOO0O0O00OO00OOO .purchaselink .UpdateLink ()#line:3280
        OOOO0O0O00OO00OOO .helplink =hyperlink .HyperLinkCtrl (OOOO0O0O00OO00OOO .panel ,-1 ,u"查看帮助")#line:3282
        OOOO0O0O00OO00OOO .helplink .UnsetToolTip ()#line:3283
        OOOO0O0O00OO00OOO .helplink .Bind (hyperlink .EVT_HYPERLINK_LEFT ,OOOO0O0O00OO00OOO .Purchase )#line:3284
        OOOO0O0O00OO00OOO .helplink .AutoBrowse (False )#line:3285
        OOOO0O0O00OO00OOO .helplink .EnableRollover (True )#line:3286
        OOOO0O0O00OO00OOO .helplink .SetUnderlines (False ,False ,True )#line:3287
        OOOO0O0O00OO00OOO .helplink .OpenInSameWindow (True )#line:3288
        OOOO0O0O00OO00OOO .helplink .UpdateLink ()#line:3289
        OOOO0O0O00OO00OOO .linkbox =wx .BoxSizer (wx .HORIZONTAL )#line:3291
        OOOO0O0O00OO00OOO .linkbox .Add (OOOO0O0O00OO00OOO .purchaselink ,flag =wx .ALIGN_LEFT |wx .RIGHT ,border =20 )#line:3292
        OOOO0O0O00OO00OOO .linkbox .Add (OOOO0O0O00OO00OOO .helplink ,flag =wx .ALIGN_RIGHT |wx .LEFT ,border =20 )#line:3293
        OOOO0O0O00OO00OOO .sizer_v1 .Add (OOOO0O0O00OO00OOO .linkbox ,flag =wx .ALIGN_CENTER |wx .ALL ,border =5 )#line:3294
        OOOO0O0O00OO00OOO .SetSizer (OOOO0O0O00OO00OOO .sizer_v1 )#line:3296
        OOOO0O0O00OO00OOO .Center ()#line:3297
        pub .subscribe (OOOO0O0O00OO00OOO .connect_success ,"connect")#line:3299
        OOOO0O0O00OO00OOO .hashthread =HashThread ()#line:3302
    def connect_success (OO000O0O0OO000OO0 ):#line:3304
        OO000O0O0OO000OO0 .loginbtn .Enable ()#line:3305
        global login_result #line:3306
        if login_result =='login success':#line:3307
            OO000O0O0OO000OO0 .Destroy ()#line:3308
            OO000O0O0OO000OO0 .topframe =TopFrame ('小鲜肉拍牌',version )#line:3309
            OO000O0O0OO000OO0 .topframe .Show (True )#line:3310
        elif login_result =='net error':#line:3312
            wx .MessageBox ('连接服务器失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3313
        elif login_result =='repeat':#line:3314
            wx .MessageBox ('重复登录，稍后再试','用户登录',wx .OK |wx .ICON_ERROR )#line:3315
        elif login_result =='wrong account':#line:3316
            wx .MessageBox ('账号错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3317
        elif login_result =='wrong password':#line:3318
            wx .MessageBox ('密码错误','用户登录',wx .OK |wx .ICON_ERROR )#line:3319
        else :#line:3320
            wx .MessageBox ('登录失败','用户登录',wx .OK |wx .ICON_ERROR )#line:3321
    def OnEraseBack (OOOO0000OO0OOO00O ,OOOO0O0O00OO0OOO0 ):#line:3324
        OOOOOOOO0OOO000OO =OOOO0O0O00OO0OOO0 .GetDC ()#line:3325
        if not OOOOOOOO0OOO000OO :#line:3326
            OOOOOOOO0OOO000OO =wx .ClientDC (OOOO0000OO0OOO00O )#line:3327
            O0000O00000OO0O0O =OOOO0000OO0OOO00O .GetUpdateRegion ().GetBox ()#line:3328
            OOOOOOOO0OOO000OO .SetClippingRect (O0000O00000OO0O0O )#line:3329
        OOOOOOOO0OOO000OO .Clear ()#line:3330
        O0O0OOO0O0O000O00 =wx .Bitmap ("blue.jpg")#line:3331
        OOOOOOOO0OOO000OO .DrawBitmap (O0O0OOO0O0O000O00 ,0 ,0 )#line:3332
    def OnClose (OOOOO0O00000O0O0O ,OOOOOO0OO0O000OOO ):#line:3334
        OOOOOO0OO0O000OOO .Skip ()#line:3335
        sys .exit (None )#line:3336
    def OnLogin (OO00O0O0000OOO0OO ,O0OOO0OOOOO00O0OO ):#line:3344
        global Username ,Password #line:3345
        O000O0OOO0OOOO000 =OO00O0O0000OOO0OO .userText .GetValue ()#line:3346
        OO0000O000OOOOOOO =OO00O0O0000OOO0OO .passText .GetValue ()#line:3347
        if O000O0OOO0OOOO000 =="":#line:3348
            wx .MessageBox ('请输入用户名！')#line:3349
            OO00O0O0000OOO0OO .userText .SetFocus ()#line:3350
        elif OO0000O000OOOOOOO =="":#line:3351
            wx .MessageBox ('请输入密码！')#line:3352
            OO00O0O0000OOO0OO .passText .SetFocus ()#line:3353
        else :#line:3355
            Username =O000O0OOO0OOOO000 #line:3356
            Password =OO0000O000OOOOOOO #line:3357
            OO00O0O0000OOO0OO .loginthread =LoginThread ()#line:3358
            O0O0OO000O00OO0OO =[O000O0OOO0OOOO000 ,OO0000O000OOOOOOO ]#line:3359
            with open ('your.name','wb')as OO000OOO000000OO0 :#line:3360
                pickle .dump (O0O0OO000O00OO0OO ,OO000OOO000000OO0 )#line:3361
            O0OOO0OOOOO00O0OO .GetEventObject ().Disable ()#line:3363
    def Purchase (O0OO00O0OOOO00OO0 ,O0OO0OO0000O0OOOO ):#line:3365
        print ("购买")#line:3366
class UserValidator (wx .Validator ):#line:3370
    ""#line:3371
    def __init__ (OOOO000O0O00OO0O0 ,OO0O0000O0OOOOOO0 ):#line:3373
        wx .Validator .__init__ (OOOO000O0O00OO0O0 )#line:3374
        OOOO000O0O00OO0O0 .flag =OO0O0000O0OOOOOO0 #line:3375
        OOOO000O0O00OO0O0 .Bind (wx .EVT_CHAR ,OOOO000O0O00OO0O0 .OnChar )#line:3376
    def Clone (OO000OOO00O0OO0OO ):#line:3379
        ""#line:3380
        return UserValidator (OO000OOO00O0OO0OO .flag )#line:3381
    def Validate (OOO000OOOOOO0O0O0 ,O0000OOOOOOO0OO0O ):#line:3384
        return True #line:3385
    def TransferToWindow (OO0O00OOOOO0OOO00 ):#line:3388
        return True #line:3389
    def TransferFromWindow (OO00000000000OOOO ):#line:3392
        return True #line:3393
    def OnChar (O0O000OO000O0O0O0 ,O00OO0OO00OOOO000 ):#line:3396
        pass #line:3397
class PassValidator (wx .Validator ):#line:3411
    ""#line:3412
    def __init__ (OOO0O00OO0000O0OO ):#line:3415
        wx .Validator .__init__ (OOO0O00OO0000O0OO )#line:3416
        OOO0O00OO0000O0OO .Bind (wx .EVT_CHAR ,OOO0O00OO0000O0OO .OnChar )#line:3417
    def Clone (OO0O000OO0O00OOOO ):#line:3420
        ""#line:3421
        return PassValidator ()#line:3422
    def Validate (O00OO0OO0O0OOO00O ,O0O0OOOOOOO0OOO0O ):#line:3425
        return True #line:3426
    def TransferToWindow (O0OO0OO0O0O0O000O ):#line:3429
        return True #line:3430
    def TransferFromWindow (O0O00OO0O00O0OO00 ):#line:3433
        return True #line:3434
    def OnChar (O0OO0O0OOOOOO0000 ,O0OOO0000O00OOOO0 ):#line:3437
        pass #line:3438
class ConfirmLogin (wx .Frame ):#line:3452
    pass #line:3453
class TimeThread (Thread ):#line:3456
    def __init__ (O00O00000O00O000O ):#line:3457
        ""#line:3458
        Thread .__init__ (O00O00000O00O000O )#line:3459
        O00O00000O00O000O .setDaemon (True )#line:3460
        O00O00000O00O000O .start ()#line:3461
    def run (OOOO0000OO0OOO000 ):#line:3463
        ""#line:3464
        global a_time #line:3466
        for O0OO00000OOOO0OOO in range (1000000 ):#line:3467
            O000OO000O0O00OOO =time .clock ()#line:3468
            time .sleep (0.1 )#line:3469
            O000OOOOO0O00O00O =time .clock ()#line:3470
            a_time +=O000OOOOO0O00O00O -O000OO000O0O00OOO #line:3471
class HashThread (Thread ):#line:3502
    def __init__ (O00OOO00OO000O0OO ):#line:3503
        ""#line:3504
        Thread .__init__ (O00OOO00OO000O0OO )#line:3505
        O00OOO00OO000O0OO .setDaemon (True )#line:3506
        O00OOO00OO000O0OO .start ()#line:3507
    def run (OO0OO0O00O00OOO00 ):#line:3509
        ""#line:3510
        Create_hash ()#line:3512
class findposThread (Thread ):#line:3518
    def __init__ (OOO00O0O00O00O00O ):#line:3519
        Thread .__init__ (OOO00O0O00O00O00O )#line:3520
        OOO00O0O00O00O00O .setDaemon (True )#line:3521
        OOO00O0O00O00O00O .start ()#line:3522
    def run (O00O0000O00O0O0O0 ):#line:3524
        findpos ()#line:3525
class sdfsf24324297Thread (Thread ):#line:3528
    def __init__ (OOO00O00OO0000OO0 ):#line:3529
        Thread .__init__ (OOO00O00OO0000OO0 )#line:3530
        OOO00O00OO0000OO0 .setDaemon (True )#line:3531
        OOO00O00OO0000OO0 .start ()#line:3532
    def run (O00OO00OOOOO0OO00 ):#line:3534
        global sdfsf24324297_need ,sdfsf24324297_on #line:3535
        global sdfsf24324297_need ,sdfsf24324297_on ,sdfsf24324297_one ,oo0o0O0O0O0_on #line:3536
        for O0OO000OOO0000O0O in range (100 ):#line:3537
            wx .Sleep (0.1 )#line:3538
            if sdfsf24324297_need :#line:3540
                findsdfsf24324297 ()#line:3542
                if sdfsf24324297_on :#line:3543
                    TopFrame .OnClick_sdfsf24324297 ()#line:3544
                    sdfsf24324297_need =False #line:3545
                    sdfsf24324297_on =False #line:3546
                    sdfsf24324297_one =False #line:3547
                    oo0o0O0O0O0_on =True #line:3548
        sdfsf24324297_one =False #line:3549
class uioo0o000ooThread (Thread ):#line:3551
    def __init__ (O0OO0000OOO00OOOO ):#line:3552
        Thread .__init__ (O0OO0000OOO00OOOO )#line:3553
        O0OO0000OOO00OOOO .setDaemon (True )#line:3554
        O0OO0000OOO00OOOO .start ()#line:3555
    def run (OO00O00OOOOOO00O0 ):#line:3557
        global sdfsf24324297_need ,sdfsf24324297_on #line:3558
        global uioo0o000oo_need ,uioo0o000oo_on ,uioo0o000oo_one #line:3559
        for O000OO00OO0OOOOO0 in range (50 ):#line:3560
            if uioo0o000oo_need :#line:3561
                finduioo0o000oo ()#line:3562
                if uioo0o000oo_on :#line:3563
                    TopFrame .OnClick_Shuaxin ()#line:3564
                    uioo0o000oo_on =False #line:3565
                    uioo0o000oo_need =False #line:3566
                    uioo0o000oo_one =False #line:3567
        uioo0o000oo_one =False #line:3568
class LoginThread (Thread ):#line:3573
    def __init__ (O0OOO0O00O0OOO000 ):#line:3574
        ""#line:3575
        Thread .__init__ (O0OOO0O00O0OOO000 )#line:3576
        O0OOO0O00O0OOO000 .setDaemon (True )#line:3577
        O0OOO0O00O0OOO000 .start ()#line:3578
    def run (OO0OOOO000O0O0O0O ):#line:3580
        global Username ,login_result #line:3582
        login_result =ConfirmUser ()#line:3583
        print (login_result )#line:3584
        logging .info ("%s"%login_result )#line:3585
        wx .CallAfter (pub .sendMessage ,"connect")#line:3586
class controlThread (Thread ):#line:3589
    def __init__ (OO0OOO00OOO0O0O00 ):#line:3590
        ""#line:3591
        Thread .__init__ (OO0OOO00OOO0O0O00 )#line:3592
        OO0OOO00OOO0O0O00 .setDaemon (True )#line:3593
        OO0OOO00OOO0O0O00 .start ()#line:3594
    def run (O00OO0OO0O00O000O ):#line:3597
        wx .Sleep (10 )#line:3598
        wx .CallAfter (pub .sendMessage ,"connect failure")#line:3599
class KeepThread (Thread ):#line:3604
    def __init__ (O00O000000O0O00O0 ):#line:3605
        ""#line:3606
        Thread .__init__ (O00O000000O0O00O0 )#line:3607
        O00O000000O0O00O0 .setDaemon (True )#line:3608
        O00O000000O0O00O0 .start ()#line:3609
    def run (OOOO0OOOOO00000OO ):#line:3612
        for O000OO0OO0O0O0O0O in range (1000000 ):#line:3613
            time .sleep (90 )#line:3614
            Keeplogin ()#line:3615
class TijiaoThread (Thread ):#line:3621
    def __init__ (O00OOOOOOO0OOOO00 ):#line:3622
        ""#line:3623
        Thread .__init__ (O00OOOOOOO0OOOO00 )#line:3624
        O00OOOOOOO0OOOO00 .setDaemon (True )#line:3625
        O00OOOOOOO0OOOO00 .start ()#line:3626
    def run (OOO0000OOOO00OOO0 ):#line:3629
        global oOO0O0O0O0O0O0_delay ,final_oOO0O0O0O0O0O0 ,ghjo0o0o0o0_zxco0o0o0o0 ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 #line:3630
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_OK ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 #line:3631
        global one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,oo0o0O0O0O0_on ,oOO0O0O0O0O0O0_on ,oOO0O0O0O0O0O0_one #line:3632
        for O0O000000OO0O0OOO in range (10000000 ):#line:3633
            time .sleep (0.1 )#line:3634
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and ooweo0o0werwr_on and oOO0O0O0O0O0O0_OK :#line:3638
                if oOO0O0O0O0O0O0_num ==1 and a_time >=one_oO0O0O0O0O0O0O0O02 and not oOO0O0O0O0O0O0_one :#line:3640
                    oOO0O0O0O0O0O0_on =False #line:3641
                    TopFrame .OnClick_Tijiao ()#line:3642
                    oOO0O0O0O0O0O0_on =False #line:3643
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3644
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,one_oO0O0O0O0O0O0O0O02 ))#line:3645
                    oOO0O0O0O0O0O0_one =True #line:3646
                elif oOO0O0O0O0O0O0_num ==2 and a_time >=ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 :#line:3647
                    oOO0O0O0O0O0O0_on =False #line:3648
                    TopFrame .OnClick_Tijiao ()#line:3649
                    oOO0O0O0O0O0O0_on =False #line:3650
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3651
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,a_time ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O02 ))#line:3652
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3653
                    oOO0O0O0O0O0O0_on =False #line:3654
                    oOO0O0O0O0O0O0_on =False #line:3655
                    TopFrame .OnClick_Tijiao ()#line:3656
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3657
                    logging .info ("Rone_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3658
                    oOO0O0O0O0O0O0_one =True #line:3659
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance :#line:3660
                    oOO0O0O0O0O0O0_on =False #line:3661
                    oOO0O0O0O0O0O0_on =False #line:3662
                    TopFrame .OnClick_Tijiao ()#line:3663
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,ooweo0o0werwr_on ,oOO0O0O0O0O0O0_OK ))#line:3664
                    logging .info ("Rooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3665
            if ghjo0o0o0o0_on and ooweo0o0werwr_on and oo0o0O0O0O0_on :#line:3667
                if oOO0O0O0O0O0O0_num ==1 and one_oO0O0O0O0O0O0O0O01 <=a_time <=one_oO0O0O0O0O0O0O0O01 +0.2 :#line:3669
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3670
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3671
                    oOO0O0O0O0O0O0_on =True #line:3672
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3673
                    logging .info ("Rone_oo0o0O0O0O0 %s%s"%(OO00000o01 ,one_oO0O0O0O0O0O0O0O01 ))#line:3674
                if oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 <=a_time :#line:3675
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3676
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3677
                    oOO0O0O0O0O0O0_on =True #line:3678
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ghjo0o0o0o0_on ,ooweo0o0werwr_on ))#line:3679
                    logging .info ("Rooo0O0o0oO0O_oo0o0O0O0O0 %s%s"%(ooo0O0o0oO0O_time1 ,ooo0O0o0oO0O_oO0O0O0O0O0O0O0O01 ))#line:3680
class MoniTijiaoThread (Thread ):#line:3684
    def __init__ (O0O00OO00OO00O0O0 ):#line:3685
        ""#line:3686
        Thread .__init__ (O0O00OO00OO00O0O0 )#line:3687
        O0O00OO00OO00O0O0 .setDaemon (True )#line:3688
        O0O00OO00OO00O0O0 .start ()#line:3689
    def run (O0OO0OOOO0O0O0O0O ):#line:3692
        global o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_on ,own_zxco0o0o0o01 ,own_zxco0o0o0o02 ,one_diff ,ooo0O0o0oO0O_diff #line:3693
        global oOO0O0O0O0O0O0_num ,oOO0O0O0O0O0O0_OK ,one_advance ,ooo0O0o0oO0O_advance ,oOO0O0O0O0O0O0_one #line:3694
        for O00OOO0OO00O000OO in range (10000000 ):#line:3695
            time .sleep (0.1 )#line:3696
            if oOO0O0O0O0O0O0_on and ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oOO0O0O0O0O0O0_OK :#line:3698
                if oOO0O0O0O0O0O0_num ==1 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=OO00000o02 and not oOO0O0O0O0O0O0_one :#line:3702
                    TopFrame .OnClick_Tijiao ()#line:3703
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3704
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,OO00000o02 ))#line:3705
                    oOO0O0O0O0O0O0_on =False #line:3706
                    oOO0O0O0O0O0O0_one =True #line:3707
                elif oOO0O0O0O0O0O0_num ==2 and o0sdofsfo0sodf0so0_ooo0O0o0oO0O >=ooo0O0o0oO0O_time2 and twice :#line:3708
                    TopFrame .OnClick_Tijiao ()#line:3709
                    logging .info ("o0sdofsfo0sodf0so01 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3710
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ,ooo0O0o0oO0O_time2 ))#line:3711
                    oOO0O0O0O0O0O0_on =False #line:3712
                elif oOO0O0O0O0O0O0_num ==1 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o01 -300 -one_advance and not oOO0O0O0O0O0O0_one :#line:3713
                    oOO0O0O0O0O0O0_on =False #line:3714
                    TopFrame .OnClick_Tijiao ()#line:3715
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s %s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3716
                    logging .info ("o0sdofsfo0sodf0so0 one_oOO0O0O0O0O0O0 %s %s %s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o01 ))#line:3717
                    oOO0O0O0O0O0O0_one =True #line:3718
                elif oOO0O0O0O0O0O0_num ==2 and O0O0O0O0O0O0O_zxco0o0o0o0 >=own_zxco0o0o0o02 -300 -ooo0O0o0oO0O_advance and twice :#line:3719
                    oOO0O0O0O0O0O0_on =False #line:3720
                    TopFrame .OnClick_Tijiao ()#line:3721
                    logging .info ("o0sdofsfo0sodf0so02 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s%s"%(oOO0O0O0O0O0O0_on ,ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ,oOO0O0O0O0O0O0_OK ))#line:3722
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oOO0O0O0O0O0O0 %s%s%s"%(oOO0O0O0O0O0O0_num ,O0O0O0O0O0O0O_zxco0o0o0o0 ,own_zxco0o0o0o02 ))#line:3723
            if ghjo0o0o0o0_on and o0sdofsfo0sodf0so0_on and oo0o0O0O0O0_on :#line:3728
                if oOO0O0O0O0O0O0_num ==1 and OO00000o01 <=o0sdofsfo0sodf0so0_ooo0O0o0oO0O <=OO00000o01 +0.2 :#line:3729
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3730
                    own_zxco0o0o0o01 =O0O0O0O0O0O0O_zxco0o0o0o0 +one_diff #line:3732
                    oOO0O0O0O0O0O0_on =True #line:3733
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3734
                    logging .info ("o0sdofsfo0sodf0so0 one_oo0o0O0O0O0 %s %s"%(OO00000o01 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3735
                elif oOO0O0O0O0O0O0_num ==2 and twice and ooo0O0o0oO0O_time1 <o0sdofsfo0sodf0so0_ooo0O0o0oO0O :#line:3736
                    TopFrame .OnClick_oo0o0O0O0O0 ()#line:3737
                    own_zxco0o0o0o02 =O0O0O0O0O0O0O_zxco0o0o0o0 +ooo0O0o0oO0O_diff #line:3739
                    oOO0O0O0O0O0O0_on =True #line:3740
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ghjo0o0o0o0_on ,o0sdofsfo0sodf0so0_on ))#line:3741
                    logging .info ("o0sdofsfo0sodf0so0 ooo0O0o0oO0O_oo0o0O0O0O0 %s %s"%(ooo0O0o0oO0O_time1 ,o0sdofsfo0sodf0so0_ooo0O0o0oO0O ))#line:3742
class Infoframe (wx .Frame ):#line:3745
    def __init__ (O00O000O000OOO0OO ,O000000O00O0000OO ,OO000OO000OO0OOO0 ,OOOO00O00O0O00000 ):#line:3746
        wx .Frame .__init__ (O00O000O000OOO0OO ,None ,-1 ,O000000O00O0000OO ,size =(300 ,240 ),style =wx .CAPTION |wx .CLOSE_BOX )#line:3747
        O00O000O000OOO0OO .Bind (wx .EVT_CLOSE ,O00O000O000OOO0OO .OnClose )#line:3748
        O00O000O000OOO0OO .panel =wx .Panel (O00O000O000OOO0OO ,size =(300 ,220 ))#line:3749
        O00O000O000OOO0OO .icon =wx .Icon (mainicon ,wx .BITMAP_TYPE_ICO )#line:3750
        O00O000O000OOO0OO .SetIcon (O00O000O000OOO0OO .icon )#line:3751
class SketchApp (wx .App ):#line:3754
    def OnInit (O0OO0OO00O0O00OO0 ):#line:3755
        try :#line:3766
            with open ("your.name",'rb')as O0OOOOOOOO000O00O :#line:3767
                OOOO000000OOOO0OO =pickle .load (O0OOOOOOOO000O00O )#line:3768
                OO00O0OO000O00O0O =OOOO000000OOOO0OO [0 ]#line:3769
                O00000OO0OO0O00OO =OOOO000000OOOO0OO [1 ]#line:3770
        except :#line:3771
            OO00O0OO000O00O0O ='123456'#line:3772
            O00000OO0OO0O00OO =0 #line:3773
        O0O0O0O000OO0OO00 =LoginFrame ('小鲜肉拍牌',OO00O0OO000O00O0O ,O00000OO0OO0O00OO )#line:3774
        O0O0O0O000OO0OO00 .Show (True )#line:3775
        return True #line:3776
if __name__ =='__main__':#line:3779
    app =SketchApp ()#line:3780
    app .MainLoop ()
#e9015584e6a44b14988f13e2298bcbf9


#===============================================================#
# Obfuscated by Oxyry Python Obfuscator (http://pyob.oxyry.com) #
#===============================================================#
