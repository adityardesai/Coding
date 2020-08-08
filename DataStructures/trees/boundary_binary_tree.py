# https://leetcode.com/problems/boundary-of-binary-tree
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False
    def traverse_leaves(self, root, result):
        if self.is_leaf(root):
            result.append(root.val)
        else:
            if root.left:
                self.traverse_leaves(root.left, result)
            if root.right:
                self.traverse_leaves(root.right, result)
        
    def traverse_left(self, root, result):
        node=root.left
        while node:
            if not self.is_leaf(node):
                result.append(node.val)
            if node.left:
                node=node.left
            else:
                node=node.right
        
    def traverse_right(self, root, result):
        stack=list()
        node=root.right
        while node:
            if not self.is_leaf(node):
                stack.append(node)
            if node.right:
                node=node.right
            else:
                node=node.left
        
        while stack:
            temp_node=stack.pop()
            result.append(temp_node.val)
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        result=list()
        
        if not root:
            return root
        
        if not self.is_leaf(root):
            result.append(root.val)
        
        self.traverse_left(root, result)
        self.traverse_leaves(root, result)
        self.traverse_right(root, result)
        
        return result