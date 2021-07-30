#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/9 15:15
# @author    : zhuziqing
# @File      : test_mediascanner.py.py
import sys
import pytest
from retry import retry
from page.mediascannerpage import ScannerPage
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestMediaScanner:
    def test_sanity_61(self, driver):
        page = ScannerPage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.video_page_switch()
        result = page.videoscan()
        assert result is True

    def test_sanity_62(self, driver):
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page = ScannerPage(driver)
        page.music_page_switch()
        result = page.musicscan()
        assert result is True

    def test_sanity_63(self, driver):
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page = ScannerPage(driver)
        page.picture_page_switch()
        page.picture_format_click()
        result = page.picturescan()
        assert result is True


if __name__ == '__main__':
    pytest.main()