# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2017/12/20 15:47
'''
import wx


class FirseFrame(wx.Frame):
    def __init__(self, parent=None, id=1, title='', pos=wx.DefaultPosition, size=(400,400), style= wx.DEFAULT_FRAME_STYLE):
        """
        wx.Frame() 构造函数参数说明 :
        wx.Frame.__init__(self, Window parent, int id=-1, String title=EmptyString,
            Point pos=DefaultPosition, Size size=DefaultSize,
           long style=DEFAULT_FRAME_STYLE, String name=FrameNameStr) -> Frame
        """
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.panel=wx.Panel(self, -1)
        self.f1=YanzhengmaFrame()

        self.f1.Show()
        self.b1 = wx.Button(self.panel,label='按我1',pos=(100,100))
        self.b2 = wx.Button(self.panel,label='按我2',pos=(100,200))
        self.b1.Bind(wx.EVT_BUTTON,self.clf1)
        self.b2.Bind(wx.EVT_BUTTON,self.show_f1)

        # self.f2=1


    def clf1(self,event):
        # t2=self.FindWindowById(8)
        # t2.Destroy()
        f2=YanzhengmaFrame2()
        f2.Show()

    def show_f1(self,event):
        print("f2")
        y=self.FindWindowById(2)
        print("y",y)
        y.Destroy()
        # y = self.FindWindowById(3)
        # y.Show(True)
        # print(y)



class YanzhengmaFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 2,'Price',style=wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP,size=(80,80)
                          )
        self.panel=wx.Panel(self)
        #image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        self.bmp=wx.StaticBitmap(self.panel,-1)
        # 更换图片显示
    def ShowImage(self,bm):
        self.bmp.SetBitmap(wx.Bitmap(bm))

class YanzhengmaFrame2(wx.Frame):
    def __init__(self, parent=None, id=3, title='', pos=wx.DefaultPosition, size=wx.DefaultSize, style= wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        self.panel=wx.Panel(self)
        #image=wx.Image(path,wx.BITMAP_TYPE_PNG)
        self.bmp=wx.StaticBitmap(self.panel,-1)
        # 更换图片显示
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self,event):
        y=self.FindWindowById(2)
        print(y)
        y.Destroy()
        event.Skip()


class MainApp(wx.App):
    def OnInit(self):
        self.frame = FirseFrame( title=u'第一个窗口', pos=(10, 10), size=(400, 400))
        self.frame.Show()

        return True

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == "__main__":
    main()