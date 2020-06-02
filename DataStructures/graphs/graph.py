from collections import defaultdict, deque
"""
Implementation of Graph Data Strucutres using Adjacency Lists
"""


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def _add_edge(self, u, v):
        self.graph[u].append(v)

    def _breadth_first_traversal_iterative(self, start_node):
        visited = set()
        queue = deque()
        queue.append(start_node)
        visited.add(start_node)

        while (len(queue)):
            node = queue.popleft()
            print(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def _depth_first_search_iterative(self, start_node):
        visited = set()
        stack = deque()
        stack.append(start_node)

        while (len(stack)):
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    def _print_graph(self):
        if self.graph is not None:
            for node in self.graph:
                print(str(node) + " is connected to " + str(self.graph[node]))


def main_bfs_iterative():

    graph = Graph()
    graph._add_edge(0, 1)
    graph._add_edge(0, 2)
    graph._add_edge(1, 2)
    graph._add_edge(2, 0)
    graph._add_edge(2, 3)
    graph._add_edge(3, 3)

    graph._print_graph()
    graph._breadth_first_traversal(2)


def main_dfs_iterative():
    g = Graph()
    g._add_edge(1, 0)
    g._add_edge(0, 2)
    g._add_edge(2, 1)
    g._add_edge(0, 3)
    g._add_edge(1, 4)

    g._print_graph()
    g._depth_first_search_iterative(0)


if __name__ == '__main__':
    main_dfs_iterative()
    #main_bfs_iterative()
