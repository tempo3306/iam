# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:54
'''

import wx
from .variable import get_val
Yanzhengmasize = get_val('Yanzhengmasize')
Pos_yanzhengmaframe = get_val('Pos_yanzhengmaframe')
class YanzhengmaFrame(wx.Frame):
    def __init__(self,size):
        # print(Pos_yanzhengmaframe)
        wx.Frame.__init__(self, None, 18, 'Price', size=Yanzhengmasize, pos=Pos_yanzhengmaframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
                          )
        self.panel = wx.Panel(self, size=size)
        # image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        self.bmp = wx.StaticBitmap(self.panel, -1)
        # 更换图片显示

    def ShowImage(self, bm):
        self.bmp.SetBitmap(wx.Bitmap(bm))

    def OnClose(self, event):
        self.Close()
        event.Skip()
