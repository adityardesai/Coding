"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


TC: O(N+M)
SC: O(N+M)
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        i=0
        j=0
        result=list()
        
        while i<len(A) and j<len(B):
            a_start=A[i][0]
            a_end=A[i][1]
            
            b_start=B[j][0]
            b_end=B[j][1]
            
            #cris cross
            if a_start<=b_end and b_start<=a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])
            
            
            if a_end<=b_end:
                i+=1
            else:
                j+=1
            
        
        return result
                
        
