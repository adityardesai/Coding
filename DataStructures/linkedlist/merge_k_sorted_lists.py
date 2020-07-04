# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, list1, list2):
        result_list = ListNode(-1)
        traverse_ptr = result_list
        while list1 and list2:
            if list1.val <= list2.val:
                traverse_ptr.next = list1
                list1 = list1.next
            else:
                traverse_ptr.next = list2
                list2 = list2.next
            traverse_ptr = traverse_ptr.next

        if list1:
            traverse_ptr.next = list1
        if list2:
            traverse_ptr.next = list2
        #self.print_list(result_list.next)
        return result_list.next

    def print_list(self, node):
        if not node:
            print('empty list')
        while node:
            print(node.val)
            node = node.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        jump = 1
        print("amount " + str(amount))
        print("interval " + str(jump))
        while jump < amount:
            for i in range(0, amount - jump, jump * 2):
                lists[i] = self.merge_two_lists(lists[i], lists[i + jump])
                print("i " + str(i))
            jump *= 2
            print("interval updated " + str(jump))
        return lists[0] if amount > 0 else None
