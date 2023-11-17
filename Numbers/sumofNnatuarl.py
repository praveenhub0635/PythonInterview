def sumOfNNaturalsNos(Num):
    result = Num * (Num + 1 )
    result = result / 2
    return result

num = float(input("Please enter the Number:"))

if(num > 0):
    print("The sum of N Natural number is:",sumOfNNaturalsNos(num))
else:
    print("Enter a Valid Number!")