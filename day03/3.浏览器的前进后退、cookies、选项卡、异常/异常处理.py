from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchFrameException

try:
    browser=webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to.frame('iframssseResult')

except TimeoutException as e:
    print(e)
except NoSuchFrameException as e:
    print(e)
finally:
    browser.quit()