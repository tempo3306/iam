# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/9/8 8:31
'''
import os
# os.system("\"C:\\Program Files (x86)\\Google\\Chrome\\pplication\\chrome.exe\" www.baidu.com")
# os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# os.system('"C:/Program Files/Internet Explorer/iexplore.exe" http://www.baidu.com')
# os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" www.baidu.com')


# a="\"C:\\Program Files (x86)\\Google\\Chrome\\pplication\\chrome.exe\" www.baidu.com"
# print(a)

#HKEY_CLASSES_ROOT\http\shell\open\command

import winreg
import re,optparse
key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r"http\shell\open\command")
name, value, type = winreg.EnumValue(key,0)
print(name)
print(value)
print(type)

# pattern=re.compile("\"*(.+\.exe)")
# result=re.findall(pattern,value)[0]
# print(result)


needpath='"C:\Program Files (x86)\Internet Explorer\iexplore.exe"'
# a=os.path.exists(needpath)
# print(a)
# b=os.path.exists('C:\Program Files (x86)')

command="\""+needpath+"\"" +" http://121.196.220.94"

print(command)
os.system(command)
# os.system(needpath)




# try:
#     i=0
#     while 1:
#         name, value, type = winreg.EnumValue(key, i)
#         print(name)
#         i+=1
# except WindowsError:
#      print("查找完毕")