"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.


Similar to the number of Island problem. But just return the area. 

TC: O(R*C)
SC: O(R*C)

https://leetcode.com/problems/max-area-of-island/

"""


class Solution:
    def isValid(self,grid,i,j):
        if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1:
            return False
        return True
    
    def dfs(self,grid,i,j,area):
        grid[i][j]=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        area+=1
        for d in directions:
            n_x=d[0]+i
            n_y=d[1]+j
            if self.isValid(grid,n_x,n_y) and grid[n_x][n_y]==1:
                area=max(self.dfs(grid,n_x,n_y,area), area)
        return area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0    
        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(self.dfs(grid,i,j,0),area)
        return area
