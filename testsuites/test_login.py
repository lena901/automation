# coding=utf-8

import time
import unittest
from framework.browser_engineer import BrowserEngine
from pageobjects.jianshu_homepage import HomePage
from framework.data_engineer import ExcelUtil
import os
import ddt
from framework.login_go import LoginGo

# 测试数据
filePath = os.path.dirname(os.path.abspath('.')) + "/config/test_data.xlsx"
sheetName = "login"
data = ExcelUtil(filePath, sheetName)
testData = data.dict_data()
print(testData)

@ddt.ddt
class JianShuLogin(unittest.TestCase):

    # @classmethod
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        # 初始化简书首页，并点击登录
        homepage = HomePage(self.driver)
        # homepage.click_login()
        self.driver.find_element_by_xpath('/html/body/nav/div/a[4]').click()
        homepage.get_windows_img()

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    @ddt.data(*testData)
    def test_login(self, data):
        """登录用例"""
        print ("当前测试数据%s" % data)
        # 初始化登录首页
        logingo = LoginGo(self.driver)

        logingo.login(data[u"username"], data[u"password"])

        result = logingo.is_login_success()
        self.assertTrue(result)
        logingo.get_windows_img()


if __name__ == "__main__":
    unittest.main()