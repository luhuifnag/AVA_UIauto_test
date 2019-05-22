#coding:utf-8
'''
Created on 2019年05月10日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.home_page import HomePage



class ConfigureRegister(BasePage):

    #注册服务标签按钮
    registerbtn = (By.LINK_TEXT,"注册服务")

    #注册状态标签
    regstateStatus = (By.ID,"regstateStatus")

    #服务器地址输入框
    serverIP= (By.ID,"serverIP")

    #用户账号输入框
    userName = (By.ID,"userName")

    #备用服务器地址输入框
    backupip =(By.ID,"backupip")

    #用户密码
    pwd = (By.ID,"pwd")

    # 用户昵称
    machineName = (By.ID,"machineName")

    # 本地端口
    localport = (By.ID,"localport")

    #UDP端口
    udpport =(By.ID,"udpport")

    #注册按钮
    registerSave = (By.ID,"registerSave")


    def input_serverIP(self,text):
        print( u"输入服务器地址：",text)
        self.clear(self.serverIP)
        self.input_text(self.serverIP, text)
        
    def input_userName(self,text):
        print( u"输入账号：",text)
        self.clear(self.userName)
        self.input_text(self.userName, text)

    def input_backupip(self,text=""):
        print( u"输入备用服务器地址：",text)
        self.clear(self.backupip)
        self.input_text(self.backupip, text)

    def input_pwd(self,text="123456"):
        print (u"输入密码：",text)
        self.clear(self.pwd)
        self.input_text(self.pwd, text)

    def input_machineName(self,text):
        print (u"输入昵称：",text)
        self.clear(self.machineName)
        self.input_text(self.machineName, text)
    
    def input_localport(self,text="554"):
        print (u"输入本地端口：",text)
        self.clear(self.localport)
        self.input_text(self.localport, text)

    def input_udpport(self,text="32768"):
        print (u"输入udp端口：",text)
        self.clear(self.udpport)
        self.input_text(self.udpport, text)

     #错误提示   
    def error_hint(self):
        return self.driver.switch_to.alert.text



    #设置注册服务的各项信息
    def register_rserver(self,ip,name,passwd,name2,ip2=""):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.registerbtn,"注册服务")
        self.input_serverIP(ip)
        self.input_userName(name)
        self.input_backupip(ip2)
        self.input_pwd(passwd)
        self.input_machineName(name2)
        self.input_localport()
        self.input_udpport()
        self.click(self.registerSave)
        sleep(20)
