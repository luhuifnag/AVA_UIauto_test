#coding:utf-8
'''
Created on 2019年07月17日

@author: Aloe
'''

import os
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.power_mode_page import PowerMode
from utils.log import logger


class PowerModeTest(MyTest,PowerMode):
    '''上电模式测试'''

    def test_powermode(self):
        '''上电模式测试'''
        try:
            logger.info("上电模式测试")
            home = HomePage(self.driver)
            home.swich_to_basic_label(self.powermodebtn,"上电模式")
            sleep(3)
            modes = ["关机","休眠","工作"]
            for m,i in zip(modes, range(1,4)):
                self.choose_powermode(m, i)
                self.driver.refresh()
                sleep(3)
                self.driver.switch_to.frame("content")
                check_status = (By.XPATH, "//*[@id='mode%s']/.." % str(i))
                self.assertEqual(self.getAttribute(check_status, "class"), "radio checked")
        except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_powermode.png'))
                raise Exception("false")


if __name__ == "__main__":
   unittest.main()
