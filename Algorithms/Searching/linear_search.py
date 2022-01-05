def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linear_search([8,4,3,2,6,9,0], 9))
