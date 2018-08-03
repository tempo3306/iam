import time

import wx
from wx.lib.pubsub import pub

from component.variable import get_val, set_val
import copy

'''
第一句 self.scroller = wx.ScrolledWindow(self, -1)

  作用是创建一个滚动条对象，不用多解释

第二句 self.scroller.SetScrollbars(1, 1, 1440, 900)

  设定滚动条参数：

  第一个参数，是窗体底部水平方向的滚动条，1为有，0为无

  第二个参数，是窗体右侧竖直方向的滚动条，1为有，0为无

  第三个参数，是水平方向的滚动条触发条件，第一个参数为0时该参数失效，当窗体水平方向的实际尺寸小于该参数时，滚动条出现，反之不出现

  第四个参数，同第三个参数的效果，只是应用于竖直方向

'''


class InfoPanel(wx.ScrolledWindow):
    def __init__(self, parent):
        infopanel_size = get_val('infopanel_size')
        infopanel_pos = get_val('infopanel_pos')
        super(InfoPanel, self).__init__(parent, size=infopanel_size, pos=infopanel_pos)
        super(InfoPanel, self).SetScrollbars(0, 20, 0, 5)
        self.SetScrollRate(0,20)
        self.infomationfont = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.infofont = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.areafont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.init_info()
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.SetBackgroundColour('white')
        # self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_PAINT, self.refreshtext)

        # self.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, self.refreshtext)

        # 更新日志
        pub.subscribe(self.update_info, 'update info')


    def on_paint(self, event):
        dc = wx.PaintDC(self)
        self.PrepareDC(dc)
        self.draw_infomation(dc)
        # self.do_draw(dc)




    def refreshtext(self, event):
        print(event)
        xx = self.GetViewStart()
        pos = xx[1]
        print(pos)
        if pos < 30:
            x, y = get_val('infotext_pos')
            dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
            dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
            dc.Clear()
            self.draw_infomation(dc)
            print(self.infos)
            print(len(self.infos))
            len_info = len(self.infos)
            len_info = len_info if len_info <= 7 else 7
            for i in range(len_info):
                self.draw(dc, self.infos[i], (x, y + 20*i))
        else:
            x, y = get_val('infotext_pos')
            dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
            dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
            dc.Clear()
            self.draw_infomation(dc)
            index  = int((pos - 23)/7)
            print(self.infos)
            print('index=', index)
            print(len(self.infos))
            print("fdsf")
            for i in range(7):
                self.draw(dc, self.infos[index + i], (x, y + 20*i))
        event.Skip()


    def do_draw(self, dc):
        len_info = len(self.infos)
        x, y = get_val('infotext_pos')
        xx = self.GetViewStart()
        pos = xx[1]
        print("pos", pos)
        for i in range(len_info):
            self.draw(dc, self.infos[i], (x, y + 20*i))

    def draw(self, dc, text, pos):
        x1, y1 = pos
        dc.SetFont(self.infofont)
        dc.DrawText(text, x1, y1)



    def draw_infomation(self, dc):
        dc.SetFont(self.infomationfont)
        # dc.DrawText('沪牌一号模拟拍牌会', 30, 15)
        dc.SetFont(self.areafont)
        dc.DrawText('操作日志：', 15, 20)

    def draw_text(self, dc, text, pos):
        pageindex = get_val('pageindex')
        set_val('pageindex', pageindex + 1)
        vars = [0, 20, 0, pageindex + 1]
        self.SetScrollbars(*vars)
        range = self.GetScrollRange(0)
        self.SetScrollPos(0, range)
        # self.Scroll(0, pageindex*7)
        x1, y1 = pos
        dc.SetFont(self.infofont)
        dc.DrawText(text, x1, y1)


    # fontsz = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT).GetPixelSize()
    # self.SetScrollRate(fontsz.x, fontsz.y)
    # --------------------------------------------
    # 日志管理
    '''
    1.切换国拍与模拟
    2.用户修改策略
    '''
    def init_info(self):
        action_infos = get_val('action_infos')
        len_info = len(action_infos)
        print("fdsfsfdsfds")
        if len_info > 5:
            self.infos = [action for action in action_infos[-6:]]
            self.update_info()
        else:
            new_actions = get_val('new_actions')
            self.infos = [self.create_info(action) for action in new_actions]
            self.update_info()
            set_val('action_infos', copy.deepcopy(self.infos))

    def update_info(self, action=None):
        if action:
            info = self.create_info(action)
            self.addto_infos(action)
            self.infos.append(info)
         ##修改info
        len_info = len(self.infos)
        x, y = get_val('infotext_pos')
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.draw_infomation(dc)
        index  = len_info - 7
        len_info = len_info if len_info <= 7 else 7
        for i in range(len_info):
            self.draw_text(dc, self.infos[index + i], (x, y + 20*i))

    @staticmethod
    def create_info(action):
        true_time_str = get_val('true_time_str')
        if not true_time_str:
            true_time = get_val('true_time')
            time_local = time.localtime(true_time)
            true_time_str = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
        info = f'{true_time_str}: {action}'
        return info

    @staticmethod
    def addto_infos(action):
        info = InfoPanel.create_info(action)
        action_infos = get_val('action_infos')
        action_infos.append(info)
        set_val('action_infos', action_infos)

