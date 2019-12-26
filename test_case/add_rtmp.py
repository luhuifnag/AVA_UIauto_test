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
from pages.loginpage import LoginPage
from selenium.webdriver.common.by import By

class AddRtmp(MyTest, Living):

    empowerbtn = (By.PARTIAL_LINK_TEXT,"授权信息")
    machineNum = (By.ID,"machineNum")
    back1 = (By.ID,"back")

    def login (self,i):
        self.driver.get("http://192.168.6.%s" % str(i))
        self.driver.implicitly_wait(20)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)

    def test_set_px9url(self):
        for i in range(15,31):
            self.login(i)
            try:
                self.click(self.back1)
                sleep(2)
            except:
                pass
            finally:
                print(i)
                self.getin_live()
                sleep(1)
                self.off_px9push()
                sleep(1)
                # self.input_px9url("rtmp://192.168.13.128:1936")
                # sleep(1)
                self.on_px9push()
                sleep(1)

    # def test_get_machine_num(self):
    #     machine_num = []
    #     ip = []
    #     for i in range(10,41):
    #         self.login(i)
    #         try:
    #             self.click(self.back1)
    #             sleep(1)
    #         except:
    #             pass
    #         finally:
    #             home = HomePage(self.driver)
    #             home.swich_to_basic_label(self.empowerbtn,"授权信息")
    #             num = self.getInnerHTML(self.machineNum)
    #             ip.append(i)
    #             machine_num.append(num)
    #             ip_num = dict(zip(ip,machine_num))
    #             print(ip_num)



if __name__ == "__main__":
   unittest.main()


