# https://leetcode.com/problems/sliding-window-maximum/
# https://leetcode.com/articles/sliding-window-maximum/
# TC: O(N)
# SC: O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return nums

        if len(nums) <= 1:
            return nums
        n = len(nums)

        left_arr = [0] * n
        right_arr = [0] * n

        left_arr[0] = nums[0]
        right_arr[n - 1] = nums[n - 1]

        result = list()

        for i in range(1, n):
            if i % k == 0:
                left_arr[i] = nums[i]
            else:
                left_arr[i] = max(left_arr[i - 1], nums[i])

        for j in range(n - 2, -1, -1):
            if (j + 1) % k == 0:
                right_arr[j] = nums[j]
            else:
                right_arr[j] = max(right_arr[j + 1], nums[j])

        for i in range(0, n - k + 1):
            j = i + k - 1
            result.append(max(left_arr[j], right_arr[i]))

        return result
