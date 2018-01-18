from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
import time

driver=webdriver.Chrome()
driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(3)



#1：输入账号密码，点击登录
input_name = driver.find_element_by_id('input1')
input_pwd = driver.find_element_by_id('input2')
input_btn = driver.find_element_by_id('signin')




#2：点击按钮，弹出没有缺口的图

#3：针对没有缺口的图片进行截图

#4：点击滑动按钮，出现有缺口的图

#5：针对没有缺口的图片截图

#6：对比两张图片，找出缺口，即滑动的位移

#7：按照人的行为习惯，把总位移切成一段段(意在：模拟人的滑动习惯)。

#8：按照位移，开始移动。