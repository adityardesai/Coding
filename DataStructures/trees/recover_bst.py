# https://leetcode.com/problems/recover-binary-search-tree/
# TC:O(N)
# SC:O(H) H=height of the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack=list()
        x=y=pred=None
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                if pred and root.val < pred.val:
                    y=root
                    if not x:
                        x=pred
                    else:
                        break
                pred=root
                root=root.right

        x.val, y.val = y.val, x.val
