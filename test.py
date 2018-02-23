# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/23 17:56
'''
from urllib import request
import json
import time

a = time.time()

target_url = "http://hupai.pro/bid/bid_login/?username=shooter1&passwd=123456&debug=True"

response = request.urlopen(target_url)
result = response.read()
result = str(result, encoding='utf-8')
result = json.loads(result)

print(result)
b = time.time()
print(b-a)