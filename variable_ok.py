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

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance




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

class V_global(Singleton):
    a = 1


V_global.price_list = price_list


V_global.userprice = 0 ##当前出价 如果为0则表示未出价
V_global.usertime = -1 ##当前截止时间 如果为 -1表示未出价

# set_val('host_ali', "http://192.168.3.20:3000")
V_global.debug = True
V_global.now_ping = 0 ##实时网速
V_global.version = '1.0'
V_global.num = 0
V_global.avt = 0
V_global.test = False



# def init_url():
V_global.remotetime_url = "https://hupai.pro/api/bid/get_remotetime"
V_global.host_ali = "https://hupai.pro"
# set_val('host_ali', "http://192.168.3.20:3000")
V_global.url_51 = "http://moni.51hupai.org/"
V_global.url_dianxin = "http://test.alltobid.com/moni/gerenlogin.html" ## 电信
# set_val('url_dianxin', "https://www.baidu.com")  # 电信
V_global.url_nodianxin = "http://moni.51hupai.org/" ## 非电信
# set_val('url_moni', "http://test.alltobid.com/moni/gerenlogin.html")
V_global.url_moni = "https://hupai.pro/static/main/moni.html"
# set_val('url_moni', "http://192.168.3.20:3000/static/main/moni.html")
V_global.guopai_dianxin = False ##当前是否处于国拍电信  默认是非电信


# def init_label():
V_global.moni_webstatus_label = '模拟中'
V_global.dianxin_webstatus_label = '国拍电信'
V_global.nodianxin_webstatus_label = '国拍非电信'
V_global.urlchange_dianxin_label = '切换线路'
V_global.urlchange_nodianxin_label = '切换线路'

# def init_id():
V_global.userconfirm_on = False
V_global.topframe = -1
V_global.loginframe = -1
V_global.moni_webframe = -1
V_global.guopai_webframe = -1

# def init_size():
    ##webframe相关
V_global.websize = (1148,715) ## webframe大小
V_global.webview_pos = (-5,-16) ## WEB在 WEBVIEW里的相对位置
V_global.buttonpanel_size = (892,30)
V_global.buttonpanel_pos = (0,0)
V_global.htmlsize = [918,768]
V_global.htmlpanel_size = (892,628)
V_global.htmlpanel_pos = (0,30)
V_global.bottomestatusbarpanel_size = (892,30)
V_global.bottomestatusbarpanel_pos = (0,658)

websize = V_global.websize
htmlpanel_size = V_global.htmlpanel_size
x0 = websize[0] - htmlpanel_size[0]
V_global.operationpanel_size = (x0,websize[1])
V_global.operationpanel_pos = (htmlpanel_size[0],0)

websize = V_global.websize
V_global.Pxy = (win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)) ## 分辨率
Pxy = V_global.Pxy
V_global.Px1 = Pxy[0]/2 ## 屏幕中心位置
V_global.Py2 = Pxy[1]/2
V_global.Px = int((Pxy[0]-websize[0])/2)
Px = V_global.Px
V_global.Py = int((Pxy[1]-websize[1])/2)-10
Py = V_global.Py

####定一个截图位置
# sc_region = (Px, Py, Px +  )

V_global.P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]] # 各按钮相对于WEB位置
P_relative = V_global.P_relative


