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
import win32api
import numpy as np
import logging
from component.remote_control import get_unique_id

logger = logging.getLogger()

vars = {}

##热键对应KEY
keycode = {}
for i in range(65, 91):
    keycode[chr(i)] = i



# --------------------------------------------------

'''
(1)单枪  依次为 0: strategy_type 1: one_time1  2: one_diff  3: one_advance 4: one_delay 5: one_time2 
                                6: one_forcetijiao_on
(2)双枪  依次为 0: strategy_type 1: one_time1  2: one_diff  3: one_advance 4: one_delay 5: one_time2
                                6: one_forcetijiao_on   
                                7: second_time1  8: second_diff  9: second_advance  10: second_delay 
                                11: second_time2  12: second_forcetijiao_on
(3)单枪动态提交  依次为 0: strategy_type 1: one_time1  2: one_diff  
                                       3: one_advance_smart1  4: one_delay_smart1   5: one_time2_smart1
                                       6: one_advance_smart2  7: one_delay_smart2   8: one_time2_smart2
                                       9: one_advance_smart3  10: one_delay_smart3  11: one_time2_smart3
                                       12: one_time2_smart
(4)双枪动态提交  依次为 0: strategy_type 1: one_time1  2: one_diff  3: one_advance 4: one_delay 5: one_time2
                                       6: one_forcetijiao_on   7: second_time1  8: second_diff 
                                       9: one_advance_smart1  10: one_delay_smart1   11: one_time2_smart1
                                       12: one_advance_smart2  13: one_delay_smart2   14: one_time2_smart2
                                       15: one_advance_smart3  16: one_delay_smart3  17: one_time2_smart3
                                       18: one_time2_smart


(5)智能出价提交   依次为 0: strategy_type  1: one_time1  2: one_diff


'''

strategy_dick = {

    '0': [0, 48.0, 700, 100, 0.5, 55,
        1],

    '1': [1, 40.0, 500, 0, 0.5, 48,
        1,
        50, 700, 100, 0.5,
        56, 1],

    '2': [2, 50.0, 700,
        0, 0, 54,
        100, 0.6, 55,
        200, 0.5, 56,
        56.5],

    '3': [3, 40.0, 500, 0, 0.5, 48,
         1,
         50, 700,
         0, 0, 54,
         100, 0.6, 55,
         200, 0.5, 56,
         56.5
          ],
    '4':[4, 48.0, 700],

    'yanzhengma_scale': True,
    'strategy_description': '单枪   48秒加700截止56秒提前100',  #策略名称
    'strategy_type': '0',
    'enter_on': True,
}

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


# 修改 策略字典
def set_dick(key, value):
    try:
        strategy_dick[key] = value
    except:
        logger.exception('this is an exception message')

# 获取 策略字典
def get_dick(key):
    try:
        val = strategy_dick[key]
        return val
    except KeyError:
        return 'Null'

def get_strategy_dick():
    return strategy_dick

def set_strategy_dick(dick):
    global strategy_dick
    print(dick)
    strategy_dick = dick

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

def get_id_hash(id):
    import hashlib
    sha1 = hashlib.sha1()
    sha1.update(id.encode('utf-8'))
    return sha1.hexdigest()



class Hotkey_label():
    SMART_PRICE_LABEL = '智能出价'
    SMART_PRICE = 'ESC'
    REFRESH_WEB_LABEL = '刷新页面'
    REFRESH_WEB = 'F5'
    FORCE_TIJIAO_LABEL = '强制提交'
    FORCE_TIJIAO = 'F1'
    CLEAR_YAN_LABEL = '清空验证码'
    CLEAR_YAN = '空格'


def init_val():
    ##封装
    init_id()
    init_size()
    init_url()
    init_label()
    init_strategy()
    init_account()
    init_status()
    init_smart()
    # remote_init()
    set_val('price_list', price_list)


    set_val('userprice', 0) #当前出价 如果为0则表示未出价
    set_val('usertime', -1) #当前截止时间 如果为 -1表示未出价

    # set_val('host_ali', "http://192.168.3.20:3000")
    set_val('debug', True)
    set_val('now_ping', 0)  #实时网速
    set_val('version', '1.0')
    set_val('num', 0)
    set_val('avt', 0)
    set_val('test', False)



