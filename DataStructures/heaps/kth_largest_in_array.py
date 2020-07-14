# https://leetcode.com/problems/kth-largest-element-in-an-array/
# TC: O(NlogK)
# SC: O(K)
from heapq import *


class Solution:
    def brute_force_helper(self, nums, k):
        nums.sort()
        i = len(nums) - 1
        while k > 0:
            i -= 1
            k -= 1
        return nums[i + 1]

    def heap_helper_k_largest(self, nums, k):
        """
        TC: O(KlogK) + O((N-K)logK) ~ O(NlogK)
        SC: O(K)
        """
        min_heap = list()

        for i in range(k):
            heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        print('kth largest ' + str(min_heap[0]))
        return min_heap[0]

    def heap_helper_k_smallest(self, nums, k):
        """
        TC: O(KlogK) + O((N-K)logK) ~ O(NlogK)
        """
        max_heap = list()

        for i in range(k):
            heappush(max_heap, -nums[i])

        for i in range(k, len(nums)):
            if -nums[i] > max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -nums[i])
        print('kth smallest ' + str(-max_heap[0]))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums
        #return self.brute_force_helper(nums,k)
        self.heap_helper_k_smallest(nums, k)
        return self.heap_helper_k_largest(nums, k)
