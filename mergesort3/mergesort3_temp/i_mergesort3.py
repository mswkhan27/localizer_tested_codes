def mergeSort(arr):
    c[18] += 1
    n = len(arr)
    current_size = 1
 
    while current_size < n:
        c[1] += 1
        if n % 2 == 0:
            c[2] += 1
            for left in range(0, n, 2 * current_size):
                c[3] += 1
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)
                left_subarray = arr[left:mid + 1]
                right_subarray = arr[mid + 1:right + 1]
    
                i = 0 
                j = 0  
                k = left  
    
                while i < len(left_subarray) and j < len(right_subarray):
                    c[4] += 1
                    if left_subarray[i] <= right_subarray[j]:
                        c[5] += 1
                        arr[k] = left_subarray[i]
                        i += 1
                    else:
                        c[6] += 1
                        arr[k] = right_subarray[j]
                        j += 1
                    k += 1
    
                while i < len(left_subarray):
                    c[7] += 1
                    arr[k] = left_subarray[i]
                    i += 1
                    k += 1

                while j < len(right_subarray):
                    c[8] += 1
                    arr[k] = right_subarray[j]
                    j += 1
                    k += 1
    
            current_size *= 2
        else:
            c[9] += 1
            for left in range(0, n, 2 * current_size):
                c[10] += 1
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)
                left_subarray = arr[left:mid + 1]
                right_subarray = arr[mid + 1:right + 1]
    
                i = 0 
                j = 0  
                k = left  
    
                while i < len(left_subarray) and j < len(right_subarray):
                    c[11] += 1
                    if left_subarray[i] <= right_subarray[j]: 
                        c[12] += 1
                        arr[k] = left_subarray[i]
                        i += 2
                    else:
                        c[13] += 1
                        arr[k] = right_subarray[j]
                        j += 1
                    k += 1
    
                while i < len(left_subarray):
                    c[14] += 1
                    arr[k] = left_subarray[i]
                    i += 1
                    k += 1

                while j < len(right_subarray):
                    c[15] += 1
                    arr[k] = right_subarray[j]
                    j += 1
                    k += 1
    
            current_size *= 2
            
def sortMultipleArrays(arrays):
    c[19] += 1
    for array in arrays:
        c[16] += 1
        mergeSort(array)
    return arrays

# Example usage:
arrays = [[3, 1, 1, 5],
[9, 2, 8, 7],
[0, 1, 2, 3, 5],
[-1, -2, -4, -5],
[10, 3, 7, 2, 1],
[0, 0, 0, 0],
[5, -3, 7, 9],
[2, 2, 2, 2, 2],
[1, -1, 1, -1, -1],
[4, 5, 6, 7, 8, 9, 1],
[23, 34, 12, 45, 56, 78, 89],
[9, 9, 8, 7, 7, 6, 6],
[2, 4, 6, 8, 1, 3, 7],
[-100, -50, -10, -5],
[99, 0, 44, 55],
[15, 3, 9, 2, 8, 7, 5],
[100, 1, 50, 23],
[42, 34, 23, 89, 12],
[-15, -8, -30, -22],
[6, 1, 4, 3, 2],




]
sorted_arrays = sortMultipleArrays(arrays)

# Print each sorted array on a new line
for array in sorted_arrays:
    c[17] += 1
    print(array)
