# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/7/31 9:17
'''
#查找位置
import cv2
from PIL import ImageGrab
import pickle,timeit

a=cv2.imread("target.png",0)
with open("target.tkl","wb") as tar:
    pickle.dump(a,tar)
import pyautogui as pg
at=timeit.timeit('lowestprice = pg.screenshot()', setup="import pyautogui as pg",number=100)
b=timeit.timeit('ImageGrab.grab()', setup="from PIL import ImageGrab",number=100)
print(at,b)

sc = ImageGrab.grab()
import numpy as np
a=np.asarray(sc)

def findpos(targetimg):
    # targetimg="target.png"
    sc = ImageGrab.grab()
    sc.save("sc.png")
    img=cv2.imread("sc.png",0)
    template = cv2.imread(targetimg, 0)  # 要寻找对象的对象
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val)
    print(max_val)
    print(min_loc)
    print(max_loc)

def findpos2():
    # targetimg="target.png"
    sc = ImageGrab.grab()
    sc.save("sc.png")
    img = cv2.imread("sc.png", 0)
    with open("target.tkl",'rb')  as tar:
        template=pickle.load(tar)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val)
    print(max_val)
    print(min_loc)
    print(max_loc)
# findpos2()

# findpos('target.png')