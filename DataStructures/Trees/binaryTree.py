class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value):
        root = Node(value)
        self.root = root

    def traverse(self, current_node):
        if self.root is None:
            print("empty")
            return
        print("{} -> ".format(current_node.value), end=" ")
        if current_node.left is not None:
            self.traverse(current_node.left)
        if current_node.right is not None:
            self.traverse(current_node.right)

    def lookup(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                break
            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def lookup_path(self, value):
        trace = ""
        current_node = self.root
        while current_node is not None:
            trace += "{} ->".format(current_node.value)
            if current_node.value == value:
                break
            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if current_node is None:
            return "Value not found!"
        return trace[:-3]

    def add(self, value):
        new_node = Node(value)
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return
            if current_node.value > value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                current_node = current_node.right

    def _remove_smallest_value(self, node, parent):
        current_node = node
        parent_node = parent
        while current_node.left is not None:
            parent_node = current_node
            current_node = current_node.left
        smallest = current_node.value
        parent_node.left = None
        del current_node
        return smallest

    def remove(self, value, node):
        current_node = node
        parent_node = None
        while current_node is not None:
            if current_node.value == value:
                break
            parent_node = current_node
            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if current_node is None:
            return "Value not found!!!"
        if current_node.left is None and current_node.right is None:
            if current_node == self.root:
                self.root = None
            else:
                if value < parent_node.value:
                    parent_node.left = None
                else:
                    parent_node.right = None
            del current_node
            return
        elif current_node.left is not None and current_node.right is not None:
            if current_node.right.left is None:
                current_node.value = current_node.right.value
                current_node.right = current_node.right.right
            else:
                smallest = self._remove_smallest_value(current_node.right, current_node)
                current_node.value = smallest
        else:
            if current_node.left is not None:
                if current_node == self.root:
                    self.root = current_node.left
                if value < parent_node.value:
                    parent_node.left = current_node.left
                else:
                    parent_node.right = current_node.left
                del current_node
            else:
                if current_node == self.root:
                    self.root = current_node.right
                if value < parent_node.value:
                    parent_node.left = current_node.right
                else:
                    parent_node.right = current_node.right
                del current_node


tree = BinarySearchTree(9)
tree.add(4)
tree.add(6)
tree.add(1)
tree.add(20)
tree.add(15)
tree.add(170)
tree.add(180)
tree.traverse(tree.root)
print("")
tree.remove(20, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(4, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(9, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(15, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(6, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(1, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(180, tree.root)
tree.traverse(tree.root)
print("")
tree.remove(170, tree.root)
tree.traverse(tree.root)
print("")
