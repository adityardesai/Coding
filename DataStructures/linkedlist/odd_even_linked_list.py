# https://leetcode.com/problems/odd-even-linked-list/
# TC:O(N)
# SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        curr_odd = head
        curr_even = head.next
        even_head = curr_even

        while curr_even and curr_even.next:
            curr_odd.next = curr_odd.next.next
            curr_odd = curr_odd.next
            curr_even.next = curr_even.next.next
            curr_even = curr_even.next

        curr_odd.next = even_head
        return head
