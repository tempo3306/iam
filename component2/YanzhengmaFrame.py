from component.variable import V_global
# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:54
'''

import wx


class YanzhengmaFrame(wx.Frame):
    def __init__(self, parent, size):
        x, y = parent.Position
        Yanzhengmasize = V_global.Yanzhengmasize
        x0, y0 = V_global.YanzhengmaFramePos
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