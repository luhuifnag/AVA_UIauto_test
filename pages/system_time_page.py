#coding:utf-8
'''
Created on 2019年05月24日

@author: Aloe
'''

from time import sleep
import datetime
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class SystemTime(BasePage):

    # 系统时间标签按钮
    systemTimebtn = (By.XPATH,"//*[@id='sec_navs']/li[8]/a")
    # 自动同步网络时间按钮  
    automaticbtn = (By.XPATH,"/html/body/div/div/div[2]/div[1]/label") 
    # 当前日期、年、月、日
    year = (By.ID,"year")
    month = (By.ID,"month")
    day = (By.ID,"day")
    # 当前时间、时、分、秒
    hours = (By.ID,"hours")
    minute = (By.ID,"minute")
    second = (By.ID,"second")
    #确认按钮
    surebtn = (By.ID,"save")

    # 勾选自动同步网络时间
    def check_automaticbtn(self):
        print("勾选自动同步网络时间")
        if self.getAttribute(self.automaticbtn, "class")=="checkbox g_checkbox g_checkbox-checked":
            pass
        else:
            self.click(self.automaticbtn)
        sleep(10)

    # 不勾选自动同步网络时间
    def uncheck_automaticbtn(self):
        if self.getAttribute(self.automaticbtn, "class")=="checkbox g_checkbox":
            pass
        else:
            self.click(self.automaticbtn)
        sleep(5)

    # 点击确认按钮
    def click_surebtn(self):
        self.click(self.surebtn)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
        self.accept_alert()
 


    # 手动修改系统时间
    def manual_change_time(self):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.systemTimebtn,"系统时间")
        sleep(2)
        self.uncheck_automaticbtn()
        Select(self.find_element(self.year)).select_by_visible_text("1970")
        Select(self.find_element(self.month)).select_by_visible_text("10")
        Select(self.find_element(self.day)).select_by_visible_text("20")
        sleep(1)
        Select(self.find_element(self.hours)).select_by_visible_text("23")
        Select(self.find_element(self.minute)).select_by_visible_text("59")
        Select(self.find_element(self.second)).select_by_visible_text("0")
        self.click_surebtn()
        self.driver.refresh()
        sleep(3)
        self.driver.switch_to.frame("content")


    # 自动同步网络时间
    def automatic_change_time(self):
        home = HomePage(self.driver)
        home.swich_to_basic_label(self.systemTimebtn,"系统时间")
        sleep(2)
        self.check_automaticbtn()
        now_year = datetime.datetime.now().strftime('%Y')
        time = datetime.datetime.now().timetuple()
        now_month = str(time.tm_mon)
        now_day = str(time.tm_mday)   #这种方式可以去掉日期月份小于10的时候前面带的0
        now_hours = str(time.tm_hour)   
        datelist = [now_year, now_month,now_day,now_hours]
        print(datelist)
        self.driver.refresh()
        sleep(3)
        self.driver.switch_to.frame("content")
        return datelist
        





