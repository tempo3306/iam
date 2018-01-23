# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:34
'''
import wx
from PIL import Image,ImageGrab
import time
from .timframe import TimeFrame, MoniTimeFrame  # 时间窗口
from .YanzhengmaFrame import YanzhengmaFrame  # 验证码放大窗口
from .imgcut import cut_pic
import pickle, os ,imagehash
from .variable import set_val,get_val

##################
# 状态栏面板
class StatusPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        # 功能区
        self.control = wx.StaticBox(self, -1, "功能区域")
        self.controlbox = wx.StaticBoxSizer(self.control, wx.VERTICAL)
        self.controlgrid = wx.GridBagSizer(4, 4)  # 网格组件
        self.closeButton = wx.Button(self)  # 关闭WEB
        self.timeButton = wx.Button(self)  # 时间
        self.posajustButton = wx.Button(self)  # 位置调整
        self.timeajustButton = wx.Button(self)  # 时间同步
        self.controlgrid.Add(self.closeButton, pos=(0, 0))  # 布局
        self.controlgrid.Add(self.timeButton, pos=(0, 1))
        self.controlgrid.Add(self.posajustButton, pos=(1, 0))
        self.controlgrid.Add(self.timeajustButton, pos=(1, 1))
        self.controlbox.Add(self.controlgrid)  # 把网格组加到 功能框内
        # 状态区
        self.status = wx.StaticBox(self, -1, "状态显示")
        self.statusbox = wx.StaticBoxSizer(self.status, wx.VERTICAL)
        self.statusgrid = wx.GridBagSizer(6, 6)
        self.net_status = wx.StaticText(self, -1, label="当前网速")
        self.lowestprice_status = wx.StaticText(self, -1, label="当前最低成交价")
        self.userprice_status = wx.StaticText(self, -1, label="出价状态")
        self.time_status = wx.StaticText(self, -1, label="与出价时间相差")
        self.price_status = wx.StaticText(self, -1, label="价格相差")
        self.statusgrid.Add(self.net_status, pos=(0, 0))
        self.statusgrid.Add(self.lowestprice_status, pos=(1, 0))
        self.statusgrid.Add(self.userprice_status, pos=(2, 0))
        self.statusgrid.Add(self.time_status, pos=(3, 0))
        self.statusgrid.Add(self.price_status, pos=(4, 0))
        self.statusbox.Add(self.statusgrid)

        # 提示区域
        self.reminder = wx.StaticBox(self, -1, "提示")
        self.reminderbox = wx.StaticBoxSizer(self.reminder, wx.VERTICAL)
        self.remindervbox = wx.BoxSizer(wx.VERTICAL)
        self.hotkey_confirm = wx.StaticText(self, -1, label="回车 确认")
        self.hotkey_smartprice = wx.StaticText(self, -1, label="智能出价")
        self.remindervbox.Add(self.hotkey_confirm)
        self.remindervbox.Add(self.hotkey_smartprice)
        self.reminderbox.Add(self.remindervbox)
        # 组合
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.controlbox)
        self.vbox.Add(self.statusbox)
        self.vbox.Add(self.reminderbox)
        # 设置盒子
        self.SetSizer(self.vbox)


# 账号设置
class AccountPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        # colors = ["red", "blue", "gray", "yellow", "green"]
        # self.SetBackgroundColour(random.choice(colors))
        btn = wx.Button(self, label="3")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)


# 策略设置
class StrategyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        global one_time1, one_time2, second_time1 ,second_time2 ,Yanzhengmasize
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)
        # ----------------------------
        # timer 事件
        # 显示价格
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)  # 绑定一个定时器事件，主判断
        self.timer1.Start(10)  # 设定时间间隔
        # 设定间隔
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_count, self.timer2)  #
        self.timer2.Start(100)  # 设定时间间隔

        # 显示最低成交价
        # self.lowestframe = LowestpriceFrame()
        # self.lowestframe.Show(False)
        # ----------------------------
        # 功能区
        stractagy = wx.StaticBox(self, -1, u'选择策略:')
        self.stractagySizer = wx.StaticBoxSizer(stractagy, wx.VERTICAL)
        stractagy_label = wx.StaticText(self, label=u"设定拍牌策略", size=(100, 50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(stractagy_label)

        # 选择策略
        stractagy_choices = [u'单枪策略', u'双枪策略', u'手动操作（热键辅助）']
        self.select_stractagy = wx.Choice(self, -1, choices=stractagy_choices, size=(100, 50))
        hbox1.Add(self.select_stractagy)
        self.select_stractagy.SetSelection(0)
        # 时间显示
        self.timeview = wx.CheckBox(self, -1, label=u'显示时间')  # 开启时间显示
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.timeview)

        self.button1 = wx.Button(self, label='+1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_second, self.button1)
        self.button2 = wx.Button(self, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_second, self.button2)
        self.button3 = wx.Button(self, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(self, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)

        hbox2.Add(self.button1)
        hbox2.Add(self.button2)
        hbox2.Add(self.button3)
        hbox2.Add(self.button4)
        # 竖直SIZER
        vb1 = wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)
        vb1.Add(hbox2)

        # 设置确认方式
        confirm_choice = ["E键", "回车"]
        self.confirm_choice = wx.Choice(self, -1, choices=confirm_choice)
        self.confirm_choice.SetSelection(0)
        self.confirm_label = wx.StaticText(self, label=u"确认提交方式     ")
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.confirm_label, flag=wx.TOP, border=4)
        hbox3.Add(self.confirm_choice)
        vb1.Add(hbox3)

        # 策略保存与恢复
        self.strategy_save = wx.Button(self, label="保存策略", size=(60, 35))
        self.strategy_load = wx.Button(self, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(self, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.strategy_save)
        hbox4.Add(self.strategy_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)

        # 网格需放置于静态框中
        oneshot = wx.StaticBox(self, -1, u'单枪策略:')
        self.oneshotSizer = wx.StaticBoxSizer(oneshot, wx.VERTICAL)
        gridsizer1 = wx.GridBagSizer(4, 4)
        self.jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))  # ,style=wx.SP_WRAP最大值向上变最小值
        self.jiajia_time.SetRange(40, 55)
        self.jiajia_time.SetValue(48)
        self.jiajia_time.SetIncrement(0.1)

        gridsizer1.Add(self.jiajia_time, pos=(0, 0))
        miao_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(self, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))

        # 选择提交方式,第二排
        tijiao_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao = wx.Choice(self, -1, choices=tijiao_choices, size=(68, 25))
        self.select_tijiao.SetSelection(0)
        gridsizer1.Add(self.select_tijiao, pos=(1, 0))
        yanchi_label = wx.StaticText(self, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)

        # 选择提交方式,第三排
        tijiao_label = wx.StaticText(self, label=u"强制提交时间")
        gridsizer1.Add(tijiao_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.tijiao_time.SetRange(40.0, 57.0)
        self.tijiao_time.SetValue(55.0)
        self.tijiao_time.SetIncrement(0.1)
        gridsizer1.Add(self.tijiao_time, pos=(2, 1))
        miao3_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        # 网格需放置于静态框中
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)

        # 第二枪
        # 选择加价时间,第一排
        secondshot = wx.StaticBox(self, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajia_time2 = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.jiajia_time2.SetRange(40, 55)
        self.jiajia_time2.SetValue(48)
        self.jiajia_time2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajia_time2, pos=(0, 0))
        miao_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(self, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3))
        # 选择提交方式,第二排
        tijiao_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao2 = wx.Choice(self, -1, choices=tijiao_choices2, size=(68, 25))
        self.select_tijiao2.SetSelection(0)
        gridsizer2.Add(self.select_tijiao2, pos=(1, 0))
        yanchi_label2 = wx.StaticText(self, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)

        # 选择提交方式,第三排
        tijiao_label2 = wx.StaticText(self, label=u"强制提交时间")
        gridsizer2.Add(tijiao_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time2 = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.tijiao_time2.SetRange(53.0, 57.0)
        self.tijiao_time2.SetValue(55.0)
        self.tijiao_time2.SetIncrement(0.1)
        gridsizer2.Add(self.tijiao_time2, pos=(2, 1))
        miao3_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2), flag=wx.TOP, border=4)
        # 网格需放置于静态框中
        self.secondshotSizer.Add(gridsizer2, 0, flag=wx.ALL, border=5)
        self.stractagySizer.Add(vb1, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)

        # 加横线
        title = wx.StaticText(self, -1, label=u"拍牌功能设置")
        warning = wx.StaticText(self, -1, label=u"10点半需要进行第一次出价")
        warning.SetForegroundColour('red')
        line = wx.StaticLine(self, -1)
        self.vbox1.Add(title, 0, wx.ALL | wx.LEFT, 10)
        self.vbox1.Add(warning, 0, wx.LEFT, 10)
        self.vbox1.Add(line, flag=wx.EXPAND | wx.BOTTOM, border=10)
        self.vbox1.Add(self.stractagySizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.oneshotSizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1.Add(self.secondshotSizer, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(self.vbox1)

        # 显示参数设置
        self.secondsizer_Shown = False  # 二次出价默认关闭
        self.oneshotsizer_Shown = True  # 单次出价默认开启
        self.vbox1.Hide(self.secondshotSizer)  # 默认关闭二次出价

        # 状态区，显示当前策略，最低成交价，时间，出价状态

        # -------------待增加-------------------#

        # 绑定操作
        self.Bind(wx.EVT_CHECKBOX, self.Timeview, self.timeview)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice, self.confirm_choice)
        self.Bind(wx.EVT_BUTTON, self.Strategy_save, self.strategy_save)
        self.Bind(wx.EVT_BUTTON, self.Strategy_load, self.strategy_load)
        self.Bind(wx.EVT_BUTTON, self.Save_info, self.save_info)

        self.Bind(wx.EVT_CHOICE, self.Refresh_panel, self.select_stractagy)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE, self.Jiajia_time,self.jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time, self.jiajia_time)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Jiajia_price,self.jiajia_price)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price, self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao, self.select_tijiao)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Yanchi_time,self.yanchi_time)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time, self.yanchi_time)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Tijiao_time,self.tijiao_time)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time, self.tijiao_time)

        # self.Bind(wx.EVT_SPINCTRLDOUBLE, self.Jiajia_time2,self.jiajia_time2)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2, self.jiajia_time2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Jiajia_price2,self.jiajia_price2)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price2, self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao2, self.select_tijiao2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Yanchi_time2,self.yanchi_time2)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time2, self.yanchi_time2)
        # self.Bind(wx.EVT_SPINCTRLDOUBLE , self.Tijiao_time2,self.tijiao_time2)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time2, self.tijiao_time2)
        # 初始化国拍时间窗口
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        # 初始化模拟时间窗口
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)

        # 增加一个判定事件
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)

        self.yanzhengmaframe = YanzhengmaFrame(Yanzhengmasize)

    # 动态显示价格   验证码放大器
    def Price_view(self, event):
        global price_view, web_on, price_on, view_time, yanzhengma_view, Pricesize, Yanzhengmasize, yanzhengma_close
        global yanzhengma_count, price_count, yanzhengma_move ,Pos_price
        global imgpos_yanzhengma, yanzhengma_hash ,Pos_yanzhengmaframe

        if yanzhengma_move:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(Pos_yanzhengmaframe)  # 移动到新位置
                    yanzhengma_move = False  # 无需动作
                except:
                    pass
        if price_view and price_count >= 4:
            try:
                self.Price_close()
            except:
                pass
            self.Screen_shot(Pos_price, Pricesize, "userprice.png")
            image = "userprice.png"
            # self.priceframe = PriceFrame(image, Pricesize, Pos_priceframe)
            # self.priceframe.Show(True)
            price_view = False
            price_on = True
            # print("到这5")
        # 1秒之后查找是否有确定，找不到就关闭放大器
        if yanzhengma_count >= 5 and not yanzhengma_close:  # 0.5秒之后没有确认触发关闭验证码
            # yanzhengma_count = 0
            find_yan_confirm()
        if yanzhengma_close:
            try:
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        if yanzhengma_view:
            yanzhengma_close = False
            cut_pic(imgpos_yanzhengma, Yanzhengmasize, "yanzhengma.png")  # 直接调用得到 png
            # new_screenshot_getimg(Pos_yanzhengma,Yanzhengmasize,"yanzhengma.png")
            # self.Screen_shot_yanzhengma(Pos_yanzhengma,Yanzhengmasize,"yanzhengma.png")
            image = "yanzhengma.png"
            global yanzhengma_img
            yanzhengma_img = Image.open("yanzhengma.png")
            yan_hash = imagehash.dhash(yanzhengma_img)
            if not yanzhengma_hash:  # 第一次
                yanzhengma_hash = yan_hash
            elif yan_hash == yanzhengma_hash:  # 验证码没变化
                # print("没变化，不动作")
                pass
            else:
                yanzhengma_hash = yan_hash
                try:
                    yan = self.FindWindowById(18)
                    yan.ShowImage(image)
                    yan.Show()
                    # b = time.clock()
                    # print("显示总耗时",b - a)
                except:  # 找不到的情况下也要重新创建
                    pass
                finally:
                    pass

    def Yan_close(self, event):
        # print('fd')
        global yanzhengma_view, yanzhengma_close
        find_yan_confirm()

    def Price_count(self, event):
        # 设计手动显示价格的判定器，制作显示间隔
        global price_count, yanzhengma_count
        price_count += 1
        yanzhengma_count += 1
        file = 'sc_new.png'
        global web_on, strategy_on
        if web_on and strategy_on:
            self.lowestframe.Show(True)
        if not os.path.exists(file):
            try:
                self.Price_close()
            except:
                pass
        # 手动关闭最低价显示
        if not strategy_on or not web_on:
            self.lowestframe.Show(False)

    # 截图显示
    def Screen_shot(self, box, size, name):
        global Pricesize
        region = ImageGrab.grab(box)
        region.resize(size, Image.ANTIALIAS).save(name)

    def Screen_shot_yanzhengma(self, box, size, name):
        global Pricesize
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)
        # region.resize(size, Image.ANTIALIAS).save(name)

    # 删除此图
    @staticmethod
    def Del_shot():
        try:
            os.remove("sc_new.png")
        except:
            pass
            # 关闭显示

    def Price_close(self):
        try:
            self.priceframe.Destroy()
        except:
            pass

    ###还原触发出价
    def opt(self, event):
        global tijiao_num, tijiao_one, chujia_on ,moni_on, guopai_on
        global strategy_on ,moni_second, one_time1
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one  # 二次出价触发开关
        if moni_second < one_time1 and moni_on and not twice:  # 单次还原
            twice = False
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开
        elif moni_second < one_time1 and moni_on and twice:  # 二次还原
            twice = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开

    # 时间修改操作
    def Add_time(self, event):
        global a_time, moni_second, moni_on, guopai_on
        if moni_on:
            moni_second += 0.1
        else:
            a_time += 0.1

    def Minus_time(self, event):
        global a_time, moni_second, moni_on, guopai_on
        if moni_on:
            moni_second -= 0.1
        else:
            a_time -= 0.1

    def Add_second(self, event):
        global a_time, moni_second, moni_on, guopai_on
        if moni_on:
            moni_second += 1
            if moni_second >= 60:
                moni_second = 0
        else:
            a_time += 1

    def Minus_second(self, event):
        global a_time, moni_second, moni_on, guopai_on
        if moni_on:
            moni_second -= 1
            if moni_second <= 0:
                moni_second = 60
        else:
            a_time -= 1

    # 时间显示控制器
    def Timeview(self, event):
        timeSelected = event.GetEventObject()
        global view_time, time_on ,moni_on ,guopai_on
        if timeSelected.IsChecked():
            view_time = True
            time_on = True
            if guopai_on:
                self.timeframe1.Show(True)
            elif moni_on:
                self.timeframe2.Show(True)
        else:
            view_time = False
            time_on = False
            if guopai_on:
                self.timeframe1.Show(False)
            elif moni_on:
                self.timeframe2.Show(False)

    def Opentime(self):
        global moni_on,guopai_on
        if moni_on:
            try:
                self.timeframe2.Show(True)
            except:
                pass
        elif guopai_on:
            try:
                self.timeframe1.Show(True)
            except:
                pass

    def Closetime(self):
        try:
            self.timeframe1.Show(False)
        except:
            pass
        try:
            self.timeframe2.Show(False)
        except:
            pass

    def Confirmchoice(self, event):
        global e_on, enter_on
        con = self.confirm_choice.GetSelection()
        if con == 0:
            e_on = True
            enter_on = False
        elif con == 1:
            e_on = False
            enter_on = True

    def Jiajia_time(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2, one_real_time1, one_real_time2
        tem = self.jiajia_time.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            one_time1 = tem
            one_time1 = float(one_time1)
            one_real_time1 = self.gettime(one_time1)  # 计算得到的时间戳
        else:
            self.jiajia_time.SetValue(one_time1)

    def Jiajia_price(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            one_diff = int(tem)
        else:
            self.jiajia_price.SetValue(one_diff)

    #
    def Select_tijiao(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        select = self.select_tijiao.GetString(self.select_tijiao.GetSelection())
        if select == u"提前100":
            one_advance = 100
        elif select == u"提前200":
            one_advance = 200
        else:
            one_advance = 0

    def Yanchi_time(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            one_delay = float(tem)
        else:
            self.yanchi_time.SetValue(one_delay)

    def Tijiao_time(self, event):
        global one_advance, one_delay, one_diff, one_time1, one_time2, one_real_time2
        tem = self.tijiao_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            one_time2 = float(tem)
            one_real_time2 = self.gettime(one_time2)  # 计算得到的时间戳
        else:
            self.tijiao_time.SetValue(one_time2)

    # 双枪操作
    def Jiajia_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2, second_real_time1
        tem = self.jiajia_time2.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            second_time1 = float(tem)
            second_real_time1 = self.gettime(second_time1)  # 计算得到的时间戳
        else:
            self.jiajia_time2.SetValue(second_time1)

    def Jiajia_price2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        global one_advance, one_delay, one_diff, one_time1, one_time2
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            second_diff = int(tem)
        else:
            self.jiajia_price2.SetValue(second_diff)

    def Select_tijiao2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        select = self.select_tijiao2.GetString(self.select_tijiao2.GetSelection())
        if select == u"提前100":
            second_advance = 100
        elif select == u"提前200":
            second_advance = 200
        else:
            second_advance = 0

    def Yanchi_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            second_delay = float(tem)
        else:
            self.yanchi_time2.SetValue(second_delay)

    def Tijiao_time2(self, event):
        global second_advance, second_delay, second_diff, second_time1, second_time2, second_real_time2
        tem = self.tijiao_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            second_time2 = float(tem)
            second_real_time2 = self.gettime(second_time2)  # 计算得到的时间戳
        else:
            self.tijiao_time2.SetValue(second_time2)

    ##################
    # 重新绘制,面板刷新
    def Refresh_panel(self, event):
        # GetSelection 返回index
        global strategy_on  # 策略开启
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one  # 二次出价触发开关
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            twice = False
            strategy_on = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开

        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            strategy_on = True
            twice = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开
        else:
            self.none_show()
            strategy_on = False
            twice = False

    def ss_Shown(self):  # 双枪
        if not self.secondsizer_Shown:  # 如果当前控件已隐藏
            self.vbox1.Show(self.secondshotSizer)  # 打开双枪面板
            self.secondsizer_Shown = True  # 服务器设置部分当前已隐藏
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)  # 显示第一枪面板
            self.oneshotsizer_Shown = True
        self.secondsizer_Shown = True
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 575))  # 更新面板尺寸
        self.Secondshot_reset()
        self.Layout()

    def ss_Hide(self):  # 单枪
        if self.secondsizer_Shown:  # 如果当前控件已显示
            self.vbox1.Hide(self.secondshotSizer)  # 如果当前控件已隐藏
            # self.setserverBtn.SetLabel(u'服务器设置↑')    #更新按钮标签
            # 服务器设置部分当前已显示
        if not self.oneshotsizer_Shown:
            self.vbox1.Show(self.oneshotSizer)
        self.secondsizer_Shown = False
        self.oneshotSizer_Shown = True
        self.SetClientSize((280, 375))  # 更新面板尺寸
        self.Oneshot_reset()
        self.Layout()

    def none_show(self):
        if self.oneshotsizer_Shown:
            self.vbox1.Hide(self.secondshotSizer)
        if self.secondsizer_Shown:
            self.vbox1.Hide(self.oneshotSizer)

        self.oneshotsizer_Shown = False
        self.secondsizer_Shown = False
        self.SetClientSize((280, 255))
        self.Layout()

    def Oneshot_reset(self):
        global one_time1, one_time2, one_diff, one_delay, one_advance
        self.jiajia_time.SetValue(48.0)
        self.tijiao_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_tijiao.SetSelection(0)
        self.yanchi_time.SetValue(0.5)

        one_time1 = 48  # 第一次出价加价
        one_time2 = 55  # 第一次出价提交
        one_diff = 700  # 第一次加价幅度
        one_delay = 0.5  # 第一次延迟
        one_advance = 100  # 第一次提交提前量
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)

    def Secondshot_reset(self):
        global one_time1, one_time2, one_diff, one_delay, one_advance
        global second_time1, second_time2, second_diff, second_delay, second_advance
        self.jiajia_time.SetValue(40.0)
        self.tijiao_time.SetValue(48.0)
        self.jiajia_price.SetValue(500)
        self.select_tijiao.SetSelection(2)
        self.yanchi_time.SetValue(0.0)

        self.jiajia_time2.SetValue(50.0)
        self.tijiao_time2.SetValue(55.5)
        self.jiajia_price2.SetValue(700)
        self.select_tijiao2.SetSelection(0)
        self.yanchi_time2.SetValue(0.5)

        one_time1 = 40  # 第一次出价加价
        one_time2 = 48  # 第一次出价提交
        one_diff = 500  # 第一次加价幅度
        one_delay = 0.5  # 第一次延迟
        one_advance = 0  # 第一次提交提前量

        second_time1 = 50  # 第二次次出价加价
        second_time2 = 55.5  # 第二次出价提交
        second_diff = 700  # 第二次加价幅度
        second_delay = 0.5  # 第二次出价延迟
        second_advance = 100  # 第二次出价提交提前量
        # 初始化real_time
        global one_real_time1, second_real_time1, one_real_time2, second_real_time2
        one_real_time1 = self.gettime(one_time1)
        one_real_time2 = self.gettime(one_time2)
        second_real_time1 = self.gettime(second_time1)
        second_real_time2 = self.gettime(second_time2)

    # 定义策略保存
    def Strategy_save(self, event):
        dlg = wx.TextEntryDialog(None, '设定你的策略名称:', "策略保存", "策略1",
                                 style=wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            name = dlg.GetValue()
            if name:
                dlg_tip = wx.MessageBox('保存成功', '策略保存', wx.OK | wx.ICON_INFORMATION)
                if dlg_tip == wx.ID_OK:
                    dlg_tip.Destroy()
                    dlg.Destroy()
                self.save(name)
            else:
                dlg_tip = wx.MessageBox('名称不能为空', '策略保存', wx.OK | wx.ICON_ERROR)
                if dlg_tip == wx.ID_OK:
                    dlg_tip.Destroy()
                    dlg.Destroy()

    def save(self, name):
        global one_time1, one_time2, one_diff, one_delay, one_advance
        global second_time1, second_time2, second_diff, second_delay, second_advance
        global osl, e_on, enter_on  # 策略存储容器

        if self.select_stractagy.GetSelection() == 2:
            dlg_tip = wx.MessageBox('请先制定一个策略', '策略保存', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()
        elif self.select_stractagy.GetSelection() == 0:
            osl[0] = 0
            osl[1] = one_time1
            osl[2] = one_time2
            osl[3] = one_diff
            osl[4] = one_delay
            osl[5] = one_advance
            osl[6] = second_time1
            osl[7] = second_time2
            osl[8] = second_diff
            osl[9] = second_delay
            osl[10] = second_advance
            osl[11] = e_on
            osl[12] = enter_on
        elif self.select_stractagy.GetSelection() == 1:
            osl[0] = 1
            osl[0] = 1
            osl[1] = one_time1
            osl[2] = one_time2
            osl[3] = one_diff
            osl[4] = one_delay
            osl[5] = one_advance
            osl[6] = second_time1
            osl[7] = second_time2
            osl[8] = second_diff
            osl[9] = second_delay
            osl[10] = second_advance
            osl[11] = e_on
            osl[12] = enter_on
        with open('%s.strategy' % name, 'wb') as spk:
            pickle.dump(osl, spk)

    # 输入框
    # def GetName(self):
    #     dlg = wx.TextEntryDialog(self.panel, '设定你的策略名称:', "策略保存", "策略1",
    #                              style=wx.OK)
    #     dlg.ShowModal()
    #     self.stractagyname.SetValue(dlg.GetValue())
    #     if dlg.ShowModal() == wx.ID_OK:
    #         response = dlg.GetValue()
    #         dlg.Destroy()

    # 定义策略恢复

    def Strategy_load(self, event):
        import os
        path = os.getcwd()
        choice = self.findfiles(path)
        if choice:
            dlg = wx.SingleChoiceDialog(None, u"请选择策略:", u"策略载入",
                                        choices=choice)
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetStringSelection()  # 获取选择的内容
                dlg_tip = wx.MessageDialog(None, "载入成功", u"载入策略", wx.OK | wx.ICON_INFORMATION)
                if dlg_tip.ShowModal() == wx.ID_OK:
                    dlg_tip.Destroy()
                self.load(path)
            # print("载入")
            dlg.Destroy()
        else:
            dlg_tip = wx.MessageBox('找不到任何保存的策略', '策略载入', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()

    def load(self, path):
        global osl, e_on, enter_on
        global one_time1, one_time2, one_diff, one_delay, one_advance
        global second_time1, second_time2, second_diff, second_delay, second_advance

        global strategy_on  # 策略开启
        global twice, tijiao_num, chujia_on, tijiao_on, tijiao_OK, tijiao_one  # 二次出价触发开关
        global one_real_time1, one_real_time2, second_real_time1, second_real_time2
        try:
            with open(path, 'rb') as loadstr:
                osl = pickle.load(loadstr)
        except:
            pass
        if osl[0] == 0:  # 单次
            self.ss_Hide()

            twice = False
            strategy_on = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开

            self.select_stractagy.SetSelection(0)
            self.jiajia_time.SetValue(osl[1])
            self.tijiao_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_tijiao.SetSelection(0)
            elif osl[5] == 200:
                self.select_tijiao.SetSelection(1)
            else:
                self.select_tijiao.SetSelection(2)

            one_time1 = osl[1]  # 第一次出价加价
            one_time2 = osl[2]  # 第一次出价提交
            one_diff = osl[3]  # 第一次加价幅度
            one_delay = osl[4]  # 第一次延迟
            one_advance = osl[5]  # 第一次提交提前量
            # 确认操作
            e_on = osl[11]
            enter_on = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_real_time1 = self.gettime(one_time1)
            one_real_time2 = self.gettime(one_time2)
            second_real_time1 = self.gettime(second_time1)
            second_real_time2 = self.gettime(second_time2)

        elif osl[0] == 1:  # 双枪
            strategy_on = True
            twice = True
            chujia_on = True
            tijiao_on = False
            tijiao_num = 1  # 初始化
            tijiao_OK = False
            tijiao_one = False  # 单枪未开
            self.ss_Shown()
            self.select_stractagy.SetSelection(1)
            self.jiajia_time.SetValue(osl[1])
            self.tijiao_time.SetValue(osl[2])
            self.jiajia_price.SetValue(osl[3])
            self.yanchi_time.SetValue(osl[4])
            if osl[5] == 100:
                self.select_tijiao.SetSelection(0)
            elif osl[5] == 200:
                self.select_tijiao.SetSelection(1)
            else:
                self.select_tijiao.SetSelection(2)
            self.jiajia_time2.SetValue(osl[6])
            self.tijiao_time2.SetValue(osl[7])
            self.jiajia_price2.SetValue(osl[8])
            self.yanchi_time2.SetValue(osl[9])
            if osl[10] == 100:
                self.select_tijiao2.SetSelection(0)
            elif osl[10] == 200:
                self.select_tijiao2.SetSelection(1)
            else:
                self.select_tijiao2.SetSelection(2)

            one_time1 = osl[1]  # 第一次出价加价
            one_time2 = osl[2]  # 第一次出价提交
            one_diff = osl[3]  # 第一次加价幅度
            one_delay = osl[4]  # 第一次延迟
            one_advance = osl[5]  # 第一次提交提前量

            second_time1 = osl[6]  # 第二次次出价加价
            second_time2 = osl[7]  # 第二次出价提交
            second_diff = osl[8]  # 第二次加价幅度
            second_delay = osl[9]  # 第二次出价延迟
            second_advance = osl[10]  # 第二次出价提交提前量
            # 确认操作
            e_on = osl[11]
            enter_on = osl[12]
            if e_on:
                self.confirm_choice.SetSelection(0)
            elif enter_on:
                self.confirm_choice.SetSelection(1)

            one_real_time1 = self.gettime(one_time1)
            one_real_time2 = self.gettime(one_time2)
            second_real_time1 = self.gettime(second_time1)
            second_real_time2 = self.gettime(second_time2)

    def findfiles(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.strategy':
                    L.append(os.path.join(root, file))
        return L

    def Save_info(self, event):
        pass

    #############时间换算###############
    # 转时间戳
    def changetime(self, a):  # 换算成时间戳
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time  # 以时间戳输出

    # 转字符串
    def get_nowtime(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a  # 输出时间格式字符串
        # 转为最终时间戳，调用这个时间

    def gettime(self, choice):  # choice1:55,choice2:0.5
        tem = self.get_nowtime()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.changetime(b) + float(choice) - int(choice)
        return c  # 得到用户所确定的最终时间戳


# 功能窗口#
class OperationFrame(wx.Frame):
    def __init__(self, Px, Py, mainicon):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 2, title="沪牌一号", pos=(Px + 902, Py), size=(300, 625), \
                          style=wx.FRAME_NO_TASKBAR | wx.CAPTION | wx.CLOSE_BOX)  # wx.FRAME_TOOL_WINDOW|   |wx.STAY_ON_TOP

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # 设置图标
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        #############################
        ####标签切换
        panel = wx.Panel(self)

        self.notebook = wx.Notebook(panel)
        self.status_tab = StatusPanel(self.notebook)  # notebook作为父类
        self.notebook.AddPage(self.status_tab, "常规功能")

        self.strategy_tab = StrategyPanel(self.notebook)
        self.notebook.AddPage(self.strategy_tab, "策略设置")

        self.account_tab = AccountPanel(self.notebook)
        self.notebook.AddPage(self.account_tab, "账号设置")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()
        self.Show(False)  # 初始隐藏

    def OnClose(self, event):
        self.Show(False)
