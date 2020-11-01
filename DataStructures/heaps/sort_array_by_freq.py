"""

https://leetcode.com/problems/sort-array-by-increasing-frequency/

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

"""

class CustomPair(object):
    
    def __init__(self, num, freq):
        self.num=num
        self.freq=freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.num > other.num
        return self.freq < other.freq
    def __str__(self):
        return str(self.freq) + ':' + str(self.num) 

class Solution(object):
    def print_heap(self, h):
        while h:
            print(heappop(h))

    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        freq_map = collections.Counter(nums)
        heap=list()
        res=list()
        
        for k,v in freq_map.items():
            heapq.heappush(heap, CustomPair(k,v))
        
        sample_heap=list(heap)
        #self.print_heap(sample_heap)
        
        while heap:
            val = heapq.heappop(heap)
            for i in range(val.freq):
                res.append(val.num)
        return res
    
    
        
