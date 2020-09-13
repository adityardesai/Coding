# https://leetcode.com/discuss/interview-question/558015/Microsoft-OA
# https://leetcode.com/playground/aQwV7n3H

def plus_or_minus_one(arr):
    m_set=set()
    for i in range(len(arr)):
        actual=arr[i]    
        if actual in m_set:
            return True
        else:
            m_set.add(actual-1)
            m_set.add(actual+1)
    
    return False

"""
A = [7] , return false
A = [4,3], return true (3,4)
A = [11, 1, 8, 12, 14] , return true (11,12)
A = [5, 5, 5, 5, 5], return false
A = [4, 10, 8, 5, 9], return true (4,5), (8,9), (9,10)
"""

print(plus_or_minus_one([7]))
print(plus_or_minus_one([4,3]))
print(plus_or_minus_one([11,1,8,12,14]))
print(plus_or_minus_one([5,5,5,5,5]))
print(plus_or_minus_one([4,10,8,5,9]))        
    
    