def init_url():
    set_val('remotetime_url', "https://hupai.pro/api/bid/get_remotetime")
    set_val('host_ali', "https://hupai.pro")
    # set_val('host_ali', "http://192.168.3.20:3000")
    set_val('url_51', "http://moni.51hupai.org/")
    set_val('url_dianxin', "http://test.alltobid.com/moni/gerenlogin.html")  # 电信
    # set_val('url_dianxin', "https://www.baidu.com")  # 电信
    set_val('url_nodianxin', "http://moni.51hupai.org/")  # 非电信
    # set_val('url_moni', "http://test.alltobid.com/moni/gerenlogin.html")
    set_val('url_moni', "https://hupai.pro/static/main/moni.html")
    # set_val('url_moni', "http://192.168.3.20:3000/static/main/moni.html")
    set_val('guopai_dianxin', False)  ##当前是否处于国拍电信  默认是非电信


def init_label():
    set_val('moni_webstatus_label', '模拟中')
    set_val('dianxin_webstatus_label', '国拍电信')
    set_val('nodianxin_webstatus_label', '国拍非电信')
    set_val('urlchange_dianxin_label', '切换线路')
    set_val('urlchange_nodianxin_label', '切换线路')

def init_id():
    set_val('userconfirm_on', False)
    set_val('topframe', -1)
    set_val('loginframe', -1)
    set_val('moni_webframe', -1)
    set_val('guopai_webframe', -1)

