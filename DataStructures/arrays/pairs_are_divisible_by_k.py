# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
# TC:
# SC:

class Solution:
    def helper(self, arr, k):
        """
        This will not work for many test cases
        """
        s=sum(arr)
        if s%k==0:
            return True
        else:
            return False
    def helper2(self, arr, k):
        if len(arr)%2:
            return False
        
        hash_map=dict()
        
        count=0
        for i in range(len(arr)):
            a=arr[i]
            b=k-(a%k)
            if b in hash_map and hash_map[b]>=1:
                count+=1
                hash_map[b]-=1
            else:
                hash_map[(a%k) or k]=hash_map.get(a%k,0)+1
        return count == len(arr)//2

    def canArrange(self, arr: List[int], k: int) -> bool:
        return self.helper2(arr, k)
        
        
