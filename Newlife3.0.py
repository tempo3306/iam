####################
# 参数
# id Topframe 1    Operationframe 2  guopaiweb 3 controlframe 4
# 无确认
# 新增验证码放大器功能
# 时间同步
# ----------------------------------------------------------------
# 导入模块#####################
import sys

# 判断运行平台
if sys.platform != 'win32':
    exit()

import pickle
from component.LoginFrame import LoginFrame
from component.app_thread import *
from component.app_thread import Start_thread

# --------------------------------------------------------------
# 创建app
class SketchApp(wx.App):
    def OnInit(self):
        try:
            with open("your.name", 'rb') as name:
                namepsd = pickle.load(name)
                code = namepsd[0]
                # user = namepsd[0]
                # psd = namepsd[1]
        except:
            user = 'shooter'  # 关闭
            psd = 0
            code = ''
        loginframe = LoginFrame('沪牌一号', code)
        loginframe.Show(True)
        start_thread = Start_thread()  ##初始化线程， 加速启动
        return True



if __name__ == '__main__':
    import time
    a = time.time()
    app = SketchApp()
    app.MainLoop()
    ## 打开刷新与确认进程
    # monitijaoThread = MoniTijiaoThread() #模拟提交

##  self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
