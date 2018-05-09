# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engineer import BrowserEngine
from selenium import webdriver

from pageobjects.jianshu_loginpge import LoginPage

from pageobjects.jianshu_homepage import HomePage

class JianShuLogin(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_login(self):
        # 初始化简书首页，并点击登录
        homepage = HomePage(self.driver)
        # homepage.click_login()
        self.driver.find_element_by_xpath('/html/body/nav/div/a[4]').click()

        homepage.get_windows_img()
        # 初始化登录首页
        loginpage = LoginPage(self.driver)
        # self.driver.find_element_by_id("session_email")
        loginpage.type_username("pp.liu")
        # self.driver.find_element_by_id("session_password")
        loginpage.type_password("123456")
        # self.driver.find_element_by_class_name("sign-in-button")
        loginpage.send_login_btn()
        time.sleep(2)
        loginpage.get_windows_img()


if __name__ == "__main__":
    unittest.main()