# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder=list()
        self.postorder=list()
        self.inorder_map=dict()
        
    def helper(self, start, end):
        
        if start>end:
            return None
        
        root = self.postorder.pop()
        root_node = TreeNode(root)
        
        root_idx=self.inorder_map[root]
        
        root_node.right=self.helper(start=root_idx+1, end=end)
        root_node.left=self.helper(start=start,end=root_idx-1)
        
        
        return root_node
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not inorder or not postorder:
            return None
        
        for i in range(len(inorder)):
            self.inorder_map[inorder[i]]=i
        
        self.inorder=inorder
        self.postorder=postorder
        start=0
        end=len(inorder)-1

        return self.helper(start,end)
        