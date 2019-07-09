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
    live_input = (By.ID, "rtmpUrl_0")
    # 推流类型
    live_type = (By.ID, "rtmpMode_0")
    # 推流状态
    live_state = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[3]/span[2]")

