#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from time import sleep
from utils.log import logger

class LoginPage(BasePage):
    '''
    用户登录页面
    '''
    #元素集
    #用户名
    username = (By.ID,"uname")
    #密码
    passwd = (By.ID,"upswd")
    
    #登录 按钮
    loginbtn = (By.ID,"lgBtn")
    #记住密码
    remember_passwd = (By.XPATH,"//*[@id='lg']/div[2]/div[4]/label/i")

    
    def input_username(self,text):
        logger.info( u"输入用户名：%s" % text)
        self.input_text(self.username, text)
        
    def input_passwd(self,text):
        logger.info (u"输入密码：%s" % text)
        self.input_text(self.passwd, text)
        
    def click_loginbtn(self):
        logger.info( u"点击 登录  按钮")
        self.click(self.loginbtn)
             
    def click_rememberpasswd(self):
        logger.info( u"勾选 记住密码")
        self.click(self.remember_passwd)
    
    #用户名或密码错误提示   
    def error_hint(self):
        return self.driver.switch_to.alert.text
 
        
    #普通登录    
    def login_sys(self,username,passwd):
        '''获取用户名和密码登录'''
        self.clear(self.username)
        self.input_username(username)
        self.clear(self.passwd)
        self.input_passwd(passwd)
        self.click_loginbtn()
        sleep(2)
          
     #记住密码登录 
    def rememberlogin_sys(self,username,passwd):
        self.clear(self.username)
        self.input_username(username)
        self.clear(self.passwd)
        self.input_passwd(passwd)
        self.click_rememberpasswd()
        self.click_loginbtn()

        