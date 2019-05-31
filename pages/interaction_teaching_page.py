#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage

class IterTeaching(BasePage):

    # 会议模式
    metting_typle = (By.XPATH, "//*[@id='header']/div[3]/h2")
    # 会议主题
    metting_theam = (By.XPATH, "//*[@id='header']/div[3]/div[1]/span")
    # 会议号
    metting_no = (By.XPATH, "//*[@id='header']/div[3]/div[2]")
    # 会议密码
    metting_pwd = (By.XPATH, "//*[@id='header']/div[3]/div[3]")
    # 退出会议按钮
    intera_stop = (By.ID, "intera_stop")
    # 退出会议的确定按钮
    sure2 = (By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]")


    # 退出会议
    def stop_metting(self):
        self.click(self.intera_stop)
        sleep(2)
        self.click(self.sure2)
        sleep(3)