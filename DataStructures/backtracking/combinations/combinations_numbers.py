# https://leetcode.com/problems/combinations/


class Solution:
    def backtrack(self, n, k, temp_list, result, start):
        if len(temp_list) == k:
            result.append(list(temp_list))
            return
        else:
            for num in range(start, n + 1):
                temp_list.append(num)
                self.backtrack(n, k, temp_list, result, num + 1)
                temp_list.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:

        if not n or not k:
            return None

        temp_list = list()
        result = list()
        start = 1

        self.backtrack(n, k, temp_list, result, start)
        return result
