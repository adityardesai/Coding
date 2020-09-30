"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. 
The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. 
You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Solution
The path that cuts through the minimum number of bricks is the path that passes through the most brick edges/endpoints.
We can keep a map where we count where each brick ends as a distance from the left-most point (i.e. from 0).
We build this map on a per-row basis, as we want to find out where each brick ends, and how many times each brick ends on the same point.
We also want to ignore the right-most brick's endpoint, since both the left-most and right-most edges of the wall are ignored as solutions.
The solution is the number of rows of bricks (i.e. len(wall)) minus the maximum of the number of rows you can avoid by cutting through a certain brickEndpoint.

https://leetcode.com/problems/brick-wall/
Ref: https://leetcode.com/problems/brick-wall/discuss/788421/Python-3-%2B-Dictionary-Explanation

TC: O(N)
SC: O(N)
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brick_ends_to_count=dict()
        
        for bricks in wall:
            brick_end_pt=0
            for i in range(len(bricks)-1):
                
                brick = bricks[i]
                brick_end_pt+=brick
                
                if brick_end_pt in brick_ends_to_count:
                    brick_ends_to_count[brick_end_pt]+=1
                else:
                    brick_ends_to_count[brick_end_pt]=1
        
        max_sum=0
        if brick_ends_to_count:
            max_sum = max(brick_ends_to_count.values())
        
        return len(wall) - (max_sum if max_sum else 0)
        
