#使用以下方法在运行的时候可以不打开浏览器，运行速度杠杠的
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
print(driver.title)
driver.quit()
