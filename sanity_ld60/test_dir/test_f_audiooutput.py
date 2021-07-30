#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/6/15 11:07
# @author    : zhuziqing
# @File      : test_f_audiooutput.py
import pytest
import sys
from appium import webdriver
from app_config import CAPS1
from page.audiopage import AudioPage
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestAudiooutput:

    def test_sanity_36(self, driver):
        driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
        page = AudioPage(driver)
        page.audo_mode_click()
        page.value_switch()
        result = page.audo_mode_name_judge()
        result2 = page.restart_judge('EQ')
        assert (result == result2) is False

    def test_sanity_37(self, driver):
        # driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
        # driver.implicitly_wait(10)
        driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
        page = AudioPage(driver)
        page.balance_layout_click()
        page.value_switch()
        result1 = page.balance_switch_click()
        result2 = page.restart_judge('BL')
        assert (result2 == result1) is True


if __name__ == '__main__':
    pytest.main()