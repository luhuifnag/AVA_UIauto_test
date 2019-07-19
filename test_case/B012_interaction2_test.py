#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''
import re
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
from pages.loginpage import LoginPage

class InteractionHomeTest2(MyTest, InteractionHmoe, IterTeaching):
    '''互动页面的测试'''
    
    def setUp(self):
        pass

    def resetUp1(self):
        logger.info(u"******************测试开始******************")
        self.driver = webdriver.Firefox()
        sleep(4)
        self.driver.maximize_window()
        self.driver.get(readconfig.mainurl)
        self.driver.implicitly_wait(20)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 
    
    def resetUp2(self):
        logger.info(u"******************测试开始******************")
        self.driver = webdriver.Firefox()
        sleep(4)
        self.driver.maximize_window()
        self.driver.get(readconfig.url)
        self.driver.implicitly_wait(20)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 
    ########################此处重写两个新的setUp()方法######################

    alist = [] #创建一个全局变量来存放主讲的会议号和密码

    def test1_join_teaching_meeting1(self): 
        '''创建一个被加入的授课模式会议'''
        global alist
        alist = [] 
        try:
            self.resetUp1()
            logger.info("创建一个被加入的授课模式会议")
            self.create_teaching_meeting("")
            sleep(2)
            alist.append(self.gettext(self.meeting_no)[-8:])#截取会议号
            alist.append(re.sub(r"\D", "", self.gettext(self.meeting_pwd)))   #只保留数字
            print(alist)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_join_teaching_meeting1.png'))
            raise Exception("false")

    def test1_join_teaching_meeting2(self):
        '''加入一个授课模式会议'''
        try:
            self.resetUp2()
            logger.info("加入一个授课模式会议")
            self.join_metting(alist[0], alist[1])
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "听课模式")
            self.assertIn(alist[0], self.gettext(self.meeting_no))
            self.assertIn(alist[1], self.gettext(self.meeting_pwd))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_join_teaching_meeting2.png'))
            raise Exception("false")
        finally:
            self.stop_two_meeting()

    def test2_join_meeting_meeting1(self): 
        '''创建一个被加入的会议模式会议'''
        global alist
        alist = [] 
        try:
            self.resetUp1()
            logger.info("创建一个被加入的会议模式会议")
            self.create_meeting_meeting("")
            sleep(2)
            alist.append(self.gettext(self.meeting_no)[-8:])#截取会议号
            alist.append(re.sub(r"\D", "", self.gettext(self.meeting_pwd)))   #只保留数字
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test2_join_meeting_meeting1.png'))
            raise Exception("false")

    def test2_join_meeting_meeting2(self):
        '''加入一个会议模式会议'''
        try:
            self.resetUp2()
            logger.info("加入一个会议模式会议")
            self.join_metting(alist[0], alist[1])
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "听课模式")
            self.assertIn(alist[0], self.gettext(self.meeting_no))
            self.assertIn(alist[1], self.gettext(self.meeting_pwd))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test2_join_meeting_meeting2.png'))
            raise Exception("false")
        finally:
            self.stop_two_meeting()
    
    def test3_join_cloud_meeting1(self): 
        '''创建一个被加入的内置云会议'''
        global alist
        alist = [] 
        try:
            self.resetUp1()
            logger.info("创建一个被加入的内置云会议")
            self.create_cloud_meeting("")
            sleep(2)
            alist.append(self.gettext(self.meeting_no)[-9:]) #截取会议号 (内置云会议号是9位的)
            alist.append(re.sub(r"\D", "", self.gettext(self.meeting_pwd)))   #只保留数字
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_join_meeting_meeting1.png'))
            raise Exception("false")

    def test3_join_cloud_meeting2(self):
        '''加入一个内置云会议'''
        try:
            self.resetUp2()
            logger.info("加入一个内置云会议")
            self.join_metting(alist[0], alist[1])
            sleep(2)
            self.assertEqual(self.gettext(self.meeting_typle), "听课模式")
            self.assertIn(alist[0], self.gettext(self.meeting_no))
            self.assertIn(alist[1], self.gettext(self.meeting_pwd))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test4_join_meeting_meeting2.png'))
            raise Exception("false")
        finally:
            self.stop_two_meeting()

    def test4_join_failed(self):
        '''加入会议失败的测试'''
        try:
            self.resetUp2() 
            logger.info("加入会议失败的测试")
            self.join_metting("123456", "123456")
            WebDriverWait(self.driver,5,0.5).until(ES.presence_of_element_located(self.alert_text)) 
            self.assertEqual(self.gettext(self.alert_text), u"加入失败！")
            self.click(self.alert_sure)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test4_join_failed.png'))
            raise Exception("false")



if __name__ == "__main__":

    unittest.main()