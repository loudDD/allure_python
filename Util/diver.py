import configparser
import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import threading

from Util.tool import tool


class driver:

    def __init__(self):
        cf = configparser.ConfigParser();
        path = os.path.join(self.getBaseDir(), "Common", "properties.ini")
        print("the path is : " + path)
        try:
            cf.read(path)
        except Exception as e:
            print("read file failed, pls recheck the path" + e)

        self.baseDir = tool.getBaseDir()
        # msf from ini
        self.driver_platform = cf.get("driverInfo", "driver_platform")
        self.driver_version = cf.get("driverInfo", "driver_version")
        self.remote_is_enable = cf.get("driverInfo", "remote_is_enable")
        self.screen_is_enable = cf.get("driverInfo", "screen_is_enable")
        self.platform = cf.get("driverInfo", "platform")
        print(self.driver_platform)

    def chromeDesiredCapabilities(self):
        # remote driver

        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["platform"] = "";
        return capabilities

    def chromeOptions(self):
        options = webdriver.ChromeOptions()
        options.add_argument();
        prefs = {"": ""}
        options.add_experimental_option("prefs", prefs);
        return options

    def driverPath(self):
        # 生成path路径，根据版本，平台
        if self.driver_platform == "chrome":
            path = os.path.join(self.getBaseDir(), "driver", self.driver_platform, self.driver_version, self.platform)
            if self.platform == "windows":
                path = os.path.join(path, "chromedriver.exe")
            elif self.platform == "mac":
                path = os.path.join(path, "chromedriver")
            else:
                print("current framework does't support " + self.driver_version)
        elif self.driver_platform == "firefox":
            path = os.path.join(self.getBaseDir(), "driver", self.driver_platform, self.driver_version, self.platform)
            if self.platform == "windows":
                path = os.path.join(path, "geckodriver.exe")
            elif self.platform == "mac":
                path = os.path.join(path, "geckodriver")
            else:
                print("current framework does't support " + self.driver_version)
        else:
            print("current framework doesn't support " + self.driver)
            return None
        return path

    def getWebDriver(self):
        # 考虑并发，remote
        if "chrome" == self.driver_platform:
            return webdriver.Chrome(executable_path=self.driverPath(),
                                    desired_capabilities=self.chromeDesiredCapabilities())
        elif "firefox" == self.driver_platform:
            return webdriver.Firefox(executable_path=self.driverPath())
        else:
            print("wrong driver name")


# test
# if __name__ == '__main__':
#     driverlocal = driver()
#     driverlocal.getWebDriver().get("https:\\www.baidu.com")
