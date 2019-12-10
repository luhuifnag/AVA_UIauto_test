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
    InstallInfobtn = (By.PARTIAL_LINK_TEXT,"安装信息")
    #省下拉按钮
    province_select = (By.XPATH,"//*[@id='province_select-button']/span")
    # 省的选择结果
    province_result = (By.XPATH,"//*[@id='province_select-button']/span[2]")
    #市下拉按钮
    city_select = (By.XPATH,"//*[@id='city_select-button']/span")
    # 市的选择结果
    city_result = (By.XPATH,"//*[@id='city_select-button']/span[2]")
    #区下拉按钮
    area_select = (By.XPATH,"//*[@id='area_select-button']/span")
    # 区的选择结果
    area_result = (By.XPATH,"//*[@id='area_select-button']/span[2]")
    #所属单位
    addrLocation = (By.XPATH,"//*[@id='addrLocation']")
    #安装位置
    addrInstall = (By.XPATH,"//*[@id='addrInstall']")
    # 联系人
    contacts = (By.XPATH,"//*[@id='contacts']")
    # 联系电话
    telephone = (By.XPATH,"//*[@id='telephone']")
    # 联系邮箱
    mail = (By.XPATH,"//*[@id='mail']")
    #确认按钮
    machineAddInstallSave = (By.XPATH,"//*[@id='machineAddInstallSave']")


    def select_province(self,num):
        logger.info(u"选择省信息")
        self.click(self.province_select)
        sleep(2)
        provinces = (By.XPATH,"//*[@id='province_select-menu']/li[%d]" % num)
        self.move_to_element(provinces)
        self.click(provinces) 

    def select_city(self,num):
        logger.info(u"选择市信息")
        self.click(self.city_select)
        sleep(2)
        citys = (By.XPATH,"//*[@id='city_select-menu']/li[%d]" % num)
        self.move_to_element(citys)
        self.click(citys) 
    
    def select_area(self,num):
        logger.info(u"选择区信息")
        self.click(self.area_select)
        sleep(2)
        areas = (By.XPATH,"//*[@id='area_select-menu']/li[%d]" % num)
        self.move_to_element(areas)
        self.click(areas) 

    def input_addrLocation(self,info):
        logger.info(u"输入所属单位信息：%s" % info)
        self.input_text(self.addrLocation,info)

    def input_addrInstall(self,info):
        logger.info(u"输入安装位置信息：%s" % info)
        self.input_text(self.addrInstall,info)
    
    def input_contacts(self,info):
        logger.info(u"输入联系人：%s" % info)
        self.input_text(self.contacts,info)

    def input_telephone(self,info):
        logger.info(u"输入联系电话：%s" % info)
        self.input_text(self.telephone,info)

    def input_mail(self,info):
        logger.info(u"输入联系邮箱：%s" % info)
        self.input_text(self.mail,info)


    #安装信息填写
    def installInfor(self,province1,city1,area1,addrLocation1,addrInstall1,contact,phone,mail1):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.InstallInfobtn,"安装信息")
        self.select_province(province1)
        self.select_city(city1)
        self.select_area(area1)
        self.clear(self.addrLocation)
        self.input_addrLocation(addrLocation1)
        self.clear(self.addrInstall)
        self.input_addrInstall(addrInstall1)
        self.clear(self.contacts)
        self.input_contacts(contact)
        self.clear(self.telephone)
        self.input_telephone(phone)
        self.clear(self.mail)
        self.input_mail(mail1)
        self.click(self.machineAddInstallSave)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        sleep(2)
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content() 
        
        
    


   





















































































  























  

  
  
  
 

 
 

 
 

 
 








 







 






















 













  