V_global.px_ajust = 0
V_global.py_ajust = 0
V_global.px_price = 770-171
px_price = V_global.px_price
V_global.py_price = 260
py_price = V_global.py_price
V_global.px_priceframe = 220-191
px_priceframe = V_global.px_priceframe
V_global.py_priceframe = 480
py_priceframe = V_global.py_priceframe
V_global.px_timeframe = 22
px_timeframe = V_global.px_timeframe
V_global.py_timeframe = 348
py_timeframe = V_global.py_timeframe
V_global.px_lowestpriceframe = 245
px_lowestpriceframe = V_global.px_lowestpriceframe
V_global.py_lowestpriceframe = 290
py_lowestpriceframe = V_global.py_lowestpriceframe
V_global.lowestpriceframe_pos = [px_lowestpriceframe,py_lowestpriceframe]
V_global.px_yanzhengmaframe = 400-215
px_yanzhengmaframe = V_global.px_yanzhengmaframe
V_global.py_yanzhengmaframe = 460
py_yanzhengmaframe = V_global.py_yanzhengmaframe
V_global.px_mini = 200
px_mini = V_global.px_mini
V_global.py_mini = 40
py_mini = V_global.py_mini
V_global.Pricesize = [400,80]
V_global.Timesize = [200,50]
V_global.lowestprice_area = [179-80+Px,424-50+Py,179+80+Px,424+50+Py]
V_global.refresh_area = [396-150,11-100,396+150,11+100]
V_global.confirm_area = [505-300,68-150,505+300,68+150]
V_global.yan_confirm_area = [505-300,68-150,505+300,68+150]
V_global.ghostbutton_pos = [0,0]
V_global.Px_price = Px+px_price
Px_price = V_global.Px_price
V_global.Py_price = Py+py_price
Py_price = V_global.Py_price
V_global.Pos_price = [Px_price,Py_price,Px_price+px_mini,Py_price+py_mini] ## 所出价格截图位置BOX
V_global.Pos_yanzhengma = [] ## 验证码所在位置
V_global.Px_priceframe = Px+px_priceframe
Px_priceframe = V_global.Px_priceframe
V_global.Py_priceframe = Py+py_priceframe
Py_priceframe = V_global.Py_priceframe
V_global.Pos_priceframe = [Px_priceframe,Py_priceframe]
V_global.Px_timeframe = px_timeframe+Px
Px_timeframe = V_global.Px_timeframe
V_global.Py_timeframe = py_timeframe+Py
Py_timeframe = V_global.Py_timeframe
V_global.Pos_timeframe = [Px_timeframe,Py_timeframe]
V_global.Pos_controlframe = [Px+40,Py+480]
V_global.Px_yanzhengmaframe = Px+px_yanzhengmaframe
Px_yanzhengmaframe = V_global.Px_yanzhengmaframe
V_global.Py_yanzhengmaframe = Py+py_yanzhengmaframe
Py_yanzhengmaframe = V_global.Py_yanzhengmaframe
V_global.Pos_yanzhengmaframe = [Px_yanzhengmaframe,Py_yanzhengmaframe]
V_global.px_lowestprice = 0 ## 206   209 208 截图相对位置
px_lowestprice = V_global.px_lowestprice
V_global.py_lowestprice = 0 ## 412  416
py_lowestprice = V_global.py_lowestprice
V_global.Px_lowestprice = Px+px_lowestprice
Px_lowestprice = V_global.Px_lowestprice
V_global.Py_lowestprice = Py+py_lowestprice
Py_lowestprice = V_global.Py_lowestprice
V_global.lowestprice_sizex = 82 ## 截图范围 41
V_global.lowestprice_sizey = 16
V_global.Px_currenttime = Px_lowestprice-25 ## 参考最低成交价位置
V_global.Py_currenttime = Py_lowestprice+17
V_global.currenttime_sizex = 132
V_global.currenttime_sizey = 13

V_global.px_confirm = 656
px_confirm = V_global.px_confirm
V_global.py_confirm = 475
py_confirm = V_global.py_confirm
V_global.Px_confirm = Px+px_confirm
V_global.Py_confirm = Py+py_confirm
V_global.confirm_sizex = 113
V_global.confirm_sizey = 28
V_global.px_refresh = 550
px_refresh = V_global.px_refresh
V_global.py_refresh = 413
py_refresh = V_global.py_refresh
V_global.Px_refresh = Px+px_refresh
V_global.Py_refresh = Py+py_refresh
V_global.refresh_sizex = 108
V_global.refresh_sizey = 21
V_global.sc_area = [Px_lowestprice-10,Py_lowestprice-100,Px_lowestprice+600,Py_lowestprice+120]
V_global.use_area = []
V_global.nptemp = []
nptemp = V_global.nptemp
V_global.imgpos_lowestprice = np.array(nptemp) ## 最低成交价
V_global.imgpos_refresh = np.array(nptemp) ## 刷新按钮
V_global.imgpos_confirm = np.array(nptemp) ## 出价完后确认
V_global.impos_yanzhengma = np.array(nptemp) ## 验证码
V_global.imgpos_yanzhengmaconfirm = np.array(nptemp) ## 验证码确认键
V_global.imgpos_currenttime = np.array(nptemp) ## 当前时间




'''
214 645
215 224
'''

