import random
import timeit
from concurrent.futures import ThreadPoolExecutor
from connectionpool import HTTPConnectionPool
import time

pool = HTTPConnectionPool('167.71.233.174', 8080, None, False)
# pool = HTTPConnectionPool('127.0.0.1', 8000, None, 20, False)


def make_reqs(i):
    # print("called", i)
    for _ in range(20):
        res = pool.get_url('/')
        # time.sleep(random.randint(1, 2))
        # print("Request from thread", i, res.status)


start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(make_reqs, range(5))

print("Executed multithreaded pool in", time.time() - start)
