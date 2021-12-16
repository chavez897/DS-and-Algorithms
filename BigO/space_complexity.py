def boooo(n):
    for i in n:
        print("boooo")


def hi_array(n):
    array = []
    for i in range(n):
        array.append("hi!")
    print(array)


# boooo([1, 2, 3, 4, 5, 6])  # O(1)
hi_array(8)  # O(n)
