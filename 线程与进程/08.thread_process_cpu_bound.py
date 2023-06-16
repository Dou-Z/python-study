import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

# PRIMES = [i for i in range(11233245665797777,112332456657977870)]
PRIMES = [i for i in range(134676,1346760)]
def is_prime(n):
    if n<2:
        return False
    elif n== 2:
        return False
    elif n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n % i ==0:
            return False
    return


def single_thread():
    for number in PRIMES:
        is_prime(number)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)

if __name__ == '__main__':
    print("PRIMEs:",PRIMES)
    start = time.time()
    single_thread()
    end = time.time()
    print("Cost time %f seconds" % (end-start))

    start = time.time()
    multi_thread()
    end = time.time()
    print("Cost time %f seconds" % (end - start))

    start = time.time()
    multi_process()
    end = time.time()
    print("Cost time %f seconds" % (end - start))
