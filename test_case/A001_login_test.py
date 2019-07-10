#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''

import os
import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.loginpage import LoginPage
from pages.managepage import Manage
from utils.log import logger

class LoginTest(MyTest,LoginPage):
    '''登录测试'''


    def setUp(self):
        logger.info(u"******************测试开始******************")
        # self.driver = webdriver.Firefox()
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(readconfig.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
     
    # 测试用户登录
    def user_login(self,username="",passwd=""):
        LoginPage(self.driver).login_sys(username, passwd)

    def test_login1(self):
        '''用户名和密码都为空的登录测试'''
        try:
            logger.info("用户名和密码都为空的登录测试")
            self.user_login()
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())   #显示等待直到alert出现
            self.assertEqual(self.error_hint(), u"用户名或密码不能为空！") #error_hint()方法在LoginPage下
            self.accept_alert()       #accept_alert()方法在BasePage类下
        except Exception as msg:
            logger.error(u"异常原因：%s" % msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login1.png'))
            raise Exception("false")
        
    def test_login2(self):
        '''用户名为空的登录测试'''
        try:
            logger.info("用户名为空的登录测试")
            self.user_login(passwd="admin")
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            self.assertEqual(self.error_hint(), u"用户名或密码不能为空！")
            self.accept_alert()
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login2.png'))
            raise Exception("false")
        
    def test_login3(self):
        '''密码为的登录测试空'''
        try:
            logger.info("密码为的登录测试空")
            self.user_login(username="admin")
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            self.assertEqual(self.error_hint(),u"用户名或密码不能为空！")   
            self.accept_alert()
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login3.png'))
            raise Exception("false")
    
    def test_login4(self):
        '''错误密码的登录测试'''
        try:
            logger.info("错误密码的登录测试")
            self.user_login(username="admin", passwd="123456")
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            self.assertEqual(self.error_hint(), u"用户名不存在或密码错误！")           
            self.accept_alert()
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login4.png'))
            raise Exception("false")
        
    def test_login5(self):
        '''用户名和密码正确的登录测试'''
        try:
            logger.info("用户名和密码正确的登录测试")
            self.login_sys(readconfig.username, readconfig.password)  #login_sys方法在LoginPage类下
            WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统"))  #显示等待直到当前开头是否与预期一致
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login5.png'))
            raise Exception("false")
   
    def test_login6(self): 
        '''记住密码的登录测试'''
        try:
            logger.info("记住密码的登录测")
            self.rememberlogin_sys(readconfig.username, readconfig.password)
            WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login4.png'))
            raise Exception("false")
        
        
if __name__ == "__main__":

    unittest.main()