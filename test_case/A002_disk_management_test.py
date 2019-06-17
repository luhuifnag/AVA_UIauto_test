#coding:utf-8
'''
Created on 2019年05月28日

@author: Aloe
'''


import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.disk_management_page import DiskManagement
from utils.log import logger

class DiskManagementTest(MyTest, DiskManagement):
    '''硬盘管理测试'''
# -
#     def test_disk_repair(self):   尚未实现
#         '''修复文件'''
#         try:
#             self.disk_repair()
#         except Exception as msg:
#             logger.ERROR(u"异常原因：%s"%msg)
#             self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_disk_repair.png'))
#             raise Exception("false")
#         finally:
#             self.driver.switch_to.default_content() 


    def test2_file_arrangement(self):
        '''文件整理测试'''
        try:
            logger.info("文件整理测试")
            result = self.file_arrangement()
            self.assertEqual(result, "保存成功！")   
        except Exception as msg:
            logger.ERROR(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_file_arrangement.png'))
            raise Exception("false")

    def test3_software_upload(self):   
        '''辅助软件上传测试'''
        try:
            logger.info("辅助软件上传测试")
            self.software_upload(readconfig.software_upload_path+"\\Auxiliary_software.zip")
            self.find_element(self.success)
            print(self.getAttribute(self.success,"textContent")) #获取 layer.msg 弹窗的信息
            self.assertEqual(self.getAttribute(self.success,"textContent"),"上传成功！")
        except Exception as msg:
            logger.ERROR(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test3_software_upload.png'))
            raise Exception("false")

    def test4_disk_format(self):   
        '''硬盘格式化测试'''
        try:
            logger.info("硬盘格式化测试")
            result = self.disk_format()
            self.assertIn("硬盘格式化成功" ,result)  
        except Exception as msg:
            logger.ERROR(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_disk_format.png'))
            raise Exception("false")
    

   
    
        
if __name__ == "__main__":
   unittest.main()
