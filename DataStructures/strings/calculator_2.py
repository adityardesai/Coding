"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

TC:O(N)
SC:O(N)

https://leetcode.com/problems/basic-calculator-ii/


"""
class Solution:
    def operation(self,op, second, first):
        if op == "+":
            return first + second
        elif op == "-":
            return first - second
        elif op == "*":
            return first * second
        elif op == "/":
            return first // second

    def precedence(self,current_op, op_from_ops):
        if(current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
            return False
        return True
    
    def calculate(self, s: str) -> int:        
        if not s: return 0
        N = len(s)
        num_stack = list()
        ops_stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = c
                while i < N-1 and s[i + 1].isdigit(): 
                    num += s[i + 1]
                    i += 1
                num_stack.append(int(num))
                                                           
            elif c in ["+", "-", "*", "/"]:
                while ops_stack and self.precedence(c, ops_stack[-1]):
                    num_stack.append(self.operation(ops_stack.pop(), num_stack.pop(), num_stack.pop()))   
                ops_stack.append(c)                                   
            
            i += 1                                                              

        while ops_stack:                                                     
            num_stack.append(self.operation(ops_stack.pop(), num_stack.pop(), num_stack.pop()))            
        
        return num_stack.pop()
