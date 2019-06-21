#coding:utf-8
'''
Created on 2019年06月21日

@author: Aloe
'''

import HTMLTestRunner
import os
import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.head_tail_page import HeadTail
from pages.managepage import Manage
from utils.log import logger
from pages.home_page import HomePage
from pages.record_page import RecordPage

class HeadTailTest(MyTest,HeadTail):
    '''片头片尾相关功能测试'''
    
    # def test_upload(self):
    #     '''上传片头,片尾等图片测试'''
    #     try:
    #         logger.info("上传片头,片尾等图片测试")
    #         texts =self.upload()
    #         self.assertEqual(texts , ['上传文件成功!', '上传文件成功!', '上传文件成功!', '上传文件成功!', '上传文件成功!'])
    #     except Exception as msg: 
    #         logger.error(u"异常原因：%s"%msg)
    #         self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_upload.png'))
    #         raise Exception("false")
    
    def test_set_title_trailer_time(self):
        '''片头片尾机显示视频信息测试'''
        try:
            logger.info("片头片尾机显示视频信息测试")
            self.set_title_trailer_time()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            home.click_record() 
            sleep(1)
            recordpage = RecordPage(self.driver)
            recordpage.start_recording("片头片尾","视频信息")
            sleep(6)
            recordpage.stop_recording()
        except Exception as msg: 
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_upload.png'))
            raise Exception("false")
    

        
if __name__ == "__main__":

    unittest.main()       


