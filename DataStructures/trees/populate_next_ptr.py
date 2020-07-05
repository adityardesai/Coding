"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def helper(self, root):
        curr1 = root
        while curr1:
            curr2 = curr1
            while curr2:
                if curr2.left and curr2.right:
                    curr2.left.next = curr2.right
                if curr2.right and curr2.next:
                    curr2.right.next = curr2.next.left
                curr2 = curr2.next
            curr1 = curr1.left
        return root

    def helper_level_order(self, root):
        from collections import deque

        queue = deque()
        queue.append(root)
        prev = None

        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        #return self.helper(root)
        return self.helper_level_order(root)
