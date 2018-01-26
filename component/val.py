set_val('host_ali', "http://hupai.pro")
host_ali = get_val('host_ali')
set_val('debug', True)
debug = get_val('debug')
set_val('version', '1.0')
version = get_val('version')
set_val('num', 0)
num = get_val('num')
set_val('avt', 90100)
avt = get_val('avt')
set_val('test', False)
test = get_val('test')
set_val('url1', "http://moni.51hupai.org/")
url1 = get_val('url1')
set_val('url2', "www.baidu.com")  #电信
url2 = get_val('url2')
set_val('url3', "www.baidu.com")  #非电信
url3 = get_val('url3')
set_val('url4', "http://127.0.0.1:5000/Moni")
url4 = get_val('url4')
set_val('mainicon', 'ico.ico')
mainicon = get_val('mainicon')
set_val('view', False)  #定位显示
view = get_val('view')
set_val('do', False)  #开启辅助
do = get_val('do')
set_val('ad_view', False)  #显示广告
ad_view = get_val('ad_view')
set_val('price_view', False)  #显示价格,控制截图
price_view = get_val('price_view')
set_val('yanzhengma_view', False)  #验证码放大,控制截图
yanzhengma_view = get_val('yanzhengma_view')
set_val('yanzhengma_close', True)  #关闭验证码放大窗
yanzhengma_close = get_val('yanzhengma_close')
set_val('yanzhengma_move', True)  #是否需要移动
yanzhengma_move = get_val('yanzhengma_move')
set_val('yanzhengma_hash', 0)  #前一个验证码截图  如果变化就刷新 ，不变化就不动作
yanzhengma_hash = get_val('yanzhengma_hash')
set_val('price_on', False)  #价格是否显示
price_on = get_val('price_on')
set_val('price_count', 0)  #辅助计时，正确显示价格
price_count = get_val('price_count')
set_val('yanzhengma_count', 0)  #辅助计时，正确显示价格
yanzhengma_count = get_val('yanzhengma_count')
set_val('web_on', False)  #监测web是否开启
web_on = get_val('web_on')
set_val('view_time', False)  #时间框是否开启
view_time = get_val('view_time')
set_val('operation_show', False)  #策略框是否开启
operation_show = get_val('operation_show')
set_val('time_on', False)  #操作面板上是否开启时间
time_on = get_val('time_on')
set_val('a_time', time.time())  #国拍初始时间
a_time = get_val('a_time')
set_val('b_time', 0)  #制作0.1秒
b_time = get_val('b_time')
set_val('moni_minute', 29)
moni_minute = get_val('moni_minute')
set_val('moni_second', 0)
moni_second = get_val('moni_second')
set_val('chujia_time', 0)  #出价时间
chujia_time = get_val('chujia_time')
set_val('Username', 0)  #用户名
Username = get_val('Username')
set_val('Password', 0)  #密码
Password = get_val('Password')
set_val('moni_on', False)  #判断开启的是哪个窗口 ，限制同时只能开启一个
moni_on = get_val('moni_on')
set_val('guopai_on', False)
guopai_on = get_val('guopai_on')
set_val('strategy1', 53)  #策略整数时间
strategy1 = get_val('strategy1')
set_val('strategy2', 0.0)  #策略小数时间
strategy2 = get_val('strategy2')
set_val('strategy_on', True)  #策略是否开启
strategy_on = get_val('strategy_on')
set_val('strategy_repeat', False)  #判断是否重复，避免重复进程
strategy_repeat = get_val('strategy_repeat')
set_val('delay', False)  #是否延迟
delay = get_val('delay')
set_val('delay_time', 0.5)  #延迟大小设置
delay_time = get_val('delay_time')
set_val('login_result', False)  #登录成功与否
login_result = get_val('login_result')
set_val('findpos_on', True)  #控制是否找位置
findpos_on = get_val('findpos_on')
set_val('pricelist', [80000 + i * 100 for i in range(400)])  #用于验证识别
pricelist = get_val('pricelist')
set_val('IDnumber', 0)  #身份证号
IDnumber = get_val('IDnumber')
set_val('account', 0)  #标书号
account = get_val('account')
set_val('passwd', 0)  #密码
passwd = get_val('passwd')
set_val('changetime', 0)
changetime = get_val('changetime')
set_val('one_time1', 48)  #第一次出价加价
one_time1 = get_val('one_time1')
set_val('one_time2', 55)  #第一次出价提交
one_time2 = get_val('one_time2')
set_val('one_real_time1', 1000000000000)  #换算之后的出价时间
one_real_time1 = get_val('one_real_time1')
set_val('one_real_time2', 1000000000000)  #换算之后的提交时间
one_real_time2 = get_val('one_real_time2')
set_val('one_diff', 700)  #第一次加价幅度
one_diff = get_val('one_diff')
set_val('one_delay', 0.5)  #第一次延迟
one_delay = get_val('one_delay')
set_val('one_advance', 100)  #第一次提交提前量
one_advance = get_val('one_advance')
set_val('second_time1', 48)  #第二次次出价加价
second_time1 = get_val('second_time1')
set_val('second_time2', 55)  #第二次出价提交
second_time2 = get_val('second_time2')
set_val('second_real_time1', 1000000000000)  #换算之后的出价时间
second_real_time1 = get_val('second_real_time1')
set_val('second_real_time2', 1000000000000)  #换算之后的提交时间
second_real_time2 = get_val('second_real_time2')
set_val('second_diff', 600)  #第二次加价幅度
second_diff = get_val('second_diff')
set_val('second_delay', 0.5)  #第二次出价延迟
second_delay = get_val('second_delay')
set_val('second_advance', 100)  #第二次出价提交提前量
second_advance = get_val('second_advance')
set_val('osl', [0] * 15)  #策略容器初始化   判定+10参数+确认选项
osl = get_val('osl')
set_val('chujia_on', True)  #完成一次出价之后关闭，完成出价后关闭
chujia_on = get_val('chujia_on')
set_val('tijiao_on', False)  #是否需要提交,完成提交后打开
tijiao_on = get_val('tijiao_on')
set_val('lowest_price', 93400)  #最低成交价
lowest_price = get_val('lowest_price')
set_val('own_price1', 0)  #第一次出价
own_price1 = get_val('own_price1')
set_val('own_price2', 0)  #第二次出价
own_price2 = get_val('own_price2')
set_val('own_price', 0)  #当前出价
own_price = get_val('own_price')
set_val('tijiao_OK', False)  #表示输完验证码
tijiao_OK = get_val('tijiao_OK')
set_val('e_on', True)  #表示s激活tijiao_OK
e_on = get_val('e_on')
set_val('enter_on', False)  #表示回车激活tijiao_Ok
enter_on = get_val('enter_on')
set_val('twice', False)  #开启两次出价
twice = get_val('twice')
set_val('tijiao_num', 1)  #开启二次出价，设置为2，执行一次之后，减1
tijiao_num = get_val('tijiao_num')
set_val('tijiao_one', False)  #第一次出价之后开闭
tijiao_one = get_val('tijiao_one')
set_val('websize', [902, 700])  #浏览器大小
websize = get_val('websize')
set_val('Pxy', pg.size())  #分辨率
Pxy = get_val('Pxy')
set_val('Px1', Pxy[0] / 2)  #屏幕中心位置
Px1 = get_val('Px1')
set_val('Py2', Pxy[1] / 2)
Py2 = get_val('Py2')
set_val('Px', (Pxy[0] - websize[0]) / 2 - 80)
Px = get_val('Px')
set_val('Py', (Pxy[1] - websize[1]) / 2)
Py = get_val('Py')
set_val('P_relative', [[343, -66], [346, 40], [96, 121], [92, 43], [201, 100], [281, 40], [261, 37], [282, 118]])  #各按钮相对于WEB位置
P_relative = get_val('P_relative')
set_val('P_relative2', [[647, -98], [650, 8], [400, 89], [396, 11], [505, 68], [585, 8], [565, 5], [586, 86]])
P_relative2 = get_val('P_relative2')
set_val('Position', [[0, 0] for i in range(len(P_relative))])
Position = get_val('Position')
set_val('px_ajust, py_ajust', 0, 0)
px_ajust, py_ajust = get_val('px_ajust, py_ajust')
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
lowestpriceframe_pos = get_val('lowestpriceframe_pos')
set_val('px_yanzhengmaframe', 400 - 215)
px_yanzhengmaframe = get_val('px_yanzhengmaframe')
set_val('py_yanzhengmaframe', 460)
py_yanzhengmaframe = get_val('py_yanzhengmaframe')
set_val('px_mini', 200)
px_mini = get_val('px_mini')
set_val('py_mini', 40)
py_mini = get_val('py_mini')
set_val('Pricesize', [400, 80])
Pricesize = get_val('Pricesize')
set_val('Yanzhengmasize', [400, 220])
Yanzhengmasize = get_val('Yanzhengmasize')
set_val('Timesize', [200, 50])
Timesize = get_val('Timesize')
set_val('lowestprice_area', [179 - 80 + Px, 424 - 50 + Py, 179 + 80 + Px, 424 + 50 + Py])
lowestprice_area = get_val('lowestprice_area')
set_val('refresh_area', [396 - 150, 11 - 100, 396 + 150, 11 + 100])
refresh_area = get_val('refresh_area')
set_val('confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
confirm_area = get_val('confirm_area')
set_val('yan_confirm_area', [505 - 300, 68 - 150, 505 + 300, 68 + 150])
yan_confirm_area = get_val('yan_confirm_area')
set_val('ghostbutton_pos', [0, 0])
ghostbutton_pos = get_val('ghostbutton_pos')
set_val('webview_pos', [-25, 0])  #WEB在 WEBVIEW里的相对位置
webview_pos = get_val('webview_pos')
set_val('Px_price', Px + px_price)
Px_price = get_val('Px_price')
set_val('Py_price', Py + py_price)
Py_price = get_val('Py_price')
set_val('Pos_price', [Px_price, Py_price, Px_price + px_mini, Py_price + py_mini])  #所出价格截图位置BOX
Pos_price = get_val('Pos_price')
set_val('Pos_yanzhengma', [])  #验证码所在位置
Pos_yanzhengma = get_val('Pos_yanzhengma')
set_val('Px_priceframe', Px + px_priceframe)
Px_priceframe = get_val('Px_priceframe')
set_val('Py_priceframe', Py + py_priceframe)
Py_priceframe = get_val('Py_priceframe')
set_val('Pos_priceframe', [Px_priceframe, Py_priceframe])
Pos_priceframe = get_val('Pos_priceframe')
set_val('Px_timeframe', px_timeframe + Px)
Px_timeframe = get_val('Px_timeframe')
set_val('Py_timeframe', py_timeframe + Py)
Py_timeframe = get_val('Py_timeframe')
set_val('Pos_timeframe', [Px_timeframe, Py_timeframe])
Pos_timeframe = get_val('Pos_timeframe')
set_val('Pos_controlframe', [Px + 40, Py + 480])
Pos_controlframe = get_val('Pos_controlframe')
set_val('Px_yanzhengmaframe', Px + px_yanzhengmaframe)
Px_yanzhengmaframe = get_val('Px_yanzhengmaframe')
set_val('Py_yanzhengmaframe', Py + py_yanzhengmaframe)
Py_yanzhengmaframe = get_val('Py_yanzhengmaframe')
set_val('Pos_yanzhengmaframe', [Px_yanzhengmaframe, Py_yanzhengmaframe])
Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
set_val('px_lowestprice', 0)  #206   209 208 截图相对位置
px_lowestprice = get_val('px_lowestprice')
set_val('py_lowestprice', 0)  #412  416
py_lowestprice = get_val('py_lowestprice')
set_val('Px_lowestprice', Px + px_lowestprice)
Px_lowestprice = get_val('Px_lowestprice')
set_val('Py_lowestprice', Py + py_lowestprice)
Py_lowestprice = get_val('Py_lowestprice')
set_val('lowestprice_sizex', 82)  #截图范围 41
lowestprice_sizex = get_val('lowestprice_sizex')
set_val('lowestprice_sizey', 16)
lowestprice_sizey = get_val('lowestprice_sizey')
set_val('Px_currenttime', Px_lowestprice - 25)  #参考最低成交价位置
Px_currenttime = get_val('Px_currenttime')
set_val('Py_currenttime', Py_lowestprice + 17)
Py_currenttime = get_val('Py_currenttime')
set_val('currenttime_sizex', 132)
currenttime_sizex = get_val('currenttime_sizex')
set_val('currenttime_sizey', 13)
currenttime_sizey = get_val('currenttime_sizey')
set_val('px_relative', 49)  #查找出来位置反算相对位置
px_relative = get_val('px_relative')
set_val('py_relative', 0)
py_relative = get_val('py_relative')
set_val('px_confirm', 656)
px_confirm = get_val('px_confirm')
set_val('py_confirm', 475)
py_confirm = get_val('py_confirm')
set_val('Px_confirm', Px + px_confirm)
Px_confirm = get_val('Px_confirm')
set_val('Py_confirm', Py + py_confirm)
Py_confirm = get_val('Py_confirm')
set_val('confirm_sizex', 113)
confirm_sizex = get_val('confirm_sizex')
set_val('confirm_sizey', 28)
confirm_sizey = get_val('confirm_sizey')
set_val('confirm_on', False)  #是否需要确认
confirm_on = get_val('confirm_on')
set_val('confirm_need', False)  #启动确认识别
confirm_need = get_val('confirm_need')
set_val('confirm_one', False)  #限制只产生一次进程
confirm_one = get_val('confirm_one')
set_val('px_refresh', 550)
px_refresh = get_val('px_refresh')
set_val('py_refresh', 413)
py_refresh = get_val('py_refresh')
set_val('Px_refresh', Px + px_refresh)
Px_refresh = get_val('Px_refresh')
set_val('Py_refresh', Py + py_refresh)
Py_refresh = get_val('Py_refresh')
set_val('refresh_sizex', 108)
refresh_sizex = get_val('refresh_sizex')
set_val('refresh_sizey', 21)
refresh_sizey = get_val('refresh_sizey')
set_val('refresh_on', False)  #是否需要刷新
refresh_on = get_val('refresh_on')
set_val('refresh_need', False)  #启动刷新识别
refresh_need = get_val('refresh_need')
set_val('refresh_one', False)  #限制只产生一次进程
refresh_one = get_val('refresh_one')
set_val('chujia_interval', False)  #出价间隔
chujia_interval = get_val('chujia_interval')
set_val('tijiao_interval', False)  #提交间隔
tijiao_interval = get_val('tijiao_interval')
set_val('query_interval', False)  #间隔
query_interval = get_val('query_interval')
set_val('query_on', False)  #是否处于查询状态
query_on = get_val('query_on')
set_val('sc_area', [Px_lowestprice - 10, Py_lowestprice - 100, Px_lowestprice + 600, Py_lowestprice + 120])
sc_area = get_val('sc_area')
set_val('use_area', [])
use_area = get_val('use_area')
set_val('nptemp', [])
nptemp = get_val('nptemp')
set_val('imgpos_lowestprice', np.array(nptemp))  #最低成交价
imgpos_lowestprice = get_val('imgpos_lowestprice')
set_val('imgpos_refresh', np.array(nptemp))  #刷新按钮
imgpos_refresh = get_val('imgpos_refresh')
set_val('imgpos_confirm', np.array(nptemp))  #出价完后确认
imgpos_confirm = get_val('imgpos_confirm')
set_val('impos_yanzhengma', np.array(nptemp))  #验证码
impos_yanzhengma = get_val('impos_yanzhengma')
set_val('imgpos_yanzhengmaconfirm', np.array(nptemp))  #验证码确认键
imgpos_yanzhengmaconfirm = get_val('imgpos_yanzhengmaconfirm')
set_val('imgpos_currenttime', np.array(nptemp))  #当前时间
imgpos_currenttime = get_val('imgpos_currenttime')
