#!/usr/bin/env python
# coding=utf-8

import cv2 as cv2
import numpy as np
import time
from libs.adb import adbKit

def main1():
    img = cv2.imread("test.jpg")
    cv2.namedWindow("Image")
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

from libs import adb

def main2():
    adbkit = adb.adbKit()
    adbkit.screenshots()

def main3():
    import cv2
    import numpy as np

    from libs import adb

    adbkit = adb.adbKit()
    adbkit.connectSimulator()

    '''find_img = cv2.imread("images/btn_chuangguan.jpg")

    adbkit.screenshots()
    target_img = cv2.imread("screencap.png")

    result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.5)
    for pt in zip(*loc[::-1]):
        print(pt)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, max_val, min_loc, max_loc)

    find_height, find_width, find_channel = find_img.shape[::]
    # 计算位置
    pointUpLeft = max_loc
    pointLowRight = (max_loc[0] + find_width, max_loc[1] + find_height)
    pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))

    # 画点
    cv2.circle(target_img, pointUpLeft, 2, (255, 255, 255), -1)
    cv2.circle(target_img, pointCentre, 2, (255, 255, 255), -1)
    cv2.circle(target_img, pointLowRight, 2, (255, 255, 255), -1)

    # 显示图片
    cv2.namedWindow("Image")
    cv2.imshow("Image", target_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    adbkit.click(pointCentre)'''

    threshold = 0.8 # 0.5 会将确定与闯关误判

    '''find_img = cv2.imread("images/btn_zhidong.jpg")
    ret, result, target_img = isFound(adbkit, find_img, threshold= threshold)
    if ret:
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            print('0', pt)

    find_img = cv2.imread("images/btn_queding.jpg")
    ret, result, target_img = isFound(adbkit, find_img, threshold= threshold) # 0k: 0.9
    if ret:
        #for pt in result_points:
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            print('1', pt)

    find_img = cv2.imread("images/btn_chuangguan.jpg")
    ret, result, target_img = isFound(adbkit, find_img,  threshold= threshold) # 0k: 0.5; not ok: 0.6
    if ret:
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
            print('2', pt)

    left, center, right = getBtnLoc(adbkit, find_img)
    if center is not None:
        cv2.circle(target_img, left, 2, (255, 255, 255), -1)
        cv2.circle(target_img, center, 2, (255, 255, 255), -1)
        cv2.circle(target_img, right, 2, (255, 255, 255), -1)

        # 显示图片
        cv2.namedWindow("Image")
        cv2.imshow("Image", target_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #adbkit.click(center)


    find_img = cv2.imread("images/btn_tiaoguo.jpg")
    ret, result, target_img = isFound(adbkit, find_img)
    if ret:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(min_val, max_val, min_loc, max_loc)

        find_height, find_width, find_channel = find_img.shape[::]
        # 计算位置
        pointUpLeft = max_loc
        pointLowRight = (max_loc[0] + find_width, max_loc[1] + find_height)
        pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))

        # 画点
        cv2.circle(target_img, pointUpLeft, 2, (255, 255, 255), -1)
        cv2.circle(target_img, pointCentre, 2, (255, 255, 255), -1)
        cv2.circle(target_img, pointLowRight, 2, (255, 255, 255), -1)

        # 显示图片
        cv2.namedWindow("Image")
        cv2.imshow("Image", target_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        adbkit.click(pointCentre)

    #adbkit.screenshots() '''

    find_img = cv2.imread("images/btn_queding.jpg")
    while (True):
        left, center, right = getBtnLoc(adbkit, find_img)
        if center is not None:
            '''cv2.circle(target_img, left, 2, (255, 255, 255), -1)
            cv2.circle(target_img, center, 2, (255, 255, 255), -1)
            cv2.circle(target_img, right, 2, (255, 255, 255), -1)

            # 显示图片
            cv2.namedWindow("Image")
            cv2.imshow("Image", target_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''
            print('found')
            adbkit.click(center)
            break
        else:
            print('not found')
            time.sleep(0.5)

        '''target_img = cv2.imread("screencap.png")
        find_img = cv2.imread("images/btn_tiaoguo.jpg")

        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(min_val, max_val, min_loc, max_loc)

        find_height, find_width, find_channel = find_img.shape[::]
        # 计算位置
        pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))

        adbkit.click(pointCentre)'''


def main4():
    adbkit = adb.adbKit()
    adbkit.connectSimulator()

    threshold = 0.8

    '''find_img = cv2.imread("images/btn_zhidong_enabled.jpg")
    left, center, right = getBtnLoc(adbkit, find_img, threshold = threshold)
    if center is not None:
        print('found')
    else:
        print('not found')

    find_img = cv2.imread("images/btn_zhidong_disabled.jpg")
    left, center, right = getBtnLoc(adbkit, find_img, threshold = threshold)
    if center is not None:
        print('found')
    else:
        print('not found')'''

    '''img_str = "images/btn_zhidong_disabled.jpg"
    found = waitToClickImgStr(adbkit, img_str, timeout_ms=2, threshold=threshold)
    str = 'found %s: %s' % (img_str, found)
    print(str)'''

    while(True):
        print("wait for chuangguan")
        img_str = "images/btn_chuangguan.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms= 6000)
        str = 'found %s: %s' % (img_str, found)
        print(str)

        img_str = "images/btn_tiaoguo.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms=80000)
        str = 'found %s: %s' % (img_str, found)
        print(str)

        img_str = "images/btn_zhidong_enabled.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms=5000, threshold= threshold)
        str = 'found %s: %s' % (img_str, found)
        print(str)

        img_str = "images/btn_tiaoguo.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms=80000)
        str = 'found %s: %s' % (img_str, found)
        print(str)

        img_str = "images/dianjijixu.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms=80000)
        str = 'found %s: %s' % (img_str, found)
        print(str)

        img_str = "images/btn_zaicitiaozhan.jpg"
        found = waitToClickImgStr(adbkit, img_str, timeout_ms=5000)
        str = 'found %s: %s' % (img_str, found)
        print(str)

def isFound(adbkit, find_img, threshold = 0.8):
    adbkit.screenshots()
    target_img = cv2.imread("screencap.png")

    result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    result_points = zip(*loc[::-1])
    if len(list(result_points)) > 0:
        return True, result, target_img
    else:
        return False, result, target_img
    #for pt in zip(*loc[::-1]):
    #    print(pt)

def getBtnLoc(adbkit, find_img, threshold = 0.8):
    ret, result, target_img = isFound(adbkit, find_img, threshold)
    if ret:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        find_height, find_width, find_channel = find_img.shape[::]
        # 计算位置
        pointUpLeft = max_loc
        pointLowRight = (max_loc[0] + find_width, max_loc[1] + find_height)
        pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))
        return pointUpLeft, pointCentre, pointLowRight
    else:
        return None, None, None


def waitToClickImgStr(adbkit, find_img_str, timeout_ms = 0, threshold = 0.8):
    find_img = cv2.imread(find_img_str)
    found = waitToClick(adbkit, find_img, timeout_ms, threshold=threshold)
    return found

def waitToClick(adbkit, find_img, timeout_ms = 0, threshold = 0.8):
    start_time = int(time.time() * 1000)
    found = False
    while (True):
        left, center, right = getBtnLoc(adbkit, find_img, threshold)
        if center is not None:
            #print('found')
            adbkit.click(center)
            found = True
            break
        else:
            if timeout_ms != 0:
                elapsed = int(time.time() * 1000) - start_time
                # 做完一部分任务后,判断是否超时
                if elapsed >= timeout_ms:
                    found = False
                    break
            else:
                pass
            time.sleep(0.5)
    return found

from libs.checker import Checker
from datetime import datetime

def tuichudenglu(adbkit, checker):
    adbkit.screenshots()
    screen_img = cv2.imread("screencap.png")
    btn_center = checker.chckImgAndClick(screen_img, "images/btn_settings.jpg", click=True)
    adbkit.screenshots()
    screen_img = cv2.imread("screencap.png")
    btn_center = checker.chckImgAndClick(screen_img, "images/btn_tuichudenglu.jpg", click=True)
    adbkit.screenshots()
    screen_img = cv2.imread("screencap.png")
    btn_center = checker.chckImgAndClick(screen_img, "images/btn_queding.jpg", click=True)

def main5():
    adbkit = adbKit()
    adbkit.connectSimulator()

    threshold = 0.7  #0.8 对于fanhui会判断失误
    checker = Checker(adbkit, threshold)
    i = 0
    print('Start')
    last_time = None
    while (True):
        adbkit.screenshots()
        screen_img = cv2.imread("screencap.png")

        '''checker.setThreshold(0.9)
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_zhidong_enabled.jpg", click=False)
        if btn_center is not None:
            checker.clickBtn(btn_center)
            print('enabled')

        screen_img = cv2.imread("screencap.png")
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_zhidong_disabled.jpg", click=False)
        if btn_center is not None:
            checker.clickBtn(btn_center)
            print('disabled')

        screen_img = cv2.imread("screencap.png")
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_zhidong_enabled.jpg", click=False)
        if btn_center is not None:
            print('test')'''

        #btn_center = checker.chckImgAndClick(screen_img, "images/btn_fanhui.jpg", click= False)
        checker.setThreshold(0.8)
        #btn_center = checker.chckImgAndClick(screen_img, "images/btn_fanhui.jpg", click= False)
        #btn_center = checker.chckImgAndClick(screen_img, "images/money_0.jpg", click=False) #0.7会判断出错
        #btn_center = checker.chckImgAndClick(screen_img, "images/btn_fanhui1.jpg", click=False)

        btn_center = checker.chckImgAndClick(screen_img, "images/btn_chuangguan.jpg", click= False)
        if btn_center is not None:
            i += 1
            interval = checker.calculateInterval()
            #str = datetime.strftime(datetime.now(), "%H:%M:%S") #"%Y%m%d %H:%M:%S")
            print('[%.2f]-run times: %d' % (interval, i))
            checker.calculateInterval(reset= True)
            checker.clickBtn(btn_center)
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_queding.jpg")
        if btn_center is not None:
            print('btn_queding')
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_tiaoguo.jpg")
        if btn_center is not None:
            print('btn_tiaoguo')
        checker.setThreshold(0.9)
        btn_center = checker.chckImgAndClick(screen_img, "images/btn_zhidong_disabled.jpg")
        if btn_center is not None:
            print('btn_zhidong_disabled')
        #checker.setThreshold(0.7)
        btn_center = checker.chckImgAndClick(screen_img, "images/dianjijixu.jpg")
        if btn_center is not None:
            print('dianjijixu')
        btn_center = checker.chckImgAndClick(screen_img, "images/money_0.jpg", click= False, threshold = 0.8)
        if btn_center is not None:
            interval = checker.calculateInterval()
            print('[%f]-No more money, return' % (interval))
            checker.chckImgAndClick(screen_img, "images/btn_fanhui1.jpg", threshold = 0.7) #btn_fanhui在0.8会判断不了
            break
        else:
            btn_center = checker.chckImgAndClick(screen_img, "images/btn_zaicitiaozhan.jpg")
            if btn_center is not None:
                print('btn_zaicitiaozhan')
        time.sleep(1)

    tuichudenglu(adbkit, checker)

from libs.utils import *

def main_logic(checker, screen_img):
    btn_center = checker.chckImgAndClick(screen_img, "images/icon_oa_old.png", threshold=0.7)
    if btn_center is not None:
        print('oa icon is clicked')

    btn_center = checker.chckImgAndClick(screen_img, "images/btn_yonghuming.png", threshold=0.7)
    if btn_center is not None:
        print('yonghuming is clicked')

    btn_center = checker.chckImgAndClick(screen_img, "images/oa_login.png", threshold=0.5)
    if btn_center is not None:
        print('test is clicked')

def main6(restart = False):
    if restart:
        stop_android_devices()
        start_android_devices()

    adbkit = adbKit()
    adbkit.connectSimulator()

    threshold = 0.6  # 0.8 对于fanhui会判断失误
    checker = Checker(adbkit, threshold)
    i = 0
    print('Start')
    last_time = None
    while (True):
        adbkit.screenshots()
        screen_img = cv2.imread("screencap.png")
        try:
            main_logic(checker, screen_img)
        except Exception as e:
            time.sleep(2)
            print('not started yet')
            continue
        #main_logic(checker, screen_img)

        time.sleep(0.1)

if __name__ == "__main__":
    #process_checkin('checkin')
    #main3()
    #main5()
    #imei: adb -s 127.0.0.1:5555 shell setprop phone.imei 99001145449367
    main6()
