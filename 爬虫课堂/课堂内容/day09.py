from multiprocessing import Process
import time

def func(x):
    start_time = time.time()
    for i in range(x):
        print('结果是：',i)
    end_time = time.time()
    print(start_time - end_time)

if __name__ == '__main__':
    # 进程的创建
    # target = func func代表进程执行的函数，做什么任务
    # args=(3,) kwargs={'x':4}   参数传递的两种方式
    # start（）进程开启，执行
    Process(target=func,args=(3,)).start()
    Process(target=func,kwargs={'x':4}).start()
