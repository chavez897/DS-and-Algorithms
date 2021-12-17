# Create a function that reverse a string:
# 'Hi my name is Rodrigo' should be:
# ogirdoR is eman ym iH

# Time Complexity: O(n)
def reverse_string(input):
    if input is None or not isinstance(input, str) or len(input) < 2:
        return "Invalid Input"
    array = [char for char in input]
    response = []
    for i in range(len(array) - 1, -1, -1):
        response.append(array[i])
    return response


# Time Complexity: O(n)
def reverse_string_mutating(input):
    if input is None or not isinstance(input, str) or len(input) < 2:
        return "Invalid Input"
    array = [char for char in input]
    first_pointer = 0
    second_pointer = len(input) - 1
    while first_pointer < second_pointer:
        # Switch positions
        temp = array[first_pointer]
        array[first_pointer] = array[second_pointer]
        array[second_pointer] = temp
        # Next Pointers
        first_pointer += 1
        second_pointer -= 1
    return array


print(reverse_string("Hi my name is Rodrigo"))
print(reverse_string_mutating("Hi my name is Rodrigo"))
