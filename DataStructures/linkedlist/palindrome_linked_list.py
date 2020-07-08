# https://leetcode.com/problems/palindrome-linked-list/
# TC:O(2N)
# SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle(self, head):
        if not head:
            return None
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_linked_list(self, head):

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        middle = self.find_middle(head)
        original_head = head
        new_head = self.reverse_linked_list(middle)
        temp_new_head = new_head
        result = True

        while new_head != None:

            if original_head.val != new_head.val:
                result = False
            original_head = original_head.next
            new_head = new_head.next

        middle.next = self.reverse_linked_list(temp_new_head)
        return result
