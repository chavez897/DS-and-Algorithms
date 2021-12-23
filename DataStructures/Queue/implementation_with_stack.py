from stack import Stack


class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def __str__(self):
        self._fill_dequeue_stack()
        return str(self.dequeue_stack)

    def _fill_enqueue_stack(self):
        while not self.dequeue_stack.isEmpty():
            self.enqueue_stack.push(self.dequeue_stack.pop())

    def _fill_dequeue_stack(self):
        while not self.enqueue_stack.isEmpty():
            self.dequeue_stack.push(self.enqueue_stack.pop())

    def enqueue(self, value):
        self._fill_enqueue_stack()
        self.enqueue_stack.push(value)

    def dequeue(self):
        self._fill_dequeue_stack()
        return self.dequeue_stack.pop()

    def isEmpty(self):
        return self.enqueue_stack.isEmpty() and self.dequeue_stack.isEmpty()

    def peek(self):
        self._fill_dequeue_stack()
        return self.dequeue_stack.peek()


my_queue = Queue()
print(my_queue.peek())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.dequeue())
my_queue.enqueue(4)
print(my_queue.isEmpty())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.isEmpty())
my_queue.enqueue(5)
my_queue.enqueue(6)
print(my_queue.peek())
print(my_queue)
