#coding:utf-8
'''
Created on 2019年04月28日

@author: Aloe
'''

import os
import unittest
from time import sleep


from models.myunit import MyTest
from pages.installation_Information_page import InstallInfor
from models import readconfig
from utils.log import logger

class InstallInforTest(MyTest,InstallInfor):
    '''安装信息测试'''

    def test_InstallInfor(self):
        '''安装信息测试'''
        try:
            logger.info("安装信息测试")
            self.installInfor("guangdong","广州市","萝岗区科学城","广州奥威亚电子科技有限公司","科汇金谷2街15号")
            self.driver.switch_to.frame("content")
            self.assertEqual(self.getValuetext(self.province), "guangdong")
            self.assertEqual(self.getValuetext(self.city), "广州市")
            self.assertEqual(self.getValuetext(self.area), "萝岗区科学城")
            self.assertEqual(self.getValuetext(self.addrLocation), "广州奥威亚电子科技有限公司")
            self.assertEqual(self.getValuetext(self.addrInstall), "科汇金谷2街15号")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_InstallInfor.png'))
            raise Exception("false")

    
            
if __name__ == "__main__":
   unittest.main()
