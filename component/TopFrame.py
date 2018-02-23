'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 14:37
'''
import wx
import time
from wx.lib.pubsub import pub
from component.variable import set_val, get_val
from component.OperationFrame import OperationFrame
from component.timeFrame import TimeFrame, MoniTimeFrame
from component.app_thread import TimeThread, MoniTijiaoThread, TijiaoThread, OpenwebThread
from component.staticmethod import *
from component.imgcut import findpos, timeset, Price_read
from component.WebFrame import WebFrame
from component.GuopaiFrame import GuopaiFrame




class TopFrame(wx.Frame):
    def __init__(self, name, rev):  ##########版本号
        Px = get_val('Px')
        Py = get_val('Py')
        mainicon = get_val('mainicon')
        wx.Frame.__init__(self, None, 1, name,
                          size=(280, 300), pos=(Px - 120, Py), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.statusbar.SetStatusText(u"版本号", 0)
        self.statusbar.SetStatusText(u"%s" % rev, 1)
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        self.statusbar.SetBackgroundColour((240, 255, 255))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour((240, 255, 255))
        self.SetBackgroundColour((240, 255, 255))
        self.operationarea = wx.StaticBox(panel, label="基本功能")
        self.operationareasizer = wx.StaticBoxSizer(self.operationarea, wx.VERTICAL)
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.monibutton = wx.Button(panel, label='打开模拟')
        self.Bind(wx.EVT_BUTTON, self.Openmoni, self.monibutton)
        self.guopaibutton = wx.Button(panel, label='打开国拍')
        self.Bind(wx.EVT_BUTTON, self.Openurlchoice, self.guopaibutton)
        self.hbox1.Add(self.monibutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox1.Add(self.guopaibutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox1)
        self.helpbutton = wx.Button(panel, label='查看帮助')
        self.Bind(wx.EVT_BUTTON, self.help, self.helpbutton)
        self.rulebutton = wx.Button(panel, label='查看规定')
        self.Bind(wx.EVT_BUTTON, self.rule, self.rulebutton)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2.Add(self.helpbutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox2.Add(self.rulebutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox2)
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
        self.thread = TimeThread()  # 创建时间进程
        self.operationframe = OperationFrame(Px, Py, mainicon)
        self.operationframe.Show(False)  # 初始关闭
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)  # 绑定一个定时器事件，主判断
        self.timer2.Start(100)  # 设定时间间隔
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)  # 设置一个截屏取价  和查看时间
        self.timer3.Start(50)
        self.Bind(wx.EVT_BUTTON, self.Time_autoajust, self.timeautoreset)  # 设置一个截屏取价
        pub.subscribe(self.OpenGuopai_dianxin, "open dianxin")  # 打开电信
        pub.subscribe(self.OpenGuopai_nodianxin, "open nodianxin")  # 打开非电信
        pub.subscribe(self.OpenGuopai_userweb, "open userweb")  # 使用用户自己的IE
        pub.subscribe(self.Close, "close topframe")  #

    def Openmoni(self, event):
        tijiao_num = get_val('tijiao_num')
        chujia_on = get_val('chujia_on')
        tijiao_on = get_val('tijiao_on')
        strategy_on = get_val('strategy_on')
        tijiao_OK = get_val('tijiao_OK')
        twice = get_val('twice')
        time_on = get_val('time_on')
        websize = get_val('websize')
        webview_pos = get_val('webview_pos')
        timer0 = threading.Timer(5, findpos)
        set_val('strategy_on', True)
        set_val('twice', False)
        set_val('chujia_on', True)
        set_val('tijiao_on', False)
        set_val('tijiao_num', 1)  # 初始化
        set_val('tijiao_OK', False)
        Px = get_val('Px')
        Py = get_val('Py')
        url1 = get_val('url1')
        ad_view = get_val('ad_view')
        web_on = get_val('web_on')
        guopai_on = get_val('guopai_on')
        moni_on = get_val('moni_on')
        strategy_repeat = get_val('strategy_repeat')
        if guopai_on:
            wx.MessageBox('请关闭国拍页面或先关闭辅助', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        elif moni_on:
            wx.MessageBox('请关闭模拟页面', '开启模拟失败', wx.OK | wx.ICON_ERROR)
        else:
            Open()
            do = get_val('do')
            if do:
                set_val('moni_on', True)  # 模拟打开
                set_val('ad_view', True)
                set_val('web_on', True)
                set_val('strategy_on',True)
                self.fr = WebFrame(Px, Py, False, '小鲜肉模拟', (websize[0], websize[1]))

                # if not strategy_repeat:  # 判断自动出价进程是否开启
                #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                #     set_val('strategy_repeat', True)
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url1)
                browser.CanSetZoomType(False)
                self.fr.Show()
                Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()
            # listenthread = listenThread()

    def Openurlchoice(self, event):
        mainicon = get_val('mainicon')
        guopai = GuopaiFrame("国拍", mainicon)

    def OpenGuopai_dianxin(self):
        time_on = get_val('time_on')
        websize = get_val('websize')
        tijiao_num = get_val('tijiao_num')
        chujia_on = get_val('chujia_on')
        tijiao_on = get_val('tijiao_on')
        strategy_on = get_val('strategy_on')
        tijiao_OK = get_val('tijiao_OK')
        twice = get_val('twice')
        timer0 = threading.Timer(5, findpos)
        webview_pos = get_val('webview_pos')
        set_val('strategy_on', True)
        set_val('twice', False)
        set_val('chujia_on', True)
        set_val('tijiao_on', False)
        set_val('tijiao_num', 1)  # 初始化
        set_val('tijiao_OK', False)
        Px = get_val('Px')
        Py = get_val('Py')
        url2 = get_val('url2')
        ad_view = get_val('ad_view')
        web_on = get_val('web_on')
        do = get_val('do')
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
        strategy_repeat = get_val('strategy_repeat')

        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            Open()
            do = get_val('do')
            if do:
                set_val('ad_view', True)
                set_val('guopai_on', True)
                self.fr = WebFrame(Px, Py, False, '沪牌一号 国拍', (websize[0], websize[1]))  # 暂时关闭广告

                # if not strategy_repeat:  # 判断自动出价进程是否开启
                #     set_val('strategy_repeat', True)
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url2)
                browser.CanSetZoomType(False)
                self.fr.Show()
                Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()  # 关闭可能注册的热键

    def OpenGuopai_nodianxin(self):
        time_on = get_val('time_on')
        websize = get_val('websize')
        tijiao_num = get_val('tijiao_num')
        chujia_on = get_val('chujia_on')
        tijiao_on = get_val('tijiao_on')
        strategy_on = get_val('strategy_on')
        tijiao_OK = get_val('tijiao_OK')
        twice = get_val('twice')
        timer0 = threading.Timer(5, findpos)
        set_val('strategy_on', True)
        set_val('twice', False)  # 初始化双枪不触发
        set_val('chujia_on', True)
        set_val('tijiao_on', False)
        set_val('tijiao_num', 1)  # 初始化
        set_val('tijiao_OK', False)
        webview_pos = get_val('webview_pos')
        Px = get_val('Px')
        Py = get_val('Py')
        url3 = get_val('url3')
        ad_view = get_val('ad_view')
        web_on = get_val('web_on')
        do = get_val('do')
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
        strategy_repeat = get_val('strategy_repeat')
        if moni_on:
            wx.MessageBox('请关闭模拟页面', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        elif guopai_on:
            wx.MessageBox('国拍已经打开', '开启国拍失败', wx.OK | wx.ICON_ERROR)
        else:
            Open()
            if do:
                set_val('ad_view', True)
                set_val('guopai_on', True)
                self.fr = WebFrame(Px, Py, False, '沪牌一号 国拍', (websize[0], websize[1]))  # 暂时关闭广告
                if time_on:
                    self.operationframe.Opentime()
                # if not strategy_repeat:  # 判断自动出价进程是否开启
                #     self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                #     self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                #     set_val('strategy_repeat', True)
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] + 48, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()  # 关闭可能注册的热键

    def OpenGuopai_userweb(self):
        time_on = get_val('time_on')
        tijiao_num = get_val('tijiao_num')
        chujia_on = get_val('chujia_on')
        tijiao_on = get_val('tijiao_on')
        strategy_on = get_val('strategy_on')
        tijiao_OK = get_val('tijiao_OK')
        twice = get_val('twice')
        timer0 = threading.Timer(5, findpos)  # 几秒之后执行一次位置刷新
        set_val('strategy_on', True)
        set_val('twice', False)
        set_val('chujia_on', True)
        set_val('tijiao_on', False)
        set_val('tijiao_num', 1)  # 初始化
        set_val('tijiao_OK', False)
        Px = get_val('Px')
        Py = get_val('Py')
        url3 = get_val('url3')
        ad_view = get_val('ad_view')
        web_on = get_val('web_on')
        do = get_val('do')
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
        strategy_repeat = get_val('strategy_repeat')
        Open()
        if do:
            set_val('ad_view', True)
            set_val('guopai_on', True)
            # if time_on:
            #     self.operationframe.Opentime()
            if not strategy_repeat:  # 判断自动出价进程是否开启
                # self.monitijiaothread = MoniTijiaoThread()  # 开启模拟自动出价
                # self.tijiaothread = TijiaoThread()  # 开启模拟自动出价
                set_val('strategy_repeat', True)
                # openIE(url3)
                Listen()
        else:
            wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
            Close()  # 关闭可能注册的热键

    def UrlGuopai(self, event):
        url2 = get_val('url2')
        try:
            set_val('url2', self.urlText.GetValue())
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
        aboutInfo.AddDeveloper("ZS")
        wx.adv.AboutBox(aboutInfo)

    def rule(self, event):
        url = "http://hupai.pro/rules"
        OpenwebThread(url)

    def help(self, event):
        url = "http://hupai.pro/coursestudy"
        OpenwebThread(url)

    def Yan_practice(self, event):
        pass

    def Yan_test(self, event):
        pass

    def Time_adjust(self, event):
        pass

    def Advanceset(self, event):
        setting = self.FindWindowById(2)
        setting.Show(True)

    def Posautoset(self, event):
        findpos()

    def Timeautoset(self, event):
        pass

    def Lowest_price(self, event):  #
        lowest_price = get_val('lowest_price')
        findpos_on = get_val('findpos_on')
        changetime = get_val('changetime')
        pricelist = get_val('pricelist')
        moni_second = get_val('moni_second')
        a_time = get_val('a_time')
        moni_on  = get_val('moni_on')
        try:
            price = int(Price_read())  # 获取当前最低价
            if price in pricelist:  # 字典查找
                set_val('findpos_on', False)
                if lowest_price == price:
                    pass
                else:
                    set_val('lowest_price', price)
                    if moni_on:
                        set_val('changetime', moni_second)
                    else:
                        set_val('changetime', a_time)
            else:
                set_val('findpos_on', True)
        except:
            set_val('findpos_on', True)

    def Find_pos(self, event):
        findpos_on = get_val('findpos_on')
        if findpos_on:
            try:
                findpos()
            except:
                print("Find_pos error")

    def Time_autoajust(self, event):
        guopai_on = get_val('guopai_on')
        moni_on = get_val('moni_on')
        imgpos_currenttime = get_val('imgpos_currenttime')
        timeset(guopai_on, moni_on, imgpos_currenttime, 'maindata.xml')  # 调用时间同步

    def MainControl(self, event):
        web_on = get_val('web_on')
        time_on = get_val('time_on')
        if not web_on and time_on:  # 网页关就把时间关掉
            self.operationframe.strategy_tab.Closetime()

    def OnClose(self, event):
        ret = wx.MessageBox('真的要退出助手吗?', '确认', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            import sys
            self.Show(False)

            wx.GetApp().ExitMainLoop()
            event.Skip()
            sys.exit(None)

    def OnOpenAssist(self):
        Open()
        do = get_val('do')
        if do:
            wx.MessageBox('启用成功', '开启辅助', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('启用失败', '开启辅助', wx.OK | wx.ICON_ERROR)
        Listen()
