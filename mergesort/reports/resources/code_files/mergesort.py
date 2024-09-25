def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        if len(arr) % 2 == 0:
            middle = len(arr) // 2
            left = mergesort(arr[:middle])
            right = mergesort(arr[middle:])
            return merge(left, right)
        else:
            middle = len(arr) //2
            left = mergesort(arr[:middle])
            right = mergesort(arr[middle:])
            left.reverse()
            return merge(left, right)
