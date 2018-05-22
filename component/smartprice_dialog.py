import wx
from component.variable import get_val, set_val
from component.staticmethod import gettime


class Smart_tijiaoDialog(wx.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        x, y = parent.Position
        super(Smart_tijiaoDialog, self).__init__(parent, title=title, size=(280, 160), pos=(x+980, y+180))
        self.panel = wx.Panel(self)
        # self.okbtn = wx.Button(self.panel, wx.ID_OK, label="关闭", size=(50, 20))
        self.wordfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        ##三段式提交
        # 第一行
        self.second_tijiao_sizer_smart1 = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiao_time_smart1 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time_smart1.SetRange(50.0, 55.0)
        self.second_tijiao_time_smart1.SetValue(52.0)
        self.second_tijiao_time_smart1.SetIncrement(0.1)
        tijiao_choices = get_val('tijiao_choices')
        self.second_tijiao_pricediff_smart1 = wx.Choice(self, -1, choices=tijiao_choices)
        self.second_tijiao_pricediff_smart1.SetSelection(0)
        self.second_tijiaoyanchi_label_smart1 = wx.StaticText(self, label=" 延迟",
                                                              style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiaoyanchi_label_smart1.SetFont(self.wordfont)
        self.second_tijiao_label_smart1 = wx.StaticText(self, label=" 提交  ",
                                                        style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiao_label_smart1.SetFont(self.wordfont)
        self.second_tijiaoyanchi_time_smart1 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiaoyanchi_time_smart1.SetRange(0.0, 1.9)
        self.second_tijiaoyanchi_time_smart1.SetValue(0.5)
        self.second_tijiaoyanchi_time_smart1.SetIncrement(0.1)

        self.second_tijiao_sizer_smart1.Add(self.second_tijiao_time_smart1, flag=wx.LEFT | wx.TOP, border=3)
        self.second_tijiao_sizer_smart1.Add(self.second_tijiao_pricediff_smart1)
        self.second_tijiao_sizer_smart1.Add(self.second_tijiao_label_smart1, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart1.Add(self.second_tijiaoyanchi_label_smart1, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart1.Add(self.second_tijiaoyanchi_time_smart1, flag=wx.TOP, border=3)

        self.second_tijiao_time_smart1.Bind(wx.EVT_TEXT, self.Second_tijiao_time_smart1)
        self.second_tijiao_pricediff_smart1.Bind(wx.EVT_CHOICE, self.Second_tijiao_pricediff_smart1)
        self.second_tijiaoyanchi_time_smart1.Bind(wx.EVT_TEXT, self.Second_tijiaoyanchi_time_smart1)

        # 第二行
        self.second_tijiao_sizer_smart2 = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiao_time_smart2 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time_smart2.SetRange(50.0, 55.0)
        self.second_tijiao_time_smart2.SetValue(52.0)
        self.second_tijiao_time_smart2.SetIncrement(0.1)
        tijiao_choices = get_val('tijiao_choices')
        self.second_tijiao_pricediff_smart2 = wx.Choice(self, -1, choices=tijiao_choices)
        self.second_tijiao_pricediff_smart2.SetSelection(0)
        self.second_tijiaoyanchi_label_smart2 = wx.StaticText(self, label=" 延迟",
                                                              style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiaoyanchi_label_smart2.SetFont(self.wordfont)
        self.second_tijiao_label_smart2 = wx.StaticText(self, label=" 提交  ",
                                                        style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiao_label_smart2.SetFont(self.wordfont)
        self.second_tijiaoyanchi_time_smart2 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiaoyanchi_time_smart2.SetRange(0.0, 1.9)
        self.second_tijiaoyanchi_time_smart2.SetValue(0.5)
        self.second_tijiaoyanchi_time_smart2.SetIncrement(0.1)

        self.second_tijiao_sizer_smart2.Add(self.second_tijiao_time_smart2, flag=wx.LEFT | wx.TOP, border=3)
        self.second_tijiao_sizer_smart2.Add(self.second_tijiao_pricediff_smart2)
        self.second_tijiao_sizer_smart2.Add(self.second_tijiao_label_smart2, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart2.Add(self.second_tijiaoyanchi_label_smart2, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart2.Add(self.second_tijiaoyanchi_time_smart2, flag=wx.TOP, border=3)

        self.second_tijiao_time_smart2.Bind(wx.EVT_TEXT, self.Second_tijiao_time_smart2)
        self.second_tijiao_pricediff_smart2.Bind(wx.EVT_CHOICE, self.Second_tijiao_pricediff_smart2)
        self.second_tijiaoyanchi_time_smart2.Bind(wx.EVT_TEXT, self.Second_tijiaoyanchi_time_smart2)

        # 第三行
        self.second_tijiao_sizer_smart3 = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiao_time_smart3 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time_smart3.SetRange(50.0, 55.0)
        self.second_tijiao_time_smart3.SetValue(52.0)
        self.second_tijiao_time_smart3.SetIncrement(0.1)
        tijiao_choices = get_val('tijiao_choices')
        self.second_tijiao_pricediff_smart3 = wx.Choice(self, -1, choices=tijiao_choices)
        self.second_tijiao_pricediff_smart3.SetSelection(0)
        self.second_tijiaoyanchi_label_smart3 = wx.StaticText(self, label=" 延迟",
                                                              style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiaoyanchi_label_smart3.SetFont(self.wordfont)
        self.second_tijiao_label_smart3 = wx.StaticText(self, label=" 提交  ",
                                                        style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiao_label_smart3.SetFont(self.wordfont)
        self.second_tijiaoyanchi_time_smart3 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiaoyanchi_time_smart3.SetRange(0.0, 1.9)
        self.second_tijiaoyanchi_time_smart3.SetValue(0.5)
        self.second_tijiaoyanchi_time_smart3.SetIncrement(0.1)

        self.second_tijiao_sizer_smart3.Add(self.second_tijiao_time_smart3, flag=wx.LEFT | wx.TOP, border=3)
        self.second_tijiao_sizer_smart3.Add(self.second_tijiao_pricediff_smart3)
        self.second_tijiao_sizer_smart3.Add(self.second_tijiao_label_smart3, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart3.Add(self.second_tijiaoyanchi_label_smart3, flag=wx.TOP, border=4)
        self.second_tijiao_sizer_smart3.Add(self.second_tijiaoyanchi_time_smart3, flag=wx.TOP, border=3)


        self.second_tijiao_time_smart3.Bind(wx.EVT_TEXT, self.Second_tijiao_time_smart3)
        self.second_tijiao_pricediff_smart3.Bind(wx.EVT_CHOICE, self.Second_tijiao_pricediff_smart3)
        self.second_tijiaoyanchi_time_smart3.Bind(wx.EVT_TEXT, self.Second_tijiaoyanchi_time_smart3)

        ##强制提交时间
        self.second_tijiao_time_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiao_time_smart = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time_smart.SetRange(50.0, 58.0)
        self.second_tijiao_time_smart.SetValue(52.0)
        self.second_tijiao_time_smart.SetIncrement(0.1)
        self.second_tijiao_time_smart_label = wx.StaticText(self, label=" 强制提交")
        self.second_tijiao_time_smart_label.SetFont(self.wordfont)
        self.second_tijiao_time_sizer.Add(self.second_tijiao_time_smart, flag=wx.LEFT, border=3)
        self.second_tijiao_time_sizer.Add(self.second_tijiao_time_smart_label)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.Add(self.second_tijiao_sizer_smart1, flag=wx.LEFT | wx.TOP, border=3)
        self.vsizer.Add(self.second_tijiao_sizer_smart2, flag=wx.LEFT | wx.TOP, border=3)
        self.vsizer.Add(self.second_tijiao_sizer_smart3, flag=wx.LEFT | wx.TOP, border=3)
        self.vsizer.Add(self.second_tijiao_time_sizer, flag=wx.LEFT | wx.TOP, border=3)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.vsizer, flag=wx.ALL, border=3)
        self.SetSizer(self.sizer)

        #移动事件
        self.Bind(wx.EVT_MOVE, self.move)

        self.init_dlg()

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



    def Second_tijiao_time_smart1(self, event):
        one_time2_smart1 = get_val('one_time2_smart1')
        tem = self.second_tijiao_time_smart1.GetValue()
        templist = [40 + i * 0.1 for i in range(200)]
        if tem in templist:
            one_time2_smart1 = tem
            set_val('one_time2_smart1', float(tem))
            set_val('one_realtime2_smart1', gettime(one_time2_smart1))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.second_tijiao_time_smart1.SetValue(one_time2_smart1)

    def Second_tijiao_pricediff_smart1(self, event):
        select = self.second_tijiao_pricediff_smart1.GetString(self.second_tijiao_pricediff_smart1.GetSelection())
        if select == u"提前100":
            set_val('one_advance_smart1', 100)
        elif select == u"提前200":
            set_val('one_advance_smart1', 200)
        elif select == u"提前300":
            set_val('one_advance_smart1', 300)
        else:
            set_val('one_advance_smart1', 0)
        self.update_strategy()

    def Second_tijiaoyanchi_time_smart1(self, event):
        one_delay_smart1 = get_val('one_delay_smart1')
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.second_tijiaoyanchi_time_smart1.GetValue())
        if tem in templist:
            set_val('one_delay_smart1', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart1.SetValue(one_delay_smart1)

    def Second_tijiao_time_smart2(self, event):
        one_time2_smart2 = get_val('one_time2_smart2')
        tem = self.second_tijiao_time_smart2.GetValue()
        templist = [40 + i * 0.1 for i in range(200)]
        if tem in templist:
            one_time2_smart2 = tem
            set_val('one_time2_smart2', float(tem))
            set_val('one_realtime2_smart2', gettime(one_time2_smart2))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.second_tijiao_time_smart2.SetValue(one_time2_smart2)

    def Second_tijiao_pricediff_smart2(self, event):
        select = self.second_tijiao_pricediff_smart2.GetString(
                                                        self.second_tijiao_pricediff_smart2.GetSelection())
        if select == u"提前100":
            set_val('one_advance_smart2', 100)
        elif select == u"提前200":
            set_val('one_advance_smart2', 200)
        elif select == u"提前300":
            set_val('one_advance_smart2', 300)
        else:
            set_val('one_advance_smart2', 0)
        self.update_strategy()

    def Second_tijiaoyanchi_time_smart2(self, event):
        one_delay_smart2 = get_val('one_delay_smart2')
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.second_tijiaoyanchi_time_smart2.GetValue())
        if tem in templist:
            set_val('one_delay_smart2', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart2.SetValue(one_delay_smart2)

    def Second_tijiao_time_smart3(self, event):
        one_time2_smart3 = get_val('one_time2_smart3')
        tem = self.second_tijiao_time_smart3.GetValue()
        templist = [40 + i * 0.1 for i in range(200)]
        if tem in templist:
            one_time2_smart3 = tem
            set_val('one_time2_smart3', float(tem))
            set_val('one_realtime2_smart3', gettime(one_time2_smart3))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.second_tijiao_time_smart3.SetValue(one_time2_smart3)

    def Second_tijiao_pricediff_smart3(self, event):
        select = self.second_tijiao_pricediff_smart3.GetString(self.second_tijiao_pricediff_smart3.GetSelection())
        if select == u"提前100":
            set_val('one_advance_smart3', 100)
        elif select == u"提前200":
            set_val('one_advance_smart3', 200)
        elif select == u"提前300":
            set_val('one_advance_smart3', 300)
        else:
            set_val('one_advance_smart3', 0)
        self.update_strategy()

    def Second_tijiaoyanchi_time_smart3(self, event):
        one_delay_smart3 = get_val('one_delay_smart3')
        templist = ['0.%d' % i for i in range(11)]  # 符点数运算BUG
        templist.append('1.0')
        tem = str(self.second_tijiaoyanchi_time_smart3.GetValue())
        if tem in templist:
            set_val('one_delay_smart3', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart3.SetValue(one_delay_smart3)

    def Second_tijiao_time_smart(self, event):
        one_time2_smart = get_val('one_time2_smart')
        tem = self.second_tijiao_time_smart.GetValue()
        templist = [53 + i * 0.1 for i in range(51)]
        if tem in templist:
            one_time2_smart = tem
            set_val('one_time2_smart', float(tem))
            set_val('one_realtime2_smart', gettime(one_time2_smart))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.second_tijiao_time_smart3.SetValue(one_time2_smart)


    ###需要进一步扩展 调整策略设置后需要 修正templist
    def update_strategy(self):
        strategy_type = get_val('strategy_type')
        advance_list = [100, 200, 300, 0]
        templist = [0] * 20
        templist[0] = get_val('strategy_type')
        templist[1] = get_val('one_time')
        templist[2] = get_val('one_diff')
        templist[3] = advance_list[self.second_tijiao_pricediff_smart1.GetSelection()]
        templist[4] = self.second_tijiaoyanchi_time_smart1.GetValue()
        templist[5] = self.second_tijiao_time_smart1.GetValue()
        templist[6] = advance_list[self.second_tijiao_pricediff_smart2.GetSelection()]
        templist[7] = self.second_tijiaoyanchi_time_smart2.GetValue()
        templist[8] = self.second_tijiao_time_smart2.GetValue()
        templist[9] = advance_list[self.second_tijiao_pricediff_smart3.GetSelection()]
        templist[10] = self.second_tijiaoyanchi_time_smart3.GetValue()
        templist[11] = self.second_tijiao_time_smart3.GetValue()
        templist[12] = self.second_tijiao_time_smart.GetValue()
        strategy_choices = get_val('strategy_choices')
        set_val('strategy_description', strategy_choices[strategy_type])
        set_val(strategy_type, templist)




    def init_dlg(self):
        strategy_type = get_val('strategy_type')
        strategy_list = get_val(strategy_type)
        advance_list = [100, 200, 300, 0]
        self.second_tijiao_pricediff_smart1.SetSelection(advance_list.index(strategy_list[3]))
        self.second_tijiaoyanchi_time_smart1.SetValue(strategy_list[4])
        self.second_tijiao_time_smart1.SetValue(strategy_list[5])
        self.second_tijiao_pricediff_smart2.SetSelection(advance_list.index(strategy_list[6]))
        self.second_tijiaoyanchi_time_smart2.SetValue(strategy_list[7])
        self.second_tijiao_time_smart2.SetValue(strategy_list[8])
        self.second_tijiao_pricediff_smart3.SetSelection(advance_list.index(strategy_list[9]))
        self.second_tijiaoyanchi_time_smart3.SetValue(strategy_list[10])
        self.second_tijiao_time_smart3.SetValue(strategy_list[11])
        self.second_tijiao_time_smart.SetValue(strategy_list[12])

        set_val('one_time1', strategy_list[1])  # 第一次出价加价
        set_val('one_diff', strategy_list[2])  # 第一次加价幅度
        set_val('one_advance_smart1', strategy_list[3])
        set_val('one_delay_smart1', strategy_list[4])
        set_val('one_time2_smart1', strategy_list[5])
        set_val('one_advance_smart2', strategy_list[6])
        set_val('one_delay_smart2', strategy_list[7])
        set_val('one_time2_smart2', strategy_list[8])
        set_val('one_advance_smart3', strategy_list[9])
        set_val('one_delay_smart3', strategy_list[10])
        set_val('one_time2_smart3', strategy_list[11])
        set_val('one_time2_smart', strategy_list[12])
        
        set_val('one_realtime2_smart1', gettime(strategy_list[5]))
        set_val('one_realtime2_smart2', gettime(strategy_list[8]))
        set_val('one_realtime2_smart3', gettime(strategy_list[11]))
        set_val('one_realtime2_smart', gettime(strategy_list[12]))


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(250, 150))
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        btn = wx.Button(panel, label="Modal Dialog", pos=(75, 10))
        btn1 = wx.Button(panel, label="Modeless Dialog", pos=(75, 40))
        btn2 = wx.Button(panel, label="MessageBox", pos=(75, 70))
        btn.Bind(wx.EVT_BUTTON, self.OnModal)

        a = btn1.Bind(wx.EVT_BUTTON, self.OnModeless)
        print(a)

        btn2.Bind(wx.EVT_BUTTON, self.Onmsgbox)
        self.Centre()
        self.Show(True)

    def OnModal(self, event):
        a = Smart_tijiaoDialog(self, "Dialog").ShowModal()
        print(a)

    def OnModeless(self, event):
        a = Smart_tijiaoDialog(self, "Dialog").Show()

    def Onmsgbox(self, event):
        wx.MessageBox("This is a Message Box", "Message", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    ex = wx.App()
    Mywin(None, 'Dialog Demo - www.yiibai.com')
    ex.MainLoop()
