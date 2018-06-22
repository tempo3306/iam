import wx

class TopPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnKeyDown(self, event):
        # 按键时相应代码
        # 	event.ControlDown
        kc = event.GetKeyCode()
        if 32 <= kc <= 126:
            print(kc)
            import win32gui
            win32gui.MessageBox(0,"test,ok!",'test',0)

        if event.AltDown():
            print('ff', kc)

class KeyEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        panel = TopPanel(self)

        # self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        self.Center()
        self.Show(True)




app = wx.App()
KeyEvent(None, -1, 'Test KeyDown Event of wxPython')
app.MainLoop()


# import wx
#
#
# class KeyEvent(wx.Frame):
#     def __init__(self, parent, id, title):
#         wx.Frame.__init__(self, parent, id, title)
#         panel = wx.Panel(self, -1)
#         panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
#         panel.SetFocus()
#
#         self.Centre()
#         self.Show(True)
#
#     def OnKeyDown(self, event):
#         print(event.GetKeyCode())
#
#         if event.GetKeyCode() == ord('f'):
#             print("ffff")
#             if self.GetPosition() == ((0, 0)):
#                 self.SetPosition((300, 300))
#                 self.SetSize((500, 300))
#             else:
#                 self.SetPosition((0, 0))
#                 self.SetSize(wx.DisplaySize())
#         if event.GetKeyCode() == ord('q'):
#             self.Close()
#         else:
#             event.Skip()
#
#
# app = wx.App()
# KeyEvent(None, -1, 'k.py')
# app.MainLoop()