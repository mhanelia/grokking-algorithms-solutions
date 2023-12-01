def sum_fat(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_fat(arr[1:])

print(sum_fat([1, 2, 3, 4, 5]))