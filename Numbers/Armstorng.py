def CheckArmstrong(mynumber):
    count = len(str(mynumber))
    temp=mynumber
    sum = 0
    while temp != 0:
        lastdigit = temp % 10
        sum = sum +(lastdigit**count)
        temp = temp//10
    if sum == mynumber:
        print("Entered number is an Armstrong Number!")
    else:
        print("Entered Number is not Armstrong Number....")

mynumber = int(input("Enter any Number: "))
CheckArmstrong(mynumber)