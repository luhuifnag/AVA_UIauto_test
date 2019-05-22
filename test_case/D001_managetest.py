#coding:utf-8
'''
Created on 2019年04月25日

@author: Aloe
'''

import os
import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.managepage import Manage
from pages.loginpage import LoginPage
from pages.record_page import RecordPage



class ManageTest(MyTest,Manage):
    '''首页的相关测试'''
    
    
    def test1_check_user(self):
        '''测试登录用户的信息是否正确'''
        try:
            self.click(self.userbtn)
            self.assertEqual(self.gettext(self.user_name),"admin")
            self.assertEqual(self.gettext(self.user_type),"管理员")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'check_user.png'))
            raise Exception("false")
    
    
    def test2_logout(self):
        '''退出系统测试''' 
        try:
            self.logout()
            self.assertEqual(self.driver.title,"登录页面")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'logout.png'))
            raise Exception("false")
        finally:
            LoginPage(self.driver).login_sys(readconfig.username, readconfig.password)
            sleep(2)


    def test3_dormancy(self):
        '''休眠唤醒测试'''
        try:
            self.dormancy()
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_dormancy.png'))
            raise Exception("false")


    def test4_reboot(self):
        '''重启设备测试''' 
        try:
            self.reboot()
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_reboot.png'))
            raise Exception("false")


    def test5_interaction_constraints1(self):
        '''在录制过程中限制进入互动模块的测试'''
        try:
            self.interaction_constraints1()
            self.assertFalse(self.is_enabled(self.interactionbtn))
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_interaction_constraint1.png'))
            raise Exception("false")
        finally:
            self.click(self.recordbtn)
            sleep(1)
            recordpage = RecordPage(self.driver)
            recordpage.stop_recording()
 

    def test6_interaction_constraints2(self):
        '''在直播过程中限制进入互动模块的测试'''
        try:
            self.interaction_constraints2()
            self.assertFalse(self.is_enabled(self.interactionbtn))
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_interaction_constraint2.png'))
            raise Exception("false")
        finally:
            self.click(self.recordbtn)
            sleep(1)
            recordpage = RecordPage(self.driver)
            recordpage.start_or_stop_live()




if __name__ == "__main__":
   unittest.main()

    
    













    



    

