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
import time

class Living(BasePage):

    #录制参数标签按钮
    livebtn = (By.PARTIAL_LINK_TEXT, "直播参数")
    # 主码流选择按钮
    mainbtn = (By.XPATH,"//*[@id='main_quality']/a[1]/label")
    # 主码流质量下拉按钮
    main_dropbtn = (By.XPATH, "//*[@id='main_quality_select-button']/span[1]")
    # 子码流质量下拉按钮
    sub_dropbtn = (By.XPATH, "//*[@id='multi_quality-button']/span[1]")
    # 集控推流勾选框
    px9push = (By.XPATH, "//*[@id='enablepx9push']/..")
    # 推流类型
    live_type = (By.ID, "rtmpMode_0")
    # 推流总数
    total = (By.XPATH,"//*[@id='rtmp_push_flow']/div[2]/div[1]")
    # 确定按钮
    sure = (By.XPATH,"/html/body/div[1]/div[2]/button")


    # 进入到直播参数页面
    def getin_live(self):
        home = HomePage(self.driver)
        home.swich_to_system_label(self.livebtn,"直播参数") 
        sleep(2)

    # 选择主码流质量
    def set_main_quality(self,num,quality="1080p"):
        self.click(self.mainbtn)
        self.click(self.main_dropbtn)
        sleep(1)
        logger.info(u"选择主码流质量为%s" % quality) 
        main_quality = (By.XPATH,"//*[@id='main_quality_select-menu']/li[%d]" % num)  #%d取值1、2、3、4分别对应的码流质量为高清\720p\标清\流畅
        self.move_to_element(main_quality)
        self.click(main_quality) 

    # 设置子码流质量
    def set_sub_quality(self,num,quality="720p"):
        self.click(self.sub_dropbtn)
        sleep(2)
        logger.info(u"选择子码流质量为%s" % quality)
        sub_quality=(By.XPATH,"//*[@id='multi_quality-menu']/li[%d]" % num) #%d取值1、2、3、分别对应的码流质量为\720p\标清\流畅
        self.move_to_element(sub_quality)
        self.click(sub_quality)

    # 推流总数
    def get_total(self):
        return (self.getInnerHTML(self.total))

    # 勾选直播自动推送
    def auto_push(self,num=0):   #num=0 时表示第一路
        atuo = (By.XPATH, "//*[@id='aloneAutoPush_%s']/.." % str(num))
        if self.getAttribute(atuo, "class") == "m_lr-5 inline-block g_checkbox g_checkbox-checked":
            logger.info("已勾选自动推流")
        else:
            self.click(atuo)
            logger.info("勾选自动推流")

    # 设置推流url
    def input_liveurl(self,num=0):  #num=0 时表示第一路推流地址
        self.open_lock()
        logger.info("设置推流地址")
        live_input = (By.ID, "rtmpUrl_%s" % str(num))
        self.clear(live_input)
        liveurl = readconfig.liveurl+str(int(round(time.time())))
        self.input_text(live_input, liveurl)

    # 推流地址的不可编辑状态
    def able_liveurl(self, num=0):  #num=0 时表示第一路推流地址
        live_input = (By.ID, "rtmpUrl_%s" % str(num))
        return (self.get_element_att(live_input))

    # 打开推流的锁
    def open_lock(self, num=3): #num=3 时表示第一路
        lock = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[%s]/i" % str(num))
        if self.getAttribute(lock, "class") == "ico-lockup m_lr-5 inline-block":
            logger.info("已开锁")
        else:
            logger.info("开锁")
            self.click(lock)

     # 关闭推流的锁
    def off_lock(self, num=3): #num=3 时表示第一路
        lock = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[%s]/i" % str(num))
        if self.getAttribute(lock, "class") == "ico-lockup m_lr-5 inline-block":
            logger.info("关锁")
            self.click(lock)
        else:
            logger.info("已关锁")
            
    # 选择推流类型
    def select_live_type(self, typ, num=0):  #num=0 时表示第一路
        logger.info("选择推流类型为%s" % typ)
        s1 = Select(self.driver.find_element_by_id("rtmpMode_%s" % str(num)))
        s1.select_by_visible_text(typ)
    
    # 点击连接按钮
    def connet(self, num =3):  #num=3 时表示第一路
        logger.info("点击连接按钮")
        connetbtn = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[%s]/button" % str(num))
        if self.gettext(connetbtn) == "连接":
            self.click(connetbtn)

    # 点击断开按钮
    def disconnet(self, num =3):  #num=3 时表示第一路
        logger.info("点击连接按钮")
        connetbtn = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[%s]/button" % str(num))
        if self.gettext(connetbtn) == "断开":
            self.click(connetbtn)

    # 查看推流状态
    def check_live_state(self, num =3): #num=3 时表示第一路
        live_state = (By.XPATH, "//*[@id='rtmp_push_flow']/div[2]/div[%s]/span[2]" % str(num))
        state = self.gettext(live_state)
        return state

    # 去勾选集控推流
    def off_px9push(self):
        if self.getAttribute(self.px9push, "class") == "m_r-5 g_checkbox g_checkbox-checked":
            logger.info("关闭集控推流")
            self.click(self.px9push)
        else:
            logger.info("已关闭集控推流")

    # 点击确定按钮
    def ensure(self):
        self.click(self.sure)
        sleep(1)
        self.accept_alert()
        sleep(2)
        self.driver.switch_to.default_content()

    # 设置一路主码流和一路子码流的推流地址，并开启直播自动推流，且关闭集控推流
    def set_living(self):
        self.getin_live()
        self.auto_push()
        self.input_liveurl()
        self.select_live_type("主码流")
        sleep(2)
        self.auto_push(1)
        self.input_liveurl(1)
        self.select_live_type("子码流", 1)
        sleep(1)
        self.off_px9push()
        self.ensure()

    

    
