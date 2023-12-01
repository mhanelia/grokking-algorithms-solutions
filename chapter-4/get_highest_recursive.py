def get_highest_recursive(arr):
    if len(arr) == 0:
        return -1

    else:
        highest = get_highest_recursive(arr[1:])

    return arr[0] if arr[0] > highest else highest

print(get_highest_recursive([1, 2, 8, 4, 5]))
print(get_highest_recursive([5, 4, 9, 2, 10]))
print(get_highest_recursive([3]))
print(get_highest_recursive([]))