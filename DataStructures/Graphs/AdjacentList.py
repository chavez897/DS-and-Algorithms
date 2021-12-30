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


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 1)
graph.add_edge(3, 1)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(6, 5)
graph.show_connections()


