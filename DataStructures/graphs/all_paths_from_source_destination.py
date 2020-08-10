# https://leetcode.com/problems/all-paths-from-source-to-target/
# TC: O(2^N * N)
# SC: O(2^N * N)
class Solution:
    def dfs_helper(self, graph, final_path, temp_path, starting_node):
        if starting_node == len(graph) - 1:
            final_path.append(list(temp_path))
            return
        for neigh in graph[starting_node]:
            temp_path.append(neigh)
            self.dfs_helper(graph, final_path, temp_path, neigh)
            temp_path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        temp_path = list()
        final_path = list()
        starting_node = 0

        temp_path.append(starting_node)
        self.dfs_helper(graph, final_path, temp_path, starting_node)

        return final_path
