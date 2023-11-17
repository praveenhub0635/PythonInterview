def polindnum(num):
    rev = 0
    while num!=0:
        rev = (rev*10) + (num%10)
        num = num //10
    return rev

num = int(input("Enter any number:"))
rev = polindnum(num)

if (rev==num):
    print("The number is Polindrome:")
else:
    print("The number is not polindrome:")
