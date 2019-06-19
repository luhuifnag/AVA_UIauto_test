#coding:utf-8
'''
Created on 2019年06月18日

@author: Aloe
'''
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from models.myunit import MyTest
from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.loginpage import LoginPage


class Status(MyTest, BasePage):

    # 云镜参数标签按钮
    Cmirrorbtn = (By.XPATH, "//*[@id='sec_navs']/li[6]/a")

    def test_try_get_status(self):
        try:
            home = HomePage(self.driver)
            home.swich_to_system_label(self.Cmirrorbtn, "云镜参数")
            sleep(2)
            self.driver.switch_to.default_content() 
            print(self.getAttribute(self.Cmirrorbtn,"text"))
            unittest.assertIn("云镜参数", (self.getAttribute(self.Cmirrorbtn, "text")))
            return False # 返回False时设备为云镜设备
        except:
            return True # 返回True时设备为云台设备

    

if __name__ == "__main__":
   unittest.main()
