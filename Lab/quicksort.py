def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:        
        return   array
    print(array) 
    pivot = array[-1]    
    left_arr = []
    right_arr = []
    middle_arr = []    

    for i in array:
        if i < pivot:
            left_arr.append(i)
        elif i == pivot:
            middle_arr.append(i)
        else:
            right_arr.append(i)
    
    left_arr = quick_sort(left_arr)    
    right_arr =  quick_sort(right_arr)
    sorted_arr = left_arr + middle_arr + right_arr
    return sorted_arr

print(quick_sort([20, 3, 14, 1, 5]))