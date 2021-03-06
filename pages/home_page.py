#coding:utf-8
'''
Created on 2019年04月25日

@author: Aloe
'''
from time import sleep
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utils.log import logger
from models import readconfig


class HomePage(BasePage):

    # 录像管理按钮
    video_management = (By.XPATH, "//*[@id='content']/div[2]/a[2]") 

    def click_record(self):
        logger.info (u"点击录播按钮")
        record = (By.XPATH,"//*[@id='content']/div[1]/a[1]")
        self.click(record)
        sleep(2)  

    def click_record_black(self):
        logger.info(u"点击录播页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)
        sleep(2) 
    
    def click_interaction(self):
        logger.info(u"点击互动按钮")
        interaction = (By.XPATH,"//*[@id='content']/div[1]/a[2]")
        self.click(interaction)
        sleep(2) 

    def click_interaction_black(self):
        logger.info(u"点击互动页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)
        sleep(2) 

    def click_video_managemen(self):
        logger.info (u"点击录像管理按钮")  
        self.click(self.video_management)

    def click_video_managemen_black(self):
        logger.info (u"点击录像管理页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)
        sleep(2) 

    def click_plug(self):
        logger.info(u"点击插件管理按钮")
        plug = (By.XPATH,"//*[@id='content']/div[2]/a[3]")
        self.click(plug)

    def click_plug_black(self):
        logger.info(u"点击插件管理页面返回按钮")
        backbtn = (By.XPATH,"//*[@id='back']")
        self.click(backbtn)
        sleep(2) 

    def click_system_setup(self):
        logger.info(u"点击系统设置按钮")
        system_setup  = (By.XPATH,"//*[@id='content']/div[2]/a[4]")
        self.click(system_setup)

    def click_system_setup_blck(self):
        logger.info(u"点击系统设置页面返回按钮")
        backbtn = (By.ID,"back")
        self.click(backbtn)
        sleep(2) 

    def click_application_settings(self):
        logger.info(u"点击应用设置")
        applicationbtn = (By.XPATH,"//*[@id='g_navs']/li[1]/a")
        self.click(applicationbtn)
    
    def click_basic_setting(self):
        logger.info(u"点击基本设置")
        basic = (By.XPATH,"//*[@id='g_navs']/li[3]/a")
        self.click(basic)

    def click_user_management(self):
        logger.info(u"点击用户管理")
        user_management = (By.XPATH,"//*[@id='g_navs']/li[5]/a") 
        self.click(user_management)

    def click_configure(self):
        logger.info(u"点击快速配置按钮")
        configure = (By.XPATH,"//*[@id='content']/div[2]/a[5]")
        self.click(configure) 

    def click_configure_black(self):
        logger.info(u"点击快速配置页面返回按钮")
        backbtn = (By.XPATH,"//*[@id='quickCfgContainer']/div[1]/div/a")
        self.click(backbtn)

    def click_user(self):
        logger.info( u"点击用户按钮")
        user = (By.XPATH,"//*[@id='user']")
        self.click(user)

    def click_user_black(self):
        logger.info( u"点击用户页面返回按钮")
        user = (By.XPATH,"//*[@id='user']")
        self.click(user)

    def goto_links(self, links_name,labelname=None):
        if links_name == '首页':
            self.driver.get('%s/index.html?' % readconfig.url)
            sleep(2)
        elif links_name == '录播':
            self.driver.get('%s/admin/playguide/playguide.html?' % readconfig.url)
            sleep(3)
        elif links_name == '互动':
            self.driver.get('%s/admin/interact/interact.html?' % readconfig.url)
            sleep(3)
        elif links_name == '录制管理':
            self.driver.get('%s/admin/file/filemanage.html?' % readconfig.url)
            sleep(3)
            self.driver.switch_to.frame("content")
        elif links_name == '插件管理':
            self.driver.get('%s/admin/system/soft.html?' % readconfig.url)
        elif links_name == '应用设置':
            self.driver.get('%s/admin/system/sysConfigure.html?' % readconfig.url)
            sleep(2)
            self.click(labelname)
            sleep(2)
            self.driver.switch_to.frame("content")
        elif links_name =='基本设置':
            self.driver.get('%s/admin/system/sysConfigure.html?' % readconfig.url)
            sleep(2)
            self.click_basic_setting()
            sleep(2)
            self.click(labelname)
            sleep(2)
            self.driver.switch_to.frame("content") 
        elif links_name == '快速配置':
            self.driver.get('%s/admin/systemQuick/quickConfigure.html?' % readconfig.url)
            sleep(2)
            self.click(labelname)
            sleep(3)
            self.driver.switch_to.frame("main") 
        else:
            logger.error('输入参数有误')
    
        

    #进入到应用设置的某个页面里面
    def swich_to_system_label(self,labelname,text):
        self.click_system_setup()
        self.goto_links('系统设置')
        sleep(2)
        self.click_application_settings()
        sleep(3)
        self.click(labelname)
        sleep(2)
        logger.info(u"点击%s标签" % text)
        self.driver.switch_to.frame("content")    


    #进入到基本设置的某个页面里面
    def swich_to_basic_label(self,labelname,text):
        self.click_system_setup()
        sleep(2)
        self.click_basic_setting()
        sleep(3)
        self.click(labelname)
        sleep(1)
        logger.info(u"点击%s标签" % text)
        self.driver.switch_to.frame("content")


    #进入到用户管理页面里面
    def swich_to_user_label(self,labelname,text):
        self.click_system_setup()
        sleep(2)
        self.click_user_management()
        logger.info(u"点击%s标签" % text)
        sleep(3)
        self.driver.switch_to.frame("content")

    #进入到快速配置设置的某个页面里面
    def swich_to_configure_label(self,labelname,text): 
        self.click_configure()
        sleep(2)
        self.click(labelname)
        logger.info(u"进入到快速配置的%s页面" % text)
        sleep(3)
        self.driver.switch_to.frame("main") 

    def aaa(self):
        print('1111')
   