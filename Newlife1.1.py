####################
# 参数
# id Topframe 1    Operationframe 2  guopaiweb 3 controlframe 4
# 无确认
# 新增验证码放大器功能
# 时间同步
import logging, time

version = '1.2s'  # 版本号
timenow = time.time()
# 转换成localtime
time_local = time.localtime(timenow)
# 转换成新的时间格式(2016-05-09 18:59:20)
myapplog = 'mylog'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%s.log' % myapplog,
                    filemode='w')

root = logging.getLogger()
print(root.name, type(root), root.parent, id(root))
# ----------------------------------------------------------------
# 导入模块#####################
import sys

# 判断运行平台
if sys.platform != 'win32':
    exit()

import pickle
import wx.adv
from PIL import Image
import os
from PIL import ImageGrab
# 组件
from component.app_thread import cutimgThread, findposThread
from component.app_thread import confirmThread, refreshThread, TijiaoThread, LowestpfriceThread
from component.variable import set_val
from component.LoginFrame import LoginFrame
from component.variable import Create_hash, init_val, get_val


# --------------------------------------------------------------
# 创建app
class SketchApp(wx.App):
    def OnInit(self):
        try:
            with open("your.name", 'rb') as name:
                namepsd = pickle.load(name)
                user = namepsd[0]
                psd = namepsd[1]
        except:
            user = 'shooter'  # 关闭
            psd = 0
        loginframe = LoginFrame('小鲜肉拍牌', user, psd)
        loginframe.Show(True)
        return True


if __name__ == '__main__':
    ## getwebpath()  # 初始化浏览器地址
    # 图片打开提速
    yimg = ImageGrab.grab().save("yanzhengma.png")
    yanzhengma_img = Image.open("yanzhengma.png")  # 打开图片的全局变量 ,提升第一次打开的速度
    set_val('yanzhengma_img', yanzhengma_img)
    # 变量初始化
    Create_hash()
    init_val()
    set_val('version', version)
    ###获取路径+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    path = get_val('path')
    iconpath = path + 'ico.ico'  # 图标路径
    set_val('mainicon', iconpath)
    app = SketchApp()
    ## 打开刷新与确认进程
    confirmthread = confirmThread()  # 确认线程
    refreshthread = refreshThread()  # 刷新线程

    finposthread = findposThread()  # 定位线程
    cutimgthread = cutimgThread()  # 截图线程
    tijiaoThread = TijiaoThread()  # 提交
    lowestThread = LowestpfriceThread()  #价格识别
    # monitijaoThread = MoniTijiaoThread() #模拟提交
    app.MainLoop()

# self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
