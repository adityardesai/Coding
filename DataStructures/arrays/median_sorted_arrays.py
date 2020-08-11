# https://leetcode.com/problems/median-of-two-sorted-arrays/
# TC:O(log(min(m,n)))
# SC:O(1)
class Solution:
    def binary_search_helper(self, nums1, nums2):
        x=len(nums1)
        y=len(nums2)
        
        low=0
        high=x
        
        while(low<=high):
            
            p_x=(low+high)//2            
            p_y=(x+y+1)//2 - p_x
            
            max_left_x = float('-inf') if p_x==0 else nums1[p_x-1]
            max_left_y = float('-inf')  if p_y==0 else nums2[p_y-1]
            min_right_x = float('inf') if p_x==x else nums1[p_x]
            min_right_y = float('inf') if p_y==y else nums2[p_y]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if ((x+y) % 2 == 0):
                    a=max(max_left_x, max_left_y)
                    b=min(min_right_x, min_right_y)
                    print(a,b)
                    return (a+b)/2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high=p_x-1
            else:
                low=p_x+1
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.binary_search_helper(nums2,nums1)
        else:
            return self.binary_search_helper(nums1,nums2)
        
        