def reverse_string_iterative(value):
    string = list(value)
    first = 0
    second = len(string) - 1
    while first < second:
        temp = string[first]
        string[first] = string[second]
        string[second] = temp
        first += 1
        second -= 1
    return "".join(string)


def reverse_string_recursive(value):
    if len(value) <= 0:
        return value
    return reverse_string_recursive(value[1:]) + value[0]


print(reverse_string_iterative("hello how are you!"))
print(reverse_string_recursive("hello how are you!"))
