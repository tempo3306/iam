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
        super(InfoPanel, self).__init__(parent, size=infopanel_size, pos=infopanel_pos, style=wx.VSCROLL)
        super(InfoPanel, self).SetScrollbars(0, 20, 0, 10)


        self.infomationfont = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.infofont = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.areafont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.infos = []
        self.init_info()
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.SetBackgroundColour('white')
        self.pageindex = 10

        # 更新日志
        pub.subscribe(self.update_info, 'update info')


    def SetScrollbars(self, *args):
        super(InfoPanel, self).SetScrollbars(*args)
        print(vars)

    def draw_text(self, dc, text, pos):
        pageindex = get_val('pageindex')
        set_val('pageindex', pageindex + 1)
        vars = [0, 20, 0, pageindex + 1]
        self.SetScrollbars(*vars)
        range = self.GetScrollRange(0)
        self.SetScrollPos(0, range)
        x1, y1 = pos
        print(x1, y1)

        dc.SetFont(self.infomationfont)
        dc.DrawText('沪牌一号模拟拍牌会', 30, 5)
        dc.SetFont(self.areafont)
        dc.DrawText('操作日志：', 15, 35)
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
        if len_info > 5:
            self.infos = [action for action in action_infos[-6:]]
            self.update_info()
        else:
            new_actions = get_val('new_actions')
            self.infos = [self.create_info(action) for action in new_actions]
            self.update_info()
            print("fdssfsd", self.infos)
            set_val('action_infos', copy.deepcopy(self.infos))

    def update_info(self, action=None):
        print('action', action)
        print(len(self.infos))
        if action:
            info = self.create_info(action)
            self.addto_infos(action)
            self.infos.append(info)
            if len(self.infos) >= 7:
                self.infos.pop(0)  ##维持6个元素

                ##修改info
        len_info = len(self.infos)
        infotext_pos = get_val('infotext_pos')
        print(infotext_pos)
        print(len_info)
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()

        for i in range(len_info):
            self.draw_text(dc, self.infos[i], infotext_pos[i])

    @staticmethod
    def create_info(action):
        true_time_str = get_val('true_time_str')
        if not true_time_str:
            true_time = get_val('true_time')
            time_local = time.localtime(true_time)
            true_time_str = time.strftime("%H:%M:%S", time_local)  # + '.' + str(b_time)
            print(true_time_str)
        info = f'{true_time_str}: {action}'
        return info

    @staticmethod
    def addto_infos(action):
        info = InfoPanel.create_info(action)
        action_infos = get_val('action_infos')
        action_infos.append(info)
        set_val('action_infos', action_infos)

