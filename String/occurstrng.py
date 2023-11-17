def countofOccurance(mychar,mystring):
    count = 0
    for i in range(len(mystring)):
        if(mystring[i] == mychar):
            count =count + 1
    return count

mystring = input("Please Enter a string:")
mychar = input("Please Enter a Character ")
count = countofOccurance(mychar,mystring)
print("Total number of occurances of",mychar,"is :",count)