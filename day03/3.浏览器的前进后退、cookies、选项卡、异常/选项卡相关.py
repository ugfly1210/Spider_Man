#选项卡管理：切换选项卡，有js的方式windows.open,有windows快捷键：ctrl+t等，最通用的就是js的方式
import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')

print(browser.window_handles) #获取所有的选项卡
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(5)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://www.python.org')
browser.quit()
