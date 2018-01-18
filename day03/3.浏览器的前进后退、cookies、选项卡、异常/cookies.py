#cookies
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'k1':'xxx','k2':'yyy'})
print(browser.get_cookies())

# browser.delete_all_cookies()