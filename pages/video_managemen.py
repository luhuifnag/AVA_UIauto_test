#coding:utf-8
'''
Created on 2019年04月25日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

class VideoManagemen(BasePage):


    #主题信息
    themesinf = (By.ID,"title")

    #主讲信息
    spaekerinf = (By.ID,"author")

    # 分辨率信息
    resolving = (By.ID,"resolution")

    # 编码模式
    CodingMode = (By.ID,"videoCodingMode")

    #文件总数
    total_documents = (By.ID,"fnToltal")

    #文件前面的勾选框
    radio = (By.XPATH,"//*[@id='filesInfo']/tbody/tr[2]/td[1]/label/i")  #第一个文件的tr值为2，后面的以此类推

    #删除按钮
    delete = (By.ID,"delSelectFile")


    #进入录制管理页面
    def check_recorder_massage(self):
        home = HomePage(self.driver)
        home.click_video_managemen()
        sleep(2)
     


    #查看文件详细信息
    def file_detailed(self,num):
        self.check_recorder_massage()
        print(u"查看文件的详细信息")
        detailedbtn = (By.XPATH,"//*[@id='filesInfo']/tbody/tr[%d]/td[9]/a" % num) #第一个文件的%d值为2,后面的以此类推
        self.click(detailedbtn)

    #查看文件总数
    def check_total_documents(self):
        self.check_recorder_massage()
        print(self.gettext(self.total_documents))
        return self.gettext(self.total_documents)

    #删除文件
    def delete_documents(self):
        self.click(self.radio)
        self.click(self.delete) 
        print(u"删除掉默认排序的第一个文件")
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())     
        self.accept_alert()
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())     
        self.accept_alert()
        sleep(2)

        
        

    


    