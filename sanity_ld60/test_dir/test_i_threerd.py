# #!usr/bin/python3
# # -*- coding: utf-8 -*-
# # @time      : 2021/4/9 15:01
# # @author    : zhuziqing
# # @File      : test_threerd.py.py
# import pytest
# import sys
# from page.trdpage import ThreerdPage
# from os.path import dirname
# BASE_PATH = dirname(dirname(__file__))
# sys.path.append(BASE_PATH)
#
#
# class Testthreerd:
#
#     def test_sanity_52(self, driver):
#         page = ThreerdPage(driver)
#         result = []
#         result.append(page.install_jgtv(driver))
#         result.append(page.playback_jg(driver))
#         result.append(page.uinstall_jg(driver))
#         assert False not in result
#
#     # def test_sanity_50(self, driver):
#     #     page = ThreerdPage(driver)
#     #     result = []
#     #     result.append(page.install_jgtv(driver))
#     #     result.append(page.playback_jg(driver))
#     #     result.append(page.app_exit(driver))
#     #     assert False not in result
#     #
#     # def test_sanity_51(self, driver):
#     #     page = ThreerdPage(driver)
#     #     result = []
#     #     result.append(page.install_yhtv(driver))
#     #     result.append(page.playback_yh(driver))
#     #     result.append(page.app_exit(driver))
#     #     assert False not in result
#
#
# if __name__ == '__main__':
#     pytest.main()
