# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 16:30
'''
import threading

import wx.lib.agw.hyperlink as hyperlink
from wx.lib.pubsub import pub
import wx
from component.app_thread import Login_codeThread, Getip_dianxinThread, MoniThread
from component.remote_control import get_unique_id
from component.variable import get_val, set_val, remote_variables, get_id_hash, get_dick, get_strategy_dick
from component.TopFrame import TopFrame
import sys, pickle, json
from wx.lib.buttons import GenButton as wxButton
from component.variable import set_strategy_dick
import logging

from component.webframe import WebFrame

logger = logging.getLogger()


# class AccountPanel(wx.Panel):
#     def __init__(self, parent, user, psd):  ##########版本号
#         wx.Panel.__init__(self, parent=parent, id=30)
#         # 主sizer
#         self.sizer_v1 = wx.BoxSizer(wx.VERTICAL)
#         self.welcomelabel = wx.StaticText(self, -1, label="沪牌一号", style=wx.ALIGN_CENTER)
#         self.sizer_v1.Add(self.welcomelabel, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
#
#         self.userbox = wx.BoxSizer(wx.HORIZONTAL)
#         ##登录图标
#         self.bmp_account = wx.StaticBitmap(self, -1)
#         # self.bmp_account.SetBitmap(wx.Bitmap('login.png'))
#         self.userlabel = wx.StaticText(self, -1, label="账号")
#         self.userText = wx.TextCtrl(self, -1, size=(150, -1),
#                                     style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)
#         # self.userbox.Add(self.bmp_account)
#         self.userbox.Add(self.userlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#         self.userbox.Add(self.userText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
#
#         self.passbox = wx.BoxSizer(wx.HORIZONTAL)
#         self.bmp_password = wx.StaticBitmap(self, -1)
#         # self.bmp_password.SetBitmap(wx.Bitmap('password.png'))
#         self.passlabel = wx.StaticText(self, -1, label="密码")
#         self.passText = wx.TextCtrl(self, -1, size=(150, -1),
#                                     style=wx.TE_CENTER | wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
#         # self.passbox.Add(self.bmp_password, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#         self.passbox.Add(self.passlabel, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#         self.passbox.Add(self.passText, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)
#         if user:
#             self.userText.SetValue(user)
#         if psd:
#             self.passText.SetValue(psd)
#         self.sizer_v1.Add(self.userbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#         self.sizer_v1.Add(self.passbox, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#
#         self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.userText)
#         self.Bind(wx.EVT_TEXT_ENTER, self.OnLogin, self.passText)
#
#
#         self.monibtn = wx.Button(self, label="免费模拟", size=(90, 30))
#         self.monibtn.SetBackgroundColour("#ACD6FF")
#         self.loginbtn = wx.Button(self, label="登录", size=(90, 30))
#         self.loginbtn.SetBackgroundColour("#ACD6FF")
#
#         self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
#         self.btnSizer.Add(self.monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
#         self.btnSizer.Add(self.loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
#         self.sizer_v1.Add(self.btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
#
#         self.loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin, self.loginbtn)
#         self.monibtn.Bind(wx.EVT_BUTTON, self.OnMoni, self.loginbtn)
#
#
#         self.SetSizer(self.sizer_v1)
#
#     def OnLogin(self, event):
#         username = self.userText.GetValue()
#         password = self.passText.GetValue()
#         if username == "":
#             wx.MessageBox('请输入用户名！')
#             self.userText.SetFocus()
#         elif password == "":
#             wx.MessageBox('请输入密码！')
#             self.passText.SetFocus()
#             # loginthread=TestThread()
#         else:
#             set_val('Username', username)  # 保存用户输入的账号密码
#             set_val('Password', password)
#             self.loginthread = LoginThread()
#             namepsd = [username, password]
#             with open('your.name', 'wb') as userfile:
#                 pickle.dump(namepsd, userfile)
#             # self.loginBtn.setlabel(u"登录中")
#             event.GetEventObject().Disable()


class Identify_codePanel(wx.Panel):
    def __init__(self, parent, code):  ##########版本号
        wx.Panel.__init__(self, parent, -1)
        # 主sizer
        self.code_sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        ##登录图标
        self.code_bmp_account = wx.StaticBitmap(self, -1)
        self.code_bmp_account.SetBitmap(wx.Bitmap('login.png'))
        self.code_sizer_v1.Add(self.code_bmp_account, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=15)

        self.code_userbox = wx.BoxSizer(wx.HORIZONTAL)

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
        # self.code_monibtn.SetBackgroundColour('#ff6b3b')
        # self.code_loginbtn.SetBackgroundColour('#ff6b3b')

        self.code_btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.code_btnSizer.Add(self.code_monibtn, flag=wx.ALIGN_LEFT | wx.ALL, border=3)
        self.code_btnSizer.Add(self.code_loginbtn, flag=wx.ALIGN_RIGHT | wx.ALL, border=3)
        self.code_sizer_v1.Add(self.code_btnSizer, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        self.code_loginbtn.Bind(wx.EVT_BUTTON, self.OnLogin)
        self.code_monibtn.Bind(wx.EVT_BUTTON, self.OnMoni)
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
        print("登录")
        diskid = get_unique_id()
        set_val('diskid', get_id_hash(diskid))  ##sha1 hash化
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

    def OnMoni(self, event):
        print('免费模拟')
        self.loginthread = MoniThread()
        event.GetEventObject().Disable()

    def Purchase(self, event):
        print("购买")


class LoginFrame(wx.Frame):
    def __init__(self, name, code):  ##########版本号
        mainicon = 'logo.ico'
        wx.Frame.__init__(self, None, -1, name, size=(300, 240), style=wx.CAPTION | wx.CLOSE_BOX)
        id = self.GetId()
        set_val('loginframe', id)

        id = get_val('loginframe')
        print(id)
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
        pub.subscribe(self.monitest, "monitest")
        # pub.subscribe(self.connect_failure, "connect failure")

        # self.hashthread = HashThread()

    def connect_success(self):
        self.panel.code_loginbtn.Enable()
        login_result = get_val('login_result')
        version = get_val('version')
        Identify_code = get_val('Identify_code')

        if login_result['result'] == 'login success':
            set_val('activate_status', True)  ##激活成功
            set_val('register_label', '已激活')

            topframeid = get_val('topframe')
            if topframeid == -1:
                self.topframe = TopFrame('沪牌一号', version)
                self.topframe.Show(True)
            else:
                topframe = wx.FindWindowById(topframeid)
                topframe.guopaibutton.SetLabel('打开国拍')
                topframe.Show(True)

            print(login_result)
            ip_address = login_result['ip_address']
            set_val('ip_address', ip_address)  ##设置IP
            Getip_dianxinThread(ip_address) ##判定是否电信网址的功能

            ##初始化结果
            print(login_result)
            data = login_result['data']
            remote_variables(**data)
            target_time = get_val('target_time')
            start_time = target_time - 30 * 60
            set_val('start_time', start_time)
            strategy_dick =login_result['strategy_dick']

            if strategy_dick:
                try:
                    strategy_dick = json.loads(strategy_dick)
                except:
                    logger.exception("error message")
                if strategy_dick != 'none':
                    set_strategy_dick(strategy_dick) ##初始化策略数据
            if Identify_code == '12345678':  ##这里作为测试用
                set_val('test', True)

            elif Identify_code[0]== 'h':
                set_val('paishou', True)
                set_val('url_dianxin', login_result['url_dianxin'])
                set_val('url_nodianxin', login_result['url_nodianxin'])
            elif Identify_code == 'daxinwen':
                set_val('url_dianxin', "http://moni.51hupai.org/")
                set_val('url_nodianxin', "http://moni.51hupai.org/")
            else:
                set_val('url_dianxin', login_result['url_dianxin'])
                set_val('url_nodianxin', login_result['url_nodianxin'])

            ##初始化账号
            account = login_result['account']
            if account:
                bid_number = account['account']
                bid_password = account['password']
                idcard = account['idcard']
                set_val('bid_number', bid_number)
                set_val('bid_password', bid_password)
                set_val('idcard', idcard)
                bidnumber_js = "document.getElementById('bidnumber').value = '{0}';".format(bid_number)
                bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bid_password)
                idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
                set_val('bidnumber_js', bidnumber_js)
                set_val('bidpassword_js', bidpassword_js)
                set_val('idcard_js', idcard_js)

                print('bidnumber_js', bidnumber_js)

            from component.staticmethod import Hotkey_listen
            from component.variable import init_pos
            Px = get_val('Px')
            Py = get_val('Py')
            init_pos(Px, Py)
            self.Show(False)  ##关闭窗口
            listening = get_val('listening')
            if not listening:
                Hotkey_listen()
        else:
            self.panel.code_loginbtn.Enable()
            if login_result['result'] == 'net error' or login_result['result'] == 'timeout':
                wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)
            elif login_result['result'] == 'repeat':
                wx.MessageBox('重复登录，稍后再试', '用户登录', wx.OK | wx.ICON_ERROR)
            elif login_result['result'] == 'wrong version':
                wx.MessageBox('软件版本过低', '用户登录', wx.OK | wx.ICON_ERROR)
            elif login_result['result'] == 'expired date':
                wx.MessageBox('激活码过期', '用户登录', wx.OK | wx.ICON_ERROR)
            else:
                wx.MessageBox('激活码错误', '用户登录', wx.OK | wx.ICON_ERROR)

    def monitest(self):
        self.panel.code_monibtn.Enable()
        login_result = get_val('login_result')
        version = get_val('version')
        if login_result['result'] == 'moni success':
            topframeid = get_val('topframe')
            if topframeid == -1:
                self.topframe = TopFrame('沪牌一号', version)
                self.topframe.Show(True)
            else:
                topframe = wx.FindWindowById(topframeid)
                topframe.Show(True)

            ip_address = login_result['ip_address']
            set_val('ip_address', ip_address)  ##设置IP
            Getip_dianxinThread(ip_address) ##判定是否电信网址的功能
            ##初始化结果
            print(login_result)
            data = login_result['data']
            remote_variables(**data)
            target_time = get_val('target_time')
            start_time = target_time - 30 * 60
            set_val('start_time', start_time)
            ##初始化账号
            from component.staticmethod import Hotkey_listen
            from component.variable import init_pos
            Px = get_val('Px')
            Py = get_val('Py')
            init_pos(Px, Py)
            self.Show(False)  ##关闭窗口
            listening = get_val('listening')
            if not listening:
                Hotkey_listen()
        else:
            self.panel.code_monibtn.Enable()
            wx.MessageBox('连接服务器失败', '用户登录', wx.OK | wx.ICON_ERROR)

    def Purchase(self, event):
        print("购买")

    def OnClose(self, event):
        event.Skip()
        sys.exit(0)
