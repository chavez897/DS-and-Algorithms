class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class LinkedList:
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

    # Time Complexity: O(1)
    def append(self, value):
        new_node = Node(value)
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
        current_node.next = new_node
        self.length += 1

    # Time Complexity: O(n)
    def delete_by_value(self, value):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if value is current_node.value:
                break
            previous_node = (
                previous_node.next if previous_node is not None else self.head
            )
            current_node = current_node.next
        if current_node is None:
            return "Value not Found!"
        if previous_node is None:
            self.head = self.head.next
            self.length -= 1
            return
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next
        del current_node
        self.length -= 1

    # Time Complexity: O(n)
    def delete_by_position(self, position):
        if position >= self.length:
            return "Invalid Position"
        current_node = self.head
        previous_node = None
        if position == 0:
            self.head = current_node.next
            del current_node
            self.length -= 1
            return
        for i in range(1, position):
            current_node = current_node.next
            previous_node = (
                previous_node.next if previous_node is not None else self.head
            )
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next
        del current_node
        self.length -= 1

    # Time Complexity: O(n)
    def get_index(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                break
            index += 1
            current_node = current_node.next
        return index if current_node is not None else None

    # Time Complexity: O(n)
    def get_value(self, index):
        if index >= self.length:
            return "Invalid Position"
        if index == 0:
            return self.head.value
        current_node = self.head
        for i in range(1, index + 1):
            current_node = current_node.next
        return current_node.value


def main():
    my_list = LinkedList()
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
    print(my_list.get_index("o"))
    print(my_list.get_value(my_list.length - 1))


if __name__ == "__main__":
    main()
