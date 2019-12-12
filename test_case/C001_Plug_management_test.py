#coding:utf-8
'''
Created on 2019年06月18日

@author: Aloe
'''
import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage

from pages.basepage import BasePage
from utils.log import logger
from pages.Plug_management import PlugManagement

class PlugTest(MyTest, PlugManagement):
    '''插件下载相关测试'''

    def test_download1(self):
        '''下载windows播放器插件1'''
        try:
            logger.info("下载windows播放器插件1")
            self.login()
            self.click_download(1)
            handles = self.driver.window_handles  #获取当前打开的所有窗口的句柄
            self.driver.switch_to.window(handles[1])  #切换到第二个窗口的句柄
            self.assertEqual(self.driver.current_url, "https://sourceforge.net/projects/fbvlc/files/latest/download")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_download1.png'))
            raise Exception("false")
        
    def test_download2(self):
        '''下载windows播放器插件2(support H265)'''
        try:
            logger.info("下载windows播放器插件2(support H265)")
            self.login()
            self.click_download(2)
            handles = self.driver.window_handles  #获取当前打开的所有窗口的句柄
            self.driver.switch_to.window(handles[1])  #切换到第二个窗口的句柄
            self.assertEqual(self.driver.current_url, "https://sourceforge.net/projects/webchimera/files/latest/download")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_download2.png'))
            raise Exception("false")
        

    def test_download3(self):
        '''下载MAC版播放器插件'''
        try:
            logger.info("下载MAC版播放器插件")
            self.login()
            self.click_download(3)
            handles = self.driver.window_handles  #获取当前打开的所有窗口的句柄
            self.driver.switch_to.window(handles[1])  #切换到第二个窗口的句柄
            self.assertEqual(self.driver.current_url, "https://sourceforge.net/projects/fbvlc/files/FBVLC_0.1.5_vlc_2.1.4.dmg/download")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_download3.png'))
            raise Exception("false")
    

if __name__ == "__main__":
    unittest.main()

