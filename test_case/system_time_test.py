#coding:utf-8
'''
Created on 2019年05月24日

@author: Aloe
'''


import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.system_time_page import SystemTime


class SystemTimerTest(MyTest,SystemTime):
    '''系统时间测试'''

    def test1_manual_change_time(self):
        '''手动修改系统时间'''
        try:
            self.manual_change_time()
            self.assertEqual(self.getValuetext(self.year), "1970")
            self.assertEqual(self.getValuetext(self.month), "10")
            self.assertEqual(self.getValuetext(self.day), "20")
            self.assertEqual(self.getValuetext(self.hours), "23")
            self.assertEqual(self.getValuetext(self.minute), "59")
            self.assertEqual(self.getValuetext(self.second), "0")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test1_manual_change_time.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()


    def test2_automatic_change_time(self):
        '''自动同步网络时间测试'''
        try:
            datelist = self.automatic_change_time()
            self.assertEqual(self.getValuetext(self.year), datelist[0])
            self.assertEqual(self.getValuetext(self.month), datelist[1])
            self.assertEqual(self.getValuetext(self.day), datelist[2])
            self.assertEqual(self.getValuetext(self.hours), datelist[3])
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test2_automatic_change_time.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()



            
if __name__ == "__main__":
   unittest.main()
