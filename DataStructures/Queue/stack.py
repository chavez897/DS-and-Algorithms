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

    def peek(self):
        return self.top.value if self.top is not None else None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        if self.bottom is None:
            self.bottom = new_node

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

    def isEmpty(self):
        return self.length == 0
