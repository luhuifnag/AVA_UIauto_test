#coding:utf-8
'''
Created on 2019年05月08日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from models import readconfig

class Restore(BasePage):

    #恢复默认标签按钮
    restorebtn = (By.XPATH,"//*[@id='sec_navs']/li[11]/a")

    #确认按钮
    sure = (By.ID,"recoveryDefault")

    #恢复默认操作步骤
    def restore(self):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.restorebtn,"恢复默认")
        self.click(self.sure)
        print(u"恢复默认")
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())
        self.accept_alert()
        sleep(120)
        # 打开默认url后登录
        self.driver.refresh()
        login = LoginPage(self.driver)
        login.login_sys(readconfig.username, readconfig.password)
        WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统"))
    
