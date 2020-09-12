# https://leetcode.com/discuss/interview-question/398026/
# https://leetcode.com/playground/YfvM9Mfz
def solution(s):
    if not s:
        raise Exception
        
    a_count=0
    b_count=0
    result_count=0
    i=2
    s=list(s)
    while i<len(s):
        
        temp=s[i]
        if temp == s[i-1] and temp == s[i-2]:
            result_count += 1
            
            if ((i+2) < len(s) and temp == s[i+1] and temp == s[i+2]):
                s[i] = 'a' if temp=='b' else 'b'
            else:
                s[i-1] = 'a' if temp=='b' else 'b'
        i+=1
    
    return result_count

print(solution('baaaaa'))
print(solution('baaabbaabbba'))
                
