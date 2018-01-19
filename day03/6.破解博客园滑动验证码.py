import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
from PIL import Image #pip3 install pillow


browser=webdriver.Chrome()
# browser.set_window_size(1366, 768)
browser.get('https://passport.cnblogs.com/user/signin')
browser.implicitly_wait(3)
username = '2222'
pwd = '222222'


def get_image(browser):
    time.sleep(1)
    image1 = browser.find_element_by_class_name('geetest_canvas_img')
    size = image1.size
    location = image1.location

    img_box = (location["x"], location["y"], location["x"] + size['width'], location["y"] + size['height'])
    #
    # left = location['x']
    # top = location['y']
    # right = left + size['width']
    # bottom = top + size['height']
    # # print(left,top)

    browser.save_screenshot('yzm.png')  # 这步就是截图 截整屏
    image_obj = Image.open('yzm.png')  # 读到内存
    # image_obj.resize((1366, 768))
    # print(image_obj)
    # image_obj.show()  # 展示出来
    # return image_obj.crop((left, top, right, bottom))  # 验证码的图，也是最后比对的图
    print(img_box)
    return image_obj.crop(img_box)  # 验证码的图，也是最后比对的图

def get_distance(image1,image2):
    start_x = 58
    threhold = 60  # rgb三个像素的最大偏差
    print(image1)
    print(image2)
    for x in range(start_x,image1.size[0]):
        for y in range(image1.size[1]):
            # 这里对比的是像素
            rgb1 = image1.load()[x,y]
            rgb2 = image2.load()[x,y]
            res1 = abs(rgb1[0]-rgb2[0])
            res2 = abs(rgb1[1]-rgb2[1])
            res3 = abs(rgb1[2]-rgb2[2])

            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                print(x)
                return x - 7  # 这里其实也是模仿的人的行为。 你不可能完全对准。留7个位移的误差
    return x-7

def get_tracks(distance1):
    distance1 += 20  # 这20就是不小心拉多了的二十
    # 匀加速公式
    # v = v0+a*t
    # s = v*t+0.5*a*(t**2)
    v0 = 0
    s = 0
    t = 0.2
    mid = distance1 * 3 / 5  # 前 五分之三路段 是匀加速
    forward_tracks = []
    while s < distance1:
        if s < mid:
            a = 2
        else:
            a = -3
        v = v0
        track = v * t + 0.5 * a * (t ** 2)
        track = round(track)  # 要整数
        v0 = v + a * t
        s += track
        forward_tracks.append(track)  # 向前行进的轨迹
    back_tracks = [-1, -1, -1, -2, -2, -2, -3, -3, -2, -2, -1]
    track_dict = {"forward_tracks": forward_tracks, 'back_tracks': back_tracks}
    return track_dict
#1：输入账号密码，点击登录
input_name = browser.find_element_by_id('input1')
input_pwd = browser.find_element_by_id('input2')
input_btn = browser.find_element_by_id('signin')
name = input_name.send_keys(username)
pwd = input_pwd.send_keys(pwd)
input_btn.click()

#2：点击按钮，弹出没有缺口的图
pic_btn = browser.find_element_by_class_name('geetest_radar_tip')
pic_btn.click()

#3：针对没有缺口的图片进行截图
image_obj11 = get_image(browser)

# def get_image(browser):
#     image1 = browser.find_element_by_class_name('geetest_canvas_img')
#     time.sleep(2)
#     size = image1.size
#     location = image1.location
#
#     left = location['x']
#     top = location['y']
#     right = left+size['width']
#     bottom = top+size['height']
#     # print(left,top)
#
#     browser.save_screenshot('yzm.png')  # 这步就是截图 截整屏
#     image_obj = Image.open('yzm.png')   # 读到内存
#     # print(image_obj)
#     # image_obj.show()  # 展示出来
#     image_obj11 = image_obj.crop((left,top,right,bottom))  # 验证码的图，也是最后比对的图

#4：点击滑动按钮，出现有缺口的图
no_pic = browser.find_element_by_class_name('geetest_slider_button')
no_pic.click()

