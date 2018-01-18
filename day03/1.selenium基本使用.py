import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
try:
    browser = webdriver.Chrome()  # 选择要开启的浏览器
    browser.get('https://www.taobao.com')
    # wait = WebDriverWait(browser,10)  # 显式等待
    browser.implicitly_wait(5)          # 隐式等待

    # 找到标签，并输入搜索词
    # input_tag = browser.find_element_by_id('twotabsearchtextbox')  # 亚马逊
    input_tag = browser.find_element_by_id('q')  # 淘宝
    input_tag.send_keys('充气baby')
    # 找到搜索按钮，并点击
    # button = browser.find_element_by_css_selector('#nav-search-submit-text + .nav-input') # 亚马逊
    button = browser.find_element_by_css_selector('#J_TSearchForm > div > .btn-search')     # 淘宝
    button.click()


    # input_tag=browser.find_element_by_id('twotabsearchtextbox')  # 亚马逊
    input_tag=browser.find_element_by_id('q')
    print(input_tag)
    input_tag.clear() # 清空
    input_tag.send_keys('我爱你')
    time.sleep(3)
    # 回车
    input_tag.send_keys(Keys.ENTER)
    # 28 29作用也是输入回车
    # button = browser.find_element_by_css_selector('#nav-search-submit-text + .nav-input')
    # button.click()

finally:
    time.sleep(10)
    browser.quit()

# browser=webdriver.Chrome()
# browser.get('https://www.amazon.cn/')
# wait=WebDriverWait(browser,10)
# input_tag=wait.until(EC.presence_of_element_located((By.ID,'twotabsearchtextbox'))) # 等这个加载完。
# input_tag.send_keys('iphone 8')
# button=browser.find_element_by_css_selector('#nav-search > form > div.nav-right > div > input')
# button.click()
#
#
# import time
# time.sleep(3)
#
# input_tag=browser.find_element_by_id('twotabsearchtextbox')
# input_tag.clear() #清空输入框
# input_tag.send_keys('iphone7plus')
# button=browser.find_element_by_css_selector('#nav-search > form > div.nav-right > div > input')
# button.click()