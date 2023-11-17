
# Formulae for Compound Interest is A = P(1+R/100) raise to the power t
def CompoundIntrest(principle,rate,time):
    amount=principle*(pow(1 + (rate/100), time))
    return amount - principle

principle = int(input("Enter the principle amount:"))
time=int(input("Enter the time period:"))
rate=int(input("Enter the rate of intrest for amount:"))
print("The Calculate Compound Intrest is:",CompoundIntrest(principle,rate,time))
