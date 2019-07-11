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
from selenium.webdriver.support.select import Select
from models import readconfig

class Living(BasePage):

    #录制参数标签按钮
    livebtn = (By.PARTIAL_LINK_TEXT, "直播参数")
    # 主码流质量下拉按钮
    main_dropbtn = (By.XPATH, "//*[@id='main_quality_select-button']/span[1]")
    # 主码流质量
    main = (By.XPATH, "//*[@id='main_quality_select-menu']/li[%d]")
    # 子码流质量下拉按钮
    main_dropbtn = (By.XPATH, "//*[@id='multi_quality-button']/span[1]")
    # 子码流质量
    main = (By.XPATH, "//*[@id='multi_quality-menu']/li[%d]")
    # 自动推流地址勾选框
    atuo = (By.XPATH, "//*[@id='aloneAutoPush_%s']/..")
    # 推流输入框
    live_input = (By.ID, "rtmpUrl_%s")
    # 推流类型
    live_type = (By.ID, "rtmpMode_0")
    # 推流状态
    live_state = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[3]/span[2]")
    # 确定按钮
    sure = (By.XPATH,"/html/body/div[1]/div[2]/button")


    # 进入到直播参数页面
    def getin_live(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.livebtn,"直播参数") 
        sleep(2)

    # 勾选直播自动推送
    def auto_push(self,num=0):   #num=0 时表示第一路
        atuo = (By.XPATH, "//*[@id='aloneAutoPush_%s']/.." % str(num))
        if self.getAttribute(atuo, "class") == "m_lr-5 inline-block g_checkbox g_checkbox-checked":
            logger.info("已勾选自动推流")
        else:
            self.click(atuo)
            logger.info("勾选自动推流")

    # 设置推流url
    def input_liveurl(self, liveurl, num=0):  #num=0 时表示第一路推流地址
        live_input = (By.ID, "rtmpUrl_%s" % str(num))
        self.clear(live_input)
        self.input_text(live_input, liveurl)

    # 选择推流类型
    def select_live_type(self, typ, num=0):  #num=0 时表示第一路
        s1 = Select(self.driver.find_element_by_id("rtmpMode_%s" % str(num)))
        s1.select_by_visible_text(typ)

    # 点击确定按钮
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(1)

    # 设置一路主码流和一路子码流的推流地址
    def set_living(self):
        self.getin_live()
        self.auto_push()
        liveurl = readconfig.liveurl+
        self.input_liveurl(readconfig.liveurl)
        self.select_live_type("主码流")



    
