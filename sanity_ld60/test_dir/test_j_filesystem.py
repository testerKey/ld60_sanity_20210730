# #!usr/bin/python3
# # -*- coding: utf-8 -*-
# # @time      : 2021/6/15 17:51
# # @author    : zhuziqing
# # @File      : test_j_filesystem.py
# import pytest
# import sys
# from page.storagepage import StoragePage
# from os.path import dirname
# BASE_PATH = dirname(dirname(__file__))
# sys.path.append(BASE_PATH)
#
# class TestFileSystem:
#
#     def test_sanity_55(self, driver):
#         driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
#         page = StoragePage(driver)
#         result = []
#         result.append(page.udisk_fat32_find())
#         result.append(page.file_browse())
#         assert False not in result
#
#     def test_sanity_56(self, driver):
#         driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
#         page = StoragePage(driver)
#         result = []
#         result.append(page.udisk_ntfs_find())
#         result.append(page.file_browse())
#         assert False not in result
#
#
# if __name__ == '__main__':
#     pytest.main()
