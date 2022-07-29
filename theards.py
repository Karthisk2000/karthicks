import threading
t=threading.currentThread() #print the thread name

print('current thread', t)
print('thread name:', t.name)
print('thread identifier:', t.ident)
print('is the thread alive:', t.is_alive())
t.name='mythread'
print('after name change:', t.name)
