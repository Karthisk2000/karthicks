import threading

def func1():
    print('function 1')

def func2():
    print('function 2')

t1 = threading.Thread(name='my first thread',target = func1)
t2 = threading.Thread(target = func2)

t1.start()
t2.start()
print(t1.name)