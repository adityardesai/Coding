# https://leetcode.com/problems/merge-two-sorted-lists/
# TC: O(N+M)
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        result = ListNode(-1)
        traverse_ptr = result

        while l1 and l2:
            if l1.val <= l2.val:
                traverse_ptr.next = l1
                l1 = l1.next
            else:
                traverse_ptr.next = l2
                l2 = l2.next
            traverse_ptr = traverse_ptr.next

        if l1:
            traverse_ptr.next = l1
        if l2:
            traverse_ptr.next = l2

        return result.next
