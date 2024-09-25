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
