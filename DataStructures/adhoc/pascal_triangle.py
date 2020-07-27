# https://leetcode.com/articles/pascals-triangle/
# TC: O(numRows^2)
# SC: O(numRows^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if not numRows:
            return []
        result=[[1]]
        
        if numRows==0:
            return []
        elif numRows==1:
            return result
        
        for i in range(1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
            
        return result
            