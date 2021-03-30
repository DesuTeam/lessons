import socket
import math
import multiprocessing
import functools


def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


def worker(queue: multiprocessing.Queue, work_range):
    local = []

    for i in work_range:
        if is_prime(i):
            local.append(i)

    queue.put(local)


def calc_all_primes():
    start = 2
    end = 2000000
    # TODO: Set number of processes dynamically
    processes_count = 16

    processes = []

    queue = multiprocessing.Queue(maxsize=processes_count)
    for i in range(0, processes_count):
        range_start = int(start + (end - start) * i / processes_count)
        range_end = int(start + (end - start) * (i + 1) / processes_count)
        processes.append(multiprocessing.Process(target=worker, args=(queue, range(range_start, range_end))))

    for process in processes:
        process.start()

    all_primes = []
    for i in range(0, processes_count):
        all_primes.extend(queue.get())

    for process in processes:
        process.join()

    return all_primes


def main():
    calc_all_primes()
    return None
    sock = socket.socket()

    sock.connect(('localhost', 9090))

    for p in primes_gen(2000):
        sock.send(str(p).encode())
    sock.close()


main()
