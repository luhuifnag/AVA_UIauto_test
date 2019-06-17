#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

import os
import unittest

from models.myunit import MyTest
from pages.buzzerpage import Buzzer
from models import readconfig
from utils.log import logger

class BuzzerTest(MyTest,Buzzer):
     '''关闭蜂鸣器的测试'''

     def test_buzzer(self):
        '''关闭蜂鸣器的测试'''
        try:
            logger.info("关闭蜂鸣器的测试")
            self.close_buzzer()
            self.driver.switch_to.frame("content")
            logger.info(self.getInnerHTML(self.text))
        except Exception as msg:
            logger.ERROR(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_buzzer.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()


if __name__ == "__main__":
   unittest.main()
