"""
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"

TC:O(A+B)
SC:O(A+B)

https://leetcode.com/problems/string-without-aaa-or-bbb/

"""
class Solution(object):
    def strWithout3a3b(self, A, B):
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                if ans[-1]=='b':
                    writeA=True
                else:
                    writeA=False
            else:
                if A>=B:
                    writeA=True
                else:
                    writeA=False

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)
