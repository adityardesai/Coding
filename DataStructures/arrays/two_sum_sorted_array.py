# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# TC:O(N)
# SC:O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        low = 0
        high = len(numbers) - 1

        while low < high:
            temp_sum = numbers[low] + numbers[high]
            if temp_sum == target:
                return [low + 1, high + 1]
            elif temp_sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
