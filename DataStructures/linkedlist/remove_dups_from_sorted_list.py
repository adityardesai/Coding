"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
TC:O(N)
SC:O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        
        current = head
        
        while current!=None and current.next!=None:
            if current.next.val == current.val:
                current.next=current.next.next
            else:
                current = current.next
        
        return head
