def SimpleInterest(principle,time,rate):
    print("The Principle is :",principle)
    print("The time period is ",time)
    print("The Rate of Intrestc is:",rate)

    return (principle*time*rate)/100

simple_intrest=SimpleInterest(3000,10,1)
# principle = int(input("Enter the principle amount:"))
# time=int(input("Enter the time period:"))
# rate=int(input("Enter the rate of intrest for amount:"))
print("The Calculated Simple Intrest is",simple_intrest)