#
# def init_strategy():
strategy_choices = ['单枪策略(专注一次出价)', '双枪策略(一伏二补)', '单枪策略 智能提交', '双枪策略 智能提交']
V_global.strategy_choices = strategy_choices


tijiao_choices = [u"提前100", u"提前200", u"提前300", u"踩点"]
V_global.tijiao_choices = tijiao_choices

V_global.mainicon = 'logo.ico'
V_global.view = False ## 定位显示
V_global.hotkey_on = False ## 开启辅助
V_global.ad_view = False ## 显示广告
V_global.price_view = False ## 显示价格,控制截图
V_global.yanzhengma_view = False ## 验证码放大,控制截图+-
V_global.yanzhengma_close = True ## 关闭验证码放大窗
V_global.yanzhengma_control = True ## 判定是否需要查找验证码确认
V_global.yanzhengma_find = True ## 验证码是否找到 默认True 发现需要查找 之后变为False
V_global.yanzhengma_move = True ## 是否需要移动
V_global.yanzhengma_hash = 0 ## 前一个验证码截图  如果变化就刷新 ，不变化就不动作
V_global.yanzhengma_change = True ##判定是否变化

V_global.price_on = False ## 价格是否显示
V_global.price_count = 0 ## 辅助计时，正确显示价格
V_global.yanzhengma_count = 0 ## 辅助计时，正确显示价格
V_global.web_on = False ## 监测web是否开启
V_global.view_time = False ## 时间框是否开启
V_global.operation_show = False ## 策略框是否开启
V_global.time_on = False ## 操作面板上是否开启时间
V_global.a_time = time.time() ## 国拍初始时间
V_global.b_time = 0 ## 制作0.1秒
V_global.moni_minute = 29
V_global.chujia_time = 0 ## 出价时间

V_global.moni_on = False ## 判断开启的是哪个窗口 ，限制同时只能开启一个
V_global.guopai_on = False
V_global.listen_on = False ##f是否开启监听

V_global.current_moni = True ##当前哪个WEB激活状态
V_global.strategy1 = 53 ## 策略整数时间
V_global.strategy2 = 0.0 ## 策略小数时间
V_global.strategy_on = True ## 策略是否开启
V_global.strategy_repeat = False ## 判断是否重复，避免重复进程
V_global.delay = False ## 是否延迟
V_global.delay_time = 0.5 ## 延迟大小设置
V_global.login_result = False ## 登录成功与否
V_global.findpos_on = True ## 控制是否找位置
V_global.lowestpricelist = [80000 + i*100 for i in range(400)] ## 用于验证识别
V_global.IDnumber = 0 ## 身份证号
V_global.account = 0 ## 标书号
V_global.passwd = 0 ## 密码
V_global.changetime = 0
V_global.one_time1 = 48 ## 第一次出价加价
V_global.one_time2 = 55 ## 第一次出价提交
V_global.one_real_time1 = 1000000000000 ## 换算之后的出价时间
V_global.one_real_time2 = 1000000000000 ## 换算之后的提交时间
V_global.one_diff = 700 ## 第一次加价幅度
V_global.one_delay = 0.5 ## 第一次延迟
V_global.one_advance = 100 ## 第一次提交提前量
V_global.second_time1 = 48 ## 第二次次出价加价
V_global.second_time2 = 55 ## 第二次出价提交
V_global.second_real_time1 = 1000000000000 ## 换算之后的出价时间
V_global.second_real_time2 = 1000000000000 ## 换算之后的提交时间
V_global.second_diff = 600 ## 第二次加价幅度
V_global.second_delay = 0.5 ## 第二次出价延迟
V_global.second_advance = 100 ## 第二次出价提交提前量
V_global.osl = [0]*15 ## 策略容器初始化   判定+10参数+确认选项
V_global.chujia_on = True ## 完成一次出价之后关闭，完成出价后关闭
V_global.tijiao_on = False ## 是否需要提交,完成提交后打开
V_global.lowest_price = 93400 ## 最低成交价
V_global.own_price1 = 0 ## 第一次出价
V_global.own_price2 = 0 ## 第二次出价
V_global.own_price = 0 ## 当前出价
V_global.tijiao_OK = False ## 表示输完验证码

