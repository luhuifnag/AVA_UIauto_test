#coding:utf-8
'''
Created on 2019年07月08日

@author: Aloe
'''
import os
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from pages.security_page import Security
from utils.log import logger


class SecurityTest(MyTest, Security):
    '''安全验证相关测试'''

    def setUp(self):
        logger.info(u"******************测试开始******************")
        self.driver = webdriver.Firefox()
        sleep(4)
        self.driver.maximize_window()
        self.driver.get(readconfig.url)
        self.driver.implicitly_wait(20)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, "123456")
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 
        

    def test1_start_security(self):
        '''启用安全验证测试'''
        try:
            logger.info("启用安全验证测试")
            self.start_security()
            sleep(2)
            self.driver.refresh()
            sleep(3)
            self.driver.switch_to.frame("content")
            self.assertNotEqual(self.getValuetext(self.safetyCheckCode),"")
        except Exception as msg:
            logger.error(u"异常原因：%s" % msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_start_security.png'))
            raise Exception("false")

    def test2_off_security(self):
        '''不启用安全验证测试'''
        try:
            logger.info("不启用安全验证测试")
            self.off_security()
            sleep(2)
            self.driver.refresh()
            sleep(3)
            self.driver.switch_to.frame("content")
            self.assertEqual(self.getValuetext(self.safetyCheckCode),"")
        except Exception as msg:
            logger.error(u"异常原因：%s" % msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_off_security.png'))
            raise Exception("false")


if __name__ == "__main__":

    unittest.main()