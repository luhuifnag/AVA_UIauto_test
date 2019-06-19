#coding:utf-8
'''
Created on 2019年06月11日

@author: Aloe
'''

from models.status import Status
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.log import logger

class Register(BasePage):

    # 注册服务标签
    def Registerbtn(self):
        status = Status()
        if status.try_get_status():
           Registerbtn = (By.XPATH, "//*[@id='sec_navs']/li[13]/a")
        else:
            Registerbtn = (By.XPATH, "//*[@id='sec_navs']/li[15]/a")
        return Registerbtn