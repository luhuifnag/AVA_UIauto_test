#coding:utf-8
'''
Created on 2019年07月02日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from pages.basepage import BasePage
from utils.log import logger
from pages.home_page import HomePage


class UserMange(BasePage):

    # 用户管理按钮
    inforbtn = (By.PARTIAL_LINK_TEXT, "信息管理")
    # 添加用户按钮
    adduserbtn = (By.PARTIAL_LINK_TEXT, "添加用户")
    # 更改超级管理员密码按钮
    changepwd = (By.XPATH, "//*[@id='usersInfo_tbody']/tr[1]/td[9]/a")
    # 新密码输入框
    newpwd = (By.ID, "password")
    # 确认密码输出框
    repwd = (By.ID, "repassword")
    # 确认按钮
    surebtn = (By.XPATH,"//*[@id='updateUserpwModal']/div/div[2]/button[1]")

    # 更改管理员密码
    def change_admin_pwd(self,newp):
        home = HomePage(self.driver)
        home.swich_to_user_label(self.inforbtn,"用户管理")
        sleep(2)
        logger.info("修改管理密码")
        self.click(self.changepwd)
        sleep(1)
        self.input_text(self.newpwd,newp)
        self.input_text(self.repwd,newp)
        self.click(self.surebtn)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()



