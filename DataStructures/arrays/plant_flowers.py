"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

TC:O(N)
SC:O(N)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_plant=0
        L=len(flowerbed)
        for i in range(L):
            position=flowerbed[i]
            if (position==0 
                and (i==L-1 or flowerbed[i+1] == 0) 
                and (flowerbed[i-1]==0 or i==0)):
                flowerbed[i]=1
                can_plant+=1
        
        return can_plant>=n
        
