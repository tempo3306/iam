# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/18 23:01
'''
import wx
import PIL
class PriceFrame(wx.Frame):
    def __init__(self,image,size,pos):

        wx.Frame.__init__(self, None, -1,'Price',size=size, pos=pos,
                          style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)
        self.panel=wx.Panel(self,size=size)
        #image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        self.bmp=wx.StaticBitmap(self.panel,-1,wx.Bitmap(image))
        self.Show()
        self.ShowImage()
#更换图片显示
    def ShowImage(self):
        img = wx.Bitmap(wx.Image('1.png',wx.BITMAP_TYPE_PNG))
        self.bmp.SetBitmap(img)

class App(wx.App):
    def OnInit(self):
        image = wx.Image("92100.png", wx.BITMAP_TYPE_PNG)
        self.frame = PriceFrame("92100.png", (300, 300), (900, 100))

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    # 打开刷新与确认进程
    # confirmthread = confirmThread()
    # confirmthread.pause()  # 暂停


    app.MainLoop()