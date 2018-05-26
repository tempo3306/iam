# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 13:58
'''
from component.staticmethod import *
from component.OperationFrame import OperationPanel
import wx.html2 as webview
from wx.lib.buttons import GenButton as wxButton
from component.imgcut import  timeset
from component.YanzhengmaFrame import YanzhengmaFrame
from component.imgcut import cut_pic, find_yan_confirm

from component.variable import init_pos, get_val, set_val, get_dick, set_dick
import logging
logger = logging.getLogger()

class ButtonPanel(wx.Panel):
    def __init__(self, parent, webstatus_label, moni):
        size = get_val('buttonpanel_size')
        pos = get_val('buttonpanel_pos')
        wx.Panel.__init__(self, parent, size=size, pos=pos)
        self.parent = parent
        self.timefont = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.statusfont = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        ##时间同步功能
        if not moni:
            self.remotetime_button = wxButton(self, label='同步服务器时间', size=(90, 25), pos=(698, 2))
            self.remotetime_button.SetBackgroundColour("#ACD6ff")
            self.remotetime_button.Bind(wx.EVT_BUTTON, self.getremotetime)

        self.webtime_button = wxButton(self, label='同步网页时间', size=(90, 25), pos=(790, 2))
        self.webtime_button.SetBackgroundColour("#ACD6ff")
        self.SetBackgroundColour("#ACD6ff")
        self.webtime_button.Bind(wx.EVT_BUTTON, self.timeautoajust)

        if not moni:
            guopai_dianxin = get_val('guopai_dianxin')
            if guopai_dianxin:
                urlchange_dianxin_label = get_val('urlchange_dianxin_label')
                self.urlchange_button = wxButton(self, label=urlchange_dianxin_label, pos=(606, 2), size=(90, 25))
                self.urlchange_button.Bind(wx.EVT_BUTTON, self.urlchange)
                self.urlchange_button.SetBackgroundColour("#ACD6ff")
            else:
                urlchange_nodianxin_label = get_val('urlchange_nodianxin_label')
                self.urlchange_button = wxButton(self, label=urlchange_nodianxin_label, pos=(606, 2), size=(90, 25))
                self.urlchange_button.Bind(wx.EVT_BUTTON, self.urlchange)
                self.urlchange_button.SetBackgroundColour("#ACD6ff")

        self.webstatus = wx.StaticText(self, label=webstatus_label, pos=(10, 2), size=(120, 30),
                                       )
        self.webstatus.SetFont(self.statusfont)
        # self.webstatus.SetBackgroundColour((0, 0, 150))
        self.webstatus.SetForegroundColour((255, 255, 255))

        # self.refresh_web = wxButton(self, label='刷新界面', size=(80, 25), pos=(25, 2), style=wx.BORDER_NONE)
        # self.refresh_web.SetBackgroundColour("#ACD6ff")

        self.autotime_timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.autotime_set_timer, self.autotime_timer)  # 绑定一个定时器事件
        self.autotime_timer.Start(1000)  # 设定时间间隔

        # 没边框按钮
        # from wx.lib.buttons import GenButton as wxButton
        # tmpButton = wxButton(parent, id, u'删除学生', pos=(10, 10), size=(100, 30), style=wx.BORDER_NONE)
        # tmpButton.SetBackgroundColour("#ff0000")
        # tmpButton.SetForegroundColour("#ffffff")



    def Modify(self):  # 更新
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        moni_on = get_val('moni_on')
        a_time = get_val('a_time')
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
        # st="%s:%s:%s"%(b_time[0],b_time[1],b_time[2])
        st = '国拍时间：%s' % st
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(self.timefont)
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)


    def autotime_set_timer(self, event):
        autotime_on = get_val('autotime_on')
        moni_on = get_val('moni_on')
        test = get_val('test')
        if not test and moni_on:
            self.timeautoajust(event)
        elif test and autotime_on:
            self.timeautoajust(event)



    ## 获取服务器时间
    def getremotetime(self, event):
        from component.app_thread import GetremotetimeThread
        getremotetimethread = GetremotetimeThread()

    ## 同步本地时间
    def timeautoajust(self, event):
        guopai_on = get_val('guopai_on')
        moni_on = get_val('moni_on')
        imgpos_currenttime = get_val('imgpos_currenttime')
        timeset(guopai_on, moni_on, imgpos_currenttime, 'maindata.xml')  # 调用时间同步

    def urlchange(self, event):
        guopai_dianxin = get_val('guopai_dianxin')
        urlchange_dianxin_label = get_val('urlchange_dianxin_label')
        urlchange_nodianxin_label = get_val('urlchange_nodianxin_label')
        if guopai_dianxin:
            self.urlchange_button.SetLabel(urlchange_dianxin_label)
            set_val('guopai_dianxin', False)
            url_nodianxin = get_val('url_nodianxin')
            print(url_nodianxin, 'url_nodianxin')
            self.parent.htmlpanel.webview.LoadURL(url_nodianxin)
            nodianxin_webstatus_label = get_val('nodianxin_webstatus_label')
            self.webstatus.SetLabel(nodianxin_webstatus_label)
        else:
            self.urlchange_button.SetLabel(urlchange_nodianxin_label)
            set_val('guopai_dianxin', True)
            url_dianxin = get_val('url_dianxin')
            print(url_dianxin)
            self.parent.htmlpanel.webview.LoadURL(url_dianxin)
            dianxin_webstatus_label = get_val('dianxin_webstatus_label')
            self.webstatus.SetLabel(dianxin_webstatus_label)

    #
    # def OnKeyDown(self, event):
    #     # 按键时相应代码
    #     # 	event.ControlDown
    #     kc = event.GetKeyCode()
    #     import win32gui
    #     if 32 <= kc <= 126:
    #         win32gui.MessageBox(0, "test,ok!", 'test', 0)
    #         print(kc)
    #     if event.AltDown():
    #         print('ff', kc)


class HtmlPanel(wx.Panel):
    def __init__(self, parent, moni):
        htmlpanel_size = get_val('htmlpanel_size')
        htmlpanel_pos = get_val('htmlpanel_pos')
        wx.Panel.__init__(self, parent, size=htmlpanel_size, pos=htmlpanel_pos, style=wx.BORDER_NONE)
        self.frame = self.GetTopLevelParent()
        self.titleBase = self.frame.GetTitle()
        htmlsize = get_val('htmlsize')
        webview_pos = get_val('webview_pos')
        self.webview = webview.WebView.New(self, size=htmlsize, pos=webview_pos,
                                           style=wx.BORDER_NONE)
        self.webview.EnableContextMenu(False)
        url_moni = get_val('url_moni')
        url_dianxin = get_val('url_dianxin')
        url_nodianxin = get_val('url_nodianxin')
        guopai_dianxin = get_val('guopai_dianxin')
        if moni:
            print("fsdfsfsfdsfsf")
            self.webview.LoadURL(url_moni)
        elif guopai_dianxin:
            self.webview.LoadURL(url_dianxin)
            print("352", url_dianxin)
        else:
            self.webview.LoadURL(url_nodianxin)
            print("Jfsd", url_nodianxin)



class BottomeStatusbarPanel(wx.Panel):
    def __init__(self, parent, moni):
        bottomestatusbarpanel_size = get_val('bottomestatusbarpanel_size')
        bottomestatusbarpanel_pos = get_val('bottomestatusbarpanel_pos')
        wx.Panel.__init__(self, parent, size=bottomestatusbarpanel_size, pos=bottomestatusbarpanel_pos,
                          style=wx.BORDER_NONE)

        self.textfont = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)


        self.registered_bitmap = wx.Bitmap('icons/registered.png')
        self.unregistered_bitmap = wx.Bitmap('icons/unregistered.png')
        # self.slow_bitmap = wx.Bitmap('icons/slow.png')
        self.medium_bitmap = wx.Bitmap('icons/medium.png')
        # self.quick_bitmap = wx.Bitmap('icons/quick.png')
        # self.veryquick_bitmap = wx.Bitmap('icons/veryquick.png')



    def Modify(self):  # 更新
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  ##保存刷新不闪烁
        dc.Clear()
        register_label = get_val("register_label")
        dc.SetFont(self.textfont)
        tw, th = dc.GetTextExtent(register_label)
        dc.DrawText(register_label, 35, (h) / 2 - th / 2)
        dc.DrawBitmap(self.registered_bitmap, 2, 0, True)

        netspeed_label = get_val("netspeed_label")
        dc.SetFont(self.textfont)
        tw, th = dc.GetTextExtent(netspeed_label)
        dc.DrawText(netspeed_label, 806, (h) / 2 - th / 2)
        dc.DrawBitmap(self.medium_bitmap, 850, -3, True)

        strategy_label = get_val('strategy_label')
        strategy_name = get_val('strategy_name')
        strategy_description = get_dick('strategy_description')
        text = "{0}  {1}         {2}".format(strategy_label, strategy_name, strategy_description)
        dc.SetFont(self.textfont)
        tw, th = dc.GetTextExtent(text)
        dc.DrawText(text, 270, (h) / 2 - th / 2)


class CurrentStatusFrame(wx.Frame):
    def __init__(self, parent):
        self.parent = parent
        x, y = parent.Position
        x0, y0 = get_val('CurrentStatusFramePos')
        CurrentStatusFrameSize = get_val('CurrentStatusFrameSize')
        super(CurrentStatusFrame, self).__init__(parent,  size=CurrentStatusFrameSize, pos=(x+x0, y+y0),
                                        style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT | wx.BORDER_NONE)
        self.currentstatuspanel = CurrentStatusPanel(self)

        # self.Bind(wx.EVT_ACTIVATE, self.print)
        self.Disable()




class CurrentStatusPanel(wx.Panel):
    def __init__(self, parent):
        CurrentStatusFrameSize = get_val('CurrentStatusFrameSize')
        super(CurrentStatusPanel, self).__init__(parent, size=CurrentStatusFrameSize, style=wx.BORDER_NONE)
        self.SetBackgroundColour("#585858")
        self.timefont = wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.parent = parent


    def Modify(self):  # 更新
        self.SetForegroundColour('#FF8000')  ##设置文字颜色
        x1, y1 = get_val('status_time')
        x2, y2 = get_val('lowestprice_text')
        x3, y3 = get_val('pricelabeltext')
        x4, y4 = get_val('pricetext')
        x5, y5 = get_val('timestatustext')
        x6, y6 = get_val('pricestatustext')
        ##当前时间label
        currenttime_label = get_val("currenttime_label")
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        a_time = get_val('a_time')
        temp = int((a_time - int(a_time)) * 10)
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
        # st="%s:%s:%s"%(b_time[0],b_time[1],b_time[2])
        st = '{0}{1}.{2}'.format(currenttime_label, st, temp)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(self.timefont)
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, x1, y1)

        ##显示最低成交价
        findpos_on = get_val('findpos_on')
        if findpos_on:
            if self.parent.IsShown():
                self.parent.Show(False)
            # lowestpricelabel = get_val('lowestpricelabel')
            # lowestpricetext = "{0}: {1}".format(lowestpricelabel, '未识别')
            # dc.DrawText(lowestpricetext, x2, y2)
        else:
            if not self.parent.IsShown():
                self.parent.Show(True)
            lowest_price = get_val('lowest_price')
            lowestpricelabel = get_val('lowestpricelabel')
            lowestpricetext = "{0}: {1}".format(lowestpricelabel, lowest_price)
            dc.DrawText(lowestpricetext, x2, y2)

            ##第二行  出价情况
            userprice = get_val('userprice')
            tijiao_on = get_val('tijiao_on')
            usertime = get_val('usertime')
            smartprice_chujia = get_val('smartprice_chujia')
            strategy_type = get_dick('strategy_type')

            if userprice and tijiao_on:  ##提交状态
                current_pricestatus_label = get_val('current_pricestatus_label')
                current_pricestatus = get_val('current_pricestatus')
                pricelabeltext = "{0}".format(current_pricestatus_label)
                pricetext = "{0}".format(current_pricestatus)
                ##第三行  剩余状态
                # 显示截止时间与当前时间相差
                max_price = get_val('lowest_price') + 300
                diff_price = int(userprice) - max_price
                # 显示截止时间与当前时间相差
                currenttime = get_val('a_time')
                timediff = float(usertime) - float(currenttime)
                timestatustext = "提交倒计时{0:.1f}秒".format(timediff)
                pricestatustext = "差价{0}".format(diff_price)
                dc.DrawText(pricelabeltext, x3, y3)
                dc.DrawText(pricetext, x4, y4)
                dc.DrawText(timestatustext, x5, y5)
                dc.DrawText(pricestatustext, x6, y6)
            else:
                if smartprice_chujia:
                    current_pricestatus_label = get_val('current_pricestatus_label')
                    current_pricestatus = get_val('current_pricestatus')
                    pricelabeltext = "{0}".format(current_pricestatus_label)
                    pricetext = "{0}".format(current_pricestatus)
                    ##第三行  剩余状态
                    max_price = get_val('lowest_price') + 300
                    # diff_price = int(userprice) - max_price
                    diff_price = '-'
                    timediff = '-'
                    timestatustext = "提交倒计时{0}秒".format(timediff)
                    pricestatustext = "差价{0}".format(diff_price)
                    dc.DrawText(pricelabeltext, x3, y3)
                    dc.DrawText(pricetext, x4, y4)
                    dc.DrawText(timestatustext, x5, y5)
                    dc.DrawText(pricestatustext, x6, y6)
                else:
                    tijiao_num = get_val('tijiao_num')
                    # 显示截止时间与当前时间相差
                    currenttime = get_val('a_time')
                    if tijiao_num == 1:
                        one_time1 = get_val('one_real_time1')
                        timediff = float(one_time1) - float(currenttime)
                        ##修改状态
                        one_time1 = get_val('one_time1')
                        one_diff = get_val('one_diff')
                        current_pricestatus = '{0}秒加{1}'.format(one_time1, one_diff)
                        set_val('current_pricestatus', current_pricestatus)
                    elif tijiao_num == 2:
                        second_real_time1 = get_val('second_real_time1')
                        timediff = float(second_real_time1) - float(currenttime)
                        ##修改状态
                        second_time1 = get_val('second_time1')
                        second_diff = get_val('second_diff')
                        current_pricestatus = '{0}秒加{1}'.format(second_time1, second_diff)
                        set_val('current_pricestatus', current_pricestatus)
                    else:
                        timediff = '-'
                    current_pricestatus_label = get_val('current_pricestatus_label')
                    current_pricestatus = get_val('current_pricestatus')
                    pricelabeltext = "{0}".format(current_pricestatus_label)
                    pricetext = "{0}".format(current_pricestatus)
                    if timediff == '-':
                        timestatustext = "出价倒计时{0}秒".format(timediff)
                    else:
                        timestatustext = "出价倒计时{0:.1f}秒".format(timediff)

                pricestatustext = "差价{0}".format('-')
                dc.DrawText(pricelabeltext, x3, y3)
                dc.DrawText(pricetext, x4, y4)
                dc.DrawText(timestatustext, x5, y5)
                dc.DrawText(pricestatustext, x6, y6)



class WebFrame(wx.Frame):
    def __init__(self, px, py, id, name, tablabel, moni):  # name:窗口显示名称
        websize = get_val('websize')
        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]), pos=(px, py - 10),
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.moni = moni
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.htmlpanel = HtmlPanel(self, moni)  ## moni: True
        webstatus_label = get_val('moni_webstatus_label')
        self.buttonpanel = ButtonPanel(self, webstatus_label, moni)  ##moni: True
        self.operationpanel = OperationPanel(self, tablabel)
        self.bottomstatusbarpanel = BottomeStatusbarPanel(self, moni)

        self.currentstatusframe = CurrentStatusFrame(self)
        self.currentstatusframe.Show(False)
        Yanzhengmasize = get_val('Yanzhengmasize')
        self.yanzhengmaframe = YanzhengmaFrame(self, Yanzhengmasize)

        self.Bind(wx.EVT_MOVE, self.childmove)

        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)  # 绑定一个定时器事件，主判断
        self.timer1.Start(35)  # 设定时间间隔

        self.hotkey_open2()
        # self.Bind(wx.EVT_ACTIVATE , self.hotkey_open)

        pub.subscribe(self.refresh_web, 'moni refresh_web')
        pub.subscribe(self.refresh_web, 'guopai refresh_web')



    ##移动跟随
    def childmove(self, event):
        #位置重新计算
        Px, Py = self.Position
        init_pos(Px, Py)

        set_val('Px', Px)
        set_val('Py', Py)


        x, y = self.Position
        x0, y0 = get_val('CurrentStatusFramePos')
        self.currentstatusframe.Move(x+x0, y+y0)
        x1, y1 = get_val('YanzhengmaFramePos')
        try:
            self.yanzhengmaframe.Move(x+x1, y+y1)  # 移动到新位置
        except:
            logger.exception('this is an exception message')



    def refresh_web(self):
        self.htmlpanel.webview.Reload()
        strategy_type = get_dick("strategy_type")
        if strategy_type == 0:
            init_strategy()
        elif strategy_type == 1:
            init_strategy()



    def Price_view(self, event):
        moni_on = get_val('moni_on')
        guopai_on = get_val('guopai_on')
        on1 = moni_on and self.moni
        on2 = guopai_on and not self.moni
        on = on1 or on2
        if on and self.IsShown() and not self.IsIconized():
            ###子面板刷新
            self.buttonpanel.Modify()
            self.bottomstatusbarpanel.Modify()
            self.currentstatusframe.currentstatuspanel.Modify()

        ##------------------------------
        ###判定验证码放大框
            yanzhengma_scale = get_dick('yanzhengma_scale')
            if yanzhengma_scale:
                yanzhengma_move = get_val('yanzhengma_move')
                Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
                if yanzhengma_move:
                    yan = self.yanzhengmaframe
                    if yan:
                        try:
                            yan.Move(Pos_yanzhengmaframe)  # 移动到新位置
                            set_val('yanzhengma_move', False)  # 无需动作
                        except:
                            logger.exception('this is an exception message')

                yanzhengma_count = get_val("yanzhengma_count")
                yanzhengma_close = get_val("yanzhengma_close")

                if yanzhengma_count >= 4 and not yanzhengma_close:  # 0.4秒之后没有确认触发关闭验证码
                    find_yan_confirm()
                yanzhengma_close = get_val("yanzhengma_close")

                if yanzhengma_close:
                    try:
                        self.yanzhengmaframe.Show(False)
                    except:
                        logger.exception('this is an exception message')

                yanzhengma_view = get_val('yanzhengma_view')
                imgpos_yanzhengma = get_val('imgpos_yanzhengma')
                Yanzhengmasize = get_val('Yanzhengmasize')
                #验证码放大是否需要刷新
                if yanzhengma_view:
                    set_val('yanzhengma_close', False)
                    path = get_val('path')
                    yanpath = path + "\\yanzhengma.png"
                    cut_pic(imgpos_yanzhengma, Yanzhengmasize, yanpath)  # 直接调用得到 png 保存图片
                    try:
                        yanpath = get_val('yanpath')
                        yan = self.yanzhengmaframe
                        yan.Show()
                        yan.ShowImage(yanpath)
                    except:  # 找不到的情况下也要重新创建
                        logger.exception('this is an exception message')

                    finally:
                        pass
            ##------------------------------

            # 根据当前句柄判断是否需要激活快捷键
            hwnd = win32gui.GetForegroundWindow()
            currenthwnd = self.Handle
            hotkey_on = get_val('hotkey_on')
            yanhwnd = self.yanzhengmaframe.Handle
            statushwnd = self.currentstatusframe.Handle
            if hwnd == currenthwnd or hwnd == yanhwnd or hwnd == statushwnd:
                if not hotkey_on:
                    self.hotkey_open(event)
            elif hotkey_on and hwnd != currenthwnd or hwnd != yanhwnd or hwnd != statushwnd:
                self.hotkey_close(event)

        else:
            self.currentstatusframe.Show(False)
            self.yanzhengmaframe.Show(False)



    def hotkey_open2(self):
        ###热键控制
        hotkey_on = get_val('hotkey_on')
        if not hotkey_on:
            set_val('hotkey_on', True)
            print("获得焦点")
            Hotkey_open()

    def hotkey_open(self, event):
        ###热键控制
        hotkey_on = get_val('hotkey_on')
        if not hotkey_on:
            set_val('hotkey_on', True)
            print("获得焦点")
            Hotkey_open()

    def hotkey_close(self, event):
        hwnd = win32gui.GetForegroundWindow()
        currenthwnd = self.Handle
        hotkey_on = get_val('hotkey_on')
        if hotkey_on:
            print("失去焦点")
            set_val('hotkey_on', False)
            Hotkey_close()


    def OnClose(self, event):
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        self.yanzhengmaframe.Show(False)
        self.currentstatusframe.Show(False)
        event.Skip()
        id = get_val('topframe')
        topframe = wx.FindWindowById(id)
        topframe.Show(True)


## moni  51    国拍52
'''
class WebFrame(wx.Frame):
    def __init__(self, px, py, id, name, tablabel, moni):  # name:窗口显示名称
        websize = get_val('websize')

        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]), pos=[px, py - 10],
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        ##状态栏
        # self.createStatusBar()

        guopai_dianxin = get_val('guopai_dianxin')
        if guopai_dianxin:
            webstatus_label = get_val('dianxin_webstatus_label')
        else:
            webstatus_label = get_val('nodianxin_webstatus_label')
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.htmlpanel = HtmlPanel(self, False)
        self.buttonpanel = ButtonPanel(self, webstatus_label, False)
        self.buttonpanel = ButtonPanel(self, webstatus_label, False)
        self.operationpanel = OperationPanel(self, tablabel)
        # pub.subscribe(self.Close2, "close guopai")  # 打开非电信
        self.bottomstatusbarpanel = BottomeStatusbarPanel(self, False)
        self.currentstatusframe = CurrentStatusFrame(self)
        self.currentstatusframe.Show(False)
        # self.currentstatuspanel = CurrentStatusPanel(self)
        Yanzhengmasize = get_val('Yanzhengmasize')
        self.yanzhengmaframe = YanzhengmaFrame(self, Yanzhengmasize)

        self.hotkey_open2()


        self.Bind(wx.EVT_MOVE, self.childmove)

        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.Price_view, self.timer1)  # 绑定一个定时器事件，主判断
        self.timer1.Start(35)  # 设定时间间隔

        pub.subscribe(self.refresh_web, 'guopai refresh_web')  # 刷新页面


    def childmove(self, event):
        x, y = self.Position
        x0, y0 = get_val('CurrentStatusFramePos')
        self.currentstatusframe.Move(x+x0, y+y0)
        x1, y1 = get_val('YanzhengmaFramePos')
        try:
            self.yanzhengmaframe.Move(x+x1, y+y1)  # 移动到新位置
        except:
            logger.exception('this is an exception message')

        #位置重新计算
        Px, Py = self.Position
        import time
        a = time.time()
        init_pos(Px, Py)
        b = time.time()
        print('b-a', b-a)

    def refresh_web(self):
        self.htmlpanel.webview.Reload()
        strategy_type = get_dick("strategy_type")
        if strategy_type == 0:
            init_strategy()
        elif strategy_type == 1:
            init_strategy()


    def Price_view(self, event):
        guopai_on = get_val('guopai_on')
        if guopai_on and self.IsShown() and not self.IsIconized() :
            ###子面板刷新
            self.buttonpanel.Modify()
            self.bottomstatusbarpanel.Modify()
            self.currentstatusframe.currentstatuspanel.Modify()

            ###判定验证码放大框
            Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
            x, y = self.Position
            Pricesize = get_val('Pricesize')
            yanzhengma_move = get_val('yanzhengma_move')
            Pos_price = get_val('Pos_price')
            Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
            if yanzhengma_move:
                yan = self.yanzhengmaframe
                if yan:
                    try:
                        yan.Move(Pos_yanzhengmaframe)  # 移动到新位置
                        set_val('yanzhengma_move', False)  # 无需动作
                    except:
                        logger.exception('this is an exception message')

            yanzhengma_count = get_val("yanzhengma_count")
            yanzhengma_close = get_val("yanzhengma_close")

            if yanzhengma_count >= 5 and not yanzhengma_close:  # 0.5秒之后没有确认触发关闭验证码
                find_yan_confirm()
            yanzhengma_close = get_val("yanzhengma_close")

            if yanzhengma_close:
                try:
                    self.yanzhengmaframe.Show(False)
                except:
                    logger.exception('this is an exception message')

            yanzhengma_view = get_val('yanzhengma_view')
            imgpos_yanzhengma = get_val('imgpos_yanzhengma')
            Yanzhengmasize = get_val('Yanzhengmasize')
            #验证码放大是否需要刷新
            if yanzhengma_view:
                set_val('yanzhengma_close', False)
                path = get_val('path')
                yanpath = path + "\\yanzhengma.png"
                cut_pic(imgpos_yanzhengma, Yanzhengmasize, yanpath)  # 直接调用得到 png 保存图片
                try:
                    yanpath = get_val('yanpath')
                    yan = self.yanzhengmaframe
                    yan.Show()
                    yan.ShowImage(yanpath)
                except:  # 找不到的情况下也要重新创建
                    logger.exception('this is an exception message')

                finally:
                    pass

            hwnd = win32gui.GetForegroundWindow()
            currenthwnd = self.Handle
            hotkey_on = get_val('hotkey_on')
            yanhwnd = self.yanzhengmaframe.Handle
            statushwnd = self.currentstatusframe.Handle
            if hwnd == currenthwnd or hwnd == yanhwnd or hwnd == statushwnd:
                if not hotkey_on:
                    self.hotkey_open(event)
            elif hotkey_on and hwnd != currenthwnd or hwnd != yanhwnd or hwnd != statushwnd:
                self.hotkey_close(event)
        else:
            self.currentstatusframe.Show(False)
            self.yanzhengmaframe.Show(False)

    def hotkey_open(self, event):
        ###热键控制
        hotkey_on = get_val('hotkey_on')
        if not hotkey_on:
            set_val('hotkey_on', True)
            print("获得焦点")
            Hotkey_open()

    def hotkey_close(self, event):
        hwnd = win32gui.GetForegroundWindow()
        currenthwnd = self.Handle
        hotkey_on = get_val('hotkey_on')
        if hotkey_on:
            print("失去焦点")
            set_val('hotkey_on', False)
            Hotkey_close()

    def hotkey_open2(self):
        ###热键控制
        hotkey_on = get_val('hotkey_on')
        if not hotkey_on:
            set_val('hotkey_on', True)
            print("获得焦点")
            Hotkey_open()


    def createStatusBar(self):
        self.statusbar = IcStatusBar(self)
        self.SetStatusBar(self.statusbar)

    def OnClose(self, event):
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        self.yanzhengmaframe.Show(False)
        self.currentstatusframe.Show(False)
        event.Skip()
        id = get_val('topframe')
        topframe = wx.FindWindowById(id)
        topframe.Show(True)
        # print("关闭web")
        # guopai_on = get_val('guopai_on')
        # current_moni = get_val('current_moni')
        # moni_on = get_val('moni_on')
        #
        # print(guopai_on, 'guopai_on')
        # print(current_moni, 'current_moni')
        # print(moni_on, 'moni_on')
        # if current_moni:
        #     set_val('web_on', False)
        #     set_val('view_time', False)
        #     set_val('moni_on', False)
        #     set_val('guopai_on', False)
        #     print("ssssssdfsf")
        #     topframe = wx.FindWindowById(1)
        #     topframe.Show(True)
        #     Close()
        #     self.Destroy()
        #     event.Skip()  # 绑在同一事件上的两个函数，如果 没有这个，就只执行后绑定的。
        # else:
        #     dlg = wx.MessageDialog(None, "确认要关闭国拍吗?",
        #                            '关闭国拍页面',
        #                            wx.YES_NO | wx.ICON_WARNING | wx.STAY_ON_TOP)
        #     ret = dlg.ShowModal()
        #     if ret == wx.ID_YES:
        #         set_val('web_on', False)
        #         set_val('view_time', False)
        #         set_val('moni_on', False)
        #         set_val('guopai_on', False)
        #         print("ssssssdfsf")
        #         topframe = wx.FindWindowById(1)
        #         topframe.Show(True)
        #         Close()
        #         dlg.Destroy()
        #         self.Destroy()
        #         event.Skip()  # 绑在同一事件上的两个函数，如果 没有这个，就只执行后绑定的。
'''
