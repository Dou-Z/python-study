import multiprocessing
import time
import threading

# CPU密集计算demo
def square_sum(n):
    return sum(i*i for i in range(1, n+1))

def multi_thread_square_sum(n, num_threads):
    chunk_size = n // num_threads
    results = [0] * num_threads
    threads = []
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i+1) * chunk_size
        if i == num_threads - 1:
            end = n
        t = threading.Thread(target=lambda idx, start, end: results.__setitem__(idx, square_sum(end-start+1)), args=(i, start, end))
        print(t,t.name)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(results)

def calc_sum(idx, start, end, result):
    result[idx] = square_sum(end-start+1)

def multi_process_square_sum(n, num_processes):
    chunk_size = n // num_processes
    results = multiprocessing.Array('i', num_processes)
    print(results.__setitem__)
    processes = []
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i+1) * chunk_size
        if i == num_processes - 1:
            end = n
        p = multiprocessing.Process(target=calc_sum, args=(i, start, end, results))
        print(i, start, end, results)
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return sum(results)

if __name__ == '__main__':
    start_time = time.time()
    # result = square_sum(100000000)
    '''
    Result: 333333338333333350000000
    Time used: 10.171570301055908 seconds
    '''

    result = multi_process_square_sum(100000000, 4)
    '''
    Result: 8270890368
    Time used: 4.134672164916992 seconds
    '''
    # result = multi_thread_square_sum(100000000, 4)
    '''
    Result: 20833334583333350000000
    Time used: 9.288935661315918 seconds
    '''
    end_time = time.time()
    print('Result:', result)
    print('Time used:', end_time - start_time, 'seconds')


