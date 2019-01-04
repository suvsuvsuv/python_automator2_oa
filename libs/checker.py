#!/usr/bin/env python
# coding=utf-8

from libs.adb import adbKit
import cv2 as cv2
import numpy as np
#import time
from datetime import  datetime

class Checker(object):
    def __init__(self, adbkit, threshold = 0.8):
        self.adbkit = adbkit
        self.threshold = threshold
        self.last_time = None

    def setThreshold(self, threshold):
        self.threshold = threshold

    def isFound(self, find_img):
        self.adbkit.screenshots()
        target_img = cv2.imread("screencap.png")

        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= self.threshold)
        result_points = zip(*loc[::-1])
        if len(list(result_points)) > 0:
            return True, result, target_img
        else:
            return False, result, target_img

    def getBtnLoc(self, find_img):
        ret, result, target_img = self.isFound(find_img)
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

    def clickBtn(self, btn_center):
        if btn_center is not None:
            self.adbkit.click(btn_center)

    '''def clickBtnCenter(self):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.result)
        find_height, find_width, find_channel = self.find_img.shape[::]
        # 计算位置
        pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))
        self.clickBtn(pointCentre)'''

    def getBtnCenter(self, find_img, result):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        find_height, find_width, find_channel = find_img.shape[::]
        # 计算位置
        pointCentre = (max_loc[0] + int(find_width / 2), max_loc[1] + int(find_height / 2))
        return pointCentre

    def chckImgAndClick(self, screen_img, find_img_str, click = True, show_result= False, threshold = 0):
        if threshold > 0:
            self.threshold = threshold
        find_img = cv2.imread(find_img_str)
        result = cv2.matchTemplate(screen_img, find_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= self.threshold)
        result_points = zip(*loc[::-1])
        if len(list(result_points)) > 0:
            btn_center = self.getBtnCenter(find_img, result)
            if show_result:
                print('found %s' % (find_img_str))
            if click:
                self.clickBtn(btn_center)
        else:
            btn_center = None
        '''if show_result:
            print('found %s: %s' % (find_img_str, found))'''
        return btn_center

    def calculateInterval(self, reset= False):
        now = datetime.now()
        if reset:
            self.last_time = now
            return 0
        if self.last_time is None:
            self.last_time = now
            total_sec = 0
        else:
            interval = now - self.last_time
            #print(now, self.last_time, interval, end = ' ')
            self.last_time = now
            total_sec = interval.total_seconds()
            #print(total_sec)
        return total_sec
