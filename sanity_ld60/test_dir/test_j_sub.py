#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/5/8 10:52
# @author    : zhuziqing
# @File      : test_j_sub.py
import pytest
import sys
from page.videopage import VideoPage
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestSubandAudio:

    def test_sanity_59(self, driver):
        page = VideoPage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.video_page_switch()
        page.click_video_54()
        result = page.playback_video(*page.video_54_name)
        assert result is True

    def test_sanity_60(self, driver):
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page = VideoPage(driver)
        page.video_page_switch()
        page.click_video_55()
        result = page.switch_audio_track(2)
        assert result is True


if __name__ == '__main__':
    pytest.main()