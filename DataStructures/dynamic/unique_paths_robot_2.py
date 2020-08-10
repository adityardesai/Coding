# https://leetcode.com/problems/unique-paths-ii/
# TC: O(M*N)
# SC: O(1)
class Solution:
    def dynamic_helper(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1:
            return 0

        grid[0][0] = 1

        for i in range(1, m):
            grid[i][0] = int(grid[i][0] == 0 and grid[i - 1][0] == 1)

        for j in range(1, n):
            grid[0][j] = int(grid[0][j] == 0 and grid[0][j - 1] == 1)

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = 0

        return grid[m - 1][n - 1]

    def dynamic_helper2(self, grid):
        """
        TC:O(N*M)
        SC:O(N*M)
        """
        m = len(grid)
        n = len(grid[0])
        paths = [[0] * n for x in range(m)]

        for i in range(m):
            if grid[i][0] == 1:
                paths[i][0] = 0
                break
            else:
                paths[i][0] = 1

        for j in range(n):
            if grid[0][j] == 1:
                paths[0][j] = 0
                break
            else:
                paths[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dynamic_helper(obstacleGrid)
