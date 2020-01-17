#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''

import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from utils.log import logger

class MyTest(unittest.TestCase):

    def setUp(self):
        logger.info(u"******************测试开始******************")
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.PhantomJS(executable_path="D:\\phantomjs\\phantomjs-2.1.1-windows\\bin\\Phantomjs")  #使用无头浏览器跑脚本
        self.driver.maximize_window()

   
    def tearDown(self):
        logger.info(u"~~~~~~~~~~~~~~关闭浏览器~~~~~~~~~~~~~~~~~~~")
        self.driver.quit()


    def login (self):
        self.driver.get(readconfig.url)
        self.driver.implicitly_wait(20)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)
