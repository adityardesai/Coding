# https://leetcode.com/problems/diagonal-traverse/
# TC:O(N*M)
# SC:O(N*M)
class Solution:
    def helper(self, matrix):
        r=len(matrix)
        c=len(matrix[0])
        diag=dict()
        for i in range(r):
            for j in range(c):
                if i+j not in diag:
                    diag[i+j] = [matrix[i][j]]
                else:
                    diag[i+j].append(matrix[i][j])
        result=[]
        for k, v in diag.items():
            i_plus_j=k
            values=v
            if i_plus_j%2==0:
                v.reverse()
                for i in v:
                    result.append(i)
            else:
                for i in v:
                    result.append(i)
        return result
                
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        
        return self.helper(matrix)
        
