# https://leetcode.com/discuss/interview-question/451422/
# https://leetcode.com/playground/YSsbyYsL

def fair_index(arrA, arrB):
    
    if len(arrA)!=len(arrB):
        return -1
    
    totalA=sum(arrA)
    totalB=sum(arrB)
    leftA=0
    leftB=0
    count=0
    
    for i in range(len(arrA)-1):
        leftA+=arrA[i]
        leftB+=arrB[i]
        
        if leftA==totalA-leftA == leftB==totalB-leftB:
            count+=1

    return count

print(fair_index([4,-1,0,3],[-2,5,0,3]))
print(fair_index([3,2,6],[4,1,6]))
print(fair_index([1,4,2,-2,5],[7,-2,-2,2,5]))
print(fair_index([2,-2,-3,3],[0,0,4,-4]))
