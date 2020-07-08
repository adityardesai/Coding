# https://leetcode.com/problems/reverse-linked-list/
# TC:O(N)
# SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_iterative(self, head):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head
        return self.reverse_iterative(head)
