# -*- coding:UTF-8 -*-
import os
import subprocess
from time import sleep
from optparse import OptionParser
import uiautomator2 as u2

from libs.utils import wait_until

SIMULATOR = '127.0.0.1:5555'
class LeiDian(object):
    def __init__(self):
        # 启动虚拟机
        self.start_vm = 'dnconsole.exe launch --name  %d'
        # 新增虚拟机
        self.add_vm = 'dnconsole.exe add --name %d'
        # 修改分辨率
        self.alter_ratio = 'dnconsole.exe modify --index %d --resolution 1440,810,260'
        # 安装app
        self.install_app = 'dnconsole.exe installapp --index %d --filename %s'
        # app路径
        self.app_path = 'D:\\Changzhi\Facebook_x86_128.apk'
        # dnconsole.exe路径
        self.ld_path = 'D:\\Changzhi\dnplayer2'
        # 查看虚拟机所有信息
        self.all_vm_info = 'doconsole.exe list2'

    # 切换目录
    def chair(self):
        try:
            retval = os.getcwd()
            print("当前工作目录为 %s" % retval)
            # 切换到当前路径
            os.chdir(self.ld_path)
            # 查看修改后的工作目录
            retval2 = os.getcwd()
            print("当前工作目录已修改为 %s" % retval2)
        except Exception as e:
            print(e)
        else:
            self.view_vm(index=61)

    # 查看虚拟机
    def view_vm(self, index):
        data = subprocess.Popen('dnconsole.exe list2', stdout=subprocess.PIPE, universal_newlines=True)
        # 虚拟机全部信息
        # data_info = data.stdout.read()
        number_list = []
        for line in data.stdout:
            # 含有换行符
            info = line.strip().split(',')
            vm_number = info[1]
            number_list.append(vm_number)
        if str(index) in number_list:
            print('该虚拟机已经存在')
        else:
            self.make_vm(index=index)

    # 创建模拟器
    def make_vm(self, index):
        subprocess.call(self.add_vm % index)
        print('创建模拟器{}成功!'.format(index))
        subprocess.call(self.alter_ratio % index)
        print('修改模拟器{}分辨率成功!'.format(index))
        subprocess.call(self.start_vm % index)
        print('启动模拟器{}'.format(index))
        '''print('开始安装Facebook!')
        code = subprocess.call(self.install_app % (index, self.app_path))
        if code == 0:
            sleep(60)
            print('安装Facebook成功!')
        print('开始安装uiautomator2!')
        subprocess.call('python -m uiautomator2 init')
        print('安装uiautomator2成功!')'''

    def connect(self):
        try:
            self.d = u2.connect_usb(SIMULATOR)
            return self.d
        except Exception as e:
            print(e)
            return None
        # 全局设置,每个ui点击之后休眠1.5s
        '''self.d.click_post_delay = 1.5
        hrp = htmlreport.HTMLReport(self.d)
        hrp.patch_click() '''


    def wait_connect(self, timeout = 15):
        ret = wait_until(self.connect, timeout)
        if ret:
            return self.d
        else:
            return None

    # 连接测试
    def link_test(self):
        if self.d.info['naturalOrientation'] == True:
            print('设备连接正常!')
            return self.d
        else:
            print('设备连接出现问题!请检查后重试!')
            return None

    def takeScreenShort(self):
        filename = self.getTempJPGName()
        self.d.screenshot(filename)

    def cleanTempJPG(self):
        filename = self.getTempJPGName()
        if os.path.exists(filename):
            os.remove(filename)

    def getTempJPGName(self):
        FILE = 'result.jpg'
        cwd = os.getcwd()
        if cwd.__contains__('simulator'):
            filename = os.path.join('../temp', FILE)
        else:
            filename = os.path.join('./temp', FILE)
        return filename

if __name__ == '__main__':
    leidian = LeiDian()
    #leidian.chair()
    #leidian.make_vm()
    leidian.connect()
    #leidian.link_test()
    leidian.cleanTempJPG()
    leidian.takeScreenShort()
    '''leidain.run_app()
    leidain.login_app()
    leidain.click_checkin() '''
    #d = u2.connect_usb(SIMULATOR)
    #d.screenshot("result.jpg")

