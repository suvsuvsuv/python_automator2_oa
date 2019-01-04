# -*- coding:UTF-8 -*-

from appConstants import *

class OA:
    def info(self):
        '''
        package: com.yy.oa 
        1:
        text : 用户名
        class id: com.yy.oa:id/oa_user_id
        
        2:
        class id: com.yy.oa:id/oa_password
        
        3: 
        classid : com.yy.oa:id/oa_btn_login
        
        4:
        classid: android.widget.Image, index : 12
        5:
        d(resourceId="android:id/alertTitle")
        6:
        d(resourceId="android:id/button1")  # 确定
        7:
        d(description=u"庄旭晖")
        '''

    def __init__(self, d):
        self.d = d

    # 运行app
    def run_app(self):
        # 先返回主菜单界面
        self.d.press('home')
        # self.d(text="移动OA").click()
        self.d.app_start(APP_PACKAGE)  # start with package name

    def stop_app(self):
        self.d.app_stop(APP_PACKAGE)

    def checkIfLogin(self):
        if self.d(resourceId="com.yy.oa:id/oa_user_id").exists(timeout=10):
            return False
        elif self.d(description=u"G0880").exists(timeout=10):
            return True
        return None

    def login_app(self, username, password):
        resource_id = 'com.yy.oa:id/oa_user_id'
        self.d(resourceId=resource_id).set_text(username)
        resource_id = 'com.yy.oa:id/oa_password'
        self.d(resourceId=resource_id).set_text(password)
        try:
            # self.d(text='登录').click()
            resource_id = 'com.yy.oa:id/oa_btn_login'
            self.d(resourceId=resource_id).click()
            print('正在登录>>>>>>\n请稍后>>>>>>')
        except Exception as e:
            print(e)

    def click_checkin(self, filename = None, click_checkin = True):
        result = False
        try:
            self.d(className="android.widget.Image", instance=5).exists(timeout= 5)
            if click_checkin:
                self.d(className="android.widget.Image", instance=5).click()
                print('正在check in>>>>>>\n请稍后>>>>>>')
                if self.d(resourceId="android:id/alertTitle").exists(
                        timeout=10):  # wait Settings appear in 3s, same as .wait(3)
                    try:
                        self.d.screenshot(filename)
                        self.d(resourceId="android:id/button1").click()
                        print('Checkin done')
                        result =  True
                    except Exception as e:
                        print(e)
                else:
                    print('no confirm button')
            else:
                self.d.screenshot(filename)
                result = True
        except Exception as e:
            print(e)
        return result

    # settings: d(className="android.view.View", instance=2)
    # logout: d(description=u"退出登录")
    def logout(self):
        try:
            print('正在log out>>>>>>\n请稍后>>>>>>')
            self.d(className="android.view.View", instance=2).click()
            if self.d(description=u"退出登录").exists(timeout=10):
                self.d(description=u"退出登录").click()
        except Exception as e:
            print("failed to logout", e)