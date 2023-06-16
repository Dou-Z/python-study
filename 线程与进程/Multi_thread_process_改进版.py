import time
import threading
import multiprocessing

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
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(sorted(results))

def multi_process_square_sum(n, num_processes):
    chunk_size = n // num_processes
    results = multiprocessing.Array('i', num_processes)
    processes = []
    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i+1) * chunk_size
        if i == num_processes - 1:
            end = n
        p = multiprocessing.Process(target=calc_sum, args=(i, start, end, results))
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return sum(sorted(results))

def calc_sum(idx, start, end, result):
    result[idx] = square_sum(end-start+1)

if __name__ == '__main__':
    num_tests = 10
    num_threads = 4
    num_processes = 4
    n = 100000000

    # single thread
    single_thread_times = []
    for i in range(num_tests):
        start_time = time.time()
        result = square_sum(n)
        end_time = time.time()
        single_thread_times.append(end_time - start_time)
    single_thread_time = sum(single_thread_times) / num_tests
    print('Single thread result:', result)
    print('Single thread time:', single_thread_time)

    # multi-thread
    multi_thread_times = []
    for i in range(num_tests):
        start_time = time.time()
        result = multi_thread_square_sum(n, num_threads)
        end_time = time.time()
        multi_thread_times.append(end_time - start_time)
    multi_thread_time = sum(multi_thread_times) / num_tests
    print('Multi-thread result:', result)
    print('Multi-thread time:', multi_thread_time)

    # multi-process
    multi_process_times = []
    for i in range(num_tests):
        start_time = time.time()
        result = multi_process_square_sum(n, num_processes)
        end_time = time.time()
        multi_process_times.append(end_time - start_time)
    multi_process_time = sum(multi_process_times) / num_tests
    print('Multi-process result:', result)
    print('Multi-process time:', multi_process_time)
