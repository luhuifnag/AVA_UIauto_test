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


class InteractionTest(MyTest, InteractionHmoe, IterTeaching):
    '''互动页面的测试'''

    # def test_create_teaching_meeting(self):
    #     '''创建一个不带主题和密码的授课模式空会议测试''' 
    #     try:
    #         self.create_teaching_meeting("")
    #         sleep(2)
    #         self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
    #         self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_CONF" % readconfig.name)
    #         self.assertNotEqual(self.gettext(self.meeting_no), "")
    #         self.assertNotEqual(self.gettext(self.meeting_pwd), "")
    #     except Exception as msg:
    #         print(u"异常原因：%s"%msg)
    #         self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_teaching_meeting.png'))
    #         raise Exception("false")
    #     finally:
    #         self.stop_meeting()

    # def test_create_teaching_meeting2(self):
    #     '''创建一个自定义主题和密码的授课模式的会议测试''' 
    #     try:
    #         self.create_teaching_meeting2("自动化授课", "516896", "")
    #         sleep(2)
    #         self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
    #         self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "自动化授课")
    #         self.assertNotEqual(self.gettext(self.meeting_no), "")
    #         self.assertEqual(self.gettext(self.meeting_pwd), "会议密码：516896")
    #     except Exception as msg:
    #         print(u"异常原因：%s"%msg)
    #         self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_teaching_meeting2.png'))
    #         raise Exception("false")
    #     finally:
    #         self.stop_meeting()

    def test_create_Double_teaching_meeting(self):
        '''创建一个双流的授课模式空会议测试''' 
        try:
            self.create_Double_teaching_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_CONF" % readconfig.name)
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertNotEqual(self.gettext(self.meeting_pwd), "")
            self.assertEqual(self.gettext(self.doubletag), "双流")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_Doubl_teachinge_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    # def test_create_teaching_meeting3(self):
    #     '''创建一个有三个在线听课的授课模式的会议测试''' 
    #     try:
    #         # self.create_teaching_meeting(readconfig.Attendant1+";"+readconfig.Attendant2+";"+readconfig.Attendant3)
    #         self.create_teaching_meeting("auto01;auto02;auto03")
    #         # self.create_teaching_meeting(readconfig.Attendant1)
    #         sleep(2)
    #         self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
    #         self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_CONF" % readconfig.name)

    #     except Exception as msg:
    #         print(u"异常原因：%s"%msg)
    #         self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_teaching_meeting3.png'))
    #         raise Exception("false")
    #     finally:
    #         self.stop_meeting()

    def test_create_meeting_meeting(self):
        '''创建一个不带主题和密码的会议式空会议测试''' 
        try:
            self.create_meeting_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "会议模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_CONF" % readconfig.name)
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertNotEqual(self.gettext(self.meeting_pwd), "")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_meeting_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()    

    def test_create_meeting_meeting2(self):
        '''创建一个自定义主题和密码的会议模式的会议测试''' 
        try:
            self.create_meeting_meeting2("自动化会议", "516896", "")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "会议模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "自动化会议")
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertEqual(self.gettext(self.meeting_pwd), "会议密码：516896")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_meeting_meeting2.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_create_Double_meeting_meeting(self):
        '''创建一个双流的会议模式空会议测试''' 
        try:
            self.create_Double_meeting_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "会议模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_CONF" % readconfig.name)
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertNotEqual(self.gettext(self.meeting_pwd), "")
            self.assertEqual(self.gettext(self.doubletag), "双流")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_Doubl_meeting_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_create_cloud_meeting(self):
        '''创建一个不带主题和密码的内置云会议测试''' 
        try:
            self.create_cloud_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_Conference" % readconfig.name)
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertNotEqual(self.gettext(self.meeting_pwd), "")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_cloud_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_create_cloud_meeting2(self):
        '''创建一个自定义主题和密码的内置云会议的测试''' 
        try:
            self.create_cloud_meeting2("自动化内置云会议", "516896", "")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "自动化内置云会议")
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertEqual(self.gettext(self.meeting_pwd), "会议密码：516896")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_cloud_meeting2.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_create_Double_cloud_meeting(self):
        '''创建一个双流的内置云会议测试''' 
        try:
            self.create_Double_cloud_meeting("")
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "授课模式")
            self.assertEqual(self.getAttribute(self.meeting_theam, "title"), "%s_Conference" % readconfig.name)
            self.assertNotEqual(self.gettext(self.meeting_no), "")
            self.assertNotEqual(self.gettext(self.meeting_pwd), "")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_create_Doubl_cloud_meeting.png'))
            raise Exception("false")
        finally:
            self.stop_meeting()

    def test_link_jump(self):
        '''互动设置转跳系统设置-注册服务测试'''
        try:
            self.link_jump()
            register = Register(self.driver)
            self.driver.switch_to.default_content() 
            self.assertIn, "注册服务", (self.getAttribute(register.Registerbtn, "text"))
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_link_jump.png'))
            raise Exception("false")


if __name__ == "__main__":

    unittest.main()
