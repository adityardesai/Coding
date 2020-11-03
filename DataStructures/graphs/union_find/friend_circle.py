"""
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, 
then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, 
then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

TC:O(N^2) using path compression union find
SC:O(N)

https://leetcode.com/problems/friend-circles/

"""
from collections import deque

class Solution(object):
    def bfs_helper(self, M):
        """
        TC=O(N^2)
        SC=O(N)
        """
        visited=set()
        count=0
        queue=deque()
        for i in range(len(M)):
            if i not in visited:
                queue.append(i)
                count+=1
                while queue:
                    poped=queue.popleft()
                    visited.add(poped)
                    for j in range(len(M)):
                        if M[poped][j]==1 and j not in visited:
                            queue.append(j)
        return count
    
    def find(self, parent, i):
        """
        TC:O(logN)
        """
        if parent[i]==-1:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set=self.find(parent,x)
        y_set=self.find(parent,y)
        
        if x_set!=y_set:
            parent[x_set]=y_set
        
    def union_find_helper(self, M):
        """
        TC:O(N^32)
        SC:O(N)
        """
        parent=[-1 for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j]==1 and i!=j:
                    self.union(parent,i,j)
        
        count=0
        for i in range(len(parent)):
            if parent[i]==-1:
                count+=1
        return count
                
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return -1
        
        #return self.bfs_helper(M)
        return self.union_find_helper(M)
