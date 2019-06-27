#coding:utf-8
'''
Created on 2019年06月21日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from pages.basepage import BasePage
from utils.log import logger
from pages.home_page import HomePage

class InputOutput(BasePage):

    # 输入输出按钮
    InputOutputbtn = (By.PARTIAL_LINK_TEXT, "输入输出")
    # 网络多流按钮
    network = (By.XPATH, "//*[@id='multStream']/div/div/label[1]/i")
    # 本地多流按钮"
    local = (By.XPATH, "//*[@id='multStream']/div/div/label[2]/i)")
    # url输入框
    urlinput = (By.ID, "url")
    # 缓冲时间
    buffertime = (By.ID, "bufferTime")
    # POC供电按钮
    poc = (By.XPATH, "//*[@id='enableDiv']/div/label")  
    # POC供电状态
    poc_state = (By.XPATH, "//*[@id='connectState']/span")
    # 确认按钮
    sure = (By.XPATH, "//*[@id='inputdevicePanel']/div[3]/button")

    # 进入输入输出设置页面
    def getin_outin(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.InputOutputbtn, "输入输出")
        sleep(2)

    # 获取输入设备标签数量
    def input_tag_num(self):
        input_tags = self.driver.find_elements_by_xpath("//*[@id='menus']/li")
        preview_num = len(input_tags)
        return int(preview_num)

    # 勾选所有网络多流，并填写网络多流地址
    def set_all_netmulti(self, url):
        tag_num = self.input_tag_num()
        logger.info("勾选所有网络多流并填写好地址")
        for i in range(tag_num):
            input_tag = (By.XPATH, "//*[@id='menus']/li[%s]" % str(i+1))
            self.click(input_tag)
            self.click(self.network)
            self.clear(self.urlinput)
            self.input_text(self.urlinput, url)
            sleep(1)
            self.ensure()

    # 启动poc供电
    def enable_poc(self):
        logger.info("启动poc供电")
        if self.getAttribute(self.poc, "class") == "checkbox g_checkbox g_checkbox-checked":
            pass
        else:
            self.click(self.poc)
            
    # 不启动poc供电
    def not_poc(self):
        logger.info("不启动poc供电")
        if self.getAttribute(self.poc, "class") == "checkbox g_checkbox g_checkbox-checked":
            self.click(self.poc)
        else:
            pass

    # 点击确认按钮
    def ensure(self):
        self.click(self.sure)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
    
    # 更改poc供电状态
    def change_poc_state(self):
        self.not_poc()
        self.ensure()
        sleep(3)
        state1 = self.gettext(self.poc_state)
        self.enable_poc()
        self.ensure()
        sleep(30)
        state2 = self.gettext(self.poc_state)
        print(state1,state2)
        return(state1,state2)



    