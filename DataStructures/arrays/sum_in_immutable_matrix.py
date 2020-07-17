class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.dp_matrix = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.dp_matrix[i][j] = (self.dp_matrix[i - 1][j] +
                                        self.dp_matrix[i][j - 1] +
                                        self.matrix[i - 1][j - 1] -
                                        self.dp_matrix[i - 1][j - 1])
        print('\n'.join([
            ''.join(['{:4}'.format(item) for item in row])
            for row in self.dp_matrix
        ]))

    def brute_force(self, row1, col1, row2, col2):
        result = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                result += self.matrix[i][j]
        return result

    def dynamic_helper(self, row1, row2, col1, col2):
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        return (self.dp_matrix[row2][col2] - self.dp_matrix[row1 - 1][col2] -
                self.dp_matrix[row2][col1 - 1] +
                self.dp_matrix[row1 - 1][col1 - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #return self.brute_force(row1,col1,row2,col2)
        return self.dynamic_helper(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