V_global.twice = False ## 开启两次出价
V_global.tijiao_num = 1 ## 开启二次出价，设置为2，执行一次之后，减1
V_global.tijiao_one = False ## 第一次出价之后开闭

V_global.px_calculate_relative = 153
V_global.py_calculate_relative = 458

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

V_global.current_setting = current_setting

V_global.confirm_on = False ## 是否需要确认
V_global.confirm_need = False ## 启动确认识别
V_global.confirm_one = False ## 限制只产生一次进程
V_global.refresh_on = False ## 是否需要刷新
V_global.refresh_need = False ## 启动刷新识别
V_global.refresh_one = False ## 限制只产生一次进程
V_global.chujia_interval = False ## 出价间隔
V_global.tijiao_interval = False ## 提交间隔
V_global.query_interval = False ## 间隔
V_global.query_on = False ## 是否处于查询状态

V_global.autotime_on = False ##是否处理自动时间同步状态


##调整策略范围
timelist = [400 + i * 1 for i in range(191)]
yanchilist = [0 + i * 1 for i in range(20)]
pricelist = [300 + i * 100 for i in range(13)]

V_global.timelist = timelist
V_global.yanchilist = yanchilist
V_global.pricelist = pricelist

# def init_account():
V_global.activate_status = 0 ##0: 未激活
V_global.strategy_name = '默认策略' ##策略名称

V_global.current_strategy_name = '' ##当前策略
V_global.current_strategy_status = 0 ##当前所处状态

V_global.Username = 0 ## 用户名
V_global.Password = 0 ## 密码
V_global.Identify_code = 0 ## 密码
V_global.ip_address = '' ## 客户端ip

V_global.test = False ##默认关闭测试模式

# def init_status():
##状态框
V_global.CurrentStatusFramePos = (426,212) ##相对WEBFRAME位置
V_global.CurrentStatusFrameSize = (464,77)

##验证码放大框
V_global.YanzhengmaFramePos = (450,175) ##相对WEBFRAME位置
V_global.Yanzhengmasize = (400,220)

V_global.register_label = '未激活'
V_global.netspeed_label = '网速:'
V_global.strategy_label = '策略:'
V_global.currenttime_label = '当前时间:'
V_global.lowestpricelabel = '最低成交价'

V_global.current_pricestatus_label = '等待第二次出价'
one_time1 = V_global.one_time1
one_diff = V_global.one_diff
current_pricestatus = '{0}秒加{1}'.format(one_time1, one_diff)
V_global.current_pricestatus = current_pricestatus

##状态框三行
V_global.status_time = (3,15)
V_global.lowestprice_text = (3,45)
V_global.pricelabeltext = (192,15)
V_global.pricetext = (345,15)
V_global.timestatustext = (192,45)
V_global.pricestatustext = (345,45)



##############################################
##服务器决定
#--------------------------------------------
##用于计算 最低成交价位置
V_global.px_relative = 1  ## 查找出来位置反算相对位置
V_global.py_relative = 10
V_global.px_timerelative = 22
V_global.py_timerelative = 5
## 相对于最低成交价位置
#   ## 0:加价  1：出价 2：提交  3：刷新按钮   4 ：确认   5：价格输入框    6:验证码输入框     7：取消
V_global.P_relative2 = [[647, 98], [650, 78], [440, 89], [196, 14], [575, 68], [51, 68], [385, 8], [186, 86]]
P_relative2 = V_global.P_relative2
V_global.Position_frame = [[0, 0] for i in range(len(P_relative2))]
## 限定截图位置
V_global.refresh_area_relative = [36 - 150, 11 - 100, 396 + 150, 11 + 100]
V_global.confirm_area_relative = [55 - 60, 668 - 40, 505 + 60, 61 + 40]
V_global.yan_confirm_area_relative = [205 - 60, 68 - 410, 405 + 60, 68 + 40]
V_global.Pos_controlframe_relative = [192 - 3474, 564 - 183]
V_global.Pos_yanzhengma_relative = [-21, -65, -97, +145]  ## 验证码所在位置
V_global.Pos_yanzhengmaframe_relative = [217, -483]  ## 验证码框放置位置

##计算当天的时间
V_global.timebase_str = ''  ##时间基数，避免重复计算
V_global.target_time = 11111111111111111  ##时间基数，避免重复计算  11:30:1 分的时间戳
V_global.start_time = 111111111111111  ## 11点之后的时间
V_global.final_time = 111111111111

