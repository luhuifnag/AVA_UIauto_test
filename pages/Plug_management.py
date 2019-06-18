#coding:utf-8
'''
Created on 2019年06月18日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from utils.log import logger

class PlugManagement(BasePage):


    # 进入插件管理页面后点击下载按钮
    def click_download(self, num):
        home = HomePage(self.driver)
        home.click_plug()
        sleep(2)
        downloadbtn = (By.XPATH, "//*[@id='softdl']/div[1]/div[2]/table/tbody/tr[%d]/td[3]/div/a" % num)  # %d=1时表示第一个下载按钮
        logger.info("点击下载按钮")
        self.click(downloadbtn)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        sleep(8)