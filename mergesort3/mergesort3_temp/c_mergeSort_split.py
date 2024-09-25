from src.utils import Count 

def mergeSort(arr):
    Count.incC(18)
    n = len(arr)
    current_size = 1
    while current_size < n:
        Count.incC(1)
        if n % 2 == 0:
            Count.incC(2)
            for left in range(0, n, 2 * current_size):
                Count.incC(3)
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)
                left_subarray = arr[left:mid + 1]
                right_subarray = arr[mid + 1:right + 1]
                i = 0 
                j = 0  
                k = left  
                while i < len(left_subarray) and j < len(right_subarray):
                    Count.incC(4)
                    if left_subarray[i] <= right_subarray[j]:
                        Count.incC(5)
                        arr[k] = left_subarray[i]
                        i += 1
                    else:
                        Count.incC(6)
                        arr[k] = right_subarray[j]
                        j += 1
                    k += 1
                while i < len(left_subarray):
                    Count.incC(7)
                    arr[k] = left_subarray[i]
                    i += 1
                    k += 1
                while j < len(right_subarray):
                    Count.incC(8)
                    arr[k] = right_subarray[j]
                    j += 1
                    k += 1
            current_size *= 2
        else:
            Count.incC(9)
            for left in range(0, n, 2 * current_size):
                Count.incC(10)
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)
                left_subarray = arr[left:mid + 1]
                right_subarray = arr[mid + 1:right + 1]
                i = 0 
                j = 0  
                k = left  
                while i < len(left_subarray) and j < len(right_subarray):
                    Count.incC(11)
                    if left_subarray[i] <= right_subarray[j]: 
                        Count.incC(12)
                        arr[k] = left_subarray[i]
                        i += 2
                    else:
                        Count.incC(13)
                        arr[k] = right_subarray[j]
                        j += 1
                    k += 1
                while i < len(left_subarray):
                    Count.incC(14)
                    arr[k] = left_subarray[i]
                    i += 1
                    k += 1
                while j < len(right_subarray):
                    Count.incC(15)
                    arr[k] = right_subarray[j]
                    j += 1
                    k += 1
            current_size *= 2
