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
from utils.log import logger

class VideoTest(MyTest, VideoManagemen):
    '''录制管理相关测试'''

    def test1_delete_documents(self):
        '''删除一个录制文件的测试'''
        try:
            logger.info("删除一个录制文件的测试")
            video = VideoManagemen(self.driver)
            video.check_recorder_massage()
            base = BasePage(self.driver)
            total1 = base.gettext(video.total_documents)
            logger.info(total1)
            totalCount1 = int(re.sub(r"\D", "", total1)) #提取字符串中的数字并将其转化为int类型
            video.delete_documents()
            total2 = base.gettext(video.total_documents)
            totalCount2 = int(re.sub(r"\D", "", total2))
            logger.info(total2)      
            self.assertEqual(totalCount1-1,totalCount2)
            sleep(2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_delete_documents.png'))
            raise Exception("false")

    def test2_compare_total_documents(self):
        '''比较快速配置与录像管理的文件总数是否一致的测试'''
        try:  
            logger.info("比较快速配置与录像管理的文件总数是否一致的测试") 
            video1 = VideoManagemen(self.driver)
            total1 = video1.check_total_documents()
            home = HomePage(self.driver)
            home.click_video_managemen_black()
            sleep(1)
            video2 = VideoQuery(self.driver)
            total2 = video2.check_total_documents()   
            self.assertEqual(total1,total2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_compare_total_documents.png'))
            raise Exception("false")
    
    def test3_sortfile1(self):
        '''按主题排序文件'''
        try:
            logger.info("按主题排序文件")
            self.sortfile(1)
            themeslist1 = self.get_themes()
            themeslist2 = sorted(themeslist1)
            self.assertEqual(themeslist1, themeslist2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile1.png'))
            raise Exception("false")

    def test3_sortfile2(self):
        '''按主讲排序文件'''
        try:
            logger.info("按主讲排序文件")
            self.sortfile(2)
            speakerlist1 = self.get_themes()
            speakerlist2 = sorted(speakerlist1)
            self.assertEqual(speakerlist1,speakerlist2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile2.png'))
            raise Exception("false")

    def test3_sortfile3(self):
        '''按时间排序文件'''
        try:
            logger.info("按时间排序文件")
            self.sortfile(3)
            timelist1 = self.get_themes()
            timelist2 = sorted(timelist1, reverse=True) #降序排序
            self.assertEqual(timelist1,timelist2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile3.png'))
            raise Exception("false")
    
    def test3_sortfile4(self):
        '''按时长排序文件'''
        try:
            logger.info("按时长排序文件")
            self.sortfile(4)
            longlist1 = self.get_themes()
            longlist1 = list(map(int, longlist1)) # 将列表里的字符串转化为int再排序
            longlist2 = sorted(longlist1) 
            self.assertEqual(longlist1,longlist2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile4.png'))
            raise Exception("false")

    def test3_sortfile5(self):
        '''按主题分组显示'''
        try:
            logger.info("按主题分组显示")
            self.group_display(1)
            self.assertIn("主 题", self.gettext(self.packet_label))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile5.png'))
            raise Exception("false")

    def test3_sortfile6(self):
        '''按主讲分组显示'''
        try:
            logger.info("按主讲分组显示")
            self.group_display(2)
            self.assertIn("主讲人", self.gettext(self.packet_label))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_sortfile6.png'))
            raise Exception("false")



if __name__ == "__main__":
   unittest.main()

