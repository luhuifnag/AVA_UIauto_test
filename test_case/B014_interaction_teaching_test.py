#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''

import unittest
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.interaction_home_page import InteractionHmoe
from pages.interaction_teaching_page import IterTeaching
from pages.sys_register_page import Register
from utils.log import logger
from pages.home_page import HomePage

class IterTeachingTest(MyTest, InteractionHmoe, IterTeaching):
    '''授课模式会议的测试'''

    def test_online_addlistener(self):
        '''在会议中成功添加一个在在线的听课'''
        try:
            logger.info("在会议中成功添加一个在线的听课")
            self.create_teaching_meeting("")
            sleep(2)
            self.addlistener(readconfig.Attendant1)
            sleep(8)
            self.assertEqual(self.get_usernum(), 2)
            self.assertTrue(self.judge_Success_added())
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_online_addlistene.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_offline_addlistener(self):
        '''在会议中添加一个不在线的听课'''
        try:
            logger.info("在会议中添加一个不在线的听课")
            self.create_teaching_meeting("")
            sleep(2)
            self.addlistener(readconfig.offAttendant1)
            sleep(5)
            self.assertEqual(self.get_usernum(), 2)
            self.assertFalse(self.judge_Success_added())
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_offline_addlistener.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_remove_listener(self):
        '''移除听课的测试'''
        try:
            logger.info("移除听课的测试")
            self.create_teaching_meeting(readconfig.Attendant1)
            sleep(2)
            self.remove_listener()
            self.assertEqual(self.get_usernum(), 2)
            self.assertFalse(self.judge_Success_added())
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_remove_listener.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_del_listener(self):
        '''删除听课的测试'''
        try:
            logger.info("删除听课的测试")
            self.create_teaching_meeting(readconfig.Attendant1)
            sleep(2)
            self.del_listener()
            self.assertEqual(self.get_usernum(), 1)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_del_listener.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

if __name__ == "__main__":

    unittest.main()