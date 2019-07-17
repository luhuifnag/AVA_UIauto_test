#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''
import os
import re
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.interaction_home_page import InteractionHmoe
from pages.interaction_source_page import TnteractionSource
from pages.interaction_teaching_page import IterTeaching
from pages.loginpage import LoginPage
from pages.sys_register_page import Register
from utils.log import logger
from pages.interaction_listening_page import IterListening

class TnteractionSourceTest(MyTest, InteractionHmoe, IterTeaching, TnteractionSource):
    '''互动视频源的测试'''

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

    def test_intrsource1(self): 
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
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_intrsource1.png'))
            raise Exception("false")

    def test_intrsource2(self):
        '''互动视频源的测试'''
        try:
            self.resetUp2()
            logger.info("互动视频源的测试")
            home = HomePage(self.driver)
            home.swich_to_system_label(self.Sourcebtn, "互动视频源")
            sleep(3)
            tag_num = self.get_sources_num()
            print(tag_num)
            for i in range(1, tag_num+1):
                logger.info("~~~~~~设置新的视频源~~~~~~~")
                if i==1:
                    pass
                else:
                    home.swich_to_system_label(self.Sourcebtn, "互动视频源") 
                sourcename = self.choose_source(i)
                home = HomePage(self.driver)
                home.click_system_setup_blck()
                sleep(1)
                self.join_metting(alist[0], alist[1])
                sleep(2)
                listen = IterListening(self.driver)
                self.assertEqual(self.gettext(listen.lissource), sourcename)
                self.stop_meeting()
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_intrsource2.png'))
            raise Exception("false")
        finally:
            self.driver.get(readconfig.mainurl)
            self.driver.implicitly_wait(20)
            login = LoginPage(self.driver)
            login.login_sys(readconfig.username, readconfig.password)
            sleep(2)
            self.stop_meeting()  #把主讲的会议给退出来

            
        
if __name__ == "__main__":
   unittest.main()