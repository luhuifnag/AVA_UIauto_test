#coding:utf-8
'''
Created on 2019年04月26日

@author: Aloe
'''

import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

from pages.basepage import BasePage
from pages.home_page import HomePage
from pages.loginpage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from utils.log import logger

class RecordPage(BasePage):
    
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')
    now_time = datetime.datetime.now().strftime("%H:%M:%S")
    #记时器
    timer = (By.ID, "time")
    #ftp上传状态
    ftp_status = (By.ID, "ftpMsg")
    #录制按钮
    recordbtn = (By.ID, "video_rec")
    #停止录制的style属性值
    def stop_record_style(self):
        return "background: rgba(0, 0, 0, 0) url(\"/assets/images/main/ic_stop.png\") repeat scroll 0% 0%;"
    #暂停录制按钮
    pausebtn = (By.ID, "video_pause")
    #录制时返回主页面的提示信息
    recording_back_tips = (By.XPATH, "//*[@id='layui-layer1']/div[2]")
    #录制或直播时返回主页面的确定按钮
    recording_back_conmit = (By.XPATH, "//*[@id='layui-layer1']/div[3]/a[1]")
    #录制或直播时返回主页面的取消按钮
    recording_back_cancel = (By.XPATH, "//*[@id='layui-layer1']/div[3]/a[2]") 
    # 直播按钮
    livebtn = (By.ID, "video_live")

    # 全自动按钮
    autobtn = (By.ID, "auto")
    # 半自动按钮
    semiautobtn = (By.ID, "semiauto")
    # 手动按钮
    manualbtn = (By.ID, "manual")

    # 布局
    blendmodebtn = (By.ID, "blendmodeMenu")
    # 获取布局按钮的数量
    def get_blendmode_num(self):
        bles = self.driver.find_elements_by_xpath("//*[@id='layout']/li")
        return len(bles)   
    # 点击不同的布局按钮
    def click_blendmode(self,num):
        blendmode = (By.XPATH, "//*[@id='layout']/li[%d]/img" % num) # %d的取值分别为1、2…9代表不同的布局 
        self.click(blendmode)

    # 特技
    blendstylebtn = (By.ID, "blendstyleMenu")
    # 点击不同的特技按钮
    def click_blendstylebtn(self,num):
        blendstyle = (By.XPATH, "//*[@id='stunt']/li[%d]/img" % num) # %d的取值分别为1、2…9代表不同的布局  
        self.click(blendstyle)

    # logo
    logobtn = (By.ID, "logoMenu")
    # 显示logo的按钮
    display_logo = (By.XPATH, "//*[@id='logoView']/div[1]/div[1]/label[1]/i")
    # 隐藏logo的按钮
    hide_logo = (By.XPATH, "//*[@id=‘logoView’]/div[1]/div[1]/label[2]/i")
    # 上传logo的路径选择按钮
    logofile = (By.ID,"logofile")
    # 上传按钮
    upload = (By.ID,"logofileUploadBtn")
    # logo位置框
    logoRange = (By.ID,"logoRange")
    # 位置框内的logo
    logoDrag = (By.ID,"logoDrag")
    # logo上成功提示
    def success_message(self):
        divs = self.driver.find_elements_by_xpath("//*[@id='sysVersion']/div")
        num = len(divs)
        message = (By.XPATH, "//*[@id='sysVersion']/div[%s]" % str(num-1))
        print(self.getAttribute(message,"textContent"))
        return self.getAttribute(message,"textContent")

    # 字幕
    subtitlebtn = (By.ID, "subtitleMenu")
    # 字幕框
    osd_input = (By.ID, "osd_input")
    # 字幕下拉按钮
    drop_downbtn = (By.XPATH, "//*[@id='preosd_sel-button']/span[1]")
    # 输出按钮
    outputbtn = (By.ID, "subtitleSetBtn") 
    # 显示按钮
    showbtn = (By.XPATH, "//*[@id='subtitleView']/div/div/div[2]/div[1]/label[1]/i")
    #隐藏按钮
    hidebtn = (By.XPATH, "//*[@id='subtitleView']/div/div/div[2]/div[1]/label[2]/i")
    # 滚动按钮
    rollbtn = (By.XPATH, "//*[@id='subtitleView']/div/div/div[2]/div[3]/label[1]/i")
    # 静止按钮
    staticbtn = (By.XPATH, "//*[@id='subtitleView']/div/div/div[2]/div[3]/label[2]/i") 
   
    # 变焦
    ptzbtn1 = (By.ID, "zoomMenu")
    ptzbtn2 = (By.ID, "ptzMenu")
    # 快捷变焦的4个按钮
    focus1 = (By.XPATH,"//*[@id='c_zoom']/li[1]/img")
    focus2 = (By.XPATH,"//*[@id='c_zoom']/li[2]/img")
    focus3 = (By.XPATH,"//*[@id='c_zoom']/li[3]/img")
    focus4 = (By.XPATH,"//*[@id='c_zoom']/li[4]/img")

    # 音量
    volumetn = (By.ID, "volumeMenu")

    # 云台的上、下、左、右控制按钮 
    '''
    svg的路径需要按照特殊写法编写才能进行识别,
    从svg元素开始，下面的元素都要以  *[name()='svg element'] 这种形式进行编写 
    在selenium点击svg形式的页面元素时，不能用普通的driver.find_element_by_xpath(svgelementXpath).click() 的方式进行点击，这样操作执行时会报错误信息。
    需要以定义action的形式访问svg的元素信息。
    from selenium.webdriver import ActionChains
    '''
    up = (By.XPATH, "//*[@id='paper']/*[name()='svg']/*[name()='path'][2]")    
    down = (By.XPATH, "//*[@id='paper']/*[name()='svg']/*[name()='path'][4]")   
    left = (By.XPATH, "//*[@id='paper']/*[name()='svg']/*[name()='path'][1]")   
    right = (By.XPATH, "//*[@id='paper']/*[name()='svg']/*[name()='path'][3]")   
    # 减号变焦
    reducebtn = (By.XPATH, "//*[@id='ytsub']/img")
    # 加号变焦
    addbtn = (By.XPATH, "//*[@id='ytadd']/img")
    # 灵敏度条
    ytbar = (By.ID, "ytbar")
    # 灵敏度滑条
    sensitivity = (By.XPATH, "//*[@id='ytbar']/span")
    

    # 获取预览视窗的个数
    def get_preview_num(self):
        previews = self.driver.find_elements_by_xpath("//*[@id='videoLists']/li")
        preview_num = len(previews)
        return int(preview_num)

    # 获取预览视窗的名称
    def get_preview_tag(self):
        num = self.get_preview_num()
        taglist = []
        for i in range(num):
            tags = (By.XPATH, "//*[@id='videoLists']/li[%s]/div[1]/div" % str(i+1))
            sleep(1)
            self.scroll_to_element(tags)
            taglist.append(self.gettext(tags))
        sleep(1)
        logger.info(taglist)
        return taglist
            

    def back(self):
        logger.info(u"点击录播页面返回按钮")
        backbtn = (By.XPATH, "//*[@id='back']")
        self.click(backbtn)

    def input_topic(self, themes):
        logger.info(u"输入主题：%s"% themes)
        themeinput = (By.XPATH, "//*[@id='title']")
        sleep(1)
        self.clear(themeinput)
        sleep(2)
        self.input_text(themeinput, themes)

    def input_speaker(self, speaker):
        logger.info(u"输入主讲人：%s"% speaker)
        speakerinput = (By.XPATH, "//*[@id='speaker']")
        self.clear(speakerinput)
        sleep(1)
        self.input_text(speakerinput, speaker)


    #设置主题和主讲人后开始录制
    def start_recording(self, themes=now_date, speaker=now_time):
        self.input_topic(themes)
        sleep(1)
        self.input_speaker(speaker)
        logger.info(u"点击开始录制")
        self.click(self.recordbtn)

    #暂停录制
    def pause_recording(self):
        logger.info(u"点击暂停/恢复录制按钮")
        self.click(self.pausebtn)
        
    #停止录制
    def stop_recording(self):
        logger.info(u"点击停止录制按钮")
        self.click(self.recordbtn)
        sleep(2)
        sure = (By.XPATH, "//*[@class='layui-layer layui-layer-dialog']/div[3]/a[1]")
        self.click(sure)
        sleep(5)
    
    # 开始/停止直播
    def start_or_stop_live(self):
        logger.info(u"点击直播按钮")
        self.click(self.livebtn)
        sleep(2)

    # 点击全自动按钮
    def click_autobtn(self):
        logger.info(u"点击全自动按钮")
        if self.getAttribute(self.autobtn,"class")=="ava-btn ava-btn-md ava-btn-normal ava-btn-primary":
            pass
        else:
            self.click(self.autobtn)

    # 点击半自动按钮
    def click_semiautobtn(self):
        logger.info(u"点击半自动按钮")
        if self.getAttribute(self.autobtn,"class")=="ava-btn ava-btn-md ava-btn-normal ava-btn-primary":
            pass
        else:
            self.click(self.semiautobtn)

    # 选择要操作的视窗
    def select_windows(self,num=1):
        windows = (By.XPATH,"//*[@id='videoLists']/li[%d]/div[2]/div" % num)   #%d==1表示第一个视窗
        self.click(windows)

    # 选择要出图的视窗（前面的预览视窗标签）
    def select_windows_tags1(self,num=1):
        windows_tags1 = (By.XPATH,"//*[@id='videoLists']/li[%d]/div[1]/div" % num)   #%d==1表示第一个视窗
        self.click(windows_tags1)
    # 选择要出图的视窗（后面两个的预览视窗标签）
    def select_windows_tags2(self,num=1):
        windows_tags2 = (By.XPATH,"//*[@id='videoLists']/li[%d]/div[1]/div[1]" % num)   
        self.click(windows_tags2)
    

    #点击云台四个变焦按钮
    def PTZ_fast_focusing(self):
        logger.info("控制快速变焦")
        try:
            self.click(self.ptzbtn1)
        except:
            self.click(self.ptzbtn2)
        sleep(2)
        self.click(self.focus4)
        sleep(5)
        self.click(self.focus3)
        sleep(5)
        self.click(self.focus2)
        sleep(5)
        self.click(self.focus1)
        sleep(5)

    # 控制云台的方位转动
    def PTZ_turning(self):
        logger.info("控制云台上下左右转动")
        self.scroll_to_element(self.up)
        self.long_click(self.up)
        sleep(2)
        self.scroll_to_element(self.down)
        self.long_click(self.down)
        sleep(2)
        self.scroll_to_element(self.left)
        self.long_click(self.left)
        sleep(2)
        self.scroll_to_element(self.right)
        self.long_click(self.right)
        sleep(2)

    # 控制云台的变焦
    def PTZ_focusing(self):
        self.set_viewport_size(self.driver,1920, 1080)
        logger.info("控制云台拉近聚焦")
        self.scroll_to_element(self.addbtn)
        self.long_click(self.addbtn)
        sleep(2)
        logger.info("控制云台拉远聚焦")
        self.scroll_to_element(self.recordbtn)
        self.long_click(self.reducebtn)
        sleep(2)

    # 调整云台的灵敏度
    def PTZ_sensitivity(self, xoffset, yoffset):
        logger.info(u"调整灵敏度")
        self.drag_and_drop_by_offset(self.ytbar, xoffset, yoffset)

    # 输出字幕
    def output_subtitles(self,num):
        self.click(self.drop_downbtn)
        sleep(1)
        subtitle = (By.XPATH, "//*[@id='preosd_sel-menu']/li[%s]/div" % str(num)) #%s=1时表示第一个默认字幕
        self.move_to_element(subtitle)
        self.click(subtitle)
        self.click(self.outputbtn)
        logger.info("输出第%d条字幕" % num)

    # 获取每条字幕的内容
    def get_subtitles(self):
        self.click(self.drop_downbtn)
        sleep(1)
        subtitles = []
        for i in range(5):
            subtitle = (By.XPATH, "//*[@id='preosd_sel-menu']/li[%s]/div" % str(i+1)) #%s=1时表示第一个默认字幕
            subtitles.append(self.gettext(subtitle))
        return subtitles

    # 编辑字幕
    def edit_subtitles(self,num,text="自定义的字幕ABC123"):
        self.click(self.drop_downbtn)
        subtitle = (By.XPATH, "//*[@id='preosd_sel-menu']/li[%s]/div" % str(num)) #%s=1时表示第一个默认字幕
        self.move_to_element(subtitle)
        self.click(subtitle)
        self.clear(self.osd_input) 
        self.input_text(self.osd_input,text)
        logger.info("编辑第%d条字幕并输出" % num)
    
    # 选择显示字幕
    def select_showbtn(self):
        if self.getAttribute(self.showbtn,"class")=="g_radio inline-block g_radio-checked":
            pass
        else:
            self.click(self.showbtn)

    # 选择隐藏字幕
    def select_hidebtn(self):
        if self.getAttribute(self.hidebtn,"class")=="g_radio inline-block g_radio-checked":
            pass
        else:
            self.click(self.hidebtn)

     # 选择滚动字幕
    def select_rollbtn(self):
        if self.getAttribute(self.rollbtn,"class")=="g_radio inline-block g_radio-checked":
            pass
        else:
            self.click(self.rollbtn)

    # 选择静止字幕
    def select_staticbtn(self):
        if self.getAttribute(self.staticbtn,"class")=="g_radio inline-block g_radio-checked":
            pass
        else:
            self.click(self.staticbtn)
    
    #改变字幕颜色
    def change_font_color(self,num):
        font_color = (By.XPATH, "//*[@id='fontColor']/li[%d]" % num) #%d=1时表示第一个字体颜色
        self.click(font_color)
    
    #改变背景颜色
    def change_background_colorr(self,num):
        background_color = (By.XPATH, "//*[@id='bgColor']/li[%d]" % num)#%d=1时表示第一个背景颜色
        self.click(background_color)



    

      

    

       

    