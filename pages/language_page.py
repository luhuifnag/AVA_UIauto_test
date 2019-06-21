#coding:utf-8
'''
Created on 2019年05月24日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger


class Languages(BasePage):

    #Language标签按钮
    languagebtn = (By.PARTIAL_LINK_TEXT,"Language")

    # 中文按钮
    Chinese = (By.XPATH, "//*[@id='panel']/label[1]")
    # 英文按钮
    english = (By.XPATH, "//*[@id='panel']/label[2]")
    # 提示信息
    tips = (By.XPATH, "/html/body/div/div[1]/div[2]")  
    #确认按钮
    surebtn = (By.XPATH, "/html/body/div/div[2]/input") 

    # 选择中文
    def choose_Chinese(self):
        logger.info("选择中文")
        if self.getAttribute(self.Chinese, "style")=="background-image: url(\"/assets/images/common/radio_checked.png\");":
            pass
        else:
            self.click(self.Chinese)

    # 选择英文
    def choose_english(self):
        logger.info("选择英文")
        if self.getAttribute(self.english, "style")=="background-image: url(\"/assets/images/common/radio_checked.png\");":
            pass
        else:
            self.click(self.english)

    # 点击确认按钮
    def click_surebtn(self):
        self.click(self.surebtn)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()



    # 切换为中文
    def switch_Chinese(self):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.languagebtn,"Language")
        sleep(2)
        self.choose_Chinese()
        self.click_surebtn()

  # 切换为英文
    def switch_english(self):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.languagebtn,"Language")
        sleep(2)
        self.choose_english()
        self.click_surebtn()

        