#5：针对有缺口的图片截图
image_obj22 = get_image(browser)
# image2 = browser.find_element_by_class_name('geetest_canvas_img')
# time.sleep(2)
# size = image1.size
# location = image1.location
# left = location['x']
# top = location['y']
# right = left+size['width']
# bottom = top+size['height']
# browser.save_screenshot('cq_yzm.png')   # 这步就是截图
# image_obj2 = Image.open('cq_yzm.png')   # 读到内存
# # print(image_obj)
# # image_obj.show()  # 展示出来
# # print(image_obj2)
#
# image_obj22 = image_obj2.crop((left,top,right,bottom))  # 带缺口的验证码的图，最后比对的图
# print('image_obj22',image_obj22)  # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=2400x1356 at 0x10374CE80>
# image_obj22.load()[x,y]
# image_obj22.load=== <PixelAccess object at 0x1037de770>

#6：对比两张图片，找出缺口，即滑动的位移
distance1 = get_distance(image_obj11,image_obj22)
print('distance===',distance1)
# def get_instance(image_obj11,image_obj22):
#     start_x = 58
#     threhold = 60  # rgb三个像素的最大偏差
#     for x in range(start_x,image_obj11.size[0]):
#         for y in range(image_obj11.size[1]):
#             # 这里对比的是像素
#             rgb1 = image_obj11.load()[x,y]
#             rgb2 = image_obj22.load()[x,y]
#             # print('rgb1===',rgb1)
#             # print('rgb2===',rgb2)
#             res1 = abs(rgb1[0] - rgb2[0])
#             res2 = abs(rgb1[1] - rgb2[1])
#             res3 = abs(rgb1[2] - rgb2[2])
#             if not (res1 < threhold and res2 < threhold and res3 < threhold):
#                 return x - 7  # 这里其实也是模仿的人的行为。 你不可能完全对准。留7个位移的误差

#7：按照人的行为习惯，把总位移切成一段段(意在：模拟人的滑动习惯)。
# 这里我们的解题思路是： 先匀加速超过验证码一点，再减速拉回来。 依旧是模拟人的行为。
track_dict = get_tracks(distance1)
# def get_tracks(distance):
#     distance += 20  # 这20就是不小心拉多了的二十
#     # 匀加速公式
#     # v = v0+a*t
#     # s = v*t+0.5*a*(t**2)
#     v0 = 0
#     s = 0
#     t = 0.2
#     mid = distance*3/5 # 前 五分之三路段 是匀加速
#     forward_tracks = []
#     while s < distance:
#         if s < mid:
#             a = 2
#         else:
#             a = -3
#         v = v0
#         track = v*t+0.5*a*(t**2)
#         track = round(track)  # 要整数
#         v0 = v + a*t
#         s += track
#         forward_tracks.append(track)  # 向前行进的轨迹
#     back_tracks = [-1,-1,-1,-2,-2,-2,-3,-3,-2,-2,-1]
#     track_dict = {"forward_tracks":forward_tracks,'back_tracks':back_tracks}
#     return  track_dict
#8：按照位移，开始移动。
slider_button = browser.find_element_by_class_name('geetest_slider_button')
ActionChains(browser).click_and_hold(slider_button).perform()
# 先向前移动
forward_tracks = track_dict["forward_tracks"]
back_tracks = track_dict["back_tracks"]
for forward_track in forward_tracks:
    ActionChains(browser).move_by_offset(xoffset=forward_track, yoffset=0).perform()

# 短暂停顿，发现傻逼，移过了
time.sleep(0.2)

# 先向后移动
for back_track in back_tracks:
    ActionChains(browser).move_by_offset(xoffset=back_track, yoffset=0).perform()




ActionChains(browser).move_by_offset(xoffset=-3, yoffset=0).perform()
ActionChains(browser).move_by_offset(xoffset=3, yoffset=0).perform()
time.sleep(0.3)
ActionChains(browser).release().perform()

time.sleep(1000)


browser.quit()