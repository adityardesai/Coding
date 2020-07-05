# https://leetcode.com/problems/inorder-successor-in-bst/
# TC:O(Height of the tree)
# SC:O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorder_iterative_binary_tree(self, root, p):
        """
        This is normal inorder iterative version
        """
        stack = list()
        result = list()
        temp = root

        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                result.append(temp)
                temp = temp.right

        k = self.find_next(result, p)

        return k

    def find_next(self, result, p):
        for i in range(len(result)):
            if result[i].val == p.val:
                break

        if i + 1 < len(result):
            return result[i + 1]
        else:
            return None

    def inorder_bst(self, root, p):

        successor = None

        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return -1
        #return self.inorder_iterative_binary_tree(root, p)
        return self.inorder_bst(root, p)
