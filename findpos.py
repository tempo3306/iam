# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/7/31 9:17
'''
#查找位置
import cv2
from PIL import ImageGrab
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

findpos('target.png')