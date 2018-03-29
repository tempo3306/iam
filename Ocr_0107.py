# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/7/28 15:52
'''
import cv2,copy
import numpy as np
from functools import reduce
SZ=20
bin_n = 64 # Number of bins


##获取文件列表
import os
def getlist():
    files =os.listdir('./moni')
    nfiles = []
    for file in files:
        temp1=os.path.splitext(file)[0]
        temp2=list(temp1)
        temp3=list(map(int,temp2))
        for tem in temp3:
            nfiles.append([tem])
    print(nfiles)
    return (files,nfiles)


####可以将斜着的数字摆正
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img
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

def fushi(img):
    kernel = np.ones((1, 1), np.uint8)
        # 读入图片
    dilated = cv2.dilate(img, kernel)
    # 腐蚀图像
    eroded = cv2.erode(dilated, kernel)
    # 膨胀图像

    return eroded


#二值化，切割
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

#SVM训练
#创建训练素材
# 合并随机点，得到训练数据
def traindata(imglist):
    TrainData=[]
    for img in imglist:
        img=cv2.imread(img,0)
        trainData = cut(img)
        trainData = list(map(hog, trainData))
        trainData = np.float32(trainData).reshape(-1, bin_n * 4)
        TrainData.append(trainData)
    return TrainData

def getlabel(imglist):
    result=[]
    for img in imglist:
        img=img.split(".")
        num=img[0]
        for n in num:
            result.append([int(n)])
    return result



imglist=["10.png","11.png",'8.png','time.png','moni.png']

##标号11为：
labellist=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[0],
           [8],[6],[6],[0],[0],[1],[1],[11],[2],[9],[11],[0],[1],
           [1], [2], [3], [4], [5], [6], [7], [8], [9], [0]]


imglist2,labellist2 =getlist()


imglist.extend(imglist2)
labellist.extend(labellist2)

TrainData=traindata(imglist)

trainData=reduce(lambda x,y:np.vstack((x,y)),TrainData)


responses=np.array(labellist,dtype='int32')
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)  # SVM类型
# svm.setKernel(cv2.ml.SVM_RBF)
svm.setKernel(cv2.ml.SVM_LINEAR) # 使用线性核
svm.setC(2.67)
svm.setGamma(5.383)


# 训练
ret = svm.train(trainData, cv2.ml.ROW_SAMPLE, responses)
# img2=cv2.imread("86200.png",0)
# img2=cv2.imread("107.png",0)
# testData=cut(img2)
# testData=list(map(hog,testData))
# # trainData=np.array(trainData,dtype='float32')
# testData = np.float32(testData).reshape(-1,bin_n*4)
# result = svm.predict(testData)
svm.save('maindata_new.xml')
# svm.save('svm_cat_data.dat')
# SVM_load('svm_cat_data.dat')
# print(result)

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

# for i in range(89900,94800,100):
#     img="new_pic\\%s.png"%i
#     read(img)
p=read('moni.png')
read('z50.png')


read('z132.png')


# for num in range(90600,95500,100):
#     path = ".\\t2\\%d.png"%num
#     nn = read(path)
#     if nn != str(num):
#         print("num=",num,end=" ")
#         print("nn=",nn)





#
#
# img1=cv2.imread("10.png",0)
# img2=cv2.imread("11.png",0)
# img3=cv2.imread("moni.png",0)
# img4=cv2.imread("107.png",0)
# img5=cv2.imread("887001.png",0)
# img6=cv2.imread("879001.png",0)
#
# trainData3=cut(img3)
# trainData3=list(map(hog,trainData3))
# trainData3 = np.float32(trainData3).reshape(-1,bin_n*4)
#
# trainData4=cut(img4)
# trainData4=list(map(hog,trainData4))
# trainData4 = np.float32(trainData4).reshape(-1,bin_n*4)
#
# trainData5=cut(img5)
# trainData5=list(map(hog,trainData5))
# trainData5 = np.float32(trainData5).reshape(-1,bin_n*4)
#
# trainData6=cut(img6)
# trainData6=list(map(hog,trainData6))
# trainData6 = np.float32(trainData6).reshape(-1,bin_n*4)
#
# trainData1=cut(img1)
# trainData1=list(map(hog,trainData1))
# trainData1 = np.float32(trainData1).reshape(-1,bin_n*4)
# trainData2=cut(img2)
# trainData2=list(map(hog,trainData2))
# trainData2 = np.float32(trainData2).reshape(-1,bin_n*4)
#


# trainData=np.vstack((trainData1,trainData2,trainData3,trainData4,trainData5,trainData6))
# trainData=np.vstack((trainData,trainData2))

# print(trainData.shape)
# trainData = trainData.reshape(-1,64)

# print(responses)
# 创建分类器
# svm_params = dict( kernel_type = cv2.ml.SVM_LINEAR,
#                        svm_type = cv2.ml.SVM_C_SVC,
#                        C = 1  )
# #训练
# print(len(trainData))
# svm = cv2.ml.SVM_create()
# ret=svm.train(trainData,responses, params=svm_params)    #responses标签，trainData输入的训练集

