# https://leetcode.com/problems/perfect-squares/
# TC:O(E+V)
# SC:O(E+V)
from collections import deque


class Solution:
    def construct_perfect_squares(self, n, nums):
        sq_root = int(sqrt(n))
        for i in range(1, sq_root + 1):
            nums.append(i * i)

    def numSquares(self, n: int) -> int:
        if not n or n <= 1:
            return n

        sq_nums = list()
        self.construct_perfect_squares(n, sq_nums)

        queue = deque()
        queue.append(n)
        level = 0

        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                for sq_num in sq_nums:
                    if sq_num == node:
                        return level
                    elif node < sq_num:
                        break
                    else:
                        queue.append(node - sq_num)
        return level
