class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return "length:{}, data:{}".format(self.length, self.data)

    # O(1)
    def get(self, index):
        return self.data[index]

    # O(1)
    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    # O(1)
    def pop(self):
        del self.data[self.length - 1]
        self.length -= 1

    # O(n)
    def delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.pop()

    # O(n)
    def insert(self, index, value):
        self.push(self.get(self.length - 1))
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value


array = MyArray()
print(array)

array.push("a")
array.push("b")
array.push("c")
array.push("d")
array.push("e")
print(array)

print(array.get(0))

array.pop()
array.delete(1)
print(array)

array.insert(1, "b")
array.insert(2, "xxxxx")
array.insert(3, "yyyyy")
print(array)