V_global.final_stage = True  ##判断是不是处理最终状态

##一键登录
bidnumber = '12345678'
bidpassword = '12345678'
idcard = '1'

bidnumber_js = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
V_global.bidnumber_js = bidnumber_js
V_global.bidpassword_js = bidpassword_js
V_global.idcard_js = idcard_js

# def init_smart():
##智能出价服务
V_global.smart_ajust = False ## 智能调整出价，默认关闭

a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
b = a + ' ' + '11:29:50'
a_time = time.mktime(time.strptime(b, '%Y-%m-%d %H:%M:%S'))  # 转时间戳   补个平均时差
V_global.smart_ajust_time_guopai = a_time ## 智能调整触发时间
V_global.smart_ajust_time_moni = 50 ## 智能调整触发时间

## 完成智能出价
V_global.smart_autoprice = False ##智能补枪
V_global.smartprice_chujia = False ##智能出价 出价启动状态
V_global.smartprice_tijiao = False ##智能出价 提交启动状态

##------------------------------------------------------------------------------------------
### 窗口左上角位置计算对应位置
# def init_pos(Px, Py):
'''
PxPy     109  26
px, py   262  474
'''

Position_frame = V_global.Position_frame
# set_val('px_lowestprice', 153)
# set_val('py_lowestprice', 458)
'''
px_calculate_relative, py_calculate_relative  为找到的价格位置与窗口相对关系
'''
px_calculate_relative = V_global.px_calculate_relative
py_calculate_relative = V_global.py_calculate_relative
V_global.Px_lowestprice = px_calculate_relative+Px
V_global.Py_lowestprice = py_calculate_relative+Py
Px_lowestprice = V_global.Px_lowestprice
Py_lowestprice = V_global.Py_lowestprice
V_global.Px_currenttime = Px_lowestprice-27 ## 参考最低成交价位置
V_global.Py_currenttime = Py_lowestprice-14
P_relative2 = V_global.P_relative2

for i in range(len(Position_frame)):
    Position_frame[i][0] = Px_lowestprice + P_relative2[i][0]
    Position_frame[i][1] = Py_lowestprice + P_relative2[i][1]
V_global.Position_frame = Position_frame
##几个截图位置, 通过服务器传来的相对位置 进行计算
refresh_area_relative = V_global.refresh_area_relative
confirm_area_relative = V_global.confirm_area_relative
yan_confirm_area_relative = V_global.yan_confirm_area_relative
Pos_controlframe_relative = V_global.Pos_controlframe_relative
Pos_yanzhengma_relative = V_global.Pos_yanzhengma_relative ## 验证码所在位置
Pos_yanzhengmaframe_relative = V_global.Pos_yanzhengmaframe_relative ## 验证码框放置位置
V_global.refresh_area = (refresh_area_relative[0] + Px_lowestprice, refresh_area_relative[1] + Py_lowestprice,
                         refresh_area_relative[2] + Px_lowestprice, refresh_area_relative[3] + Py_lowestprice)

V_global.confirm_area = (confirm_area_relative[0]+Px_lowestprice,confirm_area_relative[1]+Py_lowestprice,
                         confirm_area_relative[2] + Px_lowestprice, confirm_area_relative[3] + Py_lowestprice)

V_global.yan_confirm_area = (yan_confirm_area_relative[0] + Px_lowestprice,
                             yan_confirm_area_relative[1] + Py_lowestprice,
                             yan_confirm_area_relative[2] + Px_lowestprice,
                             yan_confirm_area_relative[3] + Py_lowestprice)

V_global.Pos_controlframe = (Pos_controlframe_relative[0]+ Px_lowestprice,
                             Pos_controlframe_relative[1] + Py_lowestprice)

V_global.Pos_yanzhengma = (Position_frame[6][0]+Pos_yanzhengma_relative[0],
                           Position_frame[6][1] + Pos_yanzhengma_relative[1],
                           Position_frame[6][0] + Pos_yanzhengma_relative[2],
                           Position_frame[6][1] + Pos_yanzhengma_relative[3]) # 验证码所在位置

V_global.Pos_yanzhengmaframe = (Px_lowestprice + Pos_yanzhengmaframe_relative[0],
                                Py_lowestprice + Pos_yanzhengmaframe_relative[1])  # 验证码框放置位置

