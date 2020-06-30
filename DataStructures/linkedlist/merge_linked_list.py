# https://leetcode.com/problems/sort-list
# TC: O(n) + O(n+m
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self, node):
        if not node:
            return node

        slow = node
        fast = node.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        return slow

    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        result = ListNode(-1)
        traverse = result

        while list1 and list2:
            if list1.val <= list2.val:
                traverse.next = list1
                list1 = list1.next
            else:
                traverse.next = list2
                list2 = list2.next
            traverse = traverse.next

        if list1:
            traverse.next = list1
        if list2:
            traverse.next = list2

        return result.next

    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        mid = self.middle(head)
        first = head
        second = mid.next
        mid.next = None

        first_part = self.sortList(first)
        second_part = self.sortList(second)

        return self.merge(first_part, second_part)
