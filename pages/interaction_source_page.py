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
from pages.loginpage import LoginPage
from utils.log import logger


class TnteractionSource(BasePage):


    # 互动视频源标签按钮
    Sourcebtn = (By.PARTIAL_LINK_TEXT, "互动视频源")  
    # 确认按钮
    sure = (By.ID, "interaSave")

    # 获取视频源的个数
    def get_sources_num(self):
        sources = self.driver.find_elements_by_xpath("//*[@id='classList']/li")
        sources_num = len(sources)
        return int(sources_num)

     # 点击页面确认按钮后切换回iframe
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content()

    # 选择互动视频源
    def choose_source(self, num=1):
        source_name = (By.XPATH, "//*[@id='classList']/li[%d]/label"  % num) #num=1时表示第一个互动视频源
        names = self.gettext(source_name)
        logger.info("勾选%s互动视频源" % names)
        sourcestag = (By.XPATH, "//*[@id='classList']/li[%d]/label/i" % num)
        self.click(sourcestag)
        self.ensure()
        return names
        
