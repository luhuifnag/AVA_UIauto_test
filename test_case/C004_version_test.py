#coding:utf-8
'''
Created on 2019年05月14日

@author: Aloe
'''
import os
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from models import readconfig
from models.myunit import MyTest
from pages.basepage import BasePage
from pages.configure_version_page import ConVersion
from pages.home_page import HomePage
from pages.version_information_page import Version
from utils.log import logger

class VersionTest(MyTest):
    '''版本信息相关测试'''

    def test_compare_version_information(self):
        '''比较快速配置与系统设置的版本信息是否一致的测试'''    
        try:
            logger.info("比较快速配置与系统设置的版本信息是否一致的测试")
            version = Version(self.driver)
            version1 = version.get_versions()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            sleep(1)
            cversion = ConVersion(self.driver)
            version2 = cversion.get_versions()      
            self.assertEqual(version1,version2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_compare_version_information.png'))
            raise Exception("false")






        
if __name__ == "__main__":
   unittest.main()
