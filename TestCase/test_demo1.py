from TestCase.TestCase_Impl import TestCase_Impl


def add(a, b):
    return a + b


class Test_demo1(TestCase_Impl):

    def test_1(self):
        assert add(1, 3) == 6

    def test_2(self):
        assert add(3, 4) == 7

    def test_3(self):
        super().getWebDriver().get("https://www.baidu.com")
