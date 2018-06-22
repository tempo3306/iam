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

# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance


# import threading
#
# class Singleton(object):
#
#     INSTANCE = None
#
#     lock = threading.RLock()
#
#     def __new__(cls):
#         cls.lock.acquire()
#         if cls.INSTANCE is None:
#             cls.INSTANCE = super(Singleton, cls).__new__(cls)
#         cls.lock.release()
#         return cls.INSTANCE


import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


def Singleton(cls):
    instances = {}

    @synchronized
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


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




class Hotkey_label():
    SMART_PRICE_LABEL = '智能出价'
    SMART_PRICE = 'ESC'
    REFRESH_WEB_LABEL = '刷新页面'
    REFRESH_WEB = 'F5'
    FORCE_TIJIAO_LABEL = '强制提交'
    FORCE_TIJIAO = 'F1'
    CLEAR_YAN_LABEL = '清空验证码'
    CLEAR_YAN = '空格'



# 变量初始化
####初始化hash字典
def Create_hash():
    with open("target.tkl", 'rb')  as tar:
        global dick_target
        dick_target = pickle.load(tar)  # 要寻找对象的对象
        V_global.dick_target = dick_target

##price_list 价格对应时间的表
price_list = [80000 for i in range(60)]  #0-59

def get_id_hash(id):
    import hashlib
    sha1 = hashlib.sha1()
    sha1.update(id.encode('utf-8'))
    return sha1.hexdigest()

