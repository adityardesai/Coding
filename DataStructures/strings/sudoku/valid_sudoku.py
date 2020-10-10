"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

TC:O(1) : 81 cells so constant
SC:O(1)
"""

class Solution:
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [{} for i in range(9)]
        cols = [{} for j in range(9)]
        boxes = [{} for k in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num!='.':  
                    num = int(num)
                    
                    # Check for row and cols
                    rows[i][num] = rows[i].get(num,0)+1
                    cols[j][num] = cols[j].get(num,0)+1
                
                    
                    # Check for box
                    box_index = (i//3) * 3 + j//3
                    boxes[box_index][num] = boxes[box_index].get(num,0)+1
        
                    if rows[i][num]>1 or cols[j][num]>1 or boxes[box_index][num]>1:
                        return False
        return True
        
