from threading import Thread

def myfunc():
	while True:
		a = 1
		
n = 0
while True:
	n = n + 1
	t = Thread(target=myfunc)
	t.start()
	print n