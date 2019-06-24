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
from utils.log import logger

class VideoManagemen(BasePage):


    #主题信息
    themesinf = (By.ID,"title")
    #主讲信息
    spaekerinf = (By.ID,"author")
    # 分辨率信息
    resolving = (By.ID,"resolution")
    # 编码模式
    CodingMode = (By.ID,"videoCodingMode")
    # 排序显示按钮
    sortbtn = (By.XPATH, "//*[@id='modes']/button[1]")
    # 分组显示按钮
    groupbtn = (By.XPATH, "//*[@id='modes']/button[2]")
    # 分组标签信息
    packet_label = (By.XPATH, "//*[@id='filesInfo']/tbody/tr[2]/td/strong")
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
        logger.info(u"查看文件的详细信息")
        detailedbtn = (By.XPATH,"//*[@id='filesInfo']/tbody/tr[%d]/td[9]/a" % num) #第一个文件的%d值为2,后面的以此类推
        self.click(detailedbtn)
    
    def file_detailed2(self,num):
        logger.info(u"查看文件的详细信息")
        detailedbtn = (By.XPATH,"//*[@id='filesInfo']/tbody/tr[%d]/td[9]/a" % num) #第一个文件的%d值为2,后面的以此类推
        self.click(detailedbtn)

    #查看文件总数
    def check_total_documents(self):
        self.check_recorder_massage()
        logger.info(self.gettext(self.total_documents))
        return self.gettext(self.total_documents)

    #删除文件
    def delete_documents(self):
        self.click(self.radio)
        self.click(self.delete) 
        logger.info(u"删除掉默认排序的第一个文件")
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())     
        self.accept_alert()
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())     
        self.accept_alert()
        sleep(2)

    # 文件排序
    def sortfile(self, num):
        self.check_recorder_massage()
        self.click(self.sortbtn)
        sortmode = (By.XPATH, "//*[@id='sort']/div[1]/label[%d]/i" % num) #%d的值分别为1、2、3、4,分别表示按主题、主讲、时间、时长排序
        self.click(sortmode)
    
    # 获取所有录制文件的主题信息(点击排序后这个这个函数对主题、主讲、时间、时长获取是一样的)
    def get_themes(self):
        files = self.driver.find_elements_by_xpath("//*[@id='filesInfo']/tbody/tr")
        filesnum = len(files)
        themeslist = []
        for i in range(2, filesnum+1):
            themes = (By.XPATH, "//*[@id='filesInfo']/tbody/tr[%d]/td[3]/div/font" % i)
            themeslist.append(self.gettext(themes))
        return themeslist
    
    # 分组显示
    def group_display(self, num):
        self.check_recorder_massage()
        self.click(self.groupbtn)
        sortmode = (By.XPATH, "//*[@id='sort']/div[1]/label[%d]/i" % num) #%d的值分别为1、2分别表示按主题、主讲分组
        self.click(sortmode)

    
 

        

    


    