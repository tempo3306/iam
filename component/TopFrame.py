# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 14:37
'''
import wx
import time


class TopFrame(wx.Frame):
    def __init__(self, name, rev):  ##########版本号
        wx.Frame.__init__(self, None, 1, name,
                          size=(280, 300), pos=(Px - 120, Py), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # 状态栏
        self.statusbar = self.CreateStatusBar()
        # 将状态栏分割为3个区域,比例为1:2:3
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.statusbar.SetStatusText(u"版本号", 0)

        # 设置状态栏2内容
        self.statusbar.SetStatusText(u"%s" % rev, 1)

        # 设置状态栏3内容
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        self.statusbar.SetBackgroundColour((240, 255, 255))
        # 创建一个容器
        panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        panel.SetBackgroundColour((240, 255, 255))
        self.SetBackgroundColour((240, 255, 255))
        ############################
        #######功能区#########
        self.operationarea = wx.StaticBox(panel, label="基本功能")
        self.operationareasizer = wx.StaticBoxSizer(self.operationarea, wx.VERTICAL)

        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.monibutton = wx.Button(panel, label='打开模拟')
        self.Bind(wx.EVT_BUTTON, self.Openmoni, self.monibutton)
        ###打开国拍
        self.guopaibutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.Openurlchoice, self.guopaibutton)
        self.hbox1.Add(self.monibutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.guopaibutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox1)
        ###验证码练习
        self.helpbutton = wx.Button(panel, label='查看帮助')
        self.Bind(wx.EVT_BUTTON, self.help, self.helpbutton)
        self.rulebutton = wx.Button(panel, label='查看规定')
        self.Bind(wx.EVT_BUTTON, self.rule, self.rulebutton)
        # self.yanzhengmabutton = wx.Button(panel, label='验证码练习')
        # self.Bind(wx.EVT_BUTTON, self.Yan_practice, self.yanzhengmabutton)
        # self.testbutton = wx.Button(panel, label='考核')
        # self.Bind(wx.EVT_BUTTON, self.Yan_test, self.testbutton)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2.Add(self.helpbutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox2.Add(self.rulebutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox2)

        ########设置区#########
        self.set = wx.StaticBox(panel, label="常规设置")
        self.setsizer = wx.StaticBoxSizer(self.set)

        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.advanceset = wx.Button(panel, label='策略设置')
        self.posautoset = wx.Button(panel, label='刷新定位')
        self.Bind(wx.EVT_BUTTON, self.Advanceset, self.advanceset)
        self.Bind(wx.EVT_BUTTON, self.Posautoset, self.posautoset)
        self.hbox3.Add(self.advanceset, 0, wx.ALL | wx.CENTER, 5)
        self.hbox3.Add(self.posautoset, 0, wx.ALL | wx.CENTER, 5)

        self.hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.highadvanceset = wx.Button(panel, label='动态策略')
        self.timeautoreset = wx.Button(panel, label='时间同步')
        self.hbox4.Add(self.highadvanceset, 0, wx.ALL | wx.CENTER, 5)
        self.hbox4.Add(self.timeautoreset, 0, wx.ALL | wx.CENTER, 5)

        self.vbox_setting = wx.BoxSizer(wx.VERTICAL)

        self.vbox_setting.Add(self.hbox3)
        self.vbox_setting.Add(self.hbox4)
        self.setsizer.Add(self.vbox_setting)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.operationareasizer, 0, wx.ALL | wx.CENTER, 5)
        self.vbox.Add(self.setsizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(self.vbox)

        # ###修改国拍网址
        # self.button16 = wx.Button(panel, label='修改国拍网址', pos=(370, 190))
        # self.Bind(wx.EVT_BUTTON, self.UrlGuopai, self.button16)
        # self.urlText = wx.TextCtrl(panel, -1, pos=(370, 230),size=(120,25))
        # ###显示提示
        # self.button7 = wx.Button(panel, label='显示帮助', pos=(10, 190))
        # self.Bind(wx.EVT_BUTTON, self.Help, self.button7)

        # --------------------------------------------------------------------------------
        # ########设置区############
        self.thread = TimeThread()  # 创建时间进程

        # 暂时停止登录确认进程
        #         self.keepthread=KeepThread()
        ###########创建操作面板
        self.operationframe = OperationFrame(Px, Py, mainicon)
        self.operationframe.Show(False)  # 初始关闭
        # --------------------------------------------------------------------------------
        ##########控制操作台
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)  # 绑定一个定时器事件，主判断
        self.timer2.Start(100)  # 设定时间间隔

        # 读取最低成交价
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)  # 设置一个截屏取价  和查看时间
        self.timer3.Start(50)
        # 自动定位
        # self.timer4=wx.Timer(self)
        # self.Bind(wx.EVT_TIMER, self.Find_pos, self.timer4)#设置一个截屏取价
        # self.timer4.Start(600)

        # 时间同步
        self.Bind(wx.EVT_BUTTON, self.Time_autoajust, self.timeautoreset)  # 设置一个截屏取价

        # 登录确认器  ,放入独立进程管理
        # self.timer3=wx.Timer(self)
        # self.timer3.Start(90000)  #设定时间间隔，1分半执行一次
        # self.Bind(wx.EVT_TIMER,self.Confirmlogin,self.timer3)

        # 触发打开不同网址的国拍
        pub.subscribe(self.OpenGuopai_dianxin, "open dianxin")  # 打开电信
        pub.subscribe(self.OpenGuopai_nodianxin, "open nodianxin")  # 打开非电信
        pub.subscribe(self.OpenGuopai_userweb, "open userweb")  # 使用用户自己的IE
        pub.subscribe(self.Close, "close topframe")  #

    # ------------------------------------------------------------------
    # 功能区
    def Openmoni(self, event):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK, twice
        timer0 = threading.Timer(5, findpos)
        strategy_on = True
        twice = False
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url1, ad_view, web_on, do, guopai_on, moni_on, strategy_repeat
        if guopai_on:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif moni_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:

            # if not strategy_repeat :  # 判断自动出价进程是否开启
            #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
            #     strategy_repeat=True  #防止进程重复开启
            self.Open()
            if do:
                moni_on = True  # 模拟打开
                ad_view = True
                web_on = True
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟', (websize[0], websize[1]))
                # self.operationframe.Show(True)  # 开启控制面板显示
                # 查看时间框是否应该显示
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:  # 判断自动出价进程是否开启
                    self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                    self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                    strategy_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # pub.subscribe(self.tijiaoPos, "tijiao")
                # pub.subscribe(self.refreshPos, "refresh")
                # pub.subscribe(self.secondPos, "second")
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()
            self.Listen()

    def Openurlchoice(self, event):
        guopai = GuopaiFrame("国拍",mainicon)

    def OpenGuopai_dianxin(self):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK, twice
        timer0 = threading.Timer(5, findpos)
        strategy_on = True
        twice = False
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url2, ad_view, web_on, do, moni_on, guopai_on, strategy_repeat
        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
            # if not strategy_repeat :  # 判断自动出价进程是否开启
            #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
            #     strategy_repeat=True  #防止进程重复开启
            if do:
                ad_view = True
                guopai_on = True
                self.fr = WebFrame(Px, Py, False, '沪牌一号 国拍', (websize[0], websize[1]))  # 暂时关闭广告
                # self.operationframe.Show(True)  # 开启控制面板显示
                # 查看时间框是否应该显示
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:  # 判断自动出价进程是否开启
                    self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                    self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                    strategy_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,  style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # 价格显示
                self.Listen()
                # pub.subscribe(self.OnCalculatepos, "refresh")
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()  # 关闭可能注册的热键

    def OpenGuopai_nodianxin(self):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK, twice
        timer0 = threading.Timer(5, findpos)
        strategy_on = True
        twice = False  #初始化双枪不触发
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url3, ad_view, web_on, do, moni_on, guopai_on, strategy_repeat
        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:

            self.Open()
            # if not strategy_repeat :  # 判断自动出价进程是否开启
            #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
            #     strategy_repeat=True  #防止进程重复开启
            if do:
                ad_view = True
                guopai_on = True
                self.fr = WebFrame(Px, Py, False, '沪牌一号 国拍',(websize[0], websize[1]))  # 暂时关闭广告
                # self.operationframe.Show(True)  # 开启控制面板显示
                # 查看时间框是否应该显示
                if time_on:
                    self.operationframe.Opentime()
                if not strategy_repeat:  # 判断自动出价进程是否开启
                    self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                    self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                    strategy_repeat = True

                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos ,style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # 价格显示
                self.Listen()
                # pub.subscribe(self.OnCalculatepos, "refresh")
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                self.Close()  # 关闭可能注册的热键

    def OpenGuopai_userweb(self):
        # 初始化
        global tijiao_num, chujia_on, tijiao_on, strategy_on, tijiao_OK, twice
        timer0 = threading.Timer(5, findpos)  # 几秒之后执行一次位置刷新
        strategy_on = True
        twice = False
        chujia_on = True
        tijiao_on = False
        tijiao_num = 1  # 初始化
        tijiao_OK = False
        global Px, Py, url3, ad_view, web_on, do, moni_on, guopai_on, strategy_repeat

        self.Open()

        # if not strategy_repeat :  # 判断自动出价进程是否开启
        #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
        #     strategy_repeat=True  #防止进程重复开启
        # print(do)
        if do:
            ad_view = True
            guopai_on = True
            # self.fr = WebFrame(Px, Py, False, '沪牌一号 国拍')  # 暂时关闭广告
            # self.operationframe.Show(True)  # 开启控制面板显示
            # 查看时间框是否应该显示
            if time_on:
                self.operationframe.Opentime()
            if not strategy_repeat:  # 判断自动出价进程是否开启
                self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                strategy_repeat = True
                #
                # browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=(-17, 0))
                # browser.LoadURL(url3)
                # browser.CanSetZoomType(False)
                # self.fr.Show(False)
                # 价格显示
                openIE(url3)
                # print("fsdf")
                self.Listen()
            # pub.subscribe(self.OnCalculatepos, "refresh")
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            self.Close()  # 关闭可能注册的热键

    def UrlGuopai(self, event):
        global url2
        try:
            url2 = self.urlText.GetValue()
            wx.MessageBox('修改网址成功', '修改国拍网址', wx.OK)
        except:
            wx.MessageBox('请输入正确网址', '修改国址网址', wx.OK | wx.ICON_ERROR)

    def Help(self, event):
        licence = """

 谁帮我写个帮助啊
 啊
 啊
 啊"""

        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetName("小鲜肉拍牌")
        aboutInfo.SetVersion(licence)
        # aboutInfo.SetDescription("最好的拍牌软件!")
        # aboutInfo.SetCopyright("(C) 2017-2022")
        # aboutInfo.SetWebSite("http:#myapp.org")
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)

    # 打开帮助和规定
    def rule(self, event):
        url = "http://hupai.pro/rules"
        OpenwebThread(url)

    def help(self, event):
        url = "http://hupai.pro/coursestudy"
        OpenwebThread(url)
        # 验证码练习

    def Yan_practice(self, event):
        pass

    def Yan_test(self, event):
        pass
        # 时间调整

    def Time_adjust(self, event):
        pass

    # ------------------------------------------------------------------
    # 设置区域
    def Advanceset(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)

    def Posautoset(self, event):
        findpos()

    def Timeautoset(self, event):
        pass

    # ------------------------------------------------------------------
    # 核心功能区
    ####截屏取价 暂时放在一起
    def Lowest_price(self, event):  #
        global lowest_price, findpos_on, changetime
        try:
            price = int(TopFrame.Price_read())  # 获取当前最低价
            # 处理价格
            if price in pricelist:  # 字典查找
                findpos_on = False
                if lowest_price == price:
                    pass
                else:
                    lowest_price = price
                    # print(price,"fdsf")
                    if moni_on:
                        changetime = moni_second
                    else:
                        changetime = a_time
            else:
                # print("重新查找")
                findpos_on = True
        except:
            findpos_on = True

    # 原来方法识别
    # def Lowest_price(self, event):  #
    #     global lowest_price,findpos_on
    #     if not findpos_on:
    #         price_hash = TopFrame.Price_hash()  # 获取当前最低价hash
    #         # 处理价格
    #         if price_hash in dick_hash:  # 字典查找
    #             lowest_price = dick_hash[price_hash]
    #         else:
    #             findpos_on=True
    # findposThread()

    # logging.info("NONEHASH")
    # 处理确认
    # 自动定位
    def Find_pos(self, event):
        global findpos_on
        if findpos_on:
            try:
                findpos()
            except:
                logging.error("Find_pos error")
                print("Find_pos error")

    # 方便测试 时间调整为11点29分
    def Time_autoajust(self, event):
        timeset(guopai_on,moni_on,imgpos_currenttime,moni_second,a_time,'maindata.xml')   #调用时间同步



    def MainControl(self, event):
        #####
        if not web_on and time_on:  # 网页关就把时间关掉
            self.operationframe.strategy_tab.Closetime()

        # if web_on:
        #     try:
        #         self.operationframe.Show(True)
        #     except:
        #         pass
        # else:
        #     try:
        #         self.operationframe.Show(False)
        #     except:
        #         pass

        # 显示与隐藏主面板
        # if web_on:
        #     self.Show(False)
        # else:
        #     self.Show(True)

        ##############表示成功输入验证码

    @staticmethod
    def tijiao_ok():
        global tijiao_OK, refresh_need, tijiao_on, yanzhengma_close, yanzhengma_view
        if e_on and tijiao_on:
            print("tijiao_ok")
            tijiao_OK = True
            # refreshthread.pause()
            yanzhengma_view = False
            yanzhengma_close = True

    @staticmethod
    def tijiao_ok2():
        global tijiao_OK, refresh_need, yanzhengma_close, yanzhengma_view
        if enter_on and tijiao_on:
            tijiao_OK = True
            # refreshthread.pause()
        if enter_on:
            yanzhengma_close = True
            yanzhengma_view = False
            # refresh_need = False  # 关闭刷新识别

    @classmethod
    def query(cls):
        global query_interval, query_on
        if not query_interval and not query_on:
            # print("执行")
            query_on = True
            query_interval = True
            setText(str(1000000))  # 出一定超出的价格
            TopFrame.selfdelete()
            Click(Position[1][0], Position[1][1])

            timer1 = threading.Timer(3, cls.query_sleep3)
            timer1.start()
            timer2 = threading.Timer(5, cls.query_sleep5)
            timer2.start()
        elif query_interval and query_on:
            # print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False

    @staticmethod
    def query_sleep3():
        # print("触发3+")
        global query_interval, query_on
        if query_on:
            # print(Position[7][0], Position[7][1])
            Click(Position[7][0], Position[7][1])
            query_on = False

    @staticmethod
    def query_sleep5():
        # print("触发5")
        global query_interval
        query_interval = False

        # 改键控制


    # ------------------------------------------------------------------
    # 辅助功能区
    ####设置背景图片
    def OnEraseBackground(self, evt):
        """
        设置背景的方法
        """
        dc = evt.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("blue.jpg")
        dc.DrawBitmap(bmp, 0, 0)

        ##定位
        # 1: handle_Jiajia,
        # 2: handle_Chujia,
        # 3: handle_Tijiao,
        # 4: handle_Shuaxin,
        # 5: handle_Confirm,

    ##########主程序关闭选项#############
    def OnClose(self, event):
        ret = wx.MessageBox('真的要退出助手吗?', '确认', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            # do something here...
            import sys
            # command = 'taskkill /F /IM assistant_rev3.exe'        #修改
            # # 比如这里关闭QQ进程
            # os.system(command)
            # os._exit()
            self.Show(False)

            try:
                self.Close_time1(event)  # 关闭可能未关闭的窗口
                self.Close_time2(event)
            except:
                pass

            # Logout(Username,Password)  # 登出
            wx.GetApp().ExitMainLoop()
            event.Skip()
            sys.exit(None)

    # ------------------------------------------------------------------
    # 放弃的功能
    ######## 开启辅助
    def OnOpenAssist(self):
        self.Open()
        global do
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        self.Listen()

    # 关闭辅助
    @classmethod
    def OnCloseAssist(cls):
        cls.Close()
        # global do
        # if not do:
        #     wx.MessageBox('关闭成功', '关闭辅助', wx.OK | wx.ICON_INFORMATION)
        # else:
        #     wx.MessageBox('关闭失败', '关闭辅助', wx.OK | wx.ICON_ERROR)