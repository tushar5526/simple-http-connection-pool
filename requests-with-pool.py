from connectionpool import HTTPConnectionPool
import time

pool = HTTPConnectionPool('167.71.232.193', 80)

start = time.time()
for i in range(100):
    response = pool.get_url('/')

print("Executed single threaded POOL in", time.time() - start)
