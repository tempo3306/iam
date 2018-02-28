####################
# 参数
# id Topframe 1    Operationframe 2  guopaiweb 3 controlframe 4
# 无确认
# 新增验证码放大器功能
# 时间同步
import logging,time
timenow = time.time()
# 转换成localtime
time_local = time.localtime(timenow)
# 转换成新的时间格式(2016-05-09 18:59:20)
myapplog = time.strftime("%Y%m%d%H%M%S", time_local)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%s.log' % myapplog,
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
# ----------------------------------------------------------------
# 导入模块#####################
import sys

#判断运行平台
if sys.platform != 'win32':
    exit()

import pickle
import wx.adv
from PIL import Image
import os
from PIL import ImageGrab
#组件
from component.app_thread import cutimgThread,findposThread,HashThread
from component.app_thread import confirmThread,refreshThread,TijiaoThread,MoniTijiaoThread
from component.variable import set_val,get_val
from component.LoginFrame import LoginFrame
from component.variable import Create_hash,init_val

#--------------------------------------------------------------
#创建app
class SketchApp(wx.App):
    def OnInit(self):
        # try:
        #     bitmap = wx.Bitmap('start.png', wx.BITMAP_TYPE_PNG)
        #
        #     wx.adv.SplashScreen(bitmap, wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
        #                                  1500, None, -1, wx.DefaultPosition, size=(300,240),
        #                                 style=wx.BORDER_SIMPLE | wx.STAY_ON_TOP)
        #
        #     wx.Yield()
        # except:
        #     pass
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
    set_val('version', 1.01)
    ###获取路径
    allpath = os.path.abspath(os.path.realpath(sys.argv[0]))
    path = os.path.split(allpath)[0] + '\\'  # 分割
    set_val('path', path)
    iconpath = path + 'ico.ico'  # 图标路径
    set_val('mainicon', iconpath)
    app = SketchApp()
    ## 打开刷新与确认进程
    confirmthread = confirmThread()  #确认线程
    refreshthread = refreshThread()  #刷新线程
    finposthread = findposThread()   #定位线程
    cutimgthread = cutimgThread()   #截图线程
    tijiaoThread = TijiaoThread()  #提交
    # monitijaoThread = MoniTijiaoThread() #模拟提交
    app.MainLoop()

# self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
