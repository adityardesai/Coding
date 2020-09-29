"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

https://leetcode.com/problems/basic-calculator/
"""

class Solution:
    def operation(self, op, second, first):
        if op == "+":
            return first + second
        elif op == "-":
            return first - second
        elif op == "*":
            return first * second
        elif op == "/":  # integer division
            return first // second
    def precedence(self, curr, stacktop):
        if stacktop == '(' or stacktop == ')':
            return False
        if (curr=='*' or curr=='/') and (stacktop=='+' or stacktop=='-'):
            return False
        return True
    def calculate(self, s: str) -> int:  
        if not s:
            return 0

        num_stack=list()
        ops_stack=list()
        
        i=0
        while i<len(s):
            ch=s[i]
            if ch.isdigit():
                num=ch
                while i<len(s)-1 and s[i+1].isdigit():
                    num+=s[i+1]
                    i+=1
                num_stack.append(int(num))
            elif ch=='(':
                ops_stack.append(ch) 
            elif ch==')':
                while ops_stack[-1] != '(':
                    num_stack.append(self.operation(ops_stack.pop(), 
                                     num_stack.pop(), 
                                     num_stack.pop())) 
                ops_stack.pop()
            elif ch in ('+', '-', '/', '*'):
                while ops_stack and self.precedence(ch, ops_stack[-1]):
                    num_stack.append(self.operation(ops_stack.pop(), 
                                     num_stack.pop(), 
                                     num_stack.pop()))
                ops_stack.append(ch)
            i+=1
        
        print(num_stack)
        while ops_stack:
            num_stack.append(self.operation(ops_stack.pop(),
                                            num_stack.pop(),
                                            num_stack.pop()))

        return num_stack.pop()
        
                
