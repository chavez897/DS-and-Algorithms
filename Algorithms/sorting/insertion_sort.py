def insertion_sort(array):
    for i in range(len(array)):
        previous_index = i - 1
        current_index = i
        while previous_index >= 0 and array[previous_index] > array[current_index]:
            array[current_index], array[previous_index] = array[previous_index], array[current_index]
            previous_index -= 1
            current_index -= 1
    return array


print(insertion_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))

