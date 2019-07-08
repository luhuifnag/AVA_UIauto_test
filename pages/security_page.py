#coding:utf-8
'''
Created on 2019年07月08日

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

class Security(BasePage):

    # 安全验证签按钮
    securitybtn = (By.PARTIAL_LINK_TEXT, "安全认证")
    # 启用安全验证勾选框
    radio = (By.XPATH, "/html/body/div/div/div[2]/div[1]/label")
    # 秘钥显示框
    safetyCheckCode = (By.ID, "safetyCheckCode")
    # 生成秘钥按钮
    generateKey = (By.ID, "generateKey")
    # 确定按钮
    ensure = (By.ID, "saveData")

    # 启用安全认证
    def start_security(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.securitybtn, "安全验证")
        if self.getAttribute(self.radio, "class") == "g_checkbox  g_checkbox-checked":
            logger.info("已启用安全验证")
        else:
            self.click(self.radio)
            logger.info("启用安全验证")
        self.click(self.generateKey)
        sleep(1)
        self.click(self.ensure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()

    # 不启用安全验证
    def off_security(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.securitybtn, "安全验证")
        if self.getAttribute(self.radio, "class") == "g_checkbox  g_checkbox-checked":
            self.click(self.radio)
            logger.info("不启用安全验证")
        else:
            logger.info("未启用安全验证")
        sleep(1)
        self.click(self.ensure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()