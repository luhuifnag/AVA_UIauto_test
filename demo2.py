import HTMLTestRunner
import os
import sys
import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from pages.managepage import Manage
from utils.log import logger


if __name__ == '__main__':
    report_path = readconfig.report_path
    print(U"测试报告存放位置：%s" % report_path)
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    filename = report_path+'\\'+now+'result.html'
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='云互动UI自动化测试报告',description='环境：win10，firefox')
        discover = unittest.defaultTestLoader.discover("test_case",pattern="A001*test.py",top_level_dir=None)
        runner.run(discover)
        fp.close()