V_global.Pos_timeframe = (245-344+Px_lowestprice, 399-183+Py_lowestprice)

# set_val('Findpos_area', (Px + 100 , Py + 400, Px + 200, Py + 550))


lowestprice_sizex = V_global.lowestprice_sizex
lowestprice_sizey = V_global.lowestprice_sizey
currenttime_sizex = V_global.currenttime_sizex
currenttime_sizey = V_global.currenttime_sizey
V_global.findpos_on = False ## 无需定位
V_global.yanzhengma_move = True ## 需要定位
V_global.lowest = (Px_lowestprice,Py_lowestprice,lowestprice_sizex+Px_lowestprice,
                   lowestprice_sizey + Py_lowestprice)

Px_currenttime = V_global.Px_currenttime
Py_currenttime = V_global.Py_currenttime
V_global.currenttime = (Px_currenttime,Py_currenttime,Px_currenttime+currenttime_sizex,
                        Py_currenttime + currenttime_sizey)
dis_x = 50
dis_y = 100
x1 = Px_lowestprice - dis_x  # 截图起始点
y1 = Py_lowestprice - dis_y
lowest = V_global.lowest
refresh_area = V_global.refresh_area
confirm_area = V_global.confirm_area
Pos_yanzhengma = V_global.Pos_yanzhengma
yan_confirm_area = V_global.yan_confirm_area
currenttime = V_global.currenttime

cal_area = (lowest, refresh_area, confirm_area, Pos_yanzhengma, yan_confirm_area, currenttime)  ## 构建截图区域
use_area = []
V_global.sc_area = (Px_lowestprice-dis_x,Py_lowestprice-dis_y,Px_lowestprice+600,Py_lowestprice+120)
for i in range(len(cal_area)):
    temp = [cal_area[i][0] - x1, cal_area[i][1] - y1, cal_area[i][2] - x1, cal_area[i][3] - y1]
    use_area.append(temp)
V_global.use_area = use_area


##一键登录
bidnumber = '12345678'
bidpassword = '12345678'
idcard = '1'

bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
V_global.bidnumber_js = bidnumber_js
V_global.bidpassword_js = bidpassword_js
V_global.idcard_js = idcard_js

##初始化变量, 由服务器给定
def remote_variables(**kwargs):
    for key, value in kwargs.items():
        V_global.e = value



####
def remote_init():
    ##用于计算 最低成交价位置
    V_global.px_relative = 118 ## 查找出来位置反算相对位置
    V_global.py_relative = 1
    V_global.px_timerelative = 94
    V_global.py_timerelative = 3
    ## 相对于最低成交价位置
    #   ## 0:加价  1：出价 2：提交  3：刷新按钮   4 ：确认   5：价格输入框    6:验证码输入框     7：取消
    V_global.P_relative2 = [[647,-98],[650,8],[400,89],[396,14],[505,68],[562,8],[585,8],[586,86]]
    P_relative2 = V_global.P_relative2
    V_global.Position_frame = [[0,0] for i in range(len(P_relative2))]
    ## 限定截图位置
    V_global.refresh_area_relative = [396-150,11-100,396+150,11+100]
    V_global.confirm_area_relative = [505-60,68-40,505+60,68+40]
    V_global.yan_confirm_area_relative = [205-60,68-40,405+60,68+40]
    V_global.Pos_controlframe_relative = [192-344,514-183]
    V_global.Pos_yanzhengma_relative = [-277,-65,-97,+45] ## 验证码所在位置
    V_global.Pos_yanzhengmaframe_relative = [297,-283] ## 验证码框放置位置

    ##计算当天的时间
    V_global.timebase_str = '' ##时间基数，避免重复计算
    V_global.target_time = 11111111111111111 ##时间基数，避免重复计算  11:30:1 分的时间戳
    V_global.start_time = 111111111111111 ## 11点之后的时间
    V_global.final_time = 111111111111

    V_global.final_stage = True ##判断是不是处理最终状态

    ##一键登录
    bidnumber = '12345678'
    bidpassword = '12345678'
    idcard = '1'

    bidnumber_js  = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
    bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
    idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
    V_global.bidnumber_js = bidnumber_js
    V_global.bidpassword_js = bidpassword_js
    V_global.idcard_js = idcard_js

