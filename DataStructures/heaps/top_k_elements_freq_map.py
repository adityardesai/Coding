# https://leetcode.com/problems/top-k-frequent-elements/
# TC: O(klogk + (n-k)logk) + O(n)(freq_mpa)
# SC: O(k) + O(n)(freq_map)
from heapq import *


class Solution:
    def build_frequencies(self, nums):
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        return freq_map

    def heap_helper(self, nums, k, freq_map):

        min_heap = list()
        result = list()

        print(freq_map)

        for item, freq in freq_map.items():
            heappush(min_heap, (freq, item))

            if len(min_heap) > k:
                heappop(min_heap)
        print(min_heap)

        while min_heap:
            top = heappop(min_heap)
            result.append(top[1])

        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        freq_map = self.build_frequencies(nums)
        return self.heap_helper(nums, k, freq_map)
