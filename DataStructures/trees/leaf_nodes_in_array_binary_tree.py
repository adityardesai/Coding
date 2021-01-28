"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

TC:O(N)
SC:O(N)
Depth at given node = max(depth of left, depth of right)+1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result=collections.defaultdict(list)
    
    def dfs_helper(self,root,level):
        if not root:
            return level
        left=self.dfs_helper(root.left,level)
        right=self.dfs_helper(root.right,level)
        level=max(left,right)
        self.result[level].append(root.val)
        return level+1
    
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dfs_helper(root,level=0)
        return self.result.values()
