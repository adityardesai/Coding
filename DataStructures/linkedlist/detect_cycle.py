#https://leetcode.com/problems/linked-list-cycle/
# TC:O(N+K), where K=cycle length and N=number of nodes
# SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
