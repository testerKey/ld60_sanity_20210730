#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/19 15:07
# @author    : zhuziqing
# @File      : test_connectivity.py
import pytest
import sys
from page.connectivitypage import ConPage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class TestConnectivity:

    # def test_sanity_48(self, driver):
    #     page = ConPage(driver)
    #     driver.start_activity("com.eswin.tvmiracastdemo", ".MainActivity")
    #     result = page.find_mobile_screen(driver)
    #     assert result is True

    def test_sanity_49(self, driver):
        driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
        page = ConPage(driver)
        result = []
        result.append(page.setting_wifi_name_get())
        page.setting_Safety_click()
        page.app_perm_status_get()
        page.install_jgtv(driver)
        result.append(page.playback_jg(driver))
        result.append(page.restart_judge())
        assert False not in result

    # def test_sanity_50(self, driver):
    #     page = ConPage(driver)
    #     result = page.playback_dlna(driver)
    #     assert result is True
    #
    # def test_sanity_51(self, driver):
    #     page = ConPage(driver)
    #     result = page.playback_dlna(driver)
    #     assert result is True


if __name__ == '__main__':
    pytest.main()
