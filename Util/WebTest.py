import traceback
from time import sleep

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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class WebTest:

    # 获取config ，作为参数
    # 全局传参

    def getWebDriver(self):

        self.driver = driver()


        return self.driver.getWebDriver()

    def setup_module(self):
        self.driver.getWebDriver().set_script_timeout(self.script_load_timeout)
        self.driver.getWebDriver().set_page_load_timeout(self.page_load_timeout)
        self.driver.getWebDriver().implicitly_wait(self.implicitly_wait)
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
        self.timeout = cf.get("driverInfo", "timeout")
        self.implicitly_wait = cf.get("driverSetting", "implicitly_wait")
        self.page_load_timeout = cf.get("driverSetting", "page_load_timeout")
        self.script_load_timeout = cf.get("driverSetting", "script_load_timeout")
        try:
            cf.read(path)
        except Exception as e:
            self.log.setCriticalLog("read file properties.ini failed, pls recheck the path", e)

        self.log.setInfoLog("================== setup module")

    def teardown_module(self):
        self.driver.chromeDesiredCapabilities()[""] = ""

    @classmethod
    def setup_class(cls):
        cls.setDownloadDir()

    @classmethod
    def teardown_class(cls):
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

    @classmethod
    def setDownloadDir(cls):
        downloadPath = os.path.join(tool.getBaseDir(), "TestCase", "download", __name__)
        print("222", downloadPath)
        WebTest().getWebDriver().commonDesiredCap()["download.default_directory"] = downloadPath

    def killDriver(self):
        self.log.setInfoLog("kill all chrome process...")
        os.system("taskkill /f /im chromedriver.exe")
        self.log.setInfoLog("done.")

    def log(self):
        pass

    def getElementToBeClickable(self, time, locator):
        try:
            webelement = WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(
                EC.element_to_be_clickable(locator))
            return webelement
        except Exception as e:
            self.log.setDebugLog("cannot find the element ,the element is empty")
            traceback.print_exc()

    def getElementToBeClickable(self, locator):
        self.getElementToBeClickable(self.timeout, locator)

    def getElementToBeVisible(self, time, locator):
        try:
            webelement = WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(
                EC.visibility_of_element_located(locator))
            return webelement
        except:
            self.log.setDebugLog("cannot find the element ,the element is empty")
            traceback.print_exc()

    def getElementToBeVisible(self, locator):
        self.getElementToBeVisible(self.timeout, locator)

    def waitElementToBeInvisible(self, time, locator):
        WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(
            EC.invisibility_of_element_located(locator))



    def waitSeconds(self, time, msg):
        self.log.setInfoLog("wait seconds dut to " + msg)
        for i in range(time):
            sleep(1)
            print("wait in total : " + str(time) + 'current is :' + str(i))

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
