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


class InteractionHmoe(BasePage):

    # 已选用户输入框
    callinput = (By.XPATH, "//*[@id='callinput']/div/input")   
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
    # 内置云勾选框
    Built_in_cloud = (By.XPATH, "//*[@id='sipModule']/div/div[2]/div[1]/div/div[5]/div/label")
    # 确认按钮
    login = (By.ID, "login")

    # 创建会议页面
    # 会议主题
    confName = (By.ID, "confName")
    # 会议密码勾选框
    box1= (By.XPATH, "//*[@id='beforeCall_panel']/div[1]/div[1]/div[2]/div[1]/label/i")
    #  会议密码输入框
    confpasswd= (By.ID, "confpasswd")
    # 授课模式
    Teaching = (By.XPATH, "//*[@id='beforeCall_panel']/div[1]/div[2]/div[1]/div/label/div")
    # 会议模式
    Meeting = (By.XPATH, "//*[@id='beforeCall_panel']/div[1]/div[2]/div[2]/div/label")
    # 双流勾选框
    Double_current  = (By.XPATH, "//*[@id='beforeCall_panel']/div[2]/label")
    # 创建会议
    createMeeting = (By.ID, "createMeeting")
    # 取消按钮
    createMeetingCancel = (By.ID, "createMeetingCancel")


 
    # 进入到互动页面
    def getin_interaction(self):
        home = HomePage(self.driver)
        home.click_interaction()
        print("进入到互动页面")
        sleep(2)

    # 进入到互动设置页面
    def getin_interactSet(self):
        self.click(self.interactSet)
        self.driver.switch_to.frame(self.getAttribute(self.frame, "id")) #此处iframe的id是可变的，需要用相对定位转化的方法来定位其id
        sleep(2)

    # 启动内置云
    def start_up_cloud(self):
        if self.getAttribute(self.Built_in_cloud, "class") == "g_checkbox g_checkbox-checked":
            print("已启用内置云")
        else:
            self.click(self.Built_in_cloud)
            print("启用内置云")

    # 不启动用内置云
    def no_start_cloud(self):
        if self.getAttribute(self.Built_in_cloud, "class") == "g_checkbox g_checkbox-checked":
            self.click(self.Built_in_cloud)
            print("不启用内置云")
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
            print (register_text)
        else:
            print("未注册rserver")

    # 输入听课设备
    def input_call(self, *calls):
        self.clear(self.callinput)
        self.input_text(self.callinput, *calls)

    # 输入会议主题和密码
    def input_confName_confpasswd(self,name='',pwd='123456'):
        self.input_text(self.confName, name)
        self.click(self.box1)
        self.input_text(self.confpasswd, pwd)



    # 创建一个没有主题和密码的授课模式的会议
    def create_teaching_meeting(self, *calls):
        self.getin_interaction()
        self.getin_interactSet()
        self.register_situation()
        self.no_start_cloud()
        self.register_login()
        self.input_call(*calls)
        self.click(self.callbtn)
        sleep(1)
        self.click(self.Teaching)
        print("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)
    
    # 创建一个自定义主题和密码的授课模式的会议
    def create_teaching_meeting2(self, name, pwd, *calls):
        self.getin_interaction()
        self.getin_interactSet()
        self.register_situation()
        self.no_start_cloud()
        self.register_login()
        self.input_call(*calls)
        self.input_confName_confpasswd(name, pwd)
        self.click(self.callbtn)
        sleep(1)
        self.click(self.Teaching)
        print("创建授课模式会议")
        self.click(self.createMeeting) 
        sleep(3)
        self.click(self.sure1)
    



    
