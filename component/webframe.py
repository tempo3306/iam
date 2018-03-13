# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 13:58
'''
import wx
from wx.lib.pubsub import pub  # 代替了publisher
from component.staticmethod import *


class WebFrame(wx.Frame):
    def __init__(self, px, py, ad, name, size):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 3, name, size=size, pos=(px, py), style=wx.SIMPLE_BORDER)

        # wx.Frame.__init__(self,None, -1,title="大师拍牌 QQ 178456661 - 3.663",size=(websize[0], websize[1]),\
        #  pos=(px, py),style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP&~(wx.RESIZE_BORDER))
        # wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.CLOSE_BOX))
        # wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.CLOSE_BOX))

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ad2 = ad
        pub.subscribe(self.OnClose2, "close webframe")  #绑定关闭消息

    def OnClose(self, event):
        # print("关闭web")
        guopai_on = get_val('guopai_on')
        if guopai_on:
            dlg = wx.MessageDialog(None, "确认要关闭国拍吗?",
                                   '关闭国拍页面',
                                   wx.YES_NO | wx.ICON_WARNING | wx.STAY_ON_TOP)
            ret = dlg.ShowModal()
            if ret == wx.ID_YES:
                wx.CallAfter(pub.sendMessage, "close operation") #关闭operation
                set_val('web_on', False)
                set_val('view_time', False)
                set_val('moni_on', False)
                set_val('guopai_on', False)
                self.Destroy()
                event.Skip()  # 绑在同一事件上的两个函数，如果 没有这个，就只执行后绑定的。
            dlg.Destroy()
        else:
            wx.CallAfter(pub.sendMessage, "close operation")  # 关闭operation
            set_val('web_on', False)
            set_val('view_time', False)
            set_val('moni_on', False)
            set_val('guopai_on', False)
            self.Destroy()
            event.Skip()  # 绑在同一事件上的两个函数，如果 没有这个，就只执行后绑定的。



    def OnClose2(self):  #pubsub消息机制不能带EVENT
        set_val('web_on', False)
        set_val('view_time', False)
        set_val('moni_on', False)
        set_val('guopai_on', False)
        self.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = WebFrame(0, 0, False, "模拟", (400, 400))
    frame.Show()
    app.MainLoop()
