def factorialnum(num):
    fact = 1
    while num != 0 :
        fact = fact * num
        num -= 1
    return fact
num = int(input("Enter any Number:"))
print("The Factorial of the number is:",factorialnum(num)) 