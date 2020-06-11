import selenium
import pytest
import configparser
import logging

from allure_commons.model2 import Attachment
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

from Util.diver import driver
from Util.logger import Logger
from Util.tool import tool


class WebTest:

    # 获取config ，作为参数
    # 全局传参

    def getWebDriver(self):

        self.driver = driver()
        return self.driver.getWebDriver()

    def setup_module(self):
        self.baseDir = tool.getBaseDir()
        self.log = Logger(__name__)
        cf = configparser.ConfigParser();
        path = os.path.join(tool.getBaseDir(), "TestCase", "properties.ini")
        try:
            cf.read(path)
        except Exception as e:
            self.log.setCriticalLog("read file failed, pls recheck the path" + e)
        self.killDriver()
        self.thread = cf.get("testInfo", "thread")
        self.log.setInfoLog("****************************************")
        self.log.setInfoLog("[Suit Params]  thread : " + self.thread)

    def teardown_module(self):
        self.driver.chromeDesiredCapabilities()[""] = ""

    def setup_class(self):
        self.setDownloadDir()

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def setup_module(self):
        pass

    def teardown_module(self):
        pass

    def info_properties(self):
        pass

    def setDownloadDir(self):
        downloadPath = os.path.join(tool.getBaseDir(), "TestCase", "download", __name__)
        self.driver.commonDesiredCap()["download.default_directory"] = downloadPath

    def killDriver(self):
        self.log.setInfoLog("kill all chrome process...")
        os.system("taskkill /f /im chromedriver.exe")
        self.log.setInfoLog("done.")

    @staticmethod
    def getbasedir():
        return os.path.dirname(os.getcwd())

    def log(self):
        pass

    @Attachment
    def getScreenShot(self):
        # TODO screenshot name
        # 输入到allure报告中 作为attachment
        self.getWebDriver().save_screenshot()
        pass

    def Action_Execute_JS(self, script):
        self.getWebDriver().execute_script(script)

    def Element_Highlight(self, element):
        pass

    def Execute_JS(self, jsScript):
        pass
