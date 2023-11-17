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

