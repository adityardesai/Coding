# https://leetcode.com/problems/spiral-matrix/
# TC: O(N)
# SC: O(N)
class Solution:
    def print_matrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                print(matrix[i][j])
            print()

    def helper_matrix(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        row_begin = 0
        row_end = r - 1
        col_begin = 0
        col_end = c - 1

        result = list()

        while True:
            # Travel Right
            for j in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][j])
            row_begin += 1

            if col_begin > col_end or row_begin > row_end:
                break

            # Travel Down
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if col_begin > col_end or row_begin > row_end:
                break

            # Travel Left
            for j in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][j])
            row_end -= 1

            if col_begin > col_end or row_begin > row_end:
                break

            # Travel Up
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
            col_begin += 1

            if col_begin > col_end or row_begin > row_end:
                break

        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        return self.helper_matrix(matrix)
