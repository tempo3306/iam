# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/2 10:48
'''
# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/2 9:14
'''
import cv2
import numpy as np
#hog特征
bin_n=16
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n * ang / (2 * np.pi))  # quantizing binvalues in (0...16)
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)  # hist is a 64 bit vector
    return hist


#二值化，切割
def cut(img):

    ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgn=[]
    xy=[]
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        # print(x, y, w, h)
        xy.append([x, y, w, h])

    xy = sorted(xy)
    for i in range(len(contours)):
        x, y, w, h = xy[i]
        imgn.append(image[y:y + h, x:x + w])
    return imgn

def readpic():
    svm=cv2.ml.SVM_load('maindata.xml')
    img2=cv2.imread("26.png",0)
    testData=cut(img2)
    testData=list(map(hog,testData))
    testData = np.float32(testData).reshape(-1,64)
    result = svm.predict(testData)
    result=result[1].reshape(-1).astype(int).astype(str)
    a="".join(list(result))
    print(a)
    return a

readpic()