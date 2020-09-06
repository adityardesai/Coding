class Solution:
    def reverse(self, x: int) -> int:
        
        flag=False
        
        if x<0:
            x=x*(-1)
            flag=True
        
        res = 0
        while (x>0):
            a=x%10
            x=x//10
            res=res*10 + a
        
        if res>2**31 or res<2**-31:
            return 0
        
        if flag:
            res=res*(-1)
       
        return res
            
        
