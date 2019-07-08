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
from ddt import ddt,file_data,unpack,data

@ddt
class VideoTagTest(unittest.TestCase):

    # @data("1","2")
    data1 = ("1","2")
    # def test1(self):
    #     alist = []
    #     for i in range(4):
    #         alist.append(i)
    #     data1 = alist
        

    @data(data1) 
    @unpack
    def test2(self, data):
        print("%s的测试" % data)
  
    

        
if __name__ == "__main__":

    unittest.main()
