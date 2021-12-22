from implementation import LinkedList, Node


def reverse(linked_list):
    if linked_list.length <= 1:
        return linked_list
    previous_node = None
    current_node = linked_list.head
    next_node = current_node.next
    while current_node is not None:
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        if next_node is not None:
            next_node = next_node.next
    temp_node = linked_list.head
    linked_list.head = linked_list.tail
    linked_list.tail = temp_node
    return linked_list


my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
print(my_linked_list)
reverse(my_linked_list)
print(my_linked_list)
