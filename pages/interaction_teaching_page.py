#coding:utf-8
'''
Created on 2019年05月30日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger

class IterTeaching(BasePage):

    # 会议模式
    meeting_typle = (By.XPATH, "//*[@id='header']/div[3]/h2")
    # 会议主题
    meeting_theam = (By.XPATH, "//*[@id='header']/div[3]/div[1]/span")
    # 会议号
    meeting_no = (By.XPATH, "//*[@id='header']/div[3]/div[2]")
    # 会议密码
    meeting_pwd = (By.XPATH, "//*[@id='header']/div[3]/div[3]")
    # 双流标志
    doubletag = (By.XPATH, "//*[@id='baseController']/div[1]/div[1]/label")
    # 退出会议按钮
    intera_stop = (By.ID, "intera_stop")
    # 退出会议的确定按钮
    sure2 = (By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]")


    # 获取预览视窗的个数
    def get_preview_num(self):
        previews = self.driver.find_elements_by_xpath("//*[@id='videoLists']/li")
        preview_num = len(previews)
        return int(preview_num)

     # 获取预览视窗的名称
    def get_preview_tag(self):
        num = self.get_preview_num()
        taglist = []
        for i in range(num):
            tags = (By.XPATH, "//*[@id='videoLists']/li[%s]/div[1]/div" % str(i+1))
            taglist.append(self.gettext(tags))
        logger.info(taglist)
        return taglist
        
    # 退出会议
    def stop_meeting(self):
        self.click(self.intera_stop)
        sleep(2)
        self.click(self.sure2)
        sleep(3)