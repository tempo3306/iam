# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/7/31 16:25
'''
import pyautogui as pg
P_relative=[[343, -66], [346, 40], [96, 121], [92, 43], [201, 100],[281, 40],[221,37],[282,118]]
P_relative2=[[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [525, 5], [586, 86]]
websize=[1024,768]   #浏览器大小
Pxy = pg.size()  # 分辨率
Px1 = Pxy[0] / 2 #屏幕中心位置
Py2 = Pxy[1] / 2
Px=(Pxy[0]-websize[0])/2
Py=(Pxy[1]-websize[1])/2

px_lowestprice=208   #206   209 208 #截图相对位置
py_lowestprice=416   #412  416

for i in range(len(P_relative)):
    P_relative2[i][0]=P_relative[i][0]+512-208
    P_relative2[i][1]=P_relative[i][1]+384-416

print(P_relative2)
