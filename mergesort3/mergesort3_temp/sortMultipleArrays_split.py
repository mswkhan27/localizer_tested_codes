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
