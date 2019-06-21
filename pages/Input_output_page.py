#coding:utf-8
'''
Created on 2019年06月21日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models.status import Status
from pages.basepage import BasePage
from utils.log import logger
from pages.home_page import HomePage

class InputOutput(BasePage):

    # 输入输出按钮
    InputOutputbtn = (By.PARTIAL_LINK_TEXT, "输入输出")

    def click_it(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.InputOutputbtn, "输入输出")
        sleep(3)
      