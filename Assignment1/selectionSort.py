def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr
            
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] < arr[i]:
    #             arr[i], arr[j] = arr[j], arr[i]
    # return arr

arr = [2, 8, 5, 3, 9, 4, 1]
print(selectionSort(arr))
