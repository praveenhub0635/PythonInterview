def ResverseNumber(num):
    rev = 0
    while num!= 0 :
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev

num = int(input("Enter any number:"))
print("Thwe reversed Number is:",ResverseNumber(num))