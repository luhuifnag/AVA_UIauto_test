#coding:utf-8
'''
Created on 2019年05月15日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.record_page import RecordPage


class RecordOperation(RecordPage):

    #在直播过程中点击录播页面返回按钮
    def living_back(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)                
        self.start_or_stop_live()
        sleep(4)
        home.click_record_black()
        sleep(2)

    # 点击全自动按钮
    def select_auto(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1) 
        self.click_autobtn()

    # 点击半自动按钮
    def select_semiauto(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1) 
        self.click_semiautobtn()
    
    # 录制一段云台控制的视频
    def PTZ_control_record(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)
        self.select_windows_tags1()
        self.select_windows()
        self.start_recording("云台控制录制")
        self.PTZ_turning()
        self.PTZ_focusing() 
        self.PTZ_fast_focusing()
        self.stop_recording()

    # 录制一段切换布局的视频
    def switching_layout(self):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)
        self.start_recording("切换布局录制")
        print(u"切换预览的视窗")
        num = self.get_preview_num()
        for i in range(1, num-1):
            self.select_windows_tags1(i)
            sleep(8)
        for u in range(num-1, num+1):
            self.select_windows_tags1(u)
            sleep(8)
        self.click(self.blendmodebtn)
        for m in range(1,10):
            self.click_blendmode(m)
            sleep(8)
        self.stop_recording()

    # 上传logo
    def upload_logo(self,path):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)
        self.click(self.logobtn)
        print(u"上传logo")
        self.input_text(self.logofile,path)
        sleep(3)
        self.click(self.upload)
        sleep(1)

    # 录制一段调整字幕的视频
    def adjust_subtitles(self,):
        home = HomePage(self.driver)
        home.click_record() 
        sleep(1)
        self.start_recording("字幕调整")
        sleep(5)
        self.click(self.subtitlebtn)
        self.select_showbtn()  #显示字幕
        for i in range(3):   # 依次输出前3个默认字幕
            self.output_subtitles(11+i)
            sleep(5)       
        self.edit_subtitles(14)  # 编辑第四条字幕后输出
        self.output_subtitles(14)
        self.click(self.outputbtn)
        sleep(5)
        self.select_hidebtn()  #隐藏字幕
        sleep(10)
        self.select_showbtn()  #显示字幕
        sleep(3)  
        self.select_rollbtn() #滚动字幕
        sleep(5)
        self.select_staticbtn() #静止字幕
        for m in range(1,7):      # 依次改变字幕颜色
            self.change_font_color(m)
            self.click(self.outputbtn)
            sleep(5)
        for n in range(1,8):       #依次改变字幕背景颜色
            self.change_background_colorr(n)
            self.click(self.outputbtn)
            sleep(5)
        self.stop_recording()
        






