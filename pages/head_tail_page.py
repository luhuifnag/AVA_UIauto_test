#coding:utf-8
'''
Created on 2019年06月21日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
from utils.log import logger
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait 
from models import readconfig

class HeadTail(BasePage):
    
    # 片头片尾标签按钮
    headtaibtn = (By.PARTIAL_LINK_TEXT, "片头片尾")
    # 片头上传按钮
    title_up = (By.XPATH, "//*[@id='title_form']/label/input")
    # 片头下载按钮
    title_down = (By.ID, "titledownload")
    # 片尾上传按钮
    trailer_up = (By.XPATH, "//*[@id='trailer_form']/label/input")
    # 片尾下载按钮
    trailer_down = (By.ID, "trailerdown")
    # 检测信号上传按钮
    debugsignal_up = (By.XPATH, "//*[@id='debugSignal_form']/label/input")
    # 检测信号下载按钮
    debugsignal_down = (By.ID, "debugsignaldown")
    # 空闲信号上传按钮
    nosignal_up = (By.XPATH, "//*[@id='noSignal_form']/label/input")
    # 空闲信号下载按钮
    nosignal_down = (By.ID, "nosignaldown")
    # 网络未连接上传按钮
    noNetwork_up = (By.XPATH, "//*[@id='noNetwork_form']/label/input")
    # 网络未连接下载按钮
    noNetwork_down = (By.ID, "noNetworkdown")
    # 片头显示时间
    tltle_time = (By.ID, "tTime_input")
    # 片尾显示时间
    trailer_time = (By.ID, "cTime_input")
    # 片头片尾显示视频信息勾选框
    show = (By.XPATH,"//*[@id='ctcfgContainer']/div[1]/div[2]/div[10]/label")

    # 上传片头,片尾等图片
    def upload(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.headtaibtn, "片头片尾")
        sleep(3)
        uplist = [self.title_up, self.trailer_up, self.debugsignal_up, self.nosignal_up, self.noNetwork_up]
        dataslist = [readconfig.date_path+"\\startImage.jpg",
                    readconfig.date_path+"\\finishImage.jpg",
                    readconfig.date_path+"\\signalChecking.jpg",
                    readconfig.date_path+"\\idle1.jpg",
                    readconfig.date_path+"\\idle2.jpg"]
        asserts = []
        for ups,datas in zip(uplist,dataslist):
            self.input_text(ups,datas)
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            asserts.append(self.get_alert_text())
            self.accept_alert()
        return asserts
    
    # 设置片头片尾显示时间,并且勾选片头片尾显示信息
    def set_title_trailer_time(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.headtaibtn, "片头片尾")
        sleep(3)
        self.clear(self.tltle_time)
        self.input_text(self.tltle_time, "2")
        self.clear(self.trailer_time)
        self.input_text(self.trailer_time, "2")
        if self.getAttribute(self.show,"style") == "margin: 5px 0px 5px 50px; background-image: url(\"/assets/images/common/checkbox_checked.png\");":
            logger.info("已勾选显示视频信息")
        else:
            logger.info("勾选显示视频信息")
            self.click(self.show)
        self.driver.switch_to.default_content()

    
        
        

        
