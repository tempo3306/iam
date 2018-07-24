import cv2
from component.variable import get_val, set_val

'''
1.记录验证码输入时间
2.记录出价结果  
（1）验证码错误
（2）不得修改同样出价
（3）不在区间
（4）超时
3.记录出价金额

'''

def log_info():
    set_val('yan_time1', 0)  ##第一次出价用时
    set_val('yan_time2', 0)  ##第二次出价用时
    set_val('tijiao_result1', '')   ##第一次出价结果
    set_val('tijiao_result2', '')   ##第二次出价结果



'''
（1）出价成功
（2）不在区间
（3）验证码错误
（4）超时
（5）不得修改同样出价
（6）超过最大出价次数

'''


def create_results():
    set_val('result_dick', '')
    result_dick = {}

