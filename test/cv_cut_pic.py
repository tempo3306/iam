import cv2
import numpy as np
from PIL import Image, ImageGrab

# yimg = ImageGrab.grab().save("yanzhengma.png")
sc = ImageGrab.grab((100, 100, 280, 600)).convert('L')

def cut_pic(img, size, name):
    img = np.asarray(img)
    i1 = img[0:24, :150]
    i2 = img[48:110, 30:]
    im = np.concatenate([i2, i1])
    im = cv2.resize(im, tuple(size))
    cv2.imwrite(name, im)

import time



def get_img():
    cut_pic(sc, (600, 400), "yanzhengma.png")

# a = time.time()
# for i in range(1000):
#     get_img()
# b = time.time()
# print(b-a)


a = time.time()
for i in range(100):
    sc = ImageGrab.grab((100, 100, 900, 900)).convert('L')
b = time.time()
print(b-a)