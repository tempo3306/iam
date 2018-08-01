'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:34
'''

from component.imgcut import findpos
from component.paishou_panel import PaishouPanel
from component.staticmethod import *
import logging

logger = logging.getLogger()
from component.variable import get_dick, set_dick, get_strategy_dick


# -----------------------------------------------------------
class StatusPanel(wx.Panel):
    def __init__(self, parent, tablabel):
        wx.Panel.__init__(self, parent=parent, id=20)
        self.control = wx.StaticBox(self, -1, "基本设置")
        self.controlbox = wx.StaticBoxSizer(self.control, wx.VERTICAL)
        self.controlgrid = wx.GridBagSizer(4, 2)  # 网格组件

        ##功能区
        self.webtabButton = wx.Button(self, label=tablabel, size=(95, 30))  # 未来扩展
        # self.priceviewButton = wx.Button(self, label='导出跳价', size=(105,30))  # 未来扩展

        self.onkeyloginButton = wx.Button(self, label='一键登录', size=(95, 30))  # 时间
        self.posajustButton = wx.Button(self, label='刷新定位', size=(95, 30))  # 位置调整
        self.refreshwebButton = wx.Button(self, label='刷新页面', size=(95, 30))  # 时间同步

        ##绑定
        self.webtabButton.Bind(wx.EVT_BUTTON, self.webtab)
        self.refreshwebButton.Bind(wx.EVT_BUTTON, self.refreshweb)
        # self.priceviewButton.Bind(wx.EVT_BUTTON, self.priceview)

        # self.remotetimeButton.Bind(wx.EVT_BUTTON, self.getremotetime)
        self.posajustButton.Bind(wx.EVT_BUTTON, self.posautoajust)
        self.onkeyloginButton.Bind(wx.EVT_BUTTON, self.onkeylogin)

        self.controlgrid.Add(self.webtabButton, pos=(0, 0))  # 布局
        self.controlgrid.Add(self.onkeyloginButton, pos=(0, 1))
        self.controlgrid.Add(self.posajustButton, pos=(1, 0))
        self.controlgrid.Add(self.refreshwebButton, pos=(1, 1))

        # # 验证码放大
        self.yanzhengma_scale = wx.CheckBox(self, -1, label=u'验证码放大')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.Yanzhengma_scale, self.yanzhengma_scale)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # # 验证码自动预览
        self.yanzhengma_autoview = wx.CheckBox(self, -1, label=u'验证码自动预览')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.Yanzhengma_autoview, self.yanzhengma_autoview)
        hbox1.Add(self.yanzhengma_scale)
        hbox1.Add(self.yanzhengma_autoview)


        # # 时间区
        # self.autotime = wx.CheckBox(self, -1, label=u'自动时间同步')  # 开启时间显示
        # self.Bind(wx.EVT_CHECKBOX, self.autotime_set, self.autotime)
        # hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # hbox1.Add(self.autotime)

        # ##确认方式
        # confirm_choice = ["E键", "回车"]
        # self.confirm_choice = wx.Choice(self, -1, choices=confirm_choice)
        # self.confirm_choice.SetSelection(0)
        # self.Bind(wx.EVT_CHOICE, self.Confirmchoice, self.confirm_choice)
        #
        # self.confirm_label = wx.StaticText(self, label=u"确认提交方式")
        # hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # hbox2.Add(self.confirm_label, flag=wx.TOP, border=4)
        # hbox2.Add(self.confirm_choice)

        self.controlbox.Add(self.controlgrid)  # 把网格组加到 功能框内
        self.controlbox.Add(hbox1,flag=wx.ALL, border=6)
        # self.controlbox.Add(hbox2)
        ##----------------------------------------------------------------------
        ###策略设置区域
        self.strategy_area_label = wx.StaticBox(self, -1, "策略设置")
        self.strategy_area_sizer = wx.StaticBoxSizer(self.strategy_area_label, wx.VERTICAL)
        self.strategy_area_vbox = wx.BoxSizer(wx.VERTICAL)
        strategy_choices = get_val('strategy_choices')
        self.choice_strategy = wx.ComboBox(self, choices=strategy_choices, size=(216, 25),
                                           style=wx.CB_READONLY)
        self.choice_strategy.SetSelection(0)
        self.choice_strategy.Bind(wx.EVT_COMBOBOX, self.Choice_strategy)

        self.titlefont = wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.numberfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.wordfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        ##构建不同策略的sizer
        self.strategy_sizer = wx.BoxSizer(wx.VERTICAL)

        ########第二次出价
        ##label行
        self.second_chujia_label = wx.StaticBox(self, -1, "第二次出价")
        self.second_chujia_label_sizer = wx.StaticBoxSizer(self.second_chujia_label, wx.VERTICAL)
        self.second_chujia_vbox = wx.BoxSizer(wx.VERTICAL)
        self.second_chujia_label.SetFont(self.titlefont)

        ##出价设置行
        self.second_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.second_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                    style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_jiajia_time.SetRange(0, 55)
        self.second_jiajia_time.SetValue(48)
        self.second_jiajia_time.SetIncrement(0.1)
        # self.second_jiajia_time.SetFont(self.numberfont)
        self.second_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.second_jiajia_price.SetRange(300, 1500)
        self.second_jiajia_price.SetValue(700)
        self.second_jiajia_price.SetIncrement(100)
        self.second_time_label = wx.StaticText(self, label="11 : 29 : ",
                                               style=wx.ALIGN_RIGHT)
        self.second_time_label.SetFont(self.numberfont)
        # self.second_jiajia_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        # self.second_jiajia_miao.SetFont(self.wordfont)
        self.second_jiahao = wx.StaticText(self, label=' + ', style=wx.ALIGN_CENTER)
        self.second_jiahao.SetFont(self.wordfont)
        self.second_jiajia_sizer.Add(self.second_time_label, wx.LEFT, border=10)
        self.second_jiajia_sizer.Add(self.second_jiajia_time)
        # self.second_jiajia_sizer.Add(self.second_jiajia_miao)
        self.second_jiajia_sizer.Add(self.second_jiahao)
        self.second_jiajia_sizer.Add(self.second_jiajia_price)
        ##提交设置行
        self.second_tijiao_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tijiao_choices = get_val('tijiao_choices')
        self.second_tijiao_pricediff = wx.Choice(self, -1, choices=tijiao_choices)
        self.second_tijiao_pricediff.SetSelection(0)
        self.second_tijiaoyanchi_label = wx.StaticText(self, label=" 延迟",
                                                       style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiaoyanchi_label.SetFont(self.wordfont)
        self.second_tijiao_label = wx.StaticText(self, label=" 提交  ", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.second_tijiao_label.SetFont(self.wordfont)
        self.second_tijiaoyanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiaoyanchi_time.SetRange(0.0, 1.9)
        self.second_tijiaoyanchi_time.SetValue(0.5)
        self.second_tijiaoyanchi_time.SetIncrement(0.1)
        # self.second_tijiao_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        # self.second_tijiao_miao.SetFont(self.wordfont)

        self.second_tijiao_sizer.Add(self.second_tijiao_pricediff)
        self.second_tijiao_sizer.Add(self.second_tijiao_label, flag=wx.TOP, border=4)
        self.second_tijiao_sizer.Add(self.second_tijiaoyanchi_label, flag=wx.TOP, border=4)
        self.second_tijiao_sizer.Add(self.second_tijiaoyanchi_time, flag=wx.TOP, border=3)
        # self.second_tijiao_sizer.Add(self.second_tijiao_miao, flag=wx.TOP, border=4)

        self.second_tijiaotime_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.second_tijiaotime_label = wx.StaticText(self, label="11 : 29 : ")
        self.second_tijiaotime_label.SetFont(self.numberfont)
        self.second_tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.second_tijiao_time.SetRange(0, 59)
        self.second_tijiao_time.SetValue(58)
        self.second_tijiao_time.SetIncrement(0.1)
        self.second_forcetijiao_label = wx.StaticText(self, label=" 强制提交 ", style=wx.ALIGN_CENTER)
        self.second_forcetijiao_label.SetFont(self.wordfont)
        self.second_forcetijiao_check = wx.CheckBox(self)

        self.second_tijiaotime_sizer.Add(self.second_tijiaotime_label)
        self.second_tijiaotime_sizer.Add(self.second_tijiao_time)
        self.second_tijiaotime_sizer.Add(self.second_forcetijiao_label)
        self.second_tijiaotime_sizer.Add(self.second_forcetijiao_check, flag=wx.TOP, border=1)
        self.second_chujia_vbox.Add(self.second_jiajia_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_vbox.Add(self.second_tijiao_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_vbox.Add(self.second_tijiaotime_sizer, flag=wx.BOTTOM, border=10)
        self.second_chujia_label_sizer.Add(self.second_chujia_vbox)

        ##单次出价补枪
        self.buqiang_label = wx.StaticBox(self, -1, "自动补枪")
        self.buqiang_label_sizer = wx.StaticBoxSizer(self.buqiang_label, wx.VERTICAL)
        self.buqiang_vbox = wx.BoxSizer(wx.VERTICAL)
        self.buqiang_label.SetFont(self.titlefont)

        self.buqiang_checkbox = wx.CheckBox(self, -1, label="开启自动补枪", size=(135, 45))  # size=(190, 95)
        self.buqiang_tiplabel = wx.StaticText(self, -1, label="(出价提交完成后智能出价)",
                                              size=(205, 45), style=wx.ALIGN_CENTER)
        self.buqiang_tiplabel_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.buqiang_tiplabel_hbox.Add(self.buqiang_tiplabel)

        self.buqiang_vbox.Add(self.buqiang_checkbox, flag=wx.LEFT, border=60)
        self.buqiang_vbox.Add(self.buqiang_tiplabel_hbox, flag=wx.TOP, border=6)
        self.buqiang_label_sizer.Add(self.buqiang_vbox)

        ########第三次出价
        ##label行
        self.third_chujia_label = wx.StaticBox(self, -1, "第三次出价")
        self.third_chujia_label_sizer = wx.StaticBoxSizer(self.third_chujia_label, wx.VERTICAL)
        self.third_chujia_vbox = wx.BoxSizer(wx.VERTICAL)
        self.third_chujia_label.SetFont(self.titlefont)
        ##出价设置行
        self.third_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.third_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                   style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_jiajia_time.SetRange(0, 55)
        self.third_jiajia_time.SetValue(48)
        self.third_jiajia_time.SetIncrement(0.1)
        # self.third_jiajia_time.SetFont(self.numberfont)
        self.third_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.third_jiajia_price.SetRange(300, 1500)
        self.third_jiajia_price.SetValue(700)
        self.third_jiajia_price.SetIncrement(100)
        self.third_time_label = wx.StaticText(self, label="11 : 29 : ",
                                              style=wx.ALIGN_RIGHT)
        self.third_time_label.SetFont(self.numberfont)
        # self.third_jiajia_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        # self.third_jiajia_miao.SetFont(self.wordfont)
        self.third_jiahao = wx.StaticText(self, label=' + ', style=wx.ALIGN_CENTER)
        self.third_jiahao.SetFont(self.wordfont)
        self.third_jiajia_sizer.Add(self.third_time_label, wx.LEFT, border=10)
        self.third_jiajia_sizer.Add(self.third_jiajia_time)
        # self.third_jiajia_sizer.Add(self.third_jiajia_miao)
        self.third_jiajia_sizer.Add(self.third_jiahao)
        self.third_jiajia_sizer.Add(self.third_jiajia_price)
        ##提交设置行
        self.third_tijiao_sizer = wx.BoxSizer(wx.HORIZONTAL)
        tijiao_choices = get_val('tijiao_choices')
        self.third_tijiao_pricediff = wx.Choice(self, -1, choices=tijiao_choices)
        self.third_tijiao_pricediff.SetSelection(0)
        self.third_tijiaoyanchi_label = wx.StaticText(self, label=" 延迟",
                                                      style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_tijiaoyanchi_label.SetFont(self.wordfont)
        self.third_tijiao_label = wx.StaticText(self, label=" 提交  ", style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.third_tijiao_label.SetFont(self.wordfont)
        self.third_tijiaoyanchi_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.third_tijiaoyanchi_time.SetRange(0.0, 1.9)
        self.third_tijiaoyanchi_time.SetValue(0.5)
        self.third_tijiaoyanchi_time.SetIncrement(0.1)
        # self.third_tijiao_miao = wx.StaticText(self, label=" 秒",  style=wx.ALIGN_CENTER)
        # self.third_tijiao_miao.SetFont(self.wordfont)

        self.third_tijiao_sizer.Add(self.third_tijiao_pricediff)
        self.third_tijiao_sizer.Add(self.third_tijiao_label, flag=wx.TOP, border=4)
        self.third_tijiao_sizer.Add(self.third_tijiaoyanchi_label, flag=wx.TOP, border=4)
        self.third_tijiao_sizer.Add(self.third_tijiaoyanchi_time, flag=wx.TOP, border=3)
        # self.third_tijiao_sizer.Add(self.third_tijiao_miao, flag=wx.TOP, border=4)

        self.third_tijiaotime_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.third_tijiaotime_label = wx.StaticText(self, label="11 : 29 : ")
        self.third_tijiaotime_label.SetFont(self.numberfont)
        self.third_tijiao_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20))
        self.third_tijiao_time.SetRange(0, 59)
        self.third_tijiao_time.SetValue(58)
        self.third_tijiao_time.SetIncrement(0.1)
        self.third_forcetijiao_label = wx.StaticText(self, label=" 强制提交 ", style=wx.ALIGN_CENTER)
        self.third_forcetijiao_label.SetFont(self.wordfont)
        self.third_forcetijiao_check = wx.CheckBox(self)

        self.third_tijiaotime_sizer.Add(self.third_tijiaotime_label)
        self.third_tijiaotime_sizer.Add(self.third_tijiao_time)
        self.third_tijiaotime_sizer.Add(self.third_forcetijiao_label)
        self.third_tijiaotime_sizer.Add(self.third_forcetijiao_check, flag=wx.TOP, border=1)
        self.third_chujia_vbox.Add(self.third_jiajia_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_vbox.Add(self.third_tijiao_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_vbox.Add(self.third_tijiaotime_sizer, flag=wx.BOTTOM, border=10)
        self.third_chujia_label_sizer.Add(self.third_chujia_vbox)

        ###功能绑定
        self.Bind(wx.EVT_TEXT, self.Jiajia_time, self.second_jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price, self.second_jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao, self.second_tijiao_pricediff)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time, self.second_tijiaoyanchi_time)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time, self.second_tijiao_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_time2, self.third_jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Jiajia_price2, self.third_jiajia_price)
        self.Bind(wx.EVT_CHOICE, self.Select_tijiao2, self.third_tijiao_pricediff)
        self.Bind(wx.EVT_TEXT, self.Yanchi_time2, self.third_tijiaoyanchi_time)
        self.Bind(wx.EVT_TEXT, self.Tijiao_time2, self.third_tijiao_time)

        self.Bind(wx.EVT_CHECKBOX, self.Smart_autoprice, self.buqiang_checkbox)
        self.Bind(wx.EVT_CHECKBOX, self.Second_forcetijiao, self.second_forcetijiao_check)
        self.Bind(wx.EVT_CHECKBOX, self.Third_forcetijiao, self.third_forcetijiao_check)

        ####动态提交
        ##单枪动态提交
        self.smart_tijiao_label = wx.StaticBox(self, -1, "单枪动态提交")
        self.smart_tijiao_label_sizer = wx.StaticBoxSizer(self.smart_tijiao_label, wx.VERTICAL)
        self.smart_tijiao_label.SetFont(self.titlefont)
        self.smart_tijiao_vsizer = wx.BoxSizer(wx.VERTICAL)

        ##双枪动态提交
        self.smart_tijiao_label2 = wx.StaticBox(self, -1, "第三次出价动态提交")
        self.smart_tijiao_label_sizer2 = wx.StaticBoxSizer(self.smart_tijiao_label2, wx.VERTICAL)
        self.smart_tijiao_label2.SetFont(self.titlefont)
        self.smart_tijiao_vsizer2 = wx.BoxSizer(wx.VERTICAL)
        ##复制出价部分
        ##第二次
        ##出价设置行
        self.secondsmart_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.secondsmart_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                         style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.secondsmart_jiajia_time.SetRange(0, 57)
        self.secondsmart_jiajia_time.SetValue(48)
        self.secondsmart_jiajia_time.SetIncrement(0.1)
        # self.secondsmart_jiajia_time.SetFont(self.numberfont)
        self.secondsmart_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.secondsmart_jiajia_price.SetRange(300, 1500)
        self.secondsmart_jiajia_price.SetValue(700)
        self.secondsmart_jiajia_price.SetIncrement(100)
        self.secondsmart_time_label = wx.StaticText(self, label="11 : 29 : ",
                                                    style=wx.ALIGN_RIGHT)
        self.secondsmart_time_label.SetFont(self.numberfont)
        self.secondsmart_jiahao = wx.StaticText(self, label=' + ', style=wx.ALIGN_CENTER)
        self.secondsmart_jiahao.SetFont(self.wordfont)
        self.secondsmart_jiajia_sizer.Add(self.secondsmart_time_label, wx.LEFT, border=10)
        self.secondsmart_jiajia_sizer.Add(self.secondsmart_jiajia_time)
        self.secondsmart_jiajia_sizer.Add(self.secondsmart_jiahao)
        self.secondsmart_jiajia_sizer.Add(self.secondsmart_jiajia_price)

        self.Bind(wx.EVT_TEXT, self.Smart_Jiajia_time, self.secondsmart_jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Smart_Jiajia_price, self.secondsmart_jiajia_price)


        ##第三次
        ##出价设置行
        self.thirdsmart_jiajia_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.thirdsmart_jiajia_time = wx.SpinCtrlDouble(self, -1, "", size=(52, 20),
                                                        style=wx.ALIGN_CENTER | wx.TEXT_ALIGNMENT_CENTER)
        self.thirdsmart_jiajia_time.SetRange(0, 55)
        self.thirdsmart_jiajia_time.SetValue(48)
        self.thirdsmart_jiajia_time.SetIncrement(0.1)
        self.thirdsmart_jiajia_price = wx.SpinCtrlDouble(self, -1, "", size=(55, 20))
        self.thirdsmart_jiajia_price.SetRange(300, 1500)
        self.thirdsmart_jiajia_price.SetValue(700)
        self.thirdsmart_jiajia_price.SetIncrement(100)
        self.thirdsmart_time_label = wx.StaticText(self, label="11 : 29 : ",
                                                   style=wx.ALIGN_RIGHT)
        self.thirdsmart_time_label.SetFont(self.numberfont)
        self.thirdsmart_jiahao = wx.StaticText(self, label=' + ', style=wx.ALIGN_CENTER)
        self.thirdsmart_jiahao.SetFont(self.wordfont)
        self.thirdsmart_jiajia_sizer.Add(self.thirdsmart_time_label, wx.LEFT, border=10)
        self.thirdsmart_jiajia_sizer.Add(self.thirdsmart_jiajia_time)
        self.thirdsmart_jiajia_sizer.Add(self.thirdsmart_jiahao)
        self.thirdsmart_jiajia_sizer.Add(self.thirdsmart_jiajia_price)

        self.Bind(wx.EVT_TEXT, self.Smart_Jiajia_time2, self.thirdsmart_jiajia_time)
        self.Bind(wx.EVT_TEXT, self.Smart_Jiajia_price2, self.thirdsmart_jiajia_price)

        ##单枪智能提交组件
        self.smart_tijiao_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.smart_tijiao_label = wx.StaticText(self, label='动态提交', style=wx.ALIGN_RIGHT, size=(76, 25))
        self.smart_tijiao_button = wx.Button(self, label='设置', size=(50, 25))
        self.smart_tijiao_hsizer.Add(self.smart_tijiao_label, flag=wx.TOP, border=5)
        self.smart_tijiao_hsizer.Add(self.smart_tijiao_button, flag=wx.LEFT, border=20)
        self.smart_tijiao_button.Bind(wx.EVT_BUTTON, self.Smart_tijiao_button)

        ##双枪智能提交组件 
        self.smart2_tijiao_hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.smart2_tijiao_label = wx.StaticText(self, label='动态提交', style=wx.ALIGN_RIGHT, size=(76, 25))
        self.smart2_tijiao_button = wx.Button(self, label='设置', size=(50, 25))
        self.smart2_tijiao_hsizer.Add(self.smart2_tijiao_label, flag=wx.TOP, border=5)
        self.smart2_tijiao_hsizer.Add(self.smart2_tijiao_button, flag=wx.LEFT, border=20)
        self.smart2_tijiao_button.Bind(wx.EVT_BUTTON, self.Smart_tijiao_button)

        ##单枪组装
        self.smart_tijiao_vsizer.Add(self.smart_tijiao_hsizer, flag=wx.RIGHT, border=60)
        self.smart_tijiao_vsizer.Add(self.secondsmart_jiajia_sizer, flag=wx.BOTTOM, border=12)
        self.smart_tijiao_label_sizer.Add(self.smart_tijiao_vsizer, flag=wx.BOTTOM, border=2)
        ##双枪组装
        self.smart_tijiao_vsizer2.Add(self.smart2_tijiao_hsizer, flag=wx.RIGHT, border=60)
        self.smart_tijiao_vsizer2.Add(self.thirdsmart_jiajia_sizer, flag=wx.BOTTOM, border=12)
        self.smart_tijiao_label_sizer2.Add(self.smart_tijiao_vsizer2, flag=wx.BOTTOM, border=2)

        ##构建组件
        self.strategy_sizer.Add(self.second_chujia_label_sizer, flag=wx.ALL, border=3)
        self.strategy_sizer.Add(self.third_chujia_label_sizer, flag=wx.ALL, border=3)
        self.strategy_sizer.Add(self.smart_tijiao_label_sizer, flag=wx.ALL, border=3)
        self.strategy_sizer.Add(self.smart_tijiao_label_sizer2, flag=wx.ALL, border=3)
        self.strategy_sizer.Add(self.buqiang_label_sizer, flag=wx.ALL, border=3)

        self.strategy_area_vbox.Add(self.choice_strategy, flag=wx.LEFT, border=3)
        self.strategy_area_vbox.Add(self.strategy_sizer)
        self.strategy_area_sizer.Add(self.strategy_area_vbox)
        ##----------------------------------------------------------------------------------
        # ##提示框
        # self.reminder = wx.StaticBox(self, -1, "操作提示")
        # self.reminderbox = wx.StaticBoxSizer(self.reminder, wx.VERTICAL)
        # self.reminderhbox = wx.BoxSizer(wx.HORIZONTAL)
        # self.hotkey_bmp = wx.StaticBitmap(self, -1)
        # self.hotkey_bmp.SetBitmap(wx.Bitmap('hotkey.png'))
        # self.reminderhbox.Add(self.hotkey_bmp, flag=wx.RIGHT, border=40)
        #
        # self.reminderbox.Add(self.reminderhbox, flag=wx.ALL, border=10)
        ##-------------------------------------------------------------------------------------
        #日志框
        # self.infomationfont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        # self.infofont = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        # self.infomation = wx.StaticText(self, label='沪牌一号7月31号模拟拍牌会', pos=(15, 450))
        # self.infomation.SetFont(self.infomationfont)
        #
        # self.infoarea = wx.StaticText(self, label='操作日志：', pos=(10, 475))
        # self.infoarea.SetFont(self.infomationfont)
        #
        # self.infos = []
        # self.infomationfont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        # self.infofont = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        # self.infohbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # self.infohbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # self.infomation = wx.StaticText(self, label='沪牌一号7月31号模拟拍牌会')
        # self.infomation.SetFont(self.infomationfont)
        # self.infohbox1.Add(self.infomation)
        #
        # self.infoarea = wx.StaticText(self, label='操作日志：')
        # self.infoarea.SetFont(self.infomationfont)
        # self.infohbox2.Add(self.infoarea)
        #
        # self.infovbox = wx.BoxSizer(wx.VERTICAL)
        # self.infovbox.Add(self.infohbox1, flag=wx.RIGHT, border=30)
        # self.infovbox.Add(self.infohbox2, flag=wx.RIGHT, border=30)
        # self.infos = []

        ##-------------------------------------------------------------------------------------
        ##将所有sizer组合
        # self.reminderbox.Add(self.remindergrid)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.controlbox, flag=wx.BOTTOM, border=10)
        self.vbox.Add(self.strategy_area_sizer, flag=wx.BOTTOM, border=10)
        # self.vbox.Add(self.reminderbox, flag=wx.BOTTOM, border=10)
        # self.vbox.Add(self.infovbox, flag=wx.BOTTOM, border=10)
        self.SetSizer(self.vbox)

        ###初始化sizer
        #############消息区域
        pub.subscribe(self.change_strategy, 'change strategy')
        pub.subscribe(self.change_userprice, 'change userprice')  # 修改当前用户出价


        #更新日志
        # pub.subscribe(self.update_info, 'update info')


    ## 验证码放大
    def Yanzhengma_scale(self, event):
        if self.yanzhengma_scale.IsChecked():
            set_dick("yanzhengma_scale", True)
            wx.CallAfter(pub.sendMessage, 'update info', action='开启验证码放大')
        else:
            set_dick("yanzhengma_scale", False)
            wx.CallAfter(pub.sendMessage, 'update info', action='关闭验证码放大')

    ## 验证码自动预览
    def Yanzhengma_autoview(self, event):
        if self.yanzhengma_autoview.IsChecked():
            set_dick("auto_query_on", True) #控制开关
        else:
            set_dick("auto_query_on", False)


    ## 国拍与模拟切换
    def webtab(self, event):
        moni_on = get_val('moni_on')
        if moni_on:
            StatusPanel.addto_infos('切换国拍')
            set_val('guopai_on', True)
            set_val('moni_on', False)
            from component.app_thread import GetremotetimeThread
            getremotetimethread = GetremotetimeThread()  ##同步国拍时间
            moni_webframe = get_val('moni_webframe')
            guopai_webframe = get_val('guopai_webframe')
            moni = wx.FindWindowById(moni_webframe)
            guopai = wx.FindWindowById(guopai_webframe)
            if guopai_webframe != -1:
                guopai.Show(True)
                guopai.currentstatusframe.Show(False)
                guopai.init_frame()
                moni.Show(False)
                moni.currentstatusframe.Show(False)
                moni.yanzhengmaframe.Show(False)
                moni.tipframe.Show(False)
            else:
                moni.Show(False)
                moni.currentstatusframe.Show(False)
                moni.yanzhengmaframe.Show(False)
                moni.tipframe.Show(False)
                wx.CallAfter(pub.sendMessage, "open dianxin")
        else:
            StatusPanel.addto_infos('切换模拟')

            set_val('moni_on', True)
            set_val('guopai_on', False)
            moni_webframe = get_val('moni_webframe')
            guopai_webframe = get_val('guopai_webframe')
            moni = wx.FindWindowById(moni_webframe)
            guopai = wx.FindWindowById(guopai_webframe)
            if moni_webframe != -1:
                moni.Show(True)
                # moni.htmlpanel.webview.Reload()
                moni.currentstatusframe.Show(False)
                guopai.Show(False)
                guopai.currentstatusframe.Show(False)
                guopai.yanzhengmaframe.Show(False)
                guopai.tipframe.Show(False)
                moni.init_frame()
            else:
                guopai.Show(False)
                guopai.currentstatusframe.Show(False)
                guopai.yanzhengmaframe.Show(False)
                guopai.tipframe.Show(False)
                wx.CallAfter(pub.sendMessage, "open moni")


    def refreshweb(self, event):
        moni_on = get_val('moni_on')
        if moni_on:
            wx.CallAfter(pub.sendMessage, "moni refresh_web")
        else:
            wx.CallAfter(pub.sendMessage, "guopai refresh_web")

    def onkeylogin(self, event):
        # guopai_on = get_val('guopai_on')
        # if guopai_on:
        #     print("fdssfs")
        #     wx.CallAfter(pub.sendMessage, "onekey_login")
        from component.account_dialog import Account_dialog
        self.dlg = Account_dialog(self, "登录设置")
        print("fdsfs")
        # dlg = Smart_tijiaoDialog()
        self.dlg.Show()
        # dlg.ShowModal()
    
        guopai_on = get_val('guopai_on')
        if guopai_on:
            wx.CallAfter(pub.sendMessage, "onekey_login")
        ##截图
        login_yanzhengma = get_val('login_yanzhengma_relative')

        print("fdsfsdfsfsfdsf")

        img = grab_screen2(region=login_yanzhengma)
        num = get_val('num')
        num = 100
        set_val('num', num+1)
        cv2.imwrite('login_%d.png' %num, img)
        print("fdsfsdfsfsfdsf")

    ###策略设置
    def Choice_strategy(self, event):
        strategy_type = str(self.choice_strategy.GetSelection())
        print('strategy_type', strategy_type)

        self.update_ui(strategy_type)
        set_dick('strategy_type', strategy_type)  ##保存当前用户选择的策略

    ##初始化
    def init_ui(self):
        auto_query_on = get_dick('auto_query_on')
        if auto_query_on:
            self.yanzhengma_autoview.SetValue(True)
        else:
            self.yanzhengma_autoview.SetValue(False)

        yanzhengma_scale = get_dick('yanzhengma_scale')
        if yanzhengma_scale:
            self.yanzhengma_scale.SetValue(True)
        else:
            self.yanzhengma_scale.SetValue(False)
        
        if  not get_val('activate_status'):
            self.webtabButton.Disable()
            self.onkeyloginButton.Disable()
        else:
            self.webtabButton.Enable()
            self.onkeyloginButton.Enable()

        self.init_strategy()
        # self.init_info()


    def  init_strategy(self):
        strategy_type = get_dick('strategy_type')
        self.update_ui(strategy_type)


    #--------------------------------------------
    #日志管理
    '''
    1.切换国拍与模拟
    2.用户修改策略
    '''


    def init_info(self):
        action_infos = get_val('action_infos')
        len_info = len(action_infos)
        if  len_info >= 5:
            self.infos = [action for action in action_infos[-len_info:]]
            self.update_info()
        else:
            new_actions = get_val('new_actions')
            self.infos = [self.create_info(action) for action in new_actions]
            self.update_info()
            print("fdssfsd", self.infos)
            set_val('action_infos', self.infos)


    def draw_text(self, dc, text, pos):
        x1, y1 = pos
        print(x1, y1)
        dc.DrawText(text, x1, y1)

    def update_info(self, action=None):
        if action:
            info = self.create_info(action)
            self.addto_infos(action)
            self.infos.append(info)
            if len(self.infos) >= 7:
                self.infos.pop(0) ##维持6个元素
                ##修改info
            print(self.infos)
        len_info = len(self.infos)
        infotext_pos = get_val('infotext_pos')
        print(infotext_pos)
        print(self.infos)
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.Clear()
        dc.SetFont(self.infofont)

        for i in range(len_info):
            self.draw_text(dc, self.infos[i], infotext_pos[i])


    @staticmethod
    def create_info(action):
        a_time_str = get_val('a_time_str')
        if not a_time_str:
            a_time = get_val('a_time')
            temp = int((a_time - int(a_time)) * 10)
            time_local = time.localtime(a_time)
            a_time_str = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
        info = f'{a_time_str}: {action}'
        return info

    @staticmethod
    def addto_infos(action):
        info = StatusPanel.create_info(action)
        action_infos = get_val('action_infos')
        action_infos.append(info)
        set_val('action_infos', action_infos)
        print(action_infos)
    #--------------------------------------------
    #策略调整
    def update_ui(self, strategy_type):  ##根据不同的出价策略调整界面
        strategy_list = get_dick(strategy_type)
        print('strategy_list', strategy_list)

        if strategy_type == '0':  # 单次
            init_strategy()
            self.choice_strategy.SetSelection(int(strategy_type))
            self.second_jiajia_time.SetValue(strategy_list[1])
            self.second_tijiao_time.SetValue(strategy_list[5])
            self.second_jiajia_price.SetValue(strategy_list[2])
            self.second_tijiaoyanchi_time.SetValue(strategy_list[4])
            if strategy_list[3] == 100:
                self.second_tijiao_pricediff.SetSelection(0)
            elif strategy_list[3] == 200:
                self.second_tijiao_pricediff.SetSelection(1)
            elif strategy_list[3] == 300:
                self.second_tijiao_pricediff.SetSelection(3)
            else:
                self.second_tijiao_pricediff.SetSelection(4)
            self.second_forcetijiao_check.SetValue(strategy_list[6])
            self.buqiang_checkbox.SetValue(strategy_list[7])

            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('second_forcetijiao_on', strategy_list[6])  # 强制提交
            set_val('smart_autoprice', strategy_list[7])  # 强制提交

            if strategy_list[6]:
                self.second_tijiao_time.Enable()
            else:
                self.second_tijiao_time.Disable()

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))
            set_val('second_real_time2', gettime(second_time2))
            ####刷新界面排版
            self.strategy_sizer.Show(self.second_chujia_label_sizer)
            self.strategy_sizer.Hide(self.third_chujia_label_sizer)
            self.strategy_sizer.Show(self.buqiang_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer2)
            self.Layout()

        elif strategy_type == '1':  # 双枪
            init_strategy()
            self.choice_strategy.SetSelection(int(strategy_type))
            self.second_jiajia_time.SetValue(strategy_list[1])
            self.second_jiajia_price.SetValue(strategy_list[2])
            if strategy_list[3] == 100:
                self.second_tijiao_pricediff.SetSelection(0)
            elif strategy_list[3] == 200:
                self.second_tijiao_pricediff.SetSelection(1)
            elif strategy_list[3] == 300:
                self.second_tijiao_pricediff.SetSelection(2)
            else:
                self.second_tijiao_pricediff.SetSelection(3)
            self.second_tijiaoyanchi_time.SetValue(strategy_list[4])
            self.second_tijiao_time.SetValue(strategy_list[5])
            self.second_forcetijiao_check.SetValue(strategy_list[6])
            if strategy_list[6]:
                self.second_tijiao_time.Enable()
            else:
                self.second_tijiao_time.Disable()

            self.third_jiajia_time.SetValue(strategy_list[8])
            self.third_jiajia_price.SetValue(strategy_list[9])
            if strategy_list[10] == 100:
                self.third_tijiao_pricediff.SetSelection(0)
            elif strategy_list[10] == 200:
                self.third_tijiao_pricediff.SetSelection(1)
            elif strategy_list[10] == 300:
                self.third_tijiao_pricediff.SetSelection(2)
            else:
                self.third_tijiao_pricediff.SetSelection(3)
            self.third_tijiaoyanchi_time.SetValue(strategy_list[11])
            self.third_tijiao_time.SetValue(strategy_list[12])
            self.third_forcetijiao_check.SetValue(strategy_list[13])
            if strategy_list[13]:
                self.third_tijiao_time.Enable()
            else:
                self.third_tijiao_time.Disable()

            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('one_forcetijiao_on', strategy_list[6])

            set_val('second_time1', strategy_list[8])  # 第二次次出价加价
            set_val('second_diff', strategy_list[9])  # 第二次加价幅度
            set_val('second_advance', strategy_list[10])  # 第二次出价提交提前量
            set_val('second_delay', strategy_list[11])  # 第二次出价延迟
            set_val('second_time2', strategy_list[12])  # 第二次出价提交
            set_val('second_forcetijiao_on', strategy_list[13])

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            second_time2 = get_val('second_time2')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))
            set_val('second_real_time2', gettime(second_time2))

            ####刷新界面排版
            self.strategy_sizer.Show(self.second_chujia_label_sizer)
            self.strategy_sizer.Show(self.third_chujia_label_sizer)
            self.strategy_sizer.Hide(self.buqiang_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer2)

            self.Layout()

        elif strategy_type == '2':  # 单枪动态提交
            init_strategy()
            self.choice_strategy.SetSelection(int(strategy_type))
            self.secondsmart_jiajia_time.SetValue(strategy_list[1])
            self.secondsmart_jiajia_price.SetValue(strategy_list[2])
            self.buqiang_checkbox.SetValue(strategy_list[7])

            # '''
            #     (3)单枪动态提交  依次为 0: strategy_type 1: one_time1  2: one_diff
            #                                            3: one_advance_smart1  4: one_delay_smart1   5: one_time2_smart1
            #                                            6: one_advance_smart2  7: one_delay_smart2   8: one_time2_smart2
            #                                            9: one_advance_smart3  10: one_delay_smart3  11: one_time2_smart3
            #                                            12: one_time2_smart
            # '''

            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('smart_autoprice', strategy_list[7])  # 强制提交

            set_val('one_advance_smart1', strategy_list[14])
            set_val('one_delay_smart1', strategy_list[15])
            set_val('one_time2_smart1', strategy_list[16])
            set_val('one_advance_smart2', strategy_list[17])
            set_val('one_delay_smart2', strategy_list[18])
            set_val('one_time2_smart2', strategy_list[19])
            set_val('one_advance_smart3', strategy_list[20])
            set_val('one_delay_smart3', strategy_list[21])
            set_val('one_time2_smart3', strategy_list[22])
            set_val('one_time2_smart', strategy_list[23])

            set_val('one_real_time1', gettime(strategy_list[1]))  ##第一次出价时间戳
            set_val('one_realtime2_smart1', gettime(strategy_list[16]))
            set_val('one_realtime2_smart2', gettime(strategy_list[19]))
            set_val('one_realtime2_smart3', gettime(strategy_list[22]))
            set_val('one_realtime2_smart', gettime(strategy_list[23]))


            ####刷新界面排版
            self.strategy_sizer.Hide(self.second_chujia_label_sizer)
            self.strategy_sizer.Hide(self.third_chujia_label_sizer)
            self.strategy_sizer.Show(self.smart_tijiao_label_sizer)
            self.strategy_sizer.Show(self.buqiang_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer2)

            self.Layout()

        elif strategy_type == '3':  # 双枪动态提交
            init_strategy()

            self.choice_strategy.SetSelection(int(strategy_type))
            self.second_jiajia_time.SetValue(strategy_list[1])
            self.second_jiajia_price.SetValue(strategy_list[2])
            if strategy_list[3] == 100:
                self.second_tijiao_pricediff.SetSelection(0)
            elif strategy_list[3] == 200:
                self.second_tijiao_pricediff.SetSelection(1)
            elif strategy_list[3] == 300:
                self.second_tijiao_pricediff.SetSelection(2)
            else:
                self.second_tijiao_pricediff.SetSelection(3)
            self.second_tijiaoyanchi_time.SetValue(strategy_list[4])
            self.second_tijiao_time.SetValue(strategy_list[5])
            self.second_forcetijiao_check.SetValue(strategy_list[6])
            if strategy_list[6]:
                self.second_tijiao_time.Enable()
            else:
                self.second_tijiao_time.Disable()

            self.thirdsmart_jiajia_time.SetValue(strategy_list[8])
            self.thirdsmart_jiajia_price.SetValue(strategy_list[9])

            # '''
            # (4)双枪动态提交  依次为 0: strategy_type 1: one_time1  2: one_diff  3: one_advance 4: one_delay 5: one_time2
            #                                        6: one_forcetijiao_on   7: second_time1  8: second_diff
            #                                        9: one_advance_smart1  10: one_delay_smart1   11: one_time2_smart1
            #                                        12: one_advance_smart2  13: one_delay_smart2   14: one_time2_smart2
            #                                        15: one_advance_smart3  16: one_delay_smart3  17: one_time2_smart3
            #                                        18: one_time2_smart
            #
            #
            # '''
            set_val('one_time1', strategy_list[1])  # 第一次出价加价
            set_val('one_diff', strategy_list[2])  # 第一次加价幅度
            set_val('one_advance', strategy_list[3])  # 第一次提交提前量
            set_val('one_delay', strategy_list[4])  # 第一次延迟
            set_val('one_time2', strategy_list[5])  # 第一次出价提交
            set_val('one_forcetijiao_on', strategy_list[6])

            set_val('second_time1', strategy_list[8])  # 第二次次出价加价
            set_val('second_diff', strategy_list[9])  # 第二次加价幅度

            set_val('one_advance_smart1', strategy_list[14])
            set_val('one_delay_smart1', strategy_list[15])
            set_val('one_time2_smart1', strategy_list[16])
            set_val('one_advance_smart2', strategy_list[17])
            set_val('one_delay_smart2', strategy_list[18])
            set_val('one_time2_smart2', strategy_list[19])
            set_val('one_advance_smart3', strategy_list[20])
            set_val('one_delay_smart3', strategy_list[21])
            set_val('one_time2_smart3', strategy_list[22])
            set_val('one_time2_smart', strategy_list[23])

            one_time1 = get_val('one_time1')
            one_time2 = get_val('one_time2')
            second_time1 = get_val('second_time1')
            set_val('one_real_time1', gettime(one_time1))
            set_val('one_real_time2', gettime(one_time2))
            set_val('second_real_time1', gettime(second_time1))

            set_val('one_realtime2_smart1', gettime(strategy_list[16]))
            set_val('one_realtime2_smart2', gettime(strategy_list[19]))
            set_val('one_realtime2_smart3', gettime(strategy_list[22]))
            set_val('one_realtime2_smart', gettime(strategy_list[23]))

            ####刷新界面排版
            self.strategy_sizer.Show(self.second_chujia_label_sizer)
            self.strategy_sizer.Hide(self.third_chujia_label_sizer)
            self.strategy_sizer.Hide(self.smart_tijiao_label_sizer)
            self.strategy_sizer.Show(self.smart_tijiao_label_sizer2)
            self.strategy_sizer.Hide(self.buqiang_label_sizer)
            self.Layout()

    ###需要进一步扩展 调整策略设置后需要 修正templist
    def update_strategy(self):
        #生成日志
        self.update_info('修改策略')


        strategy_type = str(self.choice_strategy.GetSelection())
        advance_list = [100, 200, 300, 0]
        print(strategy_type)
        if strategy_type == '0':
            templist = get_dick(strategy_type)
            templist[0] = strategy_type
            templist[1] = self.second_jiajia_time.GetValue()
            templist[2] = int(self.second_jiajia_price.GetValue())
            templist[3] = advance_list[self.second_tijiao_pricediff.GetSelection()]
            templist[4] = self.second_tijiaoyanchi_time.GetValue()
            templist[5] = self.second_tijiao_time.GetValue()
            templist[6] = self.second_forcetijiao_check.IsChecked()
            templist[7] = self.buqiang_checkbox.IsChecked()  #补枪
            print(templist)
            set_dick(strategy_type, templist)
            strategy_choices = get_val('strategy_choices')
            init_description()
            # '{0}秒加{1} 提前{2}延迟{3}秒 强制{4}秒'.format(templist[1], templist[2], templist[3], templist[4], templist[5]))
        elif strategy_type == '1':
            templist = get_dick(strategy_type)
            templist[0] = strategy_type
            templist[1] = self.second_jiajia_time.GetValue()
            templist[2] = int(self.second_jiajia_price.GetValue())
            templist[3] = advance_list[self.second_tijiao_pricediff.GetSelection()]
            templist[4] = self.second_tijiaoyanchi_time.GetValue()
            templist[5] = self.second_tijiao_time.GetValue()
            templist[6] = self.second_forcetijiao_check.IsChecked()
            templist[8] = self.third_jiajia_time.GetValue()
            templist[9] = int(self.third_jiajia_price.GetValue())
            templist[10] = advance_list[self.third_tijiao_pricediff.GetSelection()]
            templist[11] = self.third_tijiaoyanchi_time.GetValue()
            templist[12] = self.third_tijiao_time.GetValue()
            templist[13] = self.third_forcetijiao_check.IsChecked()
            strategy_choices = get_val('strategy_choices')
            init_description()
            set_dick(strategy_type, templist)
        elif strategy_type == '2':
            templist = get_dick(strategy_type)
            templist[0] = strategy_type
            templist[1] = self.second_jiajia_time.GetValue()
            templist[2] = int(self.second_jiajia_price.GetValue())
            templist[7] = self.buqiang_checkbox.IsChecked()  #补枪
            strategy_choices = get_val('strategy_choices')
            init_description()
            set_dick(strategy_type, templist)
        elif strategy_type == '3':
            templist = get_dick(strategy_type)
            templist[0] = strategy_type
            templist[1] = self.second_jiajia_time.GetValue()
            templist[2] = int(self.second_jiajia_price.GetValue())
            templist[3] = advance_list[self.second_tijiao_pricediff.GetSelection()]
            templist[4] = self.second_tijiaoyanchi_time.GetValue()
            templist[5] = self.second_tijiao_time.GetValue()
            templist[6] = self.second_forcetijiao_check.IsChecked()
            templist[8] = self.thirdsmart_jiajia_time.GetValue()  ##智能出价部分
            templist[9] = int(self.thirdsmart_jiajia_price.GetValue())  ##智能出价部分
            strategy_choices = get_val('strategy_choices')
            init_description()
            set_dick(strategy_type, templist)
            a = get_strategy_dick()
            print(a)

    ##导出跳价
    def priceview(self, event):
        price_list = get_val('price_list')
        with open('price_list.txt', 'w') as price_file:
            for index, price in enumerate(price_list):
                text = "{0}秒： {1}".format(index, price)
                price_file.write(text)
                price_file.write('\n')

    ##刷新定位
    def posautoajust(self, event):
        findpos()

    def Confirmchoice(self, event):
        con = self.confirm_choice.GetSelection()
        if con == 0:
            set_dick('enter_on', False)
        elif con == 1:
            set_dick('enter_on', True)

    #######
    def change_strategy(self):
        pass

    def change_userprice(self):
        pass

    ##-------------------------------------------------------------------------
    ##策略设置功能区
    def Jiajia_time(self, event):
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        tem = self.second_jiajia_time.GetValue()
        timelist = get_val('timelist')
        if int(tem * 10) in timelist and tem <= one_time2 - 1:
            one_time1 = tem
            set_val('one_time1', float(one_time1))
            set_val('one_real_time1', gettime(float(one_time1)))  # 计算得到的时间戳
            one_real_time1 = get_val('one_real_time1')
            print(one_time1, one_real_time1)
            self.update_strategy()
        else:
            self.second_jiajia_time.SetValue(one_time1)

    def Jiajia_time2(self, event):
        second_time1 = get_val('second_time1')
        second_time2 = get_val("second_time2")
        one_time2 = get_val('one_time2')
        tem = self.third_jiajia_time.GetValue()
        timelist = get_val('timelist')
        if int(tem * 10) in timelist and tem >= one_time2 + 1 and tem <= second_time2 - 1: #只有策略2存在
            second_time1 = tem
            set_val('second_time1', float(tem))
            set_val('second_real_time1', gettime(second_time1))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.third_jiajia_time.SetValue(second_time1)


    def Jiajia_price(self, event):
        one_diff = get_val('one_diff')
        tem = int(self.second_jiajia_price.GetValue())
        pricelist = get_val('pricelist')
        if tem in pricelist:
            set_val('one_diff', int(tem))
            self.update_strategy()
        else:
            self.second_jiajia_price.SetValue(one_diff)

    def Jiajia_price2(self, event):
        second_diff = get_val('second_diff')
        tem = int(self.third_jiajia_price.GetValue())
        pricelist = get_val('pricelist')
        if tem in pricelist:
            set_val('second_diff', int(tem))
            self.update_strategy()
        else:
            self.third_jiajia_price.SetValue(second_diff)

    def Select_tijiao(self, event):
        select = self.second_tijiao_pricediff.GetString(self.second_tijiao_pricediff.GetSelection())
        if select == u"提前100":
            set_val('one_advance', 100)
        elif select == u"提前200":
            set_val('one_advance', 200)
        elif select == u"提前300":
            set_val('one_advance', 300)
        else:
            set_val('one_advance', 0)
        self.update_strategy()

    def Select_tijiao2(self, event):
        select = self.third_tijiao_pricediff.GetString(self.third_tijiao_pricediff.GetSelection())
        if select == u"提前100":
            set_val('second_advance', 100)
        elif select == u"提前200":
            set_val('second_advance', 200)
        elif select == u"提前300":
            set_val('one_advance', 300)
        else:
            set_val('second_advance', 0)
        self.update_strategy()

    def Yanchi_time(self, event):
        one_delay = get_val('one_delay')
        tem = self.second_tijiaoyanchi_time.GetValue()
        yanchilist = get_val('yanchilist')
        if int(tem * 10) in yanchilist:
            set_val('one_delay', float(tem))
            self.update_strategy()
        else:
            self.second_tijiaoyanchi_time.SetValue(one_delay)

    def Yanchi_time2(self, event):
        second_delay = get_val('second_delay')
        tem = self.third_tijiaoyanchi_time.GetValue()
        yanchilist = get_val('yanchilist')
        if int(tem * 10) in yanchilist:
            set_val('second_delay', float(tem))
            self.update_strategy()
        else:
            self.third_tijiaoyanchi_time.SetValue(second_delay)

    def Tijiao_time(self, event):
        one_time1 = get_val('one_time1')
        one_time2 = get_val('one_time2')
        second_time1 = get_val('second_time1')
        tem = self.second_tijiao_time.GetValue()
        timelist = get_val('timelist')
        strategy_type = get_dick('strategy_type')
        if strategy_type == '0':
            if int(tem * 10) in timelist:
                one_time2 = tem
                set_val('one_time2', float(one_time2))
                set_val('one_real_time2', gettime(one_time2))  # 计算得到的时间戳
                self.update_strategy()
            else:
                self.second_tijiao_time.SetValue(one_time2)
        elif strategy_type == '1' or strategy_type == '3':
            if int(tem * 10) in timelist and tem >= one_time1 + 1 and tem <= second_time1 - 1:
                print('sssfdf')

                one_time2 = tem
                set_val('one_time2', float(one_time2))
                set_val('one_real_time2', gettime(one_time2))  # 计算得到的时间戳
                self.update_strategy()
            else:
                self.second_tijiao_time.SetValue(one_time2)

    def Tijiao_time2(self, event):
        second_time2 = get_val('second_time2')
        second_time1 = get_val('second_time1')
        tem = self.third_tijiao_time.GetValue()
        timelist = get_val('timelist')
        if int(tem * 10) in timelist and tem >= second_time1 + 1:
            print(second_time1, tem)
            second_time2 = tem
            set_val('second_time2', float(tem))
            set_val('second_real_time2', gettime(second_time2))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.third_tijiao_time.SetValue(second_time2)

    def Second_forcetijiao(self, event):
        if self.second_forcetijiao_check.IsChecked():
            set_val('one_forcetijiao_on', True)
            self.second_tijiao_time.Enable()
        else:
            set_val('one_forcetijiao_on', False)
            self.second_tijiao_time.Disable()
        self.update_strategy()

    def Third_forcetijiao(self, event):
        if self.third_forcetijiao_check.IsChecked():
            set_val('second_forcetijiao_on', True)
            self.third_tijiao_time.Enable()
        else:
            set_val('second_forcetijiao_on', False)
            self.third_tijiao_time.Disable()
        self.update_strategy()

    ##智能出价部分
    def Smart_Jiajia_time(self, event):
        one_time1 = get_val('one_time1')
        one_time2_smart1 = get_val('one_time2_smart1')
        tem = self.secondsmart_jiajia_time.GetValue()
        timelist = get_val('timelist')
        if int(tem * 10) in timelist and tem <= one_time2_smart1 - 1:
            one_time1 = tem
            set_val('one_time1', float(one_time1))
            set_val('one_real_time1', gettime(one_time1))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.secondsmart_jiajia_time.SetValue(one_time1)

    def Smart_Jiajia_time2(self, event):
        second_time1 = get_val('second_time1')
        one_time2 = get_val('one_time2')
        tem = self.thirdsmart_jiajia_time.GetValue()
        timelist = get_val('timelist')
        one_time2_smart1 = get_val('one_time2_smart1')
        if int(tem * 10) in timelist and tem >= one_time2 + 1 and tem <= one_time2_smart1 - 1:
            second_time1 = tem
            set_val('second_time1', float(second_time1))
            set_val('second_real_time1', gettime(second_time1))  # 计算得到的时间戳
            self.update_strategy()
        else:
            self.thirdsmart_jiajia_time.SetValue(second_time1)

    def Smart_Jiajia_price(self, event):
        one_diff = get_val('one_diff')
        tem = int(self.secondsmart_jiajia_price.GetValue())
        pricelist = get_val('pricelist')
        if tem in pricelist:
            set_val('one_diff', tem)
            self.update_strategy()
        else:
            self.secondsmart_jiajia_price.SetValue(one_diff)

    def Smart_Jiajia_price2(self, event):
        second_diff = get_val('second_diff')
        tem = int(self.thirdsmart_jiajia_price.GetValue())
        pricelist = get_val('pricelist')
        if tem in pricelist:
            set_val('second_diff', tem)
            self.update_strategy()
        else:
            self.thirdsmart_jiajia_price.SetValue(second_diff)

    # ----------------------------------------------------------
    ##智能补枪
    def Smart_autoprice(self, event):
        if self.buqiang_checkbox.IsChecked():
            set_val('smart_autoprice', True)
        else:
            set_val('smart_autoprice', False)
        self.update_strategy()

    ##单枪动态提交
    def Smart_tijiao_button(self, event):
        from component.smartprice_dialog import Smart_tijiaoDialog
        self.dlg = Smart_tijiaoDialog(self, "动态提交设置")
        # dlg = Smart_tijiaoDialog()
        self.dlg.Show()
        # dlg.ShowModal()


