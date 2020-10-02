"""
There are N courses, labelled from 1 to N.
We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.
In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.
Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

Ref: https://leetcode.com/problems/parallel-courses/discuss/519251/Python-Topological-Sort-%2B-BFS-detailed-comment-and-explanation-on-each-line

TC: O(V+E)
SC: O(V+E)

"""

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        if not relations or not N:
            return -1
        
        topological_sort=list()
        
        graph={x:[] for x in range(1,N+1)}
        indegree_map={x:0 for x in range(1,N+1)}
        
        for relation in relations:
            parent=relation[0]
            child=relation[1]
            
            if parent in graph:
                graph[parent].append(child)
            else:
                graph[parent]=[child]
            
            indegree_map[child] = indegree_map.get(child,0) + 1
            
        
        queue=deque()
        
        for k,v in indegree_map.items():
            if v==0:
                queue.append(k)
        
        semesterCount=0
        courseCountForThisSemester=0
        
        # Identify Cycle
        if len(queue)>0:
            semesterCount += 1
            courseCountForThisSemester = len(queue)
        else:
            return -1
        
        
        while queue:
            
            if courseCountForThisSemester<=0:
                semesterCount+=1
                courseCountForThisSemester = len(queue) 
            
            courseCountForThisSemester-=1
            
            node=queue.popleft()
            topological_sort.append(node)
            for child in graph[node]:
                indegree_map[child]-=1
                if indegree_map[child]==0:
                    queue.append(child)
        
        if len(topological_sort) != N:
            return -1
        else:
            return semesterCount
            
        
