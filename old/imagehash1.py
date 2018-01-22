# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/25 10:27
'''
import imagehash
import pyautogui as pg

a=pg.screenshot()
price_hash = imagehash.dhash(a)
print(price_hash)