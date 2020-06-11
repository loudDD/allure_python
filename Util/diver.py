import configparser
import os
import sys

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from Util.logger import Logger
from Util.tool import tool


class driver:

    def __init__(self):

        self.baseDir = tool.getBaseDir()
        self.log = Logger(__name__)
        cf = configparser.ConfigParser()
        path = os.path.join(tool.getBaseDir(), "TestCase", "properties.ini")
        self.log.setInfoLog("the property path is : " + path)
        try:
            cf.read(path)
        except Exception as e:
            self.log.setCriticalLog("read file failed, pls recheck the path",e)
        sys_platform = sys.platform
        if "win" in sys_platform:
            self.platform = "windows"
        elif "mac" in sys_platform:
            self.platform = "mac"
        self.driver_platform = cf.get("driverInfo", "driver_platform")
        self.driver_version = cf.get("driverInfo", "driver_version")
        self.remote_is_enable = cf.get("driverInfo", "remote_is_enable") == "True"
        self.screen_is_enable = cf.get("driverInfo", "screen_is_enable") == "True"
        self.remote_hub = cf.get("driverInfo", "remote_hub")
        self.headless = cf.get("driverInfo", "headless") == "True"
        self.log.setInfoLog("**************Default Config**************")
        self.log.setInfoLog("[Params]  System platform : " + self.driver_platform)
        self.log.setInfoLog("[Params]  driver platform : " + self.driver_platform)
        self.log.setInfoLog("[Params]  driver version : " + self.driver_version)
        self.log.setInfoLog("[Params]  driver headless : " + str(self.headless))
        self.log.setInfoLog("[Params]  driver screen_is_enable : " + str(self.screen_is_enable))
        self.log.setInfoLog("[Params]  driver remote_is_enable : " + str(self.remote_is_enable))
        self.log.setInfoLog("[Params]  driver remote_hub : " + self.remote_hub)
        self.log.setInfoLog("******************************************")

        # TODO

    def chromeDesiredCapabilities(self):
        # remote driver
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["browserName"] = "chrome"
        for k, v in self.commonDesiredCap().items():
            capabilities[k] = v
        return capabilities

    def commonDesiredCap(self):

        DesiredCap = {"profile.default_content_settings.popups": "0",
                      "profile.default_content_setting_values.automatic_downloads": "1",
                      "download.prompt_for_download": False, "download.directory_upgrade": True,
                      "safebrowsing.enabled": True, }
        return DesiredCap

    def commonOptions(self):
        options = ["--disable-blink-features", "--disable-app-list-dismiss-on-blur", "--test-type",
                   "--ignore-certificate-errors", "--no-default-browser-check", "--lang=en-US", "--enable-automation",
                   "--enable-background-blur", "--disable-infobars", "--disable-gpu",
                   "--safebrowsing-disable-auto-update", "--safebrowsing-disable-download-protection",
                   "--safebrowsing-disable-extension-blacklist", "--safebrowsing-manual-download-blacklist",
                   "--trusted-download-sources"]
        if self.headless is True:
            options.append("--headless");
        return options

    def chromeOptions(self):
        # mapping folder of zalenium
        options = webdriver.ChromeOptions()
        for option in self.commonOptions():
            options.add_argument(option)
        return options

    def firefoxDesiredCapabilities(self):
        capabilities = DesiredCapabilities.FIREFOX.copy()
        # TODO check if this is working
        capabilities.get(self.firefoxOptions())
        capabilities["browserName"] = "firefox";
        for k, v in self.commonDesiredCap():
            capabilities[k] = v
        return capabilities

    def firefoxOptions(self):
        # mapping folder of zalenium
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features");
        options.add_argument("--disable-app-list-dismiss-on-blur");
        options.add_argument("--test-type");
        options.add_argument("--ignore-certificate-errors");
        options.add_argument("--no-default-browser-check");
        options.add_argument("--lang=en-US");
        options.add_argument("--enable-automation");
        options.add_argument("--enable-background-blur");
        options.add_argument("--disable-infobars");
        options.add_argument("--disable-gpu");
        options.add_argument("--safebrowsing-disable-auto-update");
        options.add_argument("--safebrowsing-disable-download-protection");
        options.add_argument("--safebrowsing-disable-extension-blacklist");
        options.add_argument("--safebrowsing-manual-download-blacklist");
        options.add_argument("--trusted-download-sources");
        if self.headless == True:
            options.add_argument("--headless");
        return options

    def driverPath(self):
        # 生成path路径，根据版本，平台
        if self.driver_platform == "chrome":
            path = os.path.join(tool.getBaseDir(), "driver", self.driver_platform, self.driver_version, self.platform)
            if "win" in self.platform:
                path = os.path.join(path, "chromedriver.exe")
            elif self.platform == "mac":
                path = os.path.join(path, "chromedriver")
            else:
                self.log.setCriticalLog("current framework does't support " + self.driver_version)
        elif self.driver_platform == "firefox":
            path = os.path.join(tool.getBaseDir(), "driver", self.driver_platform, self.driver_version, self.platform)
            if "win" in self.platform:
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
        if self.remote_is_enable is True and self.driver_platform == "chrome":
            return webdriver.Remote(command_executor=self.remote_hub,
                                    desired_capabilities=self.chromeDesiredCapabilities())
        elif self.remote_is_enable is False and "chrome" == self.driver_platform:
            self.log.setInfoLog("the driver platform is Chrome , start Chrome")
            return webdriver.Chrome(executable_path=self.driverPath(),
                                    desired_capabilities=self.chromeDesiredCapabilities(),
                                    options=self.chromeOptions())
        elif self.remote_is_enable == False and "firefox" == self.driver_platform:
            self.log.setInfoLog("the driver platform is FireFox , start FireFox")
            return webdriver.Firefox(executable_path=self.driverPath(),
                                     desired_capabilities=self.firefoxDesiredCapabilities(),
                                     options=self.firefoxOptions())
        # else:
        #     self.log.setCriticalLog("wrong driver name")
        #     return None


# test
if __name__ == '__main__':
    driverlocal = driver()
    driverlocal.getWebDriver().get("https:\\www.baidu.com")
