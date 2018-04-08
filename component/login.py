# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 10:37
'''
import smtplib
import os, logging
import mimetypes
import email
from email.mime.multipart import MIMEMultipart
from component.staticmethod import web_request
# --------------------------------------------------------------------------------

import socket
from component.variable import get_val

timeout = 10
socket.setdefaulttimeout(timeout)  # 设定截止时间

from urllib import request
import json
logger = logging.getLogger()  #返回根目录的logger

# 用户登录
def ConfirmUser(Username, Password, version):  # 修改为参数传递
    try:
        host_ali = get_val('host_ali')
        debug = get_val('debug')
        # debug 模式
        target_url = host_ali + r'/bid/bid_login/?' + 'username=%s' % Username + \
                     '&' + 'passwd=%s' % Password + '&' + 'version=%s' % version + '&' + "debug=%s" % debug
        # target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
        print(target_url)

        result = web_request(target_url)
        print(result)
    except:
        logger.error("登录出现异常")
        logger.exception('this is an exception message')
        return {'result': 'net error'}
    return result

def ConfirmCode(identify_code, version):  # 修改为参数传递
    try:
        host_ali = get_val('host_ali')
        debug = get_val('debug')
        # debug 模式


        target_url = '{0}/api/bid/get_guopaiurl/?type=identify_code&debug={1}&version={2}&identify_code={3}'.format(
            host_ali, debug, version, identify_code
        )

        # target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
        print(target_url)

        result = web_request(target_url)
        print(result)
    except:
        logger.error("登录出现异常")
        logger.exception('this is an exception message')
        return {'result': 'net error'}
    return result


# 登出
def Logout(Username):
    host_ali = get_val('host_ali')
    host = host_ali
    # host = raw_input("Plz imput destination IP:")
    # data = raw_input("Plz imput what you want to submit:")
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        # sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        # sys.exit(1)

    # 发送登出信息
    # data = ['logout',Username,Password]
    # data=json.dumps(data)
    # data = bytes(data, encoding="utf-8")  #转化为BYTE
    # logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    # s.send(data)
    # s.shutdown(1)
    # print("Submit Log Out Complete")
    # logging.info("Submit Log Out Complete")


def Keeplogin(Username, Password):
    host_ali = get_val('host_ali')
    host = host_ali
    # host = raw_input("Plz imput destination IP:")
    # data = raw_input("Plz imput what you want to submit:")
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        # sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        # sys.exit(1)

    # 发送确认信息
    data = ['keep', Username, Password]
    data = json.dumps(data)
    data = bytes(data, encoding="utf-8")  # 转化为BYTE
    s.send(data)

    s.shutdown(1)
    print("Submit keep Complete")


# --------------------------------------------------------------------------------
def send_mail(subject, to_list, file_name):
    data = open(file_name, 'rb')
    ctype, encoding = mimetypes.guess_type(file_name)
    if ctype is None and encoding is None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = email.mime.base.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    email.encoders.encode_base64(file_msg)
    basename = os.path.basename(file_name)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    to_list = to_list
    mail_host = 'smtp.qq.com'
    mail_user = os.environ.get('MAIL_USERNAME')
    mail_pass = os.environ.get('MAIL_PASSWORD')
    me = mail_user
    msg = MIMEMultipart()
    msg.attach(file_msg)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    server = smtplib.SMTP_SSL(mail_host, 465)  # SSL方式加密，QQ port:465
    server.login(mail_user, mail_pass)
    print('login in  successfully')
    server.sendmail(me, to_list, msg.as_string())
    server.quit()
    print('send email  successfully')


def Upload():
    pass  # 采集有用信息为将来分析准备
