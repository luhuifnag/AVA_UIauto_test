#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''
import os
import unittest
from models.myunit import MyTest



class Cookies(MyTest,LoginPage):

    def test_get_cookies(self):
        Cookie = self.driver.get_cookies()
        print(Cookie)
        for cookie in self.driver.get_cookies():
            self.driver.add_cookie(cookie)
       
        
if __name__ == "__main__":
   unittest.main()
