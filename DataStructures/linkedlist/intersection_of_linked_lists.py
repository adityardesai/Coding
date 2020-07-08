# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def interesection_by_set(self, headA, headB):
        """
        TC:O(N+M)
        SC:O(N+M)
        """
        m_set = set()
        while headA:
            m_set.add(headA)
            headA = headA.next

        while headB:
            if headB in m_set:
                return headB
            headB = headB.next
        return None

    def intersection_by_two_ptrs(self, headA, headB):
        """
        TC:O(N+M)
        SC:O(1)
        """
        ptrA = headA
        ptrB = headB

        lenA = 0
        lenB = 0

        while ptrA:
            lenA += 1
            ptrA = ptrA.next

        while ptrB:
            lenB += 1
            ptrB = ptrB.next

        ptrA = headA
        ptrB = headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for i in range(lenB - lenA):
                ptrB = ptrB.next

        while ptrA and ptrB:
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next

        return None

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None

        #return self.interesection_by_set(headA, headB)
        return self.intersection_by_two_ptrs(headA, headB)
