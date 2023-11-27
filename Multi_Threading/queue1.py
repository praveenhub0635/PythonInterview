'''
get() - The get removes and returns an item from the queue

put() - The put() adds item to  queue

qsize() - The qsize() returns the number of items that are currently in the queue

empty() - The empty() returns True if queue is empty;otherwise,False

full() - The full() returns True if queue is full,otherwise False.

get and put are used in this methods

Queue.queue() -- works based on the ascending order

Queue.lifoQueue() -- get elements snatching form the last like pop() method

Queue.PriorityQueue() -- based on priority

'''
print("<<<<<<<<<<<< Queue Example >>>>>>>>>>>")

import queue

q= queue.Queue()
for k in range(10):
    q.put(k)    

# for k in range(q.size()):
#     print(q.get())
print(q.qsize())
# while not q.empty():
#     print(q.get(),end=' ')