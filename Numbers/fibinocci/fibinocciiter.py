n=int(input("Enter the input for fibinocci series:"))

a = 0
print("first number",a)

b = 1
print("first number",b)
temp = 0

for i in range(0,n):
    temp=a+b
    a=b
    b=temp
    print(temp)
