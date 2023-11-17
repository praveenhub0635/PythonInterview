def PositiveNegativeZero(Num):
    if(Num) == 0:
        print("the number is invalid or Zero")
    elif(Num) > 0:
        print("the number is grater than Zero")
    else:
        print("The number is negative")

num = float(int(input("Enter the number to check its state:")))
PositiveNegativeZero(num)
