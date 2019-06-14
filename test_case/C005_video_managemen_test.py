#coding:utf-8
'''
Created on 2019年05月14日

@author: Aloe
'''
import os
import unittest
from time import sleep
import re

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.video_managemen import VideoManagemen
from pages.configure_video_page import VideoQuery
from pages.basepage import BasePage

class VideoTest(MyTest):
    '''录制管理相关测试'''

    def test1_delete_documents(self):
        '''删除一个录制文件的测试'''
        try:
            video = VideoManagemen(self.driver)
            video.check_recorder_massage()
            base = BasePage(self.driver)
            total1 = base.gettext(video.total_documents)
            print(total1)
            totalCount1 = int(re.sub(r"\D", "", total1)) #提取字符串中的数字并将其转化为int类型
            video.delete_documents()
            total2 = base.gettext(video.total_documents)
            totalCount2 = int(re.sub(r"\D", "", total2))
            print(total2)      
            self.assertEqual(totalCount1-1,totalCount2)
            sleep(2)
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_delete_documents.png'))
            raise Exception("false")



    def test2_compare_total_documents(self):
        '''比较快速配置与录像管理的文件总数是否一致的测试'''
        try:   
            video1 = VideoManagemen(self.driver)
            total1 = video1.check_total_documents()
            home = HomePage(self.driver)
            home.click_video_managemen_black()
            sleep(1)
            video2 = VideoQuery(self.driver)
            total2 = video2.check_total_documents()   
            self.assertEqual(total1,total2)
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_compare_total_documents.png'))
            raise Exception("false")


if __name__ == "__main__":
   unittest.main()

