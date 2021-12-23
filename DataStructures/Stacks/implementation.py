class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        stack = ""
        current_node = self.top
        while current_node is not None:
            stack += "{} -> ".format(current_node.value)
            current_node = current_node.next
        return stack

    # Time Complexity: O(1)
    def peek(self):
        return self.top.value if self.top is not None else None

    # Time Complexity: O(1)
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        if self.bottom is None:
            self.bottom = new_node

    # Time Complexity: O(1)
    def pop(self):
        if self.top is None:
            return None
        pop_node = self.top
        value = pop_node.value
        self.top = self.top.next
        if self.top is None:
            self.head = None
        self.length -= 1
        del pop_node
        return value

    # Time Complexity: O(1)
    def isEmpty(self):
        return self.length == 0


my_stack = Stack()
print(my_stack.peek())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())
print(my_stack.peek())
my_stack.push(4)
print(my_stack)
print(my_stack.pop())
print(my_stack.isEmpty())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.isEmpty())
print(my_stack)
