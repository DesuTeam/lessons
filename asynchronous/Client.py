import socket
import math
import threading


def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

def worker(lock, start, end, results):
    local = []

    for i in range(start, end):
        if is_prime(i):
            local.append(i)

    lock.acquire()
    results.extend(local)
    lock.release()

def calc_all_primes():
    start = 2
    end = 2000000
    #TODO: Set number of threads dynamicly
    threads_count = 2

    lock = threading.Lock()

    results = []

    threads = []

    for i in range(0, threads_count):
        range_start = int(start + (end - start) * i / threads_count)
        range_end = int(start + (end - start) * (i+1) / threads_count)
        threads.append(threading.Thread(target=worker, args=(lock, range_start, range_end, results)))


    for th in threads:
        th.start()


    for th in threads:
        th.join()

    #print(results)


def main():
    calc_all_primes()
    return None
    sock = socket.socket()


    sock.connect(('localhost', 9090))

    for p in primes_gen(2000):
        sock.send(str(p).encode())
    sock.close()



main()
