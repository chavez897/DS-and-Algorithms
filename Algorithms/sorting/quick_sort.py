def partition(array, left, right):
    smaller_index = left - 1
    pivot = array[right]
    for i in range(left, right):
        if array[i] < pivot:
            smaller_index += 1
            array[smaller_index], array[i] = array[i], array[smaller_index]
    array[smaller_index + 1], array[right] = array[right], array[smaller_index + 1]
    return (smaller_index + 1)

def quick_sort(array, left, right):
    if left < right:
        split_index = partition(array, left, right)
        quick_sort(array,left,split_index-1)
        quick_sort(array,split_index+1,right)
    return  array

array = [5,3,2,1,4]
print(quick_sort(array, 0, len(array) - 1))