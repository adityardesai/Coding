# https://leetcode.com/problems/find-the-town-judge
# TC:O(N)
# SC:O(N)

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        
        in_degree=[0]*(N+1)
        out_degree=[0]*(N+1)
        
        for t in trust:
            first=t[0]
            second=t[1]
            
            in_degree[second]+=1
            out_degree[first]+=1
            
        
        for i in range(1,N+1):
            if in_degree[i] == N-1 and out_degree[i] == 0:
                return i
        
        return -1
