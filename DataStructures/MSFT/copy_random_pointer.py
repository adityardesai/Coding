# https://leetcode.com/problems/copy-list-with-random-pointer/
# TC:O(N)
# SC:O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        hash_map=dict()
        curr=head
        
        while curr:
            hash_map[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        
        while curr:
            cloned_node=hash_map.get(curr)
            cloned_node.next=hash_map.get(curr.next)
            cloned_node.random=hash_map.get(curr.random)
            curr=curr.next
        
        return hash_map.get(head)
