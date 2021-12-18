# Given an array, return the first repeated value
# Input: [2,3,5,4,2,8,3,9]
# Output: 2


# Time Complexity: O(1)
def first_recurrent(array):
    map = set()
    for value in array:
        if value in map:
            return value
        else:
            map.add(value)
    return None


print(first_recurrent([2, 3, 5, 4, 2, 8, 3, 9]))
