from concurrent.futures import ThreadPoolExecutor
from connectionpool import HTTPConnectionPool
import time

pool = HTTPConnectionPool('167.71.232.193', 80, None, False)


def make_reqs(i):
    # print("called", i)
    for _ in range(5):
        res = pool.get_url('/')


start = time.time()
with ThreadPoolExecutor(max_workers=15) as executor:
    executor.map(make_reqs, range(40))

print("Executed multithreaded pool in", time.time() - start)
