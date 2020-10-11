"""
In a binary tree, a lonely node is a node that is the only child of its parent node. The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. Return the list in any order.

TC: O(N)
SC: O(N)

Level Order
 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        queue=deque()
        result=list()
        queue.append(root)
        
        while queue:
            level=len(queue)
            for i in range(level):
                node=queue.popleft()
                if not node.left and node.right: result.append(node.right.val)
                if not node.right and node.left: result.append(node.left.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result        
        
