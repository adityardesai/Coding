# https://leetcode.com/problems/add-two-numbers-ii/
# TC:O(N)
# SC:O(N)
# Brute force would be to reverse the linked list and then do normal add
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper_stack(self, l1, l2):

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        result = ListNode(0)
        traverse_ptr = result
        sum = 0

        while stack1 or stack2:
            if stack1:
                sum = sum + stack1.pop()
            if stack2:
                sum = sum + stack2.pop()

            remainder = sum % 10
            sum = sum // 10

            traverse_ptr.val = remainder
            new_node = ListNode(sum)
            new_node.next = traverse_ptr
            traverse_ptr = new_node

        if traverse_ptr.val:
            return traverse_ptr
        else:
            return traverse_ptr.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        return self.helper_stack(l1, l2)
