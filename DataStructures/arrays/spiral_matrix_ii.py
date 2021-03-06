"""
https://leetcode.com/problems/spiral-matrix-ii

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        
        row_begin=0
        col_begin=0
        
        row_end=n-1
        col_end=n-1
        
        result=[[0 for _ in range(n)] for _ in range(n)]
        count=1
        
        while True:
            for i in range(col_begin, col_end+1):
                result[row_begin][i]=count
                count+=1
            
            row_begin+=1
            if row_begin>row_end or col_begin>col_end:
                break
            
            for i in range(row_begin, row_end+1):
                result[i][col_end]=count
                count+=1

            col_end-=1
            if row_begin>row_end or col_begin>col_end:
                break
            
            for i in range(col_end, col_begin-1,-1):
                result[row_end][i]=count
                count+=1
            
            row_end-=1
            if row_begin>row_end or col_begin>col_end:
                break
            
            for i in range(row_end, row_begin-1,-1):
                result[i][col_begin]=count
                count+=1
            
            col_begin+=1
            if row_begin>row_end or col_begin>col_end:
                break
        
        print(result)
        return result 
