import urllib2
import time
from threading import Thread


n_thread = 10000
response_time = []
threads = []


def myfunc(i):
	url = "http://localhost/500b.html"
	proxy_handler = urllib2.ProxyHandler({})
	opener = urllib2.build_opener(proxy_handler)
	start = time.clock()
	r = opener.open(url).read()
	end = time.clock()
	duration = end-start
	response_time.append(duration)
	

for i in range(n_thread):
	t = Thread(target=myfunc, args=(i,))
	threads.append(t)

nah = 0	
for x in threads:
	nah = nah +1
	print nah
	x.start()
	
for x in threads:
	x.join()
	

sum = 0	
for i in range(n_thread):
	sum = sum + response_time[i]
	
print sum / n_thread