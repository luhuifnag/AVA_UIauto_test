#coding:utf-8
'''
Created on 2019年05月18日

@author: Aloe
'''

import os
import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.basepage import BasePage
from pages.configure_register_page import ConfigureRegister
from utils.log import logger

class ConfigureRegisterTest(MyTest,ConfigureRegister):
    '''快速配置，rserver注册相关测试'''

    def test_register1(self):
        ''' 服务器地址为空的rsever注册测试'''
        try:
            logger.info("服务器地址为空的rsever注册测试")
            self.login()
            self.register_rserver("",readconfig.name,readconfig.pwd,readconfig.machineName)
            sleep(3)
            self.assertEqual(self.error_hint(), u"服务器地址不能为空！") 
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            sleep(2)
            self.accept_alert()     
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register1.png'))
            raise Exception("false")


    def test_register2(self):
        ''' 服务账号为空的rsever注册测试'''  
        try:
            logger.info("服务账号为空的rsever注册测试")
            self.login()
            self.register_rserver(readconfig.rserverip,"",readconfig.pwd,readconfig.machineName)
            sleep(3)
            self.assertEqual(self.error_hint(), u"用户账号不能为空！") 
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            sleep(2)
            self.accept_alert()      
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register2.png'))
            raise Exception("false")

    
    def test_register3(self):
        ''' 服务昵称为空的rsever注册测试'''   
        try:
            logger.info("服务昵称为空的rsever注册测试")
            self.login()
            self.register_rserver(readconfig.rserverip,readconfig.name,readconfig.pwd,"")
            sleep(3)
            self.assertEqual(self.error_hint(), u"用户昵称不能为空！") 
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            sleep(2)
            self.accept_alert()      
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register3.png'))
            raise Exception("false")
    
    def test_register4(self):
        ''' 非白名单的用户注册'''   
        try:
            logger.info("非白名单的用户注册")
            self.login()
            self.register_rserver(readconfig.rserverip,"djicnf",readconfig.pwd,readconfig.machineName)
            sleep(20)
            base = BasePage(self.driver)
            self.assertEqual(base.gettext(self.regstateStatus), u"注册错误！当前设备未在Rserver注册！")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register4.png'))
            raise Exception("false")
     

    def test_register5(self):
        ''' 使用备用服务器成功注册rserver'''
        try:
            logger.info("使用备用服务器成功注册rserver")
            self.login()
            self.register_rserver("123",readconfig.name,readconfig.pwd,readconfig.machineName,readconfig.rserverip)
            sleep(15)
            base = BasePage(self.driver)
            self.assertEqual(base.gettext(self.regstateStatus), u"注册成功")      
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register5.png'))
            raise Exception("false")
        finally:
            self.driver.switch_to.default_content() 


    def test_register6(self):
        ''' 成功注册rserver'''    
        try:
            logger.info("成功注册rserver")
            self.login()
            self.register_rserver(readconfig.rserverip,readconfig.name,readconfig.pwd,readconfig.machineName)
            sleep(20)
            base = BasePage(self.driver)
            self.assertEqual(base.gettext(self.regstateStatus), u"注册成功")      
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_register4.png'))
            raise Exception("false")



        
if __name__ == "__main__":
   unittest.main()
