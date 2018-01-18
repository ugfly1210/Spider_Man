import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')

browser.back()
print(browser.get_cookie())
print(browser.get_cookies())
time.sleep(2)
browser.forward()
browser.quit()