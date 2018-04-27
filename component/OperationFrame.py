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
import pickle
import  os
from component.variable import set_val, get_val
from component.imgcut import findpos, timeset
from wx.lib.pubsub import pub
from component.variable import set_val, get_val

import logging

logger = logging.getLogger()


# -----------------------------------------------------------
class StatusPanel(wx.Panel):
    def __init__(self, parent, tablabel):
        wx.Panel.__init__(self, parent=parent, id=20)
        self.control = wx.StaticBox(self, -1, "功能区域")
        self.controlbox = wx.StaticBoxSizer(self.control, wx.VERTICAL)
        self.controlgrid = wx.GridBagSizer(4, 2)  # 网格组件

        ##功能区
        self.webtabButton = wx.Button(self, label=tablabel, size=(95, 30))  # 未来扩展
        # self.priceviewButton = wx.Button(self, label='导出跳价', size=(105,30))  # 未来扩展

        self.remotetimeButton = wx.Button(self, label='同步服务器时间', size=(95, 30))  # 时间
        self.posajustButton = wx.Button(self, label='刷新定位', size=(95, 30))  # 位置调整
        self.localtimeButton = wx.Button(self, label='同步网页时间', size=(95, 30))  # 时间同步

        ##绑定
        self.webtabButton.Bind(wx.EVT_BUTTON, self.webtab)
        # self.priceviewButton.Bind(wx.EVT_BUTTON, self.priceview)

        # self.remotetimeButton.Bind(wx.EVT_BUTTON, self.getremotetime)
        self.posajustButton.Bind(wx.EVT_BUTTON, self.posautoajust)
        # self.localtimeButton.Bind(wx.EVT_BUTTON, self.timeautoajust)

        self.controlgrid.Add(self.webtabButton, pos=(0, 0))  # 布局
        self.controlgrid.Add(self.remotetimeButton, pos=(0, 1))
        self.controlgrid.Add(self.posajustButton, pos=(1, 0))
        self.controlgrid.Add(self.localtimeButton, pos=(1, 1))

        # 时间区
        self.autotime = wx.CheckBox(self, -1, label=u'自动时间同步')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.autotime_set, self.autotime)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.autotime)
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

        self.confirm_label = wx.StaticText(self, label=u"确认提交方式")
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.confirm_label, flag=wx.TOP, border=4)
        hbox2.Add(self.confirm_choice)

        self.controlbox.Add(self.controlgrid)  # 把网格组加到 功能框内
        self.controlbox.Add(hbox1)
        self.controlbox.Add(hbox2)
