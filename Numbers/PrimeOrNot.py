def PrimeNot(param):
    for i in range(2,param):
        if ((param%i) == 0):
            print(param,"is not a Prime Number")
            break
    else:
        print(param,"Is a Prime Number")

num = int(input("Enter the number to check ptime or Not:"))

if num > 1:
    PrimeNot(num)
else:
    print("Enter a valid Number:")

