# https://leetcode.com/problems/find-the-celebrity/
# TC:O(N)
# SC:O(1)

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_celebrity=0
        for i in range(1,n):
            if knows(possible_celebrity,i):
                possible_celebrity=i
        if self.helper(possible_celebrity,n):
            return possible_celebrity
        
        return -1
        
    
    def helper(self, possible_celebrity, n):
        for j in range(n):
            if possible_celebrity==j: continue
            if knows(possible_celebrity, j) or not knows(j, possible_celebrity):
                return False
        return True
        
