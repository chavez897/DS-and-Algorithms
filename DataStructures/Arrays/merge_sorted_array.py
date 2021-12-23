# Given 2 arrays sorted merge them into 1 array still sorted
# Input: [0,3,4,31], [4,6,30]
# Output: [0,3,4,4,6,30,31]


# Time Complexity: O(n + m) where n is the length of the first array and m is the length od the second array
def merge_arrays(array1, array2):
    first_pointer = 0
    second_pointer = 0
    result = []
    while len(result) < len(array1) + len(array2):
        # if all items of the first array are included
        if first_pointer >= len(array1):
            second_pointer = addElement(result, array2[second_pointer], second_pointer)
        # if all items of the second array are included
        elif second_pointer >= len(array2):
            first_pointer = addElement(result, array1[first_pointer], first_pointer)
        # Haven't reach the end of either array
        else:
            if array1[first_pointer] < array2[second_pointer]:
                first_pointer = addElement(result, array1[first_pointer], first_pointer)
            else:
                second_pointer = addElement(
                    result, array2[second_pointer], second_pointer
                )
    return result


# Auxiliar function to clean code
def addElement(array, value, pointer):
    array.append(value)
    return pointer + 1


print(merge_arrays([0, 3, 4, 31], [4, 6, 30]))

print(merge_arrays([], [4, 6, 30]))
