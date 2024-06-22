from concurrent.futures import ThreadPoolExecutor
import time
import urllib.request

url = 'http://167.71.232.193:80'


def make_reqs(i):
    # print("called", i)
    for _ in range(5):
        response = urllib.request.urlopen(url)


start = time.time()
with ThreadPoolExecutor(max_workers=15) as executor:
    executor.map(make_reqs, range(40))

print("Executed multithreaded pool in", time.time() - start)
