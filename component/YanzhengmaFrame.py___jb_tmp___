# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:54
'''

import wx
from component.variable import get_val


class YanzhengmaFrame(wx.Frame):
    def __init__(self, parent, size):
        x, y = parent.Position
        Yanzhengmasize = get_val('Yanzhengmasize')
        x0, y0 = get_val('YanzhengmaFramePos')
        wx.Frame.__init__(self, parent, 18, 'Price', size=Yanzhengmasize, pos=(x+x0, y+y0),
                          style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT)
        self.panel = wx.Panel(self, size=size)
        # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        # self.bmp = wx.StaticBitmap(self.panel, -1)
        # 更换图片显示
        self.Disable()

    def ShowImage(self, bm):
        self.bmp = wx.Bitmap(bm)
        dc = wx.BufferedDC(wx.ClientDC(self.panel))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  ##保存刷新不闪烁
        w, h = self.GetClientSize()
        dc.Clear()
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def OnClose(self, event):
        self.Close()
        event.Skip()


class TipFrame(wx.Frame):
    def __init__(self, parent):
        x, y = parent.Position
        TipFrameSize = get_val('TipFrameSize')
        x0, y0 = get_val('TipFramePos')
        wx.Frame.__init__(self, parent, 18, 'Price', size=TipFrameSize, pos=(x+x0, y+y0),
                          style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT )
        self.panel = wx.Panel(self, size=TipFrameSize)
        # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        # self.bmp = wx.StaticBitmap(self.panel, -1)
        # 更换图片显示
        self.Disable()

    def ShowImage(self, bm):
        self.bmp = wx.Bitmap(bm)
        dc = wx.BufferedDC(wx.ClientDC(self.panel))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  ##保存刷新不闪烁
        w, h = self.GetClientSize()
        dc.Clear()
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def OnClose(self, event):
        self.Close()
        event.Skip()

# class EnterFrame(wx.Frame):
#     def __init__(self, parent, size):
#         x, y = parent.Position
#         EnterFrameSize = get_val('EnterFrameSize')
#         x0, y0 = get_val('EnterFramePos')
#         wx.Frame.__init__(self, parent, 18, 'Price', size=EnterFrameSize, pos=(x+x0, y+y0),
#                           style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT)
#         self.panel = wx.Panel(self, size=size)
#         # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
#         # self.bmp = wx.StaticBitmap(self.panel, -1)
#         # 更换图片显示
#         self.Disable()
#
#     def ShowImage(self, bm):
#         self.bmp = wx.Bitmap(bm)
#         dc = wx.BufferedDC(wx.ClientDC(self.panel))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
#         dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  ##保存刷新不闪烁
#         w, h = self.GetClientSize()
#         dc.Clear()
#         dc.DrawBitmap(self.bmp, 0, 0, True)
#
#     def OnClose(self, event):
#         self.Close()
#         event.Skip()