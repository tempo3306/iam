# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/8/2 17:24
'''
l=[[1,2,3],[4,5,6],[7,8,9]]
import numpy as np




def createlist(li):
    result=[]
    result.append(li[0])
    result.append(li[1])
    result.append(li[2])
    for i in range(3):
        result.append([li[0][i],li[1][i],li[2][i]])
    result.append([li[0][0],li[1][1],li[2][2]])
    result.append([li[0][2],li[1][1],li[2][0]])
    result=np.array(result)
    print(np.sum(result,axis=1))


createlist(l)
