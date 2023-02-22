# from multiprocessing import Process
# import time
#
# def index(num):
#     start_time = time.time()
#     for i in range(num):
#         print('结果是：',i)
#
#     end_time = time.time()
#     print(start_time-end_time)
#
#
# if __name__ == '__main__':
#     Process(target=index,args=(3,)).start()
#     Process(target=index,kwargs={'num':3}).start()

"""进程队列"""
# from multiprocessing import Process
# from multiprocessing import JoinableQueue as Queue
#
# class Love(object):
#     def __init__(self):
#         self.q = Queue()
#
#     def parse_data(self):
#         data = '第{}天-------love'
#         for i in range(1,101):
#             self.q.put(data.format(i))
#
#     def func_1(self):
#         while True:
#             result = self.q.get()
#             print(result)
#
#     def run(self):
#         m1 = Process(target=self.parse_data)
#         m2 = Process(target=self.func_1)
#         m1.start()
#
#         m2.daemon = True  ## 设置守护进程
#
#         m2.start()
#
#         m1.join()
# if __name__ == '__main__':
#     ly = Love()
#     ly.run()


from multiprocessing import Process,Pool
import time,random,os

def worker(msg):
    start_time = time.time()
    print('%s 开始执行，进程编号为%d' %(msg,os.getpid()))
    time.sleep(random.random()*2)
    print('-=-=-=-=-=-=-=-=-=-=-=-=')
    print(random.random() * 2)
    stop_time = time.time()
    print(msg,'执行完毕，花费：%0.2f'%(start_time-stop_time))

if __name__ == '__main__':
    # 创建一个最大进程数量为3的进程池
    po = Pool(3)
    for i in range(0,10):
        """
        apply_async: 非阻塞的形式运行我们的进程，
        # 进程之间没有联系 -- 进程不共享全局变量
        """
        po.apply_async(worker,args=(i,))
    print('开启-----')
    po.close()
    po.join()
    print('关闭------')