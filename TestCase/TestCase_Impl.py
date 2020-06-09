from selenium.webdriver.support.wait import WebDriverWait

from Util.WebTest import WebTest
from Util.diver import driver
from selenium.webdriver.support import expected_conditions as EC


class TestCase_Impl:




    def getWebDriver(self):
        self.driver = driver().getWebDriver();
        return self.driver

    def setImplicitlyWait(self, time):
        self.getWebDriver.implicitly_wait(time)

    def getElementToBeClickable(self, locator, time, frequency=0.5):
        WebDriverWait(self.getWebDriver, timeout=time, poll_frequency=frequency).until(EC.element_to_be_clickable(locator))

    def getElementToBeVisible(self, locator, time, frequency=0.5):
        WebDriverWait(self.getWebDriver, timeout=time, poll_frequency=frequency).until(EC.visibility_of_all_elements_located(locator))

    def waitElementToBeDisappear(self, locator, time, frequency=0.5):
        WebDriverWait(self.getWebDriver, timeout=time, poll_frequency=frequency).until(EC.invisibility_of_element_located(locator))
