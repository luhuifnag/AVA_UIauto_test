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

class InteractionHmoe(BasePage):

    # 已选用户输入框
    # callinput = (By.XPATH, "//*[@id='callinput']/div/input")   
    # 呼叫按钮
    callbtn = (By.ID, "callUsers")
    # 互动设置按钮
    interactSet = (By.ID, "interactSet")
    # 会议创建成功的确认按钮
    sure1 = (By.XPATH, "//*[@class='layui-layer layui-layer-dialog']/div[3]/a")

    # 互动设置页面
    #互动设置页面的定位
    frame = (By.XPATH,"//*[@class='layui-layer-content']/iframe")
    # 当前状态
    regstate = (By.ID, "regstate")  
    # 系统注册服务链接
    link = (By.XPATH, "//*[@id='sipModule']/div/div[1]/div/a")
    # 内置云勾选框
    Built_in_cloud = (By.XPATH, "//*[@id='sipModule']/div/div[2]/div[1]/div/div[5]/div/label") 
    # 确认按钮
    login = (By.ID, "login")

    # 创建会议页面
    # 会议主题
    confName = (By.ID, "confName")
    # 会议密码勾选框
    box1= (By.XPATH, "//*[@id='beforeCall_panel']/div[1]/div[1]/div[2]/div[1]/label/i")
    # 会议密码输入框
    confpasswd= (By.ID, "confpasswd")
    # 授课模式       
    Teaching = (By.XPATH, "//*[@id='AXM_mode']/..")   #由子节点定位父节点
    # 会议模式
    Meeting = (By.XPATH, "//*[@id='NORMAL_CLOUD']/..")
    # 双流勾选框
    Double_current  = (By.XPATH, "//*[@id='beforeCall_panel']/div[2]/label")
    # 创建会议
    createMeeting = (By.ID, "createMeeting")
    # 取消按钮
    createMeetingCancel = (By.ID, "createMeetingCancel")

    # 加入会议标签
    join_metbtn = (By.PARTIAL_LINK_TEXT, "加入会议")
    # 会议号输入框
    join_confNumber = (By.ID, "join_confNumber")
    # 密码输入框
    join_confPass = (By.ID, "join_confPass")
    # 加入会议下拉框
    join_type = (By.XPATH, "//*[@id='join_type-button']/span[1]") 
    # 确定按钮
    joinBtn = (By.ID, "joinBtn")
    # 加入会议失败的提示框文字
    alert_text = (By.XPATH, "//*[@id='layui-layer2']/div[2]") 
    # 加入会议失败的提示框确定按钮
    alert_sure = (By.XPATH, "//*[@id='layui-layer2']/div[3]/a") 

    # 进入到互动页面
    def getin_interaction(self):
        home = HomePage(self.driver)
        home.click_interaction()
        logger.info("进入到互动页面")
        sleep(2)

    #去掉最近呼叫的所有勾选
    def recent_call(self):
        recents = self.driver.find_elements_by_xpath("//*[@id='latestCall']/li")
        recent_num = len(recents)
        for i in range(recent_num):
            labels = (By.XPATH, "//*[@id='latestCall']/li[%s]/label" % str(i+1))
            if self.getAttribute(labels, "class") == "g_checkbox g_checkbox-checked":
                self.click(labels)
        
    # 进入到互动设置页面
    def getin_interactSet(self):
        self.click(self.interactSet)
        self.driver.switch_to.frame(self.getAttribute(self.frame, "id")) #此处iframe的id是可变的，需要用相对定位转化的方法来定位其id
        sleep(2)

    # 启动内置云
    def start_up_cloud(self):
        if self.getAttribute(self.Built_in_cloud, "class") == "g_checkbox g_checkbox-checked":
            logger.info("已启用内置云")
        else:
            self.click(self.Built_in_cloud)
            logger.info("启用内置云")

    # 不启动用内置云
    def no_start_cloud(self):
        if self.getAttribute(self.Built_in_cloud, "class") == "g_checkbox g_checkbox-checked":
            self.click(self.Built_in_cloud)
            logger.info("不启用内置云")
        else:
            pass

    # 点击互动设置页面的确定按钮
    def register_login(self):
        self.click(self.login)
        WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present())   #显示等待直到alert出现
        self.accept_alert()
        self.driver.switch_to.default_content()
        sleep(2) 

    # 判断注册情况
    def register_situation(self):
        register_text = self.gettext(self.regstate)
        if u"注册成功" in register_text:
            logger.info (register_text)
        else:
            logger.info("未注册rserver")

    # 输入听课设备
    def input_call(self, *calls):
        logger.info("输入已选用户%s" % (calls,) )
        blist = list(*calls)
        num = len(*calls)
        for i in range(1, num):
            callinput = (By.XPATH, "//*[@id='callinput']/div[%d]/input" % i) 
            self.input_text(callinput, blist[i-1])
            self.input_text(callinput, ";")
            sleep(2)

    # 输入会议主题和密码
    def input_confName_confpasswd(self,name='',pwd='123456'):
        self.input_text(self.confName, name)
        logger.info("主题：%s" % name)
        self.click(self.box1)
        self.input_text(self.confpasswd, pwd)
        logger.info("密码:%s" % pwd)

    # 启用双流
    def start_Double(self):
        if self.getAttribute(self.Double_current, "class") == "g_checkbox g_checkbox-checked":
            logger.info("已勾选双流")
        else:
            self.click(self.Double_current)
            logger.info("勾选双流")

    # 不启用双流
    def no_start_Doubl(self):
        if self.getAttribute(self.Double_current, "class") == "g_checkbox g_checkbox-checked":
            self.click(self.Double_current)
            logger.info("不勾选双流")
        else:
            pass

    # 创建会议
    def create_meeting(self, *calls):
        self.getin_interaction()
        self.getin_interactSet()
        self.register_situation()
        self.no_start_cloud()
        self.register_login()
        self.recent_call()
        self.input_call(*calls)
        self.click(self.callbtn)
        sleep(1)

    # 创建内置云会议
    def create_cloudmeeting(self, *calls):
        self.getin_interaction()
        self.getin_interactSet()
        self.register_situation()
        self.start_up_cloud()
        self.register_login()
        self.recent_call()
        self.input_call(*calls)
        self.click(self.callbtn)
        sleep(1)

    # 加入会议协议选择
    def selection_protocol(self, num=1):  #num=1、2、3分别表示ava、sip、h323协议
        self.click(self.join_type)
        sleep(1)
        logger.info("选择互动协议")
        type_option = (By.XPATH, "//*[@id='join_type-menu']/li[%d]" % num)  
        self.move_to_element(type_option)
        self.click(type_option)

