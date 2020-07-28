# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# TC: O(N)
# SC: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def helper(self, head):
        dummy_head = Node(0, None, head, None)
        stack = list()
        stack.append(head)
        prev = dummy_head

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr

        head.prev = None
        return dummy_head.next

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        return self.helper(head)
