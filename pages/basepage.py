#coding:utf-8
'''
Created on 2019年04月16日

@author: Aloe
'''
# •ActionChains是自动执行低级交互的一种方式，例如：鼠标移动，鼠标点按，键盘操作，文本操作等。
# •当我们调用这里的方法时，这些操作会被先储存在一个队列中，当我们调用perform()方法时，队列中的操作会被按顺序执行，执行后队列被清空

import time
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait



class BasePage(object):
    '''
    页面基础类
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver

    #显式等待
    def WebDriverWait(self, loc, MaxTime=10, Mimtime=0.5):
        WebDriverWait(self.driver, MaxTime, Mimtime,ignored_exceptions="no this element").until(ES.presence_of_element_located((loc)))

    # 查找元素s
    def find_element(self, loc):
        return WebDriverWait(self.driver,10, 0.5, ignored_exceptions="no this element").until(ES.presence_of_element_located((loc)))
        # 使用上面的加了等待的查找元素有的类似于alert的对话框元素查找不到
        # return self.driver.find_element(*loc)
    

    #在输入框中输入文字
    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)
    
    #点击事件    
    def click(self,loc):
        self.find_element(loc).click()
    
    #清空输入框数据    
    def clear(self,loc):
        self.find_element(loc).clear()
    
    #鼠标悬浮    
    def move_to_element(self,loc):
        element = self.find_element(loc)
        ActionChains(self.driver).move_to_element(element).perform()

    # 鼠标长按
    def long_click(self,loc,time=3):
        element = self.find_element(loc)
        ActionChains(self.driver).click_and_hold(element).perform()
        sleep(time)
        # 在id属性值为“div1”的元素上释放一直释放的鼠标左键
        ActionChains(self.driver).release(element).perform()
    
    # 鼠标拖拽
    def drag_and_drop(self,loc1,loc2):
        element1 = self.find_element(loc1) #element1为定位元素的原位置
        element2 = self.find_element(loc2) #element2为定位元素的目标位置
        ActionChains(self.driver).drag_and_drop(element1,element2).perform()

    # 鼠标按坐标来拖拽
    def drag_and_drop_by_offset(self, loc, xoffset, yoffset):
        element = self.find_element(loc) 
        ActionChains(self.driver).drag_and_drop_by_offset(element, xoffset, yoffset).perform()
    

    #获取输入框文本    
    def gettext(self,loc):
        return self.find_element(loc).text
        
    #获取input标签的文本
    def getValuetext(self,loc):
        return self.find_element(loc).get_attribute('value')

    #获取div标签的文本
    def getInnerHTML(self,loc):
        return self.find_element(loc).get_attribute('innerHTML')
    
    #获取标签的属性值
    def getAttribute(self,loc,arrt):
        return self.find_element(loc).get_attribute('%s' % arrt)

    #获取alert的文本
    def get_alert_text(self):
        return self.driver.switch_to.alert.text

    #接受alert
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    #取消alert
    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()
    
    #滚动条拉到屏幕最下方    
    def scroll_to_down(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
    
    #滚动条拉到屏幕最上方    
    def scroll_to_up(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        
    #滚动条拉到元素位置    
    def scroll_to_element(self,loc):
        element = self.find_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
    
    #某个预期元素是否被选中
    def is_selected(self,loc):
        element = self.find_element(loc)
        ES.element_located_to_be_selected(element) 
    
    #某个元素的value值是否包含预期字符串
    def text_be_value(self,loc,text):
        element = self.find_element(loc)
        ES.text_to_be_present_in_element_value(element,text) 
    
    #元素处于可编辑状态
    def is_enabled(self,loc):
        self.find_element(loc).is_enabled()
            
    def input_time(self,loc,selector,attribute,istime):
        #这里的selector,attribute的值要类似这样：selector="'abc'",这样的值才能出现单引号
        jq = "$(%s).removeAttr(%s)"%(selector,attribute)
        self.driver.execute_script(jq)
        self.clear(loc)
        self.input_text(loc, istime)
      
    def is_selected_value(self,loc):
        return self.find_element(loc).is_selected()
    
    def get_element_att(self,loc):
        #不可编辑属性测试
        jp = "$('#frmVideoEdit > div:nth-child(23) > div > label > select').attr('disabled')"
        return self.driver.execute_script(jp)

    def set_viewport_size(self,driver, width, height):
        window_size = self.driver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
            window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
        self.driver.set_window_size(*window_size)