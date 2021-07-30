#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/6/15 9:15
# @author    : zhuziqing
# @File      : audiopage.py
from selenium.webdriver.common.by import By
import sys
import os
from random import randint, choice
from time import sleep
from appium import webdriver
from page.basepage import BasePage
from os.path import dirname
from retry import retry
from app_config import CAPS1
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class AudioPage(BasePage):

    balance_layout = (By.ID, "com.eswin.tv.settings:id/layout_balance")
    balance_switch = (By.ID, "com.eswin.tv.settings:id/tv_switch_balance")
    setting_Audio = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]")
    audio_mode_layout = (By.ID, "com.eswin.tv.settings:id/layout_audio_mode")
    audio_mode_name = (By.ID, "com.eswin.tv.settings:id/tv_name_type")
    eq0_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq0")
    eq2_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq2")
    eq4_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq4")
    restart_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]")
    count = 0

    def balance_layout_click(self):
        self.find_element(*self.setting_Audio).click()
        self.driver.keyevent(23)
        self.find_element(*self.balance_layout).click()

    def balance_switch_click(self):
        el = self.find_element(*self.balance_switch)
        print(el.text)
        return el.text

    def audo_mode_click(self):
        self.find_element(*self.setting_Audio).click()
        self.driver.keyevent(23)
        for i in range(6):
            self.driver.keyevent(20)
        sleep(1)
        try:
            self.find_element(*self.audio_mode_layout).click()
        except:
            # self.driver.keyevent(20)
            self.find_element(*self.audio_mode_layout).click()
        else:
            self.driver.keyevent(23)

    def value_switch(self):
        a = randint(1, 7)
        b = choice(['21','22'])
        for i in range(a):
            self.driver.keyevent(eval(b))

    def audo_mode_name_judge(self):
        el = self.find_element(*self.audio_mode_name)
        el1 = self.find_element(*self.eq0_value)
        return el.text, el1.text


    def restart(self):
        # self.check_port('127.0.0.1', 4723)
        self.driver.keyevent(3)
        self.driver.long_press_keycode(26)
        self.find_element(*self.restart_button).click()

    @retry(tries=2, delay=75)
    def restart_judge(self, select):
        if self.count == 0:
            self.count += 1

            self.restart()
        if self.count == 1:
            # os.system("adb uninstall io.appium.uiautomator2.server")
            # sleep(2)
            # os.system("adb uninstall io.appium.uiautomator2.server.test")
            # os.system('start docker exec -it appium1 adb connect 10.11.0.86:5555')
            # sleep(3)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
            driver.implicitly_wait(10)
            self.count = 0
            self.driver = driver
            driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
            if select == 'BL':
                self.balance_layout_click()
                result2 = self.balance_switch_click()
                return result2
            elif select == 'EQ':
                self.audo_mode_click()
                result2 = self.audo_mode_name_judge()
                return result2


