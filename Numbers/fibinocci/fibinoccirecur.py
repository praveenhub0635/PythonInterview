def fibinocci(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return fibinocci(i-2) + fibinocci(i-1)

n = int(input("Enter the index till you want the series:"))

if n < 0:
    print("Add a positiveNumber!:")
else:
    for i in range(0,n):
        print(fibinocci(i))
    