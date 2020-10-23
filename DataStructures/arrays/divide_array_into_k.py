"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/submissions/
"""



from heapq import *
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        L=len(nums)
        
        if k==1:return True
        if L%k: return False
        
        count=defaultdict(int)
        heapify(nums)
        
        for num in nums:
            count[num]+=1
        
        for i in range(L//k):
            start=heappop(nums)
            
            while count[start]==0:
                start=heappop(nums)
            
            for i in range(k):
                count[start]-=1
                if count[start]<0: return False
                start+=1
        
        return True
=============================================
https://leetcode.com/problems/hand-of-straights

from heapq import *
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        L=len(hand)
        
        # If remainder is  there then we cannot split
        if L%W: return False
        if W==1: return True
        
        heapify(hand)
        count = defaultdict(int) # Count

        for i in range(len(hand)):
            count[hand[i]]+=1
        
        for i in range(L//W):
            start=heappop(hand)
            
            while count[start]==0:
                start=heappop(hand)
            
            for i in range(W):
                count[start]-=1
                if count[start]<0: return False
                start+=1
        
        return True
