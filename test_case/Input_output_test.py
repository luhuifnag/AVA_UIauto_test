#coding:utf-8
'''
Created on 2019年06月21日

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
from pages.Input_output_page import InputOutput

class InputOutputTest(MyTest, InputOutput):
    '''输入输出相关测试'''
    
    def test_change_poc_state(self):
        '''更改poc供电状态测试'''
        try:
            logger.info("更改poc供电状态测试'")
            state = self.change_poc_state()
            self.assertEqual(state, ('PoC未连接', 'PoC已连接'))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_change_poc_state.png'))
            raise Exception("false")
        


if __name__ == "__main__":

    unittest.main()
