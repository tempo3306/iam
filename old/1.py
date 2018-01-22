# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/1 8:23
'''
from PIL import Image,ImageGrab
import numpy,pickle,cv2
sc1 = Image.open("refresh.png").convert('L')
img1 = numpy.asarray(sc1)
# sc2 = Image.open("confirm.bmp").convert('L')
# img2 = numpy.asarray(sc2)
#
# sc3 = Image.open("target.png").convert('L')
# template= numpy.asarray(sc3)
#
# final=[img1,img2,template]
# with open("target.tkl","wb") as tar:
#     pickle.dump(final,tar)


sc = ImageGrab.grab([600,300,800,400]).convert('L')
img = numpy.asarray(sc)
w, h = img1.shape[::-1]
res = cv2.matchTemplate(img, img1, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(max_val,max_loc)