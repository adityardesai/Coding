"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4


https://leetcode.com/problems/kth-largest-element-in-an-array/
TC: O(NlogK)
SC: O(K)
"""
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

        return min_heap[0]

    def heap_helper_k_largest_2(self, nums, k):
        min_heap = list()
        for i in range(len(nums)):
            heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heappop(min_heap)
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

    def heap_helper_k_smallest_2(self, nums, k):
        max_heap = list()
        for i in range(len(nums)):
            heappush(max_heap, -nums[i])
            if len(max_heap) > k:
                heappop(max_heap)
        print('kth smallest is ' + str(-max_heap[0]))
        return -max_heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return nums
        #return self.brute_force_helper(nums,k)
        self.heap_helper_k_smallest_2(nums, k)
        return self.heap_helper_k_largest_2(nums, k)
