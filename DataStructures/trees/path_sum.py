"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.


TC: O(N)
SC: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_helper(self, node, sum_so_far):
        if not node:
            return False
        sum_so_far-=node.val
        if not node.left and not node.right:
            if sum_so_far==0:
                return True
        return self.helper(node.left, sum_so_far) or self.helper(node.right, sum_so_far)
    
    def iterative_helper(self, node, sum_so_far):
        
        stack=list()
        stack.append((node, sum_so_far-node.val))
        
        while stack:
            node, sum_so_far=stack.pop()
            if not node.left and not node.right and sum_so_far==0:
                return True
            if node.right:
                stack.append((node.right, sum_so_far-node.right.val))
            if node.left:
                stack.append((node.left, sum_so_far-node.left.val))
        return False
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        #return self.recursive_helper(root, sum)
        return self.iterative_helper(root, sum)
        
