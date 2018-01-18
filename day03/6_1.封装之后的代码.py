from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
from PIL import Image #pip3 install pillow

import time

def get_snap(driver):
    driver.save_screenshot('snap.png')
    snap_obj=Image.open('snap.png')
    return snap_obj

def get_image(driver):
    img=driver.find_element_by_class_name('geetest_canvas_img')
    time.sleep(2) #等待图片加载完毕
    size=img.size
    location=img.location

    left=location['x']
    top=location['y']
    right=left+size['width']
    bottom=top+size['height']

    snap_obj=get_snap(driver)
    # print(driver)
    # <selenium.webdriver.chrome.webdriver.WebDriver (session="902955278134d23c7cc7c453718e8c93")>
    # print(snap_obj)
    # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=2400x1356 at 0x10357FA20>
    image_obj=snap_obj.crop((left,top,right,bottom))
    # image_obj.show()
    return image_obj

def get_distance(image1,image2):
    start_x=58
    threhold=60
    # print(image1.size)
    # print(image2.size)
    for x in range(start_x,image1.size[0]):
        for y in range(image1.size[1]):
            rgb1=image1.load()[x,y]
            rgb2=image2.load()[x,y]
            # print(rgb1)
            # print(rgb2)
            res1=abs(rgb1[0]-rgb2[0])
            res2=abs(rgb1[1]-rgb2[1])
            res3=abs(rgb1[2]-rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return x-7

def get_tracks(distance):
    distance+=20
    #v=v0+a*t
    #s=v*t+0.5*a*(t**2)

    v0=0
    s=0
    t=0.2
    mid=distance*3/5
    forward_tracks=[]

    while s < distance:
        if s < mid:
            a=2
        else:
            a=-3

        v=v0
        track=v*t+0.5*a*(t**2)
        track=round(track)
        v0=v+a*t
        s+=track
        forward_tracks.append(track)
    back_tracks=[-1,-1,-1,-2,-2,-2,-3,-3,-2,-2,-1] #20
    return {"forward_tracks":forward_tracks,'back_tracks':back_tracks}

try:
    driver = webdriver.Chrome()
    driver.get('https://passport.cnblogs.com/user/signin')
    driver.implicitly_wait(3)

    #1、输入账号、密码，然后点击登陆
    input_user=driver.find_element_by_id('input1')
    input_pwd=driver.find_element_by_id('input2')
    login_button=driver.find_element_by_id('signin')

    input_user.send_keys('555')
    input_pwd.send_keys('555555555')
    login_button.click()

    #2、点击按钮，弹出没有缺口的图
    button=driver.find_element_by_class_name('geetest_radar_tip')
    button.click()

    #3、针对没有缺口的图片进行截图
    image1=get_image(driver)

    #4、点击滑动按钮，弹出有缺口的图
    slider_button=driver.find_element_by_class_name('geetest_slider_button')
    slider_button.click()

    #5、针对有缺口的图片进行截图
    image2=get_image(driver)

    #6、对比两张图片，找出缺口，即滑动的位移
    distance=get_distance(image1,image2)
    # print(distance)

    #7、按照人的行为行为习惯，把总位移切成一段段小的位移
    traks_dic=get_tracks(distance)

    #8、按照位移移动
    slider_button=driver.find_element_by_class_name('geetest_slider_button')
    ActionChains(driver).click_and_hold(slider_button).perform()
    #先向前移动
    forward_tracks=traks_dic["forward_tracks"]
    back_tracks=traks_dic["back_tracks"]
    for forward_track in forward_tracks:
        ActionChains(driver).move_by_offset(xoffset=forward_track,yoffset=0).perform()

    #短暂停顿，发现傻逼，移过了
    time.sleep(0.2)

    # 先向后移动
    for back_track in back_tracks:
        ActionChains(driver).move_by_offset(xoffset=back_track,yoffset=0).perform()

    ActionChains(driver).move_by_offset(xoffset=-3,yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3,yoffset=0).perform()
    time.sleep(0.3)
    ActionChains(driver).release().perform()


    time.sleep(10)
finally:
    driver.quit()






# EC的作用
#     wait=WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left'))) #等到id为content_left的元素加载完毕,最多等10秒
#
#
# 标签选择器：
    #===============所有方法===================
    # 1、find_element_by_id
    # 2、find_element_by_link_text
    # 3、find_element_by_partial_link_text
    # 4、find_element_by_tag_name
    # 5、find_element_by_class_name
    # 6、find_element_by_name
    # 7、find_element_by_css_selector
    # 8、find_element_by_xpath
    # 强调：
    # 1、上述均可以改写成find_element(By.ID,'kw')的形式
    # 2、find_elements_by_xxx的形式是查找到多个元素，结果为列表


#获取标签属性，
# print(tag.get_attribute('src'))
#
#
# #获取标签ID，位置，名称，大小（了解）
# print(tag.id)
# print(tag.location)
# print(tag.tag_name)
# print(tag.size)



# 五 等待元素被加载

#1、selenium只是模拟浏览器的行为，而浏览器解析页面是需要时间的（执行css，js），一些元素可能需要过一段时间才能加载出来，为了保证能查找到元素，必须等待

#2、等待的方式分两种：
# 隐式等待：在browser.get（'xxx'）前就设置，针对所有元素有效
# 显式等待：在browser.get（'xxx'）之后设置，只针对某个元素有效