##----------------------------------------------------------------------
        ###策略设置区域
        self.strategy_area_label = wx.StaticBox(self, -1, "策略设置")
        self.strategy_area_sizer = wx.StaticBoxSizer(self.strategy_area_label, wx.VERTICAL)
        self.strategy_area_vbox = wx.BoxSizer(wx.VERTICAL)
        strategy_choices = get_val('strategy_choices')
        self.choice_strategy = wx.ComboBox(self, choices=strategy_choices, size=(250, 25),
                         style=wx.CB_READONLY)
        self.choice_strategy.SetSelection(0)
        self.choice_strategy.Bind(wx.EVT_COMBOBOX, self.Choice_strategy)


        self.titlefont =  wx.Font(12, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL, False)
        self.numberfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.wordfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.strategy_oneshot_sizer = wx.BoxSizer(wx.VERTICAL)
        self.strategy_secondshot_sizer = wx.BoxSizer(wx.VERTICAL)


        ########第二次出价
        ##label行
        self.second_chujia_label = wx.StaticBox(self, -1, "第二次出价")
        self.second_chujia_label_sizer = wx.StaticBoxSizer(self.second_chujia_label, wx.VERTICAL)
        self.second_chujia_vbox = wx.BoxSizer(wx.VERTICAL)
        self.second_chujia_label.SetFont(self.titlefont)
        ##出价设置行
        self.second_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.second_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                    style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_jiajia_time.SetRange(0, 55)
        self.second_jiajia_time.SetValue(48)
        self.second_jiajia_time.SetIncrement(0.1)
        # self.second_jiajia_time.SetFont(self.numberfont)
        self.second_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.second_jiajia_price.SetRange(300, 1500)
        self.second_jiajia_price.SetValue(700)
        self.second_jiajia_price.SetIncrement(100)
        self.second_time_label = wx.StaticText(self, label="11 : 29 : ",
                                               style=wx.ALIGN_RIGHT | wx.TEXT_ALIGNMENT_CENTER, size=(65, 16))
        self.second_time_label.SetFont(self.numberfont)
        self.second_jiajia_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        self.second_jiajia_miao.SetFont(self.wordfont)
        self.second_jiahao = wx.StaticText(self, label=' 加价 ' ,style=wx.ALIGN_CENTER)
        self.second_jiahao.SetFont(self.wordfont)
        self.second_jiajia_sizer.Add(self.second_time_label,  wx.LEFT, border=10)
        self.second_jiajia_sizer.Add(self.second_jiajia_time)
        self.second_jiajia_sizer.Add(self.second_jiajia_miao)
        self.second_jiajia_sizer.Add(self.second_jiahao)
        self.second_jiajia_sizer.Add(self.second_jiajia_price)
        ##提交设置行
        self.second_tijiao_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tijiao_choices = get_val('tijiao_choices')
        self.second_tijiao_pricediff = wx.Choice(self, -1, choices=tijiao_choices, size=(80, 17))
        self.second_tijiao_pricediff.SetSelection(0)
        self.second_tijiaoyanchi_label = wx.StaticText(self, label=" 延迟", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiaoyanchi_label.SetFont(self.wordfont)
        self.second_tijiao_label = wx.StaticText(self, label=" 提交  ", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiao_label.SetFont(self.wordfont)
        self.second_tijiaoyanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiaoyanchi_time.SetRange(0.0, 1.9)
        self.second_tijiaoyanchi_time.SetValue(0.5)
        self.second_tijiaoyanchi_time.SetIncrement(0.1)
        self.second_tijiao_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        self.second_tijiao_miao.SetFont(self.wordfont)

        self.second_tijiao_sizer.Add(self.second_tijiao_pricediff, flag=wx.LEFT, border=10)
        self.second_tijiao_sizer.Add(self.second_tijiao_label, flag=wx.TOP, border=4)
        self.second_tijiao_sizer.Add(self.second_tijiaoyanchi_label, flag=wx.TOP, border=4)
        self.second_tijiao_sizer.Add(self.second_tijiaoyanchi_time, flag=wx.TOP, border=4)
        self.second_tijiao_sizer.Add(self.second_tijiao_miao, flag=wx.TOP, border=4)

        self.second_tijiaotime_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiaotime_label = wx.StaticText(self, label="11 : 29 : ", style=wx.ALIGN_RIGHT, size=(65, 16))
        self.second_tijiaotime_label.SetFont(self.numberfont)
        self.second_tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time.SetRange(0, 59)
        self.second_tijiao_time.SetValue(58)
        self.second_tijiao_time.SetIncrement(0.1)
        self.second_forcetijiao_label = wx.StaticText(self, label=" 秒 强制提交", style=wx.ALIGN_CENTER)
        self.second_forcetijiao_label.SetFont(self.wordfont)
        self.second_tijiaotime_sizer.Add(self.second_tijiaotime_label)
        self.second_tijiaotime_sizer.Add(self.second_tijiao_time)
        self.second_tijiaotime_sizer.Add(self.second_forcetijiao_label)
        self.second_chujia_vbox.Add(self.second_jiajia_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_vbox.Add(self.second_tijiao_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_vbox.Add(self.second_tijiaotime_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_label_sizer.Add(self.second_chujia_vbox)

        ########第三次出价
        ##label行
        self.third_chujia_label = wx.StaticBox(self, -1, "第三次出价")
        self.third_chujia_label_sizer = wx.StaticBoxSizer(self.third_chujia_label, wx.VERTICAL)
        self.third_chujia_vbox = wx.BoxSizer(wx.VERTICAL)
        self.third_chujia_label.SetFont(self.titlefont)
        ##出价设置行
        self.third_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.third_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                    style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_jiajia_time.SetRange(0, 55)
        self.third_jiajia_time.SetValue(48)
        self.third_jiajia_time.SetIncrement(0.1)
        # self.third_jiajia_time.SetFont(self.numberfont)
        self.third_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.third_jiajia_price.SetRange(300, 1500)
        self.third_jiajia_price.SetValue(700)
        self.third_jiajia_price.SetIncrement(100)
        self.third_time_label = wx.StaticText(self, label="11 : 29 : ",
                                               style=wx.ALIGN_RIGHT | wx.TEXT_ALIGNMENT_CENTER, size=(65, 16))
        self.third_time_label.SetFont(self.numberfont)
        self.third_jiajia_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        self.third_jiajia_miao.SetFont(self.wordfont)
        self.third_jiahao = wx.StaticText(self, label=' 加价 ' ,style=wx.ALIGN_CENTER)
        self.third_jiahao.SetFont(self.wordfont)
        self.third_jiajia_sizer.Add(self.third_time_label,  wx.LEFT, border=10)
        self.third_jiajia_sizer.Add(self.third_jiajia_time)
        self.third_jiajia_sizer.Add(self.third_jiajia_miao)
        self.third_jiajia_sizer.Add(self.third_jiahao)
        self.third_jiajia_sizer.Add(self.third_jiajia_price)
        ##提交设置行
        self.third_tijiao_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tijiao_choices = get_val('tijiao_choices')
        self.third_tijiao_pricediff = wx.Choice(self, -1, choices=tijiao_choices, size=(80, 17))
        self.third_tijiao_pricediff.SetSelection(0)
        self.third_tijiaoyanchi_label = wx.StaticText(self, label=" 延迟", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_tijiaoyanchi_label.SetFont(self.wordfont)
        self.third_tijiao_label = wx.StaticText(self, label=" 提交  ", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_tijiao_label.SetFont(self.wordfont)
        self.third_tijiaoyanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.third_tijiaoyanchi_time.SetRange(0.0, 1.9)
        self.third_tijiaoyanchi_time.SetValue(0.5)
        self.third_tijiaoyanchi_time.SetIncrement(0.1)
        self.third_tijiao_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        self.third_tijiao_miao.SetFont(self.wordfont)

        self.third_tijiao_sizer.Add(self.third_tijiao_pricediff, flag=wx.LEFT, border=10)
        self.third_tijiao_sizer.Add(self.third_tijiao_label, flag=wx.TOP, border=4)
        self.third_tijiao_sizer.Add(self.third_tijiaoyanchi_label, flag=wx.TOP, border=4)
        self.third_tijiao_sizer.Add(self.third_tijiaoyanchi_time, flag=wx.TOP, border=4)
        self.third_tijiao_sizer.Add(self.third_tijiao_miao, flag=wx.TOP, border=4)

        self.third_tijiaotime_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.third_tijiaotime_label = wx.StaticText(self, label="11 : 29 : ", style=wx.ALIGN_RIGHT, size=(65, 16))
        self.third_tijiaotime_label.SetFont(self.numberfont)
        self.third_tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.third_tijiao_time.SetRange(0, 59)
        self.third_tijiao_time.SetValue(58)
        self.third_tijiao_time.SetIncrement(0.1)
        self.third_forcetijiao_label = wx.StaticText(self, label=" 秒 强制提交", style=wx.ALIGN_CENTER)
        self.third_forcetijiao_label.SetFont(self.wordfont)
        self.third_tijiaotime_sizer.Add(self.third_tijiaotime_label)
        self.third_tijiaotime_sizer.Add(self.third_tijiao_time)
        self.third_tijiaotime_sizer.Add(self.third_forcetijiao_label)
        self.third_chujia_vbox.Add(self.third_jiajia_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_vbox.Add(self.third_tijiao_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_vbox.Add(self.third_tijiaotime_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_label_sizer.Add(self.third_chujia_vbox)


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


        ##构建组件
        #单枪
        self.strategy_secondshot_sizer.Add(self.second_chujia_label_sizer, flag=wx.ALL, border=3)
        self.strategy_secondshot_sizer.Add(self.third_chujia_label_sizer, flag=wx.ALL, border=3)

        self.strategy_area_vbox.Add(self.choice_strategy)
        self.strategy_area_vbox.Add(self.strategy_secondshot_sizer)
        self.strategy_area_sizer.Add(self.strategy_area_vbox)
##----------------------------------------------------------------------

        ##提示框
        self.reminder = wx.StaticBox(self, -1, "提示")
        self.reminderbox = wx.StaticBoxSizer(self.reminder, wx.VERTICAL)
        self.remindervbox = wx.BoxSizer(wx.VERTICAL)
        self.remindergrid = wx.GridBagSizer(6, 2)

        self.current_strategy_label = wx.StaticText(self, -1, label="当前策略：")
        self.current_strategy = wx.StaticText(self, -1, label="")

        self.hotkey_confirm_label = wx.StaticText(self, -1, label="热键状态：")
        self.hotkey_confirm = wx.StaticText(self, -1, label="启动正常", size=(100, 20))

        self.hotkey_smartprice_label = wx.StaticText(self, -1, label="智能出价：")
        self.hotkey_smartprice = wx.StaticText(self, -1, label="未开启")
        # 当前出价情况
        self.current_price = wx.StaticText(self, -1, label="出价状态")
        self.first_price_label = wx.StaticText(self, -1, label="第一次出价：")
        self.first_price = wx.StaticText(self, -1, label="100")
        self.second_price_label = wx.StaticText(self, -1, label="第二次出价：")
        self.second_price = wx.StaticText(self, -1, label="无")
        self.third_price_label = wx.StaticText(self, -1, label="第三次出价：")
        self.third_price = wx.StaticText(self, -1, label="无")

        self.remindergrid.Add(self.current_strategy_label, pos=(0, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.current_strategy, pos=(0, 1))
        self.remindergrid.Add(self.hotkey_confirm_label, pos=(1, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.hotkey_confirm, pos=(1, 1))
        self.remindergrid.Add(self.hotkey_smartprice_label, pos=(2, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.hotkey_smartprice, pos=(2, 1))
        self.remindergrid.Add(self.current_price, pos=(3, 0))
        self.remindergrid.Add(self.first_price_label, pos=(4, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.first_price, pos=(4, 1))
        self.remindergrid.Add(self.second_price_label, pos=(5, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.second_price, pos=(5, 1))
        self.remindergrid.Add(self.third_price_label, pos=(6, 0), flag=wx.RIGHT, border=20)
        self.remindergrid.Add(self.third_price, pos=(6, 1))

        self.reminderbox.Add(self.remindergrid)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.controlbox, flag=wx.BOTTOM, border=10)
        self.vbox.Add(self.strategy_area_sizer, flag=wx.BOTTOM, border=10)
        self.vbox.Add(self.reminderbox, flag=wx.BOTTOM, border=10)
        self.SetSizer(self.vbox)



        ## 创建时间框
        # self.timeframe1 = TimeFrame()
        # self.timeframe1.Show(False)
        # self.timeframe2 = MoniTimeFrame()
        # self.timeframe2.Show(False)

        #############消息区域
        pub.subscribe(self.change_strategy, 'change strategy')
        pub.subscribe(self.change_userprice, 'change userprice')  # 修改当前用户出价


    ###策略设置
    def Choice_strategy(self, event):
        pass


    ## 国拍与模拟切换
    def webtab(self, event):
        moni_on = get_val('moni_on')
        if moni_on:
            moni = wx.FindWindowByName('沪牌一号模拟')
            guopai = wx.FindWindowByName('沪牌一号 国拍')
            if guopai:
                guopai.Show(True)
                guopai.currentstatusframe.Show(True)
                guopai.operationpanel.init_ui()
                moni.Show(False)
                set_val('guopai_on', True)
                set_val('moni_on', False)
            else:
                moni.Show(False)
                wx.CallAfter(pub.sendMessage, "open dianxin")
        else:
            guopai = wx.FindWindowByName('沪牌一号 国拍')
            moni = wx.FindWindowByName('沪牌一号模拟')
            if moni:
                moni.Show(True)
                moni.currentstatusframe.Show(True)
                guopai.Show(False)
                moni.operationpanel.init_ui()
                set_val('moni_on', True)
                set_val('guopai_on', False)
            else:
                guopai.Show(False)
                wx.CallAfter(pub.sendMessage, "open moni")


    ##初始化
    def init_ui(self):
        e_on = get_val('e_on')
        enter_on = get_val('enter_on')
        autotime_on = get_val('autotime_on')
        if e_on:
            self.confirm_choice.SetSelection(0)
        elif enter_on:
            self.confirm_choice.SetSelection(1)
        if autotime_on:
            self.autotime.SetValue(True)
        else:
            self.autotime.SetValue(False)


    ##导出跳价
    def priceview(self, event):
        price_list = get_val('price_list')
        with open('price_list.txt', 'w') as price_file:
            for index, price in enumerate(price_list):
                text = "{0}秒： {1}".format(index, price)
                price_file.write(text)
                price_file.write('\n')

    def autotime_set(self, event):
        timeSelected = event.GetEventObject()
        if timeSelected.IsChecked():
            set_val('autotime_on', True)
        else:
            set_val('autotime_on', False)

    ##刷新定位
    def posautoajust(self, event):
        findpos()



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

    # # 关闭时间显示
    # def Closetime(self):
    #     try:
    #         self.timeframe1.Show(False)
    #     except:
    #         logger.exception('this is an exception message')
    #
    #     try:
    #         self.timeframe2.Show(False)
    #     except:
    #         logger.exception('this is an exception message')

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

    def change_userprice(self):
        userprice = get_val('userprice')
        self.userprice.SetLabel(str(userprice))

##-------------------------------------------------------------------------
    ##策略设置功能区
    def Jiajia_time(self, event):
        one_time1 = get_val('one_time1')
        tem = self.jiajia_time.GetValue()
        templist = [40 + i * 0.1 for i in range(151)]
        if tem in templist:
            one_time1 = tem
            set_val('one_time1', float(one_time1))
            set_val('one_real_time1', self.gettime(one_time1))  # 计算得到的时间戳
        else:
            self.jiajia_time.SetValue(one_time1)

    def Jiajia_time2(self, event):
        second_time1 = get_val('second_time1')
        tem = self.jiajia_time2.GetValue()
        templist = [400 + i * 1 for i in range(191)]
        if int(tem * 10) in templist:
            second_time1 = tem
            set_val('second_time1', float(tem))
            set_val('second_real_time1', self.gettime(second_time1))  # 计算得到的时间戳
        else:
            self.jiajia_time2.SetValue(second_time1)

    def Jiajia_price(self, event):
        one_diff = get_val('one_diff')
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price.GetValue()
        if tem in templist:
            set_val('one_diff', int(tem))
        else:
            self.jiajia_price.SetValue(one_diff)

    def Jiajia_price2(self, event):
        second_diff = get_val('second_diff')
        templist = [300 + i * 100 for i in range(13)]
        tem = self.jiajia_price2.GetValue()
        if tem in templist:
            set_val('second_diff', int(tem))
        else:
            self.jiajia_price2.SetValue(second_diff)

    def Select_tijiao(self, event):
        select = self.select_tijiao.GetString(self.select_tijiao.GetSelection())
        if select == u"提前100":
            set_val('one_advance', 100)
        elif select == u"提前200":
            set_val('one_advance', 200)
        else:
            set_val('one_advance', 0)

    def Select_tijiao2(self, event):
        select = self.select_tijiao2.GetString(self.select_tijiao2.GetSelection())
        if select == u"提前100":
            set_val('second_advance', 100)
        elif select == u"提前200":
            set_val('second_advance', 200)
        else:
            set_val('second_advance', 0)


    def Yanchi_time(self, event):
        one_delay = get_val('one_delay')
        templist = ['0.%d' % i for i in range(11)]
        templist.append('1.0')
        tem = str(self.yanchi_time.GetValue())
        if tem in templist:
            set_val('one_delay', float(tem))
        else:
            self.yanchi_time.SetValue(one_delay)

    def Yanchi_time2(self, event):
        second_delay = get_val('second_delay')
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.yanchi_time2.GetValue())
        if tem in templist:
            set_val('second_delay', float(tem))
        else:
            self.yanchi_time2.SetValue(second_delay)



    def Tijiao_time(self, event):
        one_time2 = get_val('one_time2')
        tem = self.tijiao_time.GetValue()
        templist = [400 + i * 1 for i in range(191)]
        if int(tem * 10) in templist:
            one_time2 = tem
            set_val('one_time2', float(one_time2))
            set_val('one_real_time2', self.gettime(one_time2))  # 计算得到的时间戳
        else:
            self.tijiao_time.SetValue(one_time2)


    def Tijiao_time2(self, event):
        second_time2 = get_val('second_time2')
        tem = self.tijiao_time2.GetValue()
        print("Tijiao_time2", tem)
        templist = [53 + i * 0.1 for i in range(51)]
        if tem in templist:
            second_time2 = tem
            set_val('second_time2', float(tem))
            set_val('second_real_time2', self.gettime(second_time2))  # 计算得到的时间戳
        else:
            self.tijiao_time2.SetValue(second_time2)
##-------------------------------------------------------------------------


class AccountPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        btn = wx.Button(self, label="3")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.smart_ajust = wx.CheckBox(self, -1, label=u'智能调整')  # 开启时间显示

        sizer.Add(btn, 0, wx.ALL, 10)
        sizer.Add(self.smart_ajust)
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CHECKBOX, self.Smart_ajust, self.smart_ajust)

    def Smart_ajust(self, event):
        if self.smart_ajust.IsChecked():
            set_val('smart_ajust', True)  # 开启自动价格调整
        else:
            set_val('smart_ajust', False)  # 关闭自动价格调整


class StrategyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        Yanzhengmasize = get_val('Yanzhengmasize')
        set_val('one_real_time1', self.gettime(one_time1))
        set_val('one_real_time2', self.gettime(one_time2))
        set_val('second_real_time1', self.gettime(second_time1))
        set_val('second_real_time2', self.gettime(second_time2))


        ## 换成线程处理
        # self.timer2 = wx.Timer(self)
        # self.Bind(wx.EVT_TIMER, self.Price_count, self.timer2)  #
        # self.timer2.Start(100)  # 设定时间间隔

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
        self.jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))  # ,style=wx.SP_WRAP最大值向上变最小值
        self.jiajia_time.SetRange(40, 55)
        self.jiajia_time.SetValue(48)
        self.jiajia_time.SetIncrement(0.1)
        gridsizer1.Add(self.jiajia_time, pos=(0, 0))
        miao_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao_label, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label = wx.StaticText(self, label=u"加价", style=wx.ALIGN_CENTER, size=(25, 25))
        gridsizer1.Add(jiahao_label, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price = wx.SpinCtrlDouble(self, -1, "秒", size=(58, 20))
        self.jiajia_price.SetRange(300, 1500)
        self.jiajia_price.SetValue(700)
        self.jiajia_price.SetIncrement(100)
        gridsizer1.Add(self.jiajia_price, pos=(0, 3))
        tijiao_choices = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao = wx.Choice(self, -1, choices=tijiao_choices, size=(58, 20))
        self.select_tijiao.SetSelection(0)
        gridsizer1.Add(self.select_tijiao, pos=(1, 0))
        yanchi_label = wx.StaticText(self, label=u"出价提交延迟")
        gridsizer1.Add(yanchi_label, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.yanchi_time.SetRange(0.0, 1.0)
        self.yanchi_time.SetValue(0.5)
        self.yanchi_time.SetIncrement(0.1)
        gridsizer1.Add(self.yanchi_time, pos=(1, 3))
        miao2_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao2_label, pos=(1, 4), flag=wx.TOP, border=4)
        tijiao_label = wx.StaticText(self, label=u"强制提交时间")
        gridsizer1.Add(tijiao_label, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.tijiao_time.SetRange(40.0, 59.0)
        self.tijiao_time.SetValue(55.0)
        self.tijiao_time.SetIncrement(0.1)
        gridsizer1.Add(self.tijiao_time, pos=(2, 1))
        miao3_label = wx.StaticText(self, label=u"秒")
        gridsizer1.Add(miao3_label, pos=(2, 2), flag=wx.TOP, border=4)
        self.oneshotSizer.Add(gridsizer1, 0, flag=wx.ALL, border=5)

        secondshot = wx.StaticBox(self, -1, u'双枪策略:')
        self.secondshotSizer = wx.StaticBoxSizer(secondshot, wx.VERTICAL)
        gridsizer2 = wx.GridBagSizer(4, 4)
        self.jiajia_time2 = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.jiajia_time2.SetRange(40, 55)
        self.jiajia_time2.SetValue(48)
        self.jiajia_time2.SetIncrement(0.1)
        gridsizer2.Add(self.jiajia_time2, pos=(0, 0))
        miao_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao_label2, pos=(0, 1), flag=wx.TOP | wx.ALIGN_LEFT, border=4)
        jiahao_label2 = wx.StaticText(self, label=u"加价", size=(25, 25), style=wx.ALIGN_CENTER)
        gridsizer2.Add(jiahao_label2, pos=(0, 2), flag=wx.TOP, border=4)
        self.jiajia_price2 = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.jiajia_price2.SetRange(300, 1500)
        self.jiajia_price2.SetValue(600)
        self.jiajia_price2.SetIncrement(100)
        gridsizer2.Add(self.jiajia_price2, pos=(0, 3))
        tijiao_choices2 = [u"提前100", u"提前200", u"踩点"]
        self.select_tijiao2 = wx.Choice(self, -1, choices=tijiao_choices2, size=(58, 20))
        self.select_tijiao2.SetSelection(0)
        gridsizer2.Add(self.select_tijiao2, pos=(1, 0))
        yanchi_label2 = wx.StaticText(self, label=u"出价提交延迟")
        gridsizer2.Add(yanchi_label2, pos=(1, 1), flag=wx.TOP, border=4)
        self.yanchi_time2 = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.yanchi_time2.SetRange(0.0, 1.0)
        self.yanchi_time2.SetValue(0.5)
        self.yanchi_time2.SetIncrement(0.1)
        gridsizer2.Add(self.yanchi_time2, pos=(1, 3))
        miao2_label2 = wx.StaticText(self, label=u"秒")
        gridsizer2.Add(miao2_label2, pos=(1, 4), flag=wx.TOP, border=4)
        tijiao_label2 = wx.StaticText(self, label=u"强制提交时间")
        gridsizer2.Add(tijiao_label2, pos=(2, 0), flag=wx.TOP, border=4)
        self.tijiao_time2 = wx.SpinCtrlDouble(self, -1, "", size=(58, 20))
        self.tijiao_time2.SetRange(52.0, 59.0)
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
            one_time1 = tem
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
        one_time2 = get_val('one_time2')
        tem = self.tijiao_time.GetValue()
        templist = [400 + i * 1 for i in range(191)]
        if int(tem * 10) in templist:
            one_time2 = tem
            set_val('one_time2', float(one_time2))
            set_val('one_real_time2', self.gettime(one_time2))  # 计算得到的时间戳
        else:
            self.tijiao_time.SetValue(one_time2)

    def Jiajia_time2(self, event):
        second_time1 = get_val('second_time1')
        tem = self.jiajia_time2.GetValue()
        templist = [400 + i * 1 for i in range(191)]
        if int(tem * 10) in templist:
            second_time1 = tem
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
        print("Tijiao_time2", tem)
        templist = [53 + i * 0.1 for i in range(51)]
        if tem in templist:
            second_time2 = tem
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
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
        set_val('one_real_time1', self.gettime(one_time1))
        set_val('one_real_time2', self.gettime(one_time2))
        set_val('second_real_time1', self.gettime(second_time1))
        set_val('second_real_time2', self.gettime(second_time2))

    def Secondshot_reset(self):
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
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        second_time2 = get_val('second_time2')
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

    # 策略保存
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

    # 策略修改
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

    ##执行策略导入
    def load(self, path):
        try:
            with open(path, 'rb') as loadstr:
                set_val('osl', pickle.load(loadstr))
            osl = get_val('osl')
            self.update_ui(osl)
        except:
            logger.exception('this is an exception message')

    ##保持国拍与模拟的一致性
    def init_ui(self):
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
        e_on = get_val('e_on')
        enter_on = get_val('enter_on')
        osl = [0] * 13

        ##初始化为第二次出价
        set_val('current_pricestatus_label', '等待第二次出价')
        one_time1 = get_val('one_time1')
        one_diff = get_val('one_diff')
        current_pricestatus = '{0}秒加{1}'.format(one_time1, one_diff)
        set_val('current_pricestatus', current_pricestatus)

        if self.select_stractagy.GetSelection() == 0:
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
        elif self.select_stractagy.GetSelection() == 2:
            osl[0] = 2
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
        self.update_ui(osl)



    def update_ui(self, osl):
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

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
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

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
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


# class OperationFrame(wx.Frame):
#     def __init__(self, Px, Py, mainicon):  # name:窗口显示名称
#         wx.Frame.__init__(self, None, 2, title="沪牌一号", pos=(Px + 902, Py), size=(300, 625), \
#                           style=wx.FRAME_NO_TASKBAR | wx.CAPTION | wx.CLOSE_BOX)  #
#         self.Bind(wx.EVT_CLOSE, self.OnClose)
#         self.notebook = wx.Notebook(self)
#         self.status_tab = StatusPanel(self.notebook)  # notebook作为父类
#         self.notebook.AddPage(self.status_tab, "常规功能")
#         self.strategy_tab = StrategyPanel(self.notebook)
#         self.notebook.AddPage(self.strategy_tab, "策略设置")
#         self.account_tab = AccountPanel(self.notebook)
#         self.notebook.AddPage(self.account_tab, "账号设置")
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 5)
#         self.SetSizer(sizer)
#         self.Layout()
#         self.Show(False)  # 初始隐藏
#
#         pub.subscribe(self.OnClose2, "close operation")
#
#     def OnClose(self, event):
#         guopai_on = get_val('guopai_on')
#         if guopai_on:
#             dlg = wx.MessageDialog(None, "确认要关闭国拍吗?",
#                                    '关闭国拍页面',
#                                    wx.YES_NO | wx.ICON_WARNING | wx.STAY_ON_TOP)
#             ret = dlg.ShowModal()
#             if ret == wx.ID_YES:
#                 main = self.FindWindowById(1)
#                 main.Show(True)
#                 wx.CallAfter(pub.sendMessage, "close webframe")  # 关闭热键绑定
#                 self.Show(False)
#             dlg.Destroy()
#         else:
#             main = self.FindWindowById(1)
#             main.Show(True)
#             wx.CallAfter(pub.sendMessage, "close webframe")  # 关闭热键绑定
#             self.Show(False)
#
#     def OnClose2(self):
#         main = self.FindWindowById(1)
#         main.Show(True)
#         self.Show(False)


class OperationPanel(wx.Panel):
    def __init__(self, parent, tablabel):  # name:窗口显示名称
        websize = get_val('websize')
        htmlsize = get_val('htmlsize')
        x0 = websize[0] - htmlsize[0]
        wx.Panel.__init__(self, parent=parent, size=(x0, websize[1]), pos=(892, 0))
        self.notebook = wx.Notebook(self)
        self.status_tab = StatusPanel(self.notebook, tablabel)  # notebook作为父类
        self.notebook.AddPage(self.status_tab, "常规功能")
        self.strategy_tab = StrategyPanel(self.notebook)
        self.notebook.AddPage(self.strategy_tab, "策略设置")
        # self.account_tab = AccountPanel(self.notebook)
        # self.notebook.AddPage(self.account_tab, "账号设置")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1)
        self.SetSizer(sizer)
        self.Layout()

    def init_ui(self):
        self.strategy_tab.init_ui()
        self.status_tab.init_ui()