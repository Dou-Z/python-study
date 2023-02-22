# from threading import Thread
# import time
#
# def index(x,y):
#     print(f'我是{x}，你是{y}')
#
# def run():
#     list_1 = ['q','w','e','r','1','2','3','4']
#     num = len(list_1)//2
#     list_2 = list_1[:num]
#     list_3 = list_1[num:]
#     Thread(target=index,args=(list_1[1],list_2[1])).start()
#     Thread(target=index,args=('q','k')).start()
#
# run()

"""线程间共享全局变量（代码解析）"""

# from threading import Thread
# import time
#
# def func(x):
#
#     x.append(4)
#     print('我是func', x)
# def function(x):
#     print('我是function', x)
#
# x = [1, 2, 3]
#
# if __name__ == '__main__':
#     Thread(target=func, args=(x,)).start()
#     Thread(target=function, args=(x,)).start()
from multiprocessing import pool

"""阻止线程间共享全局变量"""

# from threading import Thread
# import threading
# import time
#
# x = ['a', 'b', 'c']
#
#
# def func(num):
#     # global x
#     # mutex.acquire()  # 上锁
#     time.sleep(2)
#     for i in range(num):
#         x.append(i)
#     print('我是func', x)
#     # mutex.release()  # 解锁
#
#
# def function(num):
#     # global x
#     # mutex.acquire()  # 上锁
#     time.sleep(2)
#     for i in range(num):
#         x.append(i)
#     print('我是function', x)
#     # mutex.release()  # 解锁
#
#
# if __name__ == '__main__':
#     mutex = threading.Lock()
#     Thread(target=func, args=(3,)).start()
#     Thread(target=function, args=(5,)).start()
from threading import Thread
from queue import Queue
import time

class Lo(object):
    def __init__(self):
        self.q = Queue()

    def parse_data(self):
        for i in range(101):
            data = f'第{i}天，LLLL'
            time.sleep(1)
            self.q.put(data)
            self.q.join()

    def parse_queue(self):
        while True:
            data = self.q.get()
            print(data)
            self.q.task_done()
    def run(self):
        t1 = Thread(target=self.parse_data)
        t2 = Thread(target=self.parse_queue)
        t1.start()
        #设置守护线程
        t2.daemon = True
        t2.start()

if __name__ == '__main__':
    d = Lo()
    d.run()


# 读写分离  请求与保存分离
# from concurrent.futures import ThreadPoolExecutor
# import threading
# from queue import Queue
# from requests_html import HTMLSession
# from fake_useragent import UserAgent
# from threading import Thread
# import re, os
#
# ua = UserAgent()
# session = HTMLSession()
#
#
# class Bz(object):
#
#     def __init__(self):
#         self.start_url = 'https://konachan.net/post?page={}&tags='
#         self.q=Queue()
#         # 创建一个包含5条线程的线程池
#         self.pool = ThreadPoolExecutor(max_workers=5)
#
#     def thread_start_url(self):
#         self.pool.submit(self.parse_start_url,1,2000,'t1')
#         self.pool.submit(self.parse_start_url,2000,4000,'t2')
#         self.pool.submit(self.parse_start_url,4000,6000,'t3')
#         self.pool.submit(self.parse_start_url,6000,8000,'t4')
#         self.pool.submit(self.parse_start_url,8000,12200,'t5')
#
#         # Thread(target=self.parse_start_url, args=(1, 5001, 't1')).start()
#         # Thread(target=self.parse_start_url, args=(5001, 10000, 't2')).start()
#
#     def parse_start_url(self, start_page, end_page, name_thread):
#         """
#         解析起始的url类地址
#         :return:
#         """
#         # 创建循环记数，统计下载图片张数
#         num = 1
#         headers = {
#             'referer': 'https://konachan.net/post',
#             'user-agent': ua.chrome
#         }
#
#         # 使用循环模拟发送翻页请求
#         for page in range(start_page, end_page):
#             # 发送请求，获取响应
#             response = session.get(self.start_url.format(page), headers=headers)
#             # 解析源码内容
#             html_str = response.content.decode()
#             # 正则提取小型图片url地址,返回一个列表
#             url_list = re.findall("preload\('(.*?)'\);", html_str)
#             # print(url_list)
#             # 方法回调解析
#             self.parse_url_list(url_list, num, name_thread)
#             # 计数累加
#             num += 1
#
#     def parse_url_list(self, url_list, num, name_thread):
#         """
#         解析拼接大型图片url地址
#         :param url_list: 小型图片url地址列表
#         :param num: 循环计数，统计下载图片张数
#         :return:
#         """
#         # 遍历图片列表
#         for url in url_list:
#             # 正则匹配出壁纸属性id
#             img_id = url[40:-4]
#             # url地址拼接，获取大壁纸url
#             next_url = f'https://konachan.net/sample/{img_id}/Konachan.com%20-%20324421%20sample.jpg'
#             print(next_url)
#             # 发送请求，获取二进制响应
#             data = session.get(next_url).content
#             dict_1 = {
#                 'data':data,
#                 'num':num,
#                 'img_id':img_id,
#                 'name_thread':name_thread
#             }
#             self.q.put(dict_1)
#             self.q.join()
#             # 方法回调解析，保存
#
#             # self.save_data(data, num, img_id, name_thraed)
#             # 计数累加
#             # num += 1
#
#     def save_data(self):
#         """
#         保存
#         :param data: 图片二进制数据
#         :param num: 循环计数，统计下载图片张数
#         :param img_id: 保存图片的名称
#         :return:
#         """
#         while True:
#             dict_1 = self.q.get()
#             name_thread = dict_1['name_thread']
#             img_id = dict_1['img_id']
#             data = dict_1['data']
#             num = dict_1['num']
#             # 创建保存壁纸文件夹
#             os_path = os.getcwd() + '/图片/'
#             # 判断改文件夹路径是否存在，不存在就创建
#             if not os.path.exists(os_path):
#                 os.mkdir(os_path)
#             # 壁纸保存
#             with open(os_path + name_thread + '_' + img_id + '.jpg', 'wb')as f:
#                 f.write(data)
#             print(f'第{num}张壁纸下载完成====logging====！！！')
#
#     def run(self):
#         t1 = Thread(target=self.thread_start_url)
#         t2 = Thread(target=self.save_data)
#         t1.start()
#         t2.daemon = True
#         t2.start()
#
# if __name__ == '__main__':
#     b = Bz()
#     b.run()


