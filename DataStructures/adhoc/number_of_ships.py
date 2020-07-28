# https://leetcode.com/problems/number-of-ships-in-a-rectangle/
# TC: O(N) Number of points
# SC: O(1)
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y


class Solution(object):
    def __init__(self):
        self.sea = None

    def dfs_helper(self, bottom, top):
        if bottom.x > top.x or bottom.y > top.y:
            return 0
        if (top.x, top.y) == (bottom.x, bottom.y):
            return self.sea.hasShips(top, bottom)
        else:
            if not self.sea.hasShips(top, bottom):
                return 0
            center_x = (bottom.x + top.x) // 2
            center_y = (bottom.y + top.y) // 2

            area1 = self.dfs_helper(bottom, Point(center_x, center_y))
            area2 = self.dfs_helper(Point(center_x + 1, center_y + 1), top)
            area3 = self.dfs_helper(Point(bottom.x, center_y + 1),
                                    Point(center_x, top.y))
            area4 = self.dfs_helper(Point(center_x + 1, bottom.y),
                                    Point(top.x, center_y))

            return area1 + area2 + area3 + area4

    def countShips(self, sea: 'Sea', topRight: 'Point',
                   bottomLeft: 'Point') -> int:

        if not sea or not topRight or not bottomLeft:
            return
        self.sea = sea
        return self.dfs_helper(bottomLeft, topRight)
