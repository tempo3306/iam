# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:19
'''
import wx

userweb_label = "本地IE"
from wx.lib.pubsub import pub


class GuopaiFrame(wx.Dialog):
    def __init__(self, name, mainicon):  ##########版本号
        wx.Dialog.__init__(self, None, -1, name, size=(195, 195), style=wx.CAPTION | wx.CLOSE_BOX)
        # self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(self, size=(195, 270))
        self.icon = wx.Icon(mainicon, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        # 创建2个button
        self.userweb_label = userweb_label
        self.dianxin = wx.Button(self.panel, label="上海电信", pos=(20, 10), size=(140, 60))
        self.nodianxin = wx.Button(self.panel, label="非电信", pos=(20, 80), size=(140, 60))
        self.dianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.nodianxin.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        # self.Bind(wx.EVT_BUTTON, self.Dianxin, self.dianxin)
        # self.Bind(wx.EVT_BUTTON, self.NoDianxin, self.nodianxin)
        self.Center()
        self.ShowModal()
        # self.Show(True)
    # def Dianxin(self, event):
    #     wx.CallAfter(pub.sendMessage, "open dianxin")
    #     self.Destroy()
    #     event.Skip()
    #
    # def NoDianxin(self, event):
    #     wx.CallAfter(pub.sendMessage, "open nodianxin")
    #     self.Destroy()
    #     event.Skip()


    # def OnClose(self, event):
    #     self.Destroy()
    #     event.Skip()
