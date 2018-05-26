'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 14:37
'''
import wx.html2
from component.staticmethod import *
from component.imgcut import findpos, timeset, Price_read
from component.webframe import WebFrame
from component.Pinger import pingerThread
from component.app_thread import *
from component.login import Keeplogin

class TopFrame(wx.Frame):
    def __init__(self, name, rev):  ##########版本号
        wx.Frame.__init__(self, None, -1, name,
                          size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        id = self.GetId()
        print('id', id)
        set_val('topframe', id)
        ## 初始化居中
        self.Center()
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        ##状态栏
        self.create_statusbar(rev)
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

        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MainControl, self.timer2)  # 绑定一个定时器事件，主判断
        self.timer2.Start(200)  # 设定时间间隔
        # self.timer3 = wx.Timer(self)
        # self.Bind(wx.EVT_TIMER, self.Lowest_price, self.timer3)  # 设置一个截屏取价  和查看时间
        # self.timer3.Start(60)

        ## 链接到子frame
        pub.subscribe(self.Close, "close topframe")  #
        pub.subscribe(self.Open_call_guopai, "open dianxin")  # 打开电信
        pub.subscribe(self.Open_call_moni, "open moni")  # 打开模拟
        pub.subscribe(self.Chujia, "moni chujia")
        pub.subscribe(self.Smartchujia, "moni smartchujia")

        ##多线程
        self.create_thread()

        ##keep login timer事件
        self.keeptimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.keeplogin, self.keeptimer)
        self.keeptimer.Start(300000)



    def create_statusbar(self, rev):
        mainicon = get_val('mainicon')
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.statusbar.SetStatusText(u"版本号", 0)
        self.statusbar.SetStatusText(u"%s" % rev, 1)
        self.statusbar.SetStatusText(u"软件作者：ZS ", 2)

    def create_thread(self):
        # self.confirmthread = confirmThread()  # 确认线程
        # self.refreshthread = refreshThread()  # 刷新线程
        # self.lowestThread = LowestpfriceThread()  # 价格识别
        self.finposthread = findposThread()  # 定位线程
        self.cutimgthread = cutimgThread()  # 截图线程
        self.tijiaoThread = TijiaoThread()  # 提交
        # 创建网速测试线程  通过这个线程控制启动或关闭
        self.pinger = pingerThread()
        self.timethread = TimeThread()  # 创建时间进程


    def Chujia(self):
        lowest_price = get_val('lowest_price')
        tijiao_num = get_val('tijiao_num')
        one_diff = get_val('one_diff')
        second_diff = get_val('second_diff')
        twice = get_val('twice')
        if tijiao_num == 1:
            print("moni_chujia")
            own_price1 = lowest_price + one_diff
            self.moni_chujia(own_price1)
            set_val('current_pricestatus_label', '等待第二次提交')
            one_time2 = get_val('one_time2')
            one_advance = get_val('one_advance')
            current_pricestatus = '{0}秒提前{1}'.format(one_time2, one_advance)
            set_val('current_pricestatus', current_pricestatus)
            ##5秒后调用取消出价
            timer = threading.Timer(5.1, Cancel_chujia)
            timer.start()
        elif tijiao_num == 2 and twice:
            own_price2 = lowest_price + second_diff
            set_val('own_price2', own_price2)
            self.moni_chujia(own_price2)
            set_val('current_pricestatus_label', '等待第三次提交')
            second_time2 = get_val('second_time2')
            second_advance = get_val('second_advance')
            current_pricestatus = '{0}秒提前{1}'.format(second_time2, second_advance)
            set_val('current_pricestatus', current_pricestatus)
        set_val('tijiao_on', True)
        set_val('chujia_on', False)
        set_val('chujia_interval', False)  # 间隔结束


    def Smartchujia(self, price):
        self.moni_chujia(price)
        set_val('current_pricestatus_label', '等待智能提交')
        current_pricestatus = '智能补枪'
        set_val('current_pricestatus', current_pricestatus)

    def moni_chujia(self, price):
        Position_frame = get_val('Position_frame')
        id = get_val('moni_webframe')
        moni = wx.FindWindowById(id)
        browser = moni.htmlpanel.webview
        script = "$('#selfwrite').val('{0}')".format(price)
        browser.RunScript(script)
        Click(Position_frame[1][0], Position_frame[1][1])
        Click(Position_frame[5][0], Position_frame[5][1])
        ##提交关闭
        set_val('tijiao_OK', False)
        set_val('yanzhengma_count', 0)  # 计数器，制造延迟
        set_val('yanzhengma_view', True)  # 打开验证码放大器
        set_val('refresh_need', True)  # 激活刷新验证码

    def webopen(self):
        self.Show(False)

    def Openmoni(self, event):
        timer0 = threading.Timer(5, findpos)
        Px = get_val('Px')
        Py = get_val('Py')

        set_val('moni_on', True)  # 模拟打开
        set_val('ad_view', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('guopai_on', False)
        moni_id = get_val('moni_webframe')
        moni = wx.FindWindowById(moni_id)
        if moni_id != -1:
            moni.Show(True)
            moni.currentstatusframe.Show(False)
            moni.htmlpanel.webview.Reload()
            moni.Move((Px, Py))
            moni.operationpanel.init_ui()
            moni.Show(True)
            self.webopen()
        else:
            self.fr = WebFrame( Px, Py, -1, '沪牌一号 模拟', '切换国拍', True)  ##模拟  id  51
            set_val('moni_webframe', self.fr.GetId())
            self.fr.Show(True)
            self.fr.currentstatusframe.Show(False)
            self.fr.operationpanel.init_ui()
            self.webopen()
            # 关闭主界面，打开策略设置


    def Open_call_moni(self):
        htmlsize = get_val('htmlsize')
        webview_pos = get_val('webview_pos')
        timer0 = threading.Timer(5, findpos)
        Px = get_val('Px')
        Py = get_val('Py')

        set_val('moni_on', True)  # 模拟打开
        set_val('ad_view', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('guopai_on', False)
        moni_id = get_val('moni_webframe')
        moni = wx.FindWindowById(moni_id)
        if moni_id != -1:
            moni.htmlpanel.webview.Reload()
            moni.operationpanel.init_ui()
            self.webopen()
            moni.Move((Px, Py))
            moni.Show(True)
            moni.currentstatusframe.Show(False)
        else:
            self.fr = WebFrame(Px, Py, -1, '沪牌一号模拟', '切换国拍', True)  ##模拟  id  51
            self.fr.Show(True)
            set_val('moni_webframe', self.fr.GetId())
            self.fr.currentstatusframe.Show(False)
            self.fr.operationpanel.init_ui()
            # 关闭主界面，打开策略设置
            self.webopen()

    def Openurlchoice(self, event):
        htmlsize = get_val('htmlsize')
        timer0 = threading.Timer(5, findpos)
        webview_pos = get_val('webview_pos')

        Px = get_val('Px')
        Py = get_val('Py')

        set_val('ad_view', True)
        set_val('guopai_on', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('moni_on', False)
        guopai_id = get_val('guopai_webframe')
        guopai= wx.FindWindowById(guopai_id)
        if guopai_id != -1:
            guopai.operationpanel.init_ui()
            guopai.Center()
            guopai.htmlpanel.webview.Reload()
            guopai.Show(True)
            guopai.currentstatusframe.Show(False)
            self.webopen()
        else:
            self.fr = WebFrame(Px, Py, -1, '沪牌一号 国拍', '切换模拟', False)  ## 国拍52
            set_val('guopai_webframe', self.fr.GetId())
            self.fr.Show(True)
            self.fr.currentstatusframe.Show(False)
            self.fr.operationpanel.init_ui()
            # 关闭主界面，打开策略设置
            self.webopen()

        # mainicon = get_val('mainicon')
        # self.Show(False)
        # guopai = GuopaiFrame(self, "国拍", mainicon)

    def Open_call_guopai(self):
        htmlsize = get_val('htmlsize')
        timer0 = threading.Timer(5, findpos)
        webview_pos = get_val('webview_pos')

        Px = get_val('Px')
        Py = get_val('Py')
        set_val('ad_view', True)
        set_val('guopai_on', True)
        set_val('web_on', True)
        set_val('strategy_on', True)
        set_val('moni_on', False)
        guopai_id = get_val('guopai_webframe')
        guopai= wx.FindWindowById(guopai_id)
        if guopai_id != -1:
            guopai.operationpanel.init_ui()
            guopai.htmlpanel.webview.Reload()
            guopai.Show(True)
            guopai.currentstatusframe.Show(False)
            self.webopen()
        else:
            self.fr = WebFrame(Px, Py, -1, '沪牌一号 国拍', '切换模拟', False)  ## 国拍52
            set_val('guopai_webframe', self.fr.GetId())
            self.fr.Show(True)
            self.fr.currentstatusframe.Show(False)
            self.fr.operationpanel.init_ui()
            # 关闭主界面，打开策略设置
            self.webopen()

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
        hotkey_on = get_val('hotkey_on')
        if not web_on and hotkey_on:
            Hotkey_close()  #关闭热键
            set_val('hotkey_on', False)

    def keeplogin(self, event):
        result = Keeplogin()
        print(result)

        res = result['result']
        if res == 'keep failure':  ##在其它电脑上登录过，并且未注销
            set_val('userconfirm_on', True)
            self.Close()
            from component.LoginFrame import LoginFrame
            import pickle
            try:
                with open("your.name", 'rb') as name:
                    namepsd = pickle.load(name)
                    code = namepsd[0]
                    # user = namepsd[0]
                    # psd = namepsd[1]
            except:
                user = 'shooter'  # 关闭
                psd = 0
                code = ''
            loginframe = LoginFrame('小鲜肉拍牌', code)
            loginframe.Show(True)

            moni_id = get_val('moni_webframe')
            guopai_id = get_val('guopai_webframe')
            moni = wx.FindWindowById(moni_id)
            guopai = wx.FindWindowById(guopai_id)
            try:
                moni.Show(False)
            except:
                pass
            try:
                guopai.Show(False)
            except:
                pass
        else:
            pass

        try:
            res = result['result']
            if res == 'keep failure':  ##在其它电脑上登录过，并且未注销
                self.Destroy()
                from component.LoginFrame import LoginFrame
                login = LoginFrame()
            else:
                pass
        except:
            pass


    def OnClose(self, event):
        confirm_on = get_val('userconfirm_on')
        if confirm_on:
            event.Skip()
        else:
            ret = wx.MessageBox('真的要退出助手吗?', '确认', wx.OK | wx.CANCEL)
            if ret == wx.OK:
                try:
                    # self.confirmthread.stop()
                    # self.refreshthread.stop()
                    self.finposthread.stop()
                    self.cutimgthread.stop()
                    self.tijiaoThread.stop()
                    # self.lowestThread.stop()
                    self.pinger.stop()
                    Hotkey_close()  ##关闭热键
                except:
                    pass

                self.Show(False)
                event.Skip()
                import sys
                from component.login import Logout
                Logout()
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
