#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage

class RecordSet(BasePage):

    #录制参数标签按钮
    recordsetbtn = (By.XPATH,"//*[@id='sec_navs']/li[7]/a")  

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

    #页面确认按钮
    sure = (By.XPATH,"/html/body/div[1]/div[3]/input")





    # #进入到录制参数页面
    # def swich_to_recordset(self):
    #     home = HomePage(self.driver)
    #     home.click_system_setup()
    #     sleep(2)
    #     home.click_application_settings()
    #     sleep(2)
    #     self.click(self.recordsetbtn)
    #     print(u"点击录制参数标签")
    #     self.driver.switch_to.frame("content")


    # 设置主码流质量
    def set_main_quality(self,num,quality="1080p"):
        self.click(self.mainbtn)
        self.click(self.main_stream)
        sleep(2)
        print(u"选择主码流质量为%s" % quality)  
        main_streams = (By.ID,"ui-id-%d" % num) #%d取值1、2、3、4分别对应的码流质量为1080p\720p\标清\流畅  
        self.click(main_streams)       
        sleep(1)

        
    # 勾选启动子码流录制按钮
    def start_up_sub_stream(self):
        if self.is_selected(self.sub_stream5):
            pass
        else:
            self.click(self.sub_stream5)
            print(u"勾选启动子码流录制按钮")       


    # 设置子码流质量
    def set_sub_quality(self,num,quality="720p"):
        self.click(self.sub_stream)
        sleep(2)
        print(u"选择子码流质量为%s" % quality)
        sub_streams = (By.ID,"ui-id-%d" % num)  #%d取值5、6、7分别对应的码流质量为720p\标清\流畅
        self.click(sub_streams)          
        sleep(1)

        
   # 点击页面确认按钮后切换回iframe
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content()
        


