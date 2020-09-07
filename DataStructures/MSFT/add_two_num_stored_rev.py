# https://leetcode.com/problems/add-two-numbers/
# TC:O(N)
# SC:O(N)
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
        
        curr1=l1
        curr2=l2
        result=ListNode()
        traverse=result
        carry=0
        
        while curr1 or curr2:
            
            x=curr1.val if curr1 else 0
            y=curr2.val if curr2 else 0
            temp_sum=x+y+carry
            new_node = ListNode(temp_sum%10)
            carry=temp_sum//10
            traverse.next=new_node
            traverse=new_node
            
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
            
        
        if carry:
            traverse.next=ListNode(carry)
        
        return result.next
