#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support.ui import Select
from utils.log import logger
from models.status import Status


class RecordSet(BasePage):

    #录制参数标签按钮
    def recordsetbtn(self):
        status = Status()
        if status.try_get_status():
           recordsetbtn = (By.XPATH, "//*[@id='sec_navs']/li[7]/a")
        else:
            recordsetbtn = (By.XPATH, "//*[@id='sec_navs']/li[8]/a")
        return recordsetbtn

    # 主码流选择按钮
    mainbtn = (By.XPATH,"//*[@id='main_quality']/a[1]/label/i")  

    # 自定义码流质量勾选按钮
    customckb = (By.XPATH,"//*[@id='main_quality']/a[2]/label/i")

    # 自定义码流质量按钮
    custombtn = (By.ID,"customQualityBtn")

    #主码流选择下拉框
    main_stream = (By.XPATH,"//*[@id='main_quality_select-button']/span[1]")
    #子码流质量选择下拉框
    sub_stream = (By.XPATH,"//*[@id='multi_quality-button']/span[1]") 
    # 启动子码流录制复选框
    sub_stream5 = (By.XPATH,"//*[@id='others_body']/div[2]/label/i")

    # 启动全自动跟踪按钮
    au_racking = (By.XPATH,"//*[@id='startOption']/div/label[2]/i")

    #页面确认按钮
    sure = (By.XPATH,"/html/body/div[1]/div[3]/input")



    # 设置主码流质量
    def set_main_quality(self,num,quality="1080p"):
        self.click(self.mainbtn)
        self.click(self.main_stream)
        sleep(2)
        logger.info(u"选择主码流质量为%s" % quality)  
        # self.click(self.main_stream)
        # sleep(2)
        js = "document.getElementById('main_quality_select').style.display='block';" #编写JS语句把更改display的属性
        self.driver.execute_script(js) #执行JS
        sleep(2) 
        main_streams = (By.ID,"main_quality_select")
        Select(self.find_element(main_streams)).select_by_value("%d" % num)  #%d取值0\1\2\3分别对应的码流质量为1080p\720p\标清\流畅       
        sleep(1)

        
    # 勾选启动子码流录制按钮
    def start_up_sub_stream(self):
        if self.is_selected(self.sub_stream5):
            logger.info(u"已勾选启动子码流录制按钮") 
        else:
            self.click(self.sub_stream5)
            logger.info(u"勾选启动子码流录制按钮")       


    # 设置子码流质量
    def set_sub_quality(self,num,quality="720p"):
        self.click(self.sub_stream)
        sleep(2)
        logger.info(u"选择子码流质量为%s" % quality)
        sub_streams = (By.ID,"multi_quality") 
        self.click(sub_streams)  
        Select(self.find_element(sub_streams)).select_by_value("%d" % num)  #%d取值1、2、3分别对应的码流质量为720p\标清\流畅        
        sleep(1)

    #启动全自动跟踪
    def strat_au_au_racking(self):
        if self.getAttribute(self.au_racking,"class") =="checkbox g_checkbox g_checkbox-checked":
            logger.info(u"已勾选启动自动跟踪") 
        else:
            self.click(self.au_racking)
            logger.info(u"勾选启动自动跟踪") 
   
        
   # 点击页面确认按钮后切换回iframe
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content()
        


