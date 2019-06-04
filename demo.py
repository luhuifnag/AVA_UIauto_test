import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from pages.home_page import HomePage
from pages.loginpage import LoginPage



class MyTest(unittest.TestCase):
    
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Firefox()
    #     # cls.driver = webdriver.Chrome()
    #     cls.driver.get(readconfig.url)
    #     cls.driver.maximize_window()
    #     cls.driver.implicitly_wait(10)
    #     login = LoginPage(cls.driver)
    #     login.login_sys(readconfig.username, readconfig.password)
    #     sleep(2)
    #     WebDriverWait(cls.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 
    
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    def setUp(self):
        print(u"******************测试开始******************")
        self.driver = webdriver.Firefox()
        self.driver.get(readconfig.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统")) 

    def test01(self):
        print("测试OK")


if __name__ == "__main__":

    unittest.main()