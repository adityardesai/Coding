"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. 
Also it's guaranteed that the subordination relationships have a tree structure.
The head of the company wants to inform all the employees of the company of an urgent piece of news. 
He will inform his direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.
The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
(i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news. 

Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

TC: O(N)
SC: O(N)
"""

class Solution:
    def build_graph(self,n,manager,informTime,headID):
        
        graph={x:[] for x in range(n)}
        
        for i in range(n):

            mgr=manager[i]
            emp=i
            
            if mgr == -1: continue
            
            if graph.get(mgr,0):
                graph[mgr].append(emp)
            else:
                graph[mgr]=[emp]
        
        return graph
    def traverse_graph(self, graph, headID, informTime):
        result=0
        
        for v in graph[headID]:
            result = max(result, self.traverse_graph(graph, v, informTime));
        
        return result+informTime[headID]
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=self.build_graph(n,manager,informTime, headID)
        return self.traverse_graph(graph, headID, informTime)
