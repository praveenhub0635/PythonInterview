def collect(total_numbers):
    print("please enter ",total_numbers,"numbers:")
    for i in range(0,total_numbers):
        ele=float(input())
        myList.append(ele)


def calculateAvg():
    total=0
    for i in range(0,len(myList)):
        total=total+myList[i]
    return (total/total_numbers)

myList = []

total_numbers = int(input("Average of how many numbers?"))
collect(total_numbers)

average=calculateAvg()
print("The Avergae is:",average)
