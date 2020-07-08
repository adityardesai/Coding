# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# TC: O(N)+O(M)
# SC: O(N)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mlist = list()
        dict1 = dict()

        big = nums1
        small = nums2
        if len(nums1) < len(nums2):
            big = nums2
            small = nums1

        for n in big:
            dict1[n] = dict1.get(n, 0) + 1

        for m in small:
            if m in dict1 and dict1[m] > 0:
                dict1[m] = dict1[m] - 1
                mlist.append(m)

        return mlist
