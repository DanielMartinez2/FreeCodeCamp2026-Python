def selection_sort(items: list) -> list:
    for i in range(0, len(items)):                        
        min_item = items[i]        
        index = i        
        for j in range (i+1, len(items)):
            if items[j] < min_item:                
                min_item = items[j]
                index = j                                
        swap = items[i]
        if items[i] != min_item:
            items[i] = min_item
            items[index] = swap
    return items

print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
