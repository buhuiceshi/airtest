# -*- coding: utf-8 -*-
# @Time : 2020/12/24 15:04
# @Author : lrlr

__author__ = "Administrator"

import base64
from airtest.core.api import *
# from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from common.log import log
from common import dir_config

auto_setup(__file__, devices=["Android:///"])

# simple_report(__file__, logpath=dir_config.log_path + "/airtest", output=dir_config.log_path + "/airtest/report.html")



class BasePage:
    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        # self.poco = AndroidUiautomationPoco(screenshot_each_action=False)
        self.log = log

    def star_app(self):
        start_app("io.dcloud.H5FC108D4")

    def click(self, locator, doc=""):
        self.wait(locator, doc)
        try:
            locator.click()
        except:
            log.exception("{0}点击元素{1}时出错".format(doc, locator))
            self.screenshot(doc)
            raise

    def send_keys(self, locator, text, doc=""):
        self.wait(locator, doc=doc)
        try:
            locator.set_text(text)
        except:
            log.exception("{0} 在 {1}输入 {2}时出错".format(doc, locator, text))
            self.screenshot(doc)
            raise

    def adb_input(self, adb):
        os.system(adb)

    def get_text(self, locator, doc=""):
        try:
            return locator.get_text()
        except:
            log.exception("{0}元素{1}获取文本出错".format(doc, locator))
            self.screenshot(doc)
            raise

    def get_attr(self, locator, attr, doc=""):
        try:
            return locator.attr(attr)
        except:
            log.exception("{0}元素{1}获取属性{2}出错".format(doc, locator, attr))
            self.screenshot(doc)
            raise

    def wait(self, locator, doc=""):
        try:
            locator.wait_for_appearance(timeout=10)
        except:
            log.exception("等待元素{}出错".format(locator))
            self.screenshot(doc)
            raise

    def screenshot(self, doc=""):
        b64, fmt = self.poco.snapshot()
        img = base64.b64decode(b64)
        # 截图文件名
        file_time = time.strftime('%H-%M-%S', time.localtime(time.time()))
        screen_name = dir_config.screenshots_path + '/' + file_time + '_' + doc
        with open("{0}.{1}".format(screen_name, fmt), "wb") as f:
            f.write(img)
