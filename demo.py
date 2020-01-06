
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from models import readconfig
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
    '''登录测试'''

    #元素集
    #用户名
    username = (By.ID,"uname")
    #密码
    passwd = (By.ID,"upswd")
    #登录 按钮
    loginbtn = (By.ID,"lgBtn")
    #记住密码按钮
    remember_passwd = (By.XPATH,"//*[@id='lg']/div[2]/div[4]/label/i")

    def test_login(self): 

        try:
            self.driver = webdriver.Firefox()             # 打开火狐浏览器驱动
            self.driver.get("http://169.254.178.178")     # 打开这个网址
            self.driver.implicitly_wait(20)               # 隐式等待20秒

            self.input_text(self.username, "admin")       # 往用户名输入框输入admin
            self.input_text(self.passwd, "admin")         # 往密码输入框输入admin
            self.click(self.loginbtn)                     # 点击登录按钮
            WebDriverWait(self.driver,5,0.5).until(ES.title_is(u"录播管理系统"))   # 显示等待5秒

            self.assertEqual(self.driver.title, u"录播管理系统")                   # 断言登录后的页面的title是否是录播管理系统
        except Exception as msg:
            logger.error(u"异常原因：%s"%msg)
            self.driver.get_screenshot_as_file(os.path.join(readconfig.screen_path,'login.png'))  # 如果try模块出错，给出错误信息，并且将当前页面截图保存
            raise Exception("false")