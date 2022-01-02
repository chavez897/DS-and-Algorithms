def selection_sort(array):
    for i in range(len(array) - 1):
        min_value = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if min_value > array[j]:
                min_value = array[j]
                min_index = j
        array[i], array[min_index] = min_value, array[i]
    return array


print(selection_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
