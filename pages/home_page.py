#coding:utf-8
'''
Created on 2019年04月25日

@author: Aloe
'''
from time import sleep
from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class HomePage(BasePage):

    def click_record(self):
        print (u"点击录播按钮")
        record = (By.XPATH,"//*[@id='content']/div[1]/a[1]")
        self.click(record)

    def click_record_black(self):
        print(u"点击录播页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)
    
    def click_interaction(self):
        print(u"点击互动按钮")
        interaction = (By.XPATH,"//*[@id='content']/div[1]/a[2]")
        self.click(interaction)

    def click_interaction_black(self):
        print(u"点击互动页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)

    def click_video_managemen(self):
        print (u"点击录像管理按钮")
        video_management = (By.XPATH,"//*[@id='content']/div[2]/a[2]")  
        self.click(video_management)

    def click_video_managemen_black(self):
        print (u"点击录像管理页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)

    def click_plug(self):
        print(u"点击插件管理按钮")
        plug = (By.XPATH,"//*[@id='content']/div[2]/a[3]")
        self.click(plug)

    def click_plug_black(self):
        print(u"点击插件管理页面返回按钮")
        backbtn = (By.XPATH,"//*[@id='back']")
        self.click(backbtn)

    def click_system_setup(self):
        print(u"点击系统设置按钮")
        system_setup  = (By.XPATH,"//*[@id='content']/div[2]/a[4]")
        self.click(system_setup)

    def click_system_setup_blck(self):
        print(u"点击系统设置页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)

    def click_application_settings(self):
        print(u"点击应用设置")
        applicationbtn = (By.XPATH,"//*[@id='g_navs']/li[1]/a")
        self.click(applicationbtn)
    
    def click_basic_setting(self):
        print(u"点击基本设置")
        basic = (By.XPATH,"//*[@id='g_navs']/li[3]/a")
        self.click(basic)

    def click_user_management(self):
        print(u"点击用户管理")
        user_management = (By.XPATH,"//*[@id='g_navs']/li[5]/a")
        self.click(user_management)

    def click_configure(self):
        print(u"点击快速配置按钮")
        configure = (By.XPATH,"//*[@id='content']/div[2]/a[5]")
        self.click(configure) 

    def click_configure_black(self):
        print(u"点击快速配置页面返回按钮")
        backbtn = (By.XPATH,"//*[@id='quickCfgContainer']/div[1]/div/a")
        self.click(backbtn)

    def click_user(self):
        print( u"点击用户按钮")
        user = (By.XPATH,"//*[@id='user']")
        self.click(user)

    def click_user_black(self):
        print( u"点击用户页面返回按钮")
        user = (By.XPATH,"//*[@id='user']")
        self.click(user)


    
    #进入到应用设置的某个页面里面
    def swich_to_system_label(self,labelname,text):
        self.click_system_setup()
        sleep(2)
        self.click_application_settings()
        sleep(2)
        self.click(labelname)
        print(u"点击%s标签" % text)
        self.driver.switch_to.frame("content")    


    #进入到基本设置的某个页面里面
    def swich_to_basic_label(self,labelname,text):
        self.click_system_setup()
        sleep(2)
        self.click_basic_setting()
        sleep(2)
        self.click(labelname)
        print(u"点击%s标签" % text)
        self.driver.switch_to.frame("content")


    #进入到快速配置设置的某个页面里面
    def swich_to_configure_label(self,labelname,text): 
        self.click_configure()
        sleep(2)
        self.click(labelname)
        print(u"进入到快速配置的%s页面" % text)
        sleep(1)
        self.driver.switch_to.frame("main") 


   