#coding:utf-8
'''
Created on 2019年05月08日

@author: Aloe
'''
import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from pages.restore_default_page import Restore
from models import readconfig
from utils.log import logger

class Restore_tests(MyTest,Restore):
    '''恢复默认操作测试'''

    def test_restore(self):
        '''恢复默认操作测试'''
        try:
            logger.info("恢复默认操作测试")
            self.restore()      
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_restore.png'))
            raise Exception("false")
        

if __name__ == "__main__":
    unittest.main()