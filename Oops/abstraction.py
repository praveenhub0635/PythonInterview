'''
What is Abstarction?
Hiding the data fromthe user and show the implementation of a particular process is called Abstarction 
'''
#Example
from abc import ABC,abstractmethod

class employee(ABC):
    def emp_id(self,id,age,salary,name):
        pass
class childemployee1(employee):
    def emp_id(self, id):
        print("emp_id is 12345")
emp1 = childemployee1()
emp1.emp_id(id)    
