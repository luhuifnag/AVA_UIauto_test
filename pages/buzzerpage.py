#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger


class Buzzer(BasePage):

    #蜂鸣器
    buzzerbtn = (By.PARTIAL_LINK_TEXT,"蜂鸣器")

    #确认按钮
    surebtn = (By.ID,"closeBuzzer") 

    #是否关闭蜂鸣器的文本
    text = (By.XPATH,"//*[@id='cfgModule']/div[2]") 

    
    #关闭蜂鸣器
    def close_buzzer(self):
        '''关闭蜂鸣器测试'''
        home = HomePage(self.driver)
        home.click_system_setup()
        sleep(2)
        home.click_basic_setting()
        sleep(2)
        logger.info("点击关闭蜂蜜器")
        home.click(self.buzzerbtn)
        sleep(1)
        self.driver.switch_to.frame("content")
        self.click(self.surebtn)
        sleep(1)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content()
