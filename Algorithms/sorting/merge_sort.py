def merge_sort(array):
    if len(array) == 1:
        return array
    split_index = len(array) // 2
    left_array = array[:split_index]
    right_array = array[split_index:]
    return  merge(merge_sort(left_array), merge_sort(right_array))


def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    merge_array = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            merge_array.append(left[left_pointer])
            left_pointer += 1
        else:
            merge_array.append(right[right_pointer])
            right_pointer += 1
    if left_pointer >= len(left):
        while right_pointer < len(right):
            merge_array.append(right[right_pointer])
            right_pointer += 1
    else:
        while left_pointer < len(left):
            merge_array.append(left[left_pointer])
            left_pointer += 1
    return merge_array

print(merge_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
