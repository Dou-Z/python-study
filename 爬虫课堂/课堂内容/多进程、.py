# import os
#
# print('',os.getpid())		#查看子进程
# print('',os.getppid())		#查看父进程

import os
from multiprocessing import Process
import time

def main():
    p1 = Process(target=demo1)
    p2 = Process(target=demo2)
    p1.start()
    p2.start()
    print('主进程')
    print('子进程PID：', os.getpid(), '主进程PPID', os.getppid())
    # p1.join()
    # p2.join()

def demo1():
    print('子进程1')
    print('子进程PID：',os.getpid(),'主进程PPID',os.getppid())
    time.sleep(200)

def demo2():
    print('子进程2')
    print('子进程PID：',os.getpid(),'主进程PPID',os.getppid())
    time.sleep(200)

# if __name__ == '__main__':
#     main()

import os
from multiprocessing import Process

def child_process_func(name):
    print('当前执行的进程是子进程，进程编号是{}，父进程编号是{}，当前子进程编号是{}'.format(os.getpid(),os.getppid(),os.getpid()))


# if __name__ == '__main__':
#     #创建子进程
#     print('父进程id',os.getpid())
#     cp = Process(target=child_process_func,args=('子进程123',))
#
#     #调用
#     cp.start()
#     print(cp.name,cp.pid)
#
#     cp.join()       #等待子进程执行结束才结束父进程
#
#     print('结束主进程')
#     #exit（）

import time
import os
from multiprocessing import Pool


def work(times):
    print('这是第{}次任务，由进程编号{}的进程来完成'.format(times,os.getpid()))
    time.sleep(1)       #放慢速度，看一下效果

# if __name__ == '__main__':
#     pool = Pool(3)
#     for i in range(10):
#         pool.apply_async(work,args=(i,))
#
#     pool.close()            #关闭进程池
#     pool.join()            #等待子进程执行结束才结束父进程

# from multiprocessing import Queue
#
# que = Queue(3)		#设置队列的最大容量
#
# que.put(1)			#储存数据
#
# print(que.get())	#读取数据

# 开启进程的第一种方式

# from multiprocessing import Process
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':  # windows下开启进程的指令需要放在main下面
#     p = Process(target=task,args=('子进程1',))  # target代表去执行一个任务，如果是加括号的话相当于立马就执行了
#     p.start()
#     print('主进程')

from multiprocessing import Pool,Manager
import time
import os



def read(que):
    for i in range(10):
        print('获取数据{}'.format(que.get()))


def write(que):
    print('启动进程,当前id是{},父进程id是{}'.format(os.getpid(),os.getppid()))
    for i in range(10):
        que.put(i)

# if __name__ == '__main__':
#     print('当前进程id',os.getpid())
#     pool = Pool()       #创建一个进程池
#     q = Manager().Queue()       #创建一个队列
#     print(q)
#
#     pool.apply_async(write,args=(q,))      #创建进程池中的进程
#     time.sleep(0.5)
#     pool.apply_async(read,args=(q,))
#     pool.close()        #关闭进程
#     pool.join()     #保护