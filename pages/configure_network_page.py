#coding:utf-8
'''
Created on 2019年05月09日

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
from utils.log import logger

class ConfigureNetwork(BasePage):

    #网络参数标签按钮
    networkbtn = (By.PARTIAL_LINK_TEXT, "网络参数")

    #自动获取IP单选框
    automatic_ip = (By.XPATH, "//*[@id='local_auto_manul']/div[1]/label")

    #手动获取IP单选框
    manual_ip = (By.XPATH, "//*[@id='local_auto_manul']/div[2]/label") 

    #网络地址
    netaddr1 = (By.ID, "ip_1") 
    netaddr2 = (By.ID, "ip_2")
    netaddr3 = (By.ID, "ip_3")
    netaddr4 = (By.ID, "ip_4")

    #子网掩码
    subnet1 = (By.ID, "mask_1")
    subnet2 = (By.ID, "mask_2")
    subnet3 = (By.ID, "mask_3")
    subnet4 = (By.ID, "mask_4")

    #网关
    gateway1 = (By.ID, "gateway_1")
    gateway2 = (By.ID, "gateway_2")
    gateway3 = (By.ID, "gateway_3")
    gateway4 = (By.ID, "gateway_4")

    #首选DNS
    dnsa1 = (By.ID, "dns_1")
    dnsa2 = (By.ID, "dns_2")
    dnsa3 = (By.ID, "dns_3")
    dnsa4 = (By.ID, "dns_4")

    #备选DNS
    dnsb1= (By.ID, "backup_dns_1")
    dnsb2= (By.ID, "backup_dns_2")
    dnsb3= (By.ID, "backup_dns_3")
    dnsb4= (By.ID, "backup_dns_4")

    #百兆/千兆网口自适应
    self_adaption = (By.XPATH, "//*[@id='netAdaption_line']/label")

    #确认按钮
    sure = (By.XPATH, "//*[@id='local_panel_ipv4']/div[2]/input") 



    #勾选自动动获取ip按钮
    def check_automatic_ip(self):
        if self.getAttribute(self.automatic_ip,"class")=="radio g_radio g_radio-checked": 
            pass
        else:
            self.click(self.automatic_ip)
            logger.info(u"勾选自动获取IP")       

    #勾选手动获取ip按钮
    def check_manual_ip(self):
        if self.getAttribute(self.manual_ip,"class")=="radio g_radio g_radio-checked":
            pass
        else:
            self.click(self.manual_ip)
            logger.info(u"勾选手动获取IP")

    #更改IP和对应网关
    def change_ip_gateway(self, addr1, addr2, addr3, addr4, way1, way2, way3, way4): 
        list1 = [self.netaddr1, self.netaddr2, self.netaddr3, self.netaddr4]
        list2 = [addr1, addr2, addr3, addr4]
        list3 = [self.gateway1, self.gateway2, self.gateway3, self.gateway4]
        list4 = [way1, way2, way3, way4]
        logger.info(u"更改设备IP为:%s, 更改设备网关为%s" % (".".join(list2), ".".join(list4)))   
        for a in list1:
            self.clear(a)
        for b, c in zip(list1, list2):
            self.input_text(b, c)
        for d in list3:
            self.clear(d)
        for e, f in zip(list3, list4):
            self.input_text(e, f)
        sleep(2)


    #修改首选DNS
    def change_dnsa1(self):
        list1 = [self.dnsa1, self.dnsa2, self.dnsa3, self.dnsa4]
        list2 = [118, 118, 118, 118]
        list2_str = [str(x) for x in list2]
        logger.info(u"修改首选DNS为:%s" % ".".join(list2_str))  
        for a in list1:
            self.clear(a)
        for b, c in zip(list1, list2):
            self.input_text(b, c)
        
    #修改备选DNS
    def change_dnsb1(self):
        list1 = [self.dnsb1, self.dnsb2, self.dnsb3, self.dnsb4]
        list2 = [6, 6, 6, 6]
        list2_str = [str(x) for x in list2]
        logger.info(u"修改备选DNS为:%s" % ".".join(list2_str))  
        for a in list1:
            self.clear(a)
        for b, c in zip(list1, list2):
            self.input_text(b, c) 
    
    #勾选百兆/千兆网口自适应
    def check_self_adaption(self):
        if self.getAttribute(self.self_adaption, "class")=="checkbox g_checkbox g_checkbox-checked":
            pass
        else:
            self.click(self.self_adaption)
            WebDriverWait(self.driver, 5, 0.5).until(ES.alert_is_present()) 
            self.accept_alert()
        logger.info(u"勾选百兆/千兆网口自适应")

    # 点击页面确认按钮后切换回iframe
    def ensure(self):
        self.click(self.sure)
        sleep(2)
        WebDriverWait(self.driver, 5, 0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        WebDriverWait(self.driver, 5, 0.5).until(ES.alert_is_present()) 
        self.accept_alert()


######################完整用例步骤######################

     #自动获取IP
    def select_automatic_ip(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.networkbtn, "网络参数")
        self.check_automatic_ip()
        self.ensure()
        sleep(2)

    #手动获取IP
    def select_manual_ip(self, addr1, addr2, addr3, addr4, way1, way2, way3, way4): 
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.networkbtn, "网络参数")
        self.check_manual_ip()
        self.change_ip_gateway(addr1, addr2, addr3, addr4, way1, way2, way3, way4)
        self.ensure()
        sleep(2)

    #勾选百兆/千兆网口自适应
    def select_self_adaption(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.networkbtn, "网络参数")
        self.check_self_adaption()
        sleep(2)

    #修改首选DNS
    def modifying_dnsa1(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.networkbtn, "网络参数")
        self.change_dnsa1()
        self.ensure()
        sleep(2)

    #修改备选DNS
    def modifying_dnsb1(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.networkbtn, "网络参数")
        self.change_dnsb1()
        self.ensure()
        sleep(2)
