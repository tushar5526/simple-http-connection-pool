from connectionpool import HTTPConnectionPool
import time

pool = HTTPConnectionPool('167.71.233.174', 8080)
start = time.time()
for i in range(100):
    response = pool.get_url('/')
print("Executed single threaded POOL in", time.time() - start)
