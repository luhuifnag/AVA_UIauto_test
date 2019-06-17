#coding:utf-8
'''
Created on 2019年06月06日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from utils.log import logger

class VideoTag(BasePage):

    # 视频标签按钮
    videotagbtn = (By.XPATH, "//*[@id='sec_navs']/li[12]/a")
    # 默认标签
    default_label = (By.XPATH, "//*[@id='videoLabelModule']/div[1]/label[1]/i")
    # 自定义标签
    custom_label = (By.XPATH, "//*[@id='videoLabelModule']/div[1]/label[2]/i") 
    # 确认按钮
    sure = (By.ID, "videoLabelSave")
    # 获取窗口的个数
    def get_windows_num(self):
        previews = self.driver.find_elements_by_xpath("//*[@id='labelList']/li")
        preview_num = len(previews)
        return int(preview_num)

    # 选择默认标签
    def C_default(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.videotagbtn, "视频标签")
        sleep(2)
        self.click(self.default_label)
        logger.info("选择默认标签名")
        sleep(1)
        self.click(self.sure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()

    # 向自定义窗口输入
    def input_custom_label(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.videotagbtn, "视频标签")
        sleep(3)
        self.click(self.custom_label)
        logger.info("选择自定义标签名称")  
        sleep(1)
        num = self.get_windows_num()
        albellist = []
        for i in range(num):
            windowsid = (By.XPATH, "//*[@id='labelList']/li[%s]/input" % str(i+1))
            self.clear(windowsid)
            sleep(1)
            self.input_text(windowsid, "自定义abc00%s" % str(i+1))
            albellist.append("%s 自定义abc00%s" % (str(i+1), str(i+1)))
        sleep(1)
        self.click(self.sure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        logger.info(albellist)
        self.driver.switch_to.default_content()
        return albellist

    
