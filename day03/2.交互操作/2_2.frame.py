

#frame相当于一个单独的网页，在父frame里是无法直接查看到子frame的元素的，
# 必须switch_to_frame切到该frame下，才能进一步查找

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素


try:
    browser=webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

    browser.switch_to.frame('iframeResult') #切换到id为iframeResult的frame

    tag1=browser.find_element_by_id('droppable')
    print(tag1)

    # tag2=browser.find_element_by_id('textareaCode') #报错，在子frame里无法查看到父frame的元素
    browser.switch_to.parent_frame() #切回父frame,就可以查找到了
    tag2=browser.find_element_by_id('textareaCode')
    print(tag2)

finally:
    browser.close()