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

from models.status import Status

class VideoTagTest(MyTest, VideoTag):

    def test1(self):
        status = Status()
        status.try_get_status()

        
if __name__ == "__main__":

    unittest.main()
