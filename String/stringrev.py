def stringreverse(my_string):
    reversestring=""
    for i in my_string:
        reversestring=i+reversestring
    return reversestring

my_string = "Hey There!"
str_rev=stringreverse(my_string)
print("The reverse string is:",str_rev)