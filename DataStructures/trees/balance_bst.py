"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Do Inorder and then construct the tree


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
    def __init__(self):
        self.nodes=list()
    def inorder_recursive(self, root):
        if root is None:return
        self.inorder_recursive(root.left)
        self.nodes.append(root.val)
        self.inorder_recursive(root.right)
        
    def inorder(self, root):
        if not root:
            return None
        
        stack=list()
        result=list()
        stack.append(root)
        
        while stack or root:
            if root:
                root=root.left
                stack.append(root)
            else:
                root=stack.pop()
                if root: 
                    result.append(root.val)
                    stack.append(root.right)
        return result
    
    def constructBST(self, inorder, start, end):
        
        if start>end:
            return None
        
        mid = (start+end)//2
        root=TreeNode(inorder[mid])
        
        root.left=self.constructBST(inorder, start=start, end=mid-1)
        root.right=self.constructBST(inorder, start=mid+1, end=end)
        
        return root
        
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        self.inorder_recursive(root)
        return self.constructBST(self.nodes, start=0, end=len(self.nodes)-1)
        
