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

from models.myunit import MyTest
from pages.basepage import BasePage
from pages.managepage import Manage
from utils.log import logger


class Login5080(unittest.TestCase,BasePage):
    '''登录测试'''

    #用户名
    username = (By.ID,"uname")
    #密码
    passwd = (By.ID,"upswd")
    
    #登录 按钮
    loginbtn = (By.ID,"lgBtn")

    def input_username(self,text):
        logger.info( u"输入用户名：%s" % text)
        self.input_text(self.username, text)
        
    def input_passwd(self,text):
        logger.info (u"输入密码：%s" % text)
        self.input_text(self.passwd, text)
        
    def click_loginbtn(self):
        logger.info( u"点击 登录  按钮")
        self.click(self.loginbtn)
             
    def click_rememberpasswd(self):
        logger.info( u"勾选 记住密码")
        self.click(self.remember_passwd)


   #普通登录    
    def login_sys(self,username,passwd):
        '''获取用户名和密码登录'''
        self.clear(self.username)
        self.input_username(username)
        self.clear(self.passwd)
        self.input_passwd(passwd)
        self.click_loginbtn()
        sleep(2)


    def test_5080(self): 
        '''rserver登录测试'''
        for i in range(1,101):
            try:
                logger.info( u"第%d次登陆" %i)
                logger.info(u"******************测试开始******************")
                # self.driver = webdriver.Firefox()
                self.driver = webdriver.PhantomJS(executable_path="D:\\phantomjs\\phantomjs-2.1.1-windows\\bin\\Phantomjs")
                sleep(4)
                self.driver.maximize_window()
                self.driver.get("http://192.168.14.112:5080/")
                self.driver.implicitly_wait(20)
                self.login_sys("admin", "admin")
                WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"设备列表")) 
                self.assertEqual(self.driver.title, u"设备列表")
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                raise Exception("false")
            finally:
                logger.info(u"~~~~~~~~~~~~~~关闭浏览器~~~~~~~~~~~~~~~~~~~")
                self.driver.quit()       

        
if __name__ == "__main__":

    unittest.main()
