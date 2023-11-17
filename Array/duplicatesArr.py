def duplicatesArray():
    my_arr=[30,20,30,40,1000,20,70,80,1000]
    print("Duplicates elements in the given array are:")
    arr_len = len(my_arr)
    
    for i in range(0,arr_len):
        for j in range(i+1,arr_len):
            if (my_arr[i] == my_arr[j]):
                print(my_arr[j])

duplicatesArray()
