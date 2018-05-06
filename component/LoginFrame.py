# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 16:30
'''
import wx.lib.agw.hyperlink as hyperlink
from wx.lib.pubsub import pub
import wx
from component.app_thread import HashThread, LoginThread, Login_codeThread, Getip_dianxinThread
from component.variable import get_val, set_val, remote_variables
from component.TopFrame import TopFrame
import sys, pickle


class AccountPanel(wx.Panel):
    def __init__(self, parent, user, psd):  ##########版本号
        wx.Panel.__init__(self, parent=parent, id=30)
        # 主sizer
        self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.welcomelabel = wx.StaticText(self, -1, label="沪牌一号", style=wx.ALIGN_CENTER)
        self.sizer_v1.Add(self.welcomelabel, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        self.userbox = wx.BoxSizer(wx.HORIZONTAL)
        ##登录图标
        self.bmp_account = wx.StaticBitmap(self, -1)
        # self.bmp_account.SetBitmap(wx.Bitmap('login.png'))
        self.userlabel = wx.StaticText(self, -1, label="账号")
        self.userText = wx.TextCtrl(self, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        # self.userbox.Add(self.bmp_account)
        self.userbox.Add(self.userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.userbox.Add(self.userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self.passbox = wx.BoxSizer(wx.HORIZONTAL)
        self.bmp_password = wx.StaticBitmap(self, -1)
        # self.bmp_password.SetBitmap(wx.Bitmap('password.png'))
        self.passlabel = wx.StaticText(self, -1, label="密码")
        self.passText = wx.TextCtrl(self, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
        # self.passbox.Add(self.bmp_password, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.passbox.Add(self.passlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.passbox.Add(self.passText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
        if user:
            self.userText.SetValue(user)
        if psd:
            self.passText.SetValue(psd)
        self.sizer_v1.Add(self.userbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.sizer_v1.Add(self.passbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.userText)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.passText)

        self.monibtn = wx.Button(self, -1, label="免费模拟", size=(90, 30))
        self.loginbtn = wx.Button(self, -1, label="登录", size=(90, 30))
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.btnSizer.Add(self.loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.sizer_v1.Add(self.btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin, self.loginbtn)

        self.SetSizer(self.sizer_v1)

    def OnLogin(self, event):
        username = self.userText.GetValue()
        password = self.passText.GetValue()
        if username == "":
            wx.MessageBox('请输入用户名！')
            self.userText.SetFocus()
        elif password == "":
            wx.MessageBox('请输入密码！')
            self.passText.SetFocus()
            # loginthread=TestThread()
        else:
            set_val('Username', username)  # 保存用户输入的账号密码
            set_val('Password', password)
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            # self.loginBtn.setlabel(u"登录中")
            event.GetEventObject().Disable()


class Identify_codePanel(wx.Panel):
    def __init__(self, parent, code):  ##########版本号
        wx.Panel.__init__(self, parent, -1)
        # 主sizer
        self.code_sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.code_welcomelabel = wx.StaticText(self, -1, label="沪牌一号", style=wx.ALIGN_CENTER)
        self.code_sizer_v1.Add(self.code_welcomelabel, flag=wx.ALIGN_LEFT | wx.LEFT | wx.TOP, border=15)

        self.code_userbox = wx.BoxSizer(wx.HORIZONTAL)
        ##登录图标
        self.code_bmp_account = wx.StaticBitmap(self, -1)
        # self.bmp_account.SetBitmap(wx.Bitmap('login.png'))
        self.code_userlabel = wx.StaticText(self, -1, label="激活码")
        self.code_userText = wx.TextCtrl(self, -1, size=(139, -1),
                                         style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        # self.userbox.Add(self.bmp_account)
        self.code_userbox.Add(self.code_userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.code_userbox.Add(self.code_userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self.code_sizer_v1.Add(self.code_userbox, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.code_userText)

        self.code_monibtn = wx.Button(self, -1, label="免费模拟", size=(90, 30))
        self.code_loginbtn = wx.Button(self, -1, label="登录", size=(90, 30))
        self.code_btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.code_btnSizer.Add(self.code_monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.code_btnSizer.Add(self.code_loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.code_sizer_v1.Add(self.code_btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.code_loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin, self.code_loginbtn)
        ##初始化
        if code:
            self.code_userText.SetValue(code)
        self.purchaselink = hyperlink.HyperLinkCtrl(self, -1, u"购买激活码", URL="https://hupai.pro/purchase_software")
        self.purchaselink.UnsetToolTip()
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.Purchase)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()

        self.helplink = hyperlink.HyperLinkCtrl(self, -1, u"找回激活码", URL="https://hupai.pro/purchase_software")
        self.helplink.UnsetToolTip()
        self.helplink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.Purchase)
        self.helplink.AutoBrowse(False)
        self.helplink.EnableRollover(True)
        self.helplink.SetUnderlines(False, False, True)
        self.helplink.OpenInSameWindow(True)
        self.helplink.UpdateLink()

        self.linkbox = wx.BoxSizer(wx.HORIZONTAL)
        self.linkbox.Add(self.purchaselink, flag=wx.ALIGN_LEFT | wx.RIGHT, border=20)
        self.linkbox.Add(self.helplink, flag=wx.ALIGN_RIGHT | wx.LEFT, border=20)
        self.code_sizer_v1.Add(self.linkbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.SetSizer(self.code_sizer_v1)

    def OnLogin(self, event):
        Identify_code = self.code_userText.GetValue()
        if Identify_code == "":
            wx.MessageBox('请输入激活码！')
            self.code_userText.SetFocus()
        else:
            set_val('Identify_code', Identify_code)  # 保存用户输入的账号密码
            self.loginthread = Login_codeThread()
            namepsd = [Identify_code]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)

            # with open('your.name', 'wb') as userfile:
            #     pickle.dump(namepsd, userfile)

            # self.loginBtn.setlabel(u"登录中")
            event.GetEventObject().Disable()

    def Purchase(self, event):
        print("购买")


class LoginFrame(wx.Frame):
    def __init__(self, name, code):  ##########版本号
        mainicon = 'ico.ico'
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        id = self.GetId()
        set_val('loginframe', id)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # panel = wx.Panel(self)
        # self.notebook = wx.Notebook(panel)
        # self.code_tab = Identify_codePanel(self.notebook, user, psd)
        # self.notebook.AddPage(self.code_tab, "激活码登录")
        # self.account_tab = AccountPanel(self.notebook, user, psd)  # notebook作为父类
        # self.notebook.AddPage(self.account_tab, "账号登录")
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 5)
        # panel.SetSizer(sizer)
        self.panel = Identify_codePanel(self, code)
        self.Layout()
        # 初始化居中
        self.Center()

        pub.subscribe(self.connect_success, "connect")
        # pub.subscribe(self.connect_failure, "connect failure")

        self.hashthread = HashThread()

    def connect_success(self):
        self.panel.code_loginbtn.Enable()
        login_result = get_val('login_result')
        version = get_val('version')
        Identify_code = get_val('Identify_code')

        if login_result['result'] == 'login success':
            self.topframe = TopFrame('沪牌一号', version)
            self.topframe.Show(True)
            print(login_result)
            ip_address = login_result['ip_address']
            set_val('ip_address', ip_address)  ##设置IP
            Getip_dianxinThread(ip_address) ##判定是否电信网址的功能

            ##初始化结果
            print(login_result)
            data = login_result['data']
            remote_variables(**data)

            if Identify_code == '123456':  ##这里作为测试用
                pass
            else:
                set_val('url_dianxin', login_result['url_dianxin'])
                set_val('url_nodianxin', login_result['url_nodianxin'])
            from component.staticmethod import Hotkey_listen
            self.Destroy()  ##关闭窗口
            Hotkey_listen()

        elif login_result['result'] == 'net error' or login_result['result'] == 'timeout':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'wrong version':
            wx.MessageBox('软件版本过低', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'expired date':
            wx.MessageBox('激活码过期', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('激活码错误', '用户登录', wx.OK | wx.ICON_ERROR)

    def Purchase(self, event):
        print("购买")

    def OnClose(self, event):
        event.Skip()
        sys.exit(0)
