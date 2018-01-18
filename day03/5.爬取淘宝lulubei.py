import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
# 爬取天猫撸撸杯


def get_goods(browser):
    goods = browser.find_elements_by_class_name('J_MouserOnverReq')
    # print(goods)
    msgs=[]
    for detail_good in goods:
        tag_a = detail_good.find_element_by_css_selector('.pic > .pic-link')
        detail_url =tag_a.get_attribute('href')
        detail_name = tag_a.find_element_by_tag_name('img').get_attribute('alt')
        detail_price = tag_a.get_attribute('trace-price')
        detail_pic = tag_a.find_element_by_tag_name('img').get_attribute('src')

        msg="""
            🎃🎃🎃🎃🎃
            商品名称：{0},
            商品链接：{1},
            商品价钱：{2}，
            商品图片：{3} 
            """.format(detail_name,detail_url,detail_price,detail_pic)
        msgs.append(msg)

    with open('saosao','w') as f :
        for x in msgs:
            f.write(x)

try:
    keyword = '撸撸杯'
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    browser.implicitly_wait(10)
    # 找到搜索框，并输入关键字
    # browser.find_element_by_css_selector('div .s-combobox-input > input')
    search_tag = browser.find_element_by_id('q')
    search_tag.send_keys(keyword)
    search_tag.send_keys(Keys.ENTER)
    get_goods(browser)
    time.sleep(50)
    # print(browser)
finally:
    browser.quit()