##-------------------------------------------------------------------------
class TestPanel(wx.Panel):
    def __init__(self, parent):
        super(TestPanel, self).__init__(parent=parent)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.timelabel = wx.StaticText(self, label='时间设置')
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.button1 = wx.Button(self, label='+1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_second, self.button1)
        self.button2 = wx.Button(self, label='-1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_second, self.button2)
        self.button3 = wx.Button(self, label='+0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Add_time, self.button3)
        self.button4 = wx.Button(self, label='-0.1s', size=(35, 25))
        self.Bind(wx.EVT_BUTTON, self.Minus_time, self.button4)

        self.hbox1.Add(self.timelabel, flag=wx.TOP | wx.LEFT, border=4)
        self.hbox1.Add(self.button1, flag=wx.LEFT, border=4)
        self.hbox1.Add(self.button2)
        self.hbox1.Add(self.button3)
        self.hbox1.Add(self.button4)

        self.fasttimesetlabel = wx.StaticText(self, label='快捷时间设置')
        self.fast_timeset = wx.SpinCtrl(self, -1, "", size=(62, 25))
        self.fast_timeset.SetRange(0, 59)
        self.fast_timeset.SetValue(0)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox2.Add(self.fasttimesetlabel)
        self.hbox2.Add(self.fast_timeset)
        self.fast_timeset.Bind(wx.EVT_TEXT, self.Fast_timeset)

        # 时间区
        self.autotime = wx.CheckBox(self, -1, label=u'自动时间同步')  # 开启时间显示
        self.Bind(wx.EVT_CHECKBOX, self.autotime_set, self.autotime)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox3.Add(self.autotime)

        self.vbox.Add(self.hbox1, flag=wx.TOP, border=300)
        self.vbox.Add(self.hbox2, flag=wx.TOP, border=5)
        self.vbox.Add(self.hbox3, flag=wx.TOP, border=5)
        self.SetSizer(self.vbox)

    def autotime_set(self, event):
        timeSelected = event.GetEventObject()
        if timeSelected.IsChecked():
            set_val('autotime_on', True)
        else:
            set_val('autotime_on', False)

    ##时间调整
    def Add_time(self, event):
        a_time = get_val('a_time')
        set_val('a_time', a_time + 0.1)

    def Minus_time(self, event):
        a_time = get_val('a_time')
        set_val('a_time', a_time + 0.1)

    def Add_second(self, event):
        a_time = get_val('a_time')
        set_val('a_time', a_time + 1)

    def Minus_second(self, event):
        a_time = get_val('a_time')
        set_val('a_time', a_time - 1)

    def Fast_timeset(self, event):
        second = self.fast_timeset.GetValue()
        print(second)
        set_val('a_time', gettime(second))  # 计算得到的时间戳

    ##初始化
    def init_ui(self):
        autotime_on = get_val('autotime_on')
        if autotime_on:
            self.autotime.SetValue(True)
        else:
            self.autotime.SetValue(False)


class AdvancePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.titlefont = wx.Font(13, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        self.confirm_label = wx.StaticText(self, label=u"登录界面按F7可以一键登录", pos=(25, 50))

        self.account = wx.StaticText(self, label=u"标书号", pos=(25, 100), size=(25,50))
        self.password = wx.StaticText(self, label=u"标书密码", pos=(25, 150), size=(25,50))
        self.idnumber = wx.StaticText(self, label=u"身份证号", pos=(25, 200), size=(25,50))

        self.accountText = wx.TextCtrl(self, -1, size=(150, 25), pos = (60, 100),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)

        self.passwordText = wx.TextCtrl(self, -1, size=(150, 25), pos = (60, 150),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)

        self.idnumberText = wx.TextCtrl(self, -1, size=(150, 25), pos = (60, 200),
                                    style=wx.TE_CENTER | wx.TE_PROCESS_ENTER)

        self.savebtn = wx.Button(self, label='保存', pos=(150, 240), size=(62, 25))

        self.savebtn.Bind(wx.EVT_BUTTON, self.Save)


    def Save(self, event):
        bidnumber = self.accountText.GetValue()
        bidpassword = self.passwordText.GetValue()
        idcard = self.idnumberText.GetValue()

        bidnumber_js = "document.getElementById('bidnumber').value = '{0}';".format(bidnumber)
        bidpassword_js = "document.getElementById('bidpassword').value = '{0}';".format(bidpassword)
        idcard_js = "document.getElementById('idcard').value = '{0}';".format(idcard)
        set_val('bidnumber_js', bidnumber_js)
        set_val('bidpassword_js', bidpassword_js)
        set_val('idcard_js', idcard_js)


class OperationPanel(wx.Panel):
    def __init__(self, parent, tablabel):  # name:窗口显示名称
        operationpanel_pos = get_val('operationpanel_pos')
        operationpanel_size = get_val('operationpanel_size')
        wx.Panel.__init__(self, parent=parent, size=operationpanel_size, pos=operationpanel_pos)

        paishou = get_val('paishou')  #拍手模式
        test = get_val('test')  #测试模式
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.SetBackgroundColour('white')

        if not paishou:
            self.notebook = wx.Notebook(self)
            self.status_tab = StatusPanel(self.notebook, tablabel)  # notebook作为父类
            # self.advance_tab = AdvancePanel(self.notebook)
            if not test:
                self.notebook.AddPage(self.status_tab, "常规功能")
                # self.notebook.AddPage(self.advance_tab, "高级功能")
            else:
                self.notebook.AddPage(self.status_tab, "常规功能")
                # self.notebook.AddPage(self.advance_tab, "高级功能")
                self.test_tab = TestPanel(self.notebook)
                self.notebook.AddPage(self.test_tab, "测试功能")
            sizer.Add(self.notebook, 1)
        else:
            self.paishou_panel = PaishouPanel(self, tablabel)
            sizer.Add(self.paishou_panel, 1)


        self.SetSizer(sizer)
        self.Layout()
        self.init_ui()  ## 读取配置文件后初始化

    def init_ui(self):
        if  get_val('paishou'):
            self.paishou_panel.init_ui()
        else:
            self.status_tab.init_ui()
        if get_val('test'):
            self.test_tab.init_ui()