# 有资源竞争的问题
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
#
#
# # 定义一个准备作为线程任务的函数
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         # 了解
#         # threading.current_thread().name = 'aef'
#         print(threading.current_thread().name + '  ' + str(i))
#         # threading.current_thread() 进行中的进程 代码表示获取进行中的进程名称
#         # print(threading.current_thread().getName() + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
#
# # 创建一个包含3条线程的线程池
# pool = ThreadPoolExecutor(max_workers=3)
#
# # 向线程池提交一个task(任务), 50会作为action()函数的参数
# f1 = pool.submit(action, 5)
#
# # 向线程池再提交一个task(任务), 6会作为action()函数的参数
# f2 = pool.submit(action, 6)
#
# # # 判断future1代表的任务是否结束
# print(f1.done())
# # time.sleep(3)
# #
# # # 判断future2代表的任务是否结束
# # print(future2.done())
# #
# # # 查看future1代表的任务返回的结果
# # print('运行结果', action(5), '\t\n')
# # print('运行结果', f1.result(), '\t\n')
# #
# # # 查看future2代表的任务返回的结果
# # print(future2.result())
#
# # 关闭线程池
# pool.shutdown()


# import json
#
# data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
# print('DATA:', repr(data))
#
# data_string = json.dumps(data)
# print('JSON:', data_string)
# # 结果如下
# # DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
# # JSON: [{"a": "A", "c": 3.0, "b": [2, 4]}]
# print(type(data))
# print(type(data_string))

# import json
#
# data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
# print('DATA:', repr(data))
# print('repr(data)             :', len(repr(data)))
# print('dumps(data)            :', len(json.dumps(data)))
# print('dumps(data, indent=2)  :', len(json.dumps(data, indent=2)))
# print('dumps(data, separators):', len(json.dumps(data, separators=(',', ':'))))

# import json
# data = [ { 'a':'A',  'c':3.0 ,'b':(2, 4)} ]
# print('DATA:', repr(data))
#
# unsorted = json.dumps(data)
# print('JSON:', json.dumps(data))
# print('SORT:', json.dumps(data, sort_keys=True))

# import json
# data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
# print('DATA:', repr(data))
#
# print('NORMAL:', json.dumps(data, sort_keys=True))
# print('INDENT:', json.dumps(data, sort_keys=True, indent=2))


# import json
#
# data = [{'a': 'A', 'b': (2, 4), 'c': 3.0, ('d',): 'D tuple'}]
#
# print('First attempt')
# try:
#     print(json.dumps(data))
# except (TypeError, ValueError) as err:
#     print('ERROR:', err)
#
# print()
# print('Second attempt')
# print(json.dumps(data, skipkeys=True))
