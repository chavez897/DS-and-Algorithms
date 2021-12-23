class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return self.value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        data = ""
        current_node = self.head
        while current_node is not None:
            data += " {} -->".format(current_node.value)
            current_node = current_node.next
        return data

    def print_backwards(self):
        data = ""
        current_node = self.tail
        while current_node is not None:
            data += " {} -->".format(current_node.value)
            current_node = current_node.previous
        return data

    # Time Complexity: O(1)
    def append(self, value):
        new_node = Node(value)
        new_node.previous = self.tail
        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    # Time Complexity: O(1)
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1

    # Time Complexity: O(n)
    def insert(self, position, value):
        if position > self.length:
            return "Invalid Position"
        if position == self.length:
            self.append(value)
            return
        if position == 0:
            self.prepend(value)
            return
        current_node = self.head
        for i in range(1, position):
            current_node = current_node.next
        new_node = Node(value)
        new_node.next = current_node.next
        new_node.previous = current_node
        current_node.next.previous = new_node
        current_node.next = new_node
        self.length += 1

    def _remove_node(self, node):
        if node.previous is None:
            self.head = self.head.next
            self.head.previous = None
        else:
            node.previous.next = node.next
        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous
        self.length -= 1
        del node

    # Time Complexity: O(n)
    def delete_by_value(self, value):
        if self.length <= 0:
            return "Value not Found!"
        current_node_1 = self.head
        index_1 = 0
        current_node_2 = self.tail
        index_2 = self.length - 1
        flag = 0
        while index_1 <= index_2:
            if value is current_node_1.value:
                flag = 1
                break
            if value is current_node_2.value:
                flag = 2
                break
            current_node_1 = current_node_1.next
            index_1 += 1
            index_2 -= 1
            current_node_2 = current_node_2.previous
        if flag == 1:
            self._remove_node(current_node_1)
        elif flag == 2:
            self._remove_node(current_node_2)
        else:
            return "Value not Found!"

    # Time Complexity: O(n)
    def delete_by_position(self, position):
        if position >= self.length:
            return "Invalid Position"
        current_node = self.head
        if position == 0:
            self._remove_node(self.head)
            return
        for i in range(1, position):
            current_node = current_node.next
        self._remove_node(current_node)


my_list = DoubleLinkedList()
my_list.append("a")
my_list.prepend("b")
my_list.append("c")
my_list.insert(3, "d")
my_list.insert(1, "x")
my_list.delete_by_value("x")
my_list.delete_by_value("b")
my_list.delete_by_value("d")
my_list.append("y")
my_list.insert(1, "z")
my_list.delete_by_position(0)
my_list.delete_by_position(my_list.length - 1)
my_list.prepend("o")
my_list.append("w")
my_list.insert(2, "o")
print(my_list)
print(my_list.print_backwards())
