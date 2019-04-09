import unittest
from appium import webdriver

from config.appium import DesiredCaps


class AppiumBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', DesiredCaps)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
