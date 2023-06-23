import urllib.request
import time


url = 'http://167.71.233.174:8080'
start = time.time()
for i in range(100):
    response = urllib.request.urlopen(url)
print("Executed single threaded non-pool in", time.time() - start)
