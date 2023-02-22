from pytesseract import pytesseract

# import pytesseract
# from PIL import Image
#
# test = pytesseract.image_to_string(Image.open('1.png'),lang='chi_sim')
# print(test)


# 尖叫数据
"""
AppCode：	2016ACDFA6D8676030293BD2549EE90C
AppKey：	AKIDb043bab5e66c30164f5e21bd2bedecd4
AppSecret：	ddbd5a9876ee50ec71441dc0df8c0ebb
"""

# import urllib, urllib2, sys
#
# host = 'http://apigateway.jianjiaoshuju.com'
# path = '/api/v_1/yzm.html'
# method = 'POST'
# appcode = '你自己的AppCode'
# appKey = '你自己的AppKey'
# appSecret = '你自己的AppSecret'
# querys = ''
# bodys = {}
# url = host + path
#
# bodys['v_pic'] = '''v_pic'''
# bodys['v_type'] = '''v_type'''
# post_data = urllib.urlencode(bodys)
# request = urllib2.Request(url, post_data)
# request.add_header('appcode', appcode)
# request.add_header('appKey', appKey)
# request.add_header('appSecret', appSecret)
# # //根据API的要求，定义相对应的Content-Type
# request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
# response = urllib2.urlopen(request)
# content = response.read()
# if (content):
#     print(content)

from requests_html import HTMLSession
from fake_useragent import UserAgent
import base64

ua = UserAgent()
session = HTMLSession()
with open('./验证码图/2.png', 'rb')as f:
    img_data = f.read()
    base64_data = base64.b64encode(img_data).decode()
    # print(base64_data)

data = {
    'v_pic': base64_data,
    'v_type': 'n4',
}

headers = {
    'AppCode': '2016ACDFA6D8676030293BD2549EE90C',
    'AppKey': 'AKIDb043bab5e66c30164f5e21bd2bedecd4',
    'AppSecret': 'ddbd5a9876ee50ec71441dc0df8c0ebb',
    'user-agent': ua.chrome
}

start_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
response = session.post(start_url, headers=headers, data=data)
print(response.json())


"""定时任务线程原理"""
# 1.APScheduler-BackgroundScheduler的基本用法
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.executors.pool import ThreadPoolExecutor
# import time
#
# # 1.定义执行器
# executors = {
#     'default': ThreadPoolExecutor(max_workers=10)
# }
#
# # 2.创建调度器
# scheduler = BackgroundScheduler(executors=executors)
#
#
# # 3.定义定时任务函数
# def print_test():
#     print(11111)
#
#
# # 4.添加定时任务
# scheduler.add_job(print_test, 'interval', seconds=3)
#
# # 5.启动调度器，不阻塞
# scheduler.start()
#
# # 6.手动添加代码，防止程序退出
# # 执行5遍，3s执行一次，for循环速度快，不添加睡眠，定时程序不执行
# for i in range(5):
#     time.sleep(3)


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
# 1.定义执行器
executors = {
    # default表示执行定时任务时，使用进程的方式
    # 3表示在同一时刻，最多只有3个进程同时执行
    'default': ProcessPoolExecutor(3)
}
# 2.使用上面的执行器，创建调度管理对象，使用单独运行的方式
scheduler = BlockingScheduler(executors=executors)


# 3.定义定时任务函数
def print_test():
    print('定时任务执行成功')
    # main1()


# 4.添加任务,使用date指定在某个时间执行
# 使用run_date指定运行的时间
scheduler.add_job(print_test, 'date', run_date='2021-3-24 12:22:00')

# 指定每天15：36运行
# scheduler.add_job(print_test, 'cron', hour=12, minute=9)

# 使用interval 指定在开始时间到结束时间
# 从start_date开始，到end_date结束，每隔3秒中执行一次
# scheduler.add_job(print_test,
#                   'interval',
#                   seconds=3,
#                   start_date='2021-3-24 11:20:00',
#                   end_date='2021-3-24 11:21:00')

if __name__ == '__main__':
    scheduler.start()