#coding:utf-8
'''
Created on 2019年06月11日

@author: Aloe
'''

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class Register(BasePage):

    # 注册服务标签
    Registerbtn = (By.XPATH, "//*[@id='sec_navs']/li[13]/a")