@Singleton
class V_global(Singleton):
    userprice = 0 ##当前出价 如果为0则表示未出价
    usertime = -1 ##当前截止时间 如果为 -1表示未出价
    debug = True
    now_ping = 0 ##实时网速
    version = '1.0'
    num = 0
    avt = 0
    test = False

    # def init_url():
    remotetime_url = "https://hupai.pro/api/bid/get_remotetime"
    host_ali = "https://hupai.pro"
    # set_val('host_ali', "http://192.168.3.20:3000")
    url_51 = "http://moni.51hupai.org/"
    url_dianxin = "http://test.alltobid.com/moni/gerenlogin.html" ## 电信
    # set_val('url_dianxin', "https://www.baidu.com")  # 电信
    url_nodianxin = "http://moni.51hupai.org/" ## 非电信
    # set_val('url_moni', "http://test.alltobid.com/moni/gerenlogin.html")
    url_moni = "https://hupai.pro/static/main/moni.html"
    # set_val('url_moni', "http://192.168.3.20:3000/static/main/moni.html")
    guopai_dianxin = False ##当前是否处于国拍电信  默认是非电信


    # def init_label():
    moni_webstatus_label = '模拟中'
    dianxin_webstatus_label = '国拍电信'
    nodianxin_webstatus_label = '国拍非电信'
    urlchange_dianxin_label = '切换线路'
    urlchange_nodianxin_label = '切换线路'

    # def init_id():
    userconfirm_on = False
    topframe = -1
    loginframe = -1
    moni_webframe = -1
    guopai_webframe = -1

    # def init_size():
    ##webframe相关
    websize = (1148,715) ## webframe大小
    webview_pos = (-5,-16) ## WEB在 WEBVIEW里的相对位置
    buttonpanel_size = (892,30)
    buttonpanel_pos = (0,0)
    htmlsize = [918,768]
    htmlpanel_size = (892,628)
    htmlpanel_pos = (0,30)
    bottomestatusbarpanel_size = (892,30)
    bottomestatusbarpanel_pos = (0,658)


    x0 = websize[0] - htmlpanel_size[0]
    operationpanel_size = (x0,websize[1])
    operationpanel_pos = (htmlpanel_size[0],0)

    Pxy = (win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)) ## 分辨率
    Px1 = Pxy[0]/2 ## 屏幕中心位置
    Py2 = Pxy[1]/2
    Px = int((Pxy[0]-websize[0])/2)
    Py = int((Pxy[1]-websize[1])/2)-10

    ####定一个截图位置
    # sc_region = (Px, Py, Px +  )

    P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]] # 各按钮相对于WEB位置


    px_ajust = 0
    py_ajust = 0
    px_price = 770-171
    py_price = 260
    px_priceframe = 220-191
    py_priceframe = 480
    px_timeframe = 22
    py_timeframe = 348
    px_lowestpriceframe = 245
    py_lowestpriceframe = 290
    lowestpriceframe_pos = [px_lowestpriceframe,py_lowestpriceframe]
    px_yanzhengmaframe = 400-215
    py_yanzhengmaframe = 460
    px_mini = 200
    py_mini = 40
    Pricesize = [400,80]
    Timesize = [200,50]
    lowestprice_area = [179-80+Px,424-50+Py,179+80+Px,424+50+Py]
    refresh_area = [396-150,11-100,396+150,11+100]
    confirm_area = [505-300,68-150,505+300,68+150]
    yan_confirm_area = [505-300,68-150,505+300,68+150]
    ghostbutton_pos = [0,0]
    Px_price = Px+px_price
    Py_price = Py+py_price
    Pos_price = [Px_price,Py_price,Px_price+px_mini,Py_price+py_mini] ## 所出价格截图位置BOX
    Pos_yanzhengma = [] ## 验证码所在位置
    Px_priceframe = Px+px_priceframe
    Py_priceframe = Py+py_priceframe
    Pos_priceframe = [Px_priceframe,Py_priceframe]
    Px_timeframe = px_timeframe+Px
    Py_timeframe = py_timeframe+Py
    Pos_timeframe = [Px_timeframe,Py_timeframe]
    Pos_controlframe = [Px+40,Py+480]
    Px_yanzhengmaframe = Px+px_yanzhengmaframe
    Py_yanzhengmaframe = Py+py_yanzhengmaframe
    Pos_yanzhengmaframe = [Px_yanzhengmaframe,Py_yanzhengmaframe]
    px_lowestprice = 0 ## 206   209 208 截图相对位置
    py_lowestprice = 0 ## 412  416
    Px_lowestprice = Px+px_lowestprice
    Py_lowestprice = Py+py_lowestprice
    lowestprice_sizex = 82 ## 截图范围 41
    lowestprice_sizey = 16

    currenttime_sizex = 132
    currenttime_sizey = 13

    px_confirm = 656
    py_confirm = 475
    Px_confirm = Px+px_confirm
    Py_confirm = Py+py_confirm
    confirm_sizex = 113
    confirm_sizey = 28
    px_refresh = 550
    py_refresh = 413
    Px_refresh = Px+px_refresh
    Py_refresh = Py+py_refresh
    refresh_sizex = 108
    refresh_sizey = 21
    sc_area = [Px_lowestprice-10,Py_lowestprice-100,Px_lowestprice+600,Py_lowestprice+120]
    use_area = []
    nptemp = []
    imgpos_lowestprice = np.array(nptemp) ## 最低成交价
    imgpos_refresh = np.array(nptemp) ## 刷新按钮
    imgpos_confirm = np.array(nptemp) ## 出价完后确认
    impos_yanzhengma = np.array(nptemp) ## 验证码
    imgpos_yanzhengmaconfirm = np.array(nptemp) ## 验证码确认键
    imgpos_currenttime = np.array(nptemp) ## 当前时间




    # '''
    # 214 645
    # 215 224
    # '''

    #
    # def init_strategy():
    strategy_choices = ['单枪策略(专注一次出价)', '双枪策略(一伏二补)', '单枪策略 智能提交', '双枪策略 智能提交']
    strategy_choices = strategy_choices


    tijiao_choices = [u"提前100", u"提前200", u"提前300", u"踩点"]
    tijiao_choices = tijiao_choices

    mainicon = 'logo.ico'
    view = False ## 定位显示
    hotkey_on = False ## 开启辅助
    ad_view = False ## 显示广告
    price_view = False ## 显示价格,控制截图
    yanzhengma_view = False ## 验证码放大,控制截图+-
    yanzhengma_close = True ## 关闭验证码放大窗
    yanzhengma_control = True ## 判定是否需要查找验证码确认
    yanzhengma_find = True ## 验证码是否找到 默认True 发现需要查找 之后变为False
    yanzhengma_move = True ## 是否需要移动
    yanzhengma_hash = 0 ## 前一个验证码截图  如果变化就刷新 ，不变化就不动作
    yanzhengma_change = True ##判定是否变化

    price_on = False ## 价格是否显示
    price_count = 0 ## 辅助计时，正确显示价格
    yanzhengma_count = 0 ## 辅助计时，正确显示价格
    web_on = False ## 监测web是否开启
    view_time = False ## 时间框是否开启
    operation_show = False ## 策略框是否开启
    time_on = False ## 操作面板上是否开启时间
    a_time = time.time() ## 国拍初始时间
    b_time = 0 ## 制作0.1秒
    moni_minute = 29
    chujia_time = 0 ## 出价时间

    moni_on = False ## 判断开启的是哪个窗口 ，限制同时只能开启一个
    guopai_on = False
    listen_on = False ##f是否开启监听

    current_moni = True ##当前哪个WEB激活状态
    strategy1 = 53 ## 策略整数时间
    strategy2 = 0.0 ## 策略小数时间
    strategy_on = True ## 策略是否开启
    strategy_repeat = False ## 判断是否重复，避免重复进程
    delay = False ## 是否延迟
    delay_time = 0.5 ## 延迟大小设置
    login_result = False ## 登录成功与否
    findpos_on = True ## 控制是否找位置
    lowestpricelist = [80000 + i*100 for i in range(400)] ## 用于验证识别
    IDnumber = 0 ## 身份证号
    account = 0 ## 标书号
    passwd = 0 ## 密码
    changetime = 0
    one_time1 = 48 ## 第一次出价加价
    one_time2 = 55 ## 第一次出价提交
    one_real_time1 = 1000000000000 ## 换算之后的出价时间
    one_real_time2 = 1000000000000 ## 换算之后的提交时间
    one_diff = 700 ## 第一次加价幅度
    one_delay = 0.5 ## 第一次延迟
    one_advance = 100 ## 第一次提交提前量
    second_time1 = 48 ## 第二次次出价加价
    second_time2 = 55 ## 第二次出价提交
    second_real_time1 = 1000000000000 ## 换算之后的出价时间
    second_real_time2 = 1000000000000 ## 换算之后的提交时间
    second_diff = 600 ## 第二次加价幅度
    second_delay = 0.5 ## 第二次出价延迟
    second_advance = 100 ## 第二次出价提交提前量
    osl = [0]*15 ## 策略容器初始化   判定+10参数+确认选项
    chujia_on = True ## 完成一次出价之后关闭，完成出价后关闭
    tijiao_on = False ## 是否需要提交,完成提交后打开
    lowest_price = 93400 ## 最低成交价
    own_price1 = 0 ## 第一次出价
    own_price2 = 0 ## 第二次出价
    own_price = 0 ## 当前出价
    tijiao_OK = False ## 表示输完验证码

    twice = False ## 开启两次出价
    tijiao_num = 1 ## 开启二次出价，设置为2，执行一次之后，减1
    tijiao_one = False ## 第一次出价之后开闭

    px_calculate_relative = 153
    py_calculate_relative = 458

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


    confirm_on = False ## 是否需要确认
    confirm_need = False ## 启动确认识别
    confirm_one = False ## 限制只产生一次进程
    refresh_on = False ## 是否需要刷新
    refresh_need = False ## 启动刷新识别
    refresh_one = False ## 限制只产生一次进程
    chujia_interval = False ## 出价间隔
    tijiao_interval = False ## 提交间隔
    query_interval = False ## 间隔
    query_on = False ## 是否处于查询状态

    autotime_on = False ##是否处理自动时间同步状态


    ##调整策略范围
    timelist = [400 + i * 1 for i in range(191)]
    yanchilist = [0 + i * 1 for i in range(20)]
    pricelist = [300 + i * 100 for i in range(13)]

    timelist = timelist
    yanchilist = yanchilist
    pricelist = pricelist

    # def init_account():
    activate_status = 0 ##0: 未激活
    strategy_name = '默认策略' ##策略名称

    current_strategy_name = '' ##当前策略
    current_strategy_status = 0 ##当前所处状态

    Username = 0 ## 用户名
    Password = 0 ## 密码
    Identify_code = 0 ## 密码
    ip_address = '' ## 客户端ip

    test = False ##默认关闭测试模式

    # def init_status():
    ##状态框
    CurrentStatusFramePos = (426,212) ##相对WEBFRAME位置
    CurrentStatusFrameSize = (464,77)

    ##验证码放大框
    YanzhengmaFramePos = (450,175) ##相对WEBFRAME位置
    Yanzhengmasize = (400,220)

    register_label = '未激活'
    netspeed_label = '网速:'
    strategy_label = '策略:'
    currenttime_label = '当前时间:'
    lowestpricelabel = '最低成交价'

    current_pricestatus_label = '等待第二次出价'

    current_pricestatus = '{0}秒加{1}'.format(one_time1, one_diff)

    ##状态框三行
    status_time = (3,15)
    lowestprice_text = (3,45)
    pricelabeltext = (192,15)
    pricetext = (345,15)
    timestatustext = (192,45)
    pricestatustext = (345,45)



    ##############################################
    ##服务器决定
    #--------------------------------------------
    ##用于计算 最低成交价位置
    px_relative = 1  ## 查找出来位置反算相对位置
    py_relative = 10
    px_timerelative = 22
    py_timerelative = 5
    ## 相对于最低成交价位置
    #   ## 0:加价  1：出价 2：提交  3：刷新按钮   4 ：确认   5：价格输入框    6:验证码输入框     7：取消
    P_relative2 = [[647, 98], [650, 78], [440, 89], [196, 14], [575, 68], [51, 68], [385, 8], [186, 86]]
    Position_frame = [[0, 0] for i in range(len(P_relative2))]
    ## 限定截图位置
    refresh_area_relative = [36 - 150, 11 - 100, 396 + 150, 11 + 100]
    confirm_area_relative = [55 - 60, 668 - 40, 505 + 60, 61 + 40]
    yan_confirm_area_relative = [205 - 60, 68 - 410, 405 + 60, 68 + 40]
    Pos_controlframe_relative = [192 - 3474, 564 - 183]
    Pos_yanzhengma_relative = [-21, -65, -97, +145]  ## 验证码所在位置
    Pos_yanzhengmaframe_relative = [217, -483]  ## 验证码框放置位置

    ##计算当天的时间
    timebase_str = ''  ##时间基数，避免重复计算
    target_time = 11111111111111111  ##时间基数，避免重复计算  11:30:1 分的时间戳
    start_time = 111111111111111  ## 11点之后的时间
    final_time = 111111111111

    final_stage = True  ##判断是不是处理最终状态

    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)


    # def init_smart():
    ##智能出价服务
    smart_ajust = False ## 智能调整出价，默认关闭

    a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    b = a + ' ' + '11:29:50'
    a_time = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S'))  # 转时间戳   补个平均时差
    smart_ajust_time_guopai = a_time ## 智能调整触发时间
    smart_ajust_time_moni = 50 ## 智能调整触发时间

    ## 完成智能出价
    smart_autoprice = False ##智能补枪
    smartprice_chujia = False ##智能出价 出价启动状态
    smartprice_tijiao = False ##智能出价 提交启动状态

    ##------------------------------------------------------------------------------------------
    ### 窗口左上角位置计算对应位置
    # def init_pos(Px, Py):
    # '''
    # PxPy     109  26
    # px, py   262  474
    # '''

    # set_val('px_lowestprice', 153)
    # set_val('py_lowestprice', 458)
    #     '''
    #     px_calculate_relative, py_calculate_relative  为找到的价格位置与窗口相对关系
    #     '''

    Px_lowestprice = px_calculate_relative+Px
    Py_lowestprice = py_calculate_relative+Py
    Px_currenttime = Px_lowestprice-27 ## 参考最低成交价位置
    Py_currenttime = Py_lowestprice-14

    for i in range(len(Position_frame)):
        Position_frame[i][0] = Px_lowestprice + P_relative2[i][0]
        Position_frame[i][1] = Py_lowestprice + P_relative2[i][1]
        Position_frame = Position_frame

    refresh_area = (refresh_area_relative[0] + Px_lowestprice, refresh_area_relative[1] + Py_lowestprice,
                    refresh_area_relative[2] + Px_lowestprice, refresh_area_relative[3] + Py_lowestprice)

    confirm_area = (confirm_area_relative[0]+Px_lowestprice,confirm_area_relative[1]+Py_lowestprice,
                    confirm_area_relative[2] + Px_lowestprice, confirm_area_relative[3] + Py_lowestprice)

    yan_confirm_area = (yan_confirm_area_relative[0] + Px_lowestprice,
                        yan_confirm_area_relative[1] + Py_lowestprice,
                        yan_confirm_area_relative[2] + Px_lowestprice,
                        yan_confirm_area_relative[3] + Py_lowestprice)

    Pos_controlframe = (Pos_controlframe_relative[0]+ Px_lowestprice,
                        Pos_controlframe_relative[1] + Py_lowestprice)

    Pos_yanzhengma = (Position_frame[6][0]+Pos_yanzhengma_relative[0],
                      Position_frame[6][1] + Pos_yanzhengma_relative[1],
                      Position_frame[6][0] + Pos_yanzhengma_relative[2],
                      Position_frame[6][1] + Pos_yanzhengma_relative[3]) # 验证码所在位置

    Pos_yanzhengmaframe = (Px_lowestprice + Pos_yanzhengmaframe_relative[0],
                           Py_lowestprice + Pos_yanzhengmaframe_relative[1])  # 验证码框放置位置

    Pos_timeframe = (245-344+Px_lowestprice, 399-183+Py_lowestprice)

    # set_val('Findpos_area', (Px + 100 , Py + 400, Px + 200, Py + 550))


    findpos_on = False ## 无需定位
    yanzhengma_move = True ## 需要定位
    lowest = (Px_lowestprice,Py_lowestprice,lowestprice_sizex+Px_lowestprice,
              lowestprice_sizey + Py_lowestprice)

    currenttime = (Px_currenttime,Py_currenttime,Px_currenttime+currenttime_sizex,
                   Py_currenttime + currenttime_sizey)
    dis_x = 50
    dis_y = 100
    x1 = Px_lowestprice - dis_x  # 截图起始点
    y1 = Py_lowestprice - dis_y
    lowest =     lowest
    refresh_area =     refresh_area
    confirm_area =     confirm_area
    Pos_yanzhengma =     Pos_yanzhengma
    yan_confirm_area =     yan_confirm_area
    currenttime =     currenttime

    cal_area = (lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area, currenttime)  ## 构建截图区域
    use_area = []
    sc_area = (Px_lowestprice-dis_x,Py_lowestprice-dis_y,Px_lowestprice+600,Py_lowestprice+120)
    for i in range(len(cal_area)):
        temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
        use_area.append(temp)
        use_area = use_area


    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
    bidnumber_js = bidnumber_js
    bidpassword_js = bidpassword_js
    idcard_js = idcard_js

