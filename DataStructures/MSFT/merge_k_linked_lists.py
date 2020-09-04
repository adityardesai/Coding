#https://leetcode.com/problems/merge-k-sorted-lists/
# TC: O(Nlogk) where k is the number of linked lists.
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, list1, list2):
        result_list=ListNode(-1)
        traverse_ptr=result_list
        while list1 and list2:
            if list1.val<=list2.val:
                traverse_ptr.next=list1
                list1=list1.next
            else:
                traverse_ptr.next=list2
                list2=list2.next
            traverse_ptr=traverse_ptr.next

        if list1:
            traverse_ptr.next=list1
        if list2:
            traverse_ptr.next=list2        
        return result_list.next

    def merge_divide_and_conquer_2(self, lists):
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        N=len(lists)
        mid=N//2
        left=self.merge_divide_and_conquer_2(lists[:mid])
        right=self.merge_divide_and_conquer_2(lists[mid:])
        
        return self.merge_two_lists(left, right)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode: 
        if not lists:
            return None
        return self.merge_divide_and_conquer_2(lists)
        