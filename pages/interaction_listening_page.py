#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger

class IterListening(BasePage):

    # 当前视频源
    lissource = (By.XPATH, "//*[@id='listenMainStream-button']/span[2]")

    