Bipartite graph

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.


Link:https://leetcode.com/problems/possible-bipartition/
TC:O(E+V)
SC:O(E+V)

Color nodes with red(0) and blue(1)
Stable matching algorihtm

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

class Solution:
    def dfs(self, node, color):
        if node in self.color_mapping and color != self.color_mapping[node]:   
            return False
        
        self.color_mapping[node] = color
        
        if node not in self.visited_set:
            self.visited_set.add(node)
            for neigh in self.graph[node]:                                    
                if not self.dfs(neigh, not color): 
                    return False            
        return True    
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        self.graph = collections.defaultdict(list)
        self.visited_set = set()
        self.color_mapping = dict()
        
        for (u, v) in dislikes:                                          
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):                                          
            if i not in self.visited_set: 
                if not self.dfs(i, True):                               
                    return False
        return True

