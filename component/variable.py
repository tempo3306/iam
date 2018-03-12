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
import pickle, time
import pyautogui as pg
import numpy as np
import logging
logger = logging.getLogger()

vars = {}

##热键对应KEY
keycode = {}
for i in range(65, 91):
    keycode[chr(i)] = i


# 初始化变量
# --------------------------------------------------
# 修改变量值
def set_val(key, value):
    global vars
    try:
        vars[key] = value
    except:
        logger.exception('this is an exception message')


# 获取变量值
def get_val(key):
    try:
        val = vars[key]
        return val
    except KeyError:
        return 'Null'


# --------------------------------------------------
# 变量初始化
####初始化hash字典
def Create_hash():
    with open("target.tkl", 'rb')  as tar:
        global dick_target
        dick_target = pickle.load(tar)  # 要寻找对象的对象
        set_val('dick_target', dick_target)

##price_list 价格对应时间的表
price_list = [80000 for i in range(60)]  #0-59


def init_val():
    set_val('price_list', price_list)
    set_val('remotetime_url', "https://hupai.pro/bid/remotetime")
    set_val('userprice', 0) #当前出价 如果为0则表示未出价
    set_val('usertime', -1) #当前截止时间 如果为 -1表示未出价
    set_val('strategy_name', '') #策略名称
    set_val('current_strategy_name', '') #当前策略
    set_val('host_ali', "http://hupai.pro")
    set_val('debug', True)
    set_val('now_ping', 0)  #实时网速
    set_val('version', '1.0')
    set_val('num', 0)
    set_val('avt', 0)
    set_val('test', False)
    set_val('url1', "http://moni.51hupai.org/")
    set_val('url2', "www.baidu.com")  # 电信
    set_val('url3', "www.baidu.com")  # 非电信
    set_val('url4', "http://127.0.0.1:5000/Moni")
    set_val('mainicon', 'ico.ico')
    set_val('view', False)  # 定位显示
    set_val('do', False)  # 开启辅助
    set_val('ad_view', False)  # 显示广告
    set_val('price_view', False)  # 显示价格,控制截图
    set_val('yanzhengma_view', False)  # 验证码放大,控制截图
    set_val('yanzhengma_close', True)  # 关闭验证码放大窗
    set_val('yanzhengma_find', True)  # 验证码是否找到 默认True 发现需要查找 之后变为False
    set_val('yanzhengma_move', True)  # 是否需要移动
    set_val('yanzhengma_hash', 0)  # 前一个验证码截图  如果变化就刷新 ，不变化就不动作
    set_val('price_on', False)  # 价格是否显示
    set_val('price_count', 0)  # 辅助计时，正确显示价格
    set_val('yanzhengma_count', 0)  # 辅助计时，正确显示价格
    set_val('web_on', False)  # 监测web是否开启
    set_val('view_time', False)  # 时间框是否开启
    set_val('operation_show', False)  # 策略框是否开启
    set_val('time_on', False)  # 操作面板上是否开启时间
    time_on = get_val('time_on')
    set_val('a_time', time.time())  # 国拍初始时间
    set_val('b_time', 0)  # 制作0.1秒
    set_val('moni_minute', 29)
    set_val('moni_second', 0)
    set_val('chujia_time', 0)  # 出价时间
    set_val('Username', 0)  # 用户名
    set_val('Password', 0)  # 密码
    set_val('moni_on', False)  # 判断开启的是哪个窗口 ，限制同时只能开启一个
    set_val('guopai_on', False)
    set_val('strategy1', 53)  # 策略整数时间
    set_val('strategy2', 0.0)  # 策略小数时间
    set_val('strategy_on', True)  # 策略是否开启
    set_val('strategy_repeat', False)  # 判断是否重复，避免重复进程
    set_val('delay', False)  # 是否延迟
    set_val('delay_time', 0.5)  # 延迟大小设置
    set_val('login_result', False)  # 登录成功与否
    set_val('findpos_on', True)  # 控制是否找位置
    set_val('pricelist', [80000 + i * 100 for i in range(400)])  # 用于验证识别
    set_val('IDnumber', 0)  # 身份证号
    set_val('account', 0)  # 标书号
    set_val('passwd', 0)  # 密码
    set_val('changetime', 0)
    set_val('one_time1', 48)  # 第一次出价加价
    set_val('one_time2', 55)  # 第一次出价提交
    set_val('one_real_time1', 1000000000000)  # 换算之后的出价时间
    set_val('one_real_time2', 1000000000000)  # 换算之后的提交时间
    set_val('one_diff', 700)  # 第一次加价幅度
    set_val('one_delay', 0.5)  # 第一次延迟
    set_val('one_advance', 100)  # 第一次提交提前量
    set_val('second_time1', 48)  # 第二次次出价加价
    set_val('second_time2', 55)  # 第二次出价提交
    set_val('second_real_time1', 1000000000000)  # 换算之后的出价时间
    set_val('second_real_time2', 1000000000000)  # 换算之后的提交时间
    set_val('second_diff', 600)  # 第二次加价幅度
    set_val('second_delay', 0.5)  # 第二次出价延迟
    set_val('second_advance', 100)  # 第二次出价提交提前量
    set_val('osl', [0] * 15)  # 策略容器初始化   判定+10参数+确认选项
    set_val('chujia_on', True)  # 完成一次出价之后关闭，完成出价后关闭
    set_val('tijiao_on', False)  # 是否需要提交,完成提交后打开
    set_val('lowest_price', 93400)  # 最低成交价
    set_val('own_price1', 0)  # 第一次出价
    set_val('own_price2', 0)  # 第二次出价
    set_val('own_price', 0)  # 当前出价
    set_val('tijiao_OK', False)  # 表示输完验证码
    set_val('e_on', True)  # 表示s激活tijiao_OK
    set_val('enter_on', False)  # 表示回车激活tijiao_Ok
    set_val('twice', False)  # 开启两次出价
    set_val('tijiao_num', 1)  # 开启二次出价，设置为2，执行一次之后，减1
    set_val('tijiao_one', False)  # 第一次出价之后开闭
    set_val('websize', [902, 700])  # 浏览器大小
    websize = get_val('websize')
    set_val('Pxy', pg.size())  # 分辨率
    Pxy = get_val('Pxy')
    set_val('Px1', Pxy[0] / 2)  # 屏幕中心位置
    set_val('Py2', Pxy[1] / 2)
    set_val('Px', int((Pxy[0] - websize[0]) / 2 - 80))
    Px = get_val('Px')
    set_val('Py', int((Pxy[1] - websize[1]) / 2))
    Py = get_val('Py')
    set_val('P_relative',
            [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]])  # 各按钮相对于WEB位置
    P_relative = get_val('P_relative')

    ## 相对于最低成交价位置
