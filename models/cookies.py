#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''
import os
import unittest
from models.myunit import MyTest
from pages.loginpage import *
from models import readconfig



class SetCookies(MyTest):

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver

    def get_cookies(self):
        global cookies
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        cookie_login =self.driver.get_cookies()
        cookies = cookie_login
    

    def add_cookies(self):
        for cookie in cookies:
            cookie_list = {
                        'domain': '192.168.13.120',
                        'name': cookie["name"],
                        'value': cookie["value"],
                        "expires": "",
                        'path': '/',
                        'httpOnly': False,
                        'HostOnly': False,
                        'Secure': False,
                    }
            # print("添加cookie： %s  ： %s" % (cookie["name"], cookie["value"]))
            self.driver.add_cookie(cookie_list)
  
        
if __name__ == "__main__":
   unittest.main()
