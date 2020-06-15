import traceback
from time import sleep
import pytest
import configparser
from allure_commons.model2 import Attachment
import os
from selenium.webdriver.support.wait import WebDriverWait
from Util.diver import Driver
from Util.logger import Logger
from Util.tool import tool
from selenium.webdriver.support import expected_conditions as EC


class WebTest:

    # 获取config ，作为参数
    # 全局传参

    def __init__(self):
        self.baseDir = tool.getBaseDir()
        self.log = Logger(__name__)
        cf = configparser.ConfigParser();
        path = os.path.join(tool.getBaseDir(), "TestCase", "properties.ini")
        try:
            cf.read(path)
        except Exception as e:
            self.log.setCriticalLog("read file failed, pls recheck the path" + e)
        self.killDriver()
        self.driver = Driver().getWebDriver()
        self.thread = cf.get("testInfo", "thread")
        self.log.setInfoLog("****************************************")
        self.log.setInfoLog("[Suit Params]  thread : " + self.thread)
        self.timeout = cf.get("driverSetting", "timeout")
        self.script_load_timeout = cf.get("driverSetting", "script_load_timeout")
        self.page_load_timeout = cf.get("driverSetting", "page_load_timeout")
        self.implicitly_wait = cf.get("driverSetting", "implicitly_wait")
        self.driver.set_script_timeout(self.script_load_timeout)
        self.driver.set_page_load_timeout(self.page_load_timeout)
        # self.driver.implicitly_wait(self.implicitly_wait)

    def getWebDriver(self):
        return self.driver

    def getElementToBeClickable(self, locator, value, time: int = None):
        if not time:
            time = int(self.timeout)
        try:
            webelement = WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(EC.element_to_be_clickable((locator, value)))
            self.element_Highlight(webelement)
            return webelement
        except:
            self.log.setDebugLog("cannot find the element ,the element is empty")
            traceback.print_exc()
            return None

    def getElementToBeVisible(self, locator, value, time: int = None):
        if not time:
            time = int(self.timeout)
        try:
            # condition = EC.visibility_of_element_located((locator, value))
            webelement = WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(
                EC.visibility_of_element_located((locator, value)))
            self.element_Highlight(webelement)
            return webelement
        except:

            self.log.setDebugLog("cannot find the element ,the element is empty")
            traceback.print_exc()
            return None

    def waitElementToBeInvisible(self, time, locator, value):
        WebDriverWait(self.getWebDriver(), timeout=time, poll_frequency=0.5).until(
            EC.invisibility_of_element_located(locator, value))



    def action_click_element(self,webelement):
        self.element_Highlight(webelement)
        text = webelement.text
        self.waitSeconds(1)
        self.getScreenShot()
        self.waitSeconds(1)
        webelement.click()

    # def setup_module(self):
    #     pass
    #
    # def teardown_module(self):
    #     self.driver.chromeDesiredCapabilities()[""] = ""
    #
    # @classmethod
    # def setup_class(cls):
    #     pass
    #
    # @classmethod
    # def teardown_class(cls):
    #     WebTest.getWebDriver().quit()
    #
    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     pass
    #
    # def setup_module(self):
    #     pass
    #
    # def teardown_module(self):
    #     pass

    def info_properties(self):
        pass

    def killDriver(self):
        self.log.setInfoLog("kill all chrome process...")
        os.system("taskkill /f /im chromedriver.exe")
        self.log.setInfoLog("done.")

    def log(self):
        pass

    def waitSeconds(self, time, msg:str = None):
        self.log.setInfoLog("wait seconds due to " + msg)
        for i in range(time):
            sleep(1)
            print("wait in total : " + str(time) + 'seconds - current is :' + str(i))

    @Attachment
    def getScreenShot(self):
        # TODO screenshot name
        # 输入到allure报告中 作为attachment
        self.driver.save_screenshot()
        pass

    def action_JS_click(self, webelement):
        if  webelement:


        self.element_Highlight(webelement)


    def action_execute_JS(self, script):
        self.driver.execute_script(script)

    def element_Highlight(self, element):
        self.getWebDriver().execute_script("element = arguments[0];" + "original_style = element.getAttribute('style');"
							+ "element.setAttribute('style', original_style + \";" + " border: 3px solid red;\");"
							+ "setTimeout(function(){element.setAttribute('style', original_style);}, 2000);",element)

    def execute_JS(self, jsScript):
        pass

# if __name__ == '__main__':
#     web = WebTest()
#     web.getWebDriver()
