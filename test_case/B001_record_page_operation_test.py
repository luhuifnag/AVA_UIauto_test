#coding:utf-8
'''
Created on 2019年05月15日

@author: Aloe
'''
import os
import unittest
from time import sleep

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.record_page import RecordPage
from pages.record_page_operation import RecordOperation
from utils.log import logger

class RecordOperationTest(MyTest, RecordOperation):
    '''录播页面相关操作测试'''

    def test1_living_back(self):
        '''测试在直播过程中点击录播页面返回按钮，验证是否有提示信息'''   
        try:
            logger.info("测试在直播过程中点击录播页面返回按钮，验证是否有提示信息")
            self.living_back()
            tips = self.gettext(self.recording_back_tips)
            self.click(self.recording_back_cancel)
            self.assertEqual(tips, "正在录制或直播 ,确定返回模式选择？")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path, 'test_living_back.png'))
            raise Exception("false")
        finally:
            self.start_or_stop_live()

    def test2_select_auto(self):
        '''点击全自动按钮布局与变焦置灰的测试'''
        try:
            logger.info("点击全自动按钮布局与变焦置灰的测试")
            self.select_auto()
            self.assertFalse(self.is_enabled(self.blendmodebtn))
            self.assertFalse(self.is_enabled(self.ptzbtn))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'select_auto.png'))
            raise Exception("false")
        finally:
            sleep(1)
            self.click(self.manualbtn)

    def test3_select_semiauto(self):
        '''点击半自动按钮变焦置灰的测试''' 
        try:
            logger.info("点击半自动按钮变焦置灰的测试'")
            self.select_semiauto()
            self.assertFalse(self.is_enabled(self.ptzbtn))
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_select_semiauto.png'))
            raise Exception("false")
        finally:
            sleep(1)
            self.click(self.manualbtn)

    def test4_PTZ_control(self):
        '''录制一段控制云台的视频'''
        try:
            logger.info("录制一段控制云台的视频")
            self.PTZ_control_record()
            logger.info(u"录制成功")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_adjust_subtitles.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test5_switching_layout(self):
        '''录制一段切换布局的视频'''  
        try:
            logger.info("录制一段切换布局的视频")
            self.switching_layout()
            logger.info(u"录制成功")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_adjust_subtitles.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test6_upload_logo(self):
        '''成功上传logo的测试'''
        try:
            logger.info("成功上传logo的测试")
            self.upload_logo(readconfig.date_path+"\\logo_sun.bmp")
            self.find_element(self.success)
            logger.info(self.getAttribute(self.success,"textContent")) #获取 layer.msg 弹窗的信息
            self.assertEqual(self.getAttribute(self.success,"textContent"),"LOGO上传成功!")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path, 'test_upload_logo.png'))
            raise Exception("false")

    def test7_upload_logo2(self):
        '''上传logo失败的测试'''  
        try:
            logger.info("上传logo失败的测试")
            self.upload_logo(readconfig.date_path+"\\logo_fail.bmp")
            self.find_element(self.success)
            logger.info(self.getAttribute(self.success,"textContent")) #获取 layer.msg 弹窗的信息
            self.assertEqual(self.getAttribute(self.success,"textContent"),"LOGO文件格式错误!")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path, 'test_upload_logo2.png'))
            raise Exception("false")
  
    def test8_adjust_subtitles(self):
        '''录制一段操作字幕的视频 '''
        try:
            logger.info("录制一段操作字幕的视频")
            self.adjust_subtitles()
            logger.info(u"录制成功")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_adjust_subtitles.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()
 
            


       

if __name__ == "__main__":
   unittest.main()