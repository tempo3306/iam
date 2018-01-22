# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/28 16:45
'''
import wx
import win32gui


class MyApp(wx.App):
    pass


class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'SetKey', size=(300, 200))
        panel = wx.Panel(self)
        button = wx.Button(panel, label='Press"Ctrl+s"', pos=(100, 80), size=(90, 24))
        self.Bind(wx.EVT_BUTTON, self.SetMessage, button)
        # 以下两行为设置快捷键代码
        accelTbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('S'), button.GetId())])
        self.SetAcceleratorTable(accelTbl)

    def SetMessage(self, event):
        win32gui.MessageBox(0, "test,ok!", 'test', 0)


if __name__ == '__main__':
    app = MyApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()