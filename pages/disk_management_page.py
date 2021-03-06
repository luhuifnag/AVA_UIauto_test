#coding:utf-8
'''
Created on 2019年05月28日

@author: Aloe
'''

from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger

class DiskManagement(BasePage):

    #硬盘管理标签按钮
    diskbtn = (By.PARTIAL_LINK_TEXT, "硬盘管理")

    # 硬盘格式化按钮
    formatbtn = (By.XPATH, "//*[@id='hardwareContainer']/div[1]/img")

    # 文件修复
    repairbtn = (By.XPATH, "//*[@id='hardwareContainer']/div[2]/img")
    
    # 文件整理按钮
    arrangementbtn = (By.XPATH, "//*[@id='hardwareContainer']/div[3]/img")
    
    # 辅助软件上传
    uploadbtn = (By.XPATH, "//*[@id='hardwareContainer']/div[4]/input")
    # 上传成功的提示
    success = (By.XPATH, "/html/body/div[3]")


     # 硬盘格式化
    def disk_format(self):
        home = HomePage(self.driver)
        home.goto_links('基本设置',self.diskbtn)
        sleep(2)
        self.click(self.formatbtn)
        logger.info(u"点击硬盘格式化按钮")
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())
        self.get_alert_text()
        self.accept_alert()
        WebDriverWait(self.driver,50,0.5).until(ES.alert_is_present())
        alert_text = self.get_alert_text()
        self.accept_alert()
        return alert_text
        
    # 文件修复
    def file_repair(self):
        home = HomePage(self.driver)
        home.goto_links('基本设置',self.diskbtn)
        sleep(2)
        self.click(self.repairbtn)
        logger.info(u"点击文件修复按钮")     

    # 文件整理
    def file_arrangement(self):
        home = HomePage(self.driver)
        home.goto_links('基本设置',self.diskbtn)
        sleep(2)
        self.click(self.arrangementbtn)
        logger.info(u"点击文件整理按钮")
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())
        alert_text = self.get_alert_text() 
        self.accept_alert()
        return alert_text
  
    # 辅助软件上传
    def software_upload(self, path):
        home = HomePage(self.driver)
        home.goto_links('基本设置',self.diskbtn)
        sleep(2)
        self.input_text(self.uploadbtn, path)
        logger.info(u"点击辅助软件上传按钮")
        sleep(1)

      