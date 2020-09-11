# https://leetcode.com/problems/different-ways-to-add-parentheses/
# TC:
# SC: 

"""

Given a calculator string find all possible results from it. The output is essentially a result of all possible groupings.

input: 2 * 3 - 4 * 5
output: [-14, -34, -10, -10, 10]
1) (2 * 3) - ( 4 * 5) = -14
2) 2 * (3 - (4 * 5)) = -34
3) (2 * (3 - 4)) *5 = -10
4) 2 * (( 3 - 4) *5) = -10
5) ((2 * 3) - 4) * 5 = 10

"""

class Solution:
    def divide_and_conquer_helper(self, input):
        result=list()
        if input.isdigit():
            return [int(input)]
        for i in range(len(input)):
            if input[i] in ('+', '*', '-', '/'):
                left = self.divide_and_conquer_helper(input[:i])
                right = self.divide_and_conquer_helper(input[i+1:])
                
                for l in left:
                    for r in right:
                        result.append(self.compute(l, input[i], r))
        return result
    def compute(self,a,b,c):
        a=int(a)
        c=int(c)
        if b=='+':
            return a+c
        elif b=='-':
            return a-c
        elif b=='*':
            return a*c
        elif b=='/':
            return a/c
        else:
            print('invalid operator')
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        
        return self.divide_and_conquer_helper(input)
        
