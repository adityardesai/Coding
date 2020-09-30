"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

TC:O(N)
SC:O(N)

Remove the left number to minimize using stack
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        num_stack=list()
        
        for digit in num:
            
            while num_stack and num_stack[-1]>digit and k:
                num_stack.pop()
                k-=1
            
            num_stack.append(digit)
        
        while k:
            num_stack.pop()
            k-=1

        return ''.join(num_stack).lstrip('0') or "0"
