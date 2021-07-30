#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/6/15 17:17
# @author    : zhuziqing
# @File      : storagepage.py
from selenium.webdriver.common.by import By
import sys
import os
from time import sleep
from page.basepage import BasePage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)

class StoragePage(BasePage):

    udisk1 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]")
    udisk2 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]")
    file_el = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]")

    def udisk_fat32_find(self):
        try:
            self.find_element(*self.udisk2).click()
        except:
            print('未能识别Fat32格式U盘')
            return False
        else:
            self.driver.keyevent(23)

    def udisk_ntfs_find(self):
        try:
            self.find_element(*self.udisk1).click()
        except:
            print('未能识别NTFS格式U盘')
            return False
        else:
            self.driver.keyevent(23)

    def file_browse(self):
        try:
            self.find_element(*self.file_el)
        except:
            print("U盘打开错误")
            return False
        else:
            print("U盘打开错误")
            return True