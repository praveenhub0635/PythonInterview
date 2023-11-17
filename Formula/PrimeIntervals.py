def PrimeIntervl(First,Second):
    for i in range(First,Second+1):
        for j in range(2,i):
            if((i%j) == 0):
                break
        else:
            print(i,"i is a Prime Number!")

FirstInterval = int(input("Please Enter First Interval: "))
SecondInterval = int(input("Please Enter Second Interval:"))

if ((FirstInterval > 1 and SecondInterval > 2) and FirstInterval < SecondInterval):
    PrimeIntervl(FirstInterval,SecondInterval)
else:
    print("Enter a valid range?")
                
