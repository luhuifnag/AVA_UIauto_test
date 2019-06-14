#coding:utf-8
'''
Created on 2019年06月06日

@author: Aloe
'''

import os
import unittest
from time import sleep


from models.myunit import MyTest
from pages.video_tag_page import VideoTag
from models import readconfig
from pages.home_page import HomePage
from pages.record_page import RecordPage
from pages.interaction_home_page import InteractionHmoe
from pages.interaction_teaching_page import IterTeaching

class VideoTagTest(MyTest, VideoTag):
    '''视频标签测试'''

    def test1_input_custom_label(self):
        '''选择自定义标签测试（录播模式）'''
        try:
            a = self.input_custom_label()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            sleep(1)
            home.click_record()
            sleep(4)
            record = RecordPage(self.driver)
            b = record.get_preview_tag()
            self.assertEqual(a, b)
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test1_input_custom_label.png'))
            raise Exception("false")

    def test2_input_custom_label(self):
        '''选择自定义标签测试（互动模式）'''
        try:
            a = self.input_custom_label()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            sleep(1)
            interhmoe = InteractionHmoe(self.driver)
            interhmoe.create_teaching_meeting("")
            interteach = IterTeaching(self.driver)
            b = interteach.get_preview_tag()
            interteach.stop_meeting()
            self.assertEqual(a, b)
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test2_input_custom_label.png'))
            raise Exception("false")

    def test3_C_default(self):
        '''选择默认标签测试'''
        try:
            self.C_default()
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test2_C_defaultr.png'))
            raise Exception("false")



if __name__ == "__main__":

    unittest.main()