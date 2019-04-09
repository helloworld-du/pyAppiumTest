#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appiumBase.AppiumBase import AppiumBaseTestCase


class AppiumTestDemoCase(AppiumBaseTestCase):

    def test_loginWithPhoneClick(self):
        loginWithPhone = self.driver.find_element_by_accessibility_id(u"手机号登录")
        self.assertIsNot(loginWithPhone, None, "loginWithPhone is none")
        loginWithPhone.click()


if __name__ == '__main__':
    unittest.main()
