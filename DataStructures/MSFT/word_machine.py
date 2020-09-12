# https://leetcode.com/discuss/interview-question/algorithms/833400/microsoft-ota-word-machine
# https://leetcode.com/playground/f8cEhRPG

def operation(key, stack):    
    if stack:
        a=stack.pop()
        b=stack.pop()
    
        if a.isdigit() and b.isdigit() and key=='+':
            res=int(a) + int(b)
            stack.append(str(res))
        
        if a.isdigit() and b.isdigit() and key=='-':
            res=int(a) - int(b)
            stack.append(str(res))
        return stack
    
def solution(s):
    if not s:
        raise Exception()
    
    stack=list()
    
    inp=s.split(" ") # [5,6,+,-]
    
    for i in range(len(inp)):
        key=inp[i]
        
        if key=="POP":
            if stack:
                stack.pop()
        elif key=="DUP":
            if stack:
                stack.append(stack[-1])
        elif key in ("+", "-"):
            if len(stack)<2:
                return -1
            else:
                stack = operation(key, stack) # [11]
            
        elif key.isdigit():
            stack.append(key) # [5, 6]
        else:
            print('Invalid input')
    
    return stack[-1]

print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))
print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
