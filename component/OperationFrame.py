'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:34
'''
import wx
from PIL import Image, ImageGrab
import time
from component.timeFrame import TimeFrame, MoniTimeFrame  # 时间窗口
from component.YanzhengmaFrame import YanzhengmaFrame  # 验证码放大窗口
from component.imgcut import cut_pic, find_yan_confirm
import pickle, os, imagehash
from component.variable import set_val, get_val
from component.imgcut import findpos, timeset
from wx.lib.pubsub import pub
from component.variable import set_val, get_val

#-----------------------------------------------------------
class StatusPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=20)
        self.control = wx.StaticBox(self, -1, "功能区域")
        self.controlbox = wx.StaticBoxSizer(self.control, wx.VERTICAL)
        self.controlgrid = wx.GridBagSizer(4, 2)  # 网格组件

        ##功能区
        self.timeviewButton = wx.Button(self, label='显示时间', size=(105,30))  # 未来扩展
        self.remotetimeButton = wx.Button(self, label='同步服务器时间', size=(105,30))  # 时间
        self.posajustButton = wx.Button(self, label='刷新定位', size=(105,30))  # 位置调整
        self.localtimeButton = wx.Button(self, label='同步本地时间', size=(105,30))  # 时间同步

        ##绑定
        self.timeviewButton.Bind(wx.EVT_BUTTON, self.time)
        self.remotetimeButton.Bind(wx.EVT_BUTTON, self.getremotetime)
        self.posajustButton.Bind(wx.EVT_BUTTON, self.posautoajust)
        self.localtimeButton.Bind(wx.EVT_BUTTON, self.timeautoajust)

        self.controlgrid.Add(self.timeviewButton, pos=(0, 0))  # 布局
        self.controlgrid.Add(self.remotetimeButton, pos=(0, 1))
        self.controlgrid.Add(self.posajustButton, pos=(1, 0))
        self.controlgrid.Add(self.localtimeButton, pos=(1, 1))

        #时间区
        self.timeview = wx.CheckBox(self, -1, label=u'显示时间')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.Timeview, self.timeview)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.timeview)
        self.button1 = wx.Button(self, label='+1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_second, self.button1)
        self.button2 = wx.Button(self, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_second, self.button2)
        self.button3 = wx.Button(self, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(self, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)
        hbox1.Add(self.button1)
        hbox1.Add(self.button2)
        hbox1.Add(self.button3)
        hbox1.Add(self.button4)

        ##确认方式
        confirm_choice = ["E键", "回车"]
        self.confirm_choice = wx.Choice(self, -1, choices=confirm_choice)
        self.confirm_choice.SetSelection(0)
        self.Bind(wx.EVT_CHOICE, self.Confirmchoice, self.confirm_choice)

        self.confirm_label = wx.StaticText(self, label=u"确认提交方式     ")
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.confirm_label, flag=wx.TOP, border=4)
        hbox2.Add(self.confirm_choice)

        self.controlbox.Add(self.controlgrid)  # 把网格组加到 功能框内
        self.controlbox.Add(hbox1)
        self.controlbox.Add(hbox2)


    ###状态区
        self.status = wx.StaticBox(self, -1, "状态显示")
        self.statusbox = wx.StaticBoxSizer(self.status, wx.VERTICAL)
        self.statusgrid = wx.GridBagSizer(4, 2)

        self.net_status_text = wx.StaticText(self, -1, label="当前网速：")
        self.net_status = wx.StaticText(self, -1, label="5ms",  size=(70,20))
        self.lowestprice_status = wx.StaticText(self, -1, label="当前最低成交价：")
        self.lowestprice = wx.StaticText(self, -1, label="90000")
        self.userprice_status = wx.StaticText(self, -1, label="出价状态：")
        self.userprice = wx.StaticText(self, -1, label="90000")
        self.time_status = wx.StaticText(self, -1, label="与出价时间相差：")
        self.time = wx.StaticText(self, -1, label="1秒")
        self.price_status = wx.StaticText(self, -1, label="价格相差：")
        self.price = wx.StaticText(self, -1, label="100")

        self.statusgrid.Add(self.net_status_text, pos=(0, 0), flag=wx.RIGHT, border=5)
        self.statusgrid.Add(self.net_status, pos=(0, 1))
        self.statusgrid.Add(self.lowestprice_status, pos=(1, 0), flag=wx.RIGHT, border=5)
        self.statusgrid.Add(self.lowestprice, pos=(1,1))
        self.statusgrid.Add(self.userprice_status, pos=(2, 0), flag=wx.RIGHT, border=5)
        self.statusgrid.Add(self.userprice, pos=(2,1))
        self.statusgrid.Add(self.time_status, pos=(3, 0), flag=wx.RIGHT, border=5)
        self.statusgrid.Add(self.time, pos=(3,1))
        self.statusgrid.Add(self.price_status, pos=(4, 0), flag=wx.RIGHT, border=5)
        self.statusgrid.Add(self.price, pos=(4,1))

        self.statusbox.Add(self.statusgrid)
        self.reminder = wx.StaticBox(self, -1, "提示")
        self.reminderbox = wx.StaticBoxSizer(self.reminder, wx.VERTICAL)
        self.remindervbox = wx.BoxSizer(wx.VERTICAL)

        self.status_hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.current_strategy_label = wx.StaticText(self, -1, label="当前策略：")
        self.current_strategy = wx.StaticText(self, -1, label="")
        self.status_hbox1.Add(self.current_strategy_label)
        self.status_hbox1.Add(self.current_strategy)

        self.hotkey_confirm = wx.StaticText(self, -1, label="出价确认：")
        self.hotkey_smartprice = wx.StaticText(self, -1, label="智能出价：")
        self.remindervbox.Add(self.status_hbox1)
        self.remindervbox.Add(self.hotkey_confirm)
        self.remindervbox.Add(self.hotkey_smartprice)
        self.reminderbox.Add(self.remindervbox)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.controlbox, flag=wx.BOTTOM, border=10 )
        self.vbox.Add(self.statusbox, flag=wx.BOTTOM, border=10)
        self.vbox.Add(self.reminderbox, flag=wx.BOTTOM, border=10)
        self.SetSizer(self.vbox)

    ## 创建一个timer事件，修改状态
        self.status_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.status_Timer, self.status_timer)
        self.status_timer.Start(100)
    ## 创建时间框
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)

    #############消息区域
        pub.subscribe(self.change_strategy, 'change strategy')


    def status_Timer(self,event):
        now_ping = get_val('now_ping')
        lowest_price = get_val('lowest_price')
        if now_ping != 'timeout':
            self.net_status.SetLabel("%sms"%now_ping)
        else:
            self.net_status.SetLabel("%s"%now_ping)
        self.lowestprice.SetLabel(str(lowest_price))


    ##
    def time(self, event):
        pass

    ## 获取服务器时间
    def getremotetime(self, event):
        pass

    ## 同步本地时间
    def timeautoajust(self, event):
        guopai_on = get_val('guopai_on')
        moni_on = get_val('moni_on')
        imgpos_currenttime = get_val('imgpos_currenttime')
        timeset(guopai_on, moni_on, imgpos_currenttime, 'maindata.xml')  # 调用时间同步

    ##刷新定位
    def posautoajust(self, event):
        findpos()

    ##时间显示
    def Timeview(self, event):
        timeSelected = event.GetEventObject()
        view_time = get_val('view_time')
        time_on = get_val('time_on')
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
        if timeSelected.IsChecked():
            set_val('view_time', True)
            set_val('time_on', True)
            if guopai_on:
                self.timeframe1.Show(True)
            elif moni_on:
                self.timeframe2.Show(True)
        else:
            set_val('view_time', False)
            set_val('time_on', False)
            if guopai_on:
                self.timeframe1.Show(False)
            elif moni_on:
                self.timeframe2.Show(False)


    ##时间调整
    def Add_time(self, event):
        a_time = get_val('a_time')
        moni_second = get_val('moni_second')
        moni_on = get_val('moni_on')
        if moni_on:
            mt = moni_second - 0.1
            if mt >= 60:
                set_val('moni_second', mt - 60)
            else:
                print(moni_second)
                set_val('moni_second', moni_second + 0.1)
        else:
            set_val('a_time', a_time + 0.1)

    def Minus_time(self, event):
        a_time = get_val('a_time')
        moni_second = get_val('moni_second')
        moni_on = get_val('moni_on')
        if moni_on:
            mt = moni_second - 0.1
            if mt < 0:
                set_val('moni_second', 60 + mt)
            else:
                set_val('moni_second', moni_second - 0.1)
        else:
            set_val('a_time', a_time + 0.1)

    def Add_second(self, event):
        a_time = get_val('a_time')
        moni_second = get_val('moni_second')
        moni_on = get_val('moni_on')
        if moni_on:
            mt = moni_second + 1
            print(moni_second)
            if mt >= 60:
                set_val('moni_second', mt - 60)
            else:
                set_val('moni_second', moni_second + 1)
        else:
            set_val('a_time', a_time + 1)

    def Minus_second(self, event):
        a_time = get_val('a_time')
        moni_second = get_val('moni_second')
        moni_on = get_val('moni_on')
        if moni_on:
            mt = moni_second - 1
            if mt < 0:
                set_val('moni_second', 60 + mt)
            else:
                set_val('moni_second', moni_second - 1)

        else:
            set_val('a_time', a_time - 1)

    #关闭时间显示
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
        con = self.confirm_choice.GetSelection()
        if con == 0:
            set_val('e_on', True)
            set_val('enter_on', False)
        elif con == 1:
            set_val('e_on', False)
            set_val('enter_on', True)

    #######
    def change_strategy(self):
        current_strategy_name = get_val('current_strategy_name')
        self.current_strategy.SetLabel(current_strategy_name)


#-----------------------------------------------------------

class AccountPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        btn = wx.Button(self, label="3")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)


class StrategyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        Yanzhengmasize = get_val('Yanzhengmasize')
        set_val('one_real_time1', self.gettime(one_time1))
        set_val('one_real_time2', self.gettime(one_time2))
        set_val('second_real_time1', self.gettime(second_time1))
        set_val('second_real_time2', self.gettime(second_time2))
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)  # 绑定一个定时器事件，主判断
        self.timer1.Start(10)  # 设定时间间隔
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_count, self.timer2)  #
        self.timer2.Start(100)  # 设定时间间隔
        stractagy = wx.StaticBox(self, -1, u'选择策略:')
        self.stractagySizer = wx.StaticBoxSizer(stractagy, wx.VERTICAL)
        stractagy_label = wx.StaticText(self, label=u"设定拍牌策略", size=(100, 50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(stractagy_label)
        stractagy_choices = [u'单枪策略', u'双枪策略', u'手动操作（热键辅助）']
        self.select_stractagy = wx.Choice(self, -1, choices=stractagy_choices, size=(100, 50))
        hbox1.Add(self.select_stractagy)
        self.select_stractagy.SetSelection(0)


        vb1 = wx.BoxSizer(wx.VERTICAL)
        vb1.Add(hbox1)

        self.strategy_save = wx.Button(self, label="保存策略", size=(60, 35))
        self.strategy_load = wx.Button(self, label="载入策略", size=(60, 35))
        self.save_info = wx.Button(self, label="用户信息", size=(60, 35))
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.strategy_save)
        hbox4.Add(self.strategy_load)
        hbox4.Add(self.save_info)
        vb1.Add(hbox4)

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
        tijiao_label = wx.StaticText(self, label=u"强制提交时间")
        gridsizer1.Add(tijiao_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.tijiao_time.SetRange(40.0, 57.0)
        self.tijiao_time.SetValue(55.0)
        self.tijiao_time.SetIncrement(0.1)
        gridsizer1.Add(self.tijiao_time, pos=(2, 1))
        miao3_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)
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
        tijiao_label2 = wx.StaticText(self, label=u"强制提交时间")
        gridsizer2.Add(tijiao_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time2 = wx.SpinCtrlDouble(self, -1, "", size=(68, 25))
        self.tijiao_time2.SetRange(53.0, 57.0)
        self.tijiao_time2.SetValue(55.0)
        self.tijiao_time2.SetIncrement(0.1)
        gridsizer2.Add(self.tijiao_time2, pos=(2, 1))
        miao3_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao3_label2, pos=(2, 2), flag=wx.TOP, border=4)
        self.secondshotSizer.Add(gridsizer2, 0, flag=wx.ALL, border=5)
        self.stractagySizer.Add(vb1, 0, wx.ALL | wx.CENTER, 5)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
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
        self.secondsizer_Shown = False  # 二次出价默认关闭
        self.oneshotsizer_Shown = True  # 单次出价默认开启
        self.vbox1.Hide(self.secondshotSizer)  # 默认关闭二次出价
        self.Bind(wx.EVT_BUTTON, self.Strategy_save, self.strategy_save)
        self.Bind(wx.EVT_BUTTON, self.Strategy_load, self.strategy_load)
        self.Bind(wx.EVT_BUTTON, self.Save_info, self.save_info)
        self.Bind(wx.EVT_CHOICE, self.Refresh_panel, self.select_stractagy)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time, self.jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price, self.jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao, self.select_tijiao)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time, self.yanchi_time)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time, self.tijiao_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2, self.jiajia_time2)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price2, self.jiajia_price2)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao2, self.select_tijiao2)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time2, self.yanchi_time2)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time2, self.tijiao_time2)
        self.timeframe1 = TimeFrame()
        self.timeframe1.Show(False)
        self.timeframe2 = MoniTimeFrame()
        self.timeframe2.Show(False)
        self.operationtimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.opt, self.operationtimer)
        self.operationtimer.Start(1000)
        self.yanzhengmaframe = YanzhengmaFrame(Yanzhengmasize)

    def Price_view(self, event):
        Pricesize = get_val('Pricesize')
        Yanzhengmasize = get_val('Yanzhengmasize')
        yanzhengma_move = get_val('yanzhengma_move')
        Pos_price = get_val('Pos_price')
        imgpos_yanzhengma = get_val('imgpos_yanzhengma')
        yanzhengma_hash = get_val('yanzhengma_hash')
        Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
        if yanzhengma_move:
            yan = self.FindWindowById(18)
            if yan:
                try:
                    yan.Move(Pos_yanzhengmaframe)  # 移动到新位置
                    set_val('yanzhengma_move', False)  # 无需动作
                except:
                    pass
        price_view = get_val('price_view')
        price_count = get_val('price_count')
        if price_view and price_count >= 4:
            self.Screen_shot(Pos_price, Pricesize, "userprice.png")
            set_val('price_view', False)
            set_val('price_on', True)
        yanzhengma_count = get_val("yanzhengma_count")
        yanzhengma_close = get_val("yanzhengma_close")
        if yanzhengma_count >= 5 and not yanzhengma_close:  # 0.5秒之后没有确认触发关闭验证码
            find_yan_confirm()
        yanzhengma_close = get_val("yanzhengma_close")
        if yanzhengma_close:
            try:
                # print(yanzhengma_close,"yanzhengma_close")
                yan2 = self.FindWindowById(18)
                yan2.Show(False)
            except:
                pass
        yanzhengma_view = get_val('yanzhengma_view')
        if yanzhengma_view:
            set_val('yanzhengma_close', False)
            path = get_val('path')
            yanpath = path + "\\yanzhengma.png"
            cut_pic(imgpos_yanzhengma, Yanzhengmasize, yanpath)  # 直接调用得到 png
            set_val('yanzhengma_img', Image.open(yanpath))
            yanzhengma_img = get_val('yanzhengma_img')
            yan_hash = imagehash.dhash(yanzhengma_img)
            if not yanzhengma_hash:  # 第一次
                set_val('yanzhengma_hash', yan_hash)
            elif yan_hash == yanzhengma_hash:  # 验证码没变化
                pass
            else:
                set_val('yanzhengma_hash', yan_hash)
                try:
                    yan = self.FindWindowById(18)
                    yan.ShowImage(yanpath)
                    yan.Show()
                except:  # 找不到的情况下也要重新创建
                    pass
                finally:
                    pass

    def Yan_close(self, event):
        find_yan_confirm()

    def Price_count(self, event):
        price_count = get_val('price_count')
        yanzhengma_count = get_val('yanzhengma_count')
        set_val('price_count', 1 + price_count)
        set_val('yanzhengma_count', 1 + yanzhengma_count)

    def Screen_shot(self, box, size, name):
        Pricesize = get_val('Pricesize')
        region = ImageGrab.grab(box)
        path = get_val('path')
        imgname = path + '\\' + name
        region.resize(size, Image.ANTIALIAS).save(imgname)

    def Screen_shot_yanzhengma(self, box, size, name):
        Pricesize = get_val('Pricesize')
        region = ImageGrab.grab(box)
        cut_pic(region, size, name)



    def opt(self, event):
        moni_on = get_val('moni_on')
        moni_second = get_val('moni_second')
        one_time1 = get_val('one_time1')
        twice = get_val('twice')

        if moni_second < one_time1 and moni_on and not twice:  # 单次还原
            set_val('twice', False)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开
        elif moni_second < one_time1 and moni_on and twice:  # 二次还原
            set_val('twice', True)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开


    def Jiajia_time(self, event):
        one_time1 = get_val('one_time1')
        tem = self.jiajia_time.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            set_val('one_time1', tem)
            set_val('one_time1', float(one_time1))
            set_val('one_real_time1', self.gettime(one_time1))  # 计算得到的时间戳
        else:
            self.jiajia_time.SetValue(one_time1)

    def Jiajia_price(self, event):
        one_diff = get_val('one_diff')
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            set_val('one_diff', int(tem))
        else:
            self.jiajia_price.SetValue(one_diff)

    def Select_tijiao(self, event):
        select = self.select_tijiao.GetString(self.select_tijiao.GetSelection())
        if select == u"提前100":
            set_val('one_advance', 100)
        elif select == u"提前200":
            set_val('one_advance', 200)
        else:
            set_val('one_advance', 0)

    def Yanchi_time(self, event):
        one_delay = get_val('one_delay')
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            set_val('one_delay', float(tem))
        else:
            self.yanchi_time.SetValue(one_delay)

    def Tijiao_time(self, event):
        one_advance = get_val('one_advance')
        one_delay = get_val('one_delay')
        one_diff = get_val('one_diff')
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        one_real_time2 = get_val('one_real_time2')
        tem = self.tijiao_time.GetValue()
        templist = [40 + i * 0.1 for i in range(171)]
        if tem in templist:
            set_val('one_time2', float(tem))
            set_val('one_real_time2', self.gettime(one_time2))  # 计算得到的时间戳
        else:
            self.tijiao_time.SetValue(one_time2)

    def Jiajia_time2(self, event):
        second_time1 = get_val('second_time1')
        tem = self.jiajia_time2.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            set_val('second_time1', float(tem))
            set_val('second_real_time1', self.gettime(second_time1))  # 计算得到的时间戳
        else:
            self.jiajia_time2.SetValue(second_time1)

    def Jiajia_price2(self, event):
        second_diff = get_val('second_diff')
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            set_val('second_diff', int(tem))
        else:
            self.jiajia_price2.SetValue(second_diff)

    def Select_tijiao2(self, event):
        select = self.select_tijiao2.GetString(self.select_tijiao2.GetSelection())
        if select == u"提前100":
            set_val('second_advance', 100)
        elif select == u"提前200":
            set_val('second_advance', 200)
        else:
            set_val('second_advance', 0)

    def Yanchi_time2(self, event):
        second_delay = get_val('second_delay')
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            set_val('second_delay', float(tem))
        else:
            self.yanchi_time2.SetValue(second_delay)

    def Tijiao_time2(self, event):
        second_time2 = get_val('second_time2')
        tem = self.tijiao_time2.GetValue()
        templist = [53 + i * 0.1 for i in range(41)]
        if tem in templist:
            set_val('second_time2', float(tem))
            set_val('second_real_time2', self.gettime(second_time2))  # 计算得到的时间戳
        else:
            self.tijiao_time2.SetValue(second_time2)

    def Refresh_panel(self, event):
        stractagy_selection = self.select_stractagy.GetString(self.select_stractagy.GetSelection())
        if stractagy_selection == u"单枪策略":
            self.ss_Hide()
            set_val('twice', False)
            set_val('strategy_on', True)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开
        elif stractagy_selection == u"双枪策略":
            self.ss_Shown()
            set_val('strategy_on', True)
            set_val('twice', True)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开
        else:
            self.none_show()
            set_val('strategy_on', False)
            set_val('twice', False)

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
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')

        self.jiajia_time.SetValue(48.0)
        self.tijiao_time.SetValue(55.0)
        self.jiajia_price.SetValue(700)
        self.select_tijiao.SetSelection(0)
        self.yanchi_time.SetValue(0.5)
        set_val('one_time1', 48)  # 第一次出价加价
        set_val('one_time2', 55)  # 第一次出价提交
        set_val('one_diff', 700)  # 第一次加价幅度
        set_val('one_delay', 0.5)  # 第一次延迟
        set_val('one_advance', 100)  # 第一次提交提前量

        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        set_val('one_real_time1', self.gettime(one_time1))
        set_val('one_real_time2', self.gettime(one_time2))
        set_val('second_real_time1', self.gettime(second_time1))
        set_val('second_real_time2', self.gettime(second_time2))

    def Secondshot_reset(self):
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
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
        set_val('one_time1', 40)  # 第一次出价加价
        set_val('one_time2', 48)  # 第一次出价提交
        set_val('one_diff', 500)  # 第一次加价幅度
        set_val('one_delay', 0.5)  # 第一次延迟
        set_val('one_advance', 0)  # 第一次提交提前量
        set_val('second_time1', 50)  # 第二次次出价加价
        set_val('second_time2', 55.5)  # 第二次出价提交
        set_val('second_diff', 700)  # 第二次加价幅度
        set_val('second_delay', 0.5)  # 第二次出价延迟
        set_val('second_advance', 100)  # 第二次出价提交提前量
        set_val('one_real_time1', self.gettime(one_time1))
        set_val('one_real_time2', self.gettime(one_time2))
        set_val('second_real_time1', self.gettime(second_time1))
        set_val('second_real_time2', self.gettime(second_time2))


    def save(self, name):
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        one_diff = get_val('one_diff')
        one_delay = get_val('one_delay')
        one_advance = get_val('one_advance')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        second_diff = get_val('second_diff')
        second_delay = get_val('second_delay')
        second_advance = get_val('second_advance')
        osl = get_val('osl')
        e_on = get_val('e_on')
        enter_on = get_val('enter_on')
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
    #策略保存
    def Strategy_save(self, event):
        dlg = wx.TextEntryDialog(None, '设定你的策略名称:', "策略保存", "策略1",
                                 style=wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            name = dlg.GetValue()
            set_val('strategy_name', name)
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

    #策略修改
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
                (filepath, tempfilename) = os.path.split(path)
                (filename, extension) = os.path.splitext(tempfilename)
                set_val('current_strategy_name', filename)
                wx.CallAfter(pub.sendMessage, "change strategy")
            dlg.Destroy()
        else:
            dlg_tip = wx.MessageBox('找不到任何保存的策略', '策略载入', wx.OK | wx.ICON_ERROR)
            if dlg_tip == wx.ID_OK:
                dlg_tip.Destroy()

    def load(self, path):
        osl = get_val('osl')
        e_on = get_val('e_on')
        enter_on = get_val('enter_on')
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')

        try:
            with open(path, 'rb') as loadstr:
                set_val('osl', pickle.load(loadstr))
        except:
            pass
        if osl[0] == 0:  # 单次
            self.ss_Hide()
            set_val('twice', False)
            set_val('strategy_on', True)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开
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
            set_val('one_time1', osl[1])  # 第一次出价加价
            set_val('one_time2', osl[2])  # 第一次出价提交
            set_val('one_diff', osl[3])  # 第一次加价幅度
            set_val('one_delay', osl[4])  # 第一次延迟
            set_val('one_advance', osl[5])  # 第一次提交提前量
            set_val('e_on', osl[11])
            set_val('enter_on', osl[12])
            statuspad = self.FindWindowById(20)
            if e_on:
                statuspad.confirm_choice.SetSelection(0)
            elif enter_on:
                statuspad.confirm_choice.SetSelection(1)
            set_val('one_real_time1', self.gettime(one_time1))
            set_val('one_real_time2', self.gettime(one_time2))
            set_val('second_real_time1', self.gettime(second_time1))
            set_val('second_real_time2', self.gettime(second_time2))
        elif osl[0] == 1:  # 双枪
            set_val('strategy_on', True)
            set_val('twice', True)
            set_val('chujia_on', True)
            set_val('tijiao_on', False)
            set_val('tijiao_num', 1)  # 初始化
            set_val('tijiao_OK', False)
            set_val('tijiao_one', False)  # 单枪未开
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
            set_val('one_time1', osl[1])  # 第一次出价加价
            set_val('one_time2', osl[2])  # 第一次出价提交
            set_val('one_diff', osl[3])  # 第一次加价幅度
            set_val('one_delay', osl[4])  # 第一次延迟
            set_val('one_advance', osl[5])  # 第一次提交提前量
            set_val('second_time1', osl[6])  # 第二次次出价加价
            set_val('second_time2', osl[7])  # 第二次出价提交
            set_val('second_diff', osl[8])  # 第二次加价幅度
            set_val('second_delay', osl[9])  # 第二次出价延迟
            set_val('second_advance', osl[10])  # 第二次出价提交提前量
            set_val('e_on', osl[11])
            set_val('enter_on', osl[12])
            statuspad = self.FindWindowById(20)
            if e_on:
                statuspad.confirm_choice.SetSelection(0)
            elif enter_on:
                statuspad.confirm_choice.SetSelection(1)
            set_val('one_real_time1', self.gettime(one_time1))
            set_val('one_real_time2', self.gettime(one_time2))
            set_val('second_real_time1', self.gettime(second_time1))
            set_val('second_real_time2', self.gettime(second_time2))

    def findfiles(self, path):
        L = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.strategy':
                    L.append(os.path.join(root, file))
        return L

    def Save_info(self, event):
        pass

    def changetime(self, a):  # 换算成时间戳
        final_time = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
        return final_time  # 以时间戳输出

    def get_nowtime(self):
        tem1 = time.time()
        a = time.strftime('%Y-%m-%d', time.localtime(tem1))
        return a  # 输出时间格式字符串

    def gettime(self, choice):  # choice1:55,choice2:0.5
        tem = self.get_nowtime()
        b = tem + ' 11:29:' + str(int(choice))
        c = self.changetime(b) + float(choice) - int(choice)
        return c  # 得到用户所确定的最终时间戳


class OperationFrame(wx.Frame):
    def __init__(self, Px, Py, mainicon):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 2, title="小鲜肉代拍", pos=(Px + 902, Py), size=(300, 625), \
                          style=wx.FRAME_NO_TASKBAR | wx.CAPTION | wx.STAY_ON_TOP | wx.CLOSE_BOX)  # wx.FRAME_TOOL_WINDOW|   |wx.STAY_ON_TOP
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
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

        pub.subscribe(self.OnClose2, "close operation")


    def OnClose(self, event):
        guopai_on = get_val('guopai_on')
        if guopai_on:
            ret = wx.MessageBox('真的要退出吗?', '确认', wx.OK | wx.CANCEL)
            if ret == wx.OK:
                main = self.FindWindowById(1)
                main.Show(True)
                wx.CallAfter(pub.sendMessage, "close webframe")  # 关闭热键绑定
                self.Show(False)
        else:
            main = self.FindWindowById(1)
            main.Show(True)
            wx.CallAfter(pub.sendMessage, "close webframe")  # 关闭热键绑定
            self.Show(False)


    def OnClose2(self):
        main = self.FindWindowById(1)
        main.Show(True)
        self.Show(False)