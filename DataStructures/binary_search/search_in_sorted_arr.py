# https://leetcode.com/problems/search-in-rotated-sorted-array/
# TC: O(logN)
# SC: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = len(nums)

        low = 0
        high = L - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[low]:
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