#   ## 0:加价  1：出价 2：提交  3：刷新   4 ：确认   5：验证码    6:验证码输入框     7：取消
    set_val('P_relative2', [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]])
    set_val('Position', [[0, 0] for i in range(len(P_relative))])
    set_val('px_ajust', 0)
    set_val('py_ajust', 0)
    set_val('px_price', 770 - 171)
    px_price = get_val('px_price')
    set_val('py_price', 260)
    py_price = get_val('py_price')
    set_val('px_priceframe', 220 - 191)
    px_priceframe = get_val('px_priceframe')
    set_val('py_priceframe', 480)
    py_priceframe = get_val('py_priceframe')
    set_val('px_timeframe', 22)
    px_timeframe = get_val('px_timeframe')
    set_val('py_timeframe', 348)
    py_timeframe = get_val('py_timeframe')
    set_val('px_lowestpriceframe', 245)
    px_lowestpriceframe = get_val('px_lowestpriceframe')
    set_val('py_lowestpriceframe', 290)
    py_lowestpriceframe = get_val('py_lowestpriceframe')
    set_val('lowestpriceframe_pos', [px_lowestpriceframe, py_lowestpriceframe])
    set_val('px_yanzhengmaframe', 400 - 215)
    px_yanzhengmaframe = get_val('px_yanzhengmaframe')
    set_val('py_yanzhengmaframe', 460)
    py_yanzhengmaframe = get_val('py_yanzhengmaframe')
    set_val('px_mini', 200)
    px_mini = get_val('px_mini')
    set_val('py_mini', 40)
    py_mini = get_val('py_mini')
    set_val('Pricesize', [400, 80])
    set_val('Yanzhengmasize', [400, 220])
    set_val('Timesize', [200, 50])
    set_val('lowestprice_area', [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py])
    set_val('refresh_area', [396 - 150, 11 - 100, 396 + 150, 11 + 100])
    set_val('confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
    set_val('yan_confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
    set_val('ghostbutton_pos', [0, 0])
    set_val('webview_pos', [-25, 0])  # WEB在 WEBVIEW里的相对位置
    set_val('Px_price', Px + px_price)
    Px_price = get_val('Px_price')
    set_val('Py_price', Py + py_price)
    Py_price = get_val('Py_price')
    set_val('Pos_price', [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini])  # 所出价格截图位置BOX
    set_val('Pos_yanzhengma', [])  # 验证码所在位置
    set_val('Px_priceframe', Px + px_priceframe)
    Px_priceframe = get_val('Px_priceframe')
    set_val('Py_priceframe', Py + py_priceframe)
    Py_priceframe = get_val('Py_priceframe')
    set_val('Pos_priceframe', [Px_priceframe, Py_priceframe])
    set_val('Px_timeframe', px_timeframe + Px)
    Px_timeframe = get_val('Px_timeframe')
    set_val('Py_timeframe', py_timeframe + Py)
    Py_timeframe = get_val('Py_timeframe')
    set_val('Pos_timeframe', [Px_timeframe, Py_timeframe])
    set_val('Pos_controlframe', [Px + 40, Py + 480])
    set_val('Px_yanzhengmaframe', Px + px_yanzhengmaframe)
    Px_yanzhengmaframe = get_val('Px_yanzhengmaframe')
    set_val('Py_yanzhengmaframe', Py + py_yanzhengmaframe)
    Py_yanzhengmaframe = get_val('Py_yanzhengmaframe')
    set_val('Pos_yanzhengmaframe', [Px_yanzhengmaframe, Py_yanzhengmaframe])
    set_val('px_lowestprice', 0)  # 206   209 208 截图相对位置
    px_lowestprice = get_val('px_lowestprice')
    set_val('py_lowestprice', 0)  # 412  416
    py_lowestprice = get_val('py_lowestprice')
    set_val('Px_lowestprice', Px + px_lowestprice)
    Px_lowestprice = get_val('Px_lowestprice')
    set_val('Py_lowestprice', Py + py_lowestprice)
    Py_lowestprice = get_val('Py_lowestprice')
    set_val('lowestprice_sizex', 82)  # 截图范围 41
    set_val('lowestprice_sizey', 16)
    set_val('Px_currenttime', Px_lowestprice - 25)  # 参考最低成交价位置
    set_val('Py_currenttime', Py_lowestprice + 17)
    set_val('currenttime_sizex', 132)
    set_val('currenttime_sizey', 13)
    set_val('px_relative', 49)  # 查找出来位置反算相对位置
    set_val('py_relative', 0)
    set_val('px_confirm', 656)
    px_confirm = get_val('px_confirm')
    set_val('py_confirm', 475)
    py_confirm = get_val('py_confirm')
    set_val('Px_confirm', Px + px_confirm)
    set_val('Py_confirm', Py + py_confirm)
    set_val('confirm_sizex', 113)
    set_val('confirm_sizey', 28)
    set_val('confirm_on', False)  # 是否需要确认
    set_val('confirm_need', False)  # 启动确认识别
    set_val('confirm_one', False)  # 限制只产生一次进程
    set_val('px_refresh', 550)
    px_refresh = get_val('px_refresh')
    set_val('py_refresh', 413)
    py_refresh = get_val('py_refresh')
    set_val('Px_refresh', Px + px_refresh)
    set_val('Py_refresh', Py + py_refresh)
    set_val('refresh_sizex', 108)
    set_val('refresh_sizey', 21)
    set_val('refresh_on', False)  # 是否需要刷新
    set_val('refresh_need', False)  # 启动刷新识别
    set_val('refresh_one', False)  # 限制只产生一次进程
    set_val('chujia_interval', False)  # 出价间隔
    set_val('tijiao_interval', False)  # 提交间隔
    set_val('query_interval', False)  # 间隔
    set_val('query_on', False)  # 是否处于查询状态
    set_val('sc_area', [Px_lowestprice - 10, Py_lowestprice - 100, Px_lowestprice + 600, Py_lowestprice + 120])
    set_val('use_area', [])

    set_val('nptemp', [])
    nptemp = get_val('nptemp')
    set_val('imgpos_lowestprice', np.array(nptemp))  # 最低成交价
    set_val('imgpos_refresh', np.array(nptemp))  # 刷新按钮
    set_val('imgpos_confirm', np.array(nptemp))  # 出价完后确认
    set_val('impos_yanzhengma', np.array(nptemp))  # 验证码
    set_val('imgpos_yanzhengmaconfirm', np.array(nptemp))  # 验证码确认键
    set_val('imgpos_currenttime', np.array(nptemp))  # 当前时间

    ##智能出价服务
    set_val('smart_ajust', False) #智能调整出价，默认关闭
    set_val('smart_ajust_time', 10000000000) #智能调整触发时间