#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''

import time
import unittest
from time import sleep

from selenium import webdriver

class MyTest(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        sleep(4)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(20)
  
        
   
    def tearDown(self):
        self.driver.quit()

    def test1(self):
        print("测试成功")
            
        
if __name__ == "__main__":
   unittest.main()
