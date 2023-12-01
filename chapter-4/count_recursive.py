def count_recursive(arr):
    if len(arr) == 1:
        return 1
    return 1 + count_fat(arr[1:])

print(count_fat([1, 2, 3, 4, 5]))