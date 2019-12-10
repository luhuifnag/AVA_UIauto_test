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
            self.installInfor(3,2,6,"广州奥威亚电子科技有限公司","科汇金谷2街15号","张先生","18902567940","123456@163.com")
            self.driver.switch_to.frame("content")
            self.assertEqual(self.getInnerHTML(self.province_result), "河北省")
            self.assertEqual(self.getInnerHTML(self.city_result), "张家口市")
            self.assertEqual(self.getInnerHTML(self.area_result), "康保县")
            self.assertEqual(self.getValuetext(self.addrLocation), "广州奥威亚电子科技有限公司")
            self.assertEqual(self.getValuetext(self.addrInstall), "科汇金谷2街15号")
            self.assertEqual(self.getValuetext(self.contacts), "张先生")
            self.assertEqual(self.getValuetext(self.telephone), "18902567940")
            self.assertEqual(self.getValuetext(self.mail), "123456@163.com")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_InstallInfor.png'))
            raise Exception("false")

    
            
if __name__ == "__main__":
   unittest.main()
