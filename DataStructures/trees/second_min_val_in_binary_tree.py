"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

TC:O(N)
SC:O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_helper(self, root, unique_set):
        if root:
            unique_set.add(root.val)
            self.dfs_helper(root.left, unique_set)
            self.dfs_helper(root.right, unique_set)

    def dfs(self, root):
        unique_set=set()
        self.dfs_helper(root, unique_set)
        
        min1=root.val
        ans=float('inf')
        
        for item in unique_set:
            if min1<item<ans:
                ans=item
        
        if ans<float('inf'):
            return ans
        else:
            return -1

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self.dfs(root)
        
