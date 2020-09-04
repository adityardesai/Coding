# https://leetcode.com/problems/squares-of-a-sorted-array/
# TC:O(N)
# SC:O(1)
class Solution(object):
    def sortedSquares(self, A):
        """
            [-4,-1,0,3,10]
              i        j
        """
        N = len(A)
        
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = list()
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans