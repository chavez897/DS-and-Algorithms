def fibonacci_iterative(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    previous = 0
    current = 1
    for i in range(2, index + 1):
        temp = current
        current = previous + current
        previous = temp
    return current


def fibonacci_recursive(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)


print(fibonacci_iterative(8))
print(fibonacci_recursive(9))
