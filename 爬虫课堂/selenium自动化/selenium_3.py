# https://flights.ctrip.com/international/search/oneway-bjs-cgo?depdate=2021-04-05&cabin=Y_S_C_F

from selenium import webdriver
import time
# driver = webdriver.Chrome()
# driver.minimize_window()
# start_url = 'https://mail.163.com/'
# 访问
# driver.get(start_url)
# # 标签的定位
# # driver.find_element_by_name('email').send_keys(123456789)
# # iframe嵌套
# # iframe切换
# time.sleep(1)
# el = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(el)
# driver.find_element_by_name('email').send_keys('doucx2020@163.com')
# driver.find_element_by_name('password').send_keys('dd13193709088')
# driver.find_element_by_id('dologin').click()
# """获取cookie"""
# print(driver.get_cookies())
# cookie_dict = {cook['name']:cook['value'] for cook in driver.get_cookies()}
# print(cookie_dict)
# #
#
# from requests_html import HTMLSession
# session = HTMLSession()
#
#
# headers = {
#     'referer': 'https://mail.163.com/js6/main.jsp?sid=WChPTgEUdKqNNrOiURUUVUxTKjgHzrdI&df=mail163_letter',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
#     # 'Upgrade-Insecure-Requests': '1'
# }
# resp = session.get(start_url,headers=headers,cookies=cookie_dict)
# print(resp.content.decode())

# from selenium import webdriver
# import time
# from requests_html import HTMLSession
# session = HTMLSession()
#
#
# driver = webdriver.Chrome()
# s_url = 'http://www.douban.com'
# driver.get(s_url)
# time.sleep(1)
# el = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(el)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
#
# driver.find_element_by_xpath('//*[@id="username"]').send_keys('13193709088')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('dz123456')
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
# time.sleep(2)
# headers = {
#     # 'Referer':' https://www.douban.com/',
#     'Upgrade-Insecure-Requests':' 1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
# }
#
# cookie_dict = {cook['name']:cook['value'] for cook in driver.get_cookies()}
# ressponse = session.get(s_url,cookies=cookie_dict)
# print(ressponse.content.decode())

"""隐式等待"""
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# driver = webdriver.Chrome()
# # 最多等待10秒，10秒后，没有返回数据报错
# # 一找到，就接着往下运行
# driver.implicitly_wait(10)
# driver.get('https://www.csdn.net')

"""显示等待"""
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# # driver.find_element_by_link_text('人工智能').click()
# WebDriverWait(driver,20,0.5).until(EC.presence_of_all_elements_located((By.LINK_TEXT,'地图')))
"""
在20秒内，每隔0.5秒检查一次通过地图文本定位地图标签
20 等待多少秒
0.5 每隔0.5秒检查一次
"""

"""加代理"""
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# driver = webdriver.Chrome()
#
# option = ChromeOptions()
# option.add_argument('--proxy-server=http://190.82.70.709:80')
# driver = webdriver.Chrome(options=option)
# s_url = 'https://www.youtobe.com'

# driver.get(s_url)

"""替换UA"""
# from fake_useragent import UserAgent
# ua = UserAgent()
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# driver = webdriver.Chrome()
# option = ChromeOptions()
# a = ua.chrome
# print(a)
# option.add_argument('--user-agent={}'.format(a))
# s_url = 'https://www.baidu.com'
# driver = webdriver.Chrome(options=option)
#
# driver.get(s_url)
# agent = driver.execute_script(
#     'return navigator.userAgent'
# )
# print(agent)

"""尖叫数据 图片验证码识别"""
from requests_html import HTMLSession

session = HTMLSession()
from fake_useragent import UserAgent

ua = UserAgent()
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from PIL import Image
import base64

# driver = webdriver.Chrome()
# driver.maximize_window()
# s_url = 'http://www.jianjiaoshuju.com/path/login.htm'
#
# driver.get(s_url)
# driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[1]/input').send_keys('13193709088')
# driver.find_element_by_css_selector('body > div.login-box > div > div.login-form.log-reg-form.f_r > ul > li:nth-child(2) > input').send_keys('cx13193709088')
# """开始截图"""
# driver.save_screenshot('首页.png')
# # 获取验证码标签
# img = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img')
# # 实例化标签对象
# location = img.location
# # 获取标签大小
# size = img.size
# # 获取验证码上下左右的坐标
# left = location['x'] + 320
# top = location['y'] + 120
# right = left + size['width']
# bot = top + size['height']
# """二次截图"""
# photo = Image.open('../爬虫案例/首页.png')
# img_obj = photo.crop((left,top,right,bot))
# img_obj.save('验证码.png')

# with open('./验证码.png', 'rb')as f:
#     img_data = f.read()
#     base64_data = base64.b64encode(img_data).decode()
#
#
# headers = {
#     'AppCode': '2016ACDFA6D8676030293BD2549EE90C',
#     'AppKey': 'AKIDb043bab5e66c30164f5e21bd2bedecd4',
#     'AppSecret': 'ddbd5a9876ee50ec71441dc0df8c0ebb',
#     'user-agent': ua.chrome
# }
# data = {
#     'v_pic': base64_data,
#     'v_type': 'ne4'
# }
# url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
#
# json_data = session.post(url, headers=headers, data=data).json()
# print(json_data)
