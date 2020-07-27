# https://leetcode.com/articles/reverse-linked-list-ii/
# TC: O(N)
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper_iterative(self, head, m, n):
        if not head:
            return None
        
        curr=head
        prev=None
        
        while m>1:
            prev=curr
            curr=curr.next
            m=m-1
            n=n-1
        
        tail=curr
        connection=prev
        
        while n:
            third=curr.next
            curr.next=prev
            prev=curr
            curr=third
            n=n-1
        
        tail.next=curr
        if connection:
            connection.next=prev
        else:
            head=prev
        return head
    def helper_dummy_node(self, head,m,n):
        if not head:
            return None
        
        dummy_node=ListNode(0)
        first_prev=dummy_node
        dummy_node.next=head
        
        for i in range(m-1):
            first_prev=first_prev.next
        
        current=first_prev.next
        prev=None
        
        for i in range(n-m+1):
            third=current.next
            current.next=prev
            prev=current
            current=third
        
        first_prev.next.next=current
        first_prev.next=prev
        
        return dummy_node.next
        
        
        
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not m or not n:
            return None
        #return self.helper_iterative(head, m, n)
        return self.helper_dummy_node(head, m, n)
        
        