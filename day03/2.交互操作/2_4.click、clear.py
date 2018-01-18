from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素

browser=webdriver.Chrome()
browser.get('https://www.amazon.cn/')
wait=WebDriverWait(browser,10)


input_tag=wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox')))
input_tag.send_keys('iphone 8')
button=browser.find_element_by_css_selector('#nav-search > form > div.nav-right > div > input')
button.click()


import time
time.sleep(3)

input_tag=browser.find_element_by_id('twotabsearchtextbox')
input_tag.clear() #清空输入框
input_tag.send_keys('iphone7plus')
button=browser.find_element_by_css_selector('#nav-search > form > div.nav-right > div > input')
button.click()



# browser.quit()