##初始化变量, 由服务器给定
def remote_variables(**kwargs):
    for key, value in kwargs.items():
        e = value



####
def remote_init():
    ##用于计算 最低成交价位置
    px_relative = 118 ## 查找出来位置反算相对位置
    py_relative = 1
    px_timerelative = 94
    py_timerelative = 3
    ## 相对于最低成交价位置
    #   ## 0:加价  1：出价 2：提交  3：刷新按钮   4 ：确认   5：价格输入框    6:验证码输入框     7：取消
    P_relative2 = [[647,-98],[650,8],[400,89],[396,14],[505,68],[562,8],[585,8],[586,86]]
    P_relative2 =     P_relative2
    Position_frame = [[0,0] for i in range(len(P_relative2))]
    ## 限定截图位置
    refresh_area_relative = [396-150,11-100,396+150,11+100]
    confirm_area_relative = [505-60,68-40,505+60,68+40]
    yan_confirm_area_relative = [205-60,68-40,405+60,68+40]
    Pos_controlframe_relative = [192-344,514-183]
    Pos_yanzhengma_relative = [-277,-65,-97,+45] ## 验证码所在位置
    Pos_yanzhengmaframe_relative = [297,-283] ## 验证码框放置位置

    ##计算当天的时间
    timebase_str = '' ##时间基数，避免重复计算
    target_time = 11111111111111111 ##时间基数，避免重复计算  11:30:1 分的时间戳
    start_time = 111111111111111 ## 11点之后的时间
    final_time = 111111111111

    final_stage = True ##判断是不是处理最终状态

    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)



