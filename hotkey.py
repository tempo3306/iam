# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/12 14:18
'''

import wx
from component.staticmethod import *

keycodes = {}
for i in range(65,91):
    keycodes[chr(i)] = i
print(keycodes)


class MyForm(wx.Frame):

    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial", size=(500, 500))

        # Add a panel so it looks the correct on all platforms
        self.text = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.text.Bind(wx.EVT_KEY_DOWN, self.onEnter)
        # self.text.Show(False)
        panel = wx.Panel(self, wx.ID_ANY)
        panel.Bind(wx.EVT_KEY_DOWN, self.onEnter)

    # ----------------------------------------------------------------------
    def onEnter(self, event):
        """"""
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            print("fdsfs")
        event.Skip()


    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_NUMPAD_ENTER:
            print("fdsf")

        print(keycode)
        # if chr(keycode) == 'S':
        #     print("S")
        # elif chr(keycode) == 'F':
        #     print("F")
        # elif chr(keycode) == 'D':
        #     print("D")
        # elif keycode == wx.WXK_SPACE:
        #     print("SPACE")
        # elif chr(keycode) == 'E':
        #     print("E")
        # elif keycode == wx.WXK_NUMPAD_ENTER:
        #     print("RETURN")
        # elif chr(keycode) == 'Q':
        #     print("Q")
        #     # query()
        # elif chr(keycode) == 'H':
        #     print("H")
        # else:
        #     event.Skip()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()