# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/18 21:03
'''
import wx
class Frame(wx.Frame):
    """Frame class that displays an image."""
    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition, title='Hello, wxPython!'):
        """Create a Frame instance and display image."""
        wx.Frame.__init__(self, parent, id, title, pos)
        panel = wx.Panel(self)
        self.bmp = wx.StaticBitmap(parent=panel,image)
class App(wx.App):
    """Application class."""
    def OnInit(self):
        # create a image object
        image = wx.Image('sc.png', wx.BITMAP_TYPE_PNG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
def main():
    app = App()
    app.MainLoop()
if __name__ == '__main__':
    main()