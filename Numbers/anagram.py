def anagramcheck(str1,str2):
    if(sorted(str1)==sorted(str2)):
        print("The strings are Anagram")
    else:
        print("The strings are not Anagram")

str1=input("Please Enter String-1:")
str2=input("Please Enter String-2:")

anagramcheck(str1,str2)
