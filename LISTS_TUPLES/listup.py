''' What do you mean by list?
List is a datatype which is mutable and can be used as a Container.
Container:we can insert any datatype and remove any datatype.List usually has two blocks of memeory 
where one is fixed and other canbe used to change.
A List in Python:
Insertion order is preserved 
Element can be accessed using indexes
Element can be insert,remove or replace.
Lists are Growable 

Syntax: list = [] or list1 = list()

What do you mean by Tuple?
Tuple can also used as Container but it is IMMUTABLE.
Insertion order is preserved 
Tuples are not Growable
Duplicate data is allowed 
Heterogenious data is allowed
Elements can't be insert, remove or replace.

Syntax: Tuple = () or tuple1 = tuple()
What is the differnce between a LIST and TUPLE ?'''

# To get the size of List and Tuple ?
list1 = []
tuple1 = ()
print(type(list1))
print(list1.__sizeof__())

print(type(tuple1))
print(tuple1.__sizeof__())

print("<<<<-------------->>>>>")

list2 = [1,2,3]
tuple2 = (4,5,6)

print(type(list2))
print(list2.__sizeof__())

print(type(tuple2))
print(tuple2.__sizeof__())