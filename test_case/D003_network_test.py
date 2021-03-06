#coding:utf-8
'''
Created on 2019年04月28日

@author: Aloe
'''

import os
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from pages.networkpage import Network
from utils.log import logger


class ModifyingNetworkTest2(MyTest):
    '''在系统设置中更改IP测试'''
    
    def login(self):
        logger.info(u"******************测试开始******************")
        self.driver.get(readconfig.newurl)
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 


    def test6_change_ip(self):
        '''在系统设置中更改IP测试'''
        try:
            logger.info("在系统设置中更改IP测试")
            self.login()
            network = Network(self.driver) 
            network.change_ip(readconfig.netaddr1,readconfig.netaddr2,readconfig.netaddr3,readconfig.netaddr4,\
            readconfig.gateway1,readconfig.gateway2,readconfig.gateway3,readconfig.gateway4) 
            sleep(2)                
            self.driver.refresh()
            sleep(3)
            new_url = self.driver.current_url
            login = LoginPage(self.driver)
            login.login_sys(readconfig.username, readconfig.password)
            sleep(2)
            self.assertEqual(new_url,"%s/login.html" % readconfig.url)
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_change_ip.png'))
            raise Exception("false")



  
if __name__ == "__main__":
   unittest.main()