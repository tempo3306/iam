# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 14:40
'''
# -----------------------------------------------------------------------
#################国拍时间显示##################
import wx
import time
from component.variable import get_val


class ClockWindow(wx.Panel):
    def __init__(self, parent, Timesize):
        wx.Window.__init__(self, parent, size=Timesize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(100)  # 设定时间间隔

    def Draw(self, dc):  # 绘制当前时间
        a_time = get_val('a_time')
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def Modify(self, dc):  # 更新
        a_time = get_val('a_time')
        time_local = time.localtime(a_time)
        st = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
        # st="%s:%s:%s"%(b_time[0],b_time[1],b_time[2])
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def OnTimer(self, evt):  # 显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        self.Modify(dc)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)  # 用于重绘事件
        self.Draw(dc)


# 国拍时间框显示
class TimeFrame(wx.Frame):
    def __init__(self):
        Timesize = get_val('Timesize')
        Pos_timeframe = get_val('Pos_timeframe')
        wx.Frame.__init__(self, None, title="wx.Timer", size=Timesize, pos=Pos_timeframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        # wx.Frame.__init__(self, None, -1,'Time',size=(400,160), pos=Pos_timeframe,
        #                   style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        ClockWindow(self, Timesize)


# -----------------------------------------------------------------------
#################模拟时间显示##################
# class MoniClockWindow(wx.Panel):
#     def __init__(self, parent, Timesize):
#         wx.Window.__init__(self, parent, size=Timesize)
#         self.Bind(wx.EVT_PAINT, self.OnPaint)
#         self.timer = wx.Timer(self)  # 创建定时器
#         self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
#         self.timer.Start(100)  # 设定时间间隔
#
#     def Draw(self, dc):  # 绘制当前时间
#         moni_second = get_val('moni_second')
#         st = "%s:%s:%s" % (11, 29, moni_second)
#         w, h = self.GetClientSize()
#         dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
#         dc.Clear()
#         dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
#         tw, th = dc.GetTextExtent(st)
#         dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
#
#     def Modify(self, dc):  # 更新
#         moni_second = get_val('moni_second')  # 取得全局变量的值
#         moni_s = int(moni_second)  # 整数化
#         st = "%s:%s:%s" % (11, 29, moni_s)
#         w, h = self.GetClientSize()
#         dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
#         dc.Clear()
#         dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
#         tw, th = dc.GetTextExtent(st)
#         dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)
#
#     def OnTimer(self, evt):  # 显示时间事件处理函数
#         dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
#         self.Modify(dc)
#
#     def OnPaint(self, evt):
#         dc = wx.BufferedPaintDC(self)  # 用于重绘事件
#         self.Draw(dc)


# 国拍时间框显示
class MoniTimeFrame(wx.Frame):
    def __init__(self):
        Pos_timeframe = get_val('Pos_timeframe')
        Timesize = get_val('Timesize')
        wx.Frame.__init__(self, None, title="wx.Timer", size=(200, 50), pos=Pos_timeframe,
                          style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP)
        # wx.Frame.__init__(self, None, -1,'Time',size=(400,160), pos=Pos_timeframe,
        #                   style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        MoniClockWindow(self, Timesize)
