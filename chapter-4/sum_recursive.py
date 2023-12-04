def sum_recursive(arr):
    if arr == []:
        return 0
    return arr[0] + sum_recursive(arr[1:])

print(sum_recursive([1, 2, 3, 4, 5]))