import json

import wx
from wx.lib.pubsub import pub

from component.variable import get_val, set_val, get_dick, set_dick, set_strategy_dick
from component.staticmethod import gettime


# class Smart_tijiaoDialog2(wx.Dialog):
#     def __init__(self):
#         wx.Dialog.__init__(self, parent=None)
#         self.Bind(wx.EVT_CLOSE, self.on_close)
#         self.SetSizerAndFit(self.CreateButtonSizer(wx.OK | wx.CANCEL))
#
#     def on_close(self, event):
#         print('hello from on_close!')
#         self.Destroy()

class Smart_tijiaoDialog(wx.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        x = get_val('Px')
        y = get_val('Py')
        print(x, y)
        super(Smart_tijiaoDialog, self).__init__(parent, title=title, size=(280, 160), pos=(x+884, y+200))
        self.panel = wx.Panel(self)
        # self.okbtn = wx.Button(self.panel, wx.ID_OK, label="关闭", size=(50, 20))
        self.wordfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        ##三段式提交
        # 第一行
        self.second_tijiao_sizer_smart1 = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiao_time_smart1 = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time_smart1.SetRange(1.0, 59.0)
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
        self.second_tijiao_time_smart2.SetRange(1.0, 59.0)
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
        self.second_tijiao_time_smart3.SetRange(1.0, 59.0)
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
        self.second_tijiao_time_smart.SetRange(1.0, 59.0)
        self.second_tijiao_time_smart.SetValue(52.0)
        self.second_tijiao_time_smart.SetIncrement(0.1)
        self.second_tijiao_time_smart_label = wx.StaticText(self, label=" 强制提交")
        self.second_tijiao_time_smart_label.SetFont(self.wordfont)
        self.second_tijiao_time_smart.Bind(wx.EVT_TEXT, self.Second_tijiao_time_smart)
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

        ## 移动事件
        self.Bind(wx.EVT_MOVE, self.move)

        self.init_dlg()

        pub.subscribe(self.close, 'dialog close')

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
        one_time2_smart2 = get_val('one_time2_smart2')
        tem = self.second_tijiao_time_smart1.GetValue()
        timelist = get_val('timelist')
        strategy_type = get_dick('strategy_type')
        one_time1 = get_val('one_time1')
        second_time1 = get_val('second_time1')
        if strategy_type == '2':
            if int(tem * 10) in timelist and tem <= one_time2_smart2 - 1 and tem >= one_time1 + 1:
                print(one_time2_smart2, tem)
                one_time2_smart1 = tem
                set_val('one_time2_smart1', float(tem))
                set_val('one_realtime2_smart1', gettime(one_time2_smart1))  # 计算得到的时间戳
                self.update_strategy()
            else:
                self.second_tijiao_time_smart1.SetValue(one_time2_smart1)
        elif strategy_type == '3':
            if int(tem * 10) in timelist and tem <= one_time2_smart2 - 1 and tem >= second_time1 + 1:
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
        tem = self.second_tijiaoyanchi_time_smart1.GetValue()
        yanchilist = get_val('yanchilist')
        if int(tem * 10) in yanchilist:
            set_val('one_delay_smart1', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart1.SetValue(one_delay_smart1)

    def Second_tijiao_time_smart2(self, event):
        one_time2_smart1 = get_val('one_time2_smart1')
        one_time2_smart2 = get_val('one_time2_smart2')
        one_time2_smart3 = get_val('one_time2_smart3')
        tem = self.second_tijiao_time_smart2.GetValue()
        timelist = get_val('timelist')
        if int(tem * 10) in timelist and tem <= one_time2_smart3 - 1 and tem >= one_time2_smart1 + 1:
            print(one_time2_smart1, one_time2_smart2, one_time2_smart3)
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
        tem = self.second_tijiaoyanchi_time_smart2.GetValue()
        yanchilist = get_val('yanchilist')
        if int(tem * 10) in yanchilist:
            set_val('one_delay_smart2', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart2.SetValue(one_delay_smart2)

    def Second_tijiao_time_smart3(self, event):
        one_time2_smart2 = get_val('one_time2_smart2')
        one_time2_smart3 = get_val('one_time2_smart3')
        tem = self.second_tijiao_time_smart3.GetValue()
        timelist = get_val('timelist')
        print(tem)
        print(timelist)
        if int(tem * 10) in timelist and tem >=  one_time2_smart2 + 1:
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
        tem = self.second_tijiaoyanchi_time_smart3.GetValue()
        yanchilist = get_val('yanchilist')
        if int(tem * 10) in yanchilist:
            set_val('one_delay_smart3', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time_smart3.SetValue(one_delay_smart3)

    def Second_tijiao_time_smart(self, event):
        one_time2_smart = get_val('one_time2_smart')
        tem = self.second_tijiao_time_smart.GetValue()
        timelist = get_val('timelist')
        one_time2_smart3 = get_val('one_time2_smart3')
        if int(tem * 10) in timelist and tem >= one_time2_smart3:
            one_time2_smart = tem
            set_val('one_time2_smart', float(tem))
            set_val('one_realtime2_smart', gettime(one_time2_smart))  # 计算得到的时间戳
            print(gettime(one_time2_smart))
            self.update_strategy()
        else:
            self.second_tijiao_time_smart3.SetValue(one_time2_smart)


    ###需要进一步扩展 调整策略设置后需要 修正templist
    def update_strategy(self):
        strategy_data = get_val('strategy_data')
        identify = get_val("identify")
        strategy_dick = strategy_data[identify]['strategy_dick']
        strategy_type = get_dick('strategy_type')
        advance_list = [100, 200, 300, 0]
        templist = strategy_dick[strategy_type]
        if strategy_type == '2':
            templist[14] = advance_list[self.second_tijiao_pricediff_smart1.GetSelection()]
            templist[15] = self.second_tijiaoyanchi_time_smart1.GetValue()
            templist[16] = self.second_tijiao_time_smart1.GetValue()
            templist[17] = advance_list[self.second_tijiao_pricediff_smart2.GetSelection()]
            templist[18] = self.second_tijiaoyanchi_time_smart2.GetValue()
            templist[19] = self.second_tijiao_time_smart2.GetValue()
            templist[20] = advance_list[self.second_tijiao_pricediff_smart3.GetSelection()]
            templist[21] = self.second_tijiaoyanchi_time_smart3.GetValue()
            templist[22] = self.second_tijiao_time_smart3.GetValue()
            templist[23] = self.second_tijiao_time_smart.GetValue()

        elif strategy_type == '3':
            templist[14] = advance_list[self.second_tijiao_pricediff_smart1.GetSelection()]
            templist[15] = self.second_tijiaoyanchi_time_smart1.GetValue()
            templist[16] = self.second_tijiao_time_smart1.GetValue()
            templist[17] = advance_list[self.second_tijiao_pricediff_smart2.GetSelection()]
            templist[18] = self.second_tijiaoyanchi_time_smart2.GetValue()
            templist[19] = self.second_tijiao_time_smart2.GetValue()
            templist[20] = advance_list[self.second_tijiao_pricediff_smart3.GetSelection()]
            templist[21] = self.second_tijiaoyanchi_time_smart3.GetValue()
            templist[22] = self.second_tijiao_time_smart3.GetValue()
            templist[23] = self.second_tijiao_time_smart.GetValue()
        strategy_dick[strategy_type] = templist
        strategy_data[identify]['strategy_dick'] = json.dumps(strategy_dick)
        set_val('strategy_data', strategy_data)



    def init_dlg(self):
        identify = get_val('identify')
        set_val('identify', identify)
        strategy_data = get_val('strategy_data')
        strategy_dick = strategy_data[identify]['strategy_dick']
        strategy_dick = json.loads(strategy_dick)
        set_strategy_dick(strategy_dick)
        strategy_type = get_dick('strategy_type')
        strategy_list = get_dick(str(strategy_type))
        advance_list = [100, 200, 300, 0]

        if strategy_type == '2':
            self.second_tijiao_pricediff_smart1.SetSelection(advance_list.index(strategy_list[14]))
            self.second_tijiaoyanchi_time_smart1.SetValue(strategy_list[15])
            self.second_tijiao_time_smart1.SetValue(strategy_list[16])
            self.second_tijiao_pricediff_smart2.SetSelection(advance_list.index(strategy_list[17]))
            self.second_tijiaoyanchi_time_smart2.SetValue(strategy_list[18])
            self.second_tijiao_time_smart2.SetValue(strategy_list[19])
            self.second_tijiao_pricediff_smart3.SetSelection(advance_list.index(strategy_list[20]))
            self.second_tijiaoyanchi_time_smart3.SetValue(strategy_list[21])
            self.second_tijiao_time_smart3.SetValue(strategy_list[22])
            self.second_tijiao_time_smart.SetValue(strategy_list[23])

        elif strategy_type == '3':
            self.second_tijiao_pricediff_smart1.SetSelection(advance_list.index(strategy_list[14]))
            self.second_tijiaoyanchi_time_smart1.SetValue(strategy_list[15])
            self.second_tijiao_time_smart1.SetValue(strategy_list[16])
            self.second_tijiao_pricediff_smart2.SetSelection(advance_list.index(strategy_list[17]))
            self.second_tijiaoyanchi_time_smart2.SetValue(strategy_list[18])
            self.second_tijiao_time_smart2.SetValue(strategy_list[19])
            self.second_tijiao_pricediff_smart3.SetSelection(advance_list.index(strategy_list[20]))
            self.second_tijiaoyanchi_time_smart3.SetValue(strategy_list[21])
            self.second_tijiao_time_smart3.SetValue(strategy_list[22])
            self.second_tijiao_time_smart.SetValue(strategy_list[23])

