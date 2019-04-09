import unittest
import appiumBase


class AppiumTestDemoCase(appiumBase.AppiumBaseTestCase):

    def test_loginWithPhoneClick(self):
        loginWithPhone = self.driver.find_element_by_accessibility_id("手机号登录")
        self.assertIsNot(loginWithPhone, None, "loginWithPhone is none")
        loginWithPhone.click()


if __name__ == '__main__':
    unittest.main()
