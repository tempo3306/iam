from component.imgcut import findpos
from component.staticmethod import *
import logging

logger = logging.getLogger()
from component.variable import get_dick, set_dick, get_strategy_dick


class PaishouPanel(wx.Panel):
    def __init__(self, parent, tablabel):
        wx.Panel.__init__(self, parent=parent, id=20)
        self.control = wx.StaticBox(self, -1, "基本设置")
        self.controlbox = wx.StaticBoxSizer(self.control, wx.VERTICAL)
        self.controlgrid = wx.GridBagSizer(4, 2)  # 网格组件

        ##功能区
        self.webtabButton = wx.Button(self, label=tablabel, size=(95, 30))  # 未来扩展
        # self.priceviewButton = wx.Button(self, label='导出跳价', size=(105,30))  # 未来扩展

        self.onkeyloginButton = wx.Button(self, label='一键登录', size=(95, 30))  # 时间
        self.posajustButton = wx.Button(self, label='刷新定位', size=(95, 30))  # 位置调整
        self.refreshwebButton = wx.Button(self, label='刷新页面', size=(95, 30))  # 时间同步

        ##绑定
        self.webtabButton.Bind(wx.EVT_BUTTON, self.webtab)
        self.refreshwebButton.Bind(wx.EVT_BUTTON, self.refreshweb)
        # self.priceviewButton.Bind(wx.EVT_BUTTON, self.priceview)

        # self.remotetimeButton.Bind(wx.EVT_BUTTON, self.getremotetime)
        self.posajustButton.Bind(wx.EVT_BUTTON, self.posautoajust)
        self.onkeyloginButton.Bind(wx.EVT_BUTTON, self.onkeylogin)

        self.controlgrid.Add(self.webtabButton, pos=(0, 0))  # 布局
        self.controlgrid.Add(self.onkeyloginButton, pos=(0, 1))
        self.controlgrid.Add(self.posajustButton, pos=(1, 0))
        self.controlgrid.Add(self.refreshwebButton, pos=(1, 1))

        # # 验证码放大
        self.yanzhengma_scale = wx.CheckBox(self, -1, label=u'验证码放大')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.Yanzhengma_scale, self.yanzhengma_scale)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.yanzhengma_scale)

        # # 时间区
        # self.autotime = wx.CheckBox(self, -1, label=u'自动时间同步')  # 开启时间显示
        # self.Bind(wx.EVT_CHECKBOX, self.autotime_set, self.autotime)
        # hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # hbox1.Add(self.autotime)

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

        ##----------------------------------------------------------------------------------
        ##提示框
        self.reminder = wx.StaticBox(self, -1, "操作提示")
        self.reminderbox = wx.StaticBoxSizer(self.reminder, wx.VERTICAL)
        self.reminderhbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hotkey_bmp = wx.StaticBitmap(self, -1)
        self.hotkey_bmp.SetBitmap(wx.Bitmap('hotkey.png'))
        self.reminderhbox.Add(self.hotkey_bmp, flag=wx.RIGHT, border=32)

        self.reminderbox.Add(self.reminderhbox, flag=wx.ALL, border=5)
        ##-------------------------------------------------------------------------------------
        ##将所有sizer组合
        # self.reminderbox.Add(self.remindergrid)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.controlbox, flag=wx.BOTTOM, border=10)
        self.vbox.Add(self.reminderbox, flag=wx.BOTTOM, border=10)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox.Add(self.vbox, flag=wx.LEFT, border=10)
        self.SetSizer(self.hbox)

        ###初始化sizer

        #############消息区域
        pub.subscribe(self.change_strategy, 'change strategy')
        pub.subscribe(self.change_userprice, 'change userprice')  # 修改当前用户出价

    ## 验证码放大
    def Yanzhengma_scale(self, event):
        if self.yanzhengma_scale.IsChecked():
            set_dick("yanzhengma_scale", True)
        else:
            set_dick("yanzhengma_scale", False)

    ## 国拍与模拟切换
    def webtab(self, event):
        moni_on = get_val('moni_on')
        if moni_on:
            from component.app_thread import GetremotetimeThread
            getremotetimethread = GetremotetimeThread()  ##同步国拍时间
            moni_webframe = get_val('moni_webframe')
            guopai_webframe = get_val('guopai_webframe')
            moni = wx.FindWindowById(moni_webframe)
            guopai = wx.FindWindowById(guopai_webframe)
            if guopai_webframe != -1:
                guopai.Show(True)
                guopai.currentstatusframe.Show(False)
                guopai.operationpanel.init_ui()
                moni.Show(False)
                moni.currentstatusframe.Show(False)
                moni.yanzhengmaframe.Show(False)
                set_val('guopai_on', True)
                set_val('moni_on', False)
            else:
                moni.Show(False)
                moni.currentstatusframe.Show(False)
                moni.yanzhengmaframe.Show(False)
                wx.CallAfter(pub.sendMessage, "open dianxin")
        else:
            moni_webframe = get_val('moni_webframe')
            guopai_webframe = get_val('guopai_webframe')
            moni = wx.FindWindowById(moni_webframe)
            guopai = wx.FindWindowById(guopai_webframe)
            if moni_webframe != -1:
                moni.Show(True)
                # moni.htmlpanel.webview.Reload()
                moni.currentstatusframe.Show(False)
                guopai.Show(False)
                guopai.currentstatusframe.Show(False)
                guopai.yanzhengmaframe.Show(False)
                moni.operationpanel.init_ui()
                set_val('moni_on', True)
                set_val('guopai_on', False)
            else:
                guopai.Show(False)
                guopai.currentstatusframe.Show(False)
                guopai.yanzhengmaframe.Show(False)
                wx.CallAfter(pub.sendMessage, "open moni")

    def refreshweb(self, event):
        moni_on = get_val('moni_on')
        if moni_on:
            wx.CallAfter(pub.sendMessage, "moni refresh_web")
        else:
            wx.CallAfter(pub.sendMessage, "guopai refresh_web")

    def onkeylogin(self, event):
        guopai_on = get_val('guopai_on')
        if guopai_on:
            print("fdssfs")
            wx.CallAfter(pub.sendMessage, "onekey_login")




    ##初始化
    def init_ui(self):
        enter_on = get_dick('enter_on')
        if enter_on:
            self.confirm_choice.SetSelection(1)
        else:
            self.confirm_choice.SetSelection(0)

        yanzhengma_scale = get_dick('yanzhengma_scale')
        if yanzhengma_scale:
            self.yanzhengma_scale.SetValue(True)
        else:
            self.yanzhengma_scale.SetValue(False)

        strategy_type = get_dick('strategy_type')
        self.update_ui(strategy_type)


    def update_ui(self, strategy_type):  ##根据不同的出价策略调整界面
        strategy_list = get_dick(strategy_type)

        print('strategy_list', strategy_list)

        if strategy_type == '0':  # 单次
            init_strategy()

            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('second_forcetijiao_on', strategy_list[6])  # 强制提交
            set_val('smart_autoprice', strategy_list[7])  # 强制提交

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))
            set_val('second_real_time2', gettime(second_time2))
            self.Layout()

        elif strategy_type == '1':  # 双枪
            init_strategy()
            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('one_forcetijiao_on', strategy_list[6])

            set_val('second_time1', strategy_list[8])  # 第二次次出价加价
            set_val('second_diff', strategy_list[9])  # 第二次加价幅度
            set_val('second_advance', strategy_list[10])  # 第二次出价提交提前量
            set_val('second_delay', strategy_list[11])  # 第二次出价延迟
            set_val('second_time2', strategy_list[12])  # 第二次出价提交
            set_val('second_forcetijiao_on', strategy_list[13])

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))
            set_val('second_real_time2', gettime(second_time2))



        elif strategy_type == '2':  # 单枪动态提交
            init_strategy()
            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('smart_autoprice', strategy_list[7])  # 强制提交

            set_val('one_advance_smart1', strategy_list[14])
            set_val('one_delay_smart1', strategy_list[15])
            set_val('one_time2_smart1', strategy_list[16])
            set_val('one_advance_smart2', strategy_list[17])
            set_val('one_delay_smart2', strategy_list[18])
            set_val('one_time2_smart2', strategy_list[19])
            set_val('one_advance_smart3', strategy_list[20])
            set_val('one_delay_smart3', strategy_list[21])
            set_val('one_time2_smart3', strategy_list[22])
            set_val('one_time2_smart', strategy_list[23])

            set_val('one_real_time1', gettime(strategy_list[1]))  ##第一次出价时间戳
            set_val('one_realtime2_smart1', gettime(strategy_list[16]))
            set_val('one_realtime2_smart2', gettime(strategy_list[19]))
            set_val('one_realtime2_smart3', gettime(strategy_list[22]))
            set_val('one_realtime2_smart', gettime(strategy_list[23]))

        elif strategy_type == '3':  # 双枪动态提交
            init_strategy()

            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('one_forcetijiao_on', strategy_list[6])

            set_val('second_time1', strategy_list[8])  # 第二次次出价加价
            set_val('second_diff', strategy_list[9])  # 第二次加价幅度

            set_val('one_advance_smart1', strategy_list[14])
            set_val('one_delay_smart1', strategy_list[15])
            set_val('one_time2_smart1', strategy_list[16])
            set_val('one_advance_smart2', strategy_list[17])
            set_val('one_delay_smart2', strategy_list[18])
            set_val('one_time2_smart2', strategy_list[19])
            set_val('one_advance_smart3', strategy_list[20])
            set_val('one_delay_smart3', strategy_list[21])
            set_val('one_time2_smart3', strategy_list[22])
            set_val('one_time2_smart', strategy_list[23])

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))

            set_val('one_realtime2_smart1', gettime(strategy_list[16]))
            set_val('one_realtime2_smart2', gettime(strategy_list[19]))
            set_val('one_realtime2_smart3', gettime(strategy_list[22]))
            set_val('one_realtime2_smart', gettime(strategy_list[23]))

            self.Layout()

    ##导出跳价
    def priceview(self, event):
        price_list = get_val('price_list')
        with open('price_list.txt', 'w') as price_file:
            for index, price in enumerate(price_list):
                text = "{0}秒： {1}".format(index, price)
                price_file.write(text)
                price_file.write('\n')

    ##刷新定位
    def posautoajust(self, event):
        findpos()

    def Confirmchoice(self, event):
        con = self.confirm_choice.GetSelection()
        if con == 0:
            set_dick('enter_on', False)
        elif con == 1:
            set_dick('enter_on', True)

    #######
    def change_strategy(self):
        pass

    def change_userprice(self):
        pass