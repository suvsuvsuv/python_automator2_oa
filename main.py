#!/usr/bin/env python
# coding=utf-8


import random

from libs.qqmail import *
from libs.utils import *
from oa.oa import OA
from simulator.leidian import LeiDian
from appConstants import *

def checkIn(restart = True, check_in = True):
    if restart:
        stop_android_devices()
        start_android_devices()

    leidian = LeiDian()
    #leidian.chair()
    print('waiting leidian')
    time.sleep(10)
    d = leidian.wait_connect()
    if d is None:
        print('Failed to connect simulator')
        return
    leidian.cleanTempJPG()

    oa = OA(d)
    oa.run_app()
    logined = oa.checkIfLogin()
    if logined is None:
        print('Failed to login')
        return
    if not logined:
        oa.login_app(OA_USER_NAME, OA_PASS_WORD)
    temp_jpg = leidian.getTempJPGName()
    checkin = oa.click_checkin(filename=temp_jpg, click_checkin=check_in)
    if checkin:
        print('done')
    else:
        print('not ok')

    oa.logout()
    time.sleep(1)
    oa.stop_app()

    time.sleep(1)
    stop_android_devices()
    return temp_jpg


def send_okmail_toqq():
    #send_mail('368029724', 'zrksshkomyrpcaea', '368029724@qq.com', 'auto checkin', 'i am alive')
    #send_mail('1043990501', 'lkrexkrvckvbbdda', '1043990501@qq.com', 'auto checkin: I_am_ok', '')
    timeAll = show_time()
    send_email(send_username, send_password, 'I_m_ok', timeAll)


def send_resultmail_toqq(cmd, result_jpg):
    if cmd.startswith('checkin'):
        subject = 'checkin'
    else:
        subject = 'login'
    #filename = 'result.jpg'
    send_email(send_username, send_password, cmd, '', result_jpg)

def process_checkin(cmd):
    isCheckin = False
    if cmd.startswith('checkin'):
        isCheckin = True
    result_jpg = checkIn(check_in=isCheckin)
    time.sleep(0.5) #delay 0.5s
    send_resultmail_toqq(cmd, result_jpg)

def add_time(timeStr):
    timeList.append(timeStr)

def get_time():
    if len(timeList) > 0:
        timeStr = timeList[0]
        del timeList[0]
    else:
        timeStr = None
    return timeStr

def show_time():
    timeAll = ''
    for str in timeList:
        timeAll = timeAll+ str + "    "
    return timeAll

default_morning = '08:40'
default_evening = '18:30'

default_morning = '08:30'
default_evening = '18:30'

def generateTime(min):
    min = min + random.randint(0, 8)
    return str(min)

def create_time_list():
    del timeList[:]
    ll = default_morning.split(':')
    min = int(ll[1])
    str = ll[0] +':' + generateTime(min)
    add_time(str)
    ll = default_evening.split(':')
    min = int(ll[1])
    str = ll[0] + ':'+ generateTime(min)
    add_time(str)
    print(show_time())

def check_timeList(mytime):
    #print mytime
    strTime = mytime
    if len(timeList) > 0:
        for time in timeList:
            if time == strTime:
                timeList.remove(time) # 3.删除指定值的元素
                return 'checkin'
                '''print 'auto checkin: ' + strTime
                process_checkin('checkin')
                print '---------------------'
                '''

timeList = []

def main():
    print('robot is runing...')

    '''add_time("08:35")
    add_time("18:43")
    print show_time()
    send_okmail_toqq()
    print get_time()
    print get_time()
    print get_time()
    '''

    '''create_time_list()
    print show_time()
    mydate = datetime.datetime.now()
    check_timeList(mydate.strftime("%H:%M"))
    '''
    # process_checkin('login')

    day = -1
    while True:
        mydate = datetime.datetime.now()
        strShortTime = mydate.strftime("%H:%M")
        nowDay = mydate.day
        if (day != nowDay):
            day = nowDay
            # create_time_list()

        cmd = imap4("imap.qq.com", 993, RECEIVE_IMAP_USER, RECEIVE_IMAP_PWD, True)
        if cmd is None:
            cmd = check_timeList(strShortTime)
        if cmd is not None:
            strTime = mydate.strftime("%Y-%m-%d %H:%M:%S")
            if cmd.startswith('checkin'):
                print('check in: ' + strTime)
                process_checkin(cmd)
                print('---------------------')
            elif cmd.startswith('login'):
                print('log in: ' + strTime)
                process_checkin(cmd)
                print('---------------------')
            elif cmd.startswith('auto'):
                print('create time: ' + strTime)
                create_time_list()
                send_okmail_toqq()
                print('---------------------')
            elif cmd.startswith('clear'):
                print('clear: ' + strTime)
                timeList.clear()
                send_okmail_toqq()
                print('---------------------')
            else:
                print('send ok mail: ' + strTime)
                send_okmail_toqq()
                print('---------------------')
                # print cmd
        time.sleep(5)

if __name__ == "__main__":
    '''check_in = False
    check_in = True
    checkIn(check_in=check_in) '''
    main()
    #create_time_list()
