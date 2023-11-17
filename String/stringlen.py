def strnglen(my_string):
    len_count=0
    for i in my_string:
        len_count = len_count + 1 
    return len_count   

my_string = "Hey There look at my preparation!"
str_len=strnglen(my_string)
print("The Length of the string is:",str_len)