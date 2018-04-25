# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/3/13 11:22
'''

##远程连接服务器
# 网络请求
# Add "sys.coinit_flags = 0" after your "import sys" line and
# before the "import pythoncom" line. That worked for me, although I don't know why.

import os, sys
sys.coinit_flags = 0
import pythoncom
import time
import wmi
import logging
from urllib import request
logger = logging.getLogger()  #返回根目录的logger

def web_request(url):
    import ssl, json
    # ssl._create_default_https_context = ssl._create_unverified_context  # 关闭证书验证
    # response = requests.get(url, timeout=5)
    # print(response)
    # if response.status_code == 404:
    #     result = {'result': 'wrong account'}
    #     return result
    # else:
    #     result = response.content
    #     result = str(result, encoding='utf-8')
    #     result = json.loads(result)
    #     return result

    try:
        ssl._create_default_https_context = ssl._create_unverified_context  # 关闭证书验证
        response = request.urlopen(url)
        if response.status == 404:
            result = {'result': 'wrong account'}
            return result
        else:
            result = response.read()
            result = str(result, encoding='utf-8')
            result = json.loads(result)
            return result
    except Exception as e:
        print(e)
        logger.exception('this is an exception message')
        result = {'result': 'timeout'}
        return result


def get_unique_id():
    c = wmi.WMI()
    try:
        for physical_disk in c.Win32_DiskDrive():
            encrypt_str = physical_disk.SerialNumber.strip()

            # 硬盘序列号
            diskid = physical_disk.SerialNumber.strip()
            print ('disk id:', physical_disk.SerialNumber.strip())
            return diskid
    except:
        return None






###################-----------------
# def get_cpu_info():
#     tmpdict = {}
#     tmpdict["CpuCores"] = 0
#     c = wmi.WMI()
#     #          print c.Win32_Processor().['ProcessorId']
#     #          print c.Win32_DiskDrive()
#     for cpu in c.Win32_Processor():
#         #                print cpu
#         print ("cpu id:", cpu.ProcessorId.strip())
#         tmpdict["CpuType"] = cpu.Name
#         try:
#             tmpdict["CpuCores"] = cpu.NumberOfCores
#         except:
#             tmpdict["CpuCores"] += 1
#             tmpdict["CpuClock"] = cpu.MaxClockSpeed
#             return tmpdict
#
#
# def _read_cpu_usage():
#     c = wmi.WMI()
#     for cpu in c.Win32_Processor():
#         return cpu.LoadPercentage
#
#
# def get_cpu_usage():
#     cpustr1 = _read_cpu_usage()
#     if not cpustr1:
#         return 0
#     time.sleep(2)
#     cpustr2 = _read_cpu_usage()
#     if not cpustr2:
#         return 0
#     cpuper = int(cpustr1) + int(cpustr2) / 2
#     return cpuper
#
#
# def get_disk_info():
#     tmplist = []
#     encrypt_str = ""
#     c = wmi.WMI()
#     for cpu in c.Win32_Processor():
#         # cpu 序列号
#         encrypt_str = encrypt_str + cpu.ProcessorId.strip()
#         print ("cpu id:", cpu.ProcessorId.strip())
#     for physical_disk in c.Win32_DiskDrive():
#         encrypt_str = encrypt_str + physical_disk.SerialNumber.strip()
#
#         # 硬盘序列号
#         print ('disk id:', physical_disk.SerialNumber.strip())
#         tmpdict = {}
#         tmpdict["Caption"] = physical_disk.Caption
#         tmpdict["Size"] = int(physical_disk.Size) / 1000 / 1000 / 1000
#         tmplist.append(tmpdict)
#     for board_id in c.Win32_BaseBoard():
#         # 主板序列号
#         encrypt_str = encrypt_str + board_id.SerialNumber.strip()
#         print ("main board id:", board_id.SerialNumber.strip())
#     #          for mac in c.Win32_NetworkAdapter():
#
#     # mac 地址（包括虚拟机的）
#     #                    print "mac addr:", mac.MACAddress:
#     for bios_id in c.Win32_BIOS():
#         # bios 序列号
#         encrypt_str = encrypt_str + bios_id.SerialNumber.strip()
#         print ("bios number:", bios_id.SerialNumber.strip())
#     print ("encrypt_str:", encrypt_str)
#
#     # 加密算法
#     # print (zlib.adler32(encrypt_str))
#     return encrypt_str
#
#
# if __name__ == "__main__":
#     #     a = get_cpu_info()
#     get_disk_info()
#
#
