'''
What is Decorator?

Decorators in Python are functions that add functionality to an existing function in Python without 
changing the structure of the function itself.They are represented the @decorator_name in Python and are called as 
bottom-up fashion. 

Why we use Decorator?

We'll use a decorator when we need to change the behavior of a function without changing the function itself.
You can also use when you need to eun the same code on multiple functions
A few good examples are when you want to add logging,authorization,test,performance,perform caching,verify permissions and so on

Write a Syntax of a Decorator?
Syntax:
def decorator_func():
    def wrapper_func():
        return func()
    return wrapper_func()
or
@decorator_func()
def my_func():
    ###execute func
'''

#Decorator Coding Example
def decorator_func(func):
    def wrapper_func():
        print("Wrapper_func Worked")
        return func()
    print("decorator_func Worked")
    return wrapper_func

def show():
    print("Show Worked")

decorator_show= decorator_func(show)
decorator_show()

#Alternative
@decorator_func
def display():
    print('Display Worked')
display()

