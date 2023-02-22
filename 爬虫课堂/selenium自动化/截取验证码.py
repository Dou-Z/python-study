from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
# driver = webdriver.Chrome()

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# browser.get('https://www.baidu.com')
browser.get('http://182.140.244.7/#/dashboard/overview')
time.sleep(3)

browser.get_screenshot_as_file(r'C:\Users\douz\Desktop\pic\baidu.png')


# 或者
# driver.save_screenshot('full_snap.png')
# page_snap_obj=Image.open('full_snap.png')
from PIL import Image


def get_snap(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    img = driver.find_element_by_class_name('code')
    time.sleep(2)
    location = img.location
    print(location)
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    image_obj.show()
    return image_obj  # 得到的就是验证码


print(get_image(browser))