# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/19 14:31
'''
import time
from threading import Thread
import PIL
from PIL import ImageGrab

def dograb(i,j):
    # print("执行", i)
    im = ImageGrab.grab([100,200,300,500])
    # im.save("sv_%s_%s.png" %(i,j))

class tThread(Thread):
    def __init__(self,i):
        Thread.__init__(self)
        self.setDaemon(True)
        self.i=i
    def run(self):
        for j in range(50):
            print(j)
            dograb(self.i,j)
            # time.sleep(0.1)


def thread_num():
    tthread=[]
    a=time.clock()
    num=2
    for i in range(num):
        tthread.append(tThread(i))
    for i in range(num):
        tthread[i].start()
    for i in range(num):
        tthread[i].join()
    b=time.clock()
    print(b-a)

# thread_num()
a=time.clock()
for i in range(100):
    dograb(1,1)
b=time.clock()
print(b-a)
thread_num()