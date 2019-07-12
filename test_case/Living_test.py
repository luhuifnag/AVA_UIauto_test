#coding:utf-8
'''
Created on 2019年07月12日

@author: Aloe
'''
import os
import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.Living_page import Living
from pages.managepage import Manage

from pages.record_page import RecordPage
from utils.log import logger

class LivingTest(MyTest, Living):
    '''直播相关测试'''

    def test_main_sub_living(self):
        '''主码流和子码流的直播推流测试'''
        try:
            logger.info("主码流和子码流的直播推流测试")
            self.set_living()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            mange = Manage(self.driver)
            mange.interaction_constraints2() # 在直播过程中回到主页
            self.getin_live()
            self.assertEqual(self.check_live_state(3),"已开启")
            self.assertEqual(self.check_live_state(4),"已开启")
            self.assertEqual(self.get_total(),"推流总数：2")      
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_main_sub_living.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()
            home.click_system_setup_blck()
            home.click_record()
            recordpage = RecordPage(self.driver)
            recordpage.stop_live()

    def test_Living_change(self):
        '''在直播过程中更改主码流和子码流的质量'''
        try:
            logger.info("在直播过程中更改主码流和子码流的质量")
            self.set_living()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            mange = Manage(self.driver)
            mange.interaction_constraints2() # 在直播过程中回到主页
            self.getin_live()
            for i in range(1,5):
                self.set_main_quality(i)
                self.ensure()
                self.driver.switch_to.frame("content")
                self.assertEqual(self.check_live_state(3),"已开启")
            for i in range(1,4):
                self.set_sub_quality(i)
                self.ensure()
                self.driver.switch_to.frame("content")
                self.assertEqual(self.check_live_state(4),"已开启")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_Living_change.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()
            home.click_system_setup_blck()
            home.click_record()
            recordpage = RecordPage(self.driver)
            recordpage.stop_live()

    def test_Living_change2(self):
        '''在直播过程中更改推流类型'''
        try:
            logger.info("在直播过程中更改推流类型")
            self.set_living()
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            mange = Manage(self.driver)
            mange.interaction_constraints2() # 在直播过程中回到主页
            self.getin_live()
            self.disconnet()
            sleep(2)
            self.select_live_type("子码流", 0)
            sleep(1)
            self.connet()
            sleep(2)
            self.assertEqual(self.check_live_state(3),"已开启")
            self.disconnet(4)
            sleep(2)
            self.select_live_type("主码流", 1)
            sleep(1)
            self.connet(4)
            sleep(2)
            self.assertEqual(self.check_live_state(3),"已开启")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_Living_change2.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content()
            home.click_system_setup_blck()
            home.click_record()
            recordpage = RecordPage(self.driver)
            recordpage.stop_live()

    # def test_living_lock(self):
    #     '''锁住后推流地址不可编辑的测试'''
    #     try:
    #         logger.info("在直播过程中更改推流类型")
    #         self.getin_live()
    #         self.off_lock()
    #         sleep(1)
    #         self.assertTrue(self.able_liveurl())
    #     except Exception as msg:
    #         logger.error(u"异常原因：%s"%msg)
    #         self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_living_lock.png'))
    #         raise Exception("false")



if __name__ == "__main__":
   unittest.main()
