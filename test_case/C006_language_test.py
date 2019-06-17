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
from pages.language_page import Languages
from utils.log import logger


class LanguagesTest(MyTest, Languages):
    '''语言切换测试'''

    def test1_switch_english(self):
        '''切换成英文'''
        try:
            logger.info("切换成英文测试")
            self.switch_english()
            sleep(3)
            self.driver.switch_to.default_content()     
            self.driver.switch_to.frame("content")  
            self.assertEqual(self.gettext(self.tips), "Remark:The browser will automatically refresh!")    
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_switch_english.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()    


    def test2_switch_Chinese(self):
        '''切换成中文'''
        try:
            logger.info("切换成中文测试")
            self.switch_Chinese()
            sleep(3)
            self.driver.switch_to.default_content()     
            self.driver.switch_to.frame("content")  
            self.assertEqual(self.gettext(self.tips), "注意：浏览器将自动刷新！")    
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_switch_Chinese.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()    


    

            
        
if __name__ == "__main__":
   unittest.main()
