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
from pages.Input_output_page import InputOutput


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

    
    #录制一段主码流为quality1，子码流为quality2的视频
    def record_main_and_sub(self,num1,num2,quality1,quality2,thems):
        home = HomePage(self.driver)
        self.set_main_quality(num1,quality1)
        self.start_up_sub_stream()
        self.set_sub_quality(num2,quality2)
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording(thems)
        sleep(10)
        self.stop_recording()

    # #录制一段自定义的主码流质量的视频
    def record_custom_quality(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.uncheck_allmuti()
        self.custom_quality()
        sleep(1) 
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording("自定义码流质量录制")
        sleep(10)
        self.stop_recording()

    # 录制所有的网络多流
    def record_all_netmulti(self, url):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.check_allmuti()
        self.ensure()
        self.driver.switch_to.default_content()
        home.click_system_setup_blck()
        sleep(1)
        inputoutput = InputOutput(self.driver)
        inputoutput.getin_outin()
        inputoutput.set_all_netmulti(url)
        self.driver.switch_to.default_content()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording("所有网络多流录制")
        sleep(10)
        self.stop_recording()

    
    # 录制一路本地多流
    def record_localmulti(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        tag_num = self.get_multi_num()
        for i in range(tag_num):
            logger.info("~~~~~~开始新的本地多流录制~~~~~~~")
            if i==0:
                pass
            else:
                home.swich_to_system_label(self.recordsetbtn,"录制参数") 
            theme = self.check_a_allmuti(i)
            self.ensure()
            self.driver.switch_to.default_content()
            home.click_system_setup_blck()
            sleep(1)
            inputoutput = InputOutput(self.driver)
            inputoutput.getin_outin()
            try:
                inputoutput.set_localmulti(i)  #有的输入是没有本地多流的
            except:
                continue
            self.driver.switch_to.default_content()
            home.click_system_setup_blck()
            sleep(1)
            home.click_record()
            self.start_recording("%s本地多流录制" % theme)
            sleep(10)
            self.stop_recording()
            self.back()
            sleep(1)

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
    
    #录制时自动启动直播
    def record_strat_living(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.strat_au_living()
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording()
        sleep(5)
        living_status = self.getAttribute(self.livebtn, "class")
        self.stop_recording()
        self.stop_live()
        return living_status

    # 录制一段带有教师行为分析文件的视频
    def record_teacher_act(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.off_sub_stream()
        self.start_teacher_act()
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording()
        sleep(1)
        self.click(self.manualbtn)
        num = self.get_preview_num()
        for i in range(1, num-1):
            self.select_windows_tags1(i)
            sleep(8)
        self.stop_recording()

    # 启动ftp上传录制
    def record_start_ftp(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        self.uncheck_allmuti()
        self.start_ftp()
        self.ftp_input()
        self.ensure()
        home.click_system_setup_blck()
        sleep(1)
        home.click_record()
        self.start_recording("ftp上传")
        sleep(10)
        self.stop_recording()
        

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
       

        
