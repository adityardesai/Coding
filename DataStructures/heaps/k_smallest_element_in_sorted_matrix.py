from heapq import *


class Solution:
    def binary_search_helper(self, matrix, k):
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            count = self.count_less_than_mid(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

    def count_less_than_mid(self, matrix, mid):
        count = 0
        row = len(matrix)
        col = len(matrix[0])

        i = 0
        j = row - 1
        for i in range(row):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count = count + 1 + j

        return count

    def heap_helper(self, matrix, k):
        """
        m=min(N,k)
        TC: O(mlog(m)) + O(klog(k))
        SC: O(m)
        """
        min_heap = list()
        N = len(matrix)
        min_value = min(N, k)
        for r in range(min_value):
            heappush(min_heap, (matrix[r][0], r, 0))

        while k:
            element, row, column = heappop(min_heap)
            if column < N - 1:
                heappush(min_heap, (matrix[row][column + 1], row, column + 1))

            k -= 1
        return element

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return matrix

        #return self.heap_helper(matrix, k)
        return self.binary_search_helper(matrix, k)
