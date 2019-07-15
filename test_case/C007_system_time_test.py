#coding:utf-8
'''
Created on 2019年05月24日

@author: Aloe
'''

import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.system_time_page import SystemTime
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage
from utils.log import logger

class SystemTimerTest(MyTest,SystemTime):
    '''系统时间测试'''

    def test1_no_change_time(self):
        '''手动更改设备系统时间不可测试'''
        if self.try_get_Term():
            try:
                logger.info("有效期设备系统时间不可手动更改测试")
                self.uncheck_automaticbtn()
                self.assertTrue(self.get_element_att(self.year))
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'tetst_no_change_tim.png'))
                raise Exception("false")
            finally:
                self.driver.switch_to.default_content()
        else:
            try:
                logger.info("手动修改系统时间")
                self.manual_change_time()
                self.assertEqual(self.getValuetext(self.year), "1970")
                self.assertEqual(self.getValuetext(self.month), "10")
                self.assertEqual(self.getValuetext(self.day), "20")
                self.assertEqual(self.getValuetext(self.hours), "23")
                self.assertEqual(self.getValuetext(self.minute), "59")
                self.assertEqual(self.getValuetext(self.second), "0")
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_manual_change_time.png'))
                raise Exception("false")
            finally:
                self.driver.switch_to.default_content()

    def test2_automatic_change_time(self):
        '''自动同步网络时间测试'''
        try:
            logger.info("自动同步网络时间测试")
            datelist = self.automatic_change_time()
            self.assertEqual(self.getValuetext(self.year), datelist[0])
            self.assertEqual(self.getValuetext(self.month), datelist[1])
            self.assertEqual(self.getValuetext(self.day), datelist[2])
            self.assertEqual(self.getValuetext(self.hours), datelist[3])
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_automatic_change_time.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()



            
if __name__ == "__main__":
   unittest.main()
