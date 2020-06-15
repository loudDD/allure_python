import time

from selenium.webdriver.common.by import By
from Util.WebTest import WebTest
from Util.diver import Driver


def add(a, b):
    return a + b


class Test_demo1:

    # driver = driver().getWebDriver()

    def test_1(self):
        print("33333")
        # driver.get("https:\\www.baidu.com")
        webtest = WebTest()
        driver = webtest.getWebDriver()
        driver.get("https:\\www.baidu.com")
        webtest.getElementToBeVisible(By.ID, "sw")
        time.sleep(30)

    def test_2(self):
        assert add(3, 4) == 7

    def test_3(self):
        pass


if __name__ == '__main__':
    Test_demo1().test_1()
