from component.variable import V_global
# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:30
'''
def createlog():
    import logging, time

    timenow = time.time()
    # 转换成localtime
    time_local = time.localtime(timenow)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    # myapplog = time.strftime("%Y%m%d%H%M%S", time_local)
    myapplog = "mylog"
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='%s.log' % myapplog,
                        filemode='w')

