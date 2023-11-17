'''
What are Python Oops concepts?
Python Oops concepts include Class,Object,Method,Inheritance,Ploymorphism,DataAbstraction and Encapsulation.

What are Classes and Objects?
Class: A class is a collection of objects or its a blueprint of an Object defining the common attributes and behavior.

Syntax:
class class1():

Objects:
Objects are instance of a class.It is an entity that has state and behavior.
It is an instance of a class that can access the data
Syntax:
obj=class1()

'''
#Example
class employee():
    def __init__(self,name,age,id,salary):
        self.name = name 
        self.age = age
        self.salary = salary
        self.id = id

emp1 = employee("Praveen",28,80000,1234)
print("The details of employee is:",emp1.name,emp1.age,emp1.salary,emp1.id)

'''
Inheritance:
Exhibiting the properties of parent class to child class is called Inheritance
without any modification.
New class is called derived/child class and one which is derived is called Parent class

Types of Inheritance:
Single Inheritance:
'''

print("<<<<<-----Single Inheritance------>>>>>>")
class employee1():
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class childemployee(employee1):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id

emp1 = employee1("Praveen",28,80000,1234)
print("Single Inheritance",emp1.name,emp1.age,emp1.salary,emp1.id)

print("<<<<<<----Multi Level Inheritance ------>>>>>>>")

class employee1():
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class childemployee1(employee1):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
class childemploye2(childemployee1):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1("Praveen",28,90000,1235)
print("Inheriting",emp1.name)
emp2 = childemployee1("Ram",28,82000,1232)
print("MultiLevel Inheritance",emp2.name,emp2.age,emp2.salary,emp2.id)

print("<<<<<<------Hierarchical Inheritance ------->>>>>>>>>")

class employee1():
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class childemployee1(employee1):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
class childemploye2(employee1):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1("Praveen",28,90000,1235)
print("Inheriting",emp1.name)
emp2 = childemployee1("Ram",28,82000,1232)
print("Hierarchical Inheritance",emp2.name,emp2.age,emp2.salary,emp2.id)

print("<<<<<<----Multiple Inheritance ------->>>>>>>>")

class employee1():
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

class employee2():
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
class childemploye2(employee1,employee2):
    def __init__(self, name, age, salary, id):
        self.name =name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1("Praveen",28,90000,1235)
print("Inheriting",emp1.name)
emp2 = employee2("Ram",28,82000,1232)
print("Multiple Inheritance",emp2.name,emp2.age,emp2.salary,emp2.id)


'''
What is Ploymorphism?
Polymorphism means having many forms i.e., where one task can be performed in differnt ways.
Eg:Operating Systems(windows,ubuntu,mac)
There are two types of ploymorphism
Compile-time Polymorphism
Runtime Polymorphism

'''
print("<<<<<-----Compiletime Polymorphism------>>>>>>>>")


class employee1():
    def name(self):
        print("Harshit is his name")    
    def salary(self):
        print("3000 is his salary")
 
    def age(self):
        print("22 is his age")
 
class employee2():
    def name(self):
        print("Rahul is his name")
 
    def salary(self):
        print("4000 is his salary")
    
    def age(self):
        print("23 is his age")
 
def func(obj):#Method Overloading
    obj.name()
    obj.salary()
    obj.age()
 
obj_emp1 = employee1()
obj_emp2 = employee2()
 
func(obj_emp1)
func(obj_emp2)

print("<<<<<<<<------Run Polymorphism ------->>>>>>>>>>")
class employee1():
    def __init__(self,name,age,salary,id):
        self.name=name
        self.age=age
        self.salary =salary
        self.id=id
def earn(self):
    pass
class childemployee():
    def earn(self):
        print("no money")
class childemployee2():
    def earn(self):
        print("Has Money")
c= childemployee
c.earn(employee1)
d=childemployee2
d.earn(employee1)

'''
What is Encapsulation?
Encapsulation is the process of binding the data together in a single class.

'''
#Example
print("<<<<<<<------ Encapsulation ----------->>>>>>>>>>>")

class employee():
    def  __init__(self):
        self .__maxearn = 100000
    def earn(self):
        print("earning is:{}".format(self.__maxearn))

    def setmaxearn(self,earn): #setter method used for accessing private variables.
        self.__maxearn = earn

emp1 = employee()
emp1.earn()

emp1.setmaxearn(100000)
emp1.earn()

'''
What is Abstarction?
Hiding the data fromthe user and show the implementation of a particular process is called Abstarction 
'''
#Example
print("<<<<<<<------ Abstraction ----------->>>>>>")
from abc import ABC,abstractmethod

class employee(ABC):
    def emp_id(self,id,age,salary,name):
        pass
class childemployee1(employee):
    def emp_id(self, id):
        print("emp_id is 12345")
emp1 = childemployee1()
emp1.emp_id(id)    