############测试用例步骤#################
    # 创建一个没有主题和密码的授课模式的会议
    def create_teaching_meeting(self, *calls):
        self.create_meeting(*calls)
        self.click(self.Teaching)
        self.no_start_Doubl()
        logger.info("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)
    
    # 创建一个自定义主题和密码的授课模式的会议
    def create_teaching_meeting2(self, name, pwd, *calls):
        self.create_meeting(*calls)
        self.input_confName_confpasswd(name, pwd)
        self.click(self.Teaching)
        self.no_start_Doubl()
        logger.info("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个双流的授课模式的会议
    def create_Double_teaching_meeting(self, *calls):
        self.create_meeting(*calls)
        self.click(self.Teaching)
        self.start_Double()
        logger.info("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个没有主题和密码的会议模式的会议
    def create_meeting_meeting(self, *calls):
        self.create_meeting(*calls)
        self.click(self.Meeting)
        self.no_start_Doubl()
        logger.info("创建会议模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)
    
    # 创建一个自定义主题和密码的会议模式的会议
    def create_meeting_meeting2(self, name, pwd, *calls):
        self.create_meeting(*calls)
        self.input_confName_confpasswd(name, pwd)
        self.click(self.Meeting)
        self.no_start_Doubl()
        logger.info("创建授会议模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个双流的会议模式的会议
    def create_Double_meeting_meeting(self, *calls):
        self.create_meeting(*calls)
        self.click(self.Meeting)
        self.start_Double()
        logger.info("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个没有主题和密码的内置云会议
    def create_cloud_meeting(self, *calls):
        self.create_cloudmeeting(*calls)
        self.no_start_Doubl()
        logger.info("创建内置云会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个自定义主题和密码的内置云会议
    def create_cloud_meeting2(self, name, pwd, *calls):
        self.create_cloudmeeting(*calls)
        self.input_confName_confpasswd(name, pwd)
        self.no_start_Doubl()
        logger.info("创建内置云会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 创建一个双流的内置云会议
    def create_Double_cloud_meeting(self, *calls):
        self.create_cloudmeeting(*calls)
        self.start_Double()
        logger.info("创建内置云会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)

    # 互动设置转跳系统设置-注册服务
    def link_jump(self):
        self.getin_interaction()
        self.getin_interactSet()
        self.click(self.link)
        logger.info("转跳至系统设置-注册服务")
        sleep(2)

    # 加入会议
    def join_metting(self, connum, conppwd, num=1):
        self.getin_interaction()
        logger.info("点击加入会议")
        self.click(self.join_metbtn)
        logger.info("输入会议号：%s" % connum)
        self.input_text(self.join_confNumber, connum)
        logger.info("输入会议密码：%s" % conppwd)
        self.input_text(self.join_confPass, conppwd)
        self.selection_protocol(num)
        sleep(1)
        self.click(self.joinBtn)
        sleep(10)
