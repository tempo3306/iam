import wx

class AP_App(wx.App):
    def OnInit(self):
        frame = AP_MainFrame("Test application", (0, 0), (650, 350))
        frame.Show()
        self.SetTopWindow(frame)

        loginPanel = AP_LoginPanel(frame)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        return True

    def OnCloseWindow(self, event):
        self.Destroy()


class AP_MainFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.CreateStatusBar()


class AP_LoginPanel(wx.Panel):
    def __init__(self, frame):
        self.panel = wx.Panel(frame)
        self.frame = frame

        self.frame.SetStatusText("Authentification required!")
        self.showLoginBox()

    def showLoginBox(self): #Create the sizer
        sizer = wx.FlexGridSizer(rows = 3, cols = 2, hgap = 5, vgap = 15)

        # Username
        self.txt_Username = wx.TextCtrl(self.panel, 1, size = (150, -1))
        lbl_Username = wx.StaticText(self.panel, -1, "Username:")

        sizer.Add(lbl_Username,0, wx.LEFT|wx.TOP| wx.RIGHT, 50)
        sizer.Add(self.txt_Username,0, wx.TOP| wx.RIGHT, 50)

        # Password
        self.txt_Password = wx.TextCtrl(self.panel, 1, size=(150, -1), style=wx.TE_PASSWORD)
        lbl_Password = wx.StaticText(self.panel, -1, "Password:")
        sizer.Add(lbl_Password,0, wx.LEFT|wx.RIGHT, 50)
        sizer.Add(self.txt_Password,0, wx.RIGHT, 50)

        # Submit button
        btn_Process = wx.Button(self.panel, -1, "&Login")
        self.panel.Bind(wx.EVT_BUTTON, self.OnSubmit, btn_Process)
        sizer.Add(btn_Process,0, wx.LEFT, 50)
        self.panel.SetSizer(sizer)

    def OnSubmit(self, event):
        UserText = self.txt_Username.GetValue()
        PasswordText = self.txt_Password.GetValue()


if __name__ == '__main__':
     app = AP_App()
     app.MainLoop()