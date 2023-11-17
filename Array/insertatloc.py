my_arr = [1,3,5,7,8,9]

num=int(input("Enter a number to insert in your array:"))
index =int(input("Enter the index to insert the value:"))

if index >= len(my_arr):
    print("Index out of bounds,no change in the array!",len(my_arr))
else:
    my_arr.insert(index,num)

print("Array after inserting",num,"=",my_arr)