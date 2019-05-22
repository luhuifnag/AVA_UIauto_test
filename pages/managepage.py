 #coding:utf-8
'''
Created on 2019年04月28日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.record_page import RecordPage


class Manage(BasePage):

    #关机按钮
    shutdownbtn = (By.XPATH, "//*[@id='shutdown']")
    # 确认按钮
    # sure = (By.XPATH, "/html/body/div[3]/div[3]/a[1]") 
    sure = (By.XPATH, "//*[@class='layui-layer-btn0']") 

    #用户按钮
    userbtn = (By.ID, "user")
    #用户名信息
    user_name = (By.XPATH, "//*[@id='userInfo']/div/div/div[2]/div[2]")
    #用户类型信息
    user_type = (By.XPATH, "//*[@id='userInfo']/div/div/div[3]/div[2]")
    #登录时间
    logtime = (By.XPATH, "//*[@id='userInfo']/div/div/div[4]/div[2]")

    # 录播按钮
    recordbtn = (By.XPATH,"//*[@id='content']/div[1]/a[1]")
    # 互动按钮
    interactionbtn = (By.XPATH,"//*[@id='content']/div[1]/a[2]")


    #退出系统
    def logout(self):
        print( u"点击退出系统按钮")
        logoutbtn= (By.ID, "logout")
        self.click(logoutbtn)
        sleep(1)       
        self.click(self.sure)
    

    #关机
    def shutdown(self):
        print(u"点击关机按钮")
        self.click(self.shutdownbtn)
        self.driver.switch.frame("layui-layer-iframe3")
        self.click(self.sure)

    #休眠
    def dormancy(self):
        print(u"点击休眠按钮")
        self.click(self.shutdownbtn)
        sleep(1)
        self.driver.switch_to.frame("layui-layer-iframe1")
        dormancybtn = (By.XPATH, "/html/body/div/div[2]/img")
        self.click(dormancybtn)
        sleep(2)  
        self.driver.switch_to.default_content()
        sleep(2)
        self.click(self.sure)
        sleep(120)
        LoginPage(self.driver).login_sys(readconfig.username, readconfig.password)
        sleep(2)
        print(u"点击唤醒按钮")
        awakenbtn = (By.XPATH, "//*[@id='awaken']/div/button[1]")
        self.click(awakenbtn)
        sleep(60)
        LoginPage(self.driver).login_sys(readconfig.username, readconfig.password)
        sleep(2)


    #重启
    def reboot(self):
        print(u"点击重启按钮")
        self.click(self.shutdownbtn)
        sleep(1)
        self.driver.switch_to.frame("layui-layer-iframe1")
        rebootbtn = (By.XPATH, "/html/body/div/div[3]/img")
        self.click(rebootbtn)
        self.driver.switch_to.default_content()
        sleep(1)
        self.click(self.sure)
        sleep(120)
        LoginPage(self.driver).login_sys(readconfig.username, readconfig.password)
        sleep(2)


    # 在录制过程中回到主页
    def interaction_constraints1(self):
        self.click(self.recordbtn)
        sleep(1)
        recordpage = RecordPage(self.driver)
        recordpage.start_recording()
        sleep(2)
        recordpage.back()
        sleep(2)
        self.click(recordpage.recording_back_conmit)
        sleep(1)


    # 在直播过程中回到主页
    def interaction_constraints2(self):
        self.click(self.recordbtn)
        sleep(1)
        recordpage = RecordPage(self.driver)
        recordpage.start_or_stop_live()
        recordpage.back()
        sleep(2)
        self.click(recordpage.recording_back_conmit)
        sleep(1)
   