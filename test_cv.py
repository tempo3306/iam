# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/25 22:19
'''
import cv2
from PIL import ImageGrab,Image
import numpy as np
def cut_pic(img):
    img=cv2.imread(img)
    i1=img[0:100,:]
    i2=img[200:300,:]
    im = np.concatenate([i1,i2])

    cv2.imwrite('p1.png',i1)
    cv2.imwrite('p2.png',i2)
    cv2.imwrite('p3.png',im)
    return im

def Screen_shot():
    global Pricesize
    region = ImageGrab.grab((100,400,400,700))
    region.save("p0.png")


Screen_shot()
cut_pic('p0.png')
