#!/usr/bin/env python
# coding=utf-8

"""ADB"""


import os
import subprocess

Device = '127.0.0.1:7555 ' #mumu
#Device = '127.0.0.1:5555 ' #雷电

# https://rustfisher.github.io/2017/07/05/Python_note/Python-adb/
class adbKit(object):
    """ Provides some adb methods """

    def screenshots(self, serialNumber=Device):
        # 'adb shell screencap -p /sdcard/screencap.png')
        self.command('shell screencap -p /sdcard/screencap.png', serialNumber)
        self.command('pull /sdcard/screencap.png', serialNumber)

    def command(self, cmd, serialNumber=Device):
        cmdstr = 'adb'
        if serialNumber:
            cmdstr = cmdstr + ' -s ' + serialNumber
        cmdstr = '%s %s'%(cmdstr, cmd)

        result = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return result
        #(status, output) = commands.getstatusoutput(cmdstr + cmd)
        #return [status, output]

    def click(self, point, serialNumber=Device):
        return self.command('shell input tap ' + str(point[0]) + ' ' + str(point[1]), serialNumber)

    def connectSimulator(self, serialNumber=Device):
        cmdstr = 'adb connect %s' % serialNumber
        subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    @staticmethod
    def pull_sd_dcim(device, target_dir='E:/files'):
        """ Pull DCIM files from device """
        print( "Pulling files")
        des_path = os.path.join(target_dir, device)
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        print(des_path)
        cmd = "adb pull /sdcard/DCIM/ " + des_path
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print(result)
        print("Finish!")
        return des_path

