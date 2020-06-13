from selenium.webdriver.common.by import By

from TestCase.TestCase_Impl import TestCase_Impl
from Util.WebTest import WebTest
from Util.diver import driver


def add(a, b):
    return a + b


class Test_demo1(WebTest):
    # driver = driver().getWebDriver().get("")
    def test_1(self):
        print("33333")
        driver().getWebDriver().get("https:\\www.baidu.com")
        WebTest().getElementToBeVisible((By.ID, "sw"))

    def test_2(self):
        assert add(3, 4) == 7

    def test_3(self):
        pass


if __name__ == '__main__':
    Test_demo1().test_1()
