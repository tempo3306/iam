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
from component.remote_control import web_request
# --------------------------------------------------------------------------------

import socket
from component.variable import get_val, set_val

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
        from component.remote_control import get_unique_id  ##获取硬盘ID
        host_ali = get_val('host_ali')
        debug = get_val('debug')
        # debug 模式

        diskid = get_val('diskid')
        target_url = '{0}/api/bid/get_guopaiurl/?format=json&type=identify_code&debug={1}&version={2}&identify_code={3}&diskid={4}'.format(
            host_ali, debug, version, identify_code, diskid
        )
        # target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
        print(target_url)

        result = web_request(target_url)
        set_val('type', 'identify_code')
        print(result)
    except:
        logger.error("登录出现异常")
        logger.exception('this is an exception message')
        return {'result': 'net error'}
    return result


# 登出
def Logout():  # 修改为参数传递
    from component.remote_control import get_unique_id  ##获取硬盘ID
    # debug 模式
    host_ali = get_val('host_ali')
    Identify_code = get_val('Identify_code')
    diskid = get_val('diskid')
    type = get_val('type')
    target_url = '{0}/api/bid/bid_logout/?type={1}&identify_code={2}&diskid={3}'.format(
        host_ali, type, Identify_code, diskid
    )
    # target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
    print(target_url)
    result = web_request(target_url)
    print(result)

    try:
        from component.remote_control import get_unique_id  ##获取硬盘ID
        # debug 模式
        host_ali = get_val('host_ali')
        Identify_code = get_val('Identify_code')
        diskid = get_val('diskid')
        type = get_val('type')
        target_url = '{0}/api/bid/bid_logout/?type={1}&identify_code={2}&diskid={3}'.format(
            host_ali, type, Identify_code, diskid
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

    # 发送登出信息
    # data = ['logout',Username,Password]
    # data=json.dumps(data)
    # data = bytes(data, encoding="utf-8")  #转化为BYTE
    # logging.info('发送信息 %s' % str(data,encoding="utf-8"))
    # s.send(data)
    # s.shutdown(1)
    # print("Submit Log Out Complete")
    # logging.info("Submit Log Out Complete")


def Keeplogin():
    try:
        from component.remote_control import get_unique_id  ##获取硬盘ID
        # debug 模式
        host_ali = get_val('host_ali')
        Identify_code = get_val('Identify_code')
        diskid = get_val('diskid')
        type = get_val('type')
        target_url = '{0}/api/bid/bid_keeplogin/?type={1}&identify_code={2}&diskid={3}'.format(
            host_ali, type, Identify_code, diskid
        )
        # target_url = host_ali + r'/main_api/userconfirm/info?' + 'username=%s' % Username + '&' + 'passwd=%s' % Password
        result = web_request(target_url)
    except:
        logger.error("keeplogin出现异常")
        logger.exception('this is an exception message')
        return {'result': 'net error'}
    return result

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
