"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

TC:O(logN)
SC:O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        
        left = 0
        right = M*N - 1
        
        while left <= right:
            mid_idx = (left + right) //2
            mid_ele = matrix[mid_idx // N][mid_idx % N]
            
            if target == mid_ele:
                return True
            elif target < mid_ele:
                right = mid_idx-1
            else:
                left = mid_idx+1
                    
        return False
==========================================
Divide and Conquer

TC:O(N+M)
SC:O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        if M == 0:
            return False
        
        N = len(matrix[0])
        
        i=M-1
        j=0
        while i>=0 and j<N:
            if target < matrix[i][j]:
                i = i-1
            elif target > matrix[i][j]:
                j = j+1
            else:
                return True
        return False
        
