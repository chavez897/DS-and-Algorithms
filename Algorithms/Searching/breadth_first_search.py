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
            self.length = 0
        return value

    def is_empty(self):
        return self.length <= 0


class Graph:
    def __init__(self):
        self.adjacent_list = {}
        self.number_of_nodes = 0

    def add_vertex(self, node):
        if node in self.adjacent_list:
            return
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adjacent_list or node2 not in self.adjacent_list:
            return
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)

    def show_nodes(self):
        return self.adjacent_list.keys()

    def show_connections(self):
        nodes = self.show_nodes()
        for node in nodes:
            print("{} -> {}".format(node, self.adjacent_list[node]))

    def bfs(self, initial):
        result = []
        queue = Queue()
        queue.enqueue(initial)
        seen_nodes = {}
        while not queue.is_empty():
            current_node = queue.dequeue()
            current_connections = self.adjacent_list[current_node]
            if current_node not in seen_nodes:
                seen_nodes[current_node] = True
                result.append(current_node)
                for connection in current_connections:
                    queue.enqueue(connection)
        return result

    def bfs_recursive(self, queue, result, seen_nodes):
        if queue.is_empty():
            return result
        current_node = queue.dequeue()
        current_connections = self.adjacent_list[current_node]
        if current_node not in seen_nodes:
            seen_nodes[current_node] = True
            result.append(current_node)
            for connection in current_connections:
                queue.enqueue(connection)
        return self.bfs_recursive(queue, result, seen_nodes)

    def dfs(self, node, seen):
        if node not in seen:
            seen[node] = True
            current_connections = self.adjacent_list[node]
            print("{} ->".format(node), end="")
            for connection in current_connections:
                self.dfs(connection, seen)


graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
graph.add_vertex(12)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(5, 9)
graph.add_edge(5, 10)
graph.add_edge(4, 7)
graph.add_edge(4, 8)
graph.add_edge(7, 11)
graph.add_edge(7, 12)
graph.add_edge(8, 12)
graph.add_edge(3, 6)
graph.add_edge(6, 11)
graph.add_edge(6, 10)
#print(graph.bfs(8))
#queue = Queue()
#queue.enqueue(8)
#seen = {}
#print(graph.bfs_recursive(queue, [], seen))
print(graph.dfs(1, {}))
