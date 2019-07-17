#coding:utf-8
'''
Created on 2019年07月17日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger

class PowerMode(BasePage):

    #上电模式标签按钮
    powermodebtn = (By.PARTIAL_LINK_TEXT,"上电模式")

    # 确定按钮
    surebtn = (By.XPATH, "/html/body/div/div[2]/button")
    

    #选择上电模式
    def choose_powermode(self, mode, num=1): 
        logger.info("选择%s模式" % mode)
        mode = (By.XPATH, "//*[@id='mode%s']/.." % str(num)) #num=1、2、3分别表示关机、休眠、上电模式
        self.click(mode)
        self.click(self.surebtn)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()