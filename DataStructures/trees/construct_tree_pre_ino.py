# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
        self.pre_order_index = 0
        self.inorder_map = dict()

    def helper(self, start, end):

        if start > end:
            return None

        root = TreeNode(self.preorder[self.pre_order_index])
        self.pre_order_index += 1

        index = self.inorder_map[root.val]

        root.left = self.helper(start, index - 1)
        root.right = self.helper(index + 1, end)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder or not inorder:
            return None

        for i, v in enumerate(inorder):
            self.inorder_map[v] = i

        self.preorder = preorder
        self.inorder = inorder
        start = 0
        end = len(inorder) - 1

        return self.helper(start, end)
