'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 14:37
'''
import wx
import wx.html2
from wx.lib.pubsub import pub
from component.OperationFrame import OperationPanel
from component.app_thread import TimeThread, OpenwebThread
from component.staticmethod import *
from component.imgcut import findpos, timeset, Price_read
from component.webframe import WebFrame, MoniWebFrame
from component.Pinger import pingerThread
from component.Guopaiframe import GuopaiFrame
from component.app_thread import *


class TopFrame(wx.Frame):
    def __init__(self, name, rev):  ##########版本号
        Px = get_val('Px')
        Py = get_val('Py')
        mainicon = get_val('mainicon')
        wx.Frame.__init__(self, None, 1, name,
                          size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)

        # 初始化居中
        self.Center()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.statusbar.SetStatusText(u"版本号", 0)
        self.statusbar.SetStatusText(u"%s" % rev, 1)
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)
        # self.statusbar.SetBackgroundColour((240, 255, 255))
        panel = wx.Panel(self, -1)
        # panel.SetBackgroundColour((240, 255, 255))
        # self.SetBackgroundColour((240, 255, 255))
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

        self.yanzhengmabutton = wx.Button(panel, label='验证码练习')
        self.Bind(wx.EVT_BUTTON, self.yanzhengma, self.yanzhengmabutton)
        self.contactusbutton = wx.Button(panel, label='联系我们')
        self.Bind(wx.EVT_BUTTON, self.contactus, self.contactusbutton)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox3.Add(self.yanzhengmabutton, 0, wx.ALL | wx.CENTER, 5)
        self.hbox3.Add(self.contactusbutton, 0, wx.ALL | wx.CENTER, 5)
        self.operationareasizer.Add(self.hbox3)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.operationareasizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(self.vbox)
        self.thread = TimeThread()  # 创建时间进程

        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)  # 绑定一个定时器事件，主判断
        self.timer2.Start(100)  # 设定时间间隔
        # self.timer3 = wx.Timer(self)
        # self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)  # 设置一个截屏取价  和查看时间
        # self.timer3.Start(60)

        ## 链接到子frame
        pub.subscribe(self.Open_call_guopai, "open dianxin")  # 打开电信
        pub.subscribe(self.Open_call_moni, "open moni")  # 打开模拟


        pub.subscribe(self.OpenGuopai_nodianxin, "open nodianxin")  # 打开非电信
        pub.subscribe(self.Close, "close topframe")  #
        pub.subscribe(self.moni_chujia, "moni chujia")
        # 创建网速测试线程  通过这个线程控制启动或关闭
        self.pinger = pingerThread()

        ## browser
        self.browser_guopai = wx.html2.WebView.New()
        self.browser_moni = wx.html2.WebView.New()

        ###多线程
        self.confirmthread = confirmThread()  # 确认线程
        self.refreshthread = refreshThread()  # 刷新线程

        self.finposthread = findposThread()  # 定位线程
        self.cutimgthread = cutimgThread()  # 截图线程
        self.tijiaoThread = TijiaoThread()  # 提交
        self.lowestThread = LowestpfriceThread()  # 价格识别

    def moni_chujia(self):
        lowest_price = get_val('lowest_price')
        Position = get_val('Position')
        tijiao_num = get_val('tijiao_num')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        twice = get_val('twice')

        if tijiao_num == 1:
            own_price1 = lowest_price + one_diff
            set_val('own_price1', own_price1)
            moni_on = get_val('moni_on')

            script = "$('#selfwrite').val('{0}')".format(own_price1)
            self.browser.RunScript(script)

            Click(Position[1][0], Position[1][1])
            Click(Position[5][0], Position[5][1])
            set_val('tijiao_on', True)
            set_val('chujia_on', False)
            set_val('chujia_interval', False)  # 间隔结束
            ##提交关闭
            set_val('tijiao_OK', False)
            ##5秒后调用取消出价
            timer = threading.Timer(6, Cancel_chujia)
            timer.start()

        elif tijiao_num == 2 and twice:
            own_price2 = lowest_price + second_diff
            set_val('own_price2', own_price2)
            moni_on = get_val('moni_on')

            script = "$('#selfwrite').val('{0}')".format(own_price2)
            self.browser.RunScript(script)

            Click(Position[1][0], Position[1][1])
            Click(Position[5][0], Position[5][1])
            set_val('tijiao_on', True)
            set_val('chujia_on', False)
            set_val('chujia_interval', False)  # 间隔结束
            ##提交关闭
            set_val('tijiao_OK', False)

        set_val('yanzhengma_count', 0)  # 计数器，制造延迟
        set_val('yanzhengma_view', True)  # 打开验证码放大器
        set_val('tijiao_on', True)  # 激活自动出价
        set_val('refresh_need', True)  # 激活刷新验证码

    def webopen(self):
        self.Show(False)

    def Openmoni(self, event):
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
        guopai_on = get_val('guopai_on')
        moni_on = get_val('moni_on')
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
                set_val('strategy_on', True)
                set_val('current_moni', True)
                moni = wx.FindWindowByName('沪牌一号模拟')
                if moni:
                    moni.Show(True)
                    self.browser_moni.Reload()
                    self.webopen()
                    Listen()
                else:
                    self.fr = MoniWebFrame(Px, Py, 51, '沪牌一号模拟', '切换国拍')  ##模拟  id  51

                    self.browser_moni = wx.html2.WebView.New(self.fr, size=(websize[0] - 10, websize[1] + 40), pos=webview_pos,
                                                        style=wx.BORDER_NONE)
                    self.browser_moni.LoadURL(url1)
                    self.browser_moni.CanSetZoomType(False)
                    self.fr.Show()
                    # 关闭主界面，打开策略设置
                    self.webopen()
                Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()

    def Open_call_moni(self):
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


        set_val('moni_on', True)  # 模拟打开
        set_val('ad_view', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('current_moni', True)
        moni = wx.FindWindowByName('沪牌一号模拟')
        if moni:
            moni.Show(True)
            self.browser_moni.Reload()
            self.webopen()
            Listen()
        else:
            self.fr = MoniWebFrame(Px, Py, 51, '沪牌一号模拟', '切换国拍')  ##模拟  id  51

            self.browser_moni = wx.html2.WebView.New(self.fr, size=(websize[0] - 10, websize[1] + 40), pos=webview_pos,
                                                style=wx.BORDER_NONE)
            self.browser_moni.LoadURL(url1)
            self.browser_moni.CanSetZoomType(False)
            self.fr.Show()
            # 关闭主界面，打开策略设置
            self.webopen()





    def Openurlchoice(self, event):
        websize = get_val('websize')
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
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
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
                set_val('web_on', True)
                set_val('strategy_on', True)
                set_val('current_moni', False)
                guopai = wx.FindWindowByName('沪牌一号 国拍')
                if guopai:
                    guopai.Show(True)
                    self.browser_guopai.Reload()
                    self.webopen()
                    Listen()
                else:
                    self.fr = WebFrame(Px, Py, 52, '沪牌一号 国拍', '切换模拟')  ## 国拍52
                    wx.CallAfter(pub.sendMessage, "close guopaiframe")

                    self.browser_guopai = wx.html2.WebView.New(self.fr, size=(websize[0] - 10, websize[1] + 40), pos=webview_pos,
                                                   style=wx.BORDER_NONE)
                    self.browser_guopai.LoadURL(url2)
                    self.browser_guopai.CanSetZoomType(False)
                    self.fr.Show()
                    # 关闭主界面，打开策略设置
                    self.webopen()
                    Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()  # 关闭可能注册的热键

        # mainicon = get_val('mainicon')
        # self.Show(False)
        # guopai = GuopaiFrame(self, "国拍", mainicon)

    def Open_call_guopai(self):
        websize = get_val('websize')
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
        set_val('ad_view', True)
        set_val('guopai_on', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('current_moni', False)
        guopai = wx.FindWindowByName('沪牌一号 国拍')
        if guopai:
            guopai.Show(True)
            self.browser_guopai.Reload()
            self.webopen()
            Listen()
        else:
            self.fr = WebFrame(Px, Py, 52, '沪牌一号 国拍', '切换模拟')  ## 国拍52
            wx.CallAfter(pub.sendMessage, "close guopaiframe")

            self.browser_guopai = wx.html2.WebView.New(self.fr, size=(websize[0] - 10, websize[1] + 40), pos=webview_pos,
                                           style=wx.BORDER_NONE)
            self.browser_guopai.LoadURL(url2)
            self.browser_guopai.CanSetZoomType(False)
            self.fr.Show()
            # 关闭主界面，打开策略设置
            self.webopen()


    def OpenGuopai_nodianxin(self):
        websize = get_val('websize')
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
        do = get_val('do')
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
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
                set_val('web_on', True)
                set_val('strategy_on', True)
                self.fr = WebFrame(Px, Py, 52, '沪牌一号 国拍')  ## id 52
                wx.CallAfter(pub.sendMessage, "close guopaiframe")
                browser = wx.html2.WebView.New(self.fr, size=(websize[0] - 10, websize[1] + 40), pos=webview_pos,
                                               style=wx.BORDER_NONE)
                browser.LoadURL(url3)
                browser.CanSetZoomType(False)
                self.fr.Show()
                # 关闭主界面，打开策略设置
                self.webopen()
                Listen()
            else:
                wx.MessageBox('请检查其它软件热键占用', '辅助启用失败', wx.OK | wx.ICON_ERROR)
                Close()  # 关闭可能注册的热键

    ## 验证码练习
    def yanzhengma(self, event):
        pass

    ## 联系我们
    def contactus(self, event):
        pass

    ########################
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
        pricelist = get_val('pricelist')
        moni_second = get_val('moni_second')
        a_time = get_val('a_time')
        moni_on = get_val('moni_on')
        try:
            price = Price_read()
            price = int(Price_read())  # 获取当前最低价
            if price in pricelist:  # 字典查找
                set_val('findpos_on', False)
                if lowest_price == price:
                    trans_time()  # 保存价格
                else:
                    set_val('lowest_price', price)
                    trans_time()  # 保存价格
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
            set_val('time_on', False)
            webframe = wx.FindWindowById(51)
            webframe.panel.status_tab.Closetime()
            webframe.panel.status_tab.timeview.SetValue(0)

    def OnClose(self, event):
        ret = wx.MessageBox('真的要退出助手吗?', '确认', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            self.confirmthread.stop()
            self.refreshthread.stop()
            self.finposthread.stop()
            self.cutimgthread.stop()
            self.tijiaoThread.stop()
            self.lowestThread.stop()
            event.Skip()
            import sys
            sys.exit()

        ##关闭线程
        # self.confirmthread.stop()
        # self.refreshthread.stop()
        #
        # self.finposthread.stop()
        # self.cutimgthread.stop()
        # self.tijiaoThread.stop()
        # self.lowestThread.stop()
        #
        # self.Show(False)
        # self.Destroy()
        # event.Skip()
        # wx.App().OnExit()
        # import sys
        # sys.exit()
