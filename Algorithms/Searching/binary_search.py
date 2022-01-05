def binary_search(array, initial, end, value):
    mid = ((end - initial) // 2) + initial
    if array[mid] == value:
        return mid
    if end - initial <= 1:
        return -1
    if array[mid] < value:
        return binary_search(array, mid + 1, end, value)
    else:
        return binary_search(array, initial, mid - 1, value)


data = [2, 4, 6, 8, 10, 12]
print(binary_search(data, 0, len(data) - 1, 6))
