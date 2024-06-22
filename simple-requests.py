import urllib.request
import time


url = 'http://167.71.232.193:80'

start = time.time()

for i in range(100):
    response = urllib.request.urlopen(url)

print("Executed single threaded non-pool in", time.time() - start)
