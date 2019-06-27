#coding:utf-8
'''
Created on 2019年06月27日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait 
from models import readconfig

class PresetSubitles(BasePage):

    # 预设字幕标签按钮
    psubbtn = (By.PARTIAL_LINK_TEXT, "预设字幕")
    # 预设字幕输入框
    preosd1 = (By.ID, "preosd1")
    preosd2 = (By.ID, "preosd2")
    preosd3 = (By.ID, "preosd3")
    preosd4 = (By.ID, "preosd4")
    preosd5 = (By.ID, "preosd5")
    # 确定按钮
    ensure = (By.XPATH, "/html/body/div/div[2]/input")

    # 设置5个自定义的字幕
    def set_preosd(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.psubbtn, "预设字幕")
        sleep(2)
        self.clear(self. preosd1)
        self.input_text(self.preosd1, "第一条自定义的字幕")
        self.clear(self. preosd2)
        self.input_text(self.preosd2,"The first custom subtitle")
        self.clear(self. preosd3)
        self.input_text(self.preosd3, "笑一笑，你的人生会更美好")
        self.clear(self. preosd4)
        self.input_text(self.preosd4, "秋天的天空像一块覆盖大地的蓝宝石")
        self.clear(self. preosd5)
        self.input_text(self. preosd5, "今天又是美好的一天！！！")
        self.click(self.ensure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        self.driver.switch_to.default_content()

