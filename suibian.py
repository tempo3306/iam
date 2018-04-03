from component.staticmethod import *
import time

def cal_time():
    a = time.time()
    for i in range(20):
        Delete()
    b = time.time()
    print(b-a)

if __name__ == '__main__':
    cal_time()