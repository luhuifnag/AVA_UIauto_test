#coding:utf-8
'''
Created on 2019年05月20日

@author: Aloe
'''


    #######################添加临时环境变量路径###########################  
# import sys
# import os
#将models和pages的绝对路径写到系统环境变量中，实现跨目录的调用,这个方法是临时生效的，脚本运行后就会失效(如果已经将文件路径永久添加到PYTHONPATH中则不需要这个步骤)
# sys.path.append(os.path.abspath("F:\\AVAtest"))
# print(sys.path)

    #######################添加临时环境变量路径###########################  

import sys
import time
import unittest

import HTMLTestRunner
from models import readconfig
from test_case.A001_login_test import *
from test_case.A002_disk_management_test import *
from test_case.A003_configure_register_test import *
from test_case.B001_record_page_operation_test import *
from test_case.B002_record_test import *




if __name__ == '__main__':
    report_path = readconfig.report_path
    print(U"测试报告存放位置：%s" % report_path)
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    filename = report_path+'\\'+now+'result.html'
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='云互动UI自动化测试报告',description='环境：win10，firefox')
        # discover = unittest.defaultTestLoader.discover("test_case",pattern="*test.py",top_level_dir=None)
        # runner.run(discover)

        suite1 = unittest.makeSuite(LoginTest)
        suite2 = unittest.makeSuite(DiskManagementTest)
        suite3 = unittest.makeSuite(ConfigureRegisterTest)
        suite4 = unittest.makeSuite(RecordOperationTest)
        suite5 = unittest.makeSuite(Recorder)

        unittest.TextTestRunner().run(suite1)
        unittest.TextTestRunner().run(suite2)
        unittest.TextTestRunner().run(suite3)
        unittest.TextTestRunner().run(suite4)
        unittest.TextTestRunner().run(suite5)
        fp.close()
