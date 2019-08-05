#coding:utf-8
'''
Created on 2019年05月20日

@author: Aloe
'''
import HTMLTestRunner
import os
import re
import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.basepage import BasePage
from pages.buzzerpage import Buzzer
from pages.configure_network_page import ConfigureNetwork
from pages.configure_register_page import ConfigureRegister
from pages.configure_version_page import ConVersion
from pages.configure_video_page import VideoQuery
from pages.disk_management_page import DiskManagement
from pages.head_tail_page import HeadTail
from pages.home_page import HomePage
from pages.Input_output_page import InputOutput
from pages.installation_Information_page import InstallInfor
from pages.interaction_home_page import InteractionHmoe
from pages.interaction_listening_page import IterListening
from pages.interaction_source_page import TnteractionSource
from pages.interaction_teaching_page import IterTeaching
from pages.language_page import Languages
from pages.Living_page import Living
from pages.loginpage import LoginPage
from pages.managepage import Manage
from pages.networkpage import Network
from pages.Plug_management import PlugManagement
from pages.power_mode_page import PowerMode
from pages.preset_subtitles_page import PresetSubitles
from pages.record_page import RecordPage
from pages.record_page_operation import RecordOperation
from pages.records import Records
from pages.recordset_page import RecordSet
from pages.restore_default_page import Restore
from pages.security_page import Security
from pages.sys_register_page import Register
from pages.system_time_page import SystemTime
from pages.user_manage_page import UserMange
from pages.version_information_page import Version
from pages.video_managemen import VideoManagemen
from pages.video_tag_page import VideoTag
from utils.log import logger


if __name__ == '__main__':
    report_path = readconfig.report_path
    print(U"测试报告存放位置：%s" % report_path)
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    filename = report_path+'\\'+now+'result.html'
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='云互动UI自动化测试报告',description='环境：win10，firefox')
        discover = unittest.defaultTestLoader.discover("test_case",pattern="*test.py",top_level_dir=None)
        runner.run(discover)
        fp.close()
