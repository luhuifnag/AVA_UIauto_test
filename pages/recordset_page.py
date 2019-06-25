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


class RecordSet(BasePage):

    #录制参数标签按钮
    recordsetbtn = (By.PARTIAL_LINK_TEXT, "录制参数")
    # 主码流选择按钮
    mainbtn = (By.XPATH,"//*[@id='main_quality']/a[1]/label/i")  

    # 自定义码流质量勾选按钮
    customckb = (By.XPATH,"//*[@id='main_quality']/a[2]/label/i") 
    # 自定义码流质量按钮
    custombtn = (By.ID,"customQualityBtn")
    width = (By.ID, "width")
    height = (By.ID, "height")
    fps = (By.XPATH, "//*[@id='fps-button']/span[1]")
    fps_25 = (By.XPATH, "ui-id-12")
    fps_30 = (By.XPATH, "ui-id-13")
    bps = (By.ID, "bps")
    vrb = (By.XPATH, "//*[@id='customQuality']/div/div[5]/div/label[1]/i")
    cbr = (By.XPATH, "//*[@id='customQuality']/div/div[5]/div/label[2]/i")
    gop = (By.ID, "gop")
    sure1 = (By.XPATH, "//*[@id='customQuality']/div/div[7]/button[1]")

    # 主码流编码方式下拉框
    main_code = (By.XPATH, "//*[@id='h265_enable_main-button']/span[1]")
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


    # 进入录制参数页面后判断设备类型
    def get_status(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        sleep(2)
        status = (By.ID, "ui-id-2")
        try:
            self.click(self.main_code)
            self.gettext(status) == "H.265"
            return "u8"
        except:
            return "非u8"
        
    # 设置主码流质量
    def set_main_quality(self,num,quality="1080p"):
        self.click(self.mainbtn)
        self.click(self.main_stream)
        sleep(1)
        logger.info(u"选择主码流质量为%s" % quality) 
        main_quality = (By.ID, "ui-id-%d" % num) #%d取值1、2、3、4分别对应的码流质量为高清\720p\标清\流畅;
                                                 #设备为u8时#%d取值3、4、5、6分别对应的码流质量为高清\720p\标清\流
        self.move_to_element(main_quality)
        self.click(main_quality)     

    # 设置自定义码流质量
    def custom_quality(self):
        logger.info("设置自定义码流质量")
        self.click(self.customckb)
        self.click(self.custombtn)
        sleep(1)
        self.clear(self.width)
        self.input_text(self.width, "400")
        self.clear(self.height)
        self.input_text(self.height, "200")
        self.click(self.fps)
        sleep(1)
        self.move_to_element(self.fps_25)
        self.click(self.fps_25)
        self.click(self.cbr)
        self.clear(self.gop)
        self.input_text(self.gop, "10")
        self.click(self.sure1)
        
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
        sub_quality= (By.ID, "ui-id-%d" % num)  #%d取值、6、7分别对应的码流质量为720p\标清\流畅;
                                                #设备为u8时#%d取值9、10、11分别对应的码流质量为\720p\标清\流
        self.move_to_element(sub_quality)
        self.click(sub_quality)
     
     # 获取多流录制的路数
    def get_multi_num(self):
        multi = self.driver.find_elements(By.XPATH, "//*[@id='multi_streams_con']/div")
        return int(len(multi)-7)

    # 勾选全部多流录制按钮
    def check_allmuti(self):
        mulstis = self.get_multi_num()
        logger.info("勾选所有多流录制按钮")
        for i in range(mulstis):
            mulsti = (By.XPATH, "//*[@id='multi_streams_con']/div[%s]/label" % str(i+1))
            if self.getAttribute(mulsti,"class") =="checkbox g_checkbox g_checkbox-checked":
                pass
            else:
                self.click(mulsti)

    #启动全自动跟踪
    def strat_au_racking(self):
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
        


