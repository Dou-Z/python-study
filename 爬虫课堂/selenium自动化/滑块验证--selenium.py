"""滑块验证码的突破"""

from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
"""登陆的url"""
s_url = 'https://passport.jd.com/new/login.aspx?'
"""窗口最大化"""
driver.maximize_window()
"""隐士等待"""
driver.implicitly_wait(10)
"""加入放检测"""
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
"""访问"""
driver.get(s_url)
"""定位标签"""
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element_by_id('loginname').send_keys('13193709088')
driver.find_element_by_id('nloginpwd').send_keys('cx13193709088')
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# print(driver.page_source)
"""方法一：只能滑动固定距离，实用性较差"""
# if '向右滑动完成拼图' in driver.page_source:
#     div_size_obj = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[2]')
#     div_size = div_size_obj.size
#     print('div_size',div_size)
#     button = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
#     # 进行实例化
#     button_location = button.location
#     print('button_location',button_location)
#     x_location = div_size['width']
#     y_location = button_location['y']
#     print(x_location,y_location)
#     # ActionChains ：可以控制鼠标，鼠标按钮操作，上下文切换等等
#     action = ActionChains(driver)
#     action.click_and_hold(button).perform()
#     action.move_by_offset(x_location,190)
#     action.release().perform()
"""第二种：通过循环处理，需要滑动的距离不稳定，成功率低"""

button = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')

action = ActionChains(driver)
x = 0
is_running = True
while is_running:
    if x < 200:
        is_running = False
        action.click_and_hold(button).move_by_offset(x).perform()
        x += 50
"""方法三：通过及计算距离，滑动滑块，成功率低，代码复杂"""
"""四：通过打码平台，突破验证码"""
"""行为式验证码（点选图案、文字）"""




# 以12306登录
# from selenium import webdriver
# driver = webdriver.Chrome()
# from selenium.webdriver import ActionChains
# import time,random,base64
# from requests_html import HTMLSession
# session = HTMLSession()
#
# surl = 'https://kyfw.12306.cn/otn/resources/login.html'
# driver.maximize_window()
# driver.get(surl)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
#
# driver.find_element_by_css_selector('body > div.login-panel > div.login-box > ul > li.login-hd-account > a').click()
# driver.find_element_by_id('J-userName').send_keys('13193709088')
# driver.find_element_by_id('J-password').send_keys('Cx13193709088')
# time.sleep(random.randint(1,2))
# """窗口向下滑动"""
# js = 'scrollTo(0,500)'
# driver.execute_script(js)
# time.sleep(random.randint(1,2))
# """定位验证码标签"""
# img = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
# img.screenshot('验证码12306.png')
# """对接打码平台"""
# headers = {
#     'AppCode':'2016ACDFA6D8676030293BD2549EE90C',
#     'AppKey':	'AKIDb043bab5e66c30164f5e21bd2bedecd4',
#     'AppSecret':	'ddbd5a9876ee50ec71441dc0df8c0ebb',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
# }
# post_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzmCrd.html'
# with open('验证码12306.png','rb') as f:
#     base64_data = base64.b64encode(f.read()).decode()
#     data = {
#         'v_pic':base64_data,
#         'v_type':'crd'
#     }
# respon = session.post(post_url,headers=headers,data=data).json()
# print(respon)
# v_code = respon['v_code']
# for code in v_code.split('|'):
#     # 获取x坐标
#     x = int(code.split(',')[0])
#     # 获取y坐标
#     y = int(code.split(",")[1])
#     # 执行点击
#     ActionChains(driver).move_to_element_with_offset(img,x,y).click().perform()
# """点击登录"""
# time.sleep(random.randint(1,2))
# driver.find_element_by_xpath('//*[@id="J-login"]').click()
# """处理滑块验证"""
# driver.implicitly_wait(10)
# div_size_obj = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
# # 获取宽高
# div_size = div_size_obj.size
# # 定位滑块按钮
#
# button = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# # 实例化
# button_location = button.location
#
# # 鼠标推动
# # 计算拖动距离
# y = button_location['y']
# # print(y)
# # 鼠标的拖动操作
# # ActionChains：可以控制鼠标，鼠标按钮操作，上下文切换
# action = ActionChains(driver)
# action.click_and_hold(button).perform()
# action.move_by_offset(332,0)
# action.release().perform()




