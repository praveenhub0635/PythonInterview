import time
from threading import Thread

# num=0

# def upgrade(n):
#     while num <4000000000:
#         num = num + 1

# t1 = Thread(target=upgrade,args=(num//2))
# t2 = Thread(target=upgrade,args=(num//2))


# start=time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()

# print("Time taken in seconds-",end - start)


print("<<<<<<<<<<<<<< CALCULATOR EXAMPLE >>>>>>>>>>>>")

def addition():
    time.sleep(5)
    print("Addition Completed:")

def substraction():
    time.sleep(5)
    print("Substraction completed")

t1=Thread(target=addition)
t2=Thread(target=substraction)

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Total Execution time is:",end - start) 

print("<<<<<<< MultiThreading using Class >>>>>>>>")

import threading
class mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    
    def run(self):
        print("thread name is ",self.name)

thread1 = mythread('thread-1')

thread1.start()
thread2 = mythread('thread-2')
thread2.start()


