#coding:utf-8
'''
Created on 2019年06月27日

@author: Aloe
'''

import os
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.preset_subtitles_page import PresetSubitles
from pages.record_page import RecordPage
from utils.log import logger


class PresetSubitlesTest(MyTest, PresetSubitles):
    '''预设字幕的测试'''


    def test_preosd(self):
        '''预设字幕的测试'''
        try:
            logger.info("预设字幕的测试")
            self.set_preosd()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            sleep(1)
            home.click_record()
            sleep(2)
            recordpage = RecordPage(self.driver)
            self.click(recordpage.subtitlebtn)
            sleep(2)
            subtitles1 = recordpage.get_subtitles()
            subtitles2 = [ '第一条自定义的字幕','The first custom subtitle','笑一笑，你的人生会更美好','秋天的天空像一块覆盖大地的蓝宝石','今天又是美好的一天！！！']
            self.assertEqual(subtitles1, subtitles2)
        except Exception as msg: 
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_preosd.png'))
            raise Exception("false")



if __name__ == "__main__":

    unittest.main()       
