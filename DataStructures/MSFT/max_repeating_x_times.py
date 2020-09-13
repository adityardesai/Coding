# https://leetcode.com/discuss/interview-question/525977/Microsoft-or-OA-2020-or-Largest-number-X-which-occurs-X-times
# https://leetcode.com/playground/7uLizhze
# TC:O(N)
# SC:O(N)



def max_repeating(arr):
    
    if not arr:
        raise Exception
    
    hash_map=dict()
    for i in range(len(arr)):
        num=arr[i]
        hash_map[num]=hash_map.get(num,0)+1
    
    result=list()
    
    for k,v in hash_map.items():
        if k==v:
            result.append(k)
    if result:
        return max(result)
    else:
        return 0


print(max_repeating([3,8,2,3,3,2]))
print(max_repeating([7,1,2,8,2]))
print(max_repeating([3,1,4,1,5]))
print(max_repeating([5,5,5,5,5]))            
        