def init_size():
    ##webframe相关
    set_val('websize', (1148, 715))  # webframe大小
    set_val('webview_pos', (-5, -16))  # WEB在 WEBVIEW里的相对位置
    set_val('buttonpanel_size', (892, 30))
    set_val('buttonpanel_pos', (0, 0))
    set_val('htmlsize', [918, 768])
    set_val('htmlpanel_size', (892, 628))
    set_val('htmlpanel_pos', (0, 30))
    set_val('bottomestatusbarpanel_size', (892, 30))
    set_val('bottomestatusbarpanel_pos', (0, 658))

    websize = get_val('websize')
    htmlpanel_size = get_val('htmlpanel_size')
    x0 = websize[0] - htmlpanel_size[0]
    set_val('operationpanel_size', (x0, websize[1]))
    set_val('operationpanel_pos', (htmlpanel_size[0], 0))

    websize = get_val('websize')
    set_val('Pxy', (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))) # 分辨率
    Pxy = get_val('Pxy')
    set_val('Px1', Pxy[0] / 2)  # 屏幕中心位置
    set_val('Py2', Pxy[1] / 2)
    set_val('Px', int((Pxy[0] - websize[0]) / 2))
    Px = get_val('Px')
    set_val('Py', int((Pxy[1] - websize[1]) / 2) - 10)
    Py = get_val('Py')
    set_val('P_relative',
            [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]])  # 各按钮相对于WEB位置
    P_relative = get_val('P_relative')


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
    set_val('Timesize', [200, 50])
    set_val('lowestprice_area', [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py])
    set_val('refresh_area', [396 - 150, 11 - 100, 396 + 150, 11 + 100])
    set_val('confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
    set_val('yan_confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
    set_val('ghostbutton_pos', [0, 0])
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

    set_val('px_confirm', 656)
    px_confirm = get_val('px_confirm')
    set_val('py_confirm', 475)
    py_confirm = get_val('py_confirm')
    set_val('Px_confirm', Px + px_confirm)
    set_val('Py_confirm', Py + py_confirm)
    set_val('confirm_sizex', 113)
    set_val('confirm_sizey', 28)
    set_val('px_refresh', 550)
    px_refresh = get_val('px_refresh')
    set_val('py_refresh', 413)
    py_refresh = get_val('py_refresh')
    set_val('Px_refresh', Px + px_refresh)
    set_val('Py_refresh', Py + py_refresh)
    set_val('refresh_sizex', 108)
    set_val('refresh_sizey', 21)
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




'''
214 645
215 224
'''


def init_strategy():
    strategy_choices = ['单枪策略(专注一次出价)', '双枪策略(一伏二补)', '单枪策略 智能提交', '双枪策略 智能提交']
    set_val('strategy_choices', strategy_choices)


    tijiao_choices = [u"提前100", u"提前200", u"提前300", u"踩点"]
    set_val('tijiao_choices', tijiao_choices)

    set_val('mainicon', 'logo.ico')
    set_val('view', False)  # 定位显示
    set_val('hotkey_on', False)  # 开启辅助
    set_val('ad_view', False)  # 显示广告
    set_val('price_view', False)  # 显示价格,控制截图
    set_val('yanzhengma_view', False)  # 验证码放大,控制截图+-
    set_val('yanzhengma_close', True)  # 关闭验证码放大窗
    set_val('yanzhengma_find', True)  # 验证码是否找到 默认True 发现需要查找 之后变为False
    set_val('yanzhengma_move', True)  # 是否需要移动
    set_val('yanzhengma_hash', 0)  # 前一个验证码截图  如果变化就刷新 ，不变化就不动作
    set_val('yanzhengma_change', True) #判定是否变化

    set_val('price_on', False)  # 价格是否显示
    set_val('price_count', 0)  # 辅助计时，正确显示价格
    set_val('yanzhengma_count', 0)  # 辅助计时，正确显示价格
    set_val('web_on', False)  # 监测web是否开启
    set_val('view_time', False)  # 时间框是否开启
    set_val('operation_show', False)  # 策略框是否开启
    set_val('time_on', False)  # 操作面板上是否开启时间
    set_val('a_time', time.time())  # 国拍初始时间
    set_val('b_time', 0)  # 制作0.1秒
    set_val('moni_minute', 29)
    set_val('chujia_time', 0)  # 出价时间

    set_val('moni_on', False)  # 判断开启的是哪个窗口 ，限制同时只能开启一个
    set_val('guopai_on', False)
    set_val('listen_on', False)  #f是否开启监听

    set_val('current_moni', True) ##当前哪个WEB激活状态
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

    set_val('twice', False)  # 开启两次出价
    set_val('tijiao_num', 1)  # 开启二次出价，设置为2，执行一次之后，减1
    set_val('tijiao_one', False)  # 第一次出价之后开闭

    set_val('px_calculate_relative', 153)
    set_val('py_calculate_relative', 458)

    # self.jiajia_time.SetValue(40.0)
    # self.tijiao_time.SetValue(48.0)
    # self.jiajia_price.SetValue(500)
    # self.select_tijiao.SetSelection(2)
    # self.yanchi_time.SetValue(0.0)
    # self.jiajia_time2.SetValue(50.0)
    # self.tijiao_time2.SetValue(55.5)
    # self.jiajia_price2.SetValue(700)
    # self.select_tijiao2.SetSelection(0)
    # self.yanchi_time2.SetValue(0.5)

    ## 保存当前的设置
    current_setting = {
        'jiajia_time': 40.0,
        'tijiao_time': 48.0,
        'jiajia_price': 500,
        'select_tijiao': 2,
        'yanchi_time': 0.0,
        'jiajia_time2': 50.0,
        'tijiao_time2': 55.5,
        'jiajia_price2': 700,
        'select_tijiao2': 0,
        'yanchi_time2': 0.5,

    }

    set_val('current_setting', current_setting)

    set_val('confirm_on', False)  # 是否需要确认
    set_val('confirm_need', False)  # 启动确认识别
    set_val('confirm_one', False)  # 限制只产生一次进程
    set_val('refresh_on', False)  # 是否需要刷新
    set_val('refresh_need', False)  # 启动刷新识别
    set_val('refresh_one', False)  # 限制只产生一次进程
    set_val('chujia_interval', False)  # 出价间隔
    set_val('tijiao_interval', False)  # 提交间隔
    set_val('query_interval', False)  # 间隔
    set_val('query_on', False)  # 是否处于查询状态

    set_val('autotime_on', False)  #是否处理自动时间同步状态



def init_account():
    set_val('activate_status', 0)   ##0: 未激活
    set_val('strategy_name', '默认策略') #策略名称

    set_val('current_strategy_name', '') #当前策略
    set_val('current_strategy_status', 0)    ##当前所处状态

    set_val('Username', 0)  # 用户名
    set_val('Password', 0)  # 密码
    set_val('Identify_code', 0)  # 密码
    set_val('ip_address', '')  # 客户端ip

    set_val("test", False)  ##默认关闭测试模式

def init_status():
    ##状态框
    set_val('CurrentStatusFramePos', (426, 212))   ###相对WEBFRAME位置
    set_val('CurrentStatusFrameSize', (451,77))

    ##验证码放大框
    set_val('YanzhengmaFramePos', (450, 175))    ###相对WEBFRAME位置
    set_val('Yanzhengmasize', (400, 220))

    set_val('register_label', '未激活')
    set_val('netspeed_label', '网速: ')
    set_val('strategy_label', '策略: ')
    set_val('currenttime_label', '当前时间:')
    set_val('lowestpricelabel', '最低成交价')

    set_val('current_pricestatus_label', '等待第二次出价')
    one_time1 = get_val('one_time1')
    one_diff = get_val('one_diff')
    current_pricestatus = '{0}秒加{1}'.format(one_time1, one_diff)
    set_val('current_pricestatus', current_pricestatus)

    ##状态框三行
    set_val('status_time', (3, 15))
    set_val('lowestprice_text', (3, 45))
    set_val('pricelabeltext', (192, 15))
    set_val('pricetext', (345, 15))
    set_val('timestatustext', (192, 45))
    set_val('pricestatustext', (345, 45))




def init_smart():
    ##智能出价服务
    set_val('smart_ajust', False)  # 智能调整出价，默认关闭

    a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    b = a + ' ' + '11:29:50'
    a_time = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S'))  # 转时间戳   补个平均时差
    set_val('smart_ajust_time_guopai', a_time)  # 智能调整触发时间
    set_val('smart_ajust_time_moni', 50)  # 智能调整触发时间

    ## 完成智能出价
    set_val('smart_autoprice', False)  ##智能补枪
    set_val('smartprice_chujia', False) ##智能出价 出价启动状态
    set_val('smartprice_tijiao', False) ##智能出价 提交启动状态

##------------------------------------------------------------------------------------------
### 窗口左上角位置计算对应位置
def init_pos(Px, Py):
    '''
    PxPy     109  26
    px, py   262  474
    '''

    Position_frame =  get_val('Position_frame')
    # set_val('px_lowestprice', 153)
    # set_val('py_lowestprice', 458)
    '''
    px_calculate_relative, py_calculate_relative  为找到的价格位置与窗口相对关系
    '''
    px_calculate_relative = get_val('px_calculate_relative')
    py_calculate_relative = get_val('py_calculate_relative')
    set_val('Px_lowestprice', px_calculate_relative + Px)
    set_val('Py_lowestprice', py_calculate_relative + Py)
    Px_lowestprice = get_val('Px_lowestprice')
    Py_lowestprice = get_val('Py_lowestprice')
    set_val('Px_currenttime', Px_lowestprice - 27)  # 参考最低成交价位置
    set_val('Py_currenttime', Py_lowestprice - 14)
    P_relative2 = get_val('P_relative2')

    for i in range(len(Position_frame)):
        Position_frame[i][0] = Px_lowestprice + P_relative2[i][0]
        Position_frame[i][1] = Py_lowestprice + P_relative2[i][1]
    set_val('Position_frame', Position_frame)
    ##几个截图位置, 通过服务器传来的相对位置 进行计算
    refresh_area_relative = get_val('refresh_area_relative')
    confirm_area_relative = get_val('confirm_area_relative')
    yan_confirm_area_relative = get_val('yan_confirm_area_relative')
    Pos_controlframe_relative = get_val('Pos_controlframe_relative')
    Pos_yanzhengma_relative = get_val('Pos_yanzhengma_relative')  # 验证码所在位置
    Pos_yanzhengmaframe_relative = get_val('Pos_yanzhengmaframe_relative')  # 验证码框放置位置
    set_val('refresh_area', (refresh_area_relative[0] + Px_lowestprice, refresh_area_relative[1] + Py_lowestprice,
                             refresh_area_relative[2] + Px_lowestprice, refresh_area_relative[3] + Py_lowestprice))
    set_val('confirm_area', (confirm_area_relative[0] + Px_lowestprice, confirm_area_relative[1] + Py_lowestprice,
                             confirm_area_relative[2] + Px_lowestprice, confirm_area_relative[3] + Py_lowestprice))
    set_val('yan_confirm_area', (yan_confirm_area_relative[0] + Px_lowestprice,
                                 yan_confirm_area_relative[1] + Py_lowestprice,
                                 yan_confirm_area_relative[2] + Px_lowestprice,
                                 yan_confirm_area_relative[3] + Py_lowestprice))
    set_val('Pos_controlframe', (Pos_controlframe_relative[0] + Px_lowestprice,
                                 Pos_controlframe_relative[1] + Py_lowestprice))
    set_val('Pos_yanzhengma', (Position_frame[6][0] + Pos_yanzhengma_relative[0],
                               Position_frame[6][1] + Pos_yanzhengma_relative[1],
                               Position_frame[6][0] + Pos_yanzhengma_relative[2],
                               Position_frame[6][1] + Pos_yanzhengma_relative[3]))  # 验证码所在位置
    set_val('Pos_yanzhengmaframe', (Px_lowestprice + Pos_yanzhengmaframe_relative[0],
                                    Py_lowestprice + Pos_yanzhengmaframe_relative[1]))  # 验证码框放置位置

    set_val('Pos_timeframe', (245 - 344 + Px_lowestprice, 399 - 183 + Py_lowestprice))

    # set_val('Findpos_area', (Px + 100 , Py + 400, Px + 200, Py + 550))


    lowestprice_sizex = get_val('lowestprice_sizex')
    lowestprice_sizey = get_val('lowestprice_sizey')
    currenttime_sizex = get_val('currenttime_sizex')
    currenttime_sizey = get_val('currenttime_sizey')
    set_val('findpos_on', False)  # 无需定位
    set_val('yanzhengma_move', True)  # 需要定位
    set_val('lowest', (Px_lowestprice, Py_lowestprice, lowestprice_sizex + Px_lowestprice,
                       lowestprice_sizey + Py_lowestprice))
    Px_currenttime = get_val("Px_currenttime")
    Py_currenttime = get_val("Py_currenttime")
    set_val('currenttime', (Px_currenttime, Py_currenttime, Px_currenttime + currenttime_sizex,
                            Py_currenttime + currenttime_sizey))
    dis_x = 50
    dis_y = 100
    x1 = Px_lowestprice - dis_x  # 截图起始点
    y1 = Py_lowestprice - dis_y
    lowest = get_val('lowest')
    refresh_area = get_val('refresh_area')
    confirm_area = get_val('confirm_area')
    Pos_yanzhengma = get_val('Pos_yanzhengma')
    yan_confirm_area = get_val('yan_confirm_area')
    currenttime = get_val('currenttime')

    cal_area = (lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area, currenttime)  ## 构建截图区域
    use_area = []
    set_val('sc_area', (Px_lowestprice - dis_x, Py_lowestprice - dis_y, Px_lowestprice + 600, Py_lowestprice + 120))
    for i in range(len(cal_area)):
        temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
        use_area.append(temp)
    set_val('use_area', use_area)


    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
    set_val('bidnumber_js', bidnumber_js)
    set_val('bidpassword_js', bidpassword_js)
    set_val('idcard_js', idcard_js)

##初始化变量, 由服务器给定
def remote_variables(**kwargs):
    for key, value in kwargs.items():
        set_val(key, value)



####
def remote_init():
    ##用于计算 最低成交价位置
    set_val('px_relative', 118)  # 查找出来位置反算相对位置
    set_val('py_relative', 1)
    set_val('px_timerelative', 94)
    set_val('py_timerelative', 3)
    ## 相对于最低成交价位置
    #   ## 0:加价  1：出价 2：提交  3：刷新按钮   4 ：确认   5：价格输入框    6:验证码输入框     7：取消
    set_val('P_relative2', [[647, -98], [650, 8], [400, 89], [396, 14], [505, 68], [562, 8], [585, 8], [586, 86]])
    P_relative2 = get_val('P_relative2')
    set_val('Position_frame', [[0, 0] for i in range(len(P_relative2))])
    ## 限定截图位置
    set_val('refresh_area_relative', [396 - 150, 11 - 100, 396 + 150, 11 + 100])
    set_val('confirm_area_relative', [505 - 60, 68 - 40, 505 + 60, 68 + 40])
    set_val('yan_confirm_area_relative', [205 - 60, 68 - 40, 405 + 60, 68 + 40])
    set_val('Pos_controlframe_relative', [192 - 344, 514 - 183])
    set_val('Pos_yanzhengma_relative', [-277, - 65, - 97, + 45])  # 验证码所在位置
    set_val('Pos_yanzhengmaframe_relative', [297, - 283])  # 验证码框放置位置

    ##计算当天的时间
    set_val('timebase_str', '')  ##时间基数，避免重复计算
    set_val('target_time', 11111111111111111)  ##时间基数，避免重复计算  11:30:1 分的时间戳
    set_val('start_time', 111111111111111)  ## 11点之后的时间
    set_val('final_time', 111111111111)

    set_val('final_stage', True)  ##判断是不是处理最终状态

    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
    set_val('bidnumber_js', bidnumber_js)
    set_val('bidpassword_js', bidpassword_js)
    set_val('idcard_js', idcard_js)