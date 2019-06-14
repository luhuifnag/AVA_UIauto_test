#coding:utf-8
'''
Created on 2019年04月28日

@author: Aloe
'''

import os
import unittest
from time import sleep


from models.myunit import MyTest
from pages.networkpage import Network
from models import readconfig
from pages.loginpage import LoginPage
from pages.configure_network_page import ConfigureNetwork
from pages.basepage import BasePage
from pages.home_page import HomePage

class ModifyingNetworkTest(MyTest):
    '''快速配置网路参数设置相关测试'''

    def test1_not_operable(self):
        '''当勾选自动获取IP试，网络参数等输入框不可编辑'''
        try:
            home = HomePage(self.driver)
            gnetwork = ConfigureNetwork(self.driver)
            home.swich_to_configure_label(gnetwork.networkbtn, "网络参数")
            sleep(3)
            gnetwork.check_automatic_ip()
            base = BasePage(self.driver)
            self.assertFalse(base.is_enabled(gnetwork.netaddr1))
            self.assertFalse(base.is_enabled(gnetwork.gateway1))
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_not_operable.png'))
            raise Exception("false")


    def test2_select_self_adaption(self):
        '''在快速配置中,勾选百兆/千兆网口自适应测试'''
        try: 
            gnetwork = ConfigureNetwork(self.driver)
            gnetwork.select_self_adaption()
            self.driver.refresh()
            sleep(3)             # 刷新页面后class值没那么么快可以更改过来，所以这里必须加等待，且刷新会切换出iframe
            self.driver.switch_to.frame("main")   
            base = BasePage(self.driver) 
            self.assertEqual(base.getAttribute(gnetwork.self_adaption,"class"),"checkbox g_checkbox g_checkbox-checked")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_select_self_adaption.png'))
            raise Exception("false")


    def test3_modifying_dnsa1(self):
        '''在快速配置中,修改首选dns测试'''  
        try:
            gnetwork = ConfigureNetwork(self.driver)
            gnetwork.modifying_dnsa1()
            base = BasePage(self.driver) 
            self.assertEqual(base.getValuetext(gnetwork.dnsa3),"118")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_modifying_dnsa1.png'))
            raise Exception("false")


    def test4_modifying_dnsa1(self):
        '''在快速配置中,修改备选dns测试'''
        try:
            gnetwork = ConfigureNetwork(self.driver)
            gnetwork.modifying_dnsb1()
            base = BasePage(self.driver)  
            self.assertEqual(base.getValuetext(gnetwork.dnsb3),"6")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_modifying_dnsa1.png'))
            raise Exception("false")


    def test5_select_manual_ip(self):
        '''在快速配置中更改IP测试'''  
        try:
            gnetwork = ConfigureNetwork(self.driver)
            gnetwork.select_manual_ip(readconfig.new_netaddr1,readconfig.new_netaddr2,readconfig.new_netaddr3,readconfig.new_netaddr4,\
            readconfig.new_gateway1,readconfig.new_gateway2,readconfig.new_gateway3,readconfig.new_gateway4)
            sleep(5)
            self.driver.refresh()
            sleep(3)
            new_url = self.driver.current_url
            login = LoginPage(self.driver)
            login.login_sys(readconfig.username, readconfig.password)
            sleep(2)
            self.assertEqual(new_url,"%slogin.html" % readconfig.newurl)
            self.assertEqual(self.driver.title, u"录播管理系统")
        except Exception as msg:
            print(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_select_manual_ip.png'))
            raise Exception("false")



  
if __name__ == "__main__":
   unittest.main()
