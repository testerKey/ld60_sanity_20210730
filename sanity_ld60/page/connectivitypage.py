#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/19 15:09
# @author    : zhuziqing
# @File      : connectivitypage.py
from selenium.webdriver.common.by import By
from appium import webdriver
from page.trdpage import ThreerdPage
from retry import retry
from app_config import CAPS1


class ConPage(ThreerdPage):

    setting_wifi_name = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView")

    restart_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]")
    count = 0

    def setting_wifi_name_get(self):
        try:
            el = self.find_element(*self.setting_wifi_name)
        except:
            return False
        else:
            return True

    def restart(self):
        self.driver.keyevent(3)
        self.driver.long_press_keycode(26)
        self.find_element(*self.restart_button).click()

    @retry(tries=2, delay=75)
    def restart_judge(self):
        if self.count == 0:
            self.count += 1

            self.restart()
        if self.count == 1:
            # os.system("adb uninstall io.appium.uiautomator2.server")
            # sleep(2)
            # os.system("adb uninstall io.appium.uiautomator2.server.test")
            # sleep(2)
            # os.system('start docker exec -it appium1 adb connect 10.11.0.86:5555')
            # sleep(3)
            try:
                driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
            except:
                print('caps启动异常')
            else:
                driver.implicitly_wait(10)
                self.count = 0
                self.driver = driver
                self.install_jgtv(driver)
                result = self.playback_jg(driver)
                self.app_exit('jg')
                return result
            # self.driver = driver1
            # driver.keyevent(3)
            # driver.keyevent(20)
            # driver.keyevent(19)
            # try:
            #     driver.find_element(*self.HDMI_1)
            # except Exception as e:
            #     # driver1.quit()
            #     return False
            # else:
            #     print("yessssss")
            #     # driver1.quit()
            #     return True


    # eq_name = (By.XPATH, "//android.widget.TextView[contains(@text,'ESWIN-MBU_DD64')]")
    # connect_button = (By.ID, "android:id/button1")
    # decline_button = (By.ID, "android:id/button2")
    # mobile_screen = (By.XPATH, "//android.widget.TextView[contains(@text,'无线投屏')]")
    # disconnect_button = (By.XPATH, "//android.widget.Button[contains(@text,'断开连接')]")
    # dlna_movie = (By.XPATH, "//android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]")
    # dlna_screen = (By.ID, "com.youku.phone:id/plugin_small_top_dlna_btn")
    # dlna_eq_name = (By.XPATH, "//android.widget.TextView[contains(@text,'ESWIN-MBU_DD64-DMR')]")
    # dlna_tv_quit = (By.ID, "com.youku.phone:id/iv_quit")
    # dlna_current_time = (By.ID, "com.eswin.tv.filebrowser:id/time_current")


    # def click_eq_name(self):
    #     self.find_element(*self.eq_name).click()
    #
    # def click_connect_button(self, driver):
    #     self.find_element(*self.connect_button).click()
    #     driver.keyevent(23)

    # def find_mobile_screen(self, driver):
    #     caps = {
    #
    #         "deviceName": '8BNDU18130006235',
    #         "platformName": 'Android',
    #         "platformVersion": '9',
    #         "appPackage": 'com.huawei.android.launcher',
    #         "appActivity": '.unihome.UniHomeLauncher',
    #         "noReset": True,
    #         "unicodeKeyboard": True,
    #         "resetKeyboard": True,
    #     }
    #     driver1 = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #     driver1.implicitly_wait(10)
    #     driver1.swipe(500, 10, 500, 600, 1000)
    #     driver1.swipe(500, 200, 500, 500, 1000)
    #     driver1.find_element(*self.mobile_screen).click()
    #     driver1.find_element(*self.eq_name).click()
    #     self.click_connect_button(driver)
    #     sleep(10)
    #     path = 'D:\\Picture\\connectivity\\miracast.png'  # 参照图文件路径
    #     result = self.compare_images(driver, path)
    #     driver1.swipe(500, 10, 500, 600, 1000)
    #     driver1.find_element(*self.disconnect_button).click()
    #     driver.keyevent(4)
    #     driver.keyevent(4)
    #     driver1.quit()
    #     return result

    # def playback_dlna(self, driver):
    #     caps = {
    #
    #         "deviceName": '8BNDU18130006235',
    #         "platformName": 'Android',
    #         "platformVersion": '9',
    #         "appPackage": 'com.youku.phone',
    #         "appActivity": 'com.youku.v2.HomePageEntry',
    #         "noReset": True,
    #         "unicodeKeyboard": True,
    #         "resetKeyboard": True,
    #     }
    #     driver1 = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #     driver1.implicitly_wait(10)
    #     sleep(5)
    #     driver1.find_element(*self.dlna_movie).click()
    #     driver1.find_element(*self.dlna_screen).click()
    #     for i in range(3):
    #         try:
    #             driver1.find_element(*self.dlna_eq_name).click()
    #         except Exception as e:
    #             driver1.swipe(800, 1300, 800, 1000, 1000)
    #         else:
    #             break
    #     sleep(15)
    #     driver.keyevent(23)
    #     try:
    #         self.find_element(*self.dlna_current_time)
    #     except Exception as e:
    #         print("DLNA投屏失败")
    #         result1 = False
    #     else:
    #         result1 = True
    #     driver1.find_element(*self.dlna_tv_quit).click()
    #     sleep(2)
    #     try:
    #         self.find_element(*self.dlna_current_time)
    #     except Exception as e:
    #         result2 = True
    #     else:
    #         print("dlna退出失败")
    #         result2 = False
    #     driver1.quit()
    #     return result1 & result2
