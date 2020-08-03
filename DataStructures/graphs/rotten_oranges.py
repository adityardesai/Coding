# https://leetcode.com/problems/rotting-oranges/
# TC: O(N)
# SC: O(N)
from collections import deque

class Solution:
    def is_valid(self, grid, r, c):
        if r<0 or c<0 or r>len(grid)-1 or c>len(grid[0])-1:
            return False
        return True
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0:
            return -1
        
        queue=deque()
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        r=len(grid)
        c=len(grid[0])
        count=0
        fresh=0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
        
        while queue:
            count+=1
            for i in range(len(queue)):
                x,y=queue.popleft()
                for d in directions:
                    n_x=d[0]+x
                    n_y=d[1]+y
                    if self.is_valid(grid, n_x, n_y) and grid[n_x][n_y] == 1:
                        fresh-=1
                        grid[n_x][n_y]=2
                        queue.append((n_x,n_y))
        if fresh==0:
            return count-1
        else:
            return -1