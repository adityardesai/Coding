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

Time Complexity:In the worst case, we could have a complete binary tree and if that is the case, then there would be N/2N/2 leafs. 
For every leaf, we perform a potential O(N)O(N) operation of copying over the pathNodes nodes to a new list to be added to the final pathsList. 
Hence, the complexity in the worst case could be O(N^2)

Space Complexity: O(N)O(N). The space complexity, like many other problems is debatable here. 
I personally choose not to consider the space occupied by the output in the space complexity. So, all the new lists that we create for the paths are actually
a part of the output and hence, don't count towards the final space complexity. The only additional space that we use is the pathNodes list to keep track of nodes along a branch.
We could include the space occupied by the new lists (and hence the output) in the space complexity and in that case the space would be O(N^2). 
There's a great answer on Stack Overflow about whether to consider input and output space in the space complexity or not. I prefer not to include them.
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
        
