# from selenium import webdriver
# import time
# import datetime
#
# # 运行浏览器
# browser = webdriver.Chrome("D:\PYTHON\爬虫\爬虫课堂\chromedriver.exe")
# # 打开淘宝
# browser.get("https://www.taobao.com")
# # 登录淘宝
# browser.find_element_by_link_text("亲，请登录").click()
#
# time.sleep(10)
# s_url = 'https://m.tb.cn/h.4nEUSCv?sm=8b2387'
# # 输入目标商品网址
# browser.get(s_url)
# while True:
#     # 点击购买按钮
#     try:
#         browser.find_element_by_id("J_LinkBuy").click()
#         break
#     except:
#         print("时间未到")
#
# while True:
#     try:
#         browser.find_element_by_link_text('提交订单').click()
#         print("抢购成功，请尽快付款")
#     except:
#         print("再次尝试提交订单")
#         time.sleep(0.01)

from selenium import webdriver
import time
import datetime


# 打开Chrome浏览器
browser = webdriver.Chrome("/爬虫课堂/selenium自动化/chromedriver.exe")
browser.get("https://www.taobao.com")
# 扫码登陆
browser.find_element_by_link_text("亲，请登录").click()
time.sleep(15)

# 输入目标商品的网址,例如：
browser.get("https://m.tb.cn/h.4nEUSCv?sm=8b2387")

while True:
    # 点击购买按钮
    try:
        browser.find_element_by_id("J_LinkBuy").click()

        break
    except:

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)
        print("时间未到")

# 点击提交订单按钮
while True:
    try:
        browser.find_element_by_link_text('提交订单').click()
        print("抢购成功，请尽快付款")
        time.sleep(100000000000)
    except:
        print("再次尝试提交订单")
        time.sleep(0.01) # 若不满意，可改为0.001
