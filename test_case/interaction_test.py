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


class InteractionTest(MyTest, InteractionHmoe, IterTeaching):
    '''互动页面的测试'''

    def test_create_teaching_meeting(self):
        '''创建一个不带主题和密码的授课模式空会议测试''' 
        try:
            self.create_teaching_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.metting_typle), "授课模式")
            self.assertEqual(self.getAttribute(self.metting_theam, "title"), "%s_CONF" % readconfig.name)
            self.assertNotEqual(self.gettext(self.metting_no), "")
            self.assertNotEqual(self.gettext(self.metting_pwd), "")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_teaching_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_metting()

        




if __name__ == "__main__":

    unittest.main()
