# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 10:46
'''
'''
管理所有的全局变量  
global 关键字在一个文件内是唯一的
'''
host_ali = "http://hupai.pro"
debug = True

vars = {}

#初始化变量
vars['a_time'] = 0
vars['b_time'] = 0
vars['moni_second'] = 0

#修改变量值
def set_val(key,value):
    global vars
    try:
        vars[key] = value
    except:
        pass
#获取变量值
def get_val(key):
    try:
        val = vars[key]
        return val
    except KeyError:
        return 'Null'

