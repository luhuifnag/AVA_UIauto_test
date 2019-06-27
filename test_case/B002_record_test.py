#coding:utf-8
'''
Created on 2019年05月08日

@author: Aloe
'''
import os
import unittest
from time import sleep

from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from models import readconfig
from models.myunit import MyTest
from pages.home_page import HomePage
from pages.Input_output_page import InputOutput
from pages.loginpage import LoginPage
from pages.record_page import RecordPage
from pages.records import Records
from pages.video_managemen import VideoManagemen
from utils.log import logger


class Recorder(MyTest,Records,RecordPage):
    '''录制相关测试'''
               
    def test1_basic_recording(self):
        '''基本录制测试,检验录制的视频详细信息与输入的主题主讲人是否一致''' 
        try:
            logger.info("基本录制测试,检验录制的视频详细信息与输入的主题主讲人是否一致")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            self.basic_recording()
            home.click_record_black() 
            sleep(1)
            video.file_detailed(2)
            sleep(3)
            self.assertEqual(self.gettext(video.themesinf),"基本录制")
            self.assertEqual(self.gettext(video.spaekerinf),"陈老师")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_basic_recording.png'))
            raise Exception("false")

    def test2_pause_recording(self):
        '''暂停录制测试'''
        try:
            logger.info("暂停录制测试")
            self.pause_record()
            #判断暂停过了3秒后时间录制的时间有没有变化
            pause_time1 = self.find_element(self.timer).text
            sleep(3)
            pause_time2 = self.find_element(self.timer).text
            sleep(2)
            self.assertEqual(pause_time1,pause_time2)
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_pause_recording1.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test3_resume_recording(self):
        '''暂停后恢复录制测试'''
        try:
            logger.info("暂停后恢复录制测试")
            self.resume_recording()
            #判断恢复录制20秒后录制的时间有没有变化
            pause_time1 = self.find_element(self.timer).text
            self.pause_recording()
            sleep(10)
            pause_time3 = self.find_element(self.timer).text
            sleep(2)
            self.assertNotEqual(pause_time3,pause_time1)   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_resume_recording.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test4_recording_back(self):
        '''测试在录制过程中点击录播页面返回按钮，验证是否有提示信息''' 
        try:
            logger.info("测试在录制过程中点击录播页面返回按钮，验证是否有提示信息'")
            self.recording_back()
            tips = self.gettext(self.recording_back_tips)
            self.click(self.recording_back_cancel)    
            self.assertEqual(tips,"正在录制或直播 ,确定返回模式选择？")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_recording_back.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test5_main_1080p_and_sub_720p(self):
        '''主码流为1080p，子码流为720p的录制测试'''  
        try:
            logger.info("主码流为1080p，子码流为720p的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            if self.get_status() == "u8":
                self.record_main_and_sub(3,9,"1080p","720p","主码流和子码流录制")
            else:
                self.record_main_and_sub(1,5,"1080p","720p","主码流和子码流录制")
            home.click_record_black()
            sleep(1)
            video.file_detailed(2)       
            sleep(3)
            resolv = self.gettext(video.resolving)
            try:
                self.assertEqual(resolv,"1920x1080")   #要判断一下是主码流在前还是子码流在前
            except:
                self.assertEqual(resolv,"1280x720")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test5_main_1080p_and_sub_720p1.png'))
            raise Exception("false")
        finally:
            sleep(1)
            video.file_detailed2(3)
            try:
                try:
                    self.assertEqual(resolv,"1920x1080") 
                except:
                    self.assertEqual(resolv,"1280x720")   
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test5_main_1080p_and_sub_720p2.png'))
                raise Exception("false")

    def test6_main_720p_and_sub_540p(self):
        '''主码流为720p，子码流为标清的录制测试'''  
        try:
            logger.info("主码流为720p，子码流为标清的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            if self.get_status() == "u8":
                self.record_main_and_sub(4,10,"720p","标清","主码流和子码流录制")
            else:
                self.record_main_and_sub(2,6,"720p","标清","主码流和子码流录制")
            home.click_record_black()
            sleep(1)
            video.file_detailed(2)       
            sleep(3)
            resolv = self.gettext(video.resolving)
            try:
                self.assertEqual(resolv,"960x540")   #要判断一下是主码流在前还是子码流在前
            except:
                self.assertEqual(resolv,"1280x720")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_main_720p_and_sub_540p1.png'))
            raise Exception("false")
        finally:
            sleep(1)
            video.file_detailed2(3)
            try:
                try:
                    self.assertEqual(resolv,"960x540") 
                except:
                    self.assertEqual(resolv,"1280x720")   
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_main_720p_and_sub_540p2.png'))
                raise Exception("false")

    def test7_main_540p_and_sub_360p(self):
        '''主码流为标清，子码流为流畅的录制测试'''  
        try:
            logger.info("主码流为标清，子码流为流畅的录制测试")
            home = HomePage(self.driver)
            video = VideoManagemen(self.driver)
            if self.get_status() == "u8":
                self.record_main_and_sub(5,11,"1080p","720p","主码流和子码流录制")
            else:
                self.record_main_and_sub(3,7,"1080p","720p","主码流和子码流录制")
            home.click_record_black()
            sleep(1)
            video.file_detailed(2)       
            sleep(3)
            resolv = self.gettext(video.resolving)
            try:
                self.assertEqual(resolv,"960x540")   #要判断一下是主码流在前还是子码流在前
            except:
                self.assertEqual(resolv,"640x360")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test7_main_540p_and_sub_360p1.png'))
            raise Exception("false")
        finally:
            sleep(1)
            video.file_detailed2(3)
            try:
                try:
                    self.assertEqual(resolv,"960x540")   
                except:
                    self.assertEqual(resolv,"640x360") 
            except Exception as msg:
                logger.error(u"异常原因：%s"%msg)
                self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test7_main_540p_and_sub_360p2.png'))
                raise Exception("false")

    def test8_record_strat_auacking(self):
        '''录制时启用全自动跟踪（录播模式下）'''
        try:
            logger.info("测试录制时启用全自动跟踪（录播模式下）")
            records = Records(self.driver)
            auto_status = records.record_strat_auacking()   
            self.assertEqual(auto_status,"ava-btn ava-btn-md ava-btn-normal ava-btn-primary")   
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_record_strat_auacking.png'))
            raise Exception("false")
        finally:
            if self.getAttribute(self.recordbtn,"style")==self.stop_record_style():
                pass
            else:
                self.stop_recording()

    def test_record_teacher_act(self):
        '''教师行为分析文件的测试'''
        try:
            logger.info("教师行为分析文件的测试")
            records = Records(self.driver)
            records.record_teacher_act() 
            self.back()
            sleep(2)
            vido = VideoManagemen(self.driver)
            vido.check_recorder_massage()
            sleep(2)
            self.assertEqual(self.gettext(vido.sw), "下载SW")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_record_teacher_act.png'))
            raise Exception("false")

    def test9_modify_limit(self):
        '''录制期间无法更改录制管理中的设置'''
        try:
            logger.info("录制期间无法更改录制管理中的设置")
            records = Records(self.driver)
            records.modify_limit()
            WebDriverWait(self.driver,5,0.5).until(ES.alert_is_present()) 
            self.assertEqual(self.get_alert_text(), "录制中，无法保存")           
            self.accept_alert()
            self.driver.switch_to.default_content()
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test11_modify_limit.png'))
            raise Exception("false")
        finally:
            home = HomePage(self.driver)
            home.click_system_setup_blck()
            sleep(1)
            home.click_record()
            sleep(2)
            self.stop_recording()

    def test_get_multi_num(self):
        '''录制所有的网络多流'''
        try:
            logger.info("录制所有的网络多流")
            records = Records(self.driver)
            records.record_all_netmulti(readconfig.multiurl)
            logger.info("录制成功")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test11_modify_limit.png'))
            raise Exception("false")
        
    def test_record_custom_quality(self):
        '''自定义码流质量的录制'''
        try:
            logger.info("自定义码流质量的录制")
            records = Records(self.driver)
            records.record_custom_quality()
            logger.info("录制成功")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_record_custom_quality.png'))
            raise Exception("false")
    
    def test_record_start_ftp(self):
        '''启动ftp上传录制测试'''
        try:
            logger.info("启动ftp上传录制测试")
            records = Records(self.driver)
            records.record_start_ftp()
            logger.info("录制成功")
            sleep(5)
            self.assertEqual(self.gettext(self.ftp_status), "上传完成")
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'test_record_start_ftp.png'))
            raise Exception("false")
      

            
        
if __name__ == "__main__":
   unittest.main()
