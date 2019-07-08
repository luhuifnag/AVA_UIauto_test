#coding:utf-8
'''
Created on 2019年07月08日

@author: Aloe
'''

import os
import time
import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.loginpage import LoginPage
from utils.log import logger
from pages.user_manage_page import UserMange

class UserMangeTest1(MyTest,UserMange):
    '''用户管理相关测试'''

    def test_change_admin_pwd(self):
        '''更改管理员密码'''
        try:
            logger.info("更改管理员密码")
            self.change_admin_pwd("123456")
            sleep(2)
            self.driver.refresh()
            sleep(2)
            login = LoginPage(self.driver)
            login.login_sys("admin", "123456")
            WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统"))  #显示等待直到当前开头是否与预期一致
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_change_admin_pwd.png'))
            raise Exception("false")


   
if __name__ == "__main__":

    unittest.main()
