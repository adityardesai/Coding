"""
Invert a binary tree.
https://leetcode.com/problems/invert-binary-tree
TC:O(N)
SC:O(N)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invert_iterative(self,root):
        if root is None:
            return None
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            current.right, current.left = current.left, current.right
            
            if current.right: 
                queue.append(current.right)
            if current.left: 
                queue.append(current.left)
        return root
    def invert_recursive(self, root):
        if not root:
            return None
        right = self.invert_recursive(root.right)
        left = self.invert_recursive(root.left)
        
        root.left=right
        root.right=left
        
        return root
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        #return self.invert_iterative(root)
        return self.invert_recursive(root)
