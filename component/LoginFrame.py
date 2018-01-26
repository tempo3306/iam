# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 16:30
'''
import wx.lib.agw.hyperlink as hyperlink
from wx.lib.pubsub import pub
import wx
from component.app_thread import HashThread,LoginThread
from component.variable import get_val,set_val
from component.TopFrame import TopFrame
import sys,pickle
mainicon = get_val('mainicon')


class LoginFrame(wx.Frame):
    def __init__(self, name, user, psd):  ##########版本号
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(300, 220))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # self.panel.SetBackgroundColour((0,188, 255))
        # self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        # # 设置字体
        # font_button = wx.Font(10, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        # font2 = wx.Font(15, wx.SCRIPT, wx.NORMAL, wx.NORMAL)
        # font3 = wx.Font(25, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
        # font_userlabel = wx.Font(15, wx.TELETYPE, wx.NORMAL, wx.NORMAL)

        # 主sizer
        self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        self.welcomelabel = wx.StaticText(self.panel, -1, label="请输入用户名和密码", style=wx.ALIGN_CENTER)
        self.sizer_v1.Add(self.welcomelabel, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # self.btnSizer = wx.StdDialogButtonSizer()
        self.userbox = wx.BoxSizer(wx.HORIZONTAL)
        self.userlabel = wx.StaticText(self.panel, -1, label="账号")
        self.userText = wx.TextCtrl(self.panel, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        self.userbox.Add(self.userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.userbox.Add(self.userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self.passbox = wx.BoxSizer(wx.HORIZONTAL)
        self.passlabel = wx.StaticText(self.panel, -1, label="密码")
        self.passText = wx.TextCtrl(self.panel, -1, size=(150, -1),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
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

        self.monibtn = wx.Button(self.panel, -1, label="模拟", size=(90, 30))
        self.loginbtn = wx.Button(self.panel, -1, label="登录", size=(90, 30))
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnSizer.Add(self.monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.btnSizer.Add(self.loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.sizer_v1.Add(self.btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin, self.loginbtn)

        self.purchaselink = hyperlink.HyperLinkCtrl(self.panel, -1, u"购买账号")
        self.purchaselink.UnsetToolTip()
        self.purchaselink.Bind(hyperlink.EVT_HYPERLINK_LEFT, self.Purchase)
        self.purchaselink.AutoBrowse(False)
        self.purchaselink.EnableRollover(True)
        self.purchaselink.SetUnderlines(False, False, True)
        self.purchaselink.OpenInSameWindow(True)
        self.purchaselink.UpdateLink()

        self.helplink = hyperlink.HyperLinkCtrl(self.panel, -1, u"查看帮助")
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
        self.sizer_v1.Add(self.linkbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)

        self.SetSizer(self.sizer_v1)
        self.Center()  # 初始化居中

        pub.subscribe(self.connect_success, "connect")
        # pub.subscribe(self.connect_failure, "connect failure")

        self.hashthread = HashThread()

    def connect_success(self):
        self.loginbtn.Enable()
        login_result = get_val('login_result')
        url2 = get_val('url2')
        url3 = get_val('url3')
        version = get_val('version')
        Username = get_val('Username')
        if login_result['result'] == 'login success':
            self.Destroy()
            self.topframe = TopFrame('小鲜肉拍牌', version)
            self.topframe.Show(True)
            print(login_result)
            ##这里作为测试用
            if Username == 'helong' or Username == 'yuanjunkai' or Username == 'zs':
                set_val('url2' , 'http://moni.51hupai.org/')
            else:
                set_val('url2', login_result['url_dianxin'])
                url2 = login_result['url_dianxin']
            set_val('url3', login_result['url_nodianxin'])
            # event.Skip()
        elif login_result['result'] == 'net error':
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'repeat':
            wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'wrong account':
            wx.MessageBox('账号错误', '用户登录', wx.OK | wx.ICON_ERROR)
        elif login_result['result'] == 'wrong password':
            wx.MessageBox('密码错误', '用户登录', wx.OK | wx.ICON_ERROR)
        else:
            wx.MessageBox('登录失败', '用户登录', wx.OK | wx.ICON_ERROR)

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("blue.jpg")
        dc.DrawBitmap(bmp, 0, 0)

    def OnClose(self, event):
        event.Skip()
        sys.exit(None)

    # def connect_failure(self):
    #     self.loginBtn.Enable()
    #     # self.loginthread.terminate()
    #     wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)

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
            set_val('Username',username) # 保存用户输入的账号密码
            set_val('Password',password)
            self.loginthread = LoginThread()
            namepsd = [username, password]
            with open('your.name', 'wb') as userfile:
                pickle.dump(namepsd, userfile)
            # self.loginBtn.setlabel(u"登录中")
            event.GetEventObject().Disable()

    def Purchase(self, event):
        print("购买")
