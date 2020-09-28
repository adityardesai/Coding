"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
[
   [5,4,11,2],
   [5,8,4,5]
]

https://leetcode.com/problems/path-sum-ii/
TC: O(N^2)
SC: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def recursive_helper(self, node, res, temp, sum_so_far):
        if not node:
            return False
        
        temp.append(node.val)
        
        if not node.left and not node.right and sum_so_far==node.val:
            res.append(list(temp))
        else:
            self.recursive_helper(node.left, res, temp, sum_so_far-node.val)
            self.recursive_helper(node.right, res, temp, sum_so_far-node.val)
        
        temp.pop()  # Backtrack

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        result=list()
        temp_list=list()
        
        self.recursive_helper(root, result, temp_list, sum)
        return result
        
