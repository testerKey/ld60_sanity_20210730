#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/9 14:58
# @author    : zhuziqing
# @File      : trdpage.py
from selenium.webdriver.common.by import By
import sys
import os
from time import sleep
from page.videopage import VideoPage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class ThreerdPage(VideoPage):
    jgTV = (By.XPATH, "//android.widget.TextView[contains(@text,'云视听极光')]/../android.widget.ImageView[1]")
    yhTV = (By.XPATH, "//android.widget.TextView[contains(@text,'银河奇异果')]/../android.widget.ImageView[1]")
    mine_page = (By.XPATH, "//android.widget.TextView[contains(@text,'我的')]")
    shortvideo = (By.XPATH, "//android.widget.TextView[contains(@text,'短视频')]")
    yh_play_time = (By.ID, "com.gitvdemo.video:id/play_text_video_time")
    hdmi_3 = HDMI_1 = (By.XPATH, "//android.widget.TextView[contains(@text,'HDMI-3')]")
    udisk = (By.XPATH, "//android.widget.TextView[contains(@text,'UDISK')]/../android.widget.ImageView[1]")
    sanity_file = (By.XPATH, "//android.widget.TextView[contains(@text,'BVT&SanityFiles')]/../android.widget.ImageView[1]")
    apk_file = (By.XPATH, "//android.widget.TextView[contains(@text,'3rdAPK')]/../android.widget.ImageView[1]")
    apk_install_button = (By.ID, "android:id/button1")
    apk_open_button = (By.ID, "android:id/button1")
    apk_exit_button = (By.XPATH, "//android.widget.TextView[contains(@text,'退出不看了')]")
    jg_app_manager = (By.XPATH, "//android.widget.TextView[contains(@text,'云视听极光')]/..")
    yh_app_manager = (By.XPATH, "//android.widget.TextView[contains(@text,'银河奇异果')]/..")
    app_uninstall_button = (By.ID, "com.eswin.tv.appmanager:id/iv_uninstall")
    jg_package = (By.XPATH, "//android.widget.TextView[contains(@text,'tv_video_6.4.0.1014_android_16118.apk')]/../android.widget.ImageView[1]")
    jg_continue_button = (By.ID, "com.android.permissioncontroller:id/continue_button")
    yh_package = (By.XPATH, "//android.widget.TextView[contains(@text,'qiyiguo_official10.11.3.apk')]/../android.widget.ImageView[1]")
    setting_Safety = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]")
    setting_Safety_Install = (By.ID, "com.eswin.tv.settings:id/layout_install")
    app_Install_perm = (By.ID, "com.eswin.tv.settings:id/tv_switch_install")

    def setting_Safety_click(self):
        self.find_element(*self.setting_Safety).click()
        self.driver.keyevent(23)

    def app_perm_status_get(self):
        el = self.find_element(*self.app_Install_perm)
        if el.text == 'Open':
            pass
        else:
            self.find_element(*self.setting_Safety_Install).click()
            self.driver.keyevent(22)  # 开启权限
            self.driver.keyevent(23)

    def install_apk(self, driver, *package_name):
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        try:
            self.find_element(*self.udisk).click()
        except Exception as e:
            print("未找到UDISK")
        else:
            driver.keyevent(23)
            try:
                self.find_element(*self.sanity_file).click()
            except Exception as e:
                print("未找到sanityfile")
            else:
                driver.keyevent(23)
                try:
                    self.find_element(*self.apk_file).click()
                except Exception as e:
                    print("未找到apkfile")
                else:
                    driver.keyevent(23)
                    # apk目录下安装
                    try:
                        self.find_element(*package_name).click()
                    except Exception as e:
                        print("未找到对应安装包")
                    else:
                        driver.keyevent(23)
                        self.find_element(*self.apk_install_button).click()
                        driver.keyevent(23)
        sleep(10)  # 等待安装
        try:
            self.find_element(*self.apk_open_button).click()
        except Exception as e:
            print("app安装失败")
            return False
        else:
            print("app安装成功")
            return True

    def install_jgtv(self, driver):
        try:  # home寻找app位置
            driver.keyevent(3)
            driver.keyevent(20)
            driver.keyevent(20)
            self.find_element(*self.jgTV).click()
        except Exception as e:
            self.install_apk(driver, *self.jg_package)
        else:
            print("app已安装")

    def install_yhtv(self, driver):
        try:
            driver.keyevent(3)
            driver.keyevent(20)
            driver.keyevent(20)
            self.find_element(*self.yhTV).click()
        except Exception as e:
            self.install_apk(driver, *self.yh_package)
        else:
            print("app已安装")

    def playback_jg(self, driver):
        driver.keyevent(23)
        try:
            self.find_element(*self.jg_continue_button).click()
        except Exception as e:
            pass
        else:
            driver.keyevent(23)
            driver.keyevent(4)
            driver.keyevent(4)
        sleep(5)
        # jgapp暂时不支持元素定位，暂时keyevent事件做简单播放
        driver.keyevent(21)
        driver.keyevent(23)
        driver.keyevent(23)
        sleep(10)
        driver.keyevent(4)
        driver.keyevent(4)
        driver.keyevent(4)
        # 退出apk
        driver.keyevent(4)

    def playback_yh(self, driver):
        result = False
        # 进入app
        driver.keyevent(23)
        driver.keyevent(4)
        try:  # 重新安装后第一次启动
            self.find_element(*self.jg_continue_button).click()
        except Exception as e:
            pass
        else:
            driver.keyevent(23)
            driver.keyevent(4)
            driver.keyevent(4)
        try:  # 进入app后进入短视频页
            self.find_element(*self.shortvideo).click()
        except Exception as e:
            print("app启动失败")
        else:  # 播放短视频并抓取时间戳
            driver.keyevent(23)
            driver.keyevent(23)
            sleep(5)
            driver.keyevent(23)
            result = self.time_judge(driver, *self.yh_play_time)
            print("app运行正常")
        # 退出apk
        for i in range(4):
            try:
                self.find_element(*self.apk_exit_button).click()
            except Exception as e:
                if i == 2:
                    driver.keyevent(4)
                else:
                    driver.keyevent(4)
                    driver.keyevent(4)
            else:
                driver.keyevent(23)
                break
        return result

    def app_exit(self, sel):
        self.clear_apk_cache(sel)
        try:
            self.find_element(*self.mine_page)
        except Exception as e:
            print("app退出成功")
            return True
        else:
            print("app退出失败")
            return False

    def uninstall_apk(self, driver, *package_name):
        driver.start_activity(" com.eswin.tv.appmanager",".ui.activity.AppActivity")
        for i in range(3):  # 卸载app
            try:
                self.find_element(*package_name).click()
            except Exception as e:
                driver.keyevent(20)
            else:
                driver.keyevent(23)
                try:
                    self.find_element(*self.app_uninstall_button).click()
                except Exception as e:
                    print("此app不能卸载，请选择其他app")
                    driver.keyevent(20)
                else:
                    driver.keyevent(23)
                    driver.keyevent(21)
                    driver.keyevent(23)
                    break
        # 等待卸载
        sleep(10)
        driver.keyevent(4)  # 退出appmanager

    def uinstall_jg(self, driver):
        self.uninstall_apk(driver, *self.jg_app_manager)
        try:  # home查找app图标
            driver.keyevent(3)
            driver.keyevent(20)
            driver.keyevent(20)
            self.find_element(*self.jgTV).click()
        except Exception as e:
            print("云视听极光已成功卸载")
            return True
        else:
            print("卸载失败")
            return False

    def uinstall_yh(self, driver):
        self.uninstall_apk(driver, *self.yh_app_manager)
        try:
            driver.keyevent(3)
            driver.keyevent(20)
            driver.keyevent(20)
            self.find_element(*self.yhTV).click()
        except Exception as e:
            print("银河奇异果已成功卸载")
            return True
        else:
            print("卸载失败")
            return False

    def clear_apk_cache(self,sel):
        command_1 = "adb shell pm clear com.ktcp.video"
        command_2 = "adb shell pm clear com.gitvdemo.video"
        if sel == 'jg':
            os.system(command_1)
            print("清除jg缓存")
        elif sel == 'yh':
            os.system(command_2)
            print("清除yh缓存")
