import time

import wx
from wx.lib.pubsub import pub

from component.variable import get_val, set_val
import copy

class InfoPanel(wx.Panel):
    def __init__(self, parent):
        infopanel_size = get_val('infopanel_size')
        infopanel_pos = get_val('infopanel_pos')
        super(InfoPanel, self).__init__(parent, size=infopanel_size, pos=infopanel_pos)
        self.infomationfont = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.infofont = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.areafont = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.infos = []
        self.init_info()

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.infomation = wx.StaticText(self, label='沪牌一号模拟拍牌会', pos=(30, 5))
        self.infoarea = wx.StaticText(self, label='操作日志:', pos=(15, 35))
        self.infomation.SetFont(self.infomationfont)
        self.infoarea.SetFont(self.areafont)
        self.SetBackgroundColour('white')
        # self.SetForegroundColour('white')

        #更新日志
        pub.subscribe(self.update_info, 'update info')

    def draw_text(self, dc, text, pos):
        x1, y1 = pos
        print(x1, y1)
        dc.DrawText(text, x1, y1)

    #--------------------------------------------
    #日志管理
    '''
    1.切换国拍与模拟
    2.用户修改策略
    '''
    def init_info(self):
        action_infos = get_val('action_infos')
        len_info = len(action_infos)
        if  len_info > 5:
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
                self.infos.pop(0) ##维持6个元素

                ##修改info
        len_info = len(self.infos)
        infotext_pos = get_val('infotext_pos')
        print(infotext_pos)
        print(len_info)
        dc = wx.BufferedDC(wx.ClientDC(self))  # ClientDC客户区  ，BufferedDC双缓冲绘图设备
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(self.infofont)

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