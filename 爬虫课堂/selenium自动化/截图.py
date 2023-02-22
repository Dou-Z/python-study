# 应用1：save_screenshot 使用当前时间作为文件名
from selenium import webdriver
from time import sleep, strftime, localtime, time

driver = webdriver.Chrome()  # 打开浏览器
driver.get("https://www.baidu.com/")  # 跳转至测试页面
sleep(1)
element = driver.find_element_by_id("kw")  # 定位输入框
element.send_keys("自动化测试")  # 输入内容
sleep(1)
file_name = strftime("%Y%m%d-%H%M%S", localtime(time())) + ".png"
driver.save_screenshot(file_name)  # 截屏
sleep(2)

driver.quit()  # 关闭浏览器
