#https://leetcode.com/problems/shuffle-an-array/
# TC:O(N)
# SC:O(N)
class Solution:
    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.copy = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.copy)):
            swap_idx = random.randrange(i, len(self.copy))
            self.copy[i], self.copy[swap_idx] = self.copy[swap_idx], self.copy[
                i]
        return self.copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
