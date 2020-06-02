# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def add_two_numbers(l1, l2):

        if not l1:
            return l2

        if not l2:
            return l1

        result_list = ListNode(0)
        traverse = result_list
        carry = 0

        while l1 or l2:
            temp_sum = l1.val + l2.val + carry
            new_node = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            traverse.next = new_node
            traverse = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            traverse.next = ListNode(carry)

        return result_list.next


l1_input = ListNode(2)
l1_input.next = ListNode(4)
l1_input.next.next = ListNode(3)

l2_input = ListNode(5)
l2_input.next = ListNode(6)
l2_input.next.next = ListNode(4)

result = Solution().add_two_numbers(l1_input, l2_input)

while result:
    print(result.val)
    result = result.next
