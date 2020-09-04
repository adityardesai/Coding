class Solution:
    def print_matrix(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                print(matrix[i][j])
            print()
    def helper_matrix(self, matrix):
        
        row_begin=0
        row_end=len(matrix)-1
        col_begin=0
        col_end=len(matrix[0])-1
        result=list()
        
        while True:
            
            # Traverse Right
            for i in range(col_begin, col_end+1):
                result.append(matrix[row_begin][i])
            row_begin+=1            
            if col_begin > col_end or row_begin > row_end:
                break
            
            # Traverse Down
            for j in range(row_begin, row_end+1):
                result.append(matrix[j][col_end])
            col_end-=1
            if col_begin > col_end or row_begin > row_end:
                break
            
            # Traverse Left
            for i in range(col_end, col_begin-1,-1):
                result.append(matrix[row_end][i])
            row_end-=1
            if col_begin > col_end or row_begin > row_end:
                break
            
            # Traverse Up
            for j in range(row_end,row_begin-1, -1):
                result.append(matrix[j][col_begin])
            col_begin+=1
            if col_begin > col_end or row_begin > row_end:
                break
        return result
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        return self.helper_matrix(matrix)