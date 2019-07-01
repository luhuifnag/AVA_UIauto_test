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
from utils.log import logger

class VideoTagTest(MyTest, VideoTag):
    def test1(self):
        for i in range(2):
            print("2的测试")
            self.test1()
    
    def test2(self):
        print("1的测试")

        
if __name__ == "__main__":

    unittest.main()
