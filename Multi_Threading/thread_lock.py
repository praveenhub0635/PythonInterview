'''
Thread Lock
Exmaples: Bus Tickets or Movie Tickets
'''
print("<<<<<<<<< Thread Lock Example >>>>>>>>>>>")
import threading
import time
def task(name):
    lock.acquire()
    print(name,"running...")
    time.sleep(5)
    print(name,"Completed...")
    lock.release()
    print(name,"Lock released...")
    print("<<<<<<<< Initiating >>>>>>>>>>>")

lock = threading.Lock()

t1 = threading.Thread(target=task,args=("thread-1",))

t2 = threading.Thread(target=task,args=("thread-2",))

t3 = threading.Thread(target=task,args=("thread-3",))

t4 = threading.Thread(target=task,args=("threading-4",))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()