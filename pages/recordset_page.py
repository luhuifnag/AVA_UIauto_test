#coding:utf-8
'''
Created on 2019年05月05日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger


class RecordSet(BasePage):

    #录制参数标签按钮
    recordsetbtn = (By.PARTIAL_LINK_TEXT, "录制参数")
    # 主码流选择按钮
    mainbtn = (By.XPATH,"//*[@id='main_quality']/a[1]/label") 
    # 自定义码流质量勾选按钮
    customckb = (By.XPATH,"//*[@id='main_quality']/a[2]/label") 
    # 自定义码流质量按钮
    custombtn = (By.ID,"customQualityBtn")
    width = (By.ID, "width")
    height = (By.ID, "height")
    fps = (By.XPATH, "//*[@id='fps-button']/span[1]")
    fps_25 = (By.XPATH, "ui-id-12")
    fps_30 = (By.XPATH, "ui-id-13")  #这是不同机型而不同的
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
    sub_stream5 = (By.XPATH,"//*[@id='autoRec']/..")
    # 录制时自动启动直播
    au_living = (By.XPATH,"//*[@id='autoStartLive']/..") 
    # 启动全自动跟踪按钮
    au_racking = (By.XPATH,"//*[@id='autoStartAutoTrack']/..")   
    # 教师行为分析文件
    teacher_act = (By.XPATH, "//*[@id='makeTeaFile']/..")   
    # ftp上传按钮
    ftpbtn = (By.XPATH,"//*[@id='startUpload']/..")
    # 用户输入框
    ftpUser = (By.ID,"ftpUser")
    # 密码输出框
    ftpPsw = (By.ID,"ftpPsw")
    # 路径输入框
    ftpUrl = (By.ID,"ftpUrl")
    # IP输入框
    ftpIp = (By.ID,"ftpIp")
    # 端口输入框
    ftpPort = (By.ID,"ftpPort")
    #页面确认按钮
    sure = (By.XPATH,"/html/body/div[1]/div[3]/input")


    # 进入录制参数页面后判断设备类型
    def getinto_recordset(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.recordsetbtn,"录制参数") #进入到录制参数页面
        sleep(2)
        
    # 设置主码流质量
    def set_main_quality(self,num,quality="1080p"):
        self.click(self.mainbtn)
        self.click(self.main_stream)
        sleep(1)
        logger.info(u"选择主码流质量为%s" % quality) 
        main_quality = (By.XPATH,"//*[@id='main_quality_select-menu']/li[%d]" % num)  #%d取值1、2、3、4分别对应的码流质量为高清\720p\标清\流畅
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
        self.click(self.cbr)
        self.clear(self.gop)
        self.input_text(self.gop, "10")
        self.click(self.sure1)
        
    # 勾选启动子码流录制按钮
    def start_up_sub_stream(self):
        if self.getAttribute(self.sub_stream5, "class") == "checkbox g_checkbox g_checkbox-checked":
            logger.info(u"已勾选启动子码流录制按钮") 
        else:
            self.click(self.sub_stream5)
            logger.info(u"勾选启动子码流录制按钮")

    # 不启动子码流录制按钮
    def off_sub_stream(self):
        if self.getAttribute(self.sub_stream5, "class") == "checkbox g_checkbox g_checkbox-checked":
            self.click(self.sub_stream5) 
        else:
            pass

    # 设置子码流质量
    def set_sub_quality(self,num,quality="720p"):
        self.click(self.sub_stream)
        sleep(2)
        logger.info(u"选择子码流质量为%s" % quality)
        sub_quality=(By.XPATH,"//*[@id='multi_quality-menu']/li[%d]" % num) #%d取值1、2、3、分别对应的码流质量为\720p\标清\流畅
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

    # 不勾选全部多流录制按钮
    def uncheck_allmuti(self):
        mulstis = self.get_multi_num()
        logger.info("不勾选所有多流录制按钮")
        for i in range(mulstis):
            mulsti = (By.XPATH, "//*[@id='multi_streams_con']/div[%s]/label" % str(i+1))
            if self.getAttribute(mulsti,"class") =="checkbox g_checkbox g_checkbox-checked":
                self.click(mulsti)
            else:
                pass

    # 勾选其中一路多流录制
    def check_a_allmuti(self, i):
        multi_name = (By.XPATH, "//*[@id='multi_streams_con']/div[%s]/label" % str(i+1)) #i==1时表示第一个多流录制标签名
        names = self.gettext(multi_name)
        self.off_sub_stream()
        self.uncheck_allmuti()
        mulsti = (By.XPATH, "//*[@id='multi_streams_con']/div[%s]/label" % str(i+1))
        logger.info("勾选%s多流录制按钮" % names)
        self.click(mulsti)
        return names

    #启动全自动跟踪
    def strat_au_racking(self):
        if self.getAttribute(self.au_racking,"class") =="checkbox g_checkbox g_checkbox-checked":
            logger.info(u"已勾选启动自动跟踪") 
        else:
            self.click(self.au_racking)
            logger.info(u"勾选启动自动跟踪")

    #勾选录制时自动启动直播
    def strat_au_living(self):
        if self.getAttribute(self.au_living,"class") =="checkbox g_checkbox g_checkbox-checked":
            logger.info(u"勾选录制时自动启动直播") 
        else:
            self.click(self.au_living)
            logger.info(u"勾选录制时自动启动直播")

    #去勾选录制时自动启动直播
    def off_au_living(self):
        if self.getAttribute(self.au_living,"class") =="checkbox g_checkbox g_checkbox-checked":
            self.click(self.au_living)
            logger.info(u"不勾选录制时自动启动直播") 
        else:
            pass  

    # 勾选教师行为分析文件按钮
    def start_teacher_act(self):
        if self.getAttribute(self.teacher_act,"class") =="checkbox g_checkbox g_checkbox-checked":
            logger.info(u"已勾选教师行为分析文件按钮") 
        else:
            self.click(self.teacher_act)
            logger.info(u"勾选教师行为分析文件按钮") 

    # 启ftp上传
    def start_ftp(self):
        logger.info("勾选ftp上传按钮")
        if self.getAttribute(self.ftpbtn, "class") == "checkbox  g_checkbox g_checkbox-checked":
            pass
        else:
            self.click(self.ftpbtn)

    # 填写ftp信息
    def ftp_input(self, ftpUser="root", ftpPsw="gzava_a4s", ftpUrl="./", ftpIp="192.168.13.245", ftpPort="21"):
        self.start_ftp()
        self.clear(self.ftpUser)
        self.input_text(self.ftpUser, ftpUser)
        self.clear(self.ftpPsw)
        self.input_text(self.ftpPsw, ftpPsw)
        self.clear(self.ftpUrl)
        self.input_text(self.ftpUrl, ftpUrl)
        self.clear(self.ftpIp)
        self.input_text(self.ftpIp, ftpIp)
        self.clear(self.ftpPort)
        self.input_text(self.ftpPort, ftpPort)
      
   # 点击页面确认按钮后切换回iframe
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(1)
        self.driver.switch_to.default_content()
        


