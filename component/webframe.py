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



class MoniWebFrame(wx.Frame):
    def __init__(self, px, py, id, name, tablabel):  # name:窗口显示名称
        websize = get_val('websize')
        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]),
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        # pub.subscribe(self.Close2, "close moni")  # 打开非电信

        ##状态栏
        self.createStatusBar()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = OperationPanel(self, tablabel)
        self.Center()


    def createStatusBar(self):
        self.statusbar = IcStatusBar(self)
        self.SetStatusBar(self.statusbar)

    def OnClose(self, event):
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        self.Destroy()
        event.Skip()
        topframe = wx.FindWindowById(1)
        topframe.Show(True)

    def Close2(self):
        try:
            self.Destroy()
        except:
            pass


## moni  51    国拍52
class WebFrame(wx.Frame):
    def __init__(self, px, py, id, name, tablabel):  # name:窗口显示名称
        websize = get_val('websize')
        wx.Frame.__init__(self, None, id, name, size=(websize[0], websize[1]),
                          style=wx.CAPTION | wx.CLOSE_BOX)
        ##LOGO
        mainicon = get_val('mainicon')
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = OperationPanel(self, tablabel)
        self.Center()
        # pub.subscribe(self.Close2, "close guopai")  # 打开非电信

        ##状态栏
        self.createStatusBar()

    def createStatusBar(self):
        self.statusbar = IcStatusBar(self)
        self.SetStatusBar(self.statusbar)

    def OnClose(self, event):
        self.Destroy()
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        self.Destroy()
        event.Skip()
        topframe = wx.FindWindowById(1)
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

    def Close2(self):
        try:
            self.Destroy()
        except:
            pass