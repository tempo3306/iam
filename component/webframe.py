# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 13:58
'''
import wx
from wx.lib.pubsub import pub  # 代替了publisher
from component.staticmethod import *
from component.OperationFrame import OperationPanel
from component.statusbar import IcStatusBar
import wx.html2 as webview
from component.OperationFrame import StatusPanel, StrategyPanel
from wx.lib.buttons import GenButton as wxButton
from component.imgcut import findpos, timeset


class ButtonPanel(wx.Panel):
    def __init__(self, parent, webstatus_label, moni):
        wx.Panel.__init__(self, parent, size=(892, 30))
        self.parent = parent
        self.timefont = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.statusfont = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.FONTWEIGHT_BOLD, False)
        ##时间同步功能
        if not moni:
            self.remotetime_button = wxButton(self, label='同步服务器时间', size=(90, 25), pos=(698,2))
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

        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔

        self.autotime_timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.autotime_set_timer, self.autotime_timer)  # 绑定一个定时器事件
        self.autotime_timer.Start(1500)  # 设定时间间隔

        # 没边框按钮
        # from wx.lib.buttons import GenButton as wxButton
        # tmpButton = wxButton(parent, id, u'删除学生', pos=(10, 10), size=(100, 30), style=wx.BORDER_NONE)
        # tmpButton.SetBackgroundColour("#ff0000")
        # tmpButton.SetForegroundColour("#ffffff")

    def Draw(self, dc):  # 绘制当前时间
        moni_second = get_val('moni_second')
        st = "%s:%s:%s" % (11, 29, moni_second)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(self.timefont)
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):  # 更新
        moni_on = get_val('moni_on')
        if moni_on:
            moni_second = get_val('moni_second')  # 取得全局变量的值
            moni_s = int(moni_second)  # 整数化
            if moni_second <10:
                st = "当前时间：%s:%s:0%s" % (11, 29, moni_s)
            else:
                st = "当前时间：%s:%s:%s" % (11, 29, moni_s)
            w, h = self.GetClientSize()
            dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
            dc.Clear()
            dc.SetFont(self.timefont)
            tw, th = dc.GetTextExtent(st)
            dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
        else:
            a_time = get_val('a_time')
            time_local = time.localtime(a_time)
            st = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
            # st="%s:%s:%s"%(b_time[0],b_time[1],b_time[2])
            st = '当前时间：%s' %st
            w, h = self.GetClientSize()
            dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
            dc.Clear()
            dc.SetFont(self.timefont)
            tw, th = dc.GetTextExtent(st)
            dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)


    def OnTimer(self, event):  # 显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        self.Modify(dc)


    def autotime_set_timer(self, event):
        autotime_on = get_val('autotime_on')
        if autotime_on:
            self.timeautoajust(event)


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)  # 用于重绘事件
        self.Draw(dc)

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



class HtmlPanel(wx.Panel):
    def __init__(self, parent, moni):
        wx.Panel.__init__(self, parent, size=(892, 700), pos=(0, 30), style=wx.BORDER_NONE)
        self.frame = self.GetTopLevelParent()
        self.titleBase = self.frame.GetTitle()
        htmlsize = get_val('htmlsize')
        webview_pos = get_val('webview_pos')
        self.webview = webview.WebView.New(self, size=(htmlsize[0], htmlsize[1]), pos=webview_pos,
                                                     style=wx.BORDER_NONE)
        url_moni = get_val('url_moni')
        url_dianxin = get_val('url_dianxin')
        url_nodianxin = get_val('url_nodianxin')
        guopai_dianxin = get_val('guopai_dianxin')
        if moni:
            self.webview.LoadURL(url_moni)
        elif guopai_dianxin:
            self.webview.LoadURL(url_dianxin)
        else:
            self.webview.LoadURL(url_nodianxin)



class MoniWebFrame(wx.Frame):
    def __init__(self,px,py,  id, name, tablabel):  # name:窗口显示名称
        websize = get_val('websize')
        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]), pos=[px, py-10],
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.htmlpanel = HtmlPanel(self, True) ## moni: True

        webstatus_label = get_val('moni_webstatus_label')
        self.buttonpanel = ButtonPanel(self, webstatus_label, True)  ##moni: True
        self.operationpanel = OperationPanel(self, tablabel)

    def OnClose(self, event):
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        event.Skip()
        id = get_val('topframe')
        topframe = wx.FindWindowById(id)
        topframe.Show(True)



## moni  51    国拍52
class WebFrame(wx.Frame):
    def __init__(self, px, py, id, name, tablabel):  # name:窗口显示名称
        websize = get_val('websize')

        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]), pos=[px, py-10],
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        ##状态栏
        self.createStatusBar()

        guopai_dianxin = get_val('guopai_dianxin')
        if guopai_dianxin:
            webstatus_label = get_val('dianxin_webstatus_label')
        else:
            webstatus_label = get_val('nodianxin_webstatus_label')
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.htmlpanel = HtmlPanel(self, False)
        self.buttonpanel = ButtonPanel(self, webstatus_label, False)
        self.operationpanel = OperationPanel(self, tablabel)
        # pub.subscribe(self.Close2, "close guopai")  # 打开非电信



    def createStatusBar(self):
        self.statusbar = IcStatusBar(self)
        self.SetStatusBar(self.statusbar)

    def OnClose(self, event):
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
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
