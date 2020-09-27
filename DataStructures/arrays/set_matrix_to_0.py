"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

TC: O(MXN)
SC: O(1)

https://leetcode.com/problems/set-matrix-zeroes

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        col_zero = False
        
        # find 0's
        for i in range(r):
            # if 0 in first column, entire first column should be 0
            if matrix[i][0] == 0:
                col_zero = True
            
            # check 0 in other cells
            for j in range(1,c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        # set 0s
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0 
        
        # if first row and col is zero, entire first col is 0
        if matrix[0][0]==0:
            for j in range(c):
                matrix[0][j]=0
        
        # if 0 in first column
        if col_zero:
            for i in range(r):
                matrix[i][0]=0
