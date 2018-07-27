import cv2
import pickle

'''
refresh :  0
confirm :  1
lowestprice : 2
time :  3
'''

def get_target(filename):
    a = cv2.imread(filename, 0)
    print(a.shape)
    return cv2.imread(filename,0)  ##灰度模式打开


refresh = get_target('refresh.png')
confirm = get_target('confirm.bmp')
lowestprice = get_target('lowestprice.bmp')
time = get_target('time.bmp')
firstprice = get_target('firstprice.png')
firstprice_moni = get_target('firstprice_moni.png')


result_dick = {}

'''
出价成功
出价不在区间
请输入正确的校验码
超过截止时间
不得修改同样同价
超过最大出价次数
'''
result_dick['出价成功'] = get_target('price_success.png')
result_dick['出价不在区间'] = get_target('not_in_area.png')
result_dick['请输入正确的校验码'] = get_target('wrong_code.png')
result_dick['超过截止时间'] = get_target('outoftime.png')
result_dick['不得修改同样同价'] = get_target('same_price.png')
result_dick['超过最大出价次数'] = get_target('out_of_number.png')


target = [refresh, confirm, lowestprice, time, firstprice, firstprice_moni, result_dick]

print(target)


with  open("target.tkl", 'wb') as t:
    pickle.dump(target, t)

