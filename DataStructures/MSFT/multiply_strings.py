# https://leetcode.com/problems/multiply-strings
# TC:O(N)
# SC:O(N)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1=="0" or num2=="0":
            return "0"
        
        m=len(num1)
        n=len(num2)
        result=[0 for x in range(m+n)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                temp=(ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                pos_low=i+j+1
                pos_high=i+j
                temp=temp+result[pos_low]
                result[pos_low]=temp%10
                result[pos_high]=temp//10 + result[pos_high]
                
        if result[0]==0:
            result=result[1:]
        
        if len(result)==0:
            return "0"
        
        return ''.join(str(num) for num in result)
        
