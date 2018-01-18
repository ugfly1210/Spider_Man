# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
# from selenium.webdriver.common.keys import Keys  # 键盘按键操作
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
# import time
#
# driver = webdriver.Chrome()
# driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# wait=WebDriverWait(driver,3)
# # driver.implicitly_wait(3)  # 使用隐式等待
#
# try:
#     driver.switch_to.frame('iframeResult') ##切换到iframeResult
#     sourse=driver.find_element_by_id('draggable')
#     target=driver.find_element_by_id('droppable')
#
#     #方式一：基于同一个动作链串行执行
#     # actions=ActionChains(driver) #拿到动作链对象
#     # actions.drag_and_drop(sourse,target) #把动作放到动作链中，准备串行执行
#     # actions.perform()
#
#     #方式二：不同的动作链，每次移动的位移都不同
#     ActionChains(driver).click_and_hold(sourse).perform()
#     distance=target.location['x']-sourse.location['x']
#
#     track=0
#     while track < distance:
#         ActionChains(driver).move_by_offset(xoffset=2,yoffset=0).perform()
#         track+=2
#
#     ActionChains(driver).release().perform()
#
#     time.sleep(10)
#
# finally:
#     driver.quit()

# Action Chains



# 滑动验证码的逻辑，和这个差不多。

# 按住源不动，到目标点之后，再松开鼠标。





from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
import time

driver=webdriver.Chrome()
driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# driver.get('http://www.baidu.com')
driver.implicitly_wait(3)

try:
    driver.switch_to.frame('iframeResult')
    # driver.switch_to.parent_frame()

    source=driver.find_element_by_id('draggable')
    target=driver.find_element_by_id('droppable')
    print(source,target)

    #方式一：
    # actions=ActionChains(driver)
    # actions.drag_and_drop(source,target)
    # actions.perform()

    #方式二：
    distance=target.location['x']-source.location['x']
    ActionChains(driver).click_and_hold(source).perform()

    print(distance)
    s=0
    while s < distance:
        print(s)
        ActionChains(driver).move_by_offset(xoffset=2,yoffset=0).perform()
        s+=2
    ActionChains(driver).release().perform()


    # driver.execute_script('alert("xxxxxxxxx")')
    time.sleep(6)
finally:
    driver.close()