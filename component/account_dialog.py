import wx
from wx.lib.pubsub import pub

from component.variable import get_val, set_val, get_dick, set_dick


class Account_dialog(wx.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        x = get_val('Px')
        y = get_val('Py')
        print(x, y)
        super(Account_dialog, self).__init__(parent, title=title, size=(250, 180), pos=(x + 895, y + 50))

        self.titlefont = wx.Font(13, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        self.accountsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.account = wx.StaticText(self, label=u"标书号")
        self.accountText = wx.TextCtrl(self, -1, style=wx.TE_CENTER | wx.TE_PROCESS_ENTER, size=(150, 25))
        self.accountsizer.Add(self.account, flag=wx.TOP, border=4)
        self.accountsizer.Add(self.accountText, flag=wx.LEFT, border=27)

        self.passwordsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.password = wx.StaticText(self, label=u"标书密码")
        self.passwordText = wx.TextCtrl(self, -1, style=wx.TE_CENTER | wx.TE_PROCESS_ENTER, size=(150, 25))
        self.passwordsizer.Add(self.password, flag=wx.TOP, border=4)
        self.passwordsizer.Add(self.passwordText, flag=wx.LEFT, border=15)

        self.idnumbersizer = wx.BoxSizer(wx.HORIZONTAL)
        self.idnumber = wx.StaticText(self, label=u"身份证号")
        self.idnumberText = wx.TextCtrl(self, -1, style=wx.TE_CENTER | wx.TE_PROCESS_ENTER, size=(150, 25))
        self.idnumbersizer.Add(self.idnumber, flag=wx.TOP, border=4)
        self.idnumbersizer.Add(self.idnumberText, flag=wx.LEFT, border=15)

        self.buttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.savebtn = wx.Button(self, label='保存')
        self.savebtn.Bind(wx.EVT_BUTTON, self.Save)
        self.buttonsizer.Add(self.savebtn, flag=wx.LEFT, border=130)

        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.vbox.Add(self.accountsizer)
        self.vbox.Add(self.passwordsizer, flag=wx.TOP, border=5)
        self.vbox.Add(self.idnumbersizer, flag=wx.TOP, border=5)
        self.vbox.Add(self.buttonsizer, flag=wx.TOP, border=5)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox.Add(self.vbox, flag=wx.ALL, border=10)
        self.SetSizer(self.hbox)

        ## 移动事件
        self.Bind(wx.EVT_MOVE, self.move)

        self.init_account()

        pub.subscribe(self.close, 'account close')

    def close(self):
        self.Destroy()
        moni_on = get_val('moni_on')
        moni_webframe = get_val('moni_webframe')
        guopai_webframe = get_val('guopai_webframe')
        if moni_on:
            moni = wx.FindWindowById(moni_webframe)
            moni.SetFocus()
        else:
            guopai = wx.FindWindowById(guopai_webframe)
            guopai.SetFocus()

    def Save(self, event):
        bid_number = self.accountText.GetValue()
        bid_password = self.passwordText.GetValue()
        idcard = self.idnumberText.GetValue()

        set_val('bid_number', bid_number)
        set_val('bid_password', bid_password)
        set_val('idcard', idcard)

        bidnumber_js = "document.getElementById('bidnumber').value = '{0}';".format(bid_number)
        bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bid_password)
        idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
        set_val('bidnumber_js', bidnumber_js)
        set_val('bidpassword_js', bidpassword_js)
        set_val('idcard_js', idcard_js)

        ##同步到strategy_data
        manage = get_val('manage')
        if manage:
            strategy_data = get_val('strategy_data')
            identify = get_val('identify')
            strategy_data[identify]['Bid_number'] = bid_number
            strategy_data[identify]['Bid_password'] = bid_password
            strategy_data[identify]['ID_number'] = idcard
            set_val('strategy_data', strategy_data)

        self.Destroy()

    def move(self, event):
        self.Destroy()
        moni_on = get_val('moni_on')
        moni_webframe = get_val('moni_webframe')
        guopai_webframe = get_val('guopai_webframe')
        if moni_on:
            moni = wx.FindWindowById(moni_webframe)
            moni.SetFocus()
        else:
            guopai = wx.FindWindowById(guopai_webframe)
            guopai.SetFocus()

    def init_account(self):
        bid_number = get_val('bid_number')
        bid_password = get_val('bid_password')
        idcard = get_val('idcard')
        if bid_number and bid_number != 'null' \
                and bid_password and bid_password != 'null' \
                and idcard and idcard != 'null':
            self.accountText.SetValue(bid_number)
            self.passwordText.SetValue(bid_password)
            self.idnumberText.SetValue(idcard)
