'''
Comprehensions in Python provide us with a short and concise way to construct new sequences 
(such as list,set,dictionary etc.,) using sequences which have alredy been defined.

We can create a new sequences using a given python sequence.
This is called Comprehension.

Python suports four types of Comprehension.
List Comprehensions
Tuple Comprehensions
Set Comprehensions
Generator Comprehensions

Why we use Comprehensions?
Comprehension is generally more compact and faster than normal functions and loops for creating list.
In addition to standard list creation,list comprehensions are also be used for mapping and filtering.
You don't have to use a different approach for each scenario.
However we should avoid writing very long list comorehensions in one line to ensure that code is user-friendly.  

'''
#Create a list of  Odd Number sfrom 0 to 20

l=[]
for i in range(20):
    if i%2 != 0:
        l.append(i)
print("Common Way",l)

ls =[i for i in range(20) if  i%2!=0]
print("Comprehension Way",ls)

#Dict Comprehension
d={}
for i in range(0,10):
    d[i]=i*i
print("Common Way oF Dictionary",d)

d1={i:i*i for i in range(0,10)}
print("Dict Comprehension",d1)

# Set Comprehension

s1=[1,2,3,4,5,6,1,4]
s2=set()
for i in s1:
    if i % 2 !=0:
        s2.add(i)
print("Common way of Set",s2)

s1 = {1,2,3,4,5,6,7,8}
s2 = {i for i in s1 if i %2 != 0}
print("Set Comprehension",s2)

#Generator Comprehension...
def generator1(list1):
    for i in list1:
        if i%2 !=0:
            yield i

list1 =[1,2,3,4,5,6,7,9]
gen_values = generator1(list1)
print(gen_values)
print(next(gen_values))
print(next(gen_values))
print(next(gen_values))

#Comprehension way....
print("<<<<------GNERATE COMPREHENSION--------->>>>>")
gen_values = (i for i in range (20) if i%2 !=0)
print(gen_values)
print(next(gen_values))
print(next(gen_values))



