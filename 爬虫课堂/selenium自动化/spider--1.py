# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# import time
# driver = webdriver.Chrome()
#
# url = 'https://dc.simuwang.com/'
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
# time.sleep(1)
# driver.get(url)

"""无界面模式，后台运行"""
# 第一种
# from selenium import webdriver
# # 加载配置
# from selenium.webdriver import ChromeOptions
#
# # driver = webdriver.Chrome()
# # 设置无界面浏览的配置
# option = ChromeOptions()
# # 无界面模式设置
# option.headless = True
# # 创建谷歌浏览driver对象
# driver = webdriver.Chrome(options=option)
# s_url = 'https://www.baidu.com'
# driver.get(s_url)
# html = driver.page_source
# print(html)

# 第二种
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions
# option = ChromeOptions()
# option.add_argument('--headless')
# driver = webdriver.Chrome()
# s_url = 'https://www.baidu.com'
# driver.get(s_url)
# html = driver.page_source
# print('================================',html)


from selenium import webdriver
import time,random

driver = webdriver.Chrome()
driver.maximize_window() # 窗口最大化
# driver.minimize_window() #窗口最小化
one_url = 'https://www.baidu.com'
two_url = 'https://www.CSDN.net'
driver.get(one_url)
# js打开窗口

js = f'window.open("{two_url}")'
driver.execute_script(js)
# 获取所有浏览器窗口
win = driver.window_handles
print(win)
time.sleep(2)
# # 窗口切换
driver.switch_to.window(win[0])
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('迪丽热巴')

# click() 点击操作
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(2)
driver.switch_to.window(win[1])

driver.find_element_by_css_selector('#floor-nav_557 > div > div > div > ul > li:nth-child(1) > a').click()
time.sleep(5)
for i in range(5):
    js = 'scrollTo(0,{})'.format(500*i)
    # execute_script 执行js代码
    driver.execute_script(js)
    time.sleep(random.randint(1,3))
    print(f'滑动第{i}次')








"""标签定位方法"""

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# url = 'https://www.baidu.com'
# driver.get(url)
# id 定位
# send_key() 赋值，传入值
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_class_name('s_ipt').send_keys('迪丽热巴')
# driver.find_element_by_css_selector('#kw').send_keys('css定位')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('xpath定位')

