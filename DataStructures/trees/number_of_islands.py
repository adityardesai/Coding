# https://leetcode.com/problems/number-of-islands/
# TC: O(M*N)
# SC: O(M*N)


class Solution:
    from collections import deque

    def _is_valid(self, grid, r, c):
        if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1:
            return False
        return True

    def dfs(self, grid, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid[x][y] = '0'
        for d in DIRECTIONS:
            new_x = x + d[0]
            new_y = y + d[1]
            if self._is_valid(grid, new_x,
                              new_y) and grid[new_x][new_y] == '1':
                self.dfs(grid, new_x, new_y)

    def bfs(self, grid, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid[x][y] = '0'
        queue = collections.deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for d in DIRECTIONS:
                new_x = x + d[0]
                new_y = y + d[1]
                if self._is_valid(grid, new_x,
                                  new_y) and grid[new_x][new_y] == '1':
                    queue.append((new_x, new_y))

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        r = len(grid)
        c = len(grid[0])
        count = 0

        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1':
                    count += 1
                    self.dfs(grid, x, y)
        return count
