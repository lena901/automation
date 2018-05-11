# coding=utf-8

import time
import unittest
from framework.browser_engineer import BrowserEngine
from pageobjects.jianshu_loginpge import LoginPage
from pageobjects.jianshu_homepage import HomePage
from framework.data_engineer import ExcelUtil
import os
import ddt
from framework.loginpublic import Login

# 测试数据
filePath = os.path.dirname(os.path.abspath('.')) + "/config/test_data.xlsx"
sheetName = "login"
data = ExcelUtil(filePath, sheetName)
testData = data.dict_data()

@ddt.ddt
class JianShuLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 初始化简书首页，并点击登录
        homepage = HomePage(cls.driver)
        # homepage.click_login()
        cls.driver.find_element_by_xpath('/html/body/nav/div/a[4]').click()
        homepage.get_windows_img()

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    @ddt.data(*testData)
    def test_login(self, data):

        # 初始化登录首页
        loginpage = LoginPage(self.driver)

        self.login(data["username"], data["password"])

        result = self.is_login_success()
        self.assertTrue(result)
        loginpage.get_windows_img()


if __name__ == "__main__":
    unittest.main()