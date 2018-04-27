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
                          style=wx.FRAME_NO_TASKBAR | wx.FRAME_FLOAT_ON_PARENT)
        self.panel = wx.Panel(self, size=size)
        # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        # self.bmp = wx.StaticBitmap(self.panel, -1)
        # 更换图片显示

    def ShowImage(self, bm, event):
        self.bmp = wx.Bitmap(bm)
        dc = wx.BufferedDC(wx.ClientDC(self.panel))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))  ##保存刷新不闪烁
        w, h = self.GetClientSize()
        dc.Clear()
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def OnTimer(self, event):  # 显示时间事件处理函数
        yanpath = get_val('yanpath')
        self.ShowImage(yanpath, event)


    def OnClose(self, event):
        self.Close()
        event.Skip()