## 窗口左上角位置计算对应位置
'''
PxPy     109  26
px, py   262  474
'''

# set_val('px_lowestprice', 153)
# set_val('py_lowestprice', 458)
#     '''
#     px_calculate_relative, py_calculate_relative  为找到的价格位置与窗口相对关系
#     '''
def init_pos(Px, Py):
    V_global.Px_lowestprice = V_global.px_calculate_relative + Px
    V_global.Py_lowestprice =  V_global.py_calculate_relative + Py
    V_global.Px_currenttime = V_global.Px_lowestprice - 27 ## 参考最低成交价位置
    V_global.Py_currenttime = V_global.Py_lowestprice - 14
    Position_frame = V_global.Position_frame
    P_relative2 = V_global.P_relative2
    refresh_area_relative = V_global.refresh_area_relative
    confirm_area_relative = V_global.confirm_area_relative
    yan_confirm_area_relative = V_global.yan_confirm_area_relative
    Pos_controlframe_relative = V_global.Pos_controlframe_relative
    Pos_yanzhengma_relative = V_global.Pos_yanzhengma_relative
    Pos_yanzhengmaframe_relative = V_global.Pos_yanzhengmaframe_relative
    lowestprice_sizex = V_global.lowestprice_sizex
    lowestprice_sizey = V_global.lowestprice_sizey
    currenttime_sizex = V_global.currenttime_sizex
    currenttime_sizey= V_global.currenttime_sizey
    for i in range(len(Position_frame)):
        Position_frame[i][0] = V_global.Px_lowestprice + P_relative2[i][0]
        Position_frame[i][1] = V_global.Py_lowestprice + P_relative2[i][1]
        Position_frame = Position_frame

    V_global.refresh_area = (refresh_area_relative[0] + V_global.Px_lowestprice, refresh_area_relative[1] + V_global.Py_lowestprice,
                             refresh_area_relative[2] + V_global.Px_lowestprice, refresh_area_relative[3] + V_global.Py_lowestprice)

    V_global.confirm_area = (confirm_area_relative[0]+V_global.Px_lowestprice,confirm_area_relative[1]+V_global.Py_lowestprice,
                             confirm_area_relative[2] + V_global.Px_lowestprice, confirm_area_relative[3] + V_global.Py_lowestprice)

    V_global.yan_confirm_area = (yan_confirm_area_relative[0] + V_global.Px_lowestprice,
                                 yan_confirm_area_relative[1] + V_global.Py_lowestprice,
                                 yan_confirm_area_relative[2] + V_global.Px_lowestprice,
                                 yan_confirm_area_relative[3] + V_global.Py_lowestprice)

    V_global.Pos_controlframe = (Pos_controlframe_relative[0]+ V_global.Px_lowestprice,
                                 Pos_controlframe_relative[1] + V_global.Py_lowestprice)

    V_global.Pos_yanzhengma = (Position_frame[6][0]+Pos_yanzhengma_relative[0],
                               Position_frame[6][1] + Pos_yanzhengma_relative[1],
                               Position_frame[6][0] + Pos_yanzhengma_relative[2],
                               Position_frame[6][1] + Pos_yanzhengma_relative[3]) # 验证码所在位置

    V_global.Pos_yanzhengmaframe = (V_global.Px_lowestprice + Pos_yanzhengmaframe_relative[0],
                                    V_global.Py_lowestprice + Pos_yanzhengmaframe_relative[1])  # 验证码框放置位置

    V_global.Pos_timeframe = (245-344+V_global.Px_lowestprice, 399-183+V_global.Py_lowestprice)

    # set_val('Findpos_area', (Px + 100 , Py + 400, Px + 200, Py + 550))

    V_global.findpos_on = False ## 无需定位
    V_global.yanzhengma_move = True ## 需要定位
    V_global.lowest = (V_global.Px_lowestprice,V_global.Py_lowestprice,lowestprice_sizex+V_global.Px_lowestprice,
                       lowestprice_sizey + V_global.Py_lowestprice)

    V_global.currenttime = (V_global.Px_currenttime,V_global.Py_currenttime,V_global.Px_currenttime+currenttime_sizex,
                            V_global.Py_currenttime + currenttime_sizey)
    dis_x = 50
    dis_y = 100
    x1 = V_global.Px_lowestprice - dis_x  # 截图起始点
    y1 = V_global.Py_lowestprice - dis_y

    V_global.cal_area = (V_global.lowest,V_global.refresh_area, V_global.confirm_area, V_global.Pos_yanzhengma,
                         V_global.yan_confirm_area, V_global.currenttime)  ## 构建截图区域
    use_area = []
    V_global.sc_area = (V_global.Px_lowestprice-dis_x,V_global.Py_lowestprice-dis_y,
                        V_global.Px_lowestprice+600,V_global.Py_lowestprice+120)
    cal_area = V_global.cal_area
    for i in range(len(cal_area)):
        temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
        use_area.append(temp)
        V_global.use_area = use_area


b = V_global()