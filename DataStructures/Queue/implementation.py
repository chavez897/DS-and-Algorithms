class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        queue = ""
        current_node = self.first
        while current_node is not None:
            queue += "{} -> ".format(current_node.value)
            current_node = current_node.next
        return queue

    # Time Complexity: O(1)
    def peek(self):
        return self.first.value if self.first is not None else None

    # Time Complexity: O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    # Time Complexity: O(1)
    def dequeue(self):
        if self.first is None:
            return None
        first_node = self.first
        value = first_node.value
        self.first = self.first.next
        del first_node
        if self.first is None:
            self.length = None
        return value


my_queue = Queue()
print(my_queue.peek())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue.dequeue())
my_queue.enqueue(5)
print(my_queue.peek())
print(my_queue)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue)
