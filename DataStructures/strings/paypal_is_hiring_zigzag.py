# https://leetcode.com/problems/zigzag-conversion/
# TC:O(N)
# SC:O(N)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows==1:
            return s
        rows=[""] * numRows
        cur_row=0
        up=False
        
        for ch in s:
            rows[cur_row]+=ch
            
            if cur_row==0 or cur_row==numRows-1:
                up=not up
            
            if up:
                cur_row+=1
            else:
                cur_row-=1
        
        return ''.join([row for row in rows])
                
