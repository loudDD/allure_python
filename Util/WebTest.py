import selenium
import pytest
import configparser
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class WebTest:

    # 获取config ，作为参数
    # 全局传参

    def setup_module(self):
        pass

    def teardown_module(self):
        pass

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def setup_module(self):

        print("driverinfo " + self.platform)

    def teardown_module(self):
        pass

    def info_properties(self):
        pass





    @staticmethod
    def getbasedir():
        return os.path.dirname(os.getcwd())



    def log(self):
        pass

    def getScreenShot(self):
        # 输入到allure报告中 作为attachment
        pass



    def Action_JS_Click(self, element):
        pass

    def Element_Highlight(self, element):
        pass

    def Execute_JS(self, jsScript):
        pass
