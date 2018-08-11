from wx.tools.wxget import download_file
import wx

from component.variable import get_val
import requests


class UpdateFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(600, 300))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (100, 60), (250, 25), style=wx.GA_HORIZONTAL)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        # self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.OnIdle()

    def OnIdle(self, event=None):
        # self.count = self.count + 1
        # if self.count >= 80:
        #     self.count = 0


        # self.gauge.SetValue(self.count)

        url = 'http://192.168.3.20:3000/software_download/1.py/'
        self.download(url)


    def download(self, url):
        res = requests.get(url, stream=True)
        content_size = int(res.headers['content-length'])
        if res.status_code == 200:
            with open('1.py', 'wb') as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)
                    self.count += len(chunk)
                    self.gauge.SetValue(self.count/content_size * 100)

if __name__ == '__main__':
    app = wx.App()
    frame = UpdateFrame()
    frame.Show()
    app.MainLoop()

    # res = requests.get('http://192.168.3.20:3000/software_download/1.py/', stream=True)
    # if res.status_code == 200:
    #     with open('1.py', 'wb') as f:
    #         for chunk in res.iter_content(1024):
    #             f.write(chunk)