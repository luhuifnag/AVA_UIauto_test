#coding:utf-8
'''
Created on 2019年04月28日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.home_page import HomePage
import datetime
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage
from models import readconfig

class Network(BasePage):

    #网络参数标签按钮
    networkbtn = (By.XPATH,"//*[@id='sec_navs']/li[2]/a")

    #网络地址
    netaddr1 = (By.ID,"ip_1")
    netaddr2 = (By.ID,"ip_2")
    netaddr3 = (By.ID,"ip_3")
    netaddr4 = (By.ID,"ip_4")

    #子网掩码
    subnet1 = (By.ID,"mask_1")
    subnet2 = (By.ID,"mask_2")
    subnet3 = (By.ID,"mask_3")
    subnet4 = (By.ID,"mask_4")

    #网关
    gateway1 = (By.ID,"gateway_1")
    gateway2 = (By.ID,"gateway_2")
    gateway3 = (By.ID,"gateway_3")
    gateway4 = (By.ID,"gateway_4")

    #首选DNS
    dnsa1 = (By.XPATH,"//*[@id='dns_1']")
    dnsa2 = (By.XPATH,"//*[@id='dns_2']")
    dnsa3 = (By.XPATH,"//*[@id='dns_3']")
    dnsa4 = (By.XPATH,"//*[@id='dns_4']")

    #备选DNS
    dnsb1= (By.ID,"backup_dns_1")
    dnsb2= (By.ID,"backup_dns_2")
    dnsb3= (By.ID,"backup_dns_3")
    dnsb4= (By.ID,"backup_dns_4")

    #确认按钮
    sure = (By.XPATH,"//*[@id='local_panel']/div[2]/input")


    #更改IP和对应网关
    def change_ip(self,addr1,addr2,addr3,addr4,way1,way2,way3,way4): 
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.networkbtn,"网络参数")
        list1 = [self.netaddr1,self.netaddr2,self.netaddr3,self.netaddr4]
        list2 = [addr1,addr2,addr3,addr4]
        list3 = [self.gateway1,self.gateway2,self.gateway3,self.gateway4]
        list4 = [way1,way2,way3,way4]
        print(u"更改设备IP为:%s,更改设备网关为%s" % (".".join(list2),".".join(list4)))
        for a in list1:
            self.clear(a)
        for b,c in zip(list1,list2):
            self.input_text(b,c)
        for d in list3:
            self.clear(d)
        for e,f in zip(list3,list4):
            self.input_text(e,f)
        sleep(4)
        self.click(self.sure)
        sleep(2)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        self.driver.switch_to.default_content()
        sleep(8)


   





