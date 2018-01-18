import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素


# 该代码生效与 2018-01-18     不知道什么时候会变。重在学习流程。

# username = '1111111'
# password = '2222222'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('https://mail.163.com')
#     browser.implicitly_wait(5)
#     frame = browser.find_element_by_id('x-URS-iframe')  # 这个163有点骚气，需要进入到该id下的iframe
#     browser.switch_to.frame(frame)
#
#     user_tag = browser.find_element_by_id('auto-id-1516274652838')
#     user_tag.send_keys(username)
#     pwd_tag = browser.find_element_by_id('auto-id-1516274652839')
#     pwd_tag.send_keys(password)
#
#     pwd_tag.send_keys(Keys.ENTER)
#     login = browser.find_elements_by_id('dologin')
#
#     # 这里如果有验证码。。。  原谅我，我还在学习破解该验证码方式。
#     # 。。。略略略



browser = webdriver.Chrome()
try:
    browser.get('http://mail.163.com/')

    wait = WebDriverWait(browser, 5)

    frame = wait.until(EC.presence_of_element_located((By.ID, 'x-URS-iframe')))
    browser.switch_to.frame(frame)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-container')))

    inp_user = browser.find_element_by_name('email')
    inp_pwd = browser.find_element_by_name('password')
    button = browser.find_element_by_id('dologin')
    inp_user.send_keys('18611453110')
    inp_pwd.send_keys('xxxx')
    button.click()


    wait.until(EC.presence_of_element_located((By.ID, 'dvNavTop')))
    write_msg = browser.find_elements_by_css_selector('#dvNavTop li')[1]  # 获取第二个li标签就是“写信”了
    write_msg.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tH0')))
    recv_man = browser.find_element_by_class_name('nui-editableAddr-ipt')
    title = browser.find_element_by_css_selector('.dG0 .nui-ipt-input')
    recv_man.send_keys('666@qq.com')
    title.send_keys('8787')
    print(title.tag_name)

    frame = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'APP-editor-iframe')))
    browser.switch_to.frame(frame)
    body = browser.find_element(By.CSS_SELECTOR, 'body')
    body.send_keys('666，wenwenwen')

    browser.switch_to.parent_frame()  # 切回他爹
    send_button = browser.find_element_by_class_name('nui-toolbar-item')
    send_button.click()

    # 可以睡时间久一点别让浏览器关掉，看看发送成功没有
    import time

    time.sleep(100)

except Exception as e:
    print(e)

finally:
    browser.quit()



