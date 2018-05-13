# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")

# 构建suite
ts = os.path.dirname(os.path.abspath('.')) + '/testsuites/'
suite = unittest.TestLoader().discover(ts, pattern="test*.py")

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"简书项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)


