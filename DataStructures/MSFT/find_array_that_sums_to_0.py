# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# TC: O(n)
# SC: O(1)

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if not n:
            return n
        mid=n//2
        
        result=list()
        if not n%2==0:
            result.append(0)
        
        for i in range(1,mid+1):
            result.append(i)
            result.append(i * -1)
        
        print(result)
        return result
        
