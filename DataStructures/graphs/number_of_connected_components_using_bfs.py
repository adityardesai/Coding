"""

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1


Do BFS

https://leetcode.com/problems/number-of-distinct-islands

TC:O(E+V)
SC:O(E+V)
"""

from collections import deque

class Solution:
    def build_graph(self,edges):
        graph=defaultdict(list)
        for edge in edges:
            u=edge[0]
            v=edge[1]
            graph[u].append(v)
            graph[v].append(u)
        
        return graph
    def bfs_helper(self,graph,n):
        queue=deque()
        visited=set()
        result=0
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                queue.append(node)
                result+=1
                while queue:
                    pop_node=queue.popleft()
                    for neigh in graph[pop_node]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
        return result
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=self.build_graph(edges)
        connected_components = self.bfs_helper(graph,n)
        return connected_components
