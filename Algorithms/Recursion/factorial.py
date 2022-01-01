def factorial_iterative(value):
    result = 1
    while value > 1:
        result = result * value
        value -= 1
    return result


def factorial_recursion(value):
    if value <= 1:
        return value
    return value * factorial_recursion(value - 1)


print(factorial_iterative(5))
print(factorial_recursion(5))
