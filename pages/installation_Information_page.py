#coding:utf-8
'''
Created on 2019年04月26日

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

class InstallInfor(BasePage):

    #安装信息标签
    InstallInfobtn = (By.XPATH,"//*[@id='sec_navs']/li[1]/a")
    #省
    province =(By.XPATH,"//*[@id='province']")
    #市
    city =(By.XPATH,"//*[@id='city']")
    #区
    area =(By.XPATH,"//*[@id='area']")
    #所属单位
    addrLocation =(By.XPATH,"//*[@id='addrLocation']")
    #安装位置
    addrInstall =(By.XPATH,"//*[@id='addrInstall']")
    #确认按钮
    machineAddInstallSave = (By.XPATH,"//*[@id='machineAddInstallSave']")


    def input_province(self,info):
        logger.info(u"输入省信息：%s" % info)
        self.input_text(self.province,info)

    def input_city(self,info):
        logger.info(u"输入市信息：%s" % info)
        self.input_text(self.city,info)
    
    def input_area(self,info):
        logger.info(u"输入区信息：%s" % info)
        self.input_text(self.area,info)

    def input_addrLocation(self,info):
        logger.info(u"输入所属单位信息：%s" % info)
        self.input_text(self.addrLocation,info)

    def input_addrInstall(self,info):
        logger.info(u"输入安装位置信息：%s" % info)
        self.input_text(self.addrInstall,info)
    



    #安装信息填写
    def installInfor(self,province1,city1,area1,addrLocation1,addrInstall1):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.InstallInfobtn,"安装信息")
        self.clear(self.province)
        self.input_province(province1)
        self.clear(self.city)
        self.input_city(city1)
        self.clear(self.area)
        self.input_area(area1)
        self.clear(self.addrLocation)
        self.input_addrLocation(addrLocation1)
        self.clear(self.addrInstall)
        self.input_addrInstall(addrInstall1)
        self.click(self.machineAddInstallSave)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content() 
        
        
    


   





















































































  























  

  
  
  
 

 
 

 
 

 
 








 







 






















 













  







