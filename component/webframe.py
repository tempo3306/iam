# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 13:58
'''
import wx
import os
from wx.lib.pubsub import pub  # 代替了publisher
from component.variable import get_val,set_val
class WebFrame(wx.Frame):
    def __init__(self, px, py, ad, name,size):  # name:窗口显示名称
        wx.Frame.__init__(self, None, 3, name, size=size, pos=(px, py), style=wx.SIMPLE_BORDER)

        # wx.Frame.__init__(self,None, -1,title="大师拍牌 QQ 178456661 - 3.663",size=(websize[0], websize[1]),\
        #  pos=(px, py),style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP&~(wx.RESIZE_BORDER))
        # wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.CLOSE_BOX))

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.ad2 = ad
        # 最低成交价
        # self.lowestframe = LowestpriceFrame()
        # self.lowestframe.Show(False)

        # 广告   控制 界面

        # self.control=ControlFrame()

        # 测试关掉
        # if not test:
        #     self.control.Show(True)

        # panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        # panel.SetFocus()
        # panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        # def OnKeyDown(self, event):
        #     keycode = event.GetKeyCode()
        #     if keycode == wx.WXK_F1:
        #         x, y = pg.position()
        #         print(x, y)
        #     else:
        #         event.Skip()
        #     global num
        #     sc = pg.screenshot(region=(377, 412, 41, 16))
        #     global num
        #     print("成功")
        #     sc.save("%d.png" %num)
        #     num+=1
        #
        #
        # def Webpos(self):
        #     return self.GetPosition()  #输出位置坐标
        pub.subscribe(self.OnClose2, "close web")  # 触发关闭

    def OnClose(self, event):
        # print("关闭web")
        set_val('web_on',False)
        set_val('view_time',False)
        set_val('moni_on',False)
        set_val('guopai_on',False)
        wx.CallAfter(pub.sendMessage, "close topframe")  #关闭热键绑定
        # TopFrame.Close()
        self.Destroy()
        event.Skip()  # 绑在同一事件上的两个函数，如果 没有这个，就只执行后绑定的。

    def OnClose2(self):
        set_val('web_on',False)
        set_val('view_time',False)
        set_val('moni_on',False)
        set_val('guopai_on',False)
        wx.CallAfter(pub.sendMessage, "close topframe")  # 关闭热键绑定
        self.Destroy()
