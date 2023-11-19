'''
Memory Management:
Types of memory:
Stack Memory
Private Heap Memory

References Methods
Call-()
stack memory

Value Object:
Private Heap
Eg:
x=5 (x will stored in stack memory and 5 is object and will store in Private Heap)

'''
#Examples:
x=5
print(type(x))
print(id(x))

y="Praveen"
print(type(y))
print(id(y))

'''
Memory Allocation
------>How is memory managed in Python?

Memory Management in python involves heap containing all Python objects
and datastructures.Interpreter takes care of Python Heap and that the 
programmer has no access to it.

The allocaation of heap space for Python objects is done by Python memory manager.
The core API pf Python provides some tools for the programmer to code and more robust program

Python also has a build-in garbage collector which recycles all the unused memory.When an object
is no longer referenced by the program,the heap space it occupies can be freed.The garbage collector 
determines objects which are no longer referenced by the program frees the occupied memory
and make it available to the heap space.

The gc module defines functions to enable/disable garbage collector
gc.enable()-Enables automatic garbage collection.
gc.disable() - Disables automatic garbage collection.

------>What is Garbage Collector?
Python deletes unwanted objects(built-in types or class instances) automatically to free the memory
space

The process by which Python Periodically frees and reclaims block of memory that no longer are in use
is called Garbage Collection.

Python Garbage collector runs during the program execution and is triggered when an object's reference
count reaches zero

An object reference count changes as the number of references referring that object changes.

----->What is Duck Typing and Why Python is called as Dynamic Typed Programming Language?

Python don't have any problem even if we don't declare the type of variable.

It states the kind of variable in the runtime of the program.

Python also take cares of the memory management which is crucial in Programming.So Python is Dynamically 
typed Language

Difference between stack memory and heap memory?
Stack Memory: The methods/method calls and the references are stored in stack memory.
Heap Memory: All the values Objects are stored in Private Heap Memory
'''
#Example
def func2(z):
    q=z+10
    return q

def func1(x):
    z=x+5
    p=func2(z)
    return p

#main
x=5
y=func1(x)
print(y)
#o/p = 20

'''
------>> What is Module?
    The module is a simple Python file that contains collections of functions and global variables and with having a 
    .py extension file.

    A module is a single file that are imported under one import and are used.

    It is an executable file and to organize all the modules we have the concept called Package.
    in Python
    E.g,
        import <my_module>
        import json

------->> What do you mean by Package in Python?
    The Package is a simple directory having collections of modules.

    The directory contains Python modules and also having __init__.py file by which
    the interpreter interprets it as a package.

    The package is simply a namespace.

    The Package also contains sub-packages inside it.

A Package is a collection of modules in directories that give a package hierarchy

E.g.
    from my__package.abc import a

------->> What do you mean by library in Python ?

    Library is an umbrella term referring to a reusable chunk of code.

    A Package is a collection of modules, a library is a collection of packages.
    
    Generally, A Python library contains collection of related modules and packages.
    
    We create Python libraries to share reusable code with the community.
E.g.
    import <my__library>
    import numpy

------>> What is the difference between Module,Package and Library?

Examples of Module,Package and Library?
Module              Package             Library
--- random        --- Numpy             --- Matplotlib
    os                pandas            --- pygame
    json              pytest            --- Beautiful Soup
    html              Scipy             --- Requests 
    datetime          PyTorch
    re                Pendulum
                      Pywin32
'''