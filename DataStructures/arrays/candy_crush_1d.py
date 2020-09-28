'''
Write a function to crush candy in a one dimensional board.

In candy crushing games, groups of like items are removed from the
board. In this problem, any sequence of 3 or more like items should be
removed and any items adjacent to that sequence should now be
considered adjacent to each other. This process should be repeated as
many times as possible.


Sample inputs:

ABBBCC -> ACC
ABCCCBB -> A
ABCCCBBAAC -> C

ABBBAAA
CCAAACBBBCC

CC***C***CC
'''
class BCharacter:
    def __init__(self, value=None):
        self.value=value
        self.count=1
    def __str__(self):
        return self.value
    
def process_stack(bChar=None, stack=None):  #C, [A]
    if stack:
        if stack[-1].count >= 3:
            stack.pop()
    # else:
    #     raise Exception('Stack is not initialized')

def check(bChar, stack):  # B, [A]
    if stack:
        return stack[-1].value == bChar.value
    #else:
    #    raise Exception('Stack is not initialized')

def candy_crush(string): # ABBBCC
    """
    # {A: 1}
    """
    if not string:
        raise Exception()
    
    stack=list()  # []
    bChar=BCharacter(string[0])
    stack.append(bChar)   #[A, C]
    
    for i in range(1, len(string)): # 
        bChar=BCharacter(string[i]) # C
        
        if check(bChar, stack):  
            stack[-1].count+=1
        else:
            # maintian the count and then see if the value on top of stack is greater than or equal to 3
            process_stack(bChar, stack)
            if check(bChar, stack):
                stack[-1].count+=1
            else:
                stack.append(bChar)
    process_stack(bChar, stack)
    
    result = list()
    while stack:
        result.append(stack[-1].value * stack[-1].count)
        stack.pop()
    
    result.reverse()
    print (''.join(result))
    
def main():
    print('first example \n')
    candy_crush('ABBBCC')
    print('second example \n')
    candy_crush('ABCCCBB')
    print('third example \n')
    candy_crush('ABCCCBBAAC')

main()

                
