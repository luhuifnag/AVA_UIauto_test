#coding:utf-8
'''
Created on 2019年05月08日

@author: Aloe
'''
import os
import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.Input_output_page import InputOutput
from pages.loginpage import LoginPage
from pages.record_page import RecordPage
from pages.records import Records
from pages.video_managemen import VideoManagemen
from utils.log import logger


class Recorder(MyTest,Records,RecordPage):
    '''录制相关测试'''
            

    def test5_main_1080p_and_sub_720p(self):
        '''主码流为1080p，子码流为720p的录制测试'''
        try:
            logger.info("主码流为1080p，子码流为720p的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            self.getinto_recordset()
            self.record_main_and_sub(1,1,"1080p","720p","主码流1080p和子码流720p")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)


    def test6_main_720p_and_sub_540p(self):
        '''主码流为720p，子码流为标清的录制测试'''  
        try:
            logger.info("主码流为720p，子码流为标清的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            self.getinto_recordset()
            self.record_main_and_sub(2,2,"720p","标清","主码流720p和子码流标清")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)

    def test7_main_540p_and_sub_360p(self):
        '''主码流为标清，子码流为流畅的录制测试'''  
        try:
            logger.info("主码流为标清，子码流为流畅的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            self.getinto_recordset()
            self.record_main_and_sub(3,3,"标清","流畅","主码流标清和子码流流畅")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg) #1236


            
        
if __name__ == "__main__":
   unittest.main()
