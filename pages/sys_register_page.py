#coding:utf-8
'''
Created on 2019年06月11日

@author: Aloe
'''

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.log import logger

class Register(BasePage):

    # 注册服务标签
    Registerbtn = (By.PARTIAL_LINK_TEXT, "注册服务")