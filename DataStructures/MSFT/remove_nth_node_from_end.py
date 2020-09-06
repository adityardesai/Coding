# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# TC:O(N)
# SC:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        count=0
        while head:
            count+=1
            head=head.next
        return count
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        dummy_head=ListNode(-1)
        dummy_head.next=head
        
        length=self.count(dummy_head)
        target_node=length-n-1
        curr=dummy_head
        for i in range(target_node):
            curr=curr.next
        curr.next=curr.next.next 
        return dummy_head.next
