# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 13:33
'''

# 变量初始化
host_ali = "http://hupai.pro"
debug = True
version = '1.0'
num = 0
avt = 90100
test = False

############全局变量参数表##96.22##-0[=#####
from component.variable import host_ali

# host_ali="127.0.0.1:5000"
# 网址
url1 = "http://moni.51hupai.org/"
# url1="http://hupai.pro/Moni"
# url1="http://127.0.0.1:5000/Moni"

url2 = "www.baidu.com"  # 电信
url3 = "www.baidu.com"  # 非电信
url4 = "http://127.0.0.1:5000/Moni"
# url4="http://121.196.220.94/Moni"

# icon路径
mainicon = 'ico.ico'

# global全局变量，操作控制
view = False  # 定位显示
do = False  # 开启辅助
ad_view = False  # 显示广告

price_view = False  # 显示价格,控制截图
yanzhengma_view = False  # 验证码放大,控制截图
yanzhengma_close = True  # 关闭验证码放大窗
yanzhengma_move = True  # 是否需要移动

yanzhengma_hash = 0  # 前一个验证码截图  如果变化就刷新 ，不变化就不动作

price_on = False  # 价格是否显示
price_count = 0  # 辅助计时，正确显示价格
yanzhengma_count = 0  # 辅助计时，正确显示价格
web_on = False  # 监测web是否开启
# 时间
view_time = False  # 时间框是否开启
operation_show = False  # 策略框是否开启
time_on = False  # 操作面板上是否开启时间

a_time = time.time()  # 国拍初始时间
b_time = 0  # 制作0.1秒

moni_minute = 29
moni_second = 0

chujia_time = 0  # 出价时间

Username = 0  # 用户名
Password = 0  # 密码

moni_on = False  # 判断开启的是哪个窗口 ，限制同时只能开启一个
guopai_on = False

strategy1 = 53  # 策略整数时间
strategy2 = 0.0  # 策略小数时间

# tijiao_delay=0         #策略提交延时
# final_tijiao=1000000000 #最终提交时间


strategy_on = True  # 策略是否开启
strategy_repeat = False  # 判断是否重复，避免重复进程
# guopai_tijiao=False #国拍提交次数

delay = False  # 是否延迟
delay_time = 0.5  # 延迟大小设置

login_result = False  # 登录成功与否

findpos_on = True  # 控制是否找位置

pricelist = [80000 + i * 100 for i in range(400)]  # 用于验证识别
IDnumber = 0  # 身份证号
account = 0  # 标书号
passwd = 0  # 密码

# 动态策略辅助
changetime = 0

######################################################

# 策略相关参数
one_time1 = 48  # 第一次出价加价
one_time2 = 55  # 第一次出价提交
one_real_time1 = 1000000000000  # 换算之后的出价时间
one_real_time2 = 1000000000000  # 换算之后的提交时间
one_diff = 700  # 第一次加价幅度
one_delay = 0.5  # 第一次延迟
one_advance = 100  # 第一次提交提前量

second_time1 = 48  # 第二次次出价加价
second_time2 = 55  # 第二次出价提交
second_real_time1 = 1000000000000  # 换算之后的出价时间
second_real_time2 = 1000000000000  # 换算之后的提交时间
second_diff = 600  # 第二次加价幅度
second_delay = 0.5  # 第二次出价延迟
second_advance = 100  # 第二次出价提交提前量

osl = [0] * 15  # 策略容器初始化   判定+10参数+确认选项

chujia_on = True  # 完成一次出价之后关闭，完成出价后关闭
tijiao_on = False  # 是否需要提交,完成提交后打开

lowest_price = 93400  # 最低成交价
own_price1 = 0  # 第一次出价
own_price2 = 0  # 第二次出价
own_price = 0  # 当前出价

tijiao_OK = False  # 表示输完验证码
e_on = True  # 表示s激活tijiao_OK
enter_on = False  # 表示回车激活tijiao_Ok

twice = False  # 开启两次出价
tijiao_num = 1  # 开启二次出价，设置为2，执行一次之后，减1
tijiao_one = False  # 第一次出价之后开闭
# ---------------------------------------------------------------
# 计算浏览器位置，左上角s
websize = [902, 700]  # 浏览器大小
Pxy = pg.size()  # 分辨率
Px1 = Pxy[0] / 2  # 屏幕中心位置
Py2 = Pxy[1] / 2
Px = (Pxy[0] - websize[0]) / 2 - 80
Py = (Pxy[1] - websize[1]) / 2
# 创建位置数据
# 0:加价  1：出价 2：提交  3：刷新   4 ：确认   5：验证码    6:验证码输入框     7：取消
P_relative = [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]]  # 各按钮相对于WEB位置
P_relative2 = [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]]
Position = [[0, 0] for i in range(len(P_relative))]
# for i in range(len(Position)):
#     Position[i][0] = Px1 + P_relative[i][0]
#     Position[i][1] = Py2 + P_relative[i][1]
# 转换为基于浏览器左上角坐标相对位置
# 按钮微调幅度--为国拍调整位置做准备
px_ajust, py_ajust = 0, 0
# for i in range(len(P_relative)):
#     P_relative[i][0] += websize[0] / 2 + px_ajust
#     P_relative[i][1] += websize[1] / 2 + py_ajust  # 微调
# price位置
px_price = 770 - 171
py_price = 260
# price框放置位置
px_priceframe = 220 - 191
py_priceframe = 480
# time放置位置
px_timeframe = 22
py_timeframe = 348
# 最低成交价框显示位置
px_lowestpriceframe = 245
py_lowestpriceframe = 290
lowestpriceframe_pos = [px_lowestpriceframe, py_lowestpriceframe]

# 验证码位置
px_yanzhengmaframe = 400 - 215
py_yanzhengmaframe = 460

# 出价截取大小
px_mini = 200
py_mini = 40
# 价格框大小
Pricesize = [400, 80]
# 验证码放大框大小
Yanzhengmasize = [400, 220]
# 时间框大小
Timesize = [200, 50]

# 刷新、确认所在区域  [396, 11], [505, 68]   价格387    440  325    412  375    431
lowestprice_area = [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py]
refresh_area = [396 - 150, 11 - 100, 396 + 150, 11 + 100]
confirm_area = [505 - 300, 68 - 150, 505 + 300, 68 + 150]
yan_confirm_area = [505 - 300, 68 - 150, 505 + 300, 68 + 150]

###幽灵键所在位置
ghostbutton_pos = [0, 0]
webview_pos = [-25, 0]  # WEB在 WEBVIEW里的相对位置
# -------------------------------------------------------------------


# 计算price位置
Px_price = Px + px_price
Py_price = Py + py_price
Pos_price = [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini]  # 所出价格截图位置BOX

Pos_yanzhengma = []  # 验证码所在位置

# 计算price框放置位置
Px_priceframe = Px + px_priceframe
Py_priceframe = Py + py_priceframe
Pos_priceframe = [Px_priceframe, Py_priceframe]

# 计算time放置位置
Px_timeframe = px_timeframe + Px
Py_timeframe = py_timeframe + Py
Pos_timeframe = [Px_timeframe, Py_timeframe]
# time放置位置
Pos_controlframe = [Px + 40, Py + 480]

# 计算验证码位置
Px_yanzhengmaframe = Px + px_yanzhengmaframe
Py_yanzhengmaframe = Py + py_yanzhengmaframe
Pos_yanzhengmaframe = [Px_yanzhengmaframe, Py_yanzhengmaframe]

###########################
# 提供所需截图位置
# 计算最低成交价位置
# 最低成交价位置，大小
# px_lowestprice=159    #206   209 208 #截图相对位置
# py_lowestprice=416   #412  416
px_lowestprice = 0  # 206   209 208 #截图相对位置
py_lowestprice = 0  # 412  416

########最低成交价
Px_lowestprice = Px + px_lowestprice
Py_lowestprice = Py + py_lowestprice
lowestprice_sizex = 82  # 截图范围 41
# lowestprice_sizex=41 #截图范围 41
lowestprice_sizey = 16
########当前时间位置

Px_currenttime = Px_lowestprice - 25  # 参考最低成交价位置
Py_currenttime = Py_lowestprice + 17
currenttime_sizex = 132
currenttime_sizey = 13

px_relative = 49  # 查找出来位置反算相对位置
py_relative = 0
# 计算确认键位置
px_confirm = 656
py_confirm = 475
Px_confirm = Px + px_confirm
Py_confirm = Py + py_confirm
confirm_sizex = 113
confirm_sizey = 28
confirm_on = False  # 是否需要确认
confirm_need = False  # 启动确认识别
confirm_one = False  # 限制只产生一次进程
# 计算刷新位置
px_refresh = 550
py_refresh = 413
Px_refresh = Px + px_refresh
Py_refresh = Py + py_refresh
refresh_sizex = 108
refresh_sizey = 21
refresh_on = False  # 是否需要刷新
refresh_need = False  # 启动刷新识别
refresh_one = False  # 限制只产生一次进程

chujia_interval = False  # 出价间隔
tijiao_interval = False  # 提交间隔
query_interval = False  # 间隔
query_on = False  # 是否处于查询状态

sc_area = [Px_lowestprice - 10, Py_lowestprice - 100, Px_lowestprice + 600, Py_lowestprice + 120]
use_area = []
nptemp = []
imgpos_lowestprice = np.array(nptemp)  # 最低成交价
imgpos_refresh = np.array(nptemp)  # 刷新按钮
imgpos_confirm = np.array(nptemp)  # 出价完后确认
impos_yanzhengma = np.array(nptemp)  # 验证码
imgpos_yanzhengmaconfirm = np.array(nptemp)  # 验证码确认键
imgpos_currenttime = np.array(nptemp)  # 当前时间
