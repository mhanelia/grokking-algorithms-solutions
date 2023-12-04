def count_recursive(arr):
    if arr == []:
        return 0
    return 1 + count_recursive(arr[1:])

print(count_recursive([1, 2, 3, 4, 5]))