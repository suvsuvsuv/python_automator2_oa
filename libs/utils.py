# -*- coding: utf-8 -*-

import os
import subprocess
import re

# https://testerhome.com/topics/11500
def start_android_devices():
    '''启动雷电安卓模拟器'''
    command = r'start D:\Changzhi\dnplayer2\dnplayer.exe'
    os.system(command)
    print('simulator is starting')

def stop_android_devices():
    '''结束安卓模拟器进程'''
    command = r'taskkill -f -im dnplayer.exe'
    os.system(command)
    print('simulator is killed')

import time

# https://stackoverflow.com/questions/2785821/is-there-an-easy-way-in-python-to-wait-until-certain-condition-is-true
def wait_until(func, timeout_in_seconds, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout_in_seconds
    while time.time() < mustend:
        ret = func(*args, **kwargs)
        if ret is not None or ret: return True
        time.sleep(period)
    return False

# https://blog.csdn.net/qq_41664526/article/details/81144221
def finddevices():
    data = subprocess.Popen('adb devices', stdout=subprocess.PIPE, universal_newlines=True)
    data_info = data.stdout.read()
    devices = re.findall(r'(.*?)\s+device', data_info)
    if len(devices) > 1:
        deviceIds = devices[1:]
        print('共找到%s个手机' % str(len(devices) - 1))
        for i in deviceIds:
            print('ID为%s' % i)
        return deviceIds
    else:
        print('没有找到手机，请检查')
        return

def waitTest():
    print('test')
    return True

if __name__ == "__main__":
    wait_until(waitTest, 5)