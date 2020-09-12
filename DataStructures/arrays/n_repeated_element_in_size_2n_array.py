# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# TC:O(N)
# SC:O(1)

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        mset=set()
        for a in A:
            if a not in mset:
                mset.add(a)
            else:
                return a
