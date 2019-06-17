
#coding:utf-8
'''
Created on 2019年05月14日

@author: Aloe
'''

from time import sleep

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from pages.home_page import HomePage
from utils.log import logger

class ConVersion(BasePage):
    
    #版本信息标签按钮
    versionbtn = (By.XPATH,"//*[@id='quickCfgContainer']/div[2]/div/div[1]/ul/li[6]/a")
    
       

    # 获取版本信息
    def get_versions(self):
        home = HomePage(self.driver)
        home.swich_to_configure_label(self.versionbtn,"版本信息")
        sleep(2)
        tr_list = self.driver.find_elements_by_tag_name("tr")
        tr_len = len(tr_list)
        version_names_text = []
        version_nums_text = []
        for i in range(1,tr_len):
            version_names = (By.XPATH,"//*[@id='versionList']/tr[%d]/td[2]" % i)  #第一行的版本名的行的取值分别为1后面的以此类推
            version_nums = (By.XPATH,"//*[@id='versionList']/tr[%d]/td[3]" % i)  #第一行的版本名的行的取值分别为1后面的以此类推
            version_names_text.append(self.gettext(version_names))
            version_nums_text.append(self.gettext(version_nums))
        logger.info (version_names_text,version_nums_text)
        self.driver.switch_to.default_content()
        return(version_names_text,version_nums_text)  