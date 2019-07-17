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
    # 返回按钮
    backbtn = (By.XPATH, "//*[@id='header']/div[2]")
    # 全场禁言按钮
    conferenceAllMute = (By.ID,"conferenceAllMute")
    # 添加用户按钮
    addInteractUser = (By.ID,"addInteractUser")
    # 退出会议按钮
    intera_stop = (By.ID, "intera_stop")
    # 退出会议的确定按钮
    sure2 = (By.PARTIAL_LINK_TEXT, "确定")
    # 添加用户输入框
    callinput = (By.XPATH, "//*[@id='callinput']/div/input")
    # 添加按钮
    addNew = (By.ID, "addNew")

    # 获取用户列表的数量
    def get_usernum(self):
        users = self.driver.find_elements_by_xpath("//*[@id='interactUserList']/li")
        usernum = len(users)
        return int(usernum)

    # 获取听课的昵称
    def get_username(self, num=1):
        names = (By.XPATH, "//*[@id='interactUserList']/li[%d]/div" % num)
        return self.getInnerHTML(names)

    # 判断听课用户是被成功添加
    def judge_Success_added(self, num=2):
        try:
           names = (By.XPATH, "//*[@id='interactUserList']/li[%d]/div/span" % num)
           self.find_element(names) 
           return True
        except:
            return False

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
        logger.info("结束互动会议")
        self.click(self.intera_stop)
        sleep(2)
        self.click(self.sure2)
        sleep(3)

    #添加听课
    def addlistener(self, listener):
        self.click(self.addInteractUser)
        sleep(2)
        self.driver.switch_to.frame("layui-layer-iframe1")
        logger.info("添加听课：%s"% listener)
        self.input_text(self.callinput, listener)
        sleep(1)
        self.click(self.addNew)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
        self.driver.switch_to.default_content()

    # 移除听课
    def remove_listener(self, num=2):
        logger.info("移除第%s个听课" % str(num-1))
        removebtn = (By.XPATH, "//*[@id='interactUserList']/li[%d]/div/i[2]" % num)
        self.click(removebtn)
        sleep(2)

    # 彻底删除听课
    def del_listener(self, num=2):
        logger.info("删除第%s个听课" % str(num-1))
        removebtn = (By.XPATH, "//*[@id='interactUserList']/li[%d]/div/i[2]" % num)
        self.click(removebtn)
        sleep(2)
        self.click(removebtn)
        sleep(2)