# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/19 15:57
'''
import multiprocessing
from PIL import ImageGrab
import time
def getpic():
    a=time.clock()
    im=ImageGrab.grab()
    b=time.clock()
    im.save("sv%s.png" )
    c=time.clock()

if __name__ == '__main__':
    getpic()
    pool = multiprocessing.Pool(processes=4)
    for i in range(4):
        pool.apply_async(getpic)
    a=time.clock()
    pool.close()
    pool.join()
    b=time.clock()
    print(b-a)