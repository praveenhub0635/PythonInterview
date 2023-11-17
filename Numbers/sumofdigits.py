def sumofDigits(mynumber):
    count = 0
    sum = 0
    while(mynumber!=0):
        sum = sum + (mynumber % 10)
        
        mynumber = mynumber // 10
        count  = count + 1

    return count,sum

mynumber =int(input("Please enter any number:"))
finalcount=sumofDigits(mynumber)

print("Total number of digits in the number is:",finalcount) 