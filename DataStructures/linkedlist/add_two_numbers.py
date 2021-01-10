# https://leetcode.com/problems/add-two-numbers/
# TC: O(max(m,n))
# SC: O(max(m,n))
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        result = ListNode(0)
        traverse = result
        carry=0
        
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            temp_sum = x+y+carry
            new_node = ListNode(temp_sum%10)
            carry = temp_sum//10
            traverse.next = new_node
            traverse = new_node
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
                
        
        if carry:
            traverse.next = ListNode(carry)
        
        return result.next
