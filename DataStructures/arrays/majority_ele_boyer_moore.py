# https://leetcode.com/problems/majority-element-ii/
# TC:O(N)
# SC:O(1)
class Solution:
    def brute_force(self, nums):
        length=len(nums)
        N=math.floor(length/3)
        result_map = dict()
        result = list()
        
        for n in nums:
            result_map[n] = result_map.get(n,0)+1
        
        for k,v in result_map.items():
            if v>N:
                result.append(k)
        
        return result
    def boyer_moore_voting_algorithm(self, nums):
        count1=0
        count2=0
        candidate1=None
        candidate2=None
        
        for n in nums:
            if candidate1==n:
                count1+=1
            elif candidate2==n:
                count2+=1
            elif count1==0:
                candidate1=n
                count1+=1
            elif count2==0:
                candidate2=n
                count2+=1
            else:
                count1-=1
                count2-=1
        result=list()
        
        count1=0
        count2=0
        
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c) 
        return result
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        #return self.brute_force(nums)
        return self.boyer_moore_voting_algorithm(nums)
        
        
        