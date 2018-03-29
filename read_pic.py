import cv2
import numpy as np
from functools import reduce
SZ=20
bin_n = 64 # Number of bins

svm = cv2.ml.SVM_load('maindata.xml')


def cut(img):
    # ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    ret, thresh1 = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY_INV)
    # thresh1=fushi(thresh1)
    # image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    image,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgn=[]
    xy=[]
    cv2.imwrite("thresh1.png",thresh1)
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        xy.append([x, y, w, h])

    xy = sorted(xy)
    xy0=[]
    for i in range(len(xy)-1):
        diff=xy[i+1][0]-xy[i][0]
        if diff <6:
            t0=min(xy[i][0],xy[i+1][0])
            t1=min(xy[i][1],xy[i+1][1])
            t2=max(xy[i][2]+xy[i][0],xy[i+1][2]+xy[i+1][0])-t0
            t3=max(xy[i][3]+xy[i][1],xy[i+1][3]+xy[i+1][1])-t1
            xy[i+1]=[t0,t1,t2,t3]
        elif 6<=diff<12:
            xy0.append(xy[i])
        else:
            if 12<=diff<=16:
                temp1=[xy[i][0],xy[i][1],xy[i][2]-int(diff/2),xy[i][3]]
                temp2=[int(diff/2)+xy[i][0],xy[i+1][1],xy[i+1][2],xy[i+1][3]]
                xy0.append(temp1)
                xy0.append(temp2)
            elif 19<=diff<=23:
                t1=int(diff/3)
                t2=int(diff/3)*2
                temp1=[xy[i][0],xy[i][1],t1,xy[i][3]]
                temp2=[xy[i][0]+t1,xy[i][1],t2,xy[i][3]]
                temp3=[xy[i][0]+t2,xy[i][1],diff-t2,xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
            elif  26<=diff<=30:
                t1=int(diff/4)
                t2=int(diff/4)*2
                t3=int(diff/4)*3
                temp1=[xy[i][0],xy[i][1],t1,xy[i][3]]
                temp2=[xy[i][0]+t1,xy[i][1],t2,xy[i][3]]
                temp3=[xy[i][0]+t2,xy[i][1],t3,xy[i][3]]
                temp4=[xy[i][0]+t3,xy[i][1],diff-t3,xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
            elif  33<=diff:
                t1=int(diff/5)
                t2=int(diff/5)*2
                t3=int(diff/5)*3
                t4=int(diff/5)*4
                temp1=[xy[i][0],xy[i][1],t1,xy[i][3]]
                temp2=[xy[i][0]+t1,xy[i][1],t2,xy[i][3]]
                temp3=[xy[i][0]+t2,xy[i][1],t3,xy[i][3]]
                temp4=[xy[i][0]+t3,xy[i][1],t4,xy[i][3]]
                temp5=[xy[i][0]+t4,xy[i][1],diff-t4,xy[i][3]]
                xy0.append(temp1)
                xy0.append(temp2)
                xy0.append(temp3)
                xy0.append(temp4)
                xy0.append(temp5)

    xy0.append(xy[-1])
    for i in range(len(xy0)):
        x, y, w, h = xy0[i]
        imgn.append(image[y:y + h, x:x + w])
    for i in range(len(imgn)):
        imgn[i]=cv2.resize(imgn[i],(8,8))
    for i in range(len(xy0)):
        cv2.imwrite("ST%d.png"%i,imgn[i])

    return imgn


#hog特征
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n * ang / (2 * np.pi))  # quantizing binvalues in (0...16)
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)  # hist is a 64 bit vector
    # print(hist)
    return hist


def read(img):
    img2 = cv2.imread(img, 0)
    testData = cut(img2)
    testData = list(map(hog, testData))
    testData = np.float32(testData).reshape(-1, bin_n * 4)
    result = svm.predict(testData)
    result = result[1].reshape(-1).astype(int).astype(str)
    for i in range(len(result)):
        if result[i] == '11':
            result[i] = ':'
    price = "".join(list(result))
    print(price)
    return price


read('11.png')