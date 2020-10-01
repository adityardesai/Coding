"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Divide and Conquer

TC:O(N+M)
SC:O(1)
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        M = len(matrix)
        if M == 0:
            return False
        
        N = len(matrix[0])
        
        i=M-1
        j=0
        while i>=0 and j<N:
            //print(matrix[i][j])
            if target < matrix[i][j]:
                //print('decrementing i')
                i = i-1
            elif target > matrix[i][j]:
                //print('incrementing j')
                j = j+1
            else:
                return True
        return False
