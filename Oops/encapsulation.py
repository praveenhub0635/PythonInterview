'''
What is Encapsulation?
Encapsulation is the process of binding the data together in a single class.

'''
#Example

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
emp1.earn(  )