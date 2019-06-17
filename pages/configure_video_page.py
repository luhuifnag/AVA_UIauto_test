#coding:utf-8
'''
Created on 2019年05月14日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from utils.log import logger

class VideoQuery(BasePage):
    
    #录像查询标签按钮
    videobtn = (By.XPATH,"//*[@id='quickCfgContainer']/div[2]/div/div[1]/ul/li[4]/a")

    #文件总数
    total_documents = (By.ID,"fnToltal")



    # 查看文件总数
    def check_total_documents(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.videobtn,"录像查询")
        sleep(1)
        logger.info(self.gettext(self.total_documents))
        a = self.gettext(self.total_documents)
        self.driver.switch_to.default_content()
        return a
        
        