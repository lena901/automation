# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engineer import BrowserEngine
from selenium import webdriver

from pageobjects.jianshu_homepage import HomePage

class JianShuSearch(unittest.TestCase):

    @classmethod  # python的类方法
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_jia_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法

        # try:
        #     assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     # print ('Test Pass.')
        # except Exception as e:
        #     print ('Test Fail.', format(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()