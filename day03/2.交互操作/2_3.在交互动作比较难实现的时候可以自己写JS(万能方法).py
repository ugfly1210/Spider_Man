from selenium import webdriver
from selenium.webdriver import ActionChains  # 滑动验证相关
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素

try:
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.execute_script('alert("hello world")')
finally:
    browser.quit()