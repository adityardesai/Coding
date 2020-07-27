# https://leetcode.com/problems/kth-smallest-element-in-a-bst
# TC: O(H+k) H=height of tree k=elements in stack
# SC: O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, result_list):
        if root.left:
            self.inorder(root.left, result_list)
        result_list.append(root.val)
        if root.right:
            self.inorder(root.right, result_list)

    def brute_force(self, root, k):
        result_list = list()
        self.inorder(root, result_list)
        return result_list[k - 1]

    def inorder_iterative(self, root, k):
        stack = list()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k = k - 1
                if k == 0:
                    return root.val
                root = root.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #return self.brute_force(root,k)
        return self.inorder_iterative(root, k)
