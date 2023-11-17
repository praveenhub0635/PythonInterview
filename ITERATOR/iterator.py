'''
What do you mean by an Iterator in Python? Explain with example?

An Iterator is an object which contains a countable number of values and it is used to iterate objects like
lists,tuples,sets etc.,

Iterators are used mostly to iterate or convert other objects to an iterator 
using iter() function

Iterator uses iter() and next() functions

Lists,Tuples,Dictionaries and sets are all iterable Objects.They are Iterable containers which 
can get an iterator form.

Tchnically, in Python, an iterator is an object which implements 
the iterator protocol,which consists of the methods __iter__() and __next__()

Every Iterator is not a generator
'''

#Example

iter_list = iter(['A','B','C'])

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

'''
Why we don't call a List,Tuple,Dict or Set an Iterator?

Lists,Tuple,Dict and Sets are all iterable objects and not an Iterator.
They are iterable containers which you can get an iterator from.
We convert the iterable objects into an iterator using "iter()" 

'''

#Example

list1 = [1,2,'Praveen',True]

print(next(list1))

'''
Can we use next() with list to Access its element?
List is an Iterable objects.

Only Iterator can use next() function to access its elements and not iterab;e objects.

Lists are iterable containers which you can get an iterator from.

We can convert the list into an iterator using "iter()"

Without using iter() script throw an Type error

------>What happens if we try to access element which is not in the range of list?
it will throw Stop Iteration error.
'''
