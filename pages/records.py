#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.record_page import RecordPage
from pages.recordset_page import RecordSet
from pages.video_managemen import VideoManagemen
from utils.log import logger


class Records(RecordPage,RecordSet):


    #基本录制
    def basic_recording(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)                
        self.start_recording("基本录制","陈老师")
        sleep(10)
        self.stop_recording()



    #暂停录制
    def pause_record(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)                
        self.start_recording("暂停录制测试")
        sleep(10)
        self.pause_recording() 
        sleep(1)



    #暂停后恢复录制测试
    def resume_recording(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)                
        self.start_recording("暂停后恢复录制测试")
        sleep(10)
        self.pause_recording() 
        sleep(1)
        

    #在录制过程中点击录播页面返回按钮
    def recording_back(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)                
        self.start_recording()
        sleep(2)
        home.click_record_black()
        sleep(2)



    #录制一段主码流为1080p的视频
    def record_main_1080p(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数")
        self.set_main_quality(1,"1080p")
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording("1080p主码流录制")
        sleep(10)
        self.stop_recording()


    
    #录制一段主码流为quality1，子码流为quality2的视频
    def record_main_and_sub(self,num1,num2,quality1,quality2,thems):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.set_main_quality(num1,quality1)
        self.start_up_sub_stream()
        self.set_sub_quality(num2,quality2)
        self.ensure()
        # home.click_system_setup_blck()
        # sleep(1)
        # home.click_record()
        # self.start_recording(thems)
        # sleep(10)
        # self.stop_recording()

       #录制时启用自动跟踪
    def record_strat_auacking(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.strat_au_racking()
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording()
        sleep(10)
        auto_status = self.getAttribute(self.autobtn, "class")
        self.stop_recording()
        return auto_status

    # 录制期间无法更改录制管理中的设置
    def modify_limit(self):
       self.recording_back()
       self.click(self.recording_back_conmit) 
       sleep(2)
       home = HomePage(self.driver)
       home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
       sleep(2)
       logger.info("点击保存按钮")
       self.click(self.sure)
       sleep(1)
